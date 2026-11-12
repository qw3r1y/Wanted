---
name: dependency-policy-rules
type: rule
description: >
  Rules for adding/using dependencies safely — trust, pinning, and vulnerability
  awareness when the assistant introduces packages.
references: [skills/appsec/supply-chain/*, skills/appsec/sast-dast/dependency-scanning]
license: MIT
version: 1.0.0
---

# Dependency Policy Rules (assistant)

When adding dependencies:
- Prefer **well-maintained, widely-used, reputable** packages; avoid abandoned/obscure
  ones (supply-chain risk).
- **Pin versions** with integrity hashes/lockfiles; don't float to `latest`.
- Beware **typosquatting / dependency confusion** — verify the exact package name +
  registry; scope internal names.
- Check for **known vulnerabilities** (reachable) before adding; avoid versions with
  critical reachable CVEs.
- Minimize dependencies (reduce transitive surface); avoid packages with suspicious
  install scripts / excess permissions.
- Keep an SBOM; update/patch regularly.
