---
name: resilient-batch-processing
description: Use when processing many files or records in a batch (OCR, parsing, imports, transformations). Ensures one bad item never stops the run — isolate failures per item, log them with identifiers, clean up temp files, and produce a results-plus-errors summary so partial success is the norm, not a crash.
---

# Purpose

Make batch jobs robust. The default failure mode is one malformed file aborting the whole run. This skill isolates each item so failures are contained, logged, and reported, and the rest of the batch completes — the right behavior for OCR, document extraction, bulk imports, and data transforms.

# When to Use

Use when iterating over a folder of files or a list of records where any individual item might fail: OCR/extraction pipelines, CSV/JSON imports, image processing, scraping, or bulk API calls.

# Inputs

- The collection of items to process (files, rows, records).
- The per-item processing function.
- Where outputs and error reports should go.

# Outputs

- Successful results for the items that processed.
- A structured error report (item identifier + reason) for failures.
- A clean workspace (temp files removed) and a run summary (processed / failed counts).

# Procedure

1. **Process each item independently** inside its own try/except. A failure returns `None`/an error record — it never raises out of the loop.
2. **Always include the identifier** (filename, row id) in every log line and error record so failures are traceable.
3. **Catch specific exceptions** where possible; never use a bare `except`. Log with context: `[ERROR] <item>: <reason>`.
4. **Generate unique temp names** (e.g. UUIDs) to avoid collisions when items are processed in parallel or quick succession.
5. **Clean up immediately.** Delete uploaded/temp files right after processing so nothing lingers on disk — important for sensitive inputs.
6. **Ensure directories exist** (`makedirs(..., exist_ok=True)`) before writing outputs.
7. **Summarize the run:** counts of processed vs. failed, and the path to the error report.
8. **Make it idempotent** where feasible so a re-run can safely retry only the failures.

# Quality Checklist

- [ ] Each item processed in isolation; one failure can't stop the batch
- [ ] Every log/error includes the item identifier
- [ ] Specific exceptions caught; no bare `except`
- [ ] Unique temp filenames prevent collisions
- [ ] Temp/uploaded files cleaned up after processing
- [ ] Output directories created if missing
- [ ] Run ends with a processed/failed summary

# Edge Cases

- **Corrupt or unreadable item:** record the error, skip, continue.
- **Partial output:** don't leave half-written files; write to a temp name and rename on success.
- **Very large batch:** stream/iterate rather than loading everything into memory; consider chunking.
- **Sensitive inputs:** delete temp files even on failure (use a finally block).

# Safety Rules

- Never let one item's exception abort the whole batch.
- Never leave uploaded/temp files on disk after processing, especially sensitive ones.
- Never log full sensitive content — log identifiers and reasons.
- Always clean up in a `finally` so cleanup runs even on error.

# Examples

**Good:** A folder of 500 documents: each is processed in its own try/except, failures are written to `errors.csv` with filename and reason, temp files are deleted in a `finally`, and the run prints "Processed 487, failed 13 — see errors.csv".

**Bad:** A loop that calls `extract(file).group(0)` directly, so the first file with no match throws and the remaining 499 never run.
