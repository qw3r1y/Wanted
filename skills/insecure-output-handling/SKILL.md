---
name: insecure-output-handling
description: >
  Use when testing/defending how an app consumes LLM output — treating model output
  as untrusted to prevent XSS, SSRF, injection, or unsafe code/command execution
  downstream. Covers the output trust-boundary (OWASP LLM05).
type: knowledge
domain: ai-security/llm-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Insecure Output Handling (test & defend)

LLM output is **untrusted data** for whatever consumes it. If the app renders it as
HTML, runs it as code/SQL/commands, or uses it in requests without validation, the
model (or an injection through it) can cause XSS, SSRF, injection, or RCE
downstream. Test the output sink; defend by validating/encoding there.

> Authorized testing only; treat model output as untrusted
> (`_shared/untrusted-input-rule.md`).

## When to use
When LLM output flows into a sink: HTML rendering, code/command execution, SQL,
API calls, file writes, or further tools.

## Procedure (gated phases)
1. **Map output sinks** — where model output goes and how it's used (render/execute/
   query/request).
2. **Test each sink (core)** — can crafted output (possibly via prompt injection)
   cause XSS (rendered), SSRF/request forgery (used in a request), injection (SQL/
   command), or unsafe code execution?
3. **Assess impact** — the downstream vulnerability triggered through the model.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the sink, and the
downstream impact. Output validated/encoded at the sink → **refuted**.

## Impact escalation
XSS, SSRF, SQL/command injection, and RCE — classic app vulns reached via the model.
CVSS per `_shared/cvss-reference.md`.

## Defenses
- Treat output as untrusted at every sink: context-aware encoding (render), no
  direct execution of model-generated code/commands without sandbox+review, validate
  URLs (SSRF), parameterize queries, and allow-list actions.

## References
- `_shared/` rules (authorization, untrusted input, evidence).
