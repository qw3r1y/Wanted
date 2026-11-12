---
name: ssti
description: >
  Use when testing an authorized web target for Server-Side Template Injection —
  any place user input is rendered by a server-side template engine (Jinja2,
  Twig, Freemarker, Velocity, ERB, Handlebars, Thymeleaf, Razor). Covers
  detection, engine fingerprinting, sandbox assessment, controlled impact and
  remediation. Do NOT use for client-side templating (that is DOM-XSS) or plain
  reflection without template evaluation.
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
  - references/engines-and-sandboxes.md
license: MIT
version: 1.0.0
---

# SSTI — Server-Side Template Injection (authorized testing)

Find input that the server **evaluates as template syntax** rather than treating
as data, identify the engine, and establish how far evaluation reaches —
expression → object access → (where scope permits and the engine/sandbox allow)
command execution. The proof is server-side evaluation of an expression you
control, not mere reflection.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Stop before
> any destructive or out-of-scope command; demonstrate impact minimally
> (`safe-execution-rules.md`).

## When to use
Anywhere user input is composed into a server-rendered template: email/report
templates, name/subject/greeting fields, customizable messages, PDF/invoice
generators, CMS/theme fields, "preview" features, and error pages that render
user data. Common where apps build templates by string concatenation.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.
- OOB listener for blind evaluation confirmation.

## Procedure (gated phases)

### Phase 1 — Detection (first gate: evaluation vs reflection)
Submit a simple arithmetic expression in the engine's delimiters and check
whether the **result** (not the literal) is returned. If a math expression
renders as its evaluated value → template evaluation; if the literal string is
returned or HTML-escaped → **refuted** (reflection/XSS territory, not SSTI).

### Phase 2 — Engine fingerprinting
Different engines use different delimiters and error behaviour. Use a small set
of distinguishing probes to identify Jinja2/Twig/Freemarker/Velocity/ERB/
Handlebars/Thymeleaf/Razor (table in `references/engines-and-sandboxes.md`).
Engine identity drives every later step.

### Phase 3 — Reach & sandbox assessment
Establish what the evaluated context exposes: variable/object access, attribute
traversal, built-ins. Many engines run sandboxed; determine whether the sandbox
is intact or bypassable for this version. Classify reach: expression-only →
object/data access → potential code/command surface.

### Phase 4 — Controlled impact demonstration
With explicit scope approval, demonstrate the **minimum** proving severity —
e.g., read a benign server-side value or confirm object access via an OOB
callback. Do **not** run arbitrary OS commands or read sensitive files beyond
what proves the class and severity.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, engine, reach tier, and
the evaluation proof (rendered result / OOB callback) path. Reflection without
evaluation → **refuted**.

## Impact escalation
Data/object exposure, information disclosure, and (engine/sandbox/scope
permitting) server-side code or command execution — a frequent critical. State
the concrete capability proven. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Math literal echoed unevaluated → not SSTI.
- Client-side framework interpolation → DOM-XSS, different class.
- A WAF blocking `{{`/`${` → signal, not refutation of the underlying sink.
- Never escalate to RCE-style commands beyond the minimal proof and scope.

## Remediation
- Never build templates from user input; pass user data as **bound context
  variables**, not as template source.
- Use a logic-less or strictly sandboxed engine; keep engines patched (sandbox
  escapes are version-specific); disable dangerous built-ins/reflection.
- Validate/encode user data at the data layer; isolate rendering with least
  privilege.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/engines-and-sandboxes.md` — per-engine delimiters, fingerprint probes, sandbox notes (4th level).
