---
name: offensive-tooling-mcp
type: mcp
description: >
  MCP server integrations that expose offensive security tools to an agent via a
  controlled gateway. Each runs behind the run-tool-gateway + sandboxing + auth
  patterns — never raw shell exposure.
references:
  - mcp/_patterns/run-tool-gateway-pattern
  - mcp/_patterns/mcp-sandboxing
  - mcp/_patterns/mcp-auth-security
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
license: MIT
version: 1.0.0
---

# Offensive Tooling MCP Catalog

Expose offensive tools to agents through a **controlled gateway** (run_tool /
run_pipeline), not arbitrary shell — each tool wrapped, argument-validated, scoped,
and sandboxed. Authorization + scope are enforced at the gateway.

> Every tool runs only against in-scope, authorized targets (scope-authorization-rule),
> bounded (safe-execution-rules). The gateway validates args and blocks out-of-scope.

## Integrations (tool → used by skill)
| MCP tool | Wraps | Used by |
|---|---|---|
| `nmap-mcp` | nmap | recon-osint/port-service-scan, network/network-scanning |
| `nuclei-mcp` | nuclei | content-discovery, web/*, cve-weaponization |
| `ffuf-mcp` | ffuf | recon-osint/content-discovery |
| `subfinder-httpx-mcp` | subfinder+httpx | recon-osint/subdomain-enumeration |
| `amass-mcp` | amass | recon-osint/subdomain-enumeration, easm |
| `katana-mcp` | katana | recon-osint/content-discovery |
| `burp-mcp` | Burp (REST) | web/* (proxy/repeater-driven) |
| `sqlmap-mcp` | sqlmap | web/sqli (bounded; confirmed oracle only) |
| `metasploit-mcp` | metasploit (RPC) | exploit-dev/* (lab/authorized only) |
| `recon-pipeline-mcp` | chained recon | agents/recon-orchestrator |

## Security requirements (per integration)
- Argument allow-listing + scope validation at the gateway (no arbitrary flags/targets).
- Sandboxed execution (mcp-sandboxing); egress limited to in-scope targets.
- Authenticated, authorized calls (mcp-auth-security); audit every invocation.
- Consequential/destructive tool modes gated (gated-workflow).

## Notes
These expose real tooling — treat the MCP server as high-privilege infrastructure and
harden it (mcp/_patterns/*). Never expose a raw-shell "run anything" tool.
