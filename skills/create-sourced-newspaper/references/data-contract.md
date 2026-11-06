# Edition JSON contract

Use `assets/example-edition.json` as a working example. UTF-8, plain text, no HTML markup. The renderer escapes strings; it does not evaluate formulas or fetch links. Unknown keys are ignored, not rendered.

## Top level

- `title`, `strapline`, `edition`, `date`, `as_of`, `audience`: nonempty strings. `date` is ISO YYYY-MM-DD; `as_of` is an ISO timestamp with timezone. It is a reporting cutoff, not a current clock.
- `sample`: Boolean. True adds visible synthetic labels. False means the agent replaced and checked all demonstration material.
- `intro`: short editorial context, not uncited factual reporting.
- `sources`: nonempty source list.
- `articles`: nonempty story list. First story is the lead. Prefer 4–8 stories but do not pad weak evidence.
- `metrics`: optional list, normally 2–4.
- `portfolio`: optional object: `title`, `caption`, `rows`, `source_ids`. Each row: `label`, integer `complete`, integer `total`, with 0 <= complete <= total and positive total. Aggregate percentage is calculated from rows; do not add a manually typed duplicate.
- `actions`: optional list: `text`, `owner`, `due`, `source_ids`. `due` is human-readable with timezone for timed actions. Label recommendations explicitly; do not manufacture commitments.
- `limitations`: optional list of nonempty strings, visibly displayed.

## Sources

- `id`: unique letter/number/hyphen/underscore ID starting with a letter, e.g. S1.
- `type`: html, excel, email, teams, transcript, public, document or csv.
- `title`, `locator`, `retrieved_at`, `access`, `note`: nonempty strings. `published_at` and `retrieved_at` are ISO timestamps with timezone. For an unknown publication time, set `published_at` to null and explain in `note`; never silently substitute retrieval time.
- `access`: public, internal or demo.
- `url`: optional verified absolute HTTPS/HTTP URL. Internal links may reveal private metadata; include only for an appropriate audience. No URL credentials, secret/tracking tokens, javascript:, data:, file paths or invented deep links. Omit when unavailable and supply a useful locator.
- `excerpt`: optional short exact audience-safe excerpt. The ledger is not an access-control boundary. Omit private raw text when attribution is sufficient.

## Stories

`id`: unique safe ID. `section`, `title`, `dek`, `label`: nonempty strings. Labels describe epistemic/editorial status: Reported update, Decision, Analysis, Open question or Illustrative story.

`paragraphs`: nonempty list of objects with `text` and nonempty `source_ids`. Every ID must exist. Headline/deck must be supported by the cited body; the script cannot verify this. Citation links follow each paragraph. There are no invented reporter bylines.

## Metrics

`label`, `value`, `unit`, `method`, `source_ids`. `value` is a finite number. `unit` may be empty. `display_decimals`: integer 0–3 (default 0). `method` explains cells, population, period and calculation; the script does not prove a manually specified metric.

Numeric labels and source notes make charts understandable without colour. Avoid numerically false precision and unsupported directional arrows.

## Controls and limits

All content is present without JavaScript. Search/filters affect stories only; portfolio/actions/ledger remain visible. Citations open a source dialog but work as anchors without JS. Motion honors the OS preference by default. Print restores all stories and hides controls.

URLs are checked for scheme, host, embedded credentials, control characters and common secret-bearing query/fragment keys. This conservative check does not detect every possible secret; editorial review must still inspect links. New-tab links use noopener noreferrer. Demo sources are rejected when `sample` is false, but plausible invented prose cannot be detected. Editorial review remains required.

## Configurable palette

Optional `theme` object maps supported token names to six-digit hex colors: `navy`, `blue`, `green`, `mint`, `ink`, `muted`, `line`, `paper`, `canvas`, `focus`. For example, `{"blue":"#006EAA","green":"#007C42"}` changes the two accents. Unknown token names, raw CSS and non-hex values are rejected. The default palette remains when the object is omitted. The renderer does not certify contrast; check at least 4.5:1 for ordinary text and 3:1 for large text and meaningful control boundaries, including tinted surfaces, after any change.
