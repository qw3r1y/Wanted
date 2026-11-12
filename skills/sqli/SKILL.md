---
name: sqli
description: >
  Use when testing an authorized web target for SQL injection — any parameter,
  header, or body field that reaches a database query. Covers injection-point
  discovery, context/DBMS fingerprinting, boolean/time/error/union/out-of-band
  confirmation, impact assessment and remediation. Do NOT use for NoSQL (see
  offensive/web/nosql-injection) or ORM-only logic bugs.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, sqlmap, oob-listener]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
  - references/injection-points-and-dbms.md
license: MIT
version: 1.0.0
---

# SQL Injection (authorized testing)

Find input that alters the **structure** of a backend SQL query, prove it with a
reliable oracle, and establish real impact (data access, authn bypass, or
beyond) — without destructive operations. A single quote in a response is a
*signal*; a differential oracle is the proof.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Keep probes
> bounded and **never run destructive SQL** (`DROP`, `DELETE`, `UPDATE`,
> stacked writes) without explicit per-command approval (`safe-execution-rules.md`).

## When to use
Any field reaching a query: URL/body parameters, JSON fields, HTTP headers
(`X-Forwarded-For`, `User-Agent`, `Referer` when logged to DB), cookies, search,
filters, sort/order columns, pagination. **High-value surfaces:** authentication
queries (login bypass), search/report endpoints (bulk read), admin filters, and
any legacy endpoint not using parameterized queries/ORM.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`); read-only posture by default.
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.
- An OOB listener for out-of-band confirmation (blind/stacked, DNS/HTTP).

## Procedure (gated phases)

### Phase 1 — Injection-point discovery
Map every parameter and its reflection into app behaviour. Probe with
syntax-breaking then syntax-balancing input and watch for a **differential**
(error, content change, timing). Order-by/column-name and header sinks are
commonly missed — include them.

### Phase 2 — Oracle selection (first gate)
Pick the weakest *reliable* oracle for the context; do not jump to UNION blindly:
| Oracle | When | Proof |
|---|---|---|
| **Error-based** | DB errors surface | Parser error text tied to your input |
| **Boolean-blind** | Response differs true/false | Stable content delta on `AND 1=1` vs `AND 1=2` logic |
| **Time-blind** | No visible diff | Controlled, repeatable delay (DBMS-specific sleep) |
| **UNION** | Columns/types align & output reflects | Your marker rows appear in output |
| **Out-of-band** | Fully blind / stacked | Callback to your unique OOB host |

A delay or delta must be **repeatable and attributable** — confirm 2–3x and rule
out network jitter / rate-limiting before claiming it.

### Phase 3 — DBMS fingerprinting
Identify the engine (MySQL/MariaDB, PostgreSQL, MSSQL, Oracle, SQLite) from error
strings, function behaviour, comment syntax, and concatenation operators — this
drives correct syntax for every later step (`references/injection-points-and-dbms.md`).

### Phase 4 — Controlled confirmation & scope of impact
Demonstrate impact **minimally**: current user/db/version, or authentication
bypass on a login oracle, or a bounded count of accessible rows — enough to
prove severity, never bulk exfiltration. Prefer a read of a non-sensitive
metadata value as the proof-of-concept. If automation (`sqlmap`) is authorized,
cap it: `--level`/`--risk` conservative, `--technique` to the confirmed oracle,
no `--dump` of sensitive tables without explicit approval.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, oracle type, DBMS, the
differential/callback proof path, and reproduction. WAF 403 on a quote, generic
500s, or framework validation errors are **signals, not confirmation** → do not
mark `confirmed` without a working oracle.

## Impact escalation
Translate to outcome: authentication bypass, unauthorized data read (PII/creds),
second-order injection via stored values, or (where the engine/privileges allow
and scope permits) file read / command surfaces — each stated with the concrete
principal and data at risk. Score with CVSS (`_shared/cvss-reference.md`).

## False positives & pitfalls
- Reflected quote or SQL error page without a working oracle → **inconclusive**.
- Timing that is not repeatable, or matches overall latency → not time-blind SQLi.
- ORM/parameterized endpoints usually **refute** structural injection — verify
  before claiming.
- Never run destructive or state-changing SQL; stacked-query writes need approval.

## Remediation
- **Parameterized queries / prepared statements** everywhere; never string-concat
  user input into SQL.
- Use an ORM/query-builder with bound parameters; allow-list for identifiers
  (column/table/sort) that cannot be parameterized.
- Least-privilege DB accounts (no DDL/file privileges for app users), WAF as
  defense-in-depth only, and generic error handling (no SQL errors to client).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/injection-points-and-dbms.md` — per-DBMS syntax & oracle variants (4th level).
