---
name: continuous-authentication
description: >
  Use when designing continuous/adaptive authentication — re-evaluating trust during
  a session based on risk signals (behavior, context, anomalies) rather than
  authenticating once. Covers adaptive/risk-based auth.
type: knowledge
domain: zero-trust
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Continuous / Adaptive Authentication

Authenticating once at login leaves a long window if a session is hijacked. Continuous
authentication re-evaluates trust throughout a session using risk signals — location/
device changes, behavioral anomalies, impossible travel — and steps up (re-auth/MFA)
or blocks when risk rises.

## When to use
When adding session-long, risk-based verification (zero-trust maturity).

## Procedure (gated phases)
1. **Define risk signals** — context (location/device/network), behavioral patterns,
   impossible travel, and anomalous actions.
2. **Risk scoring** — compute session risk continuously from signals.
3. **Adaptive response (core)** — low risk: seamless; elevated risk: step-up (MFA/
   re-auth) or restrict; high risk: terminate the session.
4. **Tune** — balance security with user friction; measure false step-ups.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = risk is evaluated during sessions and
drives adaptive responses; tuned for usability.

## Quality bar / pitfalls
- Constant friction (over-prompting) → user workarounds.
- Only authenticating at login (hijack window) — the gap this closes.

## Linkage
- Part of zero-trust; pairs with device-posture, identity-iam, and session-management
  (offensive view).

## References
- `_shared/` rules (evidence).
