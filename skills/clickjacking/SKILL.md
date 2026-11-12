---
name: clickjacking
description: >
  Use when testing an authorized web target for clickjacking / UI redressing —
  sensitive actions framable by a malicious site due to missing frame-protection.
  Covers framing analysis, actionable-PoC assessment and remediation.
type: knowledge
domain: offensive/web
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

# Clickjacking / UI Redressing (authorized testing)

Find sensitive, state-changing pages that can be **framed** by an attacker site
(no `X-Frame-Options`/`frame-ancestors`), so a victim can be tricked into
clicking a hidden action. The finding requires both framability **and** a
meaningful one/few-click action — not just any framable page.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
Account/settings changes, delete/confirm actions, OAuth consent, fund actions,
"one-click" state changes — pages where a tricked click has impact.

## Prerequisites
- Authorization + scope; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Check frame protection (first gate)** — inspect `X-Frame-Options` and CSP
   `frame-ancestors`. Present/strict → **refuted**.
2. **Confirm framability** — build a minimal page that frames the target; confirm
   it renders inside the iframe (no frame-busting).
3. **Assess actionability** — identify a sensitive action reachable with a tricked
   click; confirm it is not independently protected (re-auth, token, confirmation
   that defeats blind clicking).
4. **PoC** — a benign redressing PoC (overlay/opacity) demonstrating the tricked
   action on a test account, stored in `OUTPUT_DIR`.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, missing header/CSP, the
framable sensitive action, and the PoC. Framable page with no sensitive action →
**low/informational**.

## Impact escalation
Unauthorized state changes (settings/account/consent), likes/follows abuse, and
combined with other flaws. CVSS per `_shared/cvss-reference.md` (often low–medium
unless high-value action).

## False positives & pitfalls
- `frame-ancestors 'none'`/`X-Frame-Options: DENY` → **refuted**.
- Action needs re-auth/confirmation that blocks blind clicks → low/none.
- A framable but read-only page → informational.

## Remediation
- Set `Content-Security-Policy: frame-ancestors 'none'` (or an explicit
  allow-list) and `X-Frame-Options: DENY`/`SAMEORIGIN` on sensitive pages.
- Require explicit confirmation/re-auth for high-value actions.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
