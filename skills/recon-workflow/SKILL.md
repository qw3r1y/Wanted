---
name: recon-workflow
description: >
  Use when running an efficient bug-bounty recon workflow — chaining subdomain
  discovery, content/endpoint discovery, and surface mapping into a repeatable
  pipeline that finds the forgotten assets where bugs live. Covers recon
  orchestration for hunting.
type: knowledge
domain: bug-bounty
maturity: canonical
tools: [subfinder, httpx, katana]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Bug Bounty Recon Workflow

Bounties are often won in recon — finding the forgotten subdomain, the old API, the
unlinked endpoint others missed. Chain the recon skills into a repeatable, in-scope
pipeline that broadly maps the target's surface, so you test what others overlooked.

> Strictly in-scope (`_shared/scope-authorization-rule.md`); respectful rate
> (`safe-execution-rules.md`).

## When to use
After scope analysis, to build the testable surface.

## Procedure (gated phases)
1. **Subdomain discovery** — passive + active enumeration of in-scope apexes
   (offensive/recon-osint/subdomain-enumeration); resolve + probe live.
2. **Surface triage** — fingerprint tech, flag interesting hosts (admin/dev/staging/
   old versions), and dangling-DNS/takeover candidates.
3. **Content/endpoint discovery** — crawl + JS endpoint extraction + parameter
   discovery on promising hosts (content-discovery).
4. **Organize** — a prioritized target list feeding attack-surface-mapping + the
   vuln-class skills.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: an in-scope, prioritized surface
inventory.

## Impact / output
Breadth of attack surface → more unique findings.

## Pitfalls
- Scope creep into out-of-scope subdomains — validate against program scope.
- Noisy brute-force → rate-limits/bans.

## Linkage
- Orchestrates recon-osint skills; feeds attack-surface-mapping + hunting.

## References
- `_shared/` rules (authorization, safe execution, evidence).
