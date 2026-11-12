---
name: passive-recon
description: >
  Use when building an authorized target's footprint without touching its
  infrastructure — passive DNS, certificate transparency, ASN/IP mapping, WHOIS/
  RDAP, archives, and tech fingerprinting from third-party data. Produces the
  low-noise footprint that seeds active recon. Do NOT use for active scanning
  (see port-service-scan, subdomain-enumeration active modes).
type: knowledge
domain: offensive/recon-osint
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Passive Reconnaissance (authorized)

Map the target's external footprint using only third-party/public data sources, so
you understand scope and attack surface before sending a single packet to the
target. Low noise, high value for scoping.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Stay within the
> approved scope when deciding what to pursue (`safe-execution-rules.md`).

## When to use
At engagement start, and to keep scope current.

## Prerequisites
- Authorization + scope recorded. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Organization mapping** — WHOIS/RDAP, ASN and owned IP ranges, acquisitions,
   brands.
2. **Passive DNS & certificates** — certificate transparency logs, passive-DNS
   datasets → hostnames/subdomains without querying the target.
3. **Archive & exposure mining** — wayback/archives, public code/paste exposure,
   and tech fingerprints from third-party datasets.
4. **Consolidate** — a scoped footprint (domains, IPs, ASNs, tech) in `OUTPUT_DIR`,
   flagging in-scope vs out-of-scope.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable is the footprint; mark
inferred-but-unconfirmed assets.

## Impact escalation
Seeds subdomain-enumeration, content-discovery, and cloud-asset-discovery; exposed
data (keys/old hosts) may be findings themselves.

## False positives & pitfalls
- Shared infra/third-party assets wrongly attributed — verify ownership before
  treating as in-scope (see easm/confidence-scoring mindset).

## Remediation
- Minimize public exposure (WHOIS privacy, trimmed certs/metadata); inventory and
  retire stale assets; monitor certificate-transparency for unexpected hostnames.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
