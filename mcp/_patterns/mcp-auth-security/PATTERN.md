---
name: mcp-auth-security
type: mcp
description: >
  Pattern for MCP authentication/authorization and secrets — per-user authZ, scoped
  short-lived credentials, and avoiding the confused-deputy problem.
references:
  - skills/ai-security/mcp-security/mcp-auth-security
  - skills/identity-iam/non-human-identity
license: MIT
version: 1.0.0
---

# Pattern: MCP Auth & Secrets

MCP servers often hold powerful backend credentials and act for users — a credential
honeypot and confused-deputy risk. Secure identity end-to-end.

## Principles
1. **Authenticate callers** — no anonymous powerful access to the MCP server.
2. **Per-user authorization (core)** — act within the **calling user's** rights, not a
   shared powerful identity; prevents confused-deputy.
3. **Scoped, short-lived backend credentials** — least-privilege, rotated; prefer
   dynamic/federated over long-lived static secrets (non-human-identity, secrets-vault).
4. **Audit** — log who did what via the server.

## Checklist
- [ ] Client authentication required
- [ ] Per-user/tenant authorization on every tool/data access
- [ ] Backend credentials vaulted, least-privilege, short-lived, rotated
- [ ] No single shared service credential for all users
- [ ] Full audit trail
