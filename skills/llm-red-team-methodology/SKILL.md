---
name: llm-red-team-methodology
description: >
  Use when planning and running a structured AI red-team engagement — scoping,
  threat-modeling the AI system, combining manual + automated techniques, and
  reporting — to comprehensively assess an LLM/agent application's security and
  safety. Umbrella methodology for ai-red-team.
type: knowledge
domain: ai-security/ai-red-team
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# AI Red-Team Methodology

Run a structured red-team of an authorized LLM/agent application end-to-end: scope
and threat-model the system, test across the risk classes with both manual and
automated techniques, and report prioritized findings + hardening — a repeatable
program, not ad-hoc prompting.

> Authorized testing of an in-scope system (`_shared/scope-authorization-rule.md`).

## When to use
For a comprehensive AI security/safety assessment or ongoing AI red-team program.

## Procedure (gated phases)
1. **Scope & threat-model** — the system's inputs, model, tools/agency, data, and
   trust boundaries (llm-threat-modeling); define objectives.
2. **Test across classes** — prompt injection (direct/indirect), jailbreaks, data
   leakage, output handling, excessive agency/tool abuse, RAG, and supply chain —
   via the specific skills + automation (garak/PyRIT/promptfoo).
3. **Assess impact** — tie each finding to real consequence (data, actions).
4. **Report & harden** — prioritized findings + guardrail/architecture fixes +
   regression evals.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a structured assessment with
validated findings + remediation; coverage across risk classes.

## Impact / output
A complete AI-security posture + prioritized hardening roadmap.

## Pitfalls
- Only manual single-prompt testing — combine manual + automated + multi-turn.
- No regression evals — findings recur without them.

## Linkage
- Orchestrates all ai-security skills; feeds guardrail-design + promptfoo-eval.

## References
- `_shared/` rules (authorization, evidence).
