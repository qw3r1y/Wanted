---
name: mfa-bypass
description: >
  Use when testing an authorized target's multi-factor authentication for bypass —
  skippable verification steps, state/flow flaws, backup-code/remember-device
  weaknesses, response manipulation, and MFA-fatigue. Covers flow analysis, proof
  and remediation.
type: knowledge
domain: offensive/auth-identity
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

# MFA Bypass (authorized testing)

Test whether the second factor can be skipped, forged, or rendered ineffective —
reaching an authenticated state without completing MFA. The proof is a session
with full access obtained without a valid second factor, on a test account.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Test accounts
> only.

## When to use
Any login that enforces MFA, step-up auth, and sensitive-action re-verification.

## Prerequisites
- Authorization + scope; an MFA-enabled test account. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Map the flow** — where MFA sits, what token/state tracks "MFA passed", and
   what endpoints the pre-MFA session can reach.
2. **Bypass tests (core gate)**:
   - *Step skip:* access post-login endpoints directly with the pre-MFA session.
   - *State flaw:* force the "mfa_verified" flag/param, or reuse a prior verified
     token.
   - *Response manipulation:* alter the verification response (success/failure
     field) and see if the client/server trusts it.
   - *Backup/remember-device:* weak backup codes, forgeable "remember device"
     cookie, or OTP brute-force (see credential-attacks).
   - *MFA fatigue:* repeated push prompts (process/UX weakness) — report as a risk.
3. **Confirm full access** — a fully-authenticated action without MFA on the test
   account.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the bypass class, and the
authenticated-without-MFA proof. MFA strictly enforced at every gate → **refuted**.

## Impact escalation
Account takeover despite MFA, defeating the primary compensating control. Usually
high/critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Pre-MFA session reaching only public endpoints → not a bypass.
- Server re-checks MFA state server-side at each step → **refuted**.

## Remediation
- Track MFA completion **server-side** and enforce it on every authenticated
  endpoint; never trust client flags/responses; bind "remember device" to strong,
  signed tokens with expiry; limit push prompts (fatigue) and add number-matching;
  strong backup-code entropy and attempt limits.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
