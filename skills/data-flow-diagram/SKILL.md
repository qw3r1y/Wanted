---
name: data-flow-diagram
description: >
  Use when building a data-flow diagram for threat modeling — mapping components,
  data flows, stores, external entities, and trust boundaries as the foundation for
  STRIDE and risk analysis. Covers DFD construction for security.
type: knowledge
domain: appsec/threat-modeling
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Data-Flow Diagram (for Threat Modeling)

Build the picture threat modeling runs on: how data moves through the system, where
it is stored, who the external actors are, and — most importantly — where **trust
boundaries** are crossed (the places threats concentrate). A good DFD makes STRIDE
tractable.

## When to use
As the first step of a threat model, or to communicate a system's security-relevant
architecture.

## Procedure (gated phases)
1. **Identify elements** — processes/components, data stores, external entities, and
   the data flows between them.
2. **Draw trust boundaries** — where control/trust changes (internet↔app, app↔DB,
   tenant boundaries, privilege levels) — threats cluster here.
3. **Annotate flows** — what data (sensitivity), direction, and protocol crosses each
   boundary.
4. **Validate** — confirm the DFD matches reality (with engineers).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: an accurate DFD with trust
boundaries, ready for STRIDE.

## Quality bar / pitfalls
- DFDs without trust boundaries (the key security element).
- Diagrams that don't match the real system — validate.

## Linkage
- Foundation for stride-modeling, attack-tree, and detection requirements.

## References
- `_shared/` rules (evidence).
