---
name: account-takeover
description: >
  Use when chaining authorized findings into full account takeover — combining
  auth/identity, OAuth/SSO, reset, and injection flaws into a demonstrated ATO,
  and enumerating the common ATO paths. Covers path mapping, controlled proof and
  remediation. An umbrella skill that references the specific technique skills.
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

# Account Takeover (ATO) — Path Mapping (authorized testing)

Account takeover is usually a **chain**, not a single bug. This skill enumerates
the common ATO paths and helps combine primitives into a demonstrated takeover of
a test account — then feeds precise remediation. Each path links to its dedicated
skill.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Demonstrate ATO
> only on accounts you control.

## When to use
When individual findings exist and you need to establish whether they combine into
ATO, or to systematically test the known ATO vectors.

## Prerequisites
- Authorization + scope; test accounts. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate ATO paths** and test each via its skill:
   - Password-reset abuse (`auth-identity/password-reset-abuse`)
   - OAuth/SSO flaws & account linking (`api/oauth-oidc-abuse`)
   - MFA bypass (`auth-identity/mfa-bypass`)
   - Credential attacks / enumeration (`auth-identity/credential-attacks`)
   - Session hijack/fixation (`auth-identity/session-management`)
   - JWT forgery (`api/jwt-attacks`)
   - BOLA on the user object / email-change without re-auth (`api/bola`)
   - Stored XSS stealing session (`web/xss`)
   - Pre-account-takeover (claiming an unverified account before the victim)
2. **Chain primitives (core gate)** — combine partial findings into a complete,
   repeatable takeover of a **test** victim.
3. **Document the chain** — the exact steps from unauthenticated to full control.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the chain, and the proof
of control over the test victim account. A partial step that doesn't complete →
**inconclusive** for ATO.

## Impact escalation
Full account control (data, actions, funds), and at scale if the chain is generic.
Critical. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Individual low findings that don't actually chain → report separately, not as ATO.
- Only use test accounts for end-to-end proof.

## Remediation
- Fix each primitive per its skill; additionally: re-authenticate for sensitive
  identity changes (email/password/MFA), verify email ownership before privileges,
  invalidate sessions on security changes, and monitor/alert on ATO-indicative
  patterns.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
