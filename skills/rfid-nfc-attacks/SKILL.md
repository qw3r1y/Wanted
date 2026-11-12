---
name: rfid-nfc-attacks
description: >
  Use when assessing an authorized RFID/NFC system (access cards, tags) — card
  technology identification, clone/replay susceptibility, and backend validation
  of card data. Covers technology assessment and physical-access-control review.
type: knowledge
domain: offensive/wireless
maturity: canonical
tools: [proxmark3]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# RFID / NFC Assessment (authorized)

Assess an authorized RFID/NFC access system for weak card technologies (readable/
clonable), replay susceptibility, and whether the backend meaningfully validates
card data. The proof is demonstrating clone/replay of a **test** credential you are
authorized to use.

> Authorized testing only, with cards/systems you are authorized to test
> (`_shared/scope-authorization-rule.md`). Use test credentials, not others'
> cards.

## Prerequisites
- Authorization + scope; a reader/writer; a test card. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify technology (first gate)** — determine the card type and whether it is
   a legacy/clonable technology (static ID, weak/known keys) vs a secure one
   (mutual auth, diversified keys).
2. **Read/clone test** — for a **test** card you own, assess whether its data can be
   read and written to a blank/emulator (clone) or replayed.
3. **Backend validation** — determine whether the system relies solely on the card
   ID (clonable) or adds cryptographic challenge/response.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the technology, and the
clone/replay proof on a test credential. Secure tech with mutual auth → **refuted**.

## Impact escalation
Physical access via cloned/replayed credentials. CVSS/physical-impact context per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Secure card tech with diversified keys resists cloning → **refuted**.
- Only test credentials you are authorized to use.

## Remediation
- Use secure card technologies with mutual authentication and diversified keys;
  avoid ID-only validation; add multi-factor for sensitive doors; monitor
  anti-passback/anomalies.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
