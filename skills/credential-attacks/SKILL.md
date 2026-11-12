---
name: credential-attacks
description: >
  Use when testing an authorized target's resistance to credential-based attacks —
  password spraying, credential stuffing, login brute-force, and OTP brute-force —
  focused on whether protections hold, demonstrated minimally without real
  account compromise. Covers protection analysis and remediation.
type: knowledge
domain: offensive/auth-identity
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

# Credential Attacks — Spraying / Stuffing / Brute-Force (authorized testing)

Assess whether login and OTP flows resist automated credential attacks. The goal
is to prove a **control gap** (no lockout, no rate limit, username enumeration,
OTP brute-forceable) — not to actually compromise accounts. Demonstrate bounded;
never run a real large-scale attack on live accounts.

> Authorized testing only. **Bounded** attempts on test accounts; no real
> credential compromise (`safe-execution-rules.md`).

## When to use
Login, OTP/2FA verification, password reset, and any credential-verifying
endpoint. Pairs with api/rate-limit-bypass.

## Prerequisites
- Authorization + scope; test accounts. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate protections** — lockout threshold, rate limit (and its key),
   CAPTCHA/step-up, and whether responses/ timing **leak username validity**
   (enumeration).
2. **Control-gap tests (core gate, bounded)**:
   - *Spraying:* a few common passwords across several test usernames — is there a
     global/account lockout?
   - *Stuffing:* reused-credential pattern — is automation detected?
   - *Brute-force:* bounded attempts on a test account — does lockout/backoff fire?
   - *OTP:* is the code space small and attempts unlimited (brute-forceable)?
3. **Minimal demonstration** — show the gap (e.g., N attempts with no lockout),
   not an actual break-in.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the missing control, and
the bounded proof. Lockout/rate-limit/enum-safe responses → **refuted**.

## Impact escalation
Account takeover at scale, username enumeration enabling targeting, and OTP
bypass. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Effective lockout/rate-limit/step-up → **refuted**.
- Generic "invalid credentials" (no enumeration) is correct behaviour.
- Never conduct real brute-force against live user accounts.

## Remediation
- Account + IP-aware rate limiting and lockout/backoff; uniform, timing-safe
  responses (no username enumeration); CAPTCHA/step-up on anomalies; strong OTP
  (sufficient entropy, attempt limits, short expiry); breached-password checks and
  MFA.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
