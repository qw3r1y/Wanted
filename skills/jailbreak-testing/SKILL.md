---
name: jailbreak-testing
description: >
  Use when testing an authorized LLM's safety guardrails for jailbreaks — attempts
  to bypass content/safety policies via roleplay, obfuscation, many-shot, or
  multi-turn techniques — to measure robustness and improve guardrails. Covers
  structured jailbreak evaluation.
type: knowledge
domain: ai-security/llm-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
  - references/jailbreak-classes.md
license: MIT
version: 1.0.0
---

# Jailbreak / Guardrail Robustness Testing

Measure how robustly an authorized LLM application enforces its safety/content
policy against bypass attempts — roleplay, obfuscation/encoding, many-shot,
crescendo/multi-turn, and policy-confusion — to quantify robustness and harden
guardrails. The goal is improving safety, not producing harmful content.

> Authorized testing of your own/in-scope model to improve it
> (`_shared/scope-authorization-rule.md`). The deliverable is a robustness
> assessment + guardrail improvements, not harmful outputs.

## When to use
When evaluating/strengthening a model or app's safety guardrails.

## Procedure (gated phases)
1. **Define the policy boundary** — what the guardrails should refuse; the test is
   whether bypasses cross it.
2. **Apply technique classes** — roleplay, encoding/obfuscation, many-shot,
   multi-turn/crescendo, instruction-hierarchy confusion (`references/jailbreak-classes.md`).
3. **Measure robustness** — bypass rate per class; which techniques succeed.
4. **Harden** — feed gaps to guardrail design + ai-red-team automation.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record bypass rate per class with evidence;
robust refusal → **refuted** for that class.

## Impact / output
A guardrail-robustness scorecard + hardening recommendations.

## Pitfalls
- One-off testing — guardrails need continuous evaluation (model/app changes).
- Treating a single refusal as "safe" — test many techniques.

## Defenses
- Layered guardrails (input/output classifiers), instruction hierarchy, continuous
  red-teaming, and monitoring; don't rely on the base model alone.

## References
- `_shared/` rules; `references/jailbreak-classes.md` — technique classes (4th level).
