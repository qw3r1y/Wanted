---
name: hipaa
description: >
  Use when implementing HIPAA Security Rule safeguards for protected health
  information (PHI) — administrative, physical, and technical safeguards and risk
  analysis. Covers HIPAA security implementation focus.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# HIPAA Security Rule

For organizations handling protected health information (PHI), the HIPAA Security
Rule requires administrative, physical, and technical safeguards driven by a risk
analysis. Implement and evidence these safeguards around where PHI is created,
stored, and transmitted.

> Implementation guidance; coordinate with compliance/legal.

## When to use
For healthcare/health-data organizations (covered entities/business associates).

## Procedure (gated phases)
1. **Risk analysis (core)** — identify where ePHI is and the risks to it (the Security
   Rule's foundation); document it.
2. **Technical safeguards** — access control, audit controls, integrity, transmission
   security (encryption), and authentication for ePHI.
3. **Administrative & physical** — policies, workforce training, access management,
   contingency/IR, and physical protection; Business Associate Agreements.
4. **Evidence & maintain** — document safeguards, risk analysis, and ongoing review.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Ready" = risk-analysis-driven safeguards
implemented + evidenced around ePHI.

## Quality bar / pitfalls
- Skipping/under-doing the risk analysis (the required foundation).
- Missing encryption of ePHI in transit/at rest; no BAAs with vendors.

## Linkage
- Consumes data-privacy (pii/phi discovery), encryption, access control, IR; feeds
  risk-assessment.

## References
- `_shared/` rules (evidence).
