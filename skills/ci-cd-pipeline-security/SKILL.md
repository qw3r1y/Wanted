---
name: ci-cd-pipeline-security
description: >
  Use when securing a CI/CD pipeline as a supply-chain attack surface — protecting
  build runners, secrets, permissions, and pipeline integrity against poisoned
  builds and credential theft. Overlaps ci-cd-devsecops; here supply-chain focus.
type: knowledge
domain: appsec/supply-chain
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# CI/CD Pipeline Security (supply-chain)

The pipeline that builds and deploys your software is a prime supply-chain target:
a poisoned build or stolen pipeline credential compromises everything downstream.
Secure runner isolation, least-privilege pipeline permissions, protected secrets,
and integrity of build steps.

## When to use
When reviewing/hardening CI/CD from a supply-chain perspective.

## Procedure (gated phases)
1. **Runner security** — isolated/ephemeral runners; no shared mutable state;
   restrict what untrusted (e.g., fork PR) code can do.
2. **Permissions** — least-privilege pipeline tokens/scopes; avoid broad write/
   deploy rights; OIDC workload identity over long-lived keys.
3. **Secret protection** — scoped secrets, no exposure to untrusted jobs/logs;
   protected environments for deploy.
4. **Integrity** — pin actions/images by digest; verify inputs; protected branches
   + required reviews.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = isolated runners, least-privilege,
protected secrets, pinned/verified steps.

## Quality bar / pitfalls
- Untrusted PRs accessing secrets/privileged runners (poisoned pipeline).
- Over-privileged pipeline tokens; unpinned third-party actions.

## Linkage
- Pairs with ci-cd-devsecops, artifact-signing, slsa-provenance.

## References
- `_shared/` rules (evidence).
