---
name: mcp-server-hardening
description: >
  Use when securing an MCP (Model Context Protocol) server — authentication,
  authorization, input validation, and least-privilege tool exposure — so an MCP
  server doesn't become an over-powerful, under-secured bridge between an LLM and
  real systems. Covers MCP server security.
type: knowledge
domain: ai-security/mcp-security
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# MCP Server Hardening

An MCP server exposes tools/data to an LLM/agent — making it a powerful bridge to
real systems and a prime target. Harden it: authenticate/authorize callers, validate
all tool inputs, expose least-privilege capabilities, and gate consequential
actions, so a manipulated model can't abuse the server.

## When to use
When building/reviewing an MCP server or its deployment.

## Procedure (gated phases)
1. **AuthN/AuthZ** — authenticate clients; authorize which tools/data each may use;
   no anonymous powerful access.
2. **Least-privilege tools** — expose only needed tools, minimally scoped; separate
   read/write; avoid "run anything" tools.
3. **Input validation** — validate/constrain all tool arguments (the model supplies
   them, possibly via injection); treat them as untrusted.
4. **Gate consequential actions** — confirmation/human-gate for irreversible/
   high-impact tools; rate/scope limits; audit logging.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Hardened" = authenticated, authorized,
least-privilege, validated, with gated high-impact actions. Validate via testing.

## Quality bar / pitfalls
- Unauthenticated/over-powerful MCP servers (RCE/data bridges).
- Trusting model-supplied tool args; no action gating.

## Linkage
- Pairs with tool-abuse-defense, mcp-tool-poisoning, mcp-auth-security.

## References
- `_shared/` rules (untrusted input, evidence, gated workflow).
