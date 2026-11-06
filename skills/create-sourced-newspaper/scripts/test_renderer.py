#!/usr/bin/env python3
"""Behavioral tests for validation, escaping, attribution and computed output."""
import copy
import json
from pathlib import Path
import unittest
from render_newspaper import render, validate

ROOT = Path(__file__).resolve().parent.parent

class RendererTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'assets/example-edition.json').read_text())
    def test_sample_renders_full_attributed_content(self):
        result = render(self.data)
        self.assertIn('Synthetic demonstration', result)
        self.assertIn('84 of 100 checks complete', result)
        for a in self.data['articles']:
            self.assertIn('id="story-' + a['id'] + '"', result)
        for s in self.data['sources']:
            self.assertIn('id="source-' + s['id'] + '"', result)
        self.assertNotIn('{{TITLE}}', result)
    def test_changed_counts_recalculate_aggregate(self):
        self.data['portfolio']['rows'][0]['complete'] += 1
        self.assertIn('85 of 100 checks complete', render(self.data))
    def test_text_is_not_executable_markup(self):
        self.data['articles'][0]['paragraphs'][0]['text'] = '<script>alert("x")</script><img src=x onerror=alert(1)>'
        result = render(self.data)
        self.assertIn('&lt;script&gt;', result)
        self.assertNotIn('<img src=x', result)
        self.assertNotIn('<script>alert(', result)
    def test_rejects_unsafe_url_schemes_and_credentials(self):
        for url in ['javascript:alert(1)', 'data:text/html,x', 'file:///etc/passwd', 'https://user:secret@example.com', '//example.com', 'https://example.com\n/x', 'https://example.com\\evil', 'https://example.com/?access_token=SECRET', 'https://example.com/#token=SECRET']:
            with self.subTest(url=url):
                self.data['sources'][0]['url'] = url
                with self.assertRaises(ValueError):
                    validate(self.data)
    def test_rejects_missing_and_duplicate_sources(self):
        self.data['articles'][0]['paragraphs'][0]['source_ids'] = ['MISSING']
        with self.assertRaises(ValueError): validate(self.data)
        self.setUp()
        self.data['sources'].append(copy.deepcopy(self.data['sources'][0]))
        with self.assertRaises(ValueError): validate(self.data)
    def test_rejects_impossible_counts(self):
        self.data['portfolio']['rows'][0]['complete'] = 21
        with self.assertRaises(ValueError): validate(self.data)
    def test_rejects_demo_disguised_as_real(self):
        self.data['sample'] = False
        with self.assertRaises(ValueError): validate(self.data)
    def test_rejects_nonfinite_and_boolean_metrics(self):
        for value in [float('nan'), float('inf'), True]:
            self.data['metrics'][0]['value'] = value
            with self.assertRaises(ValueError): validate(self.data)
    def test_rejects_timezone_free_timestamp(self):
        self.data['as_of'] = '2026-11-06T09:45:00'
        with self.assertRaises(ValueError): validate(self.data)
    def test_unknown_publication_date_is_explicit(self):
        self.data['sources'][0]['published_at'] = None
        self.assertIn('Unknown; see source note.', render(self.data))
    def test_source_link_uses_safe_attributes(self):
        self.data['sources'][0]['url'] = 'https://example.com/report?a=1&b=2'
        result = render(self.data)
        self.assertIn('rel="noopener noreferrer"', result)
        self.assertIn('report?a=1&amp;b=2', result)
    def test_all_section_has_no_sentinel_collision(self):
        self.data['articles'][0]['section'] = 'all'
        result = render(self.data)
        self.assertIn('data-filter-all="true"', result)
        self.assertIn('data-section="all"', result)
        self.assertIn('active===null', result)
    def test_demo_source_count_is_dynamic(self):
        self.data['sources'].append(dict(self.data['sources'][0], id='S6'))
        self.assertIn('The 6 listed demo sources', render(self.data))
    def test_theme_is_configurable_and_css_safe(self):
        self.data['theme'] = {'blue': '#123456'}
        self.assertIn('--blue:#123456;', render(self.data))
        for theme in [{'blue': 'red; background:url(x)'}, {'arbitrary': '#123456'}]:
            self.data['theme'] = theme
            with self.assertRaises(ValueError): validate(self.data)
    def test_duplicate_article_rejected(self):
        self.data['articles'].append(copy.deepcopy(self.data['articles'][0]))
        with self.assertRaises(ValueError): validate(self.data)

if __name__ == '__main__': unittest.main(verbosity=2)
