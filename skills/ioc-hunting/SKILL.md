---
name: ioc-hunting
description: >
  Use when sweeping the environment for known indicators of compromise — hashes,
  domains, IPs, URLs, and host artifacts from threat intel or an incident — across
  historical and live telemetry, with scoping and pivoting. Covers IOC sweeps and
  retro-hunting.
type: knowledge
domain: defensive/threat-hunting
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# IOC Hunting / Retro-Hunt

Given a set of indicators (from CTI, an incident, or a phishing analysis), sweep
historical and live telemetry for any presence, scope the blast radius, and pivot
from hits to related activity — the fast "are we affected?" question.

## When to use
On new threat intel, during/after an incident, or when a related org is breached.

## Procedure (gated phases)
1. **Normalize IOCs** — dedupe and classify indicators (network/file/host) and the
   telemetry each maps to.
2. **Sweep (retro + live)** — search historical logs and current telemetry for the
   indicators across relevant data sources.
3. **Triage hits** — validate each hit (true match vs coincidence); apply the
   evidence rule; distinguish exposure from compromise.
4. **Pivot & scope** — from a confirmed hit, pivot to related activity/assets to
   scope impact; hand to IR if compromise is confirmed.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record hits with `verdict` and scope. A
match on a low-fidelity IOC alone is a signal, not confirmed compromise.

## Quality bar / pitfalls
- Low-fidelity IOCs (shared IPs, generic hashes) cause FPs — weigh fidelity.
- Only live-searching (missing retro) misses past compromise — search history too.

## Governance
- Feed confirmed compromises to IR (dfir) and new durable detections to detection
  engineering.

## References
- `_shared/` rules (evidence).
