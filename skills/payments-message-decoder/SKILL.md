---
name: payments-message-decoder
description: Use when a task involves reading, explaining, mapping, validating or generating ISO 20022 payment messages (pain.001 / pain.002 / pacs.008 / pacs.002 / pacs.004 / camt.053 / camt.054) or legacy SWIFT MT (MT101 / MT103 / MT940) — including "what does this field mean", "why was this rejected", "map MT103 to pacs.008", or building parsers, validators and test fixtures. Explains messages element by element, applies structural and business rules, and produces public-safe synthetic examples.
---

# Purpose

Payments messages are dense XML/text that hide simple business meaning:
who pays whom, how much, when, through which agents, and what went wrong.
This skill turns an agent into a reliable decoder and validator of those
messages so builders can ship payment features, debug rejections and write
tests without a specialist on call.

# When to Use

- Explaining a pain.001, pacs.008, camt.053 or MT103 to a non-specialist.
- Mapping between MT and MX (e.g. MT103 → pacs.008, MT940 → camt.053).
- Diagnosing a rejection or return (pain.002 / pacs.002 / pacs.004 reason
  codes) and saying what the sender must change.
- Building or reviewing a parser, validator, schema mapping or fixture set.
- Generating realistic **synthetic** test messages.

Not for: legal or regulatory advice on a live case, sanctions decisions,
or anything requiring data from a real customer message (see Safety).

# Inputs

- The message (or fragment), or the field/element name in question.
- Direction and role: debtor bank / creditor bank / intermediary, initiating
  party / instructing agent.
- Scheme context if known: cross-border correspondent (CBPR+), a domestic
  instant scheme, SEPA, a regional RTGS.
- For mapping: source and target message types and version (e.g.
  `pain.001.001.09`).

# Outputs

- A plain-language decode: one line per element that matters, grouped as
  **Parties · Amount & dates · Agents & routing · Purpose & remittance ·
  Charges · Identifiers · Status/reason**.
- A validation report: structural (schema/cardinality), referential
  (IDs match, agents resolve), business (dates, currency/amount, charge
  bearer, purpose codes), with severity.
- Mapping tables `source element → target element → rule/transform`.
- Synthetic fixtures (valid + one per failure mode) with obviously fake
  identifiers.

# Core map (memorise this)

| Business question | pain.001 (customer → bank) | pacs.008 (bank → bank) | MT103 |
|---|---|---|---|
| Who is paying | `Dbtr`, `DbtrAcct` | `Dbtr`, `DbtrAcct` | :50a |
| Payer's bank | `DbtrAgt` | `DbtrAgt` | :52a |
| Who is paid | `Cdtr`, `CdtrAcct` | `Cdtr`, `CdtrAcct` | :59a |
| Payee's bank | `CdtrAgt` | `CdtrAgt` | :57a |
| How much | `Amt/InstdAmt` | `IntrBkSttlmAmt` (+ `InstdAmt`) | :32A (+ :33B) |
| When | `ReqdExctnDt` | `IntrBkSttlmDt` | :32A date |
| Who pays fees | `ChrgBr` (DEBT/CRED/SHAR/SLEV) | `ChrgBr` | :71A (OUR/BEN/SHA) |
| Why | `Purp/Cd`, `RmtInf` | `Purp/Cd`, `RmtInf` | :70, :26T |
| Trace it | `MsgId`, `PmtInfId`, `EndToEndId`, `InstrId` | `MsgId`, `EndToEndId`, `TxId`, `UETR` | :20, :121 (UETR) |
| Status / reason | pain.002 `TxSts` + `StsRsnInf/Rsn/Cd` | pacs.002 same; pacs.004 `RtrRsnInf` | MT199/MT103 RETN, :72 |

Key status codes: `ACTC` accepted technical · `ACSP` accepted settlement in
process · `ACSC` settled · `RJCT` rejected · `PDNG` pending. Common reason
codes: `AC01` incorrect account · `AC04` closed account · `AC06` blocked ·
`AM04` insufficient funds · `AG01` transaction forbidden · `BE05` unknown
creditor · `RR04` regulatory reason · `FF01` invalid file format · `CUST`
requested by customer · `DUPL` duplicate · `MS03` reason not specified.

`EndToEndId` is the customer's reference and must survive the whole chain
unchanged; `UETR` (a UUID) is the network-level trace for gpi/CBPR+.

# Procedure

1. **Identify** the message type and version from the namespace
   (`urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08`) or MT block 2.
   Say which leg of the chain it is.
2. **Decode** with the seven groups above. Translate every code to words
   (`SHAR` → "fees shared: payer pays its bank, payee pays theirs").
3. **Validate** in three passes:
   - Structural: mandatory elements present, cardinality, formats (BIC
     8/11, IBAN checksum, ISO 4217 currency, dates ISO 8601, amount ≤
     18 digits with ≤ 5 decimals and currency-appropriate minor units).
   - Referential: `NbOfTxs` equals actual count; `CtrlSum` equals sum of
     amounts; agent BICs resolve; `EndToEndId` unique per batch.
   - Business: execution date not in the past (unless scheme allows),
     charge bearer allowed by scheme, purpose code from the external code
     list, structured address where the scheme mandates it, remittance
     ≤ 140 chars unstructured.
4. **Diagnose** a status/return: quote the reason code, give its meaning,
   name the element that caused it, state the fix and who applies it.
5. **Map** (if asked): produce the table; flag lossy mappings (MT free-text
   party lines → structured `PstlAdr`; :71F charges → `ChrgsInf`) and
   scheme-specific truncation.
6. **Fixture**: when producing examples, use fake BICs of the form
   `AAAABBCCXXX` with test country codes, IBANs that pass the checksum but
   belong to test ranges, names like "Example Trading Pte Ltd", and
   round amounts. Label every fixture SYNTHETIC.

# Quality Checklist

- [ ] Message type + version + chain leg stated up front.
- [ ] Every code expanded to plain words; no bare `SHAR`, `RJCT`, `AC01`.
- [ ] Validation findings carry severity (blocks / warns / note) and the
      exact XPath or MT tag.
- [ ] Mapping tables flag every lossy or scheme-dependent transform.
- [ ] Fixtures are synthetic and labelled; `CtrlSum` and `NbOfTxs` agree.
- [ ] Any statement about a scheme rule carries its version/date and a
      "check the current rulebook" note.

# Edge Cases

- Mixed versions (pain.001.001.03 vs .09): call out renamed/added elements
  (structured address, LEI, `UETR` in `PmtId`) before mapping.
- Instant schemes: timeout-driven statuses; a "pending" older than the
  scheme SLA is effectively a failure — say so.
- Cover payments (MT202COV / pacs.009 COV): two messages describe one
  payment; decode both and reconcile the underlying customer details.
- Character set: MX permits UTF-8 where CBPR+ restricts to the FIN
  X-character set — flag characters that will be mangled.

# Safety Rules

- Never paste, store or echo real customer data (names, account numbers,
  IBANs, addresses, amounts tied to a real transaction). Redact before
  analysis; work from synthetic fixtures.
- Do not make sanctions, AML or regulatory determinations; identify the
  reason code and route to the responsible function.
- Do not assert a scheme rule as current without a date; rulebooks change
  annually (CBPR+ usage guidelines, SEPA rulebooks, domestic schemes).
- Keep employer- or client-specific routing tables, BIC lists and internal
  reason-code extensions out of any shared skill or repo.

# Examples

**Ask:** "Our pacs.008 came back RJCT with AC01. What do we change?"
**Answer shape:** "AC01 = incorrect account number. The creditor account
in `CdtTrfTxInf/CdtrAcct/Id/IBAN` failed the receiving bank's check. The
IBAN passes checksum, so the account is valid-looking but not at that
agent — confirm `CdtrAgt/FinInstnId/BICFI` matches the IBAN's bank code.
The originator (initiating party) corrects and resubmits with a new
`EndToEndId`; do not reuse the rejected one."

**Ask:** "Map this MT103 to pacs.008."
**Answer shape:** table of 14 rows; two flagged lossy (`:50K` free-text
address → structured `PstlAdr` needs parsing; `:71F` → `ChrgsInf` requires
agent per charge).
