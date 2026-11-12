---
name: mcp-tool-schema-design
type: mcp
description: >
  Pattern for designing safe MCP tool schemas — minimal, well-typed, validated tool
  definitions that constrain what the model can request.
references:
  - skills/ai-security/mcp-security/mcp-tool-poisoning
license: MIT
version: 1.0.0
---

# Pattern: MCP Tool Schema Design

The tool schema is the contract the model drives — and read by the model, so it's also
untrusted content a malicious server could weaponize. Design schemas to constrain the
model and to be trustworthy.

## Principles
1. **Minimal surface** — one clear purpose per tool; avoid broad/multi-purpose tools.
2. **Strong typing + constraints** — enums/patterns/ranges on parameters so the model
   can't pass arbitrary/dangerous values; required vs optional explicit.
3. **No capability leakage** — the schema shouldn't let a model request more than the
   tool's intended scope (e.g., arbitrary paths/URLs/commands).
4. **Trust the source** — when consuming third-party tools, their schema/description is
   untrusted (mcp-tool-poisoning) — pin + vet.

## Design checklist
- [ ] Single clear purpose; least capability
- [ ] Typed/bounded parameters (enums/patterns/ranges)
- [ ] No arbitrary command/path/URL inputs without allow-listing
- [ ] Description accurate + non-instruction-laden (no hidden directives)
- [ ] Versioned + pinned for third-party tools
