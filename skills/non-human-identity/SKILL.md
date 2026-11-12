---
name: non-human-identity
description: >
  Use when securing non-human identities — service accounts, API keys, tokens, CI/CD
  and workload identities — which now vastly outnumber human identities and are a
  top breach vector. Covers NHI inventory, least-privilege, and rotation.
type: knowledge
domain: identity-iam
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Non-Human Identity (NHI) Security

Machines, services, and workloads authenticate too — with service accounts, API
keys, tokens, and certificates that often outnumber humans 10:1, are over-privileged,
rarely rotated, and poorly inventoried. Secure NHIs: inventory them, scope them
least-privilege, prefer short-lived/workload identity, and rotate/retire.

## When to use
Securing service accounts, keys, tokens, and workload identities across the estate.

## Procedure (gated phases)
1. **Inventory NHIs** — service accounts, API keys, tokens, certs, and CI/CD/cloud
   workload identities; who owns each and what it accesses.
2. **Least-privilege** — scope each to only what it needs; remove unused/over-broad
   ones and orphaned accounts.
3. **Prefer short-lived/workload identity** — OIDC/workload identity federation over
   long-lived static keys (ci-cd-devsecops).
4. **Rotate & monitor** — rotate secrets; monitor for anomalous NHI use; secrets in a
   vault (secrets-management-vault).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = NHIs inventoried, least-privilege,
short-lived where possible, rotated, and monitored.

## Quality bar / pitfalls
- Unknown/over-privileged service accounts with long-lived keys (top breach vector).
- Keys in code/config (secret-scanning) — move to managed identity.

## Linkage
- Pairs with secrets-management, cloud-iam-privesc, ci-cd (oidc-workload-identity),
  mcp-auth-security.

## References
- `_shared/` rules (evidence).
