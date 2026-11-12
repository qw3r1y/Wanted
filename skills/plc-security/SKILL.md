---
name: plc-security
description: >
  Use when assessing PLC/controller security in an OT environment — exposure,
  authentication, firmware/logic protection, and safe assessment practices. Covers
  controller security review (passive/coordinated).
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

# PLC / Controller Security Assessment

PLCs run the physical process and are often unauthenticated, reachable, and
reprogrammable over the network. Assess their exposure and protection — carefully,
because PLCs are fragile and safety-critical — focusing on isolation and access
control rather than active testing.

> Safety-critical: coordinated, passive/read-only assessment; never upload logic or
> actively test live PLCs (`_shared/safe-execution-rules.md`).

## When to use
Assessing controller exposure in an authorized OT environment.

## Procedure (gated phases)
1. **Identify controllers (passive)** — PLC makes/models and their network
   reachability.
2. **Access & auth** — is engineering/programming access authenticated and
   restricted, or can anyone on the network read/write logic? Default credentials?
3. **Firmware/logic protection** — are firmware and project logic protected (signed/
   password), and patched where feasible (OT patching is constrained)?
4. **Assess exposure** — reachability from IT/remote and the process it controls.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings: controller exposure/access risks,
assessed safely.

## Impact escalation
Unauthorized logic modification → process disruption/physical damage/safety.
Critical.

## Pitfalls
- Active interaction with live PLCs can halt processes — don't; passive + coordinated.

## Remediation
- Network isolation + access control to engineering interfaces; strong/unique
  credentials; logic/firmware protection; monitored, limited remote access;
  change control.

## References
- `_shared/` rules (authorization, safe execution, evidence).
