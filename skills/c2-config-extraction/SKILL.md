---
name: c2-config-extraction
description: >
  Use when extracting a malware sample's embedded configuration (C2 servers, keys,
  campaign IDs, settings) — locating and decoding the config to produce high-value
  IOCs and campaign intelligence. Defensive config extraction.
type: knowledge
domain: malware-re
maturity: canonical
tools: [ghidra]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# C2 Config Extraction

Recover a sample's embedded configuration — C2 endpoints, encryption keys, campaign/
botnet IDs, and operational settings — by locating and decoding the config blob.
This yields the highest-value IOCs and campaign intelligence for tracking and
blocking.

> The sample/config is hostile data; analyze, don't run on production
> (`_shared/untrusted-input-rule.md`).

## When to use
After identifying the family/decoder in static analysis, to produce actionable C2
IOCs.

## Procedure (gated phases)
1. **Locate the config** — find the config blob and the decode routine (from static
   analysis) — often encrypted/encoded and referenced by the network/init code.
2. **Understand the decoder** — the algorithm/key used to decode the config.
3. **Decode** — reproduce the decoding (statically/scripted) to recover the config
   fields.
4. **Produce intel** — C2 list, keys, campaign IDs → IOCs for blocking/hunting and
   campaign correlation (CTI).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the decoded config + method; validate
fields make sense (valid C2 formats).

## Impact / output
High-fidelity C2 IOCs + campaign intel (feeds hunting, feed-management, tracking).

## Pitfalls
- Wrong key/algorithm → garbage; validate output.
- Dynamically-fetched config (not embedded) — note and pivot to dynamic analysis.

## Governance / linkage
- Track configs across samples for campaign correlation; feed detection/blocking.

## References
- `_shared/` rules (untrusted input, evidence).
