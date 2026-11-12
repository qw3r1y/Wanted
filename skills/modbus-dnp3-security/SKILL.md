---
name: modbus-dnp3-security
description: >
  Use when assessing industrial protocols (Modbus, DNP3, S7, etc.) for security —
  their lack of authentication/encryption and the risks of command injection/
  spoofing in OT networks. Covers ICS protocol risk assessment (passive).
type: knowledge
domain: ot-ics-scada
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Industrial Protocol Security (Modbus/DNP3/S7)

Most industrial protocols were designed for isolated, trusted networks — they lack
authentication and encryption, so anyone on the OT network can read or **inject
commands** to controllers. Assess which protocols are in use and the exposure,
using **passive** methods (active probing can disrupt safety-critical systems).

> OT is safety-critical — passive observation only; never inject/fuzz on live control
> systems (`_shared/safe-execution-rules.md`).

## When to use
Assessing OT network protocol exposure (passively).

## Procedure (gated phases)
1. **Identify protocols (passive)** — observe traffic to identify Modbus/DNP3/S7comm/
   EtherNet-IP and the devices speaking them.
2. **Assess exposure** — these protocols are unauthenticated/unencrypted: who can
   reach the controllers? Is the segment flat?
3. **Reason about risk (no active injection)** — command injection/spoofing/read is
   possible for anyone with network access; the control is **network isolation**, not
   the protocol.
4. **Prioritize** — by what the device controls (safety impact) and reachability.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings: protocol exposure + reachability,
assessed passively.

## Impact escalation
Unauthorized read/command of industrial controllers → process manipulation/safety.
Critical.

## Pitfalls
- Active scanning/fuzzing of OT — can crash PLCs/cause safety events. Passive only.

## Remediation
- Network isolation/segmentation (the primary control); unidirectional gateways where
  possible; monitor OT protocol traffic for anomalies (ics-threat-hunting); use
  authenticated variants where available.

## References
- `_shared/` rules (authorization, safe execution, evidence).
