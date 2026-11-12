---
name: adversarial-examples
description: >
  Use when assessing an ML model's robustness to adversarial examples — crafted
  inputs with imperceptible perturbations that cause misclassification — especially
  for security-relevant models (malware, fraud, vision). Covers evasion-robustness
  assessment.
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

# Adversarial Examples / Evasion Robustness

ML models can be fooled by inputs with small, crafted perturbations — a malware
sample tweaked to classify as benign, a fraud transaction evading detection, or a
vision model misreading a sign. Assess how robust a security-relevant model is to
such evasion and harden it.

> Authorized assessment of your own/in-scope model (`_shared/scope-authorization-rule.md`).

## When to use
For models used in security/safety decisions (malware/fraud/abuse/vision) where
evasion has real impact.

## Procedure (gated phases)
1. **Identify the decision & threat** — what the model decides and the attacker's
   goal (evade detection/classification).
2. **Assess robustness** — can bounded perturbations (within the attacker's control)
   flip the decision? Evaluate with adversarial test inputs.
3. **Impact** — evasion of the security control the model provides.
4. **Harden** — adversarial training, input preprocessing/detection, ensembles, and
   not relying solely on the model for security decisions.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record robustness findings + impact.

## Impact escalation
Bypass of ML-based security controls (malware/fraud/abuse detection). CVSS/impact per
`_shared/cvss-reference.md`.

## Defenses
- Adversarial training + robustness evaluation; defense-in-depth (don't rely only on
  the ML model); input anomaly detection; monitor for evasion patterns.

## References
- `_shared/` rules (authorization, evidence).
