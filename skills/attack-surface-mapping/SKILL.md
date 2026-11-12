---
name: attack-surface-mapping
description: >
  Use when prioritizing where to hunt on a target — mapping the discovered surface to
  likely-vulnerable functionality and matching it to vuln classes, so testing is
  targeted rather than random. Covers hunting prioritization.
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Attack Surface Mapping (hunting)

Recon gives breadth; this turns it into a targeted plan. Map the discovered surface
to the functionality most likely to be vulnerable and valuable — auth flows, file
handling, integrations, admin features — and match each to the vuln-class skills, so
you hunt deliberately where payouts are.

> In-scope only (`_shared/scope-authorization-rule.md`).

## When to use
After recon, to decide what to test and how.

## Procedure (gated phases)
1. **Inventory functionality** — the features behind the surface (auth, uploads,
   search, APIs, integrations, admin, payments).
2. **Match to vuln classes (core)** — for each feature, the plausible classes (uploads
   → file-upload/XXE; auth → idor/auth-bypass/jwt; search → sqli/xss; redirects →
   open-redirect/ssrf), prioritizing high-impact.
3. **Prioritize** — crown-jewel functionality (auth, payments, admin, multi-tenant)
   and areas others likely skipped.
4. **Hunt** — apply the matched offensive/* skills.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a feature→vuln-class hunting plan.

## Impact / output
Targeted, efficient hunting on high-value surface.

## Pitfalls
- Random payload-throwing vs mapped, deliberate testing.
- Ignoring business-logic (high-value, tool-invisible).

## Linkage
- Consumes recon-workflow; drives the offensive/web + api + auth skills.

## References
- `_shared/` rules (authorization, evidence).
