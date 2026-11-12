---
name: side-channel-intro
description: >
  Use when assessing an authorized device for side-channel exposure at a practical
  level — timing, power-analysis, and fault-injection concepts — to understand
  whether sensitive operations leak via physical channels. Introductory/assessment
  framing.
type: knowledge
domain: hardware-iot
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Side-Channel & Fault-Injection (intro/assessment)

Sensitive operations (crypto, auth) can leak through physical side channels —
timing, power consumption, EM — or be disrupted by fault injection (glitching) to
bypass checks. Assess, at a practical level, whether an authorized device's
sensitive operations are exposed to these physical attacks.

> Authorized research on your own/in-scope hardware (`_shared/scope-authorization-rule.md`).

## When to use
Assessing high-assurance devices (secure elements, crypto devices) where physical
attacks are in scope.

## Procedure (gated phases)
1. **Identify sensitive operations** — crypto/auth/secure-boot checks that an
   attacker with physical access might target.
2. **Side-channel exposure** — does the implementation have timing/power leakage
   (non-constant-time crypto, data-dependent behaviour)?
3. **Fault-injection exposure** — can security checks (secure boot, PIN) be bypassed
   by glitching (voltage/clock/EM) — conceptually assess resistance.
4. **Assess & recommend** — the exposure and mitigations.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record exposure assessment; practical
demonstration requires specialized equipment.

## Impact escalation
Key/secret recovery or security-check bypass via physical attack. CVSS/physical per
`_shared/cvss-reference.md`.

## Pitfalls
- Requires specialized equipment/expertise for full demonstration — scope realistically.

## Remediation
- Constant-time crypto; side-channel-resistant implementations; fault-injection
  countermeasures (redundancy, sensors); secure elements for keys; tamper response.

## References
- `_shared/` rules (authorization, evidence).
