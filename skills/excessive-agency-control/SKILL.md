---
name: excessive-agency-control
description: >
  Use when constraining an AI agent's autonomy — limiting the actions it can take
  autonomously, requiring human approval for consequential/irreversible actions, and
  scoping its authority to its purpose. Covers the excessive-agency risk (OWASP
  LLM08).
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

# Excessive Agency Control

The more an agent can do autonomously, the more a single manipulation can cause.
Constrain agency: give the agent only the authority its purpose needs, require human
approval for consequential or irreversible actions, and make high-impact steps
gated — so autonomy doesn't become uncontrolled risk.

## When to use
When designing/reviewing any autonomous or semi-autonomous agent.

## Procedure (gated phases)
1. **Enumerate autonomous actions** — everything the agent can do without a human;
   classify by impact/reversibility.
2. **Scope authority to purpose** — remove capabilities beyond the task; least
   functionality + least privilege (ties to tool-abuse-defense).
3. **Gate consequential/irreversible actions (core)** — require explicit human
   approval before money movement, deletion, external sends, config changes
   (`gated-workflow-rule.md`).
4. **Bound autonomy** — limits on scope, rate, and chained actions; clear stop
   conditions.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Robust" = consequential actions can't happen
without a human gate; autonomy is scoped to purpose.

## Quality bar / pitfalls
- "Autonomous everything" agents with write/financial/external power ungated.
- Chained autonomous actions amplifying a single injection.

## Linkage
- Works with tool-abuse-defense + sandboxing; the key control against prompt-
  injection-driven harm in agents.

## References
- `_shared/` rules (evidence, gated workflow).
