---
name: attribution-analysis
description: >
  Use when assessing attribution of activity to an actor — using frameworks (Diamond
  Model, kill chain) and evidence weighting to reach a confidence-graded assessment
  while avoiding over-attribution. Covers disciplined attribution reasoning.
type: knowledge
domain: defensive/cti
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Attribution Analysis

Assess who is likely behind observed activity with discipline — structuring
evidence (Diamond Model: adversary/capability/infrastructure/victim), weighting it,
and expressing a **confidence-graded** assessment — while resisting the common trap
of over-attribution from weak or shared indicators.

## When to use
When attribution matters for response/intel, and there is enough evidence to reason
about it responsibly.

## Procedure (gated phases)
1. **Assemble evidence** — TTPs, tooling, infrastructure, and victimology; map to a
   framework (Diamond/kill chain).
2. **Weight evidence** — distinguish strong (unique TTPs/tooling) from weak/shared
   (common infra, public tools) indicators.
3. **Assess with confidence** — reach a graded assessment (low/medium/high),
   explicitly stating uncertainty and alternatives.
4. **Document** — the reasoning and evidence, not just a conclusion.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Attribution is an **assessment** with
confidence, never stated as fact without strong corroboration.

## Impact / output
A defensible, confidence-graded attribution assessment supporting decisions.

## Pitfalls
- Over-attribution from shared infra/public tools (false-flag risk) — weight
  evidence honestly.
- Presenting assessment as fact — grade confidence.

## Governance
- Peer review; document alternative hypotheses; update as evidence changes.

## References
- `_shared/` rules (untrusted input, evidence).
