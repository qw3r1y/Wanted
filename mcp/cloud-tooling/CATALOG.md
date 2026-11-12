---
name: cloud-tooling-mcp
type: mcp
description: >
  MCP integrations exposing cloud-security tools (CSPM, scanners) to agents with
  read-only, least-privilege cloud access.
references:
  - mcp/_patterns/mcp-auth-security
  - _shared/scope-authorization-rule.md
license: MIT
version: 1.0.0
---

# Cloud Tooling MCP Catalog

Expose cloud-security tooling to agents (cloud-auditor, k8s-security-agent) via
**read-only** cloud access — these tools inventory and assess cloud, so the gateway's
cloud identity must be tightly scoped.

## Integrations (tool → used by skill)
| MCP tool | Wraps | Used by |
|---|---|---|
| `aws-security-mcp` | AWS APIs (read) | cloud-infra/cloud/aws-security-audit |
| `prowler-mcp` | Prowler | cloud/cspm-posture, aws/azure/gcp audit |
| `scoutsuite-mcp` | ScoutSuite | cloud/* audit |
| `trivy-mcp` | Trivy | container-k8s/image-vulnerability-scan |
| `kube-bench-mcp` | kube-bench | container-k8s/* |
| `checkov-mcp` | Checkov | iac/terraform-security-scan, checkov-policy |

## Security requirements
- **Read-only** audit identity, least-privilege, short-lived (prefer OIDC/workload
  identity — see ci-cd/oidc-workload-identity, identity-iam/non-human-identity).
- Per-user/engagement scoping; audit all calls; no write/deploy capability via the
  agent.

## Notes
A cloud MCP with broad credentials is a prime target — scope it to read-only audit and
rotate. Prefer federated short-lived credentials over standing keys.
