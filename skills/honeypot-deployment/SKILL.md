---
name: honeypot-deployment
description: >
  Use when deploying honeypots for threat detection — decoy systems/services that
  attract and detect attackers with high fidelity, placed and monitored to catch
  lateral movement and intrusion. Covers honeypot strategy and safe deployment.
type: knowledge
domain: deception
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Honeypot Deployment

Honeypots are decoy systems/services with no legitimate use — so **any** interaction
is suspicious, making them extremely high-fidelity detectors. Deploy them to catch
attackers during reconnaissance and lateral movement, with careful placement,
monitoring, and isolation so they detect without becoming a foothold.

## When to use
To add high-fidelity detection, especially for internal lateral movement.

## Procedure (gated phases)
1. **Choose type & placement** — low/medium-interaction decoys placed where only an
   attacker would find them (internal segments, near crown jewels); mimic real
   services/naming.
2. **Isolate (core)** — the honeypot must not be usable to pivot into real systems;
   contain it; no real credentials/data.
3. **Monitor & alert** — any interaction → high-priority alert (it's inherently
   suspicious); capture attacker TTPs.
4. **Operationalize** — route alerts to SOC; feed TTPs/IOCs to detection + hunting.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = isolated decoys that alert on any
interaction with near-zero false positives.

## Quality bar / pitfalls
- A honeypot that can be used to pivot into real systems (becomes a liability).
- Obvious/unrealistic decoys that attackers ignore.

## Linkage
- Pairs with honeytoken/canary-tokens, detection-engineering, threat-hunting.

## References
- `_shared/` rules (evidence).
