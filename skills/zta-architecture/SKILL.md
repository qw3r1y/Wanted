---
name: zta-architecture
description: >
  Use when designing/assessing a Zero Trust architecture — never-trust-always-verify,
  identity-centric access, per-request authorization, and eliminating implicit
  network trust. Covers ZTA design principles and roadmap.
type: knowledge
domain: zero-trust
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Zero Trust Architecture

Replace implicit network trust ("inside = trusted") with per-request verification of
identity, device, and context. Design toward identity-centric access, least-
privilege, microsegmentation, and continuous verification — so a breached perimeter
or device doesn't grant free lateral access.

## When to use
When designing or maturing toward zero-trust across network/identity/apps.

## Procedure (gated phases)
1. **Define protect surfaces** — the critical data/assets/apps and who/what needs
   access (not the whole network at once).
2. **Identity-centric access (core)** — access decisions on verified identity +
   device posture + context, per request; strong MFA (identity-iam).
3. **Microsegmentation** — eliminate flat networks; least-privilege east-west
   (microsegmentation skill).
4. **Continuous verification** — re-evaluate trust continuously (device-posture,
   continuous-auth); log + analyze everything.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Maturing" = access is identity+context based,
least-privilege, and segmented; measure against a ZT maturity model.

## Quality bar / pitfalls
- "Zero trust" as a product purchase vs an architecture/principle.
- Big-bang rollout — iterate protect-surface by protect-surface.

## Linkage
- Integrates identity-iam, microsegmentation, device-posture, continuous-auth, and
  network-policy.

## References
- `_shared/` rules (evidence).
