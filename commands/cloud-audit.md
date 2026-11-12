---
description: "Audit an authorized cloud environment — IAM, exposure, logging, and privesc paths."
argument-hint: "<provider>"
---
# /cloud-audit
Runs cloud-auditor: provider audit (aws/azure/gcp) → cloud-iam-privesc → storage-exposure
→ prioritize (cspm). Read-only audit roles; exploitable over checklist noise.
