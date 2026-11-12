---
name: authz-patterns
description: >
  Use when designing/reviewing authorization in an application — centralized
  enforcement, object- and function-level checks, RBAC/ABAC patterns, and avoiding
  the broken-access-control mistakes that top the OWASP list. Covers robust authz
  design.
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Authorization Patterns

Broken access control is the #1 web risk. Design authorization so it is enforced
**server-side, centrally, on every request** — object-level (does this principal own
this object?) and function-level (may this principal call this operation?) — using a
clear RBAC/ABAC model rather than scattered ad-hoc checks.

## When to use
Designing/reviewing any multi-user/multi-tenant app's access control.

## Procedure (gated phases)
1. **Define the model** — roles/attributes, resources, and the rules (who can do
   what to which objects); document tenancy boundaries.
2. **Centralize enforcement** — a single policy/middleware layer checked on every
   request; avoid per-endpoint hand-rolled checks that drift.
3. **Object + function level** — verify ownership/scope for object access (prevents
   BOLA/IDOR) AND privilege for operations (prevents BFLA).
4. **Deny by default** — default-deny; explicit grants; same checks for API and UI.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Correct" = default-deny, centralized,
object+function-level, verified by authz tests (and offensive idor/bola testing).

## Quality bar / pitfalls
- UI-only or client-side authorization (trivially bypassed).
- Scattered checks that drift / miss endpoints — centralize.

## Linkage
- Prevents web/idor, api/bola, api/bfla; add authz tests to CI.

## References
- `_shared/` rules (evidence).
