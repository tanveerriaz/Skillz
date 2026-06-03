---
name: supabase-data-design
description: Use when designing a database schema on Postgres / Supabase-style platforms, or choosing between a real table and JSON storage. Covers consistent table/column naming, row-level security by default, sensible relationships and indexes, and when a JSON document store beats normalized tables — so the data layer is safe and scales.
---

# Purpose

Design data layers that are secure, consistent, and appropriately structured. Two recurring mistakes: shipping tables with no row-level security, and reaching for JSON blobs (or rigid tables) at the wrong time. This skill gives naming, security, and structure defaults for Postgres/Supabase-style stacks, plus guidance on tables vs. JSON.

# When to Use

Use when creating a new schema or table, adding row-level security, deciding between normalized tables and JSON storage, or reviewing a data model for safety and scalability.

# Inputs

- The entities and relationships to model.
- Access rules (who can read/write what).
- Query patterns and expected scale.

# Outputs

- A schema with consistent naming and sensible relationships.
- Row-level security policies enabled by default.
- Indexes aligned to query patterns.
- A clear tables-vs-JSON decision per dataset.

# Procedure

1. **Name consistently.** Pick one convention (e.g. snake_case, plural table names, `id` primary keys, `created_at`/`updated_at` timestamps) and apply it everywhere.
2. **Enable row-level security by default.** On any table holding user or tenant data, turn RLS on and write explicit policies; an exposed table without RLS is a data leak.
3. **Model relationships properly.** Use foreign keys and appropriate cardinality; normalize what's queried and filtered relationally.
4. **Choose tables vs. JSON deliberately:**
   - Use **tables/columns** when you filter, join, aggregate, or enforce constraints on the fields.
   - Use **JSON/document storage** for flexible, mostly-read-as-a-whole, schema-variable payloads (e.g. raw API responses, per-record metadata) you don't query field-by-field.
   - Avoid JSON as a dumping ground for data you'll later need to filter on.
5. **Index for access patterns.** Add indexes on columns used in filters/joins; don't over-index writes-heavy tables.
6. **Protect the service role.** The service-role/admin key bypasses RLS — backend only, never exposed to the client (see secure-env-setup).
7. **Plan migrations.** Keep schema changes as versioned migration scripts, not ad-hoc edits.

# Quality Checklist

- [ ] One naming convention applied consistently
- [ ] RLS enabled with explicit policies on all user/tenant tables
- [ ] Foreign keys and cardinality correct
- [ ] Tables vs. JSON chosen per query pattern, not by habit
- [ ] Indexes match real filter/join patterns
- [ ] Service-role key never exposed client-side
- [ ] Schema changes captured as migrations

# Edge Cases

- **Rapidly changing shape early on:** a JSON column can buy flexibility; migrate hot fields into columns once query patterns stabilize.
- **Multi-tenant:** RLS policies must scope every query by tenant; test that one tenant can't read another's rows.
- **High write volume:** minimize indexes and triggers on the hot path.
- **Public read data:** still use RLS with an explicit "allow read" policy rather than leaving the table open.

# Safety Rules

- Never expose a table with sensitive data without RLS enabled.
- Never ship the service-role/admin key to the frontend.
- Never store data you'll need to filter on as opaque JSON.
- Never put real personal data in committed seed/migration files — use placeholders.

# Examples

**Good:** `profiles` table (snake_case, `id`, `created_at`) with RLS so users read/update only their own row; a `raw_payload jsonb` column stores the unparsed provider response, while queryable fields (`amount`, `status`) are real columns with indexes.

**Bad:** A `users` table with RLS off and the service-role key shipped to the browser, storing everything in one `data jsonb` blob that later needs to be filtered by status.
