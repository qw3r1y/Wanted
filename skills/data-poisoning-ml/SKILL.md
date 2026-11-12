---
name: data-poisoning-ml
description: >
  Use when assessing/defending ML training pipelines against data poisoning —
  malicious training data that degrades the model or implants backdoors/triggers.
  Covers training-data integrity and poisoning defenses.
type: knowledge
domain: ml-model-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Data Poisoning (ML)

If an attacker influences training data, they can degrade a model or implant a
**backdoor** — a hidden trigger that causes attacker-chosen behavior. This matters
most where training data comes from untrusted/public sources or user feedback.
Assess the training pipeline's data integrity and defend it.

## When to use
For ML systems that train/retrain on external, user-contributed, or crowd-sourced
data.

## Procedure (gated phases)
1. **Map data provenance** — where training data comes from, and which sources are
   untrusted/attacker-influenceable (feedback loops, public datasets, scraped data).
2. **Poisoning risk** — can injected data degrade performance or implant a backdoor
   trigger? Assess data validation/curation.
3. **Backdoor detection** — test for trigger-based anomalous behavior; monitor for
   data/label anomalies.
4. **Defend** — vet/curate data sources, anomaly-detect training data, validate
   labels, and monitor model behavior post-training.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record provenance risks + any backdoor/
poisoning indicators.

## Impact escalation
Degraded model, or a backdoor giving attacker-controlled behavior on a trigger.
CVSS/impact per `_shared/cvss-reference.md`.

## Defenses
- Trusted/curated training data; data + label anomaly detection; provenance tracking;
  robust training; post-training behavior validation; secure the data pipeline
  (supply-chain thinking for ML).

## References
- `_shared/` rules (evidence).
