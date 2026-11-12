---
name: phishing-infra-analysis
description: >
  Use when analyzing phishing infrastructure from reported campaigns — domains,
  hosting, kits, and patterns — to extract IOCs, block proactively, and track
  campaigns targeting the organization. Covers phishing-infra intelligence.
type: knowledge
domain: email-security
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Phishing Infrastructure Analysis

Analyze the infrastructure behind phishing campaigns targeting the org — the domains,
hosting, redirectors, and phishing kits — to extract IOCs for blocking, find related
infrastructure proactively, and track campaigns, turning reactive phishing response
into proactive defense.

> Treat analyzed content/sites as untrusted; use sandboxes (`_shared/untrusted-input-rule.md`).

## When to use
After phishing reports/detections, to proactively block and track campaigns.

## Procedure (gated phases)
1. **Collect** — the phishing URLs/domains/emails from reports (phishing-detection).
2. **Analyze infrastructure** — domain registration patterns, hosting/IP, redirectors,
   and the phishing kit (if recoverable, safely) — fingerprints of the campaign.
3. **Pivot to related infra (core)** — find other domains/sites sharing the same
   registrant/hosting/kit (proactive blocking before they're used).
4. **Operationalize** — block IOCs, feed CTI, and track the campaign/actor.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record IOCs + related infra + confidence.

## Impact / output
Proactive blocking of campaign infrastructure + campaign tracking.

## Pitfalls
- Interacting with live phishing sites unsafely — sandbox.
- Low-fidelity pivots (shared hosting) → FPs; weigh evidence.

## Linkage
- Consumes phishing-detection; feeds cti/feed-management + blocking.

## References
- `_shared/` rules (untrusted input, evidence).
