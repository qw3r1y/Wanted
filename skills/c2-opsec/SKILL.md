---
name: c2-opsec
description: >
  Use when, in an authorized red-team, understanding command-and-control
  **detection surfaces** — the network/host indicators C2 generates — so defenders
  can detect it and the engagement stays controlled. Detection-centric framing; no
  operational C2 build guidance.
type: knowledge
domain: offensive/c2-redteam
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

# C2 Detection Surfaces (authorized red-team, detection-centric)

Understand the indicators that command-and-control activity produces — beaconing
patterns, protocol/traffic anomalies, and host artifacts — so that an authorized
red-team stays controllable and, more importantly, defenders can detect C2. The
deliverable is detection guidance, not instructions to build/operate covert C2.

> Authorized, coordinated testing only. Focus on detection and remediation; use
> approved, logged infrastructure (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope + blue-team coordination. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate detection surfaces** — network (beacon interval/jitter, JA3/TLS
   anomalies, DNS patterns, domain reputation) and host (process/parent anomalies,
   named pipes, memory artifacts).
2. **Map to detections (core)** — for each surface, define what telemetry/analytic
   would catch it.
3. **Validate coverage** — in the exercise, check whether the org detects these
   surfaces (feeds detection-engineering).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: C2 detection-surface →
analytic mapping with coverage results.

## Impact escalation
Better C2 detection reduces attacker dwell time; gaps are high-value fixes.

## False positives & pitfalls
- Legitimate periodic traffic can resemble beaconing — tune analytics.
- Keep the focus on detection, not operating covert infrastructure.

## Remediation
- Beaconing analytics, TLS/JA3 and DNS monitoring, egress filtering/allow-listing,
  host process-lineage detection, and threat-intel domain reputation.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
