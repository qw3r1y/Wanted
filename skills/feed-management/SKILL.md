---
name: feed-management
description: >
  Use when managing threat-intel feeds and a TIP — source selection, deduplication,
  quality/confidence scoring, aging/expiry, and controlled integration into
  detection/blocking. Covers keeping intel useful and low-noise at scale.
type: knowledge
domain: defensive/cti
maturity: canonical
tools: [misp, opencti]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Threat Feed / TIP Management

Keep intelligence feeds useful instead of noisy: pick quality sources, deduplicate
and score indicators, age/expire them, and integrate only high-confidence intel
into blocking/detection — so the SOC gets signal, not a firehose of stale
indicators.

## When to use
When operating a TIP or integrating multiple intel feeds.

## Procedure (gated phases)
1. **Source selection** — choose feeds by relevance + reliability; avoid redundant/
   low-quality sources.
2. **Normalize & dedupe** — unify formats; deduplicate across feeds; retain
   provenance.
3. **Score & age** — confidence per source/corroboration; expire indicators (IOCs
   go stale) to prevent FPs.
4. **Controlled integration** — auto-push only high-confidence indicators to
   blocking; others to enrichment/hunting.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Indicators carry confidence + source + age;
blocking uses only high-confidence, current ones.

## Impact / output
A clean, scored, current indicator base feeding detection/hunting/blocking.

## Pitfalls
- Auto-blocking raw feeds → outages/FPs.
- No aging → stale indicators cause noise.

## Governance
- Track source reliability + FP rate; prune feeds; review integration rules.

## References
- `_shared/` rules (evidence).
