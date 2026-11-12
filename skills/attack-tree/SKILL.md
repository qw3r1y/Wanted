---
name: attack-tree
description: >
  Use when analyzing how an attacker could achieve a specific goal via attack trees
  — decomposing an objective into attack paths and AND/OR steps to find the weakest
  paths and prioritize defenses. Covers goal-oriented attack analysis.
type: knowledge
domain: appsec/threat-modeling
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Attack Tree Analysis

Start from an attacker goal (e.g., "exfiltrate customer data") and decompose it into
the paths and sub-steps that achieve it (AND/OR logic), exposing the **weakest
paths** so you can defend where it matters most. Goal-oriented complement to STRIDE.

## When to use
To analyze a specific high-value attacker objective and prioritize defenses by path.

## Procedure (gated phases)
1. **Define the goal** — the attacker objective at the root.
2. **Decompose** — branch into sub-goals/steps with AND/OR relationships down to
   concrete actions.
3. **Annotate** — per leaf: difficulty, required access, detectability, and existing
   controls.
4. **Find weakest paths & defend** — identify the easiest/least-detected paths;
   prioritize mitigations/detections there.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: the tree + prioritized weak
paths + defenses.

## Quality bar / pitfalls
- Trees that are exhaustive-but-unprioritized — focus on realistic weak paths.
- Ignoring detection (not just prevention) along paths.

## Linkage
- Complements STRIDE; informs detection-coverage and offensive test planning.

## References
- `_shared/` rules (evidence).
