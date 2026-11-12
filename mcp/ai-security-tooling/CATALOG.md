---
name: ai-security-tooling-mcp
type: mcp
description: >
  MCP integrations exposing AI-security tooling (LLM scanners, eval/red-team harnesses)
  to agents for automated AI red-teaming and guardrail validation.
references:
  - mcp/_patterns/mcp-auth-security
  - _shared/scope-authorization-rule.md
license: MIT
version: 1.0.0
---

# AI-Security Tooling MCP Catalog

Expose AI-security tooling to agents (llm-red-teamer) for scaled, automated testing of
authorized models/apps.

## Integrations (tool → used by skill)
| MCP tool | Wraps | Used by |
|---|---|---|
| `garak-mcp` | garak | ai-red-team/garak-probes |
| `promptfoo-mcp` | promptfoo | ai-red-team/promptfoo-eval |
| `pyrit-mcp` | PyRIT | ai-red-team/pyrit-orchestration |
| `llm-guard-mcp` | LLM Guard | llm-security/guardrail-design (validation) |

## Security requirements
- Target only own/in-scope models (scope-authorization); the goal is robustness, not
  harmful output.
- Authenticated, rate-limited; results validated (automated judges aren't ground truth).

## Notes
These tools probe LLMs for weaknesses — results feed guardrail-design + regression
evals (promptfoo). Keep target scope explicit and authorized.
