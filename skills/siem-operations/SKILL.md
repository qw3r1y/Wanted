---
name: siem-operations
description: >
  Use when operating a SIEM — log-source onboarding, data-model normalization,
  parser/field health, retention, and ensuring the telemetry detections depend on
  actually exists and is reliable. Covers the operational backbone under detection
  engineering.
type: knowledge
domain: defensive/blue-team-ops
maturity: canonical
tools: [splunk, elastic, sentinel]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# SIEM Operations & Log Onboarding

Keep the SIEM's data layer healthy so detections have what they need: onboard the
right log sources, normalize to the data model, verify parsing/field extraction,
manage retention/cost, and catch telemetry gaps before they become detection blind
spots.

## When to use
When standing up/maintaining a SIEM, onboarding new sources, or diagnosing "the
rule didn't fire" (often a telemetry/parsing problem).

## Procedure (gated phases)
1. **Source inventory & priority** — which log sources matter for the threat model
   (EDR, auth, DNS, proxy, cloud, OS); prioritize high-value telemetry.
2. **Onboard & normalize** — ingest, map to the data model/CIM/ECS, verify parsing
   and field extraction on real events.
3. **Health monitoring** — detect silent source outages (no events), parsing
   breakage, and volume anomalies.
4. **Retention & cost** — tune retention/tiering to meet detection + investigation
   needs within budget.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = required telemetry is ingested,
parsed, and monitored for outages. Record source health.

## Quality bar / pitfalls
- Detections built on absent/broken telemetry (silent misses) — verify fields
  exist end-to-end.
- Unmonitored source outages create blind spots.

## Governance
- Source-health dashboards + alerting on ingestion gaps; map sources to detection
  coverage.

## References
- `_shared/` rules (evidence).
