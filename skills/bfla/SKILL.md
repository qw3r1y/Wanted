---
name: bfla
description: >
  Use when testing an authorized API for Broken Function Level Authorization
  (OWASP API5) — privileged functions/methods (admin endpoints, elevated HTTP
  methods) accessible to lower-privilege or unauthenticated callers. Covers
  role/method matrix testing, proof and remediation.
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

# BFLA — Broken Function Level Authorization (OWASP API5)

Find privileged **functions** (not just objects) that are reachable by callers who
should not have them — admin/management endpoints, destructive methods, or
role-restricted actions accessible to a normal or anonymous user. The proof is a
lower-privilege identity successfully invoking a higher-privilege function.

> Authorized testing only. Prove with the minimal benign invocation; destructive
> functions need per-action approval (`safe-execution-rules.md`).

## When to use
Admin/management routes, user-management, config, bulk operations, and endpoints
where the same object supports different privilege levels; also non-GET methods
(PUT/PATCH/DELETE) on resources.

## Prerequisites
- Authorization + scope; identities of **different privilege** (anon, user, admin).
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate privileged functions** — from recon, flag admin/management/
   destructive endpoints and elevated methods.
2. **Role/method matrix (core gate)** — call each privileged function with a
   **lower-privilege** (or no) token. Success → BFLA. Proper 401/403 → enforced.
   Test method-based bypass (e.g., GET-protected but PUT/PATCH open) and verb
   tunneling (`X-HTTP-Method-Override`).
3. **Confirm the action occurred** — a 200 is not enough; verify the privileged
   effect (minimally, on test data).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the function, the
lower-priv identity used, and the invocation proof.

## Impact escalation
Privilege escalation, admin takeover, data manipulation/deletion, and config
tampering. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- 200 with no actual privileged effect (e.g., filtered result) → verify the effect.
- Function protected by server-side role check → **refuted**.

## Remediation
- Deny by default; enforce **function/role authorization** server-side on every
  endpoint and method; do not rely on hidden UI routes.
- Consistent authorization middleware across all methods; validate
  method-override headers; audit admin endpoints.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
