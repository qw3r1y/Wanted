---
name: siem-detection-queries
description: >
  Use when authoring SIEM-native detection queries (Splunk SPL, Elastic/KQL,
  Sentinel KQL) for a behaviour — field mapping, correlation, thresholds, and
  tuning for the platform. Complements sigma-rule-authoring (portable) with
  platform-optimized detections.
type: knowledge
domain: defensive/detection-engineering
maturity: canonical
tools: [splunk, elastic, sentinel]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# SIEM Detection Queries

Author platform-native detection logic that turns a behaviour into a reliable
alert — correct field mapping to the data model, correlation across events,
sensible thresholds, and tuning — optimized for the specific SIEM (Splunk/Elastic/
Sentinel).

## When to use
When implementing a detection on a specific SIEM, or optimizing a converted Sigma
rule for that platform's data model.

## Procedure (gated phases)
1. **Map to the data model** — identify the index/data source and the normalized
   fields carrying the observable.
2. **Write the query** — selection + correlation (joins/stats) for the behaviour;
   use the platform's efficient idioms.
3. **Thresholds & aggregation** — set thresholds/time windows to catch the
   behaviour while limiting noise.
4. **Tune** — test against historical data; exclude known benign; measure FP rate.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = detects on historical/test data
with acceptable FP rate and performance. Record results.

## Quality bar / pitfalls
- Inefficient queries that don't scale; wrong field mapping (silent misses).
- Thresholds that cause alert fatigue or miss low-and-slow activity.

## Deployment notes
- Stage, tune, document, and version; connect to the SOC playbook (blue-team-ops)
  and coverage mapping.

## References
- `_shared/` rules (untrusted input, evidence).
