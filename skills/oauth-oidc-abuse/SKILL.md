---
name: oauth-oidc-abuse
description: >
  Use when testing an authorized OAuth2/OIDC implementation for flow flaws —
  redirect_uri validation gaps, state/CSRF, code/token leakage, PKCE absence,
  scope/consent abuse, and implicit-flow token theft. Covers flow mapping,
  controlled proof and remediation.
type: knowledge
domain: offensive/api
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

# OAuth2 / OIDC Abuse (authorized testing)

Test the authorization/token flow for the classic failures that lead to account
takeover: loose `redirect_uri` validation (token/code exfiltration), missing/
unbound `state` (login CSRF), code leakage/reuse, absent PKCE on public clients,
and over-broad scope/consent. The proof is obtaining or redirecting a token/code
you should not.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Use test
> accounts and attacker origins you control.

## When to use
Any "Sign in with…" / OAuth2 / OIDC integration, first-party or third-party IdP
flows within scope.

## Prerequisites
- Authorization + scope; test accounts; an attacker-controlled redirect host.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Map the flow** — grant type (auth-code/PKCE/implicit), parameters
   (`redirect_uri`, `state`, `scope`, `response_type`), and where code/token land.
2. **redirect_uri validation (core gate)** — test whether non-exact redirect URIs
   are accepted (subdomain, path, `@`, open-redirect chain) → code/token can be
   sent to an attacker origin.
3. **state / PKCE / code** — is `state` present and bound (CSRF)? PKCE enforced on
   public clients? Is an auth code single-use and short-lived (replay)?
4. **Scope/consent** — can scopes be escalated or consent bypassed? Implicit flow
   leaking tokens in URL/referrer?

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the flaw, and the proof
(token/code delivered to attacker origin, or CSRF login on a test account). Exact
redirect match + bound state + PKCE → **refuted** for those.

## Impact escalation
Account takeover via code/token theft, login CSRF (account linking), and scope
escalation. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Exact `redirect_uri` match → redirect attacks **refuted**.
- `state` bound to session → CSRF **refuted**.
- Keep flows on test accounts only.

## Remediation
- **Exact-match** `redirect_uri` allow-list; enforce `state` bound to the session;
  require **PKCE** for public clients; single-use short-lived codes; avoid implicit
  flow.
- Least-privilege scopes with explicit consent; never put tokens in URLs.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
