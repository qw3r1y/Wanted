---
name: open-redirect
description: >
  Use when testing an authorized web target for open redirect — input that
  controls a redirect destination, enabling phishing, token leakage via redirect,
  or as a gadget in SSRF/OAuth/CSP chains. Covers detection, bypass analysis,
  impact and remediation.
type: knowledge
domain: offensive/web
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

# Open Redirect (authorized testing)

Find input that sets a redirect target and prove the app sends users to an
attacker-chosen external origin. On its own it is usually low–medium (phishing),
but it is a powerful **gadget**: OAuth `redirect_uri` token theft, SSRF pivot, or
CSP/filter bypass.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
`?redirect=`, `?return_url=`, `?next=`, `?url=`, `?dest=`, login/logout flows,
OAuth `redirect_uri`, and post-action "continue to" links.

## Prerequisites
- Authorization + scope; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Find redirect params** — observe a legitimate redirect; note Location header
   or JS/meta redirect.
2. **External-target probe (first gate)** — set the target to a benign external
   host you control; confirm the app issues a redirect to it (Location/JS).
3. **Bypass analysis** — where a filter restricts to same-site, test allow-list
   gaps: scheme-relative (`//host`), backslash/encoding tricks, `@`-userinfo,
   substring/suffix matching, whitelisted-domain-as-prefix.
4. **Chain assessment** — if an OAuth/SSO flow or token is carried, assess token
   leakage to the external origin; if it feeds a server fetch, link to ssrf.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the redirecting param,
the bypass used, and the observed external redirect. A same-site-only redirect →
**refuted** for external impact.

## Impact escalation
Phishing (trusted-domain redirect), OAuth/SSO token theft via `redirect_uri`,
SSRF/filter-bypass gadget, and CSP bypass. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Strict allow-list to same origin → **refuted**.
- Redirect to a relative path only → not open redirect.
- Reflected but not followed (no Location/JS redirect) → not exploitable.

## Remediation
- Redirect only to a **server-side allow-list** of paths/origins; never redirect
  to a raw user-supplied URL.
- Use relative paths/tokens mapped server-side; validate the full parsed URL
  (scheme+host) after decoding; strict OAuth `redirect_uri` exact-match.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
