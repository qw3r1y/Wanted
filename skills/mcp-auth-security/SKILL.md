---
name: mcp-auth-security
description: >
  Use when securing authentication/authorization and secrets for MCP integrations —
  how the MCP server holds and uses credentials to backend systems, token scope, and
  per-user authorization. Covers the identity/secrets layer of MCP.
type: knowledge
domain: ai-security/mcp-security
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# MCP Authentication & Secrets Security

MCP servers often hold powerful credentials to backend systems and act on behalf of
users. Secure how those credentials are stored and used, scope tokens tightly, and
enforce **per-user** authorization — so the MCP layer doesn't become a credential
honeypot or a confused-deputy that acts beyond a user's rights.

## When to use
When an MCP server authenticates to backends or acts for multiple users.

## Procedure (gated phases)
1. **Credential handling** — how backend credentials/tokens are stored (secret
   manager, not plaintext), scoped, and rotated.
2. **Token scope** — least-privilege, short-lived tokens to backends; avoid broad
   standing credentials.
3. **Per-user authorization (core)** — the MCP server must act within the **calling
   user's** rights, not a shared powerful identity (confused-deputy risk).
4. **Audit** — log who did what via the MCP server.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Secure" = managed least-privilege secrets +
per-user authorization + audit. Validate with testing.

## Quality bar / pitfalls
- A single powerful service credential used for all users (confused deputy).
- Plaintext/broad standing credentials in the MCP server.

## Linkage
- Pairs with mcp-server-hardening, identity-iam (non-human-identity), secrets-mgmt.

## References
- `_shared/` rules (evidence).
