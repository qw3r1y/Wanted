---
name: owasp-llm-top10
description: >
  Use when assessing an LLM application against the OWASP Top 10 for LLM
  Applications — a structured review across the top risk categories, mapping each to
  tests and controls. An umbrella assessment that references the specific
  llm-security/agent-security skills.
type: knowledge
domain: ai-security/llm-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# OWASP LLM Top 10 Assessment

Run a structured security assessment of an authorized LLM application across the
OWASP LLM Top 10 risk categories, mapping each to concrete tests and controls — an
umbrella that ties the specific AI-security skills into a complete review.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
For a comprehensive LLM-app security review, or to structure coverage.

## Procedure (gated phases)
Assess each category, deferring to the dedicated skill:
1. **Prompt injection** (`llm-security/prompt-injection`).
2. **Insecure output handling** (`llm-security/insecure-output-handling`).
3. **Training/data poisoning & supply chain** (`ml-model-security`, `agent-security/
   mcp-security` for plugins).
4. **Model DoS / denial-of-wallet** — unbounded/expensive usage.
5. **Sensitive information disclosure** (`llm-security/data-leakage`).
6. **Excessive agency** (`agent-security/excessive-agency-control`).
7. **Insecure plugin/tool design** (`agent-security/tool-abuse-defense`, `mcp-security`).
8. **Overreliance** — unvalidated model output in decisions.
9. **Model theft** (`ml-model-security/model-extraction-defense`).
Record coverage + findings per category.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a per-category assessment
(covered/finding/N-A) with evidence and prioritized remediation.

## Impact / output
A complete LLM-app risk picture driving remediation.

## Pitfalls
- Testing only prompt injection — cover output handling, agency, and data too.

## Remediation
- Layered guardrails (guardrail-design), least agency, output validation, retrieval
  authz, usage limits, and continuous red-teaming.

## References
- `_shared/` rules (authorization, evidence).
