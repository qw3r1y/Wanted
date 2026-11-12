---
name: password-reset-abuse
description: >
  Use when testing an authorized target's password-reset flow — host-header/link
  poisoning, weak/predictable tokens, token leakage, reset without old-session
  invalidation, and user-field confusion. Covers flow analysis, proof and
  remediation. A frequent account-takeover vector.
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

# Password Reset Abuse (authorized testing)

Test the reset flow for the flaws that let an attacker take over an account:
poisoned reset links (host-header injection), weak/guessable/leaked tokens, tokens
that don't expire or bind to the user, and resets that don't invalidate existing
sessions. The proof is controlling another (test) account's reset or token.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Only accounts/
> mailboxes you control.

## When to use
"Forgot password" / account-recovery flows. Pairs with
offensive/web/host-header-injection.

## Prerequisites
- Authorization + scope; test accounts + mailboxes you control. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Map the flow** — how the token is generated, delivered, validated, and
   consumed; what builds the reset URL.
2. **Abuse tests (core gate)**:
   - *Link poisoning:* manipulate `Host`/`X-Forwarded-Host` so the emailed link
     (and token) point to your host (test account).
   - *Token strength:* is it random/unguessable, single-use, short-lived, and
     **bound to the user**? Test reuse, expiry, and cross-account use.
   - *Leakage:* token in URL/referer/response/logs.
   - *Field confusion:* multiple email/username params to redirect delivery.
   - *Session invalidation:* are existing sessions killed after reset?
3. **Confirm** — demonstrate takeover of a **test** account via the flaw.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the flaw, and the proof
(poisoned link to attacker host / token reuse) on a test account. Strong bound
single-use tokens + canonical host → **refuted**.

## Impact escalation
Account takeover (the canonical impact), and mass takeover if the flaw is generic.
Critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Canonical host for links + strong token → **refuted**.
- Only ever target accounts/mailboxes you own.

## Remediation
- Build reset URLs from a **configured canonical host**; high-entropy, single-use,
  short-lived tokens **bound to the user**; never leak tokens in URLs/referrer;
  invalidate sessions on reset; rate-limit and notify the user.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
