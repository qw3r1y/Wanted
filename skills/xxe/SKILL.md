---
name: xxe
description: >
  Use when testing an authorized target that parses user-supplied XML (or formats
  backed by XML: SVG, DOCX/XLSX, SOAP, SAML, RSS, SVG uploads) for XML External
  Entity injection. Covers detection, in-band vs blind/OOB confirmation, SSRF and
  file-read reach, and remediation. Do NOT use for JSON-only endpoints.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, oob-listener]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
  - references/xml-vectors.md
license: MIT
version: 1.0.0
---

# XXE — XML External Entity Injection (authorized testing)

Find XML parsers that resolve external entities, and prove the parser reaches
something it should not — local files, internal URLs (SSRF), or an OOB endpoint.
XXE often hides inside XML-backed formats (SVG, Office documents, SAML, SOAP),
not just obvious `.xml` endpoints.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Read the
> **minimum** needed to prove the class; no bulk file exfiltration
> (`safe-execution-rules.md`).

## When to use
Any endpoint that parses XML: API bodies with `Content-Type: application/xml` or
`text/xml`, SOAP services, SAML assertions, RSS/Atom importers, sitemap/feed
parsers, and **file uploads** that are secretly XML (SVG, DOCX/XLSX/PPTX, which
are zipped XML). Also test formats that *downgrade* to XML parsing.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.
- A unique OOB listener (DNS + HTTP) — mandatory for blind XXE.

## Procedure (gated phases)

### Phase 1 — Identify XML intake
Find where XML is accepted (directly or inside an uploaded format). Confirm the
parser processes a DOCTYPE/entity by submitting a benign internal entity and
checking whether it is expanded in the response.

### Phase 2 — In-band vs blind (first gate)
- **In-band:** a defined entity's value appears in the response → direct read.
- **Blind:** no reflection → rely on **OOB**. Point an external entity at your
  unique sub-tagged host and confirm the parser connects (out-of-band DTD
  technique). A callback from the server is the proof.

### Phase 3 — Reach classification
Determine what the parser can reach: local file read (via `file:` where allowed),
internal URLs (SSRF via `http:`), or OOB only. Note parser/platform quirks
(encoding tricks, parameter entities for blind extraction). Keep reads minimal.

### Phase 4 — Controlled impact
With scope approval, prove the minimum: read a benign local file (e.g., a
non-sensitive system file) or reach one internal endpoint via OOB — enough to
establish severity without exfiltrating sensitive data.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, XXE class (in-band/
blind/SSRF/file-read), the entity expansion or OOB callback proof, and the format
it rode in (raw XML / SVG / Office). An echoed entity literal without expansion →
**refuted**.

## Impact escalation
Local file disclosure (configs, secrets), SSRF into internal/metadata services,
denial-of-service (entity expansion — do not actually trigger), and
authentication bypass via SAML XXE. State the concrete asset reached. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Parser rejects DOCTYPE / entity not expanded → **refuted** (hardened parser).
- Error referencing your entity ≠ expansion; require value read or OOB callback.
- Never trigger billion-laughs/entity-expansion DoS against a live target.

## Remediation
- **Disable DTDs and external entities** in the XML parser (the single most
  effective fix); use parser-hardening flags for the platform.
- Prefer non-XML formats (JSON) where possible; validate and reject DOCTYPEs.
- Treat XML-backed uploads (SVG/Office) as XML intake and parse them with the
  same hardening; isolate parser egress.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/xml-vectors.md` — XML-backed formats, in-band/blind/parameter-entity techniques, parser quirks (4th level).
