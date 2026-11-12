---
name: ics-network-segmentation
description: >
  Use when designing/assessing OT network segmentation — isolating control networks
  from IT and the internet, controlled conduits, and secure remote access — the
  primary defense for ICS. Covers OT segmentation design.
type: knowledge
domain: ot-ics-scada
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# ICS / OT Network Segmentation

Because industrial protocols/devices can't defend themselves, **segmentation is the
primary ICS security control**. Isolate OT from IT and the internet, allow only
minimal inspected conduits, and tightly control remote access — so an IT breach or
ransomware can't reach the physical process.

## When to use
Designing or hardening OT network architecture.

## Procedure (gated phases)
1. **Isolate OT** — a dedicated, firewalled industrial network; an IT/OT DMZ (Purdue);
   no direct IT→control routes; no internet exposure.
2. **Minimal conduits** — only required flows between zones, inspected; default-deny;
   no dual-homed hosts bridging zones.
3. **Secure remote access (core)** — vendor/engineer access via brokered, MFA'd,
   monitored, time-bound paths (not flat VPN into OT).
4. **Monitor the boundary** — detect IT↔OT anomalies and unexpected flows.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = OT is isolated with minimal controlled
conduits and secured remote access; validated.

## Quality bar / pitfalls
- Flat IT/OT networks or jump hosts quietly bridging them.
- Unmonitored vendor remote access into OT (a common breach path).

## Remediation / linkage
- Pairs with purdue-model-review; apply zero-trust/microsegmentation principles
  adapted for OT constraints.

## References
- `_shared/` rules (evidence).
