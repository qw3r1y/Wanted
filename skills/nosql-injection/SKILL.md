---
name: nosql-injection
description: >
  Use when testing an authorized target backed by a NoSQL store (MongoDB,
  CouchDB, Redis, Elasticsearch, DynamoDB) for NoSQL injection — operator
  injection, authentication bypass, and blind boolean/time extraction. Covers
  detection, context analysis, controlled proof and remediation. Do NOT use for
  classic SQL (see offensive/web/sqli).
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, oob-listener]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# NoSQL Injection (authorized testing)

Find input that alters a NoSQL query's **structure or operators** — typically via
injected query operators in JSON/body or type-confusion in parameters — and prove
it with a reliable oracle. The classic case is authentication bypass via operator
injection; the general case is blind boolean/time extraction.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Read-only
> posture; no destructive operations (`safe-execution-rules.md`).

## When to use
Endpoints backed by document/key-value/search stores: login/auth, search/filter,
JSON APIs that pass user fields into a query, and any place a parameter's **type**
(string vs object/array) is attacker-controlled.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify the store & intake** — JSON body vs query params; whether the app
   lets a value become an object/array (operator injection) or interprets special
   syntax.
2. **Operator/type probing (first gate)** — test whether an always-true operator
   construct changes behaviour (e.g., auth returns a session, or a filter returns
   all records). A behavioural differential is the signal.
3. **Oracle selection** — boolean-blind (true/false response delta), time-blind
   (store-specific delay, repeatable 2–3x), or in-band output. Confirm
   attributable & repeatable.
4. **Controlled confirmation** — demonstrate the minimum (auth bypass on a test
   account, or a bounded record count) proving severity; no bulk extraction.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, store, oracle, and the
differential/bypass proof. A reflected `$`-sign or error alone → **inconclusive**.

## Impact escalation
Authentication bypass, unauthorized data read, filter bypass (access to all
records), and server-side JS execution where the engine evaluates it. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Parameterized/typed queries that coerce input to string → likely **refuted**.
- Framework validation rejecting objects where strings are expected → defense works.
- Non-repeatable timing → not time-blind.

## Remediation
- Enforce **type validation** (reject objects/arrays where scalars are expected);
  cast/normalize inputs before query use.
- Use parameterized query builders; never pass raw user objects into query
  operators; disable server-side JS evaluation where unused.
- Least-privilege DB users; generic errors.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
