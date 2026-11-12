---
name: secrets-management
description: >
  Use when designing how an application handles secrets — using a secret manager,
  short-lived credentials, avoiding secrets in code/config/logs, and rotation.
  Covers secure secret lifecycle in applications.
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: [vault]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Application Secrets Management

Handle secrets so they never leak and can be rotated: store them in a secret
manager (not code/config/env-in-repo), inject at runtime, prefer short-lived
dynamic credentials, keep them out of logs/errors, and make rotation routine.

## When to use
Designing/reviewing how an app obtains and uses credentials/keys/tokens.

## Procedure (gated phases)
1. **No secrets in code/repo** — remove hardcoded secrets; use a secret manager +
   runtime injection (see also supply-chain, secret-scanning).
2. **Prefer short-lived/dynamic** — dynamic DB/cloud credentials and short-lived
   tokens over long-lived static secrets.
3. **Prevent leakage** — keep secrets out of logs, error messages, and client
   bundles; scrub where needed.
4. **Rotation** — routine, automated rotation; immediate on exposure.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Correct" = no secrets in code/logs/client;
managed, rotatable, least-privilege secrets.

## Quality bar / pitfalls
- Secrets in env committed to repo, in client JS, or logged.
- Long-lived static secrets never rotated.

## Linkage
- Pairs with secret-scanning, identity-iam (secrets-management-vault), supply-chain.

## References
- `_shared/` rules (evidence).
