---
name: av-edr-evasion
description: >
  Use when, in an authorized red/purple-team engagement, evaluating EDR/AV
  detection efficacy — understanding what detection surfaces exist and where
  coverage gaps are, to improve defenses. Detection-efficacy and blue-team-
  improvement framing, not operational evasion tooling.
type: knowledge
domain: offensive/post-exploitation
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# EDR/AV Detection-Efficacy Evaluation (authorized purple-team)

In an authorized, coordinated purple-team exercise, evaluate how well the
organization's EDR/AV detects attacker techniques and where coverage gaps are — so
detection engineering can close them. The objective is **improving detection**, not
building operational evasion; work with the defensive team.

> Authorized, coordinated testing only, with the blue team aware
> (`_shared/scope-authorization-rule.md`). The deliverable is detection gaps +
> fixes, not evasion tooling.

## Prerequisites
- Authorization + scope + blue-team coordination; a lab/representative environment.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Map detection surfaces** — the telemetry EDR relies on (process/command-line,
   image loads, AMSI, ETW, network, file) for the techniques in scope.
2. **Technique coverage test (core)** — run in-scope ATT&CK techniques (benign/
   atomic) and observe whether they alert; note what detects vs misses.
3. **Gap analysis** — where detection is missing or weak, document the gap and the
   telemetry that would catch it.
4. **Hand to detection engineering** — turn gaps into detections (feeds
   defensive/detection-engineering).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a coverage matrix (technique →
detected/missed) with evidence.

## Impact escalation
Detection gaps = blind spots an attacker exploits; closing them hardens defense.

## False positives & pitfalls
- Coordinate with blue team; this is efficacy testing, not covert evasion.
- Use benign/atomic tests; avoid real malware.

## Remediation
- Build/tune detections for gaps; enable missing telemetry (command-line, AMSI,
  ETW); defense-in-depth; continuous purple-teaming.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
