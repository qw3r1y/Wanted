---
name: timeline-analysis
description: >
  Use when building and analyzing a forensic timeline — correlating artifacts from
  multiple sources (disk, memory, logs) into a unified chronology (super-timeline)
  to reconstruct the attack sequence. Covers timeline creation, pivoting, and
  anchoring.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: [plaso]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Forensic Timeline Analysis

Merge artifacts from disk, memory, and logs into a single chronological picture to
answer when and in what order the attack unfolded — initial access, execution,
lateral movement, and actions on objectives — anchored to corroborated events.

## When to use
During IR to establish the sequence/dwell time and to connect disparate artifacts.

## Procedure (gated phases)
1. **Collect sources** — filesystem metadata, execution artifacts, event logs,
   memory findings; normalize timestamps/timezones.
2. **Build the super-timeline** — generate a unified chronology; filter to the
   incident window to manage volume.
3. **Anchor & pivot** — fix key events (initial access, first execution) and pivot
   around them to find related activity.
4. **Reconstruct the sequence** — produce the ordered attack narrative with
   evidence per step.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each timeline claim cites its artifact
source; flag timestomping and timezone pitfalls.

## Impact / output
The incident chronology + dwell time (feeds reporting, IR decisions, scoping).

## Pitfalls
- Timezone/normalization errors skew order — normalize carefully.
- Volume overload — filter to the window + pivot around anchors.

## Remediation / IR linkage
- Drives scoping, containment timing, and the incident report narrative.

## References
- `_shared/` rules (untrusted input, evidence).
