---
name: iso27001-isms
description: >
  Use when building/assessing an ISO 27001 Information Security Management System —
  risk-based control selection (Annex A), the ISMS process, and certification
  readiness. Covers ISO 27001 implementation.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# ISO 27001 ISMS

ISO 27001 is a risk-based management system, not a checklist: establish an ISMS that
identifies risks, selects controls (Annex A / Statement of Applicability) to treat
them, and continually improves. Build the process + evidence for certification.

> Implementation guidance; certification is by an accredited body.

## When to use
When implementing/maturing an ISMS or pursuing ISO 27001 certification.

## Procedure (gated phases)
1. **Scope & context** — ISMS scope, interested parties, and objectives.
2. **Risk assessment & treatment (core)** — identify/assess information-security
   risks; select controls to treat them; document the Statement of Applicability
   (why each Annex A control is included/excluded).
3. **Implement controls** — the selected technical + organizational controls with
   evidence.
4. **Operate & improve** — internal audits, management review, corrective actions —
   the continual-improvement cycle.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Ready" = a risk-driven ISMS with implemented
controls, SoA, and the operating management process.

## Quality bar / pitfalls
- Treating Annex A as a checklist vs risk-driven selection.
- Documentation without an operating ISMS (audits/reviews/improvement).

## Linkage
- Built on risk-assessment; consumes technical controls; feeds metrics + policy.

## References
- `_shared/` rules (evidence).
