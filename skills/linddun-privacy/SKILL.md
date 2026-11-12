---
name: linddun-privacy
description: >
  Use when threat-modeling for privacy with LINDDUN — enumerating privacy threats
  (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure,
  Unawareness, Non-compliance) and deriving privacy controls. Covers privacy threat
  analysis.
type: knowledge
domain: appsec/threat-modeling
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# LINDDUN Privacy Threat Modeling

Model privacy threats the way STRIDE models security: walk the data flows and ask
where Linkability, Identifiability, Non-repudiation, Detectability, Disclosure,
Unawareness, or Non-compliance arise for personal data — then derive privacy
controls (minimization, anonymization, consent).

## When to use
For systems processing personal data, alongside security threat modeling.

## Procedure (gated phases)
1. **Map personal data flows** — where PII enters, flows, is stored, and leaves
   (DFD with data sensitivity).
2. **Enumerate (LINDDUN)** — per flow/store, identify applicable privacy threats.
3. **Prioritize** — by data sensitivity + likelihood + regulatory exposure.
4. **Derive controls** — data minimization, anonymization/pseudonymization, consent,
   retention limits (feeds data-privacy, grc).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: prioritized privacy threats +
controls.

## Quality bar / pitfalls
- Treating privacy as only "encrypt it" — address linkability/minimization/consent.
- Missing regulatory (GDPR/KVKK) implications.

## Linkage
- Feeds data-privacy/ and grc/ (gdpr-kvkk); complements STRIDE.

## References
- `_shared/` rules (evidence).
