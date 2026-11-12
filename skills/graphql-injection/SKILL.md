---
name: graphql-injection
description: >
  Use when testing an authorized GraphQL endpoint for GraphQL-specific issues —
  introspection exposure, excessive data/field access, broken object/field-level
  authorization, batching/alias abuse, and injection into resolvers. Covers
  schema recon, abuse testing and remediation. For classic injection in resolvers
  defer to sqli/nosql/command-injection.
type: knowledge
domain: offensive/web
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

# GraphQL Security Testing (authorized)

Map the GraphQL schema, then test the issues unique to GraphQL: introspection
leakage, authorization enforced inconsistently across fields/objects, batching/
alias-based abuse (rate-limit/brute-force amplification), and injection flowing
into resolvers. The proof is unauthorized data/field access or a resolver-backed
injection.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Keep queries
> bounded; batching can amplify load (`safe-execution-rules.md`).

## When to use
Any `/graphql`-style endpoint. Candidates: queries/mutations returning user data,
admin fields, and endpoints relying on the UI to hide sensitive fields.

## Prerequisites
- Authorization + scope; test identities for authz checks.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Schema recon (first gate)** — attempt introspection; if disabled, infer
   types via error-based field suggestions. Catalogue queries/mutations and
   sensitive fields.
2. **Authorization testing** — with two identities, request objects/fields that
   should be restricted (object-level and **field-level** authz are often
   inconsistent even when the UI enforces them) — this is GraphQL's most common
   high-impact bug (see also offensive/web/idor).
3. **Batching/alias abuse** — test aliased/batched queries to bypass rate limits
   or amplify brute-force (e.g., many login attempts in one request) — bounded.
4. **Injection into resolvers** — where arguments reach a DB/command, pivot to the
   relevant injection skill.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the issue class, the
query, and the unauthorized data/field or amplification proof. Introspection
enabled alone is **informational** unless it exposes real risk.

## Impact escalation
Unauthorized data access (object/field authz), rate-limit/brute-force
amplification, DoS via deeply nested/expensive queries, and resolver injection.
CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Field-level authz enforced server-side → **refuted** for that field.
- Introspection disabled but schema inferable → still test authz.
- Avoid heavy nested/batched queries that could DoS the target.

## Remediation
- Enforce **object- and field-level authorization** in resolvers, server-side,
  consistently; do not rely on the client hiding fields.
- Disable introspection in production; add query cost/depth limits and rate
  limiting that accounts for aliases/batching; validate/parameterize resolver
  inputs.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
