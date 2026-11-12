---
name: adversary-emulation
description: >
  Use when planning/running an authorized adversary-emulation or purple-team
  exercise — selecting a threat profile, mapping its TTPs to ATT&CK, executing
  representative (benign/atomic) techniques, and measuring detection/response.
  Detection-improvement framing, coordinated with defenders.
type: knowledge
domain: offensive/c2-redteam
maturity: canonical
tools: [atomic-red-team, caldera]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Adversary Emulation / Purple Team (authorized)

Plan and run an authorized exercise that emulates a chosen threat actor's behaviour
to measure and improve detection and response. The deliverable is a detection/
response scorecard and prioritized gaps — not a covert compromise. Work with the
blue team throughout.

> Authorized, coordinated testing only (`_shared/scope-authorization-rule.md`).
> Use benign/atomic techniques; defenders are aware (`safe-execution-rules.md`).

## Prerequisites
- Authorization + scope + blue-team coordination; a threat profile + target
  environment. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Select & map** — choose a threat profile relevant to the org; map its TTPs to
   MITRE ATT&CK; define objectives and rules of engagement.
2. **Execute (benign/atomic)** — run representative techniques across the kill chain
   (initial access → actions on objectives) using atomic/benign tests.
3. **Measure** — for each technique, record detection (alerted?), prevention
   (blocked?), and response (investigated?).
4. **Report & improve** — a coverage scorecard + prioritized detection/response
   gaps (feeds detection-engineering, threat-hunting).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: ATT&CK-mapped
detect/prevent/respond scorecard with evidence.

## Impact escalation
Identifies real detection/response gaps against relevant threats; drives concrete
blue-team improvements.

## False positives & pitfalls
- Coordinate to avoid real IR confusion; benign/atomic only.
- Emulate behaviour, don't just run tools — map to TTPs.

## Remediation
- Close detection/prevention/response gaps per technique; iterate purple-team
  regularly; align with the threat landscape (cti).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
