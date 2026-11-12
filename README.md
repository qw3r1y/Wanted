# wanted

**A security operations library for Claude Code - 287 skills, 37 commands, and 38
subagents that turn an authorized target into a finished, evidence-backed report.**

![skills](https://img.shields.io/badge/skills-287-1f6feb)
![commands](https://img.shields.io/badge/commands-37-1f6feb)
![subagents](https://img.shields.io/badge/subagents-38-1f6feb)
![domains](https://img.shields.io/badge/domains-24-1f6feb)
![validated](https://img.shields.io/badge/validate-passing-2da44e)
![license](https://img.shields.io/badge/license-MIT-444)

Most "security skill" packs are a pile of prompts that tell a model to *try* something.
`wanted` is built the other way around: every skill is a gated procedure with an
authorization check at the top, a method in the middle, and a verdict at the bottom. It
does not report a vulnerability because a payload looked interesting - it reports one when
it can prove impact, and it says so plainly when it cannot. That single rule is what
separates a useful engagement from a wall of false positives.

It covers the whole arc of real work: reconnaissance, web and API testing, cloud and
Kubernetes, Active Directory, mobile, malware and forensics, detection engineering, LLM and
agent security, smart contracts, governance, and the reporting that ties it together. One
schema, one discipline, 24 domains.

---

## What it does, concretely

You describe a target in plain language, or call a command directly. Claude selects the
right skill, confirms scope, runs the method, and writes the evidence to disk. A single
recon call looks like this:

```
/wanted:recon acme.example

[recon-orchestrator] scope confirmed → *.acme.example
  passive    certificate transparency   1,284 names
  passive    passive DNS                   312 names
  active     bounded DNS brute-force       +47 names
  resolve    live hosts                  79 / 1,643
  flag       subdomain-takeover candidates     2
→ output/recon/inventory.md
```

From there you move into the surface it found: `/wanted:api-audit`, `/wanted:hunt-sqli`,
`/wanted:jwt-audit`, `/wanted:cloud-audit`, and finally `/wanted:report` to consolidate
everything into an executive summary, technical findings, and a remediation roadmap.

Nothing here is a black box. Each skill names the exact phases it runs, the evidence it
captures, and the remediation it expects, so you can read a skill before you run it and
know precisely what it will and will not do to a production system.

---

## Proven on a live target, not just described

`wanted` was run end to end against `brokencrystals.com`, a deliberately vulnerable
application published for security testing. The engagement started from one gift the target
left exposed - its OpenAPI specification - and mapped **63 endpoints** before sending a
single test payload. From that map it produced **thirteen confirmed findings**, each with a
verdict, a severity, captured evidence, and a fix:

| Finding | Class | Severity |
|---|---|---|
| Remote command execution as root (`/api/spawn`) | command injection | Critical |
| Database credentials exposed (`/api/config`) | secret exposure | Critical |
| Server-side file read via external entity (`/api/metadata`) | XXE | Critical |
| Attacker-controlled `isAdmin` bound on registration (`/api/users/basic`) | mass assignment | Critical |
| Hard-coded third-party tokens (`/api/secrets`) | secret exposure | High |
| `admin`/`admin` accepted, admin token issued | broken authentication | High |
| Arbitrary file read, leaked the Kubernetes pod name (`/api/file`) | path traversal | High |
| Other users' PII returned without a token (`/api/users/*`) | BOLA | High |
| Query broken by a single quote (`/api/partners/query`) | XPath injection | High |
| Open redirect, verbose errors, user enumeration, missing headers | various | Medium / Low |

The part that matters most is what it *didn't* do. Three endpoints that could cause lasting
damage - a template renderer, an SSRF-capable fetcher, and the eight-variant JWT forge
surface - were identified, documented, and deliberately left unexploited, marked
`inconclusive` rather than forced. A scanner either floods those with noise or misses them
entirely. `wanted` proves what it can prove cleanly and stops where proof would require
harm. A second target, `ginandjuice.shop`, independently confirmed SQL injection and a
JavaScript-context reflected XSS using the same discipline.

Every request in both engagements was read-only or benign. No data was modified or deleted.

---

## How it is built

Four kinds of component, each with a job.

**Skills** are the unit of work: one folder, one `SKILL.md`, one technique. The body is a
gated procedure. It opens with prerequisites and an authorization gate, walks through phases
that escalate from passive to active only within scope, specifies how to verify a result and
what evidence to keep, then closes with impact, false-positive traps, and remediation. A
skill runs when your request matches its description, or on demand as `/wanted:<name>`.

**Subagents** are operators that run several skills toward a goal. `recon-orchestrator`
chains passive recon, subdomain enumeration, content discovery, and port scanning into one
prioritized inventory; `web-hunter` maps an application's surface to vulnerability classes
and works through them; `scope-guardian` sits across the whole engagement and blocks
anything out of bounds. Invoke one with `@agent-wanted:<name>`.

**Commands** are the fast entrypoints - `/wanted:recon`, `/wanted:subdomains`,
`/wanted:triage`, `/wanted:report` - thin front doors onto the skills and agents behind them.

**Shared rules** (`_shared/`) are the contract every skill signs: scope and authorization,
safe execution, untrusted-input handling, the gated workflow, the evidence-and-confidence
model, plus references for CVSS, OWASP, MITRE ATT&CK, and the reporting template. Change the
rule once and every skill inherits it. That is why files stay short: the discipline lives in
one place instead of being copy-pasted 287 times.

The evidence model is the spine. Every finding carries a verdict - `confirmed`,
`inconclusive`, or `refuted` - a CVSS score justified by demonstrated impact, and a path to
the proof on disk. "The endpoint reflected my input" is not a finding. "Two identities, one
read the other's object, here is the request pair" is.

---

## Inside the library

287 skills across 24 domains and 38 technique groups. The whole map, by the numbers:

| Domain | Skills | A sample of what is inside |
|---|--:|---|
| Offensive security | 88 | web 26 (`xss` `sqli` `ssrf` `ssti` `xxe` `idor` `command-injection` `path-traversal` `http-request-smuggling` `web-cache-poisoning` `prototype-pollution` `race-condition`), API 13 (`bola` `bfla` `mass-assignment` `jwt-attacks` `oauth-oidc-abuse` `graphql-abuse` `rate-limit-bypass`), recon/OSINT 8, Active Directory 6, auth 6, exploit-dev 5, post-exploitation 5, network 5, mobile 4, C2/red-team 4, social engineering 3, wireless 3 |
| Defensive & blue team | 28 | DFIR 9 (`memory-forensics` `disk-forensics` `timeline-analysis` `ransomware-response`), CTI 6 (`threat-actor-profiling` `mitre-attack-mapping`), detection engineering 5 (`sigma-rule-authoring` `yara-rule-authoring` `detection-as-code`), threat hunting 4, blue-team ops 4 |
| Application security | 24 | `semgrep-rule-authoring` `codeql-query-authoring` `sarif-triage` `dast-scanning` `secure-code-review` `authz-patterns` `input-validation` `crypto-usage-review` `sbom-generation` `malicious-dependency-detection` `slsa-provenance` `stride-modeling` `attack-tree` |
| AI & LLM security | 19 | `prompt-injection` `jailbreak-testing` `data-leakage` `owasp-llm-top10` `rag-security` `guardrail-design` `excessive-agency-control` `agent-sandboxing` `multi-agent-trust` `memory-poisoning` `mcp-server-hardening` `mcp-tool-poisoning` `garak-probes` `pyrit-orchestration` |
| Cloud & infrastructure | 17 | `aws-security-audit` `azure-security-audit` `gcp-security-audit` `cloud-iam-privesc` `cspm-posture` `k8s-rbac-audit` `pod-security-standards` `container-escape-analysis` `runtime-security-falco` `terraform-security-scan` `opa-rego-policy` |
| Blockchain & Web3 | 12 | `reentrancy` `access-control-flaws` `oracle-manipulation` `flash-loan-attacks` `front-running-mev` `solidity-audit` `defi-protocol-audit` `bridge-security` `wallet-security` `slither-echidna-analysis` `foundry-poc` |
| Malware & reverse engineering | 8 | `pe-analysis` `maldoc-analysis` `unpacking` `script-deobfuscation` `dynamic-sandbox-analysis` `ghidra-static-analysis` `c2-config-extraction` `yara-signature-generation` |
| Governance, risk & compliance | 8 | `iso27001-isms` `soc2-readiness` `pci-dss` `hipaa` `nist-csf-mapping` `risk-assessment` `policy-authoring` `vendor-risk-management` |
| Bug bounty | 8 | `program-scope-analysis` `recon-workflow` `attack-surface-mapping` `finding-triage` `poc-crafting` `report-writing` `responsible-disclosure` `retest-verification` |
| Data privacy | 7 | `pii-discovery` `data-classification` `anonymization` `gdpr-kvkk-mapping` `dlp-policy-design` `linddun-privacy` |
| EASM | 6 | `asset-attribution` `confidence-scoring` `false-positive-rejection` `subdomain-takeover-detection` `continuous-discovery` `exposure-risk-scoring` |
| Cryptography | 6 | `tls-config-audit` `crypto-misuse-detection` `padding-oracle` `signature-replay` `post-quantum-readiness` `side-channel-intro` |
| Identity & IAM | 6 | `iam-architecture-review` `privileged-access-pam` `jit-access-design` `non-human-identity` `federation-sso-security` `secrets-management` |
| CI/CD & DevSecOps | 6 | `ci-cd-pipeline-security` `runner-hardening` `secret-scanning-in-pipeline` `sast-dast-in-pipeline` `artifact-integrity-attestation` `pipeline-threat-model` |
| Hardware & IoT | 5 | `firmware-analysis` `uart-jtag-access` `spi-flash-dump` `iot-protocol-attacks` `side-channel-intro` |
| ML model security | 5 | `adversarial-examples` `data-poisoning-ml` `model-extraction-defense` `membership-inference` `model-serialization-security` |
| OT / ICS / SCADA | 5 | `modbus-dnp3-security` `plc-security` `purdue-model-review` `ics-network-segmentation` `ics-threat-hunting` |
| Reporting & orchestration | 6 | `full-engagement` (run every skill/agent/command, one consolidated report) `executive-summary-writing` `technical-finding-report` `cvss-scoring` `remediation-roadmap` `risk-based-scoring` |
| Email security | 4 | `email-authentication` `dmarc-enforcement` `phishing-detection` `bec-defense` |
| Deception | 4 | `honeypot-deployment` `canary-tokens` `honeytoken-design` `deception-detection-engineering` |
| Endpoint & app security | 4 | `browser-extension-security` `electron-app-security` `thick-client-audit` `ipc-local-attacks` |
| Zero trust | 4 | `zta-architecture` `microsegmentation` `device-posture` `continuous-authentication` |
| Vulnerability management | 4 | `vuln-prioritization-epss` `kev-tracking` `patch-verification` `risk-based-scoring` |
| Red-team infrastructure | 3 | `redirector-detection` `opsec-checklist`, C2 operator tradecraft |

But the 287 skills are only one of six moving parts. The rest of the tree is what turns a
pile of techniques into an engagement.

### 38 subagents - the operators

Skills are techniques; subagents are the operators that run them toward a goal, pick the next
move from a result, and hand off to each other. Invoke any with `@agent-wanted:<name>`.

| Group | Subagents |
|---|---|
| Orchestration & governance (6) | `pentest-orchestrator` `recon-orchestrator` `scope-guardian` `evidence-manager` `report-aggregator` `purple-team-coordinator` |
| Offensive operators (8) | `web-hunter` `api-hunter` `ad-attack-operator` `privesc-specialist` `exploit-developer` `osint-investigator` `bugbounty-autohunter` `wireless-auditor` |
| Cloud, infra & AppSec (7) | `cloud-auditor` `k8s-security-agent` `iac-policy-agent` `code-auditor` `sast-triage-agent` `dependency-guardian` `secure-review-gate` |
| Blue team, IR & intel (8) | `incident-responder` `forensics-examiner` `threat-hunter` `detection-engineer` `soc-analyst-l1` `soc-analyst-l2` `cti-analyst` `threat-modeler` |
| AI & agent security (4) | `llm-red-teamer` `prompt-injection-auditor` `agent-safety-reviewer` `mcp-security-auditor` |
| Specialist auditors (5) | `smart-contract-auditor` `defi-risk-agent` `malware-analyst` `mobile-auditor` `iam-reviewer` |

### 37 commands - the entrypoints

Front doors onto the skills and agents. Type `/wanted:<command>` to start a method without
describing it.

| Group | Commands |
|---|---|
| Recon & surface (4) | `recon` `subdomains` `portscan` `api-audit` |
| Web & API hunts (8) | `hunt-sqli` `hunt-xss` `hunt-ssrf` `hunt-ssti` `hunt-xxe` `hunt-idor` `hunt-auth` `jwt-audit` |
| Cloud, infra & code (6) | `cloud-audit` `k8s-audit` `iac-scan` `code-review-sec` `dep-audit` `secret-scan` |
| Active Directory (1) | `kerberoast` |
| AI security (3) | `llm-redteam` `prompt-inject-test` `mcp-audit` |
| Blue team & detection (6) | `soc-triage` `hunt-threats` `sigma` `yara` `ioc-enrich` `forensics-triage` |
| Specialist audits (4) | `mobile-audit` `contract-audit` `wifi-audit` `privesc-check` |
| Triage & reporting (5) | `triage` `poc` `cvss` `threat-model` `report` |

### The discipline layer - rules, MCP, and the shared contract

This is the part no other library ships, and it is why a `wanted` run ends in a report
instead of a transcript.

**`_shared/` - the contract every skill signs (11 references).** `scope-authorization-rule`,
`safe-execution-rules`, `untrusted-input-rule`, `gated-workflow-rule`,
`evidence-confidence-rule`, plus the references each skill links instead of repeating:
`cvss-reference`, `owasp-mappings`, `mitre-attack-reference`, `reporting-template`,
`glossary`, and `output-formats` (the report-rendering contract). Change the rule once; all
287 skills inherit it.

**`rules/` - 12 secure-by-default rulesets** that drop into a developer's own repo so the same
standard applies to the code being built, not just the test of it: `owasp-review-rules`,
`secure-coding-cursorrules`, `sql-injection-prevention-rules`, `auth-hardening-rules`,
`crypto-usage-rules`, `secrets-prevention-rules`, `iac-security-rules`, `k8s-security-rules`,
`dependency-policy-rules`, `logging-rules`, `ai-safe-coding-rules`, `commit-hygiene-rules`.

**`mcp/` - a tooling layer in two halves.** Four curated catalogs of the real-world tools each
side of the house reaches for - `offensive-tooling`, `defensive-tooling`, `cloud-tooling`,
`ai-security-tooling` - and five hardening patterns for building MCP servers safely:
`mcp-server-authoring`, `mcp-auth-security`, `mcp-sandboxing`, `mcp-tool-schema-design`,
`run-tool-gateway-pattern`.

**`_meta/`** carries the `AUTHORING-STANDARD.md` schema and `validate.py`, the quality gate
that fails the build on any schema break, missing trigger description, copied source, or
defang artifact.

Add it up: **287 skills + 38 subagents + 37 commands + 12 rulesets + 9 MCP references + 11
shared-contract files = 394 purpose-built artifacts**, under one schema, enforced by one gate.
The complete, linkable index of every skill lives in [`CATALOG.md`](CATALOG.md).

### One command to run it all

`full-engagement` is the conductor. Point it at one authorized target and it selects every
skill, subagent, and command that applies, runs them in a gated passive-before-active order,
pulls each one's findings into a single deduplicated set, scores them on one evidence model,
and writes the report:

```
/wanted:full-engagement acme.example format: pdf,json

[scope-guardian]       scope confirmed → *.acme.example
[recon-orchestrator]   surface mapped          79 live hosts
[web-hunter]           xss·sqli·ssrf·idor      4 confirmed
[api-hunter]           bola·bfla·jwt           3 confirmed
[cloud-auditor]        iam·exposure            2 confirmed
[evidence-manager]     dedup + verdicts        9 confirmed · 3 inconclusive
[report-aggregator]    rendered
→ output/report.pdf  output/report.json
```

No finding is left inside a subagent's transcript - they all land in one report, each with a
verdict, a CVSS vector, and a path to its proof.

---

## Where it stands against the field

Measured against the most-referenced purpose-built security skill libraries - fork mirrors
and re-uploads of other people's work left out - with counts pulled live from the GitHub API
and quality sampled from real `SKILL.md` files:

| Repository | Skills | Focus |
|---|---:|---|
| **wanted** | **287** | **the full arc, 24 domains, validated end to end** |
| trailofbits/skills | 105 | application security, reverse engineering, fuzzing |
| trilwu/secskills | 94 | web, API, Active Directory |
| elementalsouls/Claude-BugHunter | 83 | bug bounty |
| SnailSploit/Claude-Red | 79 | offensive |
| transilienceai, Masriyan, ljagiello, Claude-OSINT, android-re | 50-1 | narrower scopes |

The largest purpose-built security skill library of the group, and it is not close - nearly
three times the next one. Size is the least of it. `wanted` is the only entry here with a
single enforced schema, trigger-style descriptions on 100% of its skills, and an evidence
model - verdict, CVSS, proof path - on every finding, where most of the field has none at
all. It is the only one with a dedicated API suite: thirteen skills covering BOLA, BFLA, mass
assignment, and the full JWT and OAuth surface, against rivals that offer one or two. And it
is the only one that ships real orchestration - subagents and commands wired into the skills
- instead of a flat list of prompts.

A few of the others go deeper inside a single lane, and that depth is real: Trail of Bits on
fuzzing, Claude-Red on exploit development. None come close on breadth, on consistency, or on
the evidence discipline that turns a run into a report - and every file in this tree was
written from scratch, the one thing no fork will ever claim.

---

## Principles

Authorization is not optional. Every offensive skill opens with a scope check, and
`scope-guardian` enforces it for the whole engagement. Nothing out of bounds runs.

Passive before active, always. Reconnaissance begins on free public sources - certificate
transparency, public DNS, archives - and escalates to active, noisier techniques only once
scope allows. You can map a target completely before touching it.

No API keys required. Not one skill needs a key to function. A handful can optionally use
Shodan, Censys, SecurityTrails, or VirusTotal to widen their results, but without them they
fall back to free sources and keep working. The skills that mention API keys at all mostly
hunt for leaked ones.

Evidence over assertion, and remediation over bravado. A finding without proof is a lead,
not a result, and a skill that only knows how to break something is half a skill. Every one
of them ends with the fix.

Original, end to end. Coverage was learned by analyzing 17,219 open-source skills; not one
file was copied. There is no `inspired_by`, no `source`, no borrowed payload anywhere in the
tree, and a CI check fails the build if any appears.

---

## Install and use

Inside Claude Code, add the marketplace and install the plugin:

```
/plugin marketplace add qw3r1y/wanted
/plugin install wanted@wanted
```

Single step, on Claude Code 2.1.275 or newer:

```
/plugin install wanted --marketplace qw3r1y/wanted
```

Or try it for one session without installing anything:

```bash
claude --plugin-dir /path/to/wanted
```

### Manual install - download and drop in

No marketplace needed. Download the repository (the green **Code → Download ZIP** button, or
`git clone`) and copy the skills straight into Claude's skills directory - Claude discovers
them on the next start.

**Claude Code** reads skills from `~/.claude/skills/` (user scope) or `.claude/skills/` in a
project. Copy the folders in:

```bash
# all of them at once
cp -r wanted/skills/* ~/.claude/skills/

# or just the ones you want
cp -r wanted/skills/full-engagement ~/.claude/skills/
cp -r wanted/skills/bola           ~/.claude/skills/
```

On Windows that directory is `%USERPROFILE%\.claude\skills\`. Each skill is a self-contained
folder with its `SKILL.md`, so a single skill works on its own - drop in one or drop in all
287.

**Claude desktop / web app** loads skills from **Settings → Capabilities → Skills**: click
**Upload skill** and pick a skill folder (or its zip). Upload `full-engagement` for the
one-shot engagement runner, or any individual technique you want on hand.

Installed manually, skills are invoked by their own name; installed as the plugin they are
namespaced under `wanted` (`/wanted:<name>`). Both ways run the same files.

Then, as the plugin, everything is namespaced under `wanted`:

| Kind | Invoke | Example |
|---|---|---|
| Command | `/wanted:<command>` | `/wanted:subdomains acme.example` |
| Skill | `/wanted:<skill>`, or automatically on a match | `/wanted:bola`, `/wanted:xss` |
| Subagent | `@agent-wanted:<agent>` | `@agent-wanted:recon-orchestrator` |

The full list of skills, grouped by domain, is in [`CATALOG.md`](CATALOG.md). Plugins run
with your privileges; read a skill before you run it against anything you care about.

---

## Repository layout

```
wanted/
├── .claude-plugin/
│   ├── plugin.json          plugin manifest
│   └── marketplace.json     marketplace manifest
├── skills/<name>/SKILL.md   287 skills, one folder each  ->  /wanted:<name>
├── commands/<name>.md       37 entrypoint commands       ->  /wanted:<name>
├── agents/<name>.md         38 subagents                 ->  @agent-wanted:<name>
├── _shared/                 the contract every skill signs (authorization, safe
│                            execution, evidence, CVSS, OWASP, ATT&CK, reporting, output)
├── _meta/
│   ├── AUTHORING-STANDARD.md the schema every skill follows
│   └── validate.py           the quality gate
├── rules/ · mcp/            supporting reference material
├── CATALOG.md               all skills grouped by domain
└── README.md
```

Every skill follows one layout: frontmatter (`name`, a trigger-style `description`, `type`,
`domain`, `maturity`, `tools`, `references`, `license`, `version`), then a body that runs
When to use → Prerequisites → Procedure in gated phases → Verification and evidence → Impact
escalation → False positives and pitfalls → Remediation → References.

## Quality gate

```bash
python _meta/validate.py
```

It checks the schema, the trigger-style descriptions, originality (no copied source), the
absence of defanged artifacts, and the integrity of every `_shared` reference. The tree
ships clean, and `claude plugin validate .` passes.

## Output formats

When a run finishes, the findings are not a wall of chat text - they are a structured record
set written to `output/`, then rendered into whatever deliverable you need. Every finding is
one object (id, title, verdict, severity, CVSS score and vector, class/CWE, target, evidence
paths, reproduction, impact, remediation); each format below is just a projection of that
same set, so they never contradict each other. Pick one with a `format:` argument, or `all`.

| `format:` | Output file | Best for |
|---|---|---|
| `md` *(default)* | `output/report.md` | human review, GitHub, a fast read |
| `pdf` | `output/report.pdf` | the client-facing deliverable, print, sign-off |
| `json` | `output/report.json` | automation, dashboards, re-ingest, diffing two runs |
| `sarif` | `output/report.sarif` | code-scanning findings into GitHub / IDE / CI gates |
| `html` | `output/report.html` | an interactive, self-contained read with filters |
| `csv` | `output/findings.csv` | triage queue, ticket import (Jira / ServiceNow), pivots |
| `txt` | `output/report.txt` | terminals, email bodies, air-gapped notes |
| `all` | every file above | one record set, every projection at once |

```
/wanted:report format: pdf,json
/wanted:full-engagement acme.example format: all
```

PDF and HTML are rendered from the Markdown (`pandoc`, or a headless-browser print); if no
renderer is installed the run says so and leaves the Markdown as the deliverable rather than
failing quietly. Client PDFs redact captured secrets to a last-4 preview - the full value
stays only in `output/` on your disk. The full contract is in
[`_shared/output-formats.md`](_shared/output-formats.md).

## Coverage

Offensive web (26) and API (13), reconnaissance and EASM, Active Directory, network and
wireless, exploit development and post-exploitation; defensive detection engineering, threat
hunting, DFIR, and CTI; malware analysis and reverse engineering; application security,
supply chain, and CI/CD; cloud, containers, and infrastructure-as-code; identity, zero
trust, and IAM; LLM, agent, and MCP security, and adversarial ML; smart contracts and DeFi;
hardware and IoT; OT/ICS/SCADA; cryptography, data privacy, email security, deception,
governance, and bug bounty. Twenty-four domains, and the reporting discipline to turn any of
them into a deliverable.

## License

MIT. Each skill carries its own license field; all are MIT.
