---
name: osint-infra
description: >
  Use when mapping an authorized target's infrastructure from public data —
  technologies, third-party services, email/DNS security posture, exposed devices
  via internet-scan datasets (Shodan/Censys), and vendor relationships. Low-touch
  surface and risk mapping.
type: knowledge
domain: offensive/recon-osint
maturity: canonical
tools: [curl, shodan]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Infrastructure OSINT (authorized)

Characterize the target's tech and infrastructure from public internet-scan data
and metadata — exposed services, technologies, third-party/vendor dependencies,
and email/DNS security posture — without actively probing the target.

> Authorized testing only. Use public datasets; only pursue in-scope assets
> (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope; known domains/IPs/ASNs (from passive-recon). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Internet-scan datasets** — query Shodan/Censys-style data for the target's IPs/
   certs → exposed services, software, open ports (as seen by third parties).
2. **Tech & vendor mapping** — identify stacks, CDNs, cloud providers, SaaS, and
   third-party integrations.
3. **Email/DNS posture** — SPF/DKIM/DMARC, DNSSEC, mail security (feeds
   email-security).
4. **Consolidate** — an infra/risk map in `OUTPUT_DIR`, flagging notable exposures.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: infra map; third-party data
may be stale — note confidence.

## Impact escalation
Exposed services → network/vuln-mgmt targets; weak email posture → phishing risk;
vendor map → supply-chain considerations.

## False positives & pitfalls
- Stale scan data; shared-hosting misattribution — verify ownership.

## Remediation
- Reduce exposed services; strong SPF/DKIM/DMARC + DNSSEC; vendor inventory;
  monitor internet-scan exposure of owned ranges (see easm).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
