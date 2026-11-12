# Output & Report Formats (shared reference)

Every engagement writes its proof to `output/` on disk, then renders a report in one or more
of the formats below. The source of truth is always the structured finding record; the
rendered formats are projections of it. Any skill, command, or agent that produces findings
links this file and honours the format the operator asks for.

## The finding record (source of truth)

Each finding is one object, regardless of how it is later rendered:

```json
{
  "id": "WANTED-0007",
  "title": "Other users' PII returned without a token",
  "verdict": "confirmed",          // confirmed | inconclusive | refuted
  "severity": "High",              // Critical | High | Medium | Low | Info
  "cvss": { "score": 7.5, "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N" },
  "class": "BOLA",                 // OWASP / CWE class
  "cwe": "CWE-639",
  "target": "https://host/api/users/42",
  "evidence": ["output/bola/req-identityA.http", "output/bola/req-identityB.http"],
  "reproduction": "…",             // exact, minimal steps
  "impact": "…",
  "remediation": "…",
  "references": ["_shared/owasp-mappings.md"]
}
```

## Supported render formats

| Format | File | Use it for | Notes |
|---|---|---|---|
| **Markdown** | `report.md` | the default; human review, GitHub, quick read | exec summary + findings + roadmap; always produced |
| **JSON** | `report.json` | automation, dashboards, re-ingest, diffing runs | the array of finding records above; stable schema |
| **SARIF 2.1.0** | `report.sarif` | code-scanning findings into GitHub / IDE / CI gates | one `result` per finding, with `ruleId`, `level`, `locations` |
| **PDF** | `report.pdf` | the client-facing deliverable, print, sign-off | rendered from `report.md`; cover, TOC, severity table |
| **HTML** | `report.html` | an interactive, self-contained read with filters | single file, no external assets |
| **CSV** | `findings.csv` | triage queue, ticket import (Jira/ServiceNow), pivot | one row per finding: id, title, severity, cvss, verdict, target |
| **Plain text** | `report.txt` | terminals, email bodies, air-gapped notes | no markup; same structure flattened |

## Severity → CVSS discipline

Severity is never asserted — it is the band of the demonstrated-impact CVSS score
(`_shared/cvss-reference.md`). An `inconclusive` verdict carries a provisional score marked as
such; a `refuted` finding is kept in `report.json` for audit but omitted from the client PDF.

## Rendering, concretely

- **Markdown** is written directly and is the parent of PDF/HTML.
- **PDF** is produced from `report.md` with any available renderer (e.g. `pandoc report.md
  -o report.pdf`, or a headless-browser print of `report.html`); if none is installed the
  skill says so and leaves the Markdown as the deliverable rather than failing silently.
- **SARIF/JSON/CSV** are emitted straight from the finding records — no prose round-trip.
- The operator chooses with a `format:` argument (`md`, `json`, `sarif`, `pdf`, `html`,
  `csv`, `txt`, or `all`). `all` writes every format from the one record set, so they never
  disagree.

## Rules

1. One record set, many projections — never hand-edit a rendered format; regenerate it.
2. Every rendered format names the evidence path, so a reader can reach the proof.
3. No finding without a verdict and, for `confirmed`, a CVSS vector.
4. Redaction: client PDFs strip raw secrets/tokens captured as evidence to a last-4 preview;
   the full value stays only in `output/` on the operator's disk.
