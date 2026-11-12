---
name: guardrail-design
description: >
  Use when designing input/output guardrails for an LLM application — layered
  controls (input filtering, instruction hierarchy, output validation, action
  gating) that constrain the model's behaviour and blast radius. Covers defensive
  architecture.
type: knowledge
domain: ai-security/llm-security
maturity: canonical
tools: [llm-guard]
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# LLM Guardrail Design

Design the layered controls that make an LLM app safe even when the model is
tricked — because prompt-level instructions alone are not a security boundary.
Combine input filtering, clear instruction/data separation, output validation, and
capability/action gating to limit what a compromised interaction can do.

## When to use
When architecting the safety/security of any LLM feature or agent.

## Procedure (gated phases)
1. **Input controls** — classify/filter untrusted input; separate instructions from
   data (structured prompts, spotlighting); retrieval authorization.
2. **Model-level** — instruction hierarchy, minimal system-prompt secrets, and
   bounded context.
3. **Output controls** — validate/encode output per sink (insecure-output-handling);
   content/PII filtering.
4. **Action/capability gating (core)** — least-privilege tools; human-in-the-loop
   for consequential actions (`gated-workflow-rule.md`); rate/scope limits.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Robust" = layered controls that hold under
red-team testing (not a single prompt-level defense). Validate via ai-red-team.

## Quality bar / pitfalls
- Relying on "ignore injections" prompt text as the control (bypassable).
- Over-privileged tools / no human gate on consequential actions.

## Linkage
- Implements defenses for prompt-injection, output-handling, agent-security;
  validated by ai-red-team.

## References
- `_shared/` rules (evidence, gated workflow).
