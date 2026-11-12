---
name: spi-flash-dump
description: >
  Use when extracting firmware/data directly from an authorized device's flash chip
  (SPI/I2C/eMMC) — chip identification, reading, and recovering firmware/secrets for
  analysis. Covers hardware memory extraction.
type: knowledge
domain: hardware-iot
maturity: canonical
tools: [flashrom, chip-clip]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Flash Chip Extraction (SPI/I2C/eMMC)

When firmware isn't available via software, read it directly from the device's
flash chip — identify the chip, connect (in-circuit clip or desolder), and dump its
contents for firmware/secret analysis. For authorized hardware you own/test.

> Authorized testing on your own/in-scope hardware (`_shared/scope-authorization-rule.md`).

## When to use
When firmware can't be obtained via software and hardware extraction is in scope.

## Procedure (gated phases)
1. **Identify the chip** — locate the flash (SPI NOR/NAND, I2C EEPROM, eMMC); read
   its markings/datasheet for pinout/protocol.
2. **Connect** — in-circuit (SOIC clip) or desolder; wire to a programmer (flashrom-
   compatible).
3. **Dump** — read the full contents; verify integrity (re-read/compare).
4. **Analyze** — extract firmware/filesystem/secrets (firmware-analysis).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the dump + what it revealed; verify a
clean read.

## Impact escalation
Firmware/secret recovery enabling full analysis and fleet-wide risk. CVSS per
`_shared/cvss-reference.md`.

## Pitfalls
- In-circuit reads can be interfered with by the running device (power it down/
  isolate).
- Encrypted flash — note; may need key from elsewhere.

## Remediation
- Encrypted flash + secure boot; tamper detection; don't store plaintext secrets in
  flash; unique per-device keys.

## References
- `_shared/` rules (authorization, evidence).
