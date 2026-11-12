---
name: membership-inference
description: >
  Use when assessing an ML model for membership-inference / data-privacy leakage —
  whether an attacker can determine if a specific record was in the training data,
  risking privacy. Covers membership-inference risk and mitigations.
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

# Membership Inference

Models can leak whether a specific record was in their training set — a privacy
violation (e.g., inferring someone was in a medical-study dataset). Assess the model's
susceptibility (often tied to overfitting and output confidence) and mitigate with
privacy-preserving training.

> Authorized assessment of your own/in-scope model (`_shared/scope-authorization-rule.md`).

## When to use
For models trained on sensitive/personal data where membership is itself sensitive.

## Procedure (gated phases)
1. **Assess susceptibility** — overfitting (big train/test gap) and rich confidence
   outputs increase membership leakage; evaluate the model's behavior on members vs
   non-members.
2. **Test (where feasible)** — can a distinguisher tell members from non-members from
   model outputs?
3. **Privacy impact** — what membership reveals given the dataset's sensitivity.
4. **Mitigate** — reduce overfitting (regularization), limit output confidence,
   differential privacy in training, and limit query access.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record susceptibility + privacy impact.

## Impact escalation
Privacy violation (membership disclosure), regulatory exposure for sensitive datasets.
CVSS/impact per `_shared/cvss-reference.md`.

## Defenses
- Differential privacy in training; reduce overfitting; limit output detail + query
  access; assess before deploying models on sensitive data.

## References
- `_shared/` rules (authorization, evidence).
