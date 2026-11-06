#!/usr/bin/env python3
"""Render a source-attributed, offline newspaper. Python 3.9+, standard library only."""
import argparse
import datetime as dt
import html
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, parse_qsl

ID = re.compile(r'^[A-Za-z][A-Za-z0-9_-]{0,63}$')
THEME_KEYS = {'navy', 'blue', 'green', 'mint', 'ink', 'muted', 'line', 'paper', 'canvas', 'focus'}
TYPES = {'html', 'excel', 'email', 'teams', 'transcript', 'public', 'document', 'csv'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text_field(obj, key, empty=False):
    val = obj.get(key)
    require(isinstance(val, str) and (empty or bool(val.strip())), f'{key}: expected a nonempty string')
    return val


def timestamp(value, label):
    require(isinstance(value, str), f'{label}: expected an ISO timestamp')
    try:
        date = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError(f'{label}: invalid ISO timestamp') from exc
    require(date.tzinfo is not None and date.utcoffset() is not None, f'{label}: timezone required')
    return date


def safe_url(value):
    require(isinstance(value, str), 'url: expected a string')
    require(not any(ord(c) < 33 or ord(c) == 127 for c in value), 'url: control characters or spaces are forbidden')
    try:
        parsed = urlsplit(value)
        require(parsed.scheme.lower() in {'https', 'http'} and bool(parsed.hostname), 'url: expected an absolute HTTP(S) URL')
        require(not parsed.username and not parsed.password, 'url: embedded credentials are forbidden')
        _ = parsed.port
    except ValueError as exc:
        raise ValueError(f'url: invalid or unsafe link ({exc})') from exc
    require('\\' not in value, 'url: backslashes are forbidden')
    secret_keys = {'token', 'access_token', 'refresh_token', 'id_token', 'api_key', 'apikey', 'password', 'secret', 'client_secret', 'authorization', 'sig', 'signature'}
    params = parse_qsl(parsed.query, keep_blank_values=True) + parse_qsl(parsed.fragment, keep_blank_values=True)
    require(not any(key.lower() in secret_keys for key, _ in params), 'url: apparent credential or signed-link parameter; use a verified non-secret canonical URL')
    return value


def nonempty_list(obj, key):
    val = obj.get(key)
    require(isinstance(val, list) and len(val) > 0, f'{key}: expected a nonempty list')
    return val


def validate(data):
    require(isinstance(data, dict), 'edition must be a JSON object')
    for key in ('title', 'strapline', 'edition', 'date', 'as_of', 'audience', 'intro'):
        text_field(data, key)
    require(type(data.get('sample')) is bool, 'sample: expected true or false')
    try:
        require(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', data['date'])), 'date: use YYYY-MM-DD')
        dt.date.fromisoformat(data['date'])
    except ValueError as exc:
        raise ValueError('date: invalid YYYY-MM-DD') from exc
    timestamp(data['as_of'], 'as_of')
    theme = data.get('theme', {})
    require(isinstance(theme, dict), 'theme: expected an object')
    for key, value in theme.items():
        require(key in THEME_KEYS and isinstance(value, str) and re.fullmatch(r'#[0-9a-fA-F]{6}', value), 'theme: use supported token names and #RRGGBB colors only')
    sources = nonempty_list(data, 'sources')
    seen = set()
    for source in sources:
        require(isinstance(source, dict), 'each source must be an object')
        sid = text_field(source, 'id')
        require(ID.fullmatch(sid) and sid not in seen, f'invalid or duplicate source ID: {sid}')
        seen.add(sid)
        require(source.get('type') in TYPES, f'{sid}: unsupported source type')
        for key in ('title', 'locator', 'access', 'note'):
            text_field(source, key)
        require(source['access'] in {'public', 'internal', 'demo'}, f'{sid}: invalid access class')
        require(data['sample'] or source['access'] != 'demo', f'{sid}: demo sources require sample=true')
        require('published_at' in source, f'{sid}: published_at required (null if unknown)')
        if source['published_at'] is not None:
            timestamp(source['published_at'], f'{sid}.published_at')
        timestamp(source.get('retrieved_at'), f'{sid}.retrieved_at')
        if source.get('url'):
            safe_url(source['url'])
        if 'excerpt' in source:
            text_field(source, 'excerpt', empty=True)
    def refs(obj):
        ids = nonempty_list(obj, 'source_ids')
        require(all(isinstance(i, str) and i in seen for i in ids), 'unknown or invalid source reference')
        require(len(ids) == len(set(ids)), 'duplicate source reference')
    articles = nonempty_list(data, 'articles')
    article_ids = set()
    for article in articles:
        require(isinstance(article, dict), 'each article must be an object')
        aid = text_field(article, 'id')
        require(ID.fullmatch(aid) and aid not in article_ids, f'invalid or duplicate article ID: {aid}')
        article_ids.add(aid)
        for key in ('section', 'title', 'dek', 'label'):
            text_field(article, key)
        for paragraph in nonempty_list(article, 'paragraphs'):
            require(isinstance(paragraph, dict), 'each paragraph must be an object')
            text_field(paragraph, 'text')
            refs(paragraph)
    for key in ('metrics', 'actions', 'limitations'):
        require(isinstance(data.get(key, []), list), f'{key}: expected a list')
    for metric in data.get('metrics', []):
        require(isinstance(metric, dict), 'each metric must be an object')
        for key in ('label', 'method'):
            text_field(metric, key)
        text_field(metric, 'unit', empty=True)
        value = metric.get('value')
        require(type(value) in (float, int) and math.isfinite(value), 'metric value must be a finite number')
        dec = metric.get('display_decimals', 0)
        require(type(dec) is int and 0 <= dec <= 3, 'display_decimals must be 0–3')
        refs(metric)
    portfolio = data.get('portfolio')
    if portfolio is not None:
        require(isinstance(portfolio, dict), 'portfolio must be an object')
        text_field(portfolio, 'title'); text_field(portfolio, 'caption'); refs(portfolio)
        for row in nonempty_list(portfolio, 'rows'):
            require(isinstance(row, dict), 'portfolio rows must be objects')
            text_field(row, 'label')
            complete, total = row.get('complete'), row.get('total')
            require(type(complete) is int and type(total) is int and 0 <= complete <= total and total > 0, 'invalid portfolio counts')
    for action in data.get('actions', []):
        require(isinstance(action, dict), 'each action must be an object')
        for key in ('text', 'owner', 'due'):
            text_field(action, key)
        refs(action)
    require(all(isinstance(x, str) and x.strip() for x in data.get('limitations', [])), 'limitations must contain nonempty strings')
    return data


def esc(value):
    return html.escape(str(value), quote=True)


def render(data, template=None):
    validate(data)
    source_by_id = {s['id']: s for s in data['sources']}
    def refs(ids):
        return ''.join(f'<a class="cite" href="#source-{esc(sid)}" aria-label="Source {esc(sid)}: {esc(source_by_id[sid]["title"])}">[{esc(sid)}]</a>' for sid in ids)
    def article(a, lead=False):
        body = ''.join(f'<p>{esc(p["text"])} {refs(p["source_ids"])}</p>' for p in a['paragraphs'])
        label = 'Illustrative story' if data['sample'] else a['label']
        return f'<article class="article{" lead" if lead else ""}" id="story-{esc(a["id"])}" data-section="{esc(a["section"])}"><p class="eyebrow">{esc(a["section"])}<span class="article-label">{esc(label)}</span></p><h2>{esc(a["title"])}</h2><p class="dek">{esc(a["dek"])}</p><div class="body-columns">{body}</div></article>'
    sections = list(dict.fromkeys(a['section'] for a in data['articles']))
    filters = '<button class="filter" type="button" data-filter-all="true" aria-pressed="true">Front page</button>'
    filters += ''.join(f'<button class="filter" type="button" data-section="{esc(s)}" aria-pressed="false">{esc(s)}</button>' for s in sections)
    briefs = ''.join(f'<div class="brief-item"><span class="brief-number" aria-hidden="true">{i:02}</span><div><a href="#story-{esc(a["id"])}">{esc(a["title"])}</a><p>{esc(a["section"])} · {"Illustrative" if data["sample"] else esc(a["label"])}</p></div></div>' for i, a in enumerate(data['articles'][1:4], 1))
    metrics = ''
    if data.get('metrics'):
        items = []
        for m in data['metrics']:
            value = f'{m["value"]:,.{m.get("display_decimals", 0)}f}'
            items.append(f'<div class="metric"><p class="metric-label">{esc(m["label"])}</p><div class="metric-value">{value}<span>{esc(m["unit"])}</span></div><p class="metric-method">{esc(m["method"])} {refs(m["source_ids"])}</p></div>')
        metrics = f'<section class="metrics" aria-label="Key figures{" — synthetic demonstration" if data["sample"] else ""}">{"".join(items)}</section>'
    portfolio = ''
    if data.get('portfolio'):
        p = data['portfolio']; rows = p['rows']
        complete, total = sum(r['complete'] for r in rows), sum(r['total'] for r in rows)
        bars = ''.join(f'<div class="bar-row"><span>{esc(r["label"])}</span><div class="bar-track" aria-hidden="true"><div class="bar-fill" style="width:{100*r["complete"]/r["total"]:.2f}%"></div></div><span class="bar-value">{r["complete"]}/{r["total"]}</span></div>' for r in rows)
        portfolio = f'<section class="portfolio" aria-labelledby="portfolio-title"><h2 class="section-label">The data view{" · synthetic" if data["sample"] else ""}</h2><h3 id="portfolio-title">{esc(p["title"])}</h3><p class="caption">{esc(p["caption"])} {refs(p["source_ids"])}</p>{bars}<div class="plot-total"><strong>{100*complete/total:.0f}%</strong><span>{complete} of {total} checks complete. Calculated from the rows above.</span></div></section>'
    actions = ''
    if data.get('actions'):
        rows = ''.join(f'<div class="action-row"><strong>{esc(a["text"])}</strong><div class="action-meta"><b>{esc(a["owner"])}</b> · {esc(a["due"])} {refs(a["source_ids"])}</div></div>' for a in data['actions'])
        actions = f'<section class="actions" aria-labelledby="actions-title"><h2 class="section-label">What happens next{" · illustrative" if data["sample"] else ""}</h2><h3 id="actions-title">The next decision, made clear.</h3>{rows}</section>'
    source_entries = []
    for s in data['sources']:
        url = f'<a href="{esc(s["url"])}" target="_blank" rel="noopener noreferrer">Open original source ↗</a>' if s.get('url') else 'No external link. See the precise source locator.'
        published = s['published_at'] if s['published_at'] is not None else 'Unknown; see source note.'
        excerpt = f'<blockquote>{esc(s["excerpt"])}</blockquote>' if s.get('excerpt') else ''
        source_entries.append(f'<details class="source-entry" id="source-{esc(s["id"])}" data-title="{esc(s["id"])} · {esc(s["title"])}"><summary><span>{esc(s["id"])} / {esc(s["type"].upper())}</span>{esc(s["title"])}</summary><div class="source-body"><dl><dt>Access</dt><dd>{esc(s["access"])}</dd><dt>Locator</dt><dd>{esc(s["locator"])}</dd><dt>Published</dt><dd>{esc(published)}</dd><dt>Retrieved</dt><dd>{esc(s["retrieved_at"])}</dd><dt>Original</dt><dd>{url}</dd></dl>{excerpt}<p class="source-note">{esc(s["note"])}</p></div></details>')
    limitations = ''
    if data.get('limitations'):
        limitations = '<section class="limitations" aria-labelledby="limitations-title"><h3 id="limitations-title">Editorial notes & limitations</h3><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in data['limitations']) + '</ul></section>'
    words = sum(len(p['text'].split()) for a in data['articles'] for p in a['paragraphs'])
    as_of = timestamp(data['as_of'], 'as_of').astimezone(dt.timezone.utc).strftime('%d %b %Y, %H:%M UTC')
    sample = data['sample']
    tokens = {
        'THEME_OVERRIDES': ':root{' + ''.join(f'--{key}:{value};' for key, value in data.get('theme', {}).items()) + '}',
        'TITLE': esc(data['title']), 'DESCRIPTION': esc(data['strapline']), 'STRAPLINE': esc(data['strapline']),
        'AUDIENCE': esc(data['audience']), 'DATE': esc(dt.date.fromisoformat(data['date']).strftime('%A, %d %B %Y')),
        'EDITION': esc(data['edition']), 'AS_OF': as_of, 'READ_TIME': str(max(1, math.ceil(words/180))),
        'BANNER': 'Synthetic demonstration · not live reporting' if sample else 'Source-backed briefing · prepared edition',
        'EDITION_KIND': 'Design preview' if sample else 'Prepared edition',
        'FILTERS': filters, 'INTRO': esc(data['intro']), 'LEAD': article(data['articles'][0], True),
        'BRIEFS': briefs, 'STORIES': ''.join(article(a) for a in data['articles'][1:]),
        'METRICS': metrics, 'PORTFOLIO': portfolio, 'ACTIONS': actions, 'SOURCES': ''.join(source_entries),
        'LIMITATIONS': limitations,
        'RAIL_NOTE': f'Every story, number and role in this edition is fictional. The {len(data["sources"])} listed demo sources show how evidence can travel from a document to a headline.' if sample else 'Open the numbered references to inspect the evidence behind each story. Read the editorial notes for coverage limits and unresolved questions.',
        'SOURCE_CONTEXT': 'These are bundled fictional fixtures, not messages or reports from a real organisation.' if sample else 'Source links retain their original access restrictions. This file does not grant access to the originals.',
        'DISCLAIMER': 'All reporting content is synthetic. This is a configurable independent editorial template, not an official publication or an approved brand asset.' if sample else 'Prepared from the cited sources for the audience shown above. This is an independent editorial template, not an official publication or an approved brand asset.',
    }
    template = template or (Path(__file__).resolve().parent.parent / 'assets' / 'newspaper-template.html').read_text(encoding='utf-8')
    return re.sub(r'\{\{([A-Z_]+)\}\}', lambda match: tokens[match.group(1)], template)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        raw = args.input.read_text(encoding='utf-8')
        data = json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(f'Invalid JSON number: {x}')))
        output = render(data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding='utf-8')
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f'Cannot render edition: {exc}', file=sys.stderr)
        return 1
    print(f'Created {args.output} ({len(output.encode("utf-8")):,} bytes). Sources and factual accuracy still require editorial review.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
