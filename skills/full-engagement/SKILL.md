---
name: full-engagement
description: >
  Use when you want to run a complete end-to-end engagement in one shot — selecting and
  chaining every relevant skill, subagent, and command against an authorized target, then
  consolidating all of their findings into a single verdict-backed report in your chosen
  format (Markdown, JSON, SARIF, PDF, HTML, CSV, or plain text). Do NOT use for a single
  technique (call that skill directly) or for any target outside approved scope.
type: knowledge
domain: reporting-docs
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/gated-workflow-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/reporting-template.md
  - _shared/output-formats.md
license: MIT
version: 1.0.0
---

# Full Engagement — run everything, report once

One target in, one report out. This is the conductor: it decides which of the library's
skills, subagents, and commands apply to what you have, runs them in a gated order, collects
every finding each one produces, deduplicates and scores them against a single evidence
model, and renders the result in whatever format you asked for. Nothing here is new attack
surface — it is the orchestration that turns 286 separate techniques into one coherent
engagement.

> Runs strictly in-scope. `scope-guardian` is active for the whole run
> (`_shared/scope-authorization-rule.md`); every phase obeys the passive-before-active gate
> (`_shared/gated-workflow-rule.md`).

## When to use
- You have an authorized target (domain, repo, cloud account, app, contract, or LLM
  endpoint) and want the full picture, not one check.
- You want the findings from skills **and** subagents **and** commands pulled into a single
  deduplicated, prioritized report.
- You want that report in a specific deliverable format (PDF for a client, SARIF for CI,
  JSON for a dashboard).

Do **not** use it to run one technique — call that skill directly (`/wanted:hunt-sqli`).

## Prerequisites
- Written authorization and an explicit scope. The run halts at the first out-of-scope
  action (`scope-guardian`).
- A target type, so the conductor can pick the right track.
- An output directory (default `output/`) and a chosen `format:` (default `all`).

## Procedure (gated phases)

1. **Scope & classify.** Confirm authorization, fix the in-scope set, and classify the
   target into one or more tracks (web / API / cloud / k8s / AD / mobile / contract / LLM /
   code / infra). `scope-guardian` + `program-scope-analysis`.
2. **Recon (passive first).** `@agent-wanted:recon-orchestrator` → certificate transparency,
   passive DNS, bounded active enumeration, live-host probing, surface inventory. No active
   payloads yet.
3. **Surface mapping.** Turn the inventory into a tested surface and map each asset to its
   candidate vulnerability classes (`attack-surface-mapping`).
4. **Dispatch the operators.** For each track in scope, run its subagent, which in turn runs
   its skills. Only the tracks that apply fire:

   | Track | Operator | Representative skills it drives |
   |---|---|---|
   | Web | `@agent-wanted:web-hunter` | `hunt-xss` `hunt-sqli` `hunt-ssrf` `hunt-ssti` `hunt-xxe` `hunt-idor` |
   | API | `@agent-wanted:api-hunter` | `bola` `bfla` `mass-assignment` `jwt-attacks` `oauth-oidc-abuse` |
   | Cloud | `@agent-wanted:cloud-auditor` | `aws/azure/gcp-security-audit` `cloud-iam-privesc` `cspm-posture` |
   | Kubernetes | `@agent-wanted:k8s-security-agent` | `k8s-rbac-audit` `pod-security-standards` `container-escape-analysis` |
   | Active Directory | `@agent-wanted:ad-attack-operator` | `kerberos-attacks` `adcs-abuse` `ntlm-relay-coercion` |
   | Code / supply chain | `@agent-wanted:code-auditor` + `sast-triage-agent` | `secure-code-review` `semgrep-rule-authoring` `dependency-audit` `secret-scanning` |
   | Mobile | `@agent-wanted:mobile-auditor` | `mobile-storage-api` `mobile-runtime-instrumentation` |
   | Smart contract | `@agent-wanted:smart-contract-auditor` | `reentrancy` `access-control-flaws` `oracle-manipulation` |
   | LLM / agent | `@agent-wanted:llm-red-teamer` | `prompt-injection` `jailbreak-testing` `owasp-llm-top10` |

5. **Collect findings.** Every skill emits findings as the record in
   `_shared/output-formats.md`. The conductor gathers them all into one set — no finding is
   left in a subagent's local transcript.
6. **Triage & dedup.** `@agent-wanted:evidence-manager` + `finding-triage`: drop duplicates,
   reject false positives (`false-positive-rejection`), and keep only what has a verdict.
7. **Score.** Each `confirmed` finding gets a CVSS vector from demonstrated impact
   (`cvss-scoring`); severity is the band of that score, never asserted.
8. **Report.** `@agent-wanted:report-aggregator` renders the consolidated set — exec
   summary, technical findings, remediation roadmap — in the chosen format(s).

## Verification & evidence
Presence ≠ exploitation. A finding enters the report only with a verdict
(`confirmed` / `inconclusive` / `refuted`) and, when confirmed, a captured evidence path and
CVSS vector (`_shared/evidence-confidence-rule.md`). The conductor never upgrades a verdict
to make a report look fuller.

## Evidence & reporting — output formats

The operator chooses `format:` and the same record set is projected into each. See
`_shared/output-formats.md` for the full schema and rendering notes.

| `format:` | File | For |
|---|---|---|
| `md` (default parent) | `output/report.md` | human review, GitHub |
| `json` | `output/report.json` | automation, dashboards, diffing runs |
| `sarif` | `output/report.sarif` | code-scanning into GitHub / IDE / CI gates |
| `pdf` | `output/report.pdf` | client deliverable, print, sign-off |
| `html` | `output/report.html` | interactive, self-contained read |
| `csv` | `output/findings.csv` | triage queue, ticket import |
| `txt` | `output/report.txt` | terminals, email, air-gapped notes |
| `all` | all of the above | one record set, every projection — they never disagree |

Example: `/wanted:full-engagement acme.example format: pdf,json`.

## False positives / pitfalls
- **Scope creep across tracks** — a discovered asset outside the authorized set is reported
  as out-of-scope, not tested.
- **Double counting** — the same issue found by two skills is one finding after dedup.
- **Format ≠ finding** — rendering to PDF never changes a verdict; regenerate, never
  hand-edit a rendered file.
- **Missing renderer** — if no PDF/HTML engine is installed, the run says so and leaves the
  Markdown as the deliverable rather than failing silently.
- **Noise over proof** — the conductor stops a track where proof would require harm and
  marks it `inconclusive`; it does not flood the report to look thorough.

## Remediation
Every consolidated finding carries its own fix, and the report ends with a prioritized
remediation roadmap (`remediation-roadmap`) ordered by risk, not by discovery order — so the
reader fixes the Critical RCE before the missing security header.

## References
- `_shared/scope-authorization-rule.md`, `safe-execution-rules.md`, `gated-workflow-rule.md`,
  `evidence-confidence-rule.md`, `reporting-template.md`, `output-formats.md`.
- Orchestrates: `recon-orchestrator`, `web-hunter`, `api-hunter`, `cloud-auditor`,
  `k8s-security-agent`, `ad-attack-operator`, `code-auditor`, `sast-triage-agent`,
  `mobile-auditor`, `smart-contract-auditor`, `llm-red-teamer`, `evidence-manager`,
  `report-aggregator`.
