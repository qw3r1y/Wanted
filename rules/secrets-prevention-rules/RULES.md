---
name: secrets-prevention-rules
type: rule
description: >
  Rules preventing the assistant from introducing secrets into code/config, and
  guiding secure secret handling.
references: [skills/appsec/secure-coding/secrets-management, skills/appsec/sast-dast/secret-scanning]
license: MIT
version: 1.0.0
---

# Secrets Prevention Rules (assistant)

- **Never** hardcode secrets (API keys, passwords, tokens, private keys) in code,
  config, or committed files. Use environment injection from a secret manager.
- Never log secrets or put them in error messages, URLs, or client-side bundles.
- Use example/placeholder values (clearly fake) in samples/docs; store real test
  secrets in a vault or `.env` that is git-ignored.
- Prefer short-lived/dynamic credentials over long-lived static secrets.
- When you detect an existing hardcoded secret, flag it for rotation (it's compromised
  if committed) — don't just move it.
