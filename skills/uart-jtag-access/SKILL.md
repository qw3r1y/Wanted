---
name: uart-jtag-access
description: >
  Use when assessing an authorized hardware device's debug interfaces — identifying
  and accessing UART/JTAG/SWD for console/debug access, firmware dump, and exposure
  assessment. Covers hardware debug-interface testing.
type: knowledge
domain: hardware-iot
maturity: canonical
tools: [logic-analyzer]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# UART / JTAG Debug Interface Assessment

Many devices leave debug interfaces (UART console, JTAG/SWD) accessible on the
board, granting shell/debug access, firmware dump, or memory access. On an
authorized device you own/test, identify and assess these interfaces as an exposure.

> Authorized testing on your own/in-scope hardware (`_shared/scope-authorization-rule.md`).

## When to use
Hardware assessment of an authorized IoT/embedded device.

## Procedure (gated phases)
1. **Identify interfaces** — locate candidate UART/JTAG/SWD pads/headers; determine
   pinout (logic analyzer/multimeter).
2. **UART console** — connect at the right baud; assess whether it drops to a shell/
   bootloader (often unauthenticated) — console access.
3. **JTAG/SWD** — assess debug access (halt/memory/flash) if exposed.
4. **Assess exposure** — what access the interfaces grant (shell, firmware dump,
   memory) and whether they're disabled/locked in production.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the exposed interface + access gained.
Locked/disabled → **refuted**.

## Impact escalation
Shell/root access, firmware/secret extraction, and bypass of other controls. CVSS/
physical-impact per `_shared/cvss-reference.md`.

## Pitfalls
- Interfaces present but locked/authenticated → lower risk; note.
- Physical access required — factor into risk.

## Remediation
- Disable/lock debug interfaces in production (fuses, authenticated JTAG,
  password-protected console); secure boot; tamper detection.

## References
- `_shared/` rules (authorization, evidence).
