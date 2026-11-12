---
name: mass-assignment
description: >
  Use when testing an authorized API for mass assignment / auto-binding (OWASP
  API6) — endpoints that bind request fields directly to internal objects,
  letting a client set fields it should not (role, isAdmin, balance, ownership,
  verified). Covers hidden-field discovery, proof and remediation.
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

# Mass Assignment / Auto-Binding (OWASP API6)

Find create/update endpoints that bind client-supplied fields straight onto
internal models, so a client can set properties the UI never exposes — privilege,
ownership, status, pricing. The proof is a protected field changing because you
sent it.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Use test
> accounts; keep effects minimal/reversible.

## When to use
Registration, profile/update, create-resource, and settings endpoints — anywhere
a JSON/body object is bound to a model.

## Prerequisites
- Authorization + scope; test account; knowledge of model fields (from recon,
  responses, or related GET endpoints). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Discover candidate fields** — read what GET returns for the object; infer
   sensitive fields (`role`, `isAdmin`, `verified`, `owner_id`, `balance`,
   `status`, `price`). These are the targets.
2. **Inject sensitive fields (core gate)** — on a create/update request, add the
   sensitive field(s) with a value favoring you; submit as the test user.
3. **Confirm the binding** — re-read the object/behaviour; if the protected field
   changed (e.g., role elevated, price altered) → mass assignment.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the endpoint, the
injected field, and before/after proof of the field changing. Field ignored →
**refuted**.

## Impact escalation
Privilege escalation (role/admin), ownership/tenant takeover, price/balance
tampering, and verification bypass. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Server ignores unknown/extra fields → **refuted**.
- Field accepted but overwritten server-side → no real effect.

## Remediation
- Use explicit **allow-lists** (DTOs/field binding) for which fields a request may
  set; never bind request bodies directly to models.
- Separate read/write field sets; enforce authorization on sensitive fields
  server-side; reject unexpected fields.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
