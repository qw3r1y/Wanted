---
name: ioc-enrichment
description: >
  Use when enriching indicators with context — reputation, relationships, actor/
  campaign links, and confidence scoring — so alerts and hunts are actionable
  rather than raw indicators. Covers enrichment sources and confidence handling.
type: knowledge
domain: defensive/cti
maturity: canonical
tools: [misp, opencti]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# IOC Enrichment

Turn raw indicators into actionable intelligence: add reputation, first/last seen,
related infrastructure, actor/campaign associations, and a confidence score — so
SOC and hunting decisions rest on context, not just a hash or IP.

## When to use
On indicators from alerts, feeds, incidents, or hunts before acting/blocking.

## Procedure (gated phases)
1. **Normalize** — type/format each indicator; dedupe.
2. **Enrich** — reputation, passive DNS/WHOIS, related infrastructure, sandbox
   links, and actor/campaign associations (treat third-party data as untrusted).
3. **Score confidence** — weigh source reliability + corroboration; avoid blocking
   on low-fidelity indicators (e.g., shared CDN IPs).
4. **Operationalize** — push high-confidence IOCs to blocking/detection; store with
   context in the TIP.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each enriched IOC carries confidence + source
provenance.

## Impact / output
Actionable, scored indicators for detection, hunting, and blocking.

## Pitfalls
- Blocking low-fidelity indicators → outages/FPs.
- Trusting single-source enrichment — corroborate.

## Governance
- Source reliability tracking; expiry/aging of indicators; feedback from
  true/false positives.

## References
- `_shared/` rules (untrusted input, evidence).
