---
name: deception-detection-engineering
description: >
  Use when building deception into the detection strategy — integrating honeypots/
  tokens/canaries into SOC workflows, mapping them to attacker stages, and measuring
  their detection value. Covers deception as a program.
type: knowledge
domain: deception
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Deception as a Detection Program

Deception is most valuable as part of the detection strategy, not scattered gadgets:
map honeypots/honeytokens/canaries to the attacker kill chain (recon → lateral
movement → collection → exfil), integrate their high-fidelity alerts into SOC
workflows, and measure the detections they provide.

## When to use
When operationalizing deception across the environment as a detection layer.

## Procedure (gated phases)
1. **Map to attacker stages** — place deception where it catches each stage (network
   decoys for lateral movement, honeytokens for credential/collection, canaries for
   exfil).
2. **Integrate with SOC** — deception alerts (inherently high-fidelity) get priority
   handling + playbooks; they often beat signature detection.
3. **Coverage & placement** — ensure crown jewels and likely attacker paths are
   covered; avoid predictable patterns.
4. **Measure** — detections provided, time-to-detect improvement, and FP rate (should
   be near zero).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = deception is mapped, SOC-integrated,
and measurably improving detection.

## Quality bar / pitfalls
- Deploying deception gadgets without SOC integration (alerts ignored).
- Predictable/obvious placement attackers learn to avoid.

## Linkage
- Orchestrates honeypot/honeytoken/canary; feeds detection-engineering + threat-hunting.

## References
- `_shared/` rules (evidence).
