---
name: content-discovery
description: >
  Use when discovering hidden paths, files, parameters, and endpoints on an
  authorized web target — directory/file brute-force, JS endpoint extraction,
  parameter discovery, and backup/exposed-file hunting. Expands the testable
  surface of a host.
type: knowledge
domain: offensive/recon-osint
maturity: canonical
tools: [curl, ffuf, katana]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Content & Endpoint Discovery (authorized)

Find the paths, files, parameters, and endpoints a target exposes beyond what is
linked — admin panels, backups, debug endpoints, API routes, and hidden
parameters — turning a single host into a full testable surface.

> Authorized testing only. Keep brute-force bounded; respect rate limits
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; target host list (from subdomain-enumeration).
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Crawl** — spider the app; extract links, forms, and endpoints from HTML/JS
   bundles (JS often holds API routes and params).
2. **Directory/file brute-force (bounded)** — wordlist-driven discovery of paths,
   backups (`.bak`, `.old`, `.zip`), configs, and debug/admin endpoints; tune by
   observed tech.
3. **Parameter discovery** — find hidden/undocumented parameters the endpoint
   honors (fuzzing param names).
4. **Catalogue** — endpoints + params + interesting files in `OUTPUT_DIR` for the
   app-testing skills.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: the endpoint/param/file
inventory; verify interesting hits (don't report 200-soft-404s).

## Impact escalation
Feeds web/api testing; exposed backups/configs/debug endpoints can be direct
findings.

## False positives & pitfalls
- Soft-404s / catch-all routes inflating results — calibrate against a known-bad
  path.
- Respect scope and rate; avoid destructive paths.

## Remediation
- Remove backups/debug/admin exposure; enforce authz on all discovered endpoints;
  avoid leaking routes/params in client JS; add monitoring for scanning.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
