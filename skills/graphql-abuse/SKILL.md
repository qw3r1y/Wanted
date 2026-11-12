---
name: graphql-abuse
description: >
  Use when testing an authorized GraphQL API for GraphQL-specific abuse —
  introspection exposure, field/object authorization gaps, alias/batching
  amplification, and query-depth/cost DoS. Covers schema recon and abuse testing.
  For resolver injection, pivot to sqli/nosql/command-injection; overlaps
  offensive/web/graphql-injection.
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# GraphQL Abuse (authorized testing)

Exercise the issues unique to GraphQL at the API layer: introspection leakage,
authorization enforced inconsistently across fields/objects, and alias/batching
that amplify brute-force or expensive queries. The proof is unauthorized field/
object access or a demonstrable amplification/cost issue.

> Authorized testing only. Keep queries **bounded** — depth/batching can DoS
> (`safe-execution-rules.md`).

## When to use
Any GraphQL endpoint in scope, especially those relying on the UI to hide fields.

## Prerequisites
- Authorization + scope; two identities for authz. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Schema recon** — introspection if enabled; else infer via error suggestions.
   Inventory queries/mutations and sensitive fields.
2. **Field/object authz (core gate)** — with two identities, request restricted
   fields/objects; GraphQL commonly enforces authz inconsistently at field level.
3. **Alias/batching** — test aliased/batched operations for rate-limit bypass and
   amplification (bounded); test nested-query cost for DoS potential (reason about
   it; do not actually DoS).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the issue, the query, and
the unauthorized data/amplification proof. Field-level authz enforced →
**refuted** for that field.

## Impact escalation
Unauthorized data access, brute-force amplification, and DoS. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Introspection disabled yet schema inferable — still test authz.
- Avoid heavy nested/batched queries that could take down the target.

## Remediation
- Enforce field/object authorization server-side consistently; disable production
  introspection; add depth/cost limits and alias/batch-aware rate limiting.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
