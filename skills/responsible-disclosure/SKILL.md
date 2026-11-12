---
name: responsible-disclosure
description: >
  Use when handling disclosure of a vulnerability — coordinated disclosure outside a
  formal program, timelines, communication, and ethics when there's no bounty. Covers
  responsible/coordinated disclosure.
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Responsible / Coordinated Disclosure

When you find a vulnerability outside a formal bounty (or one needing coordinated
disclosure), handle it ethically: report privately to the right contact, give
reasonable time to fix, communicate professionally, and avoid public disclosure or
exploitation that would harm users — balancing the public interest with safety.

> Only report what you found through authorized/legal means; don't exceed access to
> "prove" more (`_shared/scope-authorization-rule.md`).

## When to use
Disclosing a vulnerability to an organization without a clear bounty process, or
coordinating a fix timeline.

## Procedure (gated phases)
1. **Find the contact** — security.txt, a security/VDP page, or an appropriate
   contact; prefer a secure channel.
2. **Report privately** — clear description, reproduction, and impact (report-writing);
   no public details yet.
3. **Coordinate (core)** — give reasonable remediation time; agree a timeline; stay
   professional even if the response is slow/poor.
4. **Disclose responsibly** — public disclosure (if any) only after a fix or a fair
   coordinated timeline, omitting details that enable harm; never extort.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Keep a professional record of the finding +
communications.

## Impact / output
The vulnerability gets fixed with minimal user harm; ethical, legally-sound conduct.

## Pitfalls
- Public disclosure/exploitation before a fix (harms users; legal risk).
- Exceeding authorized access to gather "more proof"; any extortion framing.

## Linkage
- Uses finding-triage + report-writing; the ethical frame for all offensive findings.

## References
- `_shared/` rules (authorization, evidence).
