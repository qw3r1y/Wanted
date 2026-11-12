---
name: network-scanning
description: >
  Use when, in an authorized internal/external network test, discovering hosts,
  services, and exposure across a network — host discovery, service mapping, and
  exposure triage at scale. Complements recon-osint/port-service-scan with an
  internal-network focus.
type: knowledge
domain: offensive/network
maturity: canonical
tools: [nmap]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Network Scanning & Exposure Mapping (authorized)

Across an authorized network, discover live hosts and exposed services, then triage
the exposure — management interfaces, databases, legacy protocols, and outdated
services that warrant deeper testing. Scope and rate discipline protect fragile
internal services.

> Authorized testing only. In-scope ranges only; respectful timing to avoid
> disrupting fragile hosts (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + **in-scope ranges**; a network position. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Host discovery** — enumerate live hosts in scope.
2. **Service mapping** — scan relevant ports; detect services/versions; capture
   banners (untrusted data).
3. **Exposure triage** — flag management (RDP/SSH/WinRM/web-admin), databases,
   file shares, legacy protocols, and outdated versions.
4. **Prioritize** — feed network/ protocol-attacks, exploit, and vuln-mgmt.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: host/service inventory with
exposure flags.

## Impact escalation
Exposed management/database/legacy services are frequent pivot/entry points.

## False positives & pitfalls
- Filtered ≠ closed; IDS skew; verify notable hits.
- Avoid scan intensity that risks disruption.

## Remediation
- Segment and firewall management/database services; patch outdated services;
  disable legacy protocols; monitor internal scanning.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
