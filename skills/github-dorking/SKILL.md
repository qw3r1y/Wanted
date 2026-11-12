---
name: github-dorking
description: >
  Use when hunting an authorized target's exposed secrets and sensitive data in
  public code — GitHub/GitLab repos, gists, commit history, and org members'
  personal repos — via targeted search and secret scanning. Covers discovery,
  validation of exposure, and remediation.
type: knowledge
domain: offensive/recon-osint
maturity: canonical
tools: [curl, trufflehog, gitleaks]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# GitHub / Code Dorking (authorized)

Search public source for a target's leaked secrets, internal hostnames, and
sensitive config — in org repos, employee personal repos, gists, and **commit
history** (secrets often live in old commits even after deletion).

> Authorized testing only. Only act on exposures within scope; validate secrets
> minimally (see api/api-key-leakage) (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; the target's org names, domains, product keywords.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify sources** — org repos, member accounts, forks, gists; map keywords
   (internal domains, project names).
2. **Targeted search** — dork for secret patterns, internal URLs, credentials,
   and config near target keywords; scan matched repos/commit history with
   secret-scanning tools.
3. **Validate exposure (first gate)** — classify each hit (true secret vs
   placeholder/public); confirm live secrets' scope minimally.
4. **Record** — exposures with location, type, and validity in `OUTPUT_DIR`.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: validated exposure list.
Placeholders/public keys → informational.

## Impact escalation
Live secret leakage → direct access to backing services; internal data aids
further recon. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Example/placeholder secrets; revoked keys → informational.
- Respect scope; employee personal data handling per rules.

## Remediation
- Secret scanning in CI + pre-commit + history; rotate exposed secrets; private
  repos for internal code; developer awareness; purge secrets from history.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
