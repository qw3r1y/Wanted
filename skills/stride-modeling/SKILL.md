---
name: stride-modeling
description: >
  Use when threat-modeling a system with STRIDE — enumerating Spoofing, Tampering,
  Repudiation, Information disclosure, Denial of service, and Elevation of privilege
  threats per component/flow, and deriving mitigations. Covers structured threat
  enumeration.
type: knowledge
domain: appsec/threat-modeling
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# STRIDE Threat Modeling

Systematically enumerate threats to a design before it ships: for each component,
data flow, and trust boundary, ask which of Spoofing / Tampering / Repudiation /
Information disclosure / DoS / Elevation-of-privilege applies, then derive
mitigations and prioritize by risk.

## When to use
During design/architecture of a new or changing system; best paired with a DFD
(data-flow-diagram).

## Procedure (gated phases)
1. **Decompose** — build/obtain a DFD: components, data flows, data stores, external
   entities, and trust boundaries.
2. **Enumerate (STRIDE)** — walk each element/flow and list applicable STRIDE
   threats; focus on trust-boundary crossings.
3. **Rate & prioritize** — likelihood × impact; identify the highest risks.
4. **Mitigate** — map each significant threat to a concrete mitigation/control and
   owner.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: prioritized threats + mitigations
tied to design elements.

## Quality bar / pitfalls
- Hand-waving ("we'll be secure") vs concrete per-element threats.
- Modeling everything equally — focus on trust boundaries + high-value assets.

## Linkage
- Feeds secure-coding/authz, detection requirements, and test cases (offensive/*).

## References
- `_shared/` rules (evidence).
