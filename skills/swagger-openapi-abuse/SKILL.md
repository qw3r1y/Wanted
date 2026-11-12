---
name: swagger-openapi-abuse
description: >
  Use when an authorized API exposes a Swagger/OpenAPI spec — leveraging it to
  discover hidden/undocumented endpoints, deprecated versions, and over-permissive
  operations, and flagging the exposure itself where unintended. Covers
  spec-driven surface expansion and remediation.
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

# Swagger / OpenAPI Exposure & Abuse (authorized testing)

An exposed API spec is a gift for surface mapping — and sometimes a finding in
itself. Use it to enumerate every operation (including undocumented-in-UI and
deprecated ones), then test those for authz/validation gaps. Flag the spec
exposure where it was not intended to be public.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
When `/swagger`, `/openapi.json`, `/api-docs`, a Swagger UI, or an embedded spec
is reachable.

## Prerequisites
- Authorization + scope. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Retrieve & parse the spec** — extract all paths, methods, params, auth
   requirements, and server/version info.
2. **Expand surface (core)** — identify operations not exposed in the UI,
   deprecated/old-version endpoints, and admin/debug operations; feed these into
   bola/bfla/mass-assignment/rest-abuse testing.
3. **Assess exposure** — determine whether the spec should be public; an internal/
   admin spec reachable unauthenticated is itself a finding.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. The deliverable is an expanded, verified
endpoint inventory plus any confirmed issues from the exposed operations; note the
spec-exposure finding where applicable.

## Impact escalation
Accelerated discovery of authz/validation bugs via hidden operations; direct
information disclosure where the spec reveals internal design/credentials. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- A spec intended to be public (developer portal) → exposure is not a finding by
  itself; the operations still warrant testing.
- Listed endpoints may be stale — confirm they are live.

## Remediation
- Restrict spec exposure to intended audiences (auth-gated or internal); keep the
  spec in sync and retire deprecated operations; ensure every documented and
  **undocumented** operation enforces authz/validation.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
