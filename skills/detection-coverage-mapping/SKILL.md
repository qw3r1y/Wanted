---
name: detection-coverage-mapping
description: >
  Use when assessing and improving detection coverage against MITRE ATT&CK —
  mapping existing detections to techniques, finding gaps, and prioritizing new
  detections by threat relevance. Covers coverage analysis and prioritization.
type: knowledge
domain: defensive/detection-engineering
maturity: canonical
tools: [attack-navigator]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Detection Coverage Mapping (ATT&CK)

Know what you can and cannot detect: map every detection to the ATT&CK techniques
it covers, visualize coverage, find the gaps, and prioritize new detections by how
relevant the technique is to the organization's threats and data availability.

## When to use
Periodically, and after purple-team/incident findings, to steer the detection
roadmap.

## Procedure (gated phases)
1. **Inventory detections** — map each rule/query to ATT&CK technique(s) and the
   log source it needs.
2. **Assess quality, not just presence** — a technique "covered" by a weak/brittle
   rule is a partial gap; grade coverage.
3. **Find gaps** — techniques with no/weak detection, weighted by threat relevance
   (from CTI) and whether telemetry even exists.
4. **Prioritize** — a ranked backlog of detections to build (feeds sigma/siem
   authoring), accounting for data-source gaps.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: an ATT&CK coverage map (graded)
+ prioritized detection backlog.

## Quality bar / pitfalls
- "Coverage" based on rule existence, not efficacy — grade honestly.
- Ignoring missing telemetry — a detection needs its data source first.

## Governance
- Tie coverage to the threat profile (adversary-emulation, cti); track coverage
  trend over time.

## References
- `_shared/` rules (evidence).
