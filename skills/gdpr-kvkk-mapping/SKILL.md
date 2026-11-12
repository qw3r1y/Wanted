---
name: gdpr-kvkk-mapping
description: >
  Use when mapping data-protection regulatory requirements (GDPR, KVKK, and similar)
  to technical/organizational controls — data subject rights, lawful basis,
  breach notification, and records — translating law into implementation. Covers
  privacy-compliance mapping.
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# GDPR / KVKK Requirement Mapping

Translate data-protection law (EU GDPR, Turkey's KVKK, and similar) into concrete
technical and organizational controls — so compliance is implemented, not just
documented: lawful basis, data-subject rights, security measures, breach
notification, and records of processing.

> Implementation guidance; not legal advice — coordinate with counsel/DPO.

## When to use
When operationalizing data-protection compliance for a system/organization.

## Procedure (gated phases)
1. **Map data processing** — what personal data is processed, why, lawful basis, and
   data flows (from pii-discovery/data map).
2. **Map rights to capability** — access, rectification, erasure, portability,
   objection → the technical ability to fulfill each (e.g., find+delete a subject's
   data).
3. **Security & breach** — appropriate technical measures (encryption, access
   control, minimization) and a breach-notification process (timelines).
4. **Records & governance** — records of processing, DPIAs for high-risk, vendor/
   processor agreements.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a requirement→control mapping
with gaps + implementation plan.

## Quality bar / pitfalls
- Paper compliance without the technical ability to fulfill rights (e.g., can't
  actually delete a subject's data everywhere).
- Treating as pure legal exercise — implement controls.

## Linkage
- Consumes pii-discovery/classification/anonymization; feeds grc.

## References
- `_shared/` rules (evidence).
