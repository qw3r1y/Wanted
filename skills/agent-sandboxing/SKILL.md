---
name: agent-sandboxing
description: >
  Use when isolating an AI agent's execution — sandboxing code execution, file/
  network access, and tool effects so a compromised agent is contained. Covers
  execution isolation for agents.
type: knowledge
domain: ai-security/agent-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Agent Execution Sandboxing

Contain what an agent can affect, especially if it runs code or has broad tools:
isolate execution (ephemeral sandbox/container), restrict filesystem and network,
and bound resource use — so a manipulated or buggy agent can't reach the host, other
tenants, or sensitive systems.

## When to use
For agents that execute code, run commands, or have powerful/broad capabilities.

## Procedure (gated phases)
1. **Isolate execution** — run agent code/tools in an ephemeral, least-privilege
   sandbox (container/VM/microVM), not on the host.
2. **Restrict resources** — filesystem (scoped/read-only where possible), network
   (egress allow-list, block internal/metadata), and CPU/memory/time limits.
3. **Contain tool effects** — scope credentials/tokens the agent uses; no ambient
   host privileges.
4. **Monitor** — log agent actions; detect anomalous behaviour (runtime detection).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Robust" = a compromised agent is confined to
the sandbox with no host/tenant/internal reach. Validate with isolation tests.

## Quality bar / pitfalls
- Running agent-generated code on the host (no isolation).
- Broad network egress enabling SSRF/exfil from the agent.

## Linkage
- Pairs with tool-abuse-defense, excessive-agency-control; limits blast radius of
  prompt injection.

## References
- `_shared/` rules (evidence).
