---
name: behavioral-hunting
description: >
  Use when hunting for attacker behaviours rather than known IOCs — anomaly and
  TTP-based hunting (living-off-the-land, lateral movement, beaconing, persistence)
  using baselines and behavioural analytics. Catches novel/unknown threats IOCs
  miss.
type: knowledge
domain: defensive/threat-hunting
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Behavioral Threat Hunting

Hunt for how attackers act, not just what they've used before — LOLBin abuse,
anomalous parent-child processes, lateral movement, beaconing, and persistence —
using baselines and behavioural analytics. This catches novel threats that
signature/IOC hunting misses.

## When to use
To find unknown/novel threats, complementing ioc-hunting, prioritized by ATT&CK
and crown-jewel exposure.

## Procedure (gated phases)
1. **Pick a behaviour** — a TTP class (e.g., beaconing, LOLBin execution, unusual
   authentication) with an observable pattern.
2. **Baseline** — establish "normal" for the relevant metric (process lineage,
   connection periodicity, auth patterns).
3. **Analytic** — build an analytic that surfaces deviations from baseline (stack
   counting, rare combinations, periodicity detection).
4. **Triage & pivot** — investigate outliers; separate benign anomalies from
   malicious; pivot to scope; operationalize good analytics into detections.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record outliers with `verdict`; a deviation
is a lead, confirmed only with corroborating evidence.

## Quality bar / pitfalls
- High benign-anomaly noise — baseline well and stack-rank.
- Over-broad behavioural analytics → fatigue; refine iteratively.

## Governance
- Convert effective analytics to detections; document gaps; track hunt outcomes.

## References
- `_shared/` rules (evidence).
