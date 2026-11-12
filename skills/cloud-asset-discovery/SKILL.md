---
name: cloud-asset-discovery
description: >
  Use when discovering an authorized target's cloud-hosted assets — storage
  buckets (S3/Azure Blob/GCS), cloud IP ranges, exposed cloud services, and
  shadow/forgotten cloud resources — to map the cloud attack surface. Covers
  discovery, exposure validation and remediation.
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

# Cloud Asset Discovery (authorized)

Find the target's cloud-hosted assets — object storage, cloud IP ranges, and
exposed managed services — including shadow/forgotten resources outside the core
inventory. Public storage exposure is a frequent, high-impact finding.

> Authorized testing only. Only access resources in scope; read the minimum to
> confirm exposure (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; org naming conventions/keywords. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Bucket/resource naming** — derive likely bucket/resource names from org/
   product keywords and known patterns.
2. **Discovery** — enumerate storage (S3/Blob/GCS) and cloud services associated
   with target IP ranges/certs (from osint-infra).
3. **Exposure validation (first gate)** — determine which are public/listable;
   confirm sensitive exposure **minimally** (e.g., a listing or one benign object),
   no bulk download.
4. **Record** — cloud asset inventory + exposures in `OUTPUT_DIR`.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: cloud asset list + validated
exposures. Private/denied → not exposed.

## Impact escalation
Public storage = direct data exposure; exposed services feed cloud-infra testing;
shadow resources = unmanaged risk (feeds easm). CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Third-party/shared buckets misattributed — verify ownership.
- Keep reads minimal; never bulk-exfiltrate.

## Remediation
- Block public access by default; least-privilege bucket/resource policies; cloud
  asset inventory + CSPM; continuous exposure monitoring (easm).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
