---
name: rate-limit-bypass
description: >
  Use when testing an authorized API's rate limiting / anti-automation (OWASP
  API4) — whether throttles on sensitive actions (login, OTP, reset, pay) can be
  bypassed, enabling brute-force or abuse. Covers limit discovery, bypass analysis
  and remediation.
type: knowledge
domain: offensive/api
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Rate-Limit / Anti-Automation Bypass (OWASP API4)

Determine whether protections on sensitive, limited actions actually hold, or can
be bypassed to enable brute-force/abuse. The proof is exceeding the intended limit
via a bypass — demonstrated **minimally**, never a real brute-force at scale.

> Authorized testing only. Keep attempts **bounded**; demonstrate the bypass
> mechanism, do not run a full brute-force (`safe-execution-rules.md`).

## When to use
Login, OTP/MFA, password reset, coupon/redeem, payment, and any costly or
security-sensitive endpoint.

## Prerequisites
- Authorization + scope; test account. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Find the limit** — how many attempts before throttle/lockout; what the limit
   is keyed on (IP, account, token, device).
2. **Bypass analysis (core gate)** — test whether the key can be rotated/forged:
   IP via `X-Forwarded-For`/`X-Real-IP`, per-account vs global gaps, header/casing
   variations, GraphQL aliasing/batching to pack many attempts in one request,
   parallel requests, or endpoint variants that skip the limiter.
3. **Minimal demonstration** — show a **small** bounded over-limit (e.g., a few
   extra attempts past the cap) proving the bypass; do not attempt real credential
   brute-force.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the limiter key, the
bypass, and the bounded over-limit proof. Limit holds across all variants →
**refuted**.

## Impact escalation
Credential/OTP brute-force, enumeration, resource/financial abuse, and DoS. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Limit enforced server-side on the true identity across variants → **refuted**.
- Never conduct an actual large-scale brute-force on real accounts.

## Remediation
- Rate-limit on a **trusted server-side identity** (not spoofable headers); apply
  to all endpoint variants and account for batching/aliasing; add lockout/backoff
  and anomaly detection on sensitive actions; CAPTCHA/step-up where appropriate.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
