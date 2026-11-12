---
name: ics-threat-hunting
description: >
  Use when hunting for threats in OT/ICS environments — passive monitoring of
  industrial traffic for anomalies, unauthorized commands, and IT→OT intrusion
  indicators. Covers OT-specific detection and hunting.
type: knowledge
domain: ot-ics-scada
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# ICS / OT Threat Hunting

Hunt for threats in OT using **passive** monitoring (active tooling risks the
process): baseline normal industrial traffic and device behavior, then detect
anomalies — unexpected commands, new devices, IT→OT lateral movement, and firmware/
logic changes — that indicate intrusion toward control systems.

## When to use
For OT detection/monitoring and proactive hunting in industrial environments.

## Procedure (gated phases)
1. **Passive visibility** — tap/SPAN OT traffic into an OT-aware IDS/monitor (no
   active probing).
2. **Baseline** — normal device communications, command patterns, and the (usually
   static) OT topology.
3. **Hunt anomalies (core)** — unauthorized/unusual commands, new/unexpected devices,
   IT→OT connections, engineering-access outside windows, and logic/firmware changes.
4. **Respond carefully** — OT incident response must weigh safety/availability;
   coordinate with engineering (cloud/standard IR adapted).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record anomalies with `verdict`; OT baselines
are stable, so deviations are high-signal.

## Impact / output
Early detection of intrusions heading toward control systems.

## Pitfalls
- Active scanning/agents on OT — avoid; passive only.
- IT detection tools unaware of OT protocols — use OT-aware monitoring.

## Remediation / linkage
- Pairs with ics-network-segmentation (boundary monitoring) + detection-engineering
  adapted for OT.

## References
- `_shared/` rules (evidence).
