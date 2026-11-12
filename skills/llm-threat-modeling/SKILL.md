---
name: llm-threat-modeling
description: >
  Use when threat-modeling an LLM/AI-agent application — enumerating AI-specific
  threats (prompt injection, data leakage, excessive agency, tool abuse, supply
  chain) and deriving controls. Bridges threat modeling to ai-security.
type: knowledge
domain: appsec/threat-modeling
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# LLM / AI Application Threat Modeling

Model the threats unique to LLM/agent systems that classic STRIDE misses: untrusted
content reaching the model (prompt injection), sensitive data in prompts/outputs,
the model's tools/agency (excessive agency, tool abuse), and the AI supply chain
(models, plugins, RAG sources) — then derive controls.

## When to use
When designing an LLM feature or autonomous agent, alongside standard threat
modeling.

## Procedure (gated phases)
1. **Map the AI data/trust flows** — prompt sources (user, retrieved/RAG, tool
   output), the model, its tools/actions, and outputs; mark trust boundaries
   (untrusted content → model).
2. **Enumerate AI threats** — prompt injection (direct/indirect), data leakage,
   insecure output handling, excessive agency/tool abuse, model/plugin supply chain,
   and denial-of-wallet (map to OWASP LLM Top 10).
3. **Prioritize** — by impact of the model's actions/data access.
4. **Derive controls** — input/output handling, tool gating/human-in-the-loop, least
   agency, and RAG-source trust (feeds ai-security).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: AI threat list + controls tied to
the design.

## Quality bar / pitfalls
- Treating the LLM as trusted / its inputs as trusted — untrusted content is the key
  boundary.
- Over-privileged agents (excessive agency) — constrain actions.

## Linkage
- Feeds ai-security/llm-security, agent-security; complements STRIDE.

## References
- `_shared/` rules (evidence).
