---
name: jit-access-design
description: >
  Use when designing just-in-time / just-enough access — replacing standing
  privilege with time-bound, approved, least-privilege grants that expire. Covers
  JIT access design to minimize standing attack surface.
type: knowledge
domain: identity-iam
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Just-In-Time (JIT) Access

Standing privilege is standing risk. JIT grants elevated access only when needed,
for a bounded time, with approval, and least-privilege scope — then it expires. This
shrinks the window an attacker can abuse a privileged account to near-zero outside
active, approved use.

## When to use
Reducing standing privileged/elevated access (cloud roles, admin, sensitive data).

## Procedure (gated phases)
1. **Identify standing privilege** — roles/permissions granted permanently that are
   used occasionally (prime JIT candidates).
2. **Design the JIT flow** — request → approval (gated) → time-bound, scoped grant →
   automatic expiry/revocation.
3. **Least-privilege scope** — grant just-enough for the task, not broad admin.
4. **Audit** — log every elevation (who/what/when/why); alert on anomalies.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = elevated access is time-bound,
approved, scoped, and auto-expires; standing privilege is minimized.

## Quality bar / pitfalls
- JIT that grants broad admin (defeats least-privilege) — scope it.
- Grants that don't actually expire — enforce auto-revocation.

## Linkage
- Pairs with privileged-access-pam, zero-trust, cloud-iam; reduces blast radius.

## References
- `_shared/` rules (evidence, gated workflow).
