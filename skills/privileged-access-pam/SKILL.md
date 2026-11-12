---
name: privileged-access-pam
description: >
  Use when designing/assessing Privileged Access Management — securing, vaulting,
  brokering, and monitoring privileged accounts/sessions to reduce the blast radius
  of admin credentials. Covers PAM design and controls.
type: knowledge
domain: identity-iam
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Privileged Access Management (PAM)

Privileged credentials are the attacker's goal. PAM reduces their risk: vault and
rotate privileged secrets, broker access through a controlled path (no direct
standing admin), enforce MFA + approval, and record privileged sessions — shrinking
the blast radius and the standing attack surface.

## When to use
Securing admin/root/service privileged access across the estate.

## Procedure (gated phases)
1. **Inventory privileged accounts** — admin, root, service, break-glass, and where
   they're used.
2. **Vault & rotate** — store privileged credentials in a vault; rotate; eliminate
   shared/static admin passwords.
3. **Broker access (core)** — access via the PAM broker with MFA + approval; avoid
   direct standing privileged logins; prefer ephemeral/JIT (jit-access-design).
4. **Monitor** — session recording + alerting on privileged activity; least-privilege
   even within admin.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = privileged access is vaulted,
brokered, MFA'd, and monitored; no standing shared admin.

## Quality bar / pitfalls
- Standing shared admin credentials (the common gap).
- PAM deployed but bypassable (direct access still possible).

## Linkage
- Pairs with jit-access-design, iam-architecture, zero-trust; protects against
  credential-dumping/lateral movement.

## References
- `_shared/` rules (evidence).
