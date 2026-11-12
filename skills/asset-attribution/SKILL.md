---
name: asset-attribution
description: >
  Use when attributing internet-facing assets to an organization for EASM —
  expanding from seeds (domains, IPs, org name) to the full owned attack surface
  via domain/IP/ASN/certificate pivots, with ownership evidence. The core of
  identity-based external attack surface discovery.
type: knowledge
domain: easm
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Asset Attribution (EASM core)

EASM is an attribution problem: given seeds (known domains, IP ranges, org/brand
names), expand to the **full set of internet-facing assets the organization
actually owns** — and only those. Attribution quality (not raw discovery volume) is
what makes EASM useful; wrong attribution creates noise and liability.

> Passive/authorized discovery; attribute to the in-scope organization only
> (`_shared/scope-authorization-rule.md`).

## When to use
Building/maintaining an organization's external attack-surface inventory.

## Procedure (gated phases)
1. **Seeds** — known apex domains, IP ranges/ASNs, org/brand names, acquisitions.
2. **Pivot to expand** — domain pivots (WHOIS/registrant, reverse-WHOIS),
   IP/ASN pivots, **certificate** pivots (shared certs/orgs), favicon/analytics IDs,
   and passive DNS — each adds candidate assets.
3. **Attach ownership evidence (core)** — for every candidate, record **why** it's
   attributed (which pivot/evidence), not just that it was found.
4. **Hand off** — candidates go to confidence-scoring + false-positive-rejection
   before entering the inventory.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each candidate carries its attribution
evidence; unproven attribution stays a candidate, not an asset.

## Impact / output
A seed-to-asset expansion with evidence — the input to scoring and monitoring.

## Pitfalls
- Shared infrastructure (CDNs, cloud ranges, shared certs) causes false attribution
  — evidence + scoring must gate inclusion.
- Volume over accuracy — wrong assets are worse than missing ones.

## Linkage
- Feeds confidence-scoring, false-positive-rejection, continuous-discovery; pairs
  with recon-osint.

## References
- `_shared/` rules (authorization, evidence).
