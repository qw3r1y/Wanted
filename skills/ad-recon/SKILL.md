---
name: ad-recon
description: >
  Use when enumerating an authorized Active Directory environment — domain/forest
  mapping, users/groups/computers, trusts, GPOs, and attack-path analysis with
  BloodHound. Produces the AD attack graph that drives every later AD test.
type: knowledge
domain: offensive/active-directory
maturity: canonical
tools: [bloodhound, ldap]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Active Directory Reconnaissance (authorized)

Build the picture of an authorized AD environment — domains, trusts, principals,
privileged groups, GPOs, and the relationships between them — and compute attack
paths (e.g., with BloodHound). This graph is the foundation for prioritizing every
AD attack-path test defensively.

> Authorized testing only, from an in-scope foothold/account
> (`_shared/scope-authorization-rule.md`). Collection can be noisy — respect scope
> and detection expectations (`safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; a low-priv domain context. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Domain/forest map** — domains, trusts, DCs, functional levels.
2. **Principals & privileges** — users, groups (esp. privileged), computers,
   service accounts (SPNs), and delegation settings.
3. **GPO & ACLs** — GPO links and interesting ACLs (who can modify what).
4. **Attack-path analysis** — ingest into BloodHound; identify shortest paths from
   owned principals to high-value targets (DA/EA).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: the AD graph + prioritized
attack paths (each links to its technique skill).

## Impact escalation
Reveals kerberoast/ASREP targets, delegation/ADCS/ACL abuse paths, and lateral
routes — prioritizing the highest-impact tests.

## False positives & pitfalls
- Stale/disabled objects in the graph; validate before acting.
- Collection is detectable; coordinate with the engagement's detection goals.

## Remediation
- Tier administration; prune privileged group membership and dangerous ACLs;
  monitor LDAP recon/BloodHound collection; least-privilege service accounts.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
