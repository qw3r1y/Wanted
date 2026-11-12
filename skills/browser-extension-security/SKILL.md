---
name: browser-extension-security
description: >
  Use when auditing a browser extension — excessive permissions, content-script
  injection risks, insecure messaging, and data handling — that can expose users'
  browsing/data. Covers extension security review.
type: knowledge
domain: endpoint-app-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Browser Extension Security

Extensions run with powerful access to users' browsing — pages, cookies, requests —
so flaws (or malice) are high-impact. Audit an extension for excessive permissions,
unsafe content-script/DOM handling, insecure message passing, and data exfiltration
risk.

> Authorized review (`_shared/scope-authorization-rule.md`).

## When to use
Auditing an extension you build or vet one before deployment.

## Procedure (gated phases)
1. **Permissions review** — are requested permissions least-privilege, or over-broad
   (`<all_urls>`, tabs, webRequest)? Excess = larger blast radius.
2. **Content-script safety** — DOM injection/handling; does untrusted page content
   reach dangerous sinks (XSS in the extension context)?
3. **Messaging** — content↔background↔external messaging authenticated/validated?
   Can a web page message the extension to abuse its privileges?
4. **Data handling** — what user/browsing data it collects, where it sends it, and
   how it's protected.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record findings (excess perms, injection,
unsafe messaging, data exfil) + impact.

## Impact escalation
Browsing/data theft, request manipulation, and credential access across sites.
CVSS per `_shared/cvss-reference.md`.

## Remediation
- Least-privilege permissions; sanitize untrusted content; validate/authenticate
  messaging; minimize + protect data; CSP for the extension; Manifest V3 best
  practices.

## References
- `_shared/` rules (authorization, evidence).
