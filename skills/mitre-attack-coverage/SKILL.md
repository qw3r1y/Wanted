---
name: mitre-attack-coverage
description: >
  Use when driving a hunting program with ATT&CK — prioritizing hunts by technique
  relevance and current detection/telemetry coverage, and tracking the program's
  maturity over time. Links hunting to coverage mapping and threat intel.
type: knowledge
domain: defensive/threat-hunting
maturity: canonical
tools: [attack-navigator]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# ATT&CK-Driven Hunt Prioritization

Use MITRE ATT&CK to decide what to hunt next: cross the techniques relevant to your
threat profile with where detection/telemetry coverage is weak, and hunt the
highest-risk, least-covered techniques first — turning hunting into a measurable,
prioritized program.

## When to use
When planning a hunting program or quarterly hunt backlog.

## Procedure (gated phases)
1. **Relevance** — from CTI/threat profile, weight techniques by likelihood against
   your org.
2. **Coverage cross-reference** — overlay current detection coverage (from
   detection-coverage-mapping) and telemetry availability.
3. **Prioritize** — rank hunts: high relevance + low coverage + available data
   first.
4. **Execute & update** — run hunts (hypothesis/behavioral/ioc), then update
   coverage with new detections produced.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a prioritized hunt backlog +
updated coverage after each hunt.

## Quality bar / pitfalls
- Hunting random techniques vs risk-prioritized ones — prioritize by relevance +
  gap.
- Not feeding results back into coverage — close the loop.

## Governance
- Track program maturity (techniques hunted/covered over time); align to adversary
  emulation.

## References
- `_shared/` rules (evidence).
