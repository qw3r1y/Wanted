---
name: secret-scanning
description: >
  Use when scanning code, history, and artifacts for exposed secrets — detection
  patterns, entropy, validation, history scanning, and remediation (rotation).
  Covers program setup and triage to prevent credential leaks.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [trufflehog, gitleaks]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Secret Scanning

Find secrets before attackers do — scan code, full git history, CI configs, and
artifacts for credentials/keys/tokens, validate which are live, and drive rotation.
History and validation matter: secrets persist in old commits, and only live
secrets are urgent.

## When to use
Continuously (CI + pre-commit) and as an audit across repos/history.

## Procedure (gated phases)
1. **Scan broadly** — code + **full history** + CI config + build artifacts; use
   pattern + entropy detection.
2. **Validate (first gate)** — distinguish live secrets from placeholders/expired;
   classify provider/type (see api/api-key-leakage for scope).
3. **Triage & prioritize** — by liveness + scope/blast radius.
4. **Remediate** — rotate exposed secrets, purge from history, move to a secret
   manager.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record validated exposures + rotation status;
placeholders → informational.

## Quality bar / pitfalls
- Scanning current tree only (missing history) → missed secrets.
- Alert fatigue from placeholders — validate.

## Deployment
- Pre-commit + CI gates; periodic history audits; developer education.

## References
- `_shared/` rules (evidence).
