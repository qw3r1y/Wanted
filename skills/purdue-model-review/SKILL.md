---
name: purdue-model-review
description: >
  Use when assessing OT/ICS network architecture against the Purdue model —
  verifying proper segmentation between IT and OT zones and controlled conduits — to
  reduce the risk of IT compromise reaching control systems. Covers OT architecture
  review.
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

# Purdue Model / OT Architecture Review

Industrial environments must keep control systems (OT) isolated from IT and the
internet. Review the architecture against the Purdue model — proper zones (enterprise,
DMZ, control, field) and controlled conduits between them — to find the flat networks
and direct IT→OT paths that let ransomware reach physical processes.

> OT is safety-critical; assessment is passive/read-only and coordinated — never
> disrupt control systems (`_shared/safe-execution-rules.md`).

## When to use
Assessing an ICS/SCADA environment's segmentation and exposure.

## Procedure (gated phases)
1. **Map zones & conduits** — enterprise (IT), industrial DMZ, control, and field
   levels; the data flows/conduits between them.
2. **Verify segmentation (core)** — is there an enforced DMZ between IT and OT? Any
   direct IT→control paths, dual-homed hosts, or internet-exposed OT?
3. **Conduit controls** — are allowed flows minimal, inspected, and controlled
   (no flat trust)?
4. **Remote access** — how vendors/engineers reach OT (a major risk path).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Findings: direct IT↔OT paths, exposure, weak
conduits — prioritized by safety impact.

## Impact escalation
IT compromise reaching control systems → process disruption / safety impact.
Critical.

## Pitfalls
- Active scanning of fragile OT devices — don't; use passive methods.
- Overlooked dual-homed/jump hosts bridging IT and OT.

## Remediation
- Enforced IT/OT DMZ; minimal controlled conduits; no internet-exposed OT; secured,
  monitored remote access; segmentation + monitoring (ics-network-segmentation).

## References
- `_shared/` rules (authorization, safe execution, evidence).
