---
name: mitre-attack-mapping
description: >
  Use when mapping observed or reported activity to MITRE ATT&CK techniques — to
  normalize intel, drive detection coverage, and enable emulation. Covers
  consistent technique mapping and its downstream uses.
type: knowledge
domain: defensive/cti
maturity: canonical
tools: [attack-navigator]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# MITRE ATT&CK Mapping

Translate activity (from incidents, reporting, or hunts) into ATT&CK
tactics/techniques consistently, so intelligence becomes a common language that
drives detection coverage, hunting, and adversary emulation.

## When to use
When processing threat reports/incidents, or building actor/campaign TTP sets.

## Procedure (gated phases)
1. **Extract behaviours** — the concrete actions observed/reported (not just
   tools/IOCs).
2. **Map to technique** — assign the correct tactic → technique (→ sub-technique),
   avoiding over-mapping ambiguous behaviours.
3. **Aggregate** — build the TTP set (e.g., an ATT&CK Navigator layer) for the
   actor/campaign.
4. **Drive downstream** — cross with detection coverage (gaps) and emulation plans.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each mapping cites the observed behaviour;
mark low-confidence mappings.

## Impact / output
Normalized TTP sets powering coverage mapping, hunting, and emulation.

## Pitfalls
- Mapping tools/IOCs instead of behaviours; over-mapping ambiguous activity.
- Inconsistent mapping across analysts — use clear criteria.

## Governance
- Standardize mapping criteria; maintain Navigator layers; link to coverage.

## References
- `_shared/` rules (evidence).
