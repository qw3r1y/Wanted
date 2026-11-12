---
name: mcp-sandboxing
type: mcp
description: >
  Pattern for sandboxing MCP tool execution — isolating tools/commands the server runs
  so a compromised/abused call can't reach the host or out-of-scope targets.
references:
  - skills/ai-security/agent-security/agent-sandboxing
  - _shared/safe-execution-rules.md
license: MIT
version: 1.0.0
---

# Pattern: MCP Execution Sandboxing

When an MCP server runs tools/commands, isolate that execution so a malicious or
mis-scoped call can't compromise the host, reach internal systems, or hit out-of-scope
targets.

## Principles
1. **Isolated execution** — run tools in an ephemeral, least-privilege sandbox
   (container/microVM), not on the host.
2. **Restricted egress (core)** — network limited to in-scope targets; block internal/
   metadata (SSRF-style) ranges; prevent the tool from pivoting.
3. **Resource bounds** — CPU/memory/time limits; no persistence between calls.
4. **Scoped credentials** — the sandbox holds only the minimal, short-lived credentials
   the tool needs.

## Checklist
- [ ] Ephemeral isolated runtime per call
- [ ] Egress allow-list to in-scope targets; internal/metadata blocked
- [ ] Resource/time limits; no persistence
- [ ] Minimal scoped credentials; host not reachable

Mirror of agent-security/agent-sandboxing applied to MCP tool execution.
