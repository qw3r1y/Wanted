---
name: session-management
description: >
  Use when testing an authorized target's session handling — fixation, predictable
  or non-rotated tokens, weak invalidation (logout/password-change), insecure
  cookie flags, and concurrent-session issues. Covers lifecycle analysis, proof
  and remediation.
type: knowledge
domain: offensive/auth-identity
maturity: canonical
tools: [curl, browser]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Session Management Testing (authorized)

Examine the session token's full lifecycle for weaknesses that allow hijacking or
persistence: fixation (token not rotated at login), predictability, missing
invalidation on logout/password change, and insecure cookie attributes. The proof
is a session remaining valid or usable when it should not be.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Test accounts.

## When to use
Any session-based auth (cookies/tokens). Pairs with jwt-attacks for JWT sessions.

## Prerequisites
- Authorization + scope; test accounts; two browsers/clients. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Capture lifecycle** — token at pre-auth, post-login, post-privilege-change,
   logout, and password change. Note cookie flags (`HttpOnly`, `Secure`,
   `SameSite`), entropy, and expiry.
2. **Lifecycle tests (core gate)**:
   - *Fixation:* does the token **rotate** on login? If a pre-auth token stays
     valid post-login, fixation is possible.
   - *Invalidation:* is the old session invalidated on logout and on password
     change? Replay the old token after each.
   - *Predictability:* is the token random/unguessable?
   - *Cookie flags:* missing `HttpOnly`/`Secure`/`SameSite` increases hijack risk.
   - *Concurrent:* are stale sessions revoked on security events?
3. **Confirm** — demonstrate the specific weakness (e.g., old token valid after
   logout) on a test account.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the weakness, and the
replay/flag proof. Proper rotation + invalidation + flags → **refuted**.

## Impact escalation
Session hijacking, fixation-based takeover, and persistence after credential
change. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Token rotates and old sessions die on logout/password-change → **refuted**.
- Missing `HttpOnly` alone is a weakness, not takeover — pair with XSS for impact.

## Remediation
- Rotate the session id on login/privilege change; invalidate server-side on
  logout and password/security changes; high-entropy tokens; `HttpOnly` +
  `Secure` + `SameSite` cookies; sensible idle/absolute timeouts; revoke sessions
  on security events.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
