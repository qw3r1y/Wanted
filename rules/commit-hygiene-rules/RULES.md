---
name: commit-hygiene-rules
type: rule
description: >
  Rules for secure commit/VCS hygiene — prevent leaking secrets/sensitive data and keep
  history clean when the assistant commits.
references: [skills/appsec/sast-dast/secret-scanning, skills/ci-cd-devsecops/secret-scanning-in-pipeline]
license: MIT
version: 1.0.0
---

# Commit Hygiene Rules (assistant)

- **Never commit secrets** or sensitive data; run/assume secret scanning pre-commit; if
  a secret was committed, treat it as compromised → rotate + purge history.
- Keep `.env`, keys, and local config **git-ignored**; commit example/placeholder
  configs only.
- Don't commit large binaries, build artifacts, or dependency trees.
- Write clear commit messages; avoid embedding sensitive context (internal hostnames,
  credentials, customer data) in messages/PRs.
- Review diffs for accidentally-included secrets/PII before committing.
- Respect signing/branch-protection; don't bypass hooks.
