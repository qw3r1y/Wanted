---
name: secure-coding-cursorrules
type: rule
description: >
  General secure-coding rules for an AI coding assistant — apply by default when
  writing/reviewing application code. Encodes the appsec/secure-coding skills as
  enforceable directives.
references: [skills/appsec/secure-coding/*]
license: MIT
version: 1.0.0
---

# Secure Coding Rules (assistant)

Apply to all code generation/review:
- **Validate untrusted input** at trust boundaries (allow-list); **context-aware output
  encoding** at every sink. Never build HTML/SQL/commands by string concat.
- Use **parameterized queries**, safe templating, and process-arg arrays — never shell
  string interpolation, never native deserialization of untrusted data.
- Enforce **authorization server-side on every request** (object + function level);
  never trust the client.
- No **hardcoded secrets**; use a secret manager; keep secrets out of logs/errors/
  client bundles.
- Use **authenticated encryption** + CSPRNG + strong KDFs; never hand-roll crypto.
- Fail closed; least privilege; keep dependencies patched.
- Prefer memory-safe constructs; avoid language footguns (see language-hardening).
