---
name: lateral-movement-persistence
description: >
  Use when, in an authorized AD engagement, assessing lateral-movement and
  persistence exposure — delegation abuse, ACL-based paths, and privileged-ticket/
  persistence techniques — focused on identifying the paths and the detection/
  remediation that close them. Defensive, path-mapping framing.
type: knowledge
domain: offensive/active-directory
maturity: canonical
tools: [bloodhound, impacket]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# AD Lateral Movement & Persistence — Path Assessment (authorized)

Map and (minimally) demonstrate the paths by which an attacker moves laterally and
persists in AD — delegation abuse (unconstrained/constrained/RBCD), ACL-based
escalation, and privileged-ticket/persistence techniques — to show reachability of
high-value targets and drive remediation.

> Authorized testing only. Demonstrate reachability of a path minimally on test
> principals; avoid establishing real persistence on production
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; the AD attack graph (from ad-recon). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Delegation review** — unconstrained/constrained/resource-based delegation
   that enables impersonation to privileged targets.
2. **ACL path review** — dangerous ACLs (GenericAll/Write, AddMember, ForceChange-
   Password) forming escalation chains from owned principals.
3. **Movement/persistence techniques** — identify where privileged tickets/
   persistence (golden/silver-style, DCShadow-style) would be possible given the
   graph; reason about detection.
4. **Minimal demonstration** — prove one path's reachability on test principals;
   do not persist on production.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the path (delegation/ACL/
ticket), and minimal reachability proof. No exploitable path → **refuted**.

## Impact escalation
Domain compromise and durable persistence; full environment control. Critical.
CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Paths requiring already-high privilege aren't escalation — evaluate the starting
  point.
- Don't create lasting persistence on production.

## Remediation
- Remove unnecessary delegation and dangerous ACLs; tier administration; protect
  privileged accounts (Protected Users, no delegation); monitor for golden/silver
  ticket and DCShadow indicators; rotate krbtgt.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
