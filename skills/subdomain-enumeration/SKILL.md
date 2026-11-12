---
name: subdomain-enumeration
description: >
  Use when enumerating an authorized target's subdomains — passive sources,
  active brute-force/permutation, and resolution/validation — to expand the attack
  surface and find forgotten/dev/staging hosts. Covers discovery, validation and
  takeover-signal flagging.
type: knowledge
domain: offensive/recon-osint
maturity: canonical
tools: [curl, subfinder, httpx]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Subdomain Enumeration (authorized)

Discover the full set of a target's subdomains (especially forgotten dev/staging/
admin hosts), validate which resolve and respond, and flag dangling records for
takeover. Breadth here directly drives the rest of the engagement.

> Authorized testing only. Keep active brute-force bounded and within scope
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope (which apex domains / wildcards are in scope).
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Passive sources** — CT logs, passive DNS, search/data aggregators (from
   passive-recon).
2. **Active discovery (bounded)** — DNS brute-force + permutation/alteration on
   known names; respect rate and scope.
3. **Resolve & probe** — resolve candidates, probe HTTP(S), capture status/title/
   tech; separate live from dead.
4. **Flag takeover signals** — subdomains with dangling CNAMEs to unclaimed
   third-party services → candidate subdomain-takeover (confirm carefully).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: validated live-subdomain
inventory + takeover candidates with evidence.

## Impact escalation
Expanded surface for every app test; subdomain takeover can be a direct finding
(see easm/takeover-detection).

## False positives & pitfalls
- Wildcard DNS inflating results — detect and filter wildcards.
- Out-of-scope subdomains — mark and exclude.

## Remediation
- Inventory and retire stale DNS records; remove dangling CNAMEs; monitor for new
  subdomains; restrict dev/staging exposure.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
