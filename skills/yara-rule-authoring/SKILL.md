---
name: yara-rule-authoring
description: >
  Use when writing YARA rules to detect malware families, tools, or file
  characteristics — selecting robust strings/conditions that catch a family
  without over-matching. Covers rule design, testing, and FP control for file/
  memory scanning.
type: knowledge
domain: defensive/detection-engineering
maturity: canonical
tools: [yara]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# YARA Rule Authoring

Write YARA rules that reliably detect a malware family/tool or a suspicious file
trait — durable strings and conditions that generalize across samples of the
family while avoiding false positives on benign files. Used for file, memory, and
feed scanning.

## When to use
After analyzing malware (malware-re) or to operationalize a family/campaign IOC set
into scalable detection.

## Procedure (gated phases)
1. **Identify durable features** — strings/byte patterns/structure that are stable
   across the family but rare in benign files (avoid volatile/compiler-generic
   strings).
2. **Write conditions** — combine strings with file-structure conditions (PE
   fields, size, entropy) and a meaningful `condition` (N-of-M) to balance
   coverage vs precision.
3. **Add metadata** — family, author, date, reference, severity.
4. **Test** — against a sample set (true positives) and a large benign corpus
   (false positives); tune.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = detects family samples with minimal
FP on benign corpus. Record TP/FP results.

## Quality bar / pitfalls
- Over-fitting to one sample (misses variants) vs over-broad strings (FPs).
- Volatile strings (paths/timestamps) make brittle rules.

## Deployment notes
- Deploy to file/memory/EDR scanning and threat-intel feeds; version and review
  rules; retire stale ones.

## References
- `_shared/` rules (untrusted input, evidence).
