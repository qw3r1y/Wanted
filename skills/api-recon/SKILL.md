---
name: api-recon
description: >
  Use when mapping an authorized API's attack surface before testing — discovering
  endpoints, methods, parameters, versions, and the spec (Swagger/OpenAPI/GraphQL
  schema). Produces the endpoint inventory that drives every other API test. Do
  NOT use for exploitation (see the specific api/* skills).
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl, ffuf]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# API Reconnaissance (authorized testing)

Build a complete inventory of an API's surface — hosts, versions, endpoints,
methods, parameters, auth model, and the formal spec — so later tests are
targeted, not guessed. Hidden/undocumented endpoints and old versions are where
most API bugs live.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Respect rate
> limits; enumeration must stay bounded (`safe-execution-rules.md`).

## When to use
At the start of any API engagement, and whenever a new API host/version appears.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Find the spec** — look for `/swagger`, `/openapi.json`, `/api-docs`,
   GraphQL introspection, `.well-known`, and client JS bundles that embed routes.
2. **Enumerate endpoints & methods** — from spec + JS + traffic; probe allowed
   methods (GET/POST/PUT/PATCH/DELETE/OPTIONS) per route; note version prefixes
   (`/v1`, `/v2`) and **old versions** still live.
3. **Map parameters & auth** — required/optional params, object references (ids),
   and the auth scheme (bearer/JWT/API key/session); note which endpoints are
   authenticated.
4. **Record the inventory** — a structured endpoint list in `OUTPUT_DIR` tagging
   each with method, params, object refs, and auth — the input for bola/bfla/
   mass-assignment/jwt/etc.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. The deliverable is the inventory; mark
discovered-but-unverified endpoints as such.

## Impact escalation
Recon enables every later finding; undocumented/old-version endpoints and exposed
specs are themselves risk signals.

## False positives & pitfalls
- 404/placeholder routes mistaken for real endpoints — confirm behaviour.
- Don't brute-force aggressively into bans; use the spec first.

## Remediation
- Keep API inventory/versioning controlled; retire old versions; restrict public
  spec exposure to what is intended; ensure auth is enforced on **every** route,
  including undocumented ones.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
