---
name: logging-rules
type: rule
description: >
  Rules for secure, useful logging in generated code — log security events, never log
  secrets, enable detection.
references: [skills/defensive/blue-team-ops/siem-operations]
license: MIT
version: 1.0.0
---

# Logging Rules (assistant)

- **Log security-relevant events** — authentication (success/failure), authorization
  failures, privilege changes, and sensitive actions — with enough context to detect
  and investigate (who/what/when/where).
- **Never log secrets/sensitive data** — passwords, tokens, keys, full card/PII; mask/
  redact where needed.
- Use **structured logging** (consistent fields) so detections/SIEM can parse it.
- Protect log integrity (tamper-resistant where it matters); don't let users control
  log content in a way that enables log injection/forging.
- Ensure the events detections depend on are actually emitted (coordinate with
  detection engineering).
