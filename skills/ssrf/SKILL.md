---
name: ssrf
description: >
  Use when testing an authorized web target for Server-Side Request Forgery —
  any feature where the server fetches a user-influenced URL (webhooks, link
  previews, PDF/image generators, importers, SSO metadata, proxies). Covers
  surface discovery, blind out-of-band confirmation, cloud-metadata and internal
  pivoting, protocol smuggling, impact and remediation. Do NOT use for pure
  client-side redirects (see offensive/web/open-redirect).
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
  - references/cloud-metadata-and-protocols.md
license: MIT
version: 1.0.0
---

# SSRF — Server-Side Request Forgery (authorized testing)

Make the server issue requests of your choosing, then prove where those requests
actually go. SSRF value is the **network position it grants** — reaching cloud
metadata, internal services, and link-local addresses the attacker cannot touch
directly. For blind cases, no out-of-band callback = no finding.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Internal/
> metadata pivoting must stay within the engagement's defined network scope;
> stop and ask at any boundary (`safe-execution-rules.md`).

## When to use
Any feature that fetches a URL server-side: webhooks, link/URL previews, PDF and
screenshot generators, image/avatar fetchers, document/feed importers, SSO/OIDC
metadata URLs, XML parsers (SSRF-via-XXE), proxy/gateway params, and "fetch from
URL" integrations.

**Crown-jewel outcomes:** cloud instance-metadata (AWS IMDS, GCP, Azure IMDS) →
temporary credentials; internal admin panels / databases reachable only from the
app tier; and protocol-smuggling to internal services (e.g., gopher → Redis).

## Prerequisites
- Authorization + network scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.
- A unique, sub-tagged OOB listener (DNS + HTTP) — **mandatory** for blind SSRF.

## Procedure (gated phases)

### Phase 1 — Surface discovery
Enumerate every server-fetch feature and its URL parameter (direct or indirect —
sometimes a hostname field, a webhook config, or an XML external entity). Note
whether the response body is returned (full-response SSRF) or not (blind).

### Phase 2 — Confirm the server fetches (first gate)
Point the parameter at your unique OOB host; sub-tag by feature so callbacks are
attributable.
```bash
# Plant a unique beacon; keep the listener open.
curl --max-time 30 --connect-timeout 10 -sk \
  "https://target/fetch?url=http://ssrf-<feature>-<rand>.<collab>/probe"
```
- **Confirmation** = a request to your unique subdomain from the *server's* IP/UA.
- **Not confirmation** = your own browser resolving it, or an error echoing the URL.

### Phase 3 — Classify & assess reach
- **Full-response SSRF:** read internal responses directly — map reachable hosts/
  ports minimally.
- **Blind SSRF:** rely on OOB timing/DNS to infer reachability.
Test whether filters allow internal/link-local targets, and how they resolve
redirects and DNS (SSRF filters are often bypassable via redirects, DNS
rebinding, alternate IP encodings, or IPv6 — `references/cloud-metadata-and-protocols.md`).

### Phase 4 — Controlled impact demonstration
With explicit scope approval, demonstrate the *minimum* that proves severity:
a single read of cloud-metadata (prove credential exposure without exfiltrating/
using them) or reaching one internal service banner. Never pivot beyond scope,
never use recovered credentials.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, SSRF class
(full/blind), the OOB callback log, which internal target was reachable, and
reproduction. A reflected URL or a connection error is a **signal**, not
confirmation.

## Impact escalation
Cloud credential theft via metadata, internal service access (admin panels,
caches, databases), SSRF→RCE via protocol smuggling, internal port scanning, and
SSRF-chained request forgery. State the concrete internal asset reached. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- URL reflected in response ≠ server fetched it. Require an OOB callback.
- A fetch of *your* external host proves SSRF exists but not internal reach —
  separate the two claims.
- WAF/allow-list that blocks internal targets → SSRF may be **low/refuted** for
  impact even if the fetch works; say so precisely.
- Do not hammer internal ranges; keep probes minimal and bounded.

## Remediation
- **Allow-list** outbound destinations (scheme + host); deny by default; block
  link-local/metadata ranges (169.254.0.0/16, fd00:ec2::254) at the app and
  network layer.
- Resolve and validate the final destination **after** redirects; pin DNS to
  prevent rebinding; disable unneeded URL schemes (file, gopher, dict, ftp).
- Enforce IMDSv2 (session-token) on AWS and equivalent metadata hardening;
  isolate the egress of fetchers; drop raw responses back to the client.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/cloud-metadata-and-protocols.md` — metadata endpoints, filter-bypass classes, protocol smuggling (4th level).
