---
name: tool-abuse-defense
description: >
  Use when securing an AI agent's tool/function use — ensuring tools are
  least-privilege, inputs/outputs validated, and dangerous actions gated, so a
  manipulated agent can't misuse its tools. Covers secure tool design for agents.
type: knowledge
domain: ai-security/agent-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Agent Tool Abuse Defense

An agent is only as safe as its tools. If a (possibly injected) agent can call tools
with attacker-chosen arguments, the tools' power becomes the attacker's. Design each
tool least-privilege, validate its inputs/outputs, and gate consequential actions —
so manipulation can't translate into damage.

## When to use
When building/reviewing an agent that can call tools/functions/APIs.

## Procedure (gated phases)
1. **Inventory tools & power** — what each tool can do and its blast radius (read vs
   write, scope, external effects).
2. **Least privilege** — scope each tool minimally; no "do anything" tools; separate
   read from write.
3. **Validate tool I/O** — validate/constrain arguments the model supplies (allow-
   lists, types, bounds); treat tool outputs as untrusted (can carry injection).
4. **Gate consequential actions** — human-in-the-loop/confirmation for
   irreversible/high-impact actions (`gated-workflow-rule.md`); rate/scope limits.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Robust" = a manipulated agent still can't
exceed tool scope or take ungated consequential actions. Validate via ai-red-team.

## Quality bar / pitfalls
- Over-powerful tools (shell/arbitrary HTTP) exposed to the model.
- Trusting model-supplied tool arguments without validation.

## Linkage
- Core defense for prompt-injection impact + excessive-agency; pairs with mcp-security.

## References
- `_shared/` rules (evidence, gated workflow).
