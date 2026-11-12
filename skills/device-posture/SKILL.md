---
name: device-posture
description: >
  Use when incorporating device trust into access decisions — verifying device
  health/compliance (managed, patched, encrypted, EDR) as a condition of access.
  Covers device-posture as a zero-trust signal.
type: knowledge
domain: zero-trust
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Device Posture in Access Decisions

In zero trust, who you are isn't enough — the device matters too. Verify device
health/compliance (managed, patched, disk-encrypted, EDR present, not jailbroken) as
a condition of access, so a valid credential from a compromised/unmanaged device
doesn't grant sensitive access.

## When to use
When adding device trust to conditional access (part of a ZT rollout).

## Procedure (gated phases)
1. **Define posture requirements** — per sensitivity: managed/enrolled, OS patch
   level, disk encryption, EDR running, screen lock, etc.
2. **Signal source** — MDM/EDR/endpoint agents providing real-time posture to the
   access decision (conditional access).
3. **Enforce in access (core)** — access to sensitive resources requires meeting
   posture; step-down/block for non-compliant devices.
4. **Remediate** — guide users to compliance; re-evaluate continuously.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = sensitive access is gated on
verified device posture, evaluated at access time.

## Quality bar / pitfalls
- Trusting a self-reported/static posture signal — use attested, real-time signals.
- All-or-nothing blocking without remediation path — frustrates users.

## Linkage
- Part of zero-trust + identity-iam conditional access; pairs with continuous-auth.

## References
- `_shared/` rules (evidence).
