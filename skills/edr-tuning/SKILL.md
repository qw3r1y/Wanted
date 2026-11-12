---
name: edr-tuning
description: >
  Use when tuning EDR/endpoint protection — policy configuration, detection/
  prevention balance, exclusion hygiene, and telemetry enablement — to maximize
  detection while controlling noise and avoiding dangerous exclusions. Covers
  policy and telemetry optimization.
type: knowledge
domain: defensive/blue-team-ops
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# EDR Tuning & Telemetry

Configure EDR so it detects/prevents real threats, emits the telemetry detection
engineering relies on, and keeps noise/exclusions under control — exclusions are a
common, dangerous blind spot that attackers abuse.

## When to use
After EDR deployment, during noise reduction, and when detection gaps trace to EDR
config/telemetry.

## Procedure (gated phases)
1. **Policy posture** — detection vs prevention mode per environment; enable
   behavioural protections (not just signatures).
2. **Telemetry enablement** — ensure the EDR forwards the events detections need
   (process, command-line, image load, network, AMSI/script).
3. **Exclusion hygiene (core)** — audit exclusions; remove overly broad ones;
   every exclusion is a potential blind spot — justify and scope each.
4. **Noise tuning** — reduce benign alerts via precise policy, not blanket
   exclusions; measure FP rate.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = behavioural protection on, needed
telemetry flowing, exclusions minimal/justified. Record config + exclusion audit.

## Quality bar / pitfalls
- Broad exclusions (whole dirs/processes) that attackers hide behind.
- Detection-only where prevention is warranted (or vice-versa) — match risk.

## Governance
- Periodic exclusion audits; telemetry validation vs detection needs; tamper
  protection enabled.

## References
- `_shared/` rules (evidence).
