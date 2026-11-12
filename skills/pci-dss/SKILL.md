---
name: pci-dss
description: >
  Use when assessing/implementing PCI DSS for cardholder-data environments — scoping
  (and reducing scope), the control requirements, and segmentation. Covers PCI DSS
  implementation focus.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# PCI DSS

PCI DSS protects payment-card data; its first lever is **scope reduction** — minimize
where cardholder data lives/flows (segmentation, tokenization, outsourcing) so fewer
systems must meet the full requirements. Then implement and evidence the controls for
the in-scope CDE.

> Implementation guidance; formal validation is via QSA/SAQ as applicable.

## When to use
For organizations handling payment-card data.

## Procedure (gated phases)
1. **Scope the CDE (core)** — identify all systems that store/process/transmit
   cardholder data and connected systems; **reduce scope** via segmentation,
   tokenization, and using compliant providers.
2. **Segment & validate** — isolate the CDE; verify segmentation (offensive testing
   confirms isolation).
3. **Implement requirements** — the control areas (network security, access control,
   encryption, monitoring/logging, vuln management, testing, policy) for the CDE.
4. **Evidence & test** — required scanning/pentesting + evidence of operating controls.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Ready" = minimized validated scope + implemented
evidenced controls for the CDE.

## Quality bar / pitfalls
- Not reducing scope (the whole network becomes in-scope — huge cost).
- Unverified segmentation leaving the CDE reachable.

## Linkage
- Consumes network segmentation, encryption, VM, logging; segmentation verified by
  offensive/network.

## References
- `_shared/` rules (evidence).
