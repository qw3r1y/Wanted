---
name: multi-agent-trust
description: >
  Use when securing multi-agent systems — trust boundaries between agents, injection
  propagation across agents, and authorization of inter-agent actions. Covers
  trust/isolation design for agent-to-agent systems.
type: knowledge
domain: ai-security/agent-security
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Multi-Agent Trust & Isolation

In multi-agent systems, one compromised/injected agent can manipulate others — its
output is untrusted input to the next agent. Design trust boundaries, treat
inter-agent messages as untrusted, and authorize inter-agent actions, so an
injection in one agent doesn't cascade through the system.

## When to use
When designing/reviewing systems where agents call or message other agents.

## Procedure (gated phases)
1. **Map the agent graph** — which agents communicate, what they pass, and each
   agent's authority/tools.
2. **Treat inter-agent messages as untrusted** — one agent's output can carry
   injection; the receiving agent must not blindly obey it (untrusted-input-rule).
3. **Authorize inter-agent actions** — an agent requesting another to act must be
   authorized; don't let a low-trust agent drive a high-privilege one.
4. **Contain propagation** — isolate agents (sandboxing), least-privilege per agent,
   and gates on consequential cross-agent actions.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Robust" = an injection in one agent cannot
drive privileged actions in another. Validate via red-team.

## Quality bar / pitfalls
- Agents implicitly trusting each other's output (injection cascade).
- A high-privilege "executor" agent driven by a low-trust "planner".

## Linkage
- Builds on tool-abuse-defense, excessive-agency, sandboxing; orchestration-level
  design.

## References
- `_shared/` rules (untrusted input, evidence).
