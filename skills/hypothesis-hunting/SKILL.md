---
name: hypothesis-hunting
description: >
  Use when running a hypothesis-driven threat hunt — forming a testable hypothesis
  from threat intel/ATT&CK, defining the data and analytics to test it, hunting,
  and converting findings into detections. Covers the structured hunt loop.
type: knowledge
domain: defensive/threat-hunting
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Hypothesis-Driven Threat Hunting

Hunt with structure: start from a specific, testable hypothesis ("actor X would do
technique Y, visible as Z in our data"), gather the relevant telemetry, run the
analytic, and — whether or not you find evil — turn the result into a durable
detection or a documented coverage gap.

## When to use
Proactively (not alert-driven), prioritized by threat intel and crown-jewel risk.

## Procedure (gated phases)
1. **Form the hypothesis** — a concrete, testable statement tied to an ATT&CK
   technique and the observable it would produce in your environment.
2. **Scope data & analytic** — identify the telemetry and the query/analytic that
   would reveal the behaviour; confirm the data exists.
3. **Hunt** — run the analytic, triage results, separate benign from suspicious
   (apply the evidence rule to any finding).
4. **Operationalize** — convert a good analytic into a detection (sigma/siem), or
   document the coverage/telemetry gap found.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. A hunt is "successful" if it either finds
activity (→ incident) or yields a new detection / documented gap — not just "found
nothing".

## Quality bar / pitfalls
- Vague hunts without a testable hypothesis — scope precisely.
- Not operationalizing results — every hunt should leave a detection or a gap note.

## Governance
- Track hunts, hypotheses, and outcomes; feed detection-coverage-mapping.

## References
- `_shared/` rules (evidence).
