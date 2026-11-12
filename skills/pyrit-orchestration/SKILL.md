---
name: pyrit-orchestration
description: >
  Use when running orchestrated, automated AI red-teaming (e.g., PyRIT) — multi-turn
  adversarial conversations, attack strategies, and scoring against an authorized
  model/app at scale. Covers automated adversarial orchestration.
type: knowledge
domain: ai-security/ai-red-team
maturity: canonical
tools: [pyrit]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Orchestrated AI Red-Teaming (PyRIT)

Go beyond single prompts: orchestrate automated, multi-turn adversarial
conversations and attack strategies against an authorized model/app, with automated
scoring, to find robustness gaps that only emerge over a conversation (crescendo,
multi-turn jailbreaks) — at a scale manual testing can't reach.

> Authorized testing of your own/in-scope model, to improve it
> (`_shared/scope-authorization-rule.md`).

## When to use
For scaled, multi-turn adversarial testing and continuous red-teaming.

## Procedure (gated phases)
1. **Define objectives & scope** — the policy/robustness goals to test; the target
   endpoint.
2. **Configure strategies** — multi-turn/converter/orchestrator strategies and a
   scorer (automated judge) for success.
3. **Run & score** — execute orchestrated attacks; collect scored results across
   strategies.
4. **Validate & operationalize** — confirm notable successes; feed gaps to guardrail
   design; integrate into CI regression.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record scored results; validate automated-
judge verdicts on significant hits.

## Impact / output
A scaled, multi-turn robustness assessment + prioritized gaps.

## Pitfalls
- Over-trusting the automated scorer — validate key findings.
- Only single-turn testing (misses multi-turn attacks).

## Linkage
- Complements garak (broad) + jailbreak-testing; feeds guardrail-design continuously.

## References
- `_shared/` rules (authorization, evidence).
