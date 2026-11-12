---
name: garak-probes
description: >
  Use when running automated LLM vulnerability scanning with garak — probing a model/
  app for known weakness classes (injection, jailbreak, toxicity, leakage) at scale
  and interpreting results. Covers automated LLM scanning.
type: knowledge
domain: ai-security/ai-red-team
maturity: canonical
tools: [garak]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Automated LLM Scanning (garak)

Run broad, automated probes against an authorized model/app to surface known LLM
weakness classes — prompt injection, jailbreaks, toxicity, data leakage,
encoding attacks — quickly and repeatably, then interpret and prioritize the
results for deeper testing and hardening.

> Authorized testing of your own/in-scope model (`_shared/scope-authorization-rule.md`).

## When to use
As a first-pass/continuous automated assessment of an LLM app's robustness.

## Procedure (gated phases)
1. **Configure** — point garak at the model/app endpoint; select relevant probe sets
   for the app's risks.
2. **Run probes** — execute the weakness-class probes; collect pass/fail per probe.
3. **Interpret (core)** — garak gives signals, not verdicts; validate notable hits
   and prioritize (ties to the specific llm-security skill).
4. **Operationalize** — feed gaps to guardrail-design; integrate into CI for
   regression.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record probe results; validate significant
findings before treating as confirmed.

## Impact / output
A broad robustness baseline + prioritized weaknesses.

## Pitfalls
- Treating raw probe output as ground truth — validate.
- One-off scans — run continuously (model/app change).

## Linkage
- Pairs with jailbreak-testing, prompt-injection, promptfoo-eval; feeds guardrails.

## References
- `_shared/` rules (authorization, evidence).
