---
name: soc-playbook-authoring
description: >
  Use when writing SOC incident/alert response playbooks — standardized triage,
  investigation, containment, and escalation steps for an alert type — to make
  response consistent, fast, and auditable. Covers playbook structure and quality.
type: knowledge
domain: defensive/blue-team-ops
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# SOC Playbook Authoring

Write response playbooks that turn an alert type into consistent, repeatable
action: how to triage, what to investigate, how to contain, when to escalate, and
what to document — reducing analyst variance and response time.

## When to use
For each major alert/incident type, and when standardizing/maturing SOC response.

## Procedure (gated phases)
1. **Scope the alert type** — the trigger, likely true/false-positive causes, and
   severity criteria.
2. **Triage steps** — concrete first checks to validate/dismiss, with decision
   points (gated: confirm before containment).
3. **Investigation** — the data to pull, pivots to make, and what "confirmed"
   looks like (ties to evidence rule).
4. **Containment & escalation** — bounded containment actions, escalation criteria/
   contacts, and required documentation.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = an analyst can execute it
consistently; test on a real/simulated alert.

## Quality bar / pitfalls
- Vague steps ("investigate the alert") — be concrete and decision-driven.
- Containment without a confirmation gate — avoid disrupting on false positives.

## Governance
- Version playbooks; review after incidents; link to detections and SOAR
  automation where applicable (soar).

## References
- `_shared/` rules (evidence, gated workflow).
