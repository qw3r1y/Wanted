---
name: phishing-campaign
description: >
  Use when designing an authorized phishing/social-engineering simulation campaign —
  pretext design, target segmentation, difficulty calibration, and ethical/consent
  guardrails — to measure and improve human resilience. Simulation-design focus;
  overlaps c2-redteam/phishing-initial-access (this one is campaign/pretext design).
type: knowledge
domain: offensive/social-engineering
maturity: canonical
tools: [gophish]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Phishing Campaign Design (authorized simulation)

Design the pretext and structure of an authorized phishing-simulation campaign that
is realistic enough to measure resilience but ethical and consented — segmenting
targets, calibrating difficulty, and planning the learning outcome. The deliverable
is a campaign plan; execution/metrics live in
c2-redteam/phishing-initial-access.

> Authorized, consented simulation only, per policy
> (`_shared/scope-authorization-rule.md`). Design for improvement, not entrapment;
> protect participant privacy.

## Prerequisites
- Authorization + management approval + policy. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Objective & segments** — define what to measure (awareness, specific lure
   susceptibility) and the target segments.
2. **Pretext design** — craft realistic, policy-compliant pretexts calibrated to
   difficulty; avoid harmful/sensitive themes.
3. **Learning plan** — pair the campaign with immediate training on interaction;
   plan aggregate, non-punitive reporting.
4. **Guardrails** — consent, scope, data handling, and escalation paths.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: an approved campaign plan ready
for execution.

## Impact escalation
Drives measurable awareness improvement and highlights high-risk segments/lures.

## False positives & pitfalls
- Overly harsh/sensitive pretexts harm trust — keep ethical.
- Aggregate, non-punitive outcomes; respect privacy.

## Remediation
- Continuous awareness training; report-phish culture; technical email defenses;
  phishing-resistant MFA.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
