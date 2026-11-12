---
name: mcp-server-authoring
type: mcp
description: >
  Pattern for building a secure MCP server that exposes tools/data to an agent —
  least-privilege design, validated tools, and the security controls from
  ai-security/mcp-security.
references:
  - skills/ai-security/mcp-security/mcp-server-hardening
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Pattern: Secure MCP Server Authoring

Build an MCP server as high-privilege infrastructure bridging a model to real systems.
Default to least capability, validate everything the model supplies, and gate
consequential actions.

## Principles
1. **Least-privilege tools** — expose only needed tools, minimally scoped; separate
   read/write; never a "run anything"/raw-shell tool.
2. **Validate inputs** — the model supplies arguments (possibly via injection) → treat
   as untrusted; allow-list/type/bound them.
3. **Gate consequential actions** — confirmation/human gate for irreversible/high-impact
   tools; rate + scope limits.
4. **AuthN/AuthZ + audit** — authenticate clients; authorize per tool/data; log every
   call (see mcp-auth-security).

## Build checklist
- [ ] Tool schemas minimal + validated (mcp-tool-schema-design)
- [ ] Gateway wraps execution (run-tool-gateway-pattern) + sandbox (mcp-sandboxing)
- [ ] Per-user authorization (not a shared powerful identity)
- [ ] Action gating + rate limits + audit logging
- [ ] Tool metadata/output treated as untrusted downstream

See skills/ai-security/mcp-security/* for the full security assessment of these.
