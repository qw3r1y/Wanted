---
description: "Enrich indicators with reputation, relationships, actor links, and a confidence score."
argument-hint: "<indicators>"
---
# /ioc-enrich
Runs ioc-enrichment: normalize → enrich (reputation/infra/actor) → score confidence →
operationalize high-confidence to blocking/detection. Don't block low-fidelity IOCs.
