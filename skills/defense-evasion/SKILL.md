---
name: defense-evasion
description: >
  Use when, in an authorized purple-team, mapping ATT&CK defense-evasion techniques
  to the organization's detection coverage — identifying which evasion behaviours
  would be caught vs missed. Coverage-gap and detection-engineering framing.
type: knowledge
domain: offensive/c2-redteam
maturity: canonical
tools: [atomic-red-team]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Defense-Evasion Coverage Mapping (authorized purple-team)

Map the MITRE ATT&CK **Defense Evasion** tactic to the organization's detections:
run representative (benign/atomic) evasion behaviours and record which the EDR/SIEM
catches. The deliverable is a coverage matrix and prioritized detection gaps.

> Authorized, coordinated testing only, with defenders aware
> (`_shared/scope-authorization-rule.md`). Benign/atomic tests; no real malware.

## Prerequisites
- Authorization + scope + blue-team coordination. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate techniques** — select in-scope Defense-Evasion techniques (e.g.,
   logging/AMSI tampering, LOLBins, masquerading) relevant to the environment.
2. **Execute (atomic)** — run benign atomic tests for each.
3. **Record coverage (core)** — detected/prevented/missed per technique, with the
   telemetry involved.
4. **Prioritize gaps** — feed detection-engineering.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: Defense-Evasion coverage matrix
with evidence.

## Impact escalation
Evasion blind spots let attackers operate undetected; closing them is high-value.

## False positives & pitfalls
- LOLBins have legitimate uses — detections need context/tuning.
- Benign/atomic only; coordinate to avoid IR confusion.

## Remediation
- Enable/monitor AMSI, ETW, script-block logging, command-line auditing; LOLBin
  behavioural detections; tamper-protection on logging/EDR; defense-in-depth.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
