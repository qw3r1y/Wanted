---
name: csrf
description: >
  Use when testing an authorized web target for Cross-Site Request Forgery —
  state-changing requests that may be forced from another origin because they
  lack anti-CSRF protection or rely on bypassable defenses. Covers token
  analysis, SameSite/defense assessment, PoC construction and remediation. Do
  NOT use for read-only endpoints or where impact is purely client-side (XSS).
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

# CSRF — Cross-Site Request Forgery (authorized testing)

Find **state-changing** requests that the server executes using the victim's
ambient session when triggered from an attacker-controlled origin. The proof is a
cross-origin request that performs the action **without** a secret the attacker
could not know (a valid, unpredictable, bound anti-CSRF token or an equivalent
defense).

> Authorized testing only (`_shared/scope-authorization-rule.md`). Demonstrate
> with a benign state change on a test account; get per-action approval for any
> real change (`safe-execution-rules.md`).

## When to use
Any authenticated, state-changing action: profile/email/password change, fund/
settings changes, create/delete resources, role changes, add-collaborator, OAuth
connect. Both form-encoded and JSON endpoints — JSON is not automatically safe.

## Prerequisites
- Authorization + scope recorded; use **test accounts** for the PoC.
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)

### Phase 1 — Identify state-changing requests
Catalogue actions and capture each request (method, body, headers, cookies).
Mark which carry a token or custom header.

### Phase 2 — Defense analysis (first gate)
Assess each protection and whether it actually holds:
| Defense | Bypass to test |
|---|---|
| Anti-CSRF token | Is it present, **unpredictable**, **bound to the session/user**, and **validated**? Try removing it, reusing another user's, empty value, or wrong method |
| SameSite cookies | `Lax`/`Strict` vs `None`; top-level GET navigations under `Lax`; subdomain/`None` gaps |
| Custom header requirement | Reachable via simple-request/form? CORS misconfig enabling it? |
| Origin/Referer check | Absent, optional, or bypassable (null origin, substring match)? |
| Double-submit cookie | Cookie attacker-settable (subdomain) → bypass |

### Phase 3 — Build a minimal PoC
If a protection is missing/bypassable, construct the **minimum** cross-origin
request (auto-submitting form for form-encoded; appropriate vector for JSON if
the content-type can be forged) that performs a benign action on a test account.
Keep the PoC self-contained in `OUTPUT_DIR`.

### Phase 4 — Confirm execution
Trigger the PoC while authenticated as the test victim; confirm the action
occurred server-side (state changed). That is the confirmation.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the defended/bypassed
mechanism, the PoC, and the observed state change. A missing token on a
**read-only** request is not CSRF.

## Impact escalation
Account takeover (email/password change), privilege/role change, fund transfer,
settings tampering, and CSRF-chained with other bugs. Severity scales with the
action. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Endpoint requires a secret/token the attacker cannot forge → **refuted**.
- `SameSite=Lax` (default on modern browsers) blocks many cross-site cookie
  sends — verify the actual browser behaviour, don't assume.
- JSON endpoints requiring `application/json` + a custom header are often not
  CSRF-able unless CORS/preflight is misconfigured.

## Remediation
- Per-session, unpredictable **anti-CSRF tokens** bound to the user and validated
  server-side on every state-changing request; or the synchronizer/double-submit
  pattern done correctly.
- `SameSite=Lax` (or `Strict`) on session cookies; verify `Origin`/`Referer` on
  sensitive actions as defense-in-depth.
- Require non-simple content types + custom headers for state-changing APIs and
  keep CORS strict.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
