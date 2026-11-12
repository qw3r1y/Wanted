---
name: prototype-pollution
description: >
  Use when testing an authorized JavaScript/Node target for prototype pollution —
  attacker-controlled keys (__proto__, constructor.prototype) that mutate object
  prototypes, leading to DoS, property injection, client-side XSS gadgets, or
  server-side RCE gadgets. Covers detection, gadget assessment and remediation.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, browser-devtools]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Prototype Pollution (authorized testing)

Find places where attacker-controlled keys reach a recursive merge/clone/`set`
and pollute `Object.prototype`, then assess whether a **gadget** turns that into
impact (client-side XSS, server-side config override/RCE, or DoS). Pollution alone
is a signal; the gadget makes it exploitable.

> Authorized testing only (`_shared/scope-authorization-rule.md`).

## When to use
Node/JS apps that deep-merge or clone user input (query/JSON/config), templating/
options objects, and client-side apps using unsafe merge utilities. Entry via
`__proto__`, `constructor.prototype`, or nested keys in JSON/query.

## Prerequisites
- Authorization + scope; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Find merge/clone sinks** — endpoints/functions that recursively assign user
   keys into objects.
2. **Pollution probe (first gate)** — inject a benign marker property via a
   prototype key and check whether an **unrelated** object now exposes it
   (client: in DevTools; server: a behavioural change). That differential confirms
   pollution.
3. **Gadget assessment** — identify a property the app reads from objects that,
   once polluted, changes behaviour (template option, `isAdmin`-style flag, HTML
   sink, child-process option). Classify client vs server impact.
4. **Controlled proof** — demonstrate the minimal gadget effect (e.g., a benign
   flag flip or OOB) proving severity.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the sink, the pollution
proof, and the gadget. Pollution with no reachable gadget → **low/inconclusive**.

## Impact escalation
Client-side XSS via polluted sink, server-side config/option override → RCE,
authz-flag tampering, and DoS. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Merge utility that blocks `__proto__`/uses null-proto objects → **refuted**.
- Pollution confirmed but no gadget → not high impact; say so.

## Remediation
- Block dangerous keys (`__proto__`, `constructor`, `prototype`) in merges; use
  `Object.create(null)`/`Map` for untrusted data; prefer safe/patched merge
  libraries.
- Freeze prototypes where feasible; validate input shape with schemas.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
