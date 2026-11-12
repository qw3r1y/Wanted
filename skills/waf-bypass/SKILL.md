---
name: waf-bypass
description: >
  Use when an authorized test is blocked by a WAF/filter and you need to determine
  whether the WAF (not the app) is the only thing stopping a confirmed-class
  vulnerability. Covers WAF fingerprinting, systematic filter analysis, and
  responsible reporting. This is a defense-evasion aid for authorized testing, not
  a standalone vuln.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# WAF / Filter Bypass (authorized testing)

Determine whether a WAF/input filter is the **only** control blocking an otherwise
real vulnerability, and characterize the filter so remediation does not rely on
the WAF alone. A WAF bypass is only meaningful attached to a confirmed underlying
issue — a WAF on a non-vulnerable endpoint is not a finding.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Keep probes
> bounded; WAFs may rate-limit/ban — respect scope limits
> (`safe-execution-rules.md`).

## When to use
When a probe for a specific vulnerability class (xss/sqli/etc.) is blocked (403/
challenge) and you need to tell "app is safe" from "WAF is hiding an app bug".

## Prerequisites
- Authorization + scope; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Confirm it's the WAF (first gate)** — distinguish a WAF block (generic 403/
   challenge page, block page, specific headers) from an app-level rejection
   (validation error). Fingerprint the WAF from headers/behaviour.
2. **Map the filter** — identify *what* triggers the block (keyword, character,
   pattern, encoding) with minimal, bounded differential probes.
3. **Reason about the underlying sink** — only pursue bypass where an underlying
   vulnerability is plausible/confirmed; the objective is to reach the app sink to
   test the real control, not to evade for its own sake.
4. **Report both** — if a bypass reaches a confirmed vuln, report the vuln (primary)
   and note WAF reliance; if the app is actually safe, say so.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict` for the **underlying**
issue; the WAF bypass is context for it. A bypass that reaches a safe app →
**refuted** (no vuln), WAF-only is informational.

## Impact escalation
The impact is that of the **underlying** vulnerability now shown reachable;
separately, WAF-only defenses are a weakness to report. CVSS reflects the real
bug, not the bypass.

## False positives & pitfalls
- Treating a WAF block as proof the app is safe (false negative) — or a bypass as
  a vuln when the app is fine (false positive). Always tie to the app sink.
- Do not hammer the WAF into bans; keep probes minimal and attributable.

## Remediation
- **Do not rely on a WAF as the primary control** — fix the underlying issue at
  the code level (encoding/parameterization/validation).
- Tune the WAF as defense-in-depth; prefer positive-security (allow-list) models;
  monitor and alert on evasion patterns.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
