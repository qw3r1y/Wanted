---
name: promptfoo-eval
description: >
  Use when building security/safety evaluations for an LLM app (e.g., promptfoo) —
  test suites that assert on prompt-injection resistance, jailbreak robustness, and
  policy compliance, integrated into CI for regression. Covers LLM security eval
  harnesses.
type: knowledge
domain: ai-security/ai-red-team
maturity: canonical
tools: [promptfoo]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# LLM Security Eval Harness (promptfoo)

Turn AI red-teaming into **regression tests**: build an evaluation suite that asserts
your app resists known injection/jailbreak/policy-bypass cases, run it in CI, and
catch regressions when prompts, models, or guardrails change — so safety doesn't
silently degrade between releases.

## When to use
To make LLM security testable and continuous (not one-off).

## Procedure (gated phases)
1. **Define assertions** — security/safety test cases (injection payloads, jailbreak
   attempts, must-refuse policies) with expected outcomes.
2. **Build the suite** — encode cases + assertions (graded by rules/LLM-judge) for
   the app endpoint.
3. **Run & gate** — execute in CI; fail on regressions in robustness/compliance.
4. **Maintain** — add new cases from garak/PyRIT/incidents; keep the suite current.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = a passing suite that catches
regressions; validate judge reliability.

## Quality bar / pitfalls
- Flaky LLM-judge assertions — calibrate; use deterministic checks where possible.
- Stale suites that miss new attack classes — update continuously.

## Linkage
- Operationalizes jailbreak-testing/garak/PyRIT findings; gates guardrail changes.

## References
- `_shared/` rules (evidence).
