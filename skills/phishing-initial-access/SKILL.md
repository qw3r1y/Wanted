---
name: phishing-initial-access
description: >
  Use when running an authorized phishing-simulation / initial-access exercise —
  scenario design, infrastructure, delivery, and measuring click/report/credential
  rates and detection — to improve awareness and email defenses. Simulation and
  awareness framing, coordinated and consented.
type: knowledge
domain: offensive/c2-redteam
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

# Phishing Simulation / Initial-Access Exercise (authorized)

Run an authorized phishing simulation to measure human and technical resilience —
click rate, credential-submission rate, report rate, and whether email/endpoint
controls catch it — to drive awareness training and email-defense tuning. Consent
and coordination are mandatory; the goal is improvement, not entrapment.

> Authorized, coordinated testing only, per organizational policy and consent
> (`_shared/scope-authorization-rule.md`). Handle any collected data per rules;
> no real credential capture beyond the sanctioned metric.

## Prerequisites
- Authorization + scope + management approval + policy alignment; a simulation
  platform. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Design scenario** — pretext, target segment, and objective (click vs
   credential vs attachment); align difficulty to goals.
2. **Infrastructure & delivery** — approved sending domain/landing; ensure the
   simulation is clearly bounded and tracked.
3. **Measure (core)** — click/submission/report rates, time-to-report, and whether
   email/endpoint controls detected/blocked it.
4. **Report & train** — results + awareness training + email-defense improvements
   (feeds social-engineering/awareness-training, email-security).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: simulation metrics +
detection results. Aggregate reporting; respect employee privacy.

## Impact escalation
Quantifies phishing risk and control efficacy; drives measurable improvement.

## False positives & pitfalls
- Coordinate to avoid real IR/alarm; follow consent/policy.
- Report aggregate, not punitive individual data.

## Remediation
- Awareness training; easy "report phish" button + response; email authentication
  (DMARC/SPF/DKIM) + gateway tuning; MFA + phishing-resistant auth.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
