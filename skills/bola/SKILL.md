---
name: bola
description: >
  Use when testing an authorized API for Broken Object Level Authorization
  (OWASP API1) — object references in API requests that return/act on another
  user's object without an ownership check. The most common and impactful API
  bug. Covers two-identity testing, proof and remediation. See also
  offensive/web/idor (same class, API focus).
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl, burp-repeater]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# BOLA — Broken Object Level Authorization (OWASP API1)

Find API endpoints that trust a client-supplied object reference without checking
the caller owns/may access it, so one user reaches another's object. The proof is
a two-identity differential: user A's token returning user B's object.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Access the
> least data needed; no bulk enumeration of real users (`safe-execution-rules.md`).

## When to use
Any API route with an object reference: `/api/users/{id}`, `/orders/{id}`,
`/documents/{id}`, tenant-scoped resources, and references in bodies/GraphQL
variables.

## Prerequisites
- Authorization + scope; **two controlled identities** (A, B).
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **From api-recon**, list endpoints carrying object references and their id
   formats (int/UUID/hash/slug).
2. **Two-identity differential (core gate)** — with A's token, request B's object
   reference. B's data returned → BOLA. 403/404/empty → authz enforced
   (**refuted** for that endpoint). Test both read and (with approval) write.
3. **Reference nuances** — sequential ids, leaked/predictable UUIDs, indirect/
   hashed refs; "hidden" API fields the UI never shows but the API accepts.
4. **Horizontal vs vertical** — peer access vs higher-privilege object (higher
   severity).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the A-token-reads-B
request/response pair, reference type, read vs write. A guessable id alone →
**inconclusive** until cross-identity access is shown.

## Impact escalation
Mass PII/financial exposure, account takeover (write on another id), cross-tenant
breach. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Accessing your own object via a different ref form → not BOLA.
- 403/404 for other ids → authz works.
- Keep enumeration minimal.

## Remediation
- Enforce **object-level authorization on every request**, server-side; verify the
  authenticated principal may access the referenced object; never trust client
  references. Centralize authz; add tests to CI. UUIDs are not access control.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
