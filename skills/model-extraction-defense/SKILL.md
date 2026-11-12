---
name: model-extraction-defense
description: >
  Use when assessing/defending an ML model against extraction/theft — attackers
  querying a model to replicate it or recover its parameters/training data. Covers
  model-theft threats and defenses (distinct from LLM prompt attacks).
type: knowledge
domain: ml-model-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Model Extraction / Theft Defense

A deployed ML model exposed via an API can be **stolen**: an attacker queries it
systematically to train a replica (stealing IP) or to approximate its parameters.
Assess the exposure (query access, output richness) and defend with rate limiting,
output restriction, and monitoring.

> Authorized assessment of your own/in-scope model (`_shared/scope-authorization-rule.md`).

## When to use
For ML models exposed via API/prediction endpoints where the model is valuable IP.

## Procedure (gated phases)
1. **Assess exposure** — query access, output richness (full probabilities/confidence
   leak more than top-1 labels), and rate limits.
2. **Extraction risk** — how feasible is replication given the query budget and output
   detail? High-detail outputs + unlimited queries = high risk.
3. **Defenses** — restrict output detail (labels not full confidence vectors), rate-
   limit/authenticate queries, add query monitoring/anomaly detection, and watermark
   the model.
4. **Monitor** — detect systematic/extraction-pattern querying.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record extraction feasibility + defenses.

## Impact escalation
IP theft (replicated model), and extracted models enabling further attacks (evasion).
CVSS/impact per `_shared/cvss-reference.md`.

## Defenses
- Minimal output detail; authenticated + rate-limited queries; query-pattern
  monitoring; model watermarking; legal/ToS controls.

## References
- `_shared/` rules (authorization, evidence).
