---
name: run-tool-gateway-pattern
type: mcp
description: >
  Pattern for safely exposing CLI/security tools to agents via a controlled gateway
  (run_tool / run_pipeline) instead of raw shell — the safe way to give agents real
  tooling.
references:
  - mcp/_patterns/mcp-sandboxing
  - _shared/safe-execution-rules.md
  - _shared/scope-authorization-rule.md
license: MIT
version: 1.0.0
---

# Pattern: Run-Tool Gateway

To let an agent use real tools (nmap, nuclei, etc.) without handing it a shell, route
execution through a controlled gateway that wraps each tool, validates inputs, enforces
scope, and sandboxes execution.

## Principles
1. **No raw shell** — expose specific wrapped tools (`run_tool`/`run_pipeline`), never a
   generic command executor.
2. **Validate + scope args** — allow-list flags/targets; reject out-of-scope targets and
   dangerous options at the gateway (scope-authorization).
3. **Sandbox execution** — run each tool isolated with bounded egress (mcp-sandboxing);
   time/resource limits.
4. **Gate + audit** — gate destructive tool modes; audit every invocation; bounded rate.

## Benefits
- Agents get powerful tooling with the safety of wrapping/validation/sandboxing.
- Scope + authorization enforced centrally, not per-prompt.

## Checklist
- [ ] Specific wrapped tools, no raw shell
- [ ] Arg allow-listing + scope validation
- [ ] Sandboxed, egress-limited execution + limits
- [ ] Destructive modes gated; full audit
