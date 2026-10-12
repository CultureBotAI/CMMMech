# Independent publication provenance finding

UTC: 2026-10-12T04:13:01.796735Z. Reviewer: Codex /root/round43_hardmetal; GPT-6; codex.

**Verdict: changes requested.** One confirmed minor provenance defect.

I authored the mineral records and source dossiers, but not the independent scientific review assessed here. This is a review-metadata finding, not independent acceptance of my own science.

## F1 — snapshot hash names the wrong referenced artifact

Stable key: `CMMMech.round45.argyrodite-review.evidence-snapshot-reference`.

Target: `reviews/structured/20261012T041053Z-argyrodite-round45-resolution/review.yaml`, field `evidence[evidence_id=correction].snapshot_sha256`. The evidence reference is `research/sources/round45-ge-minerals/20261012T040630Z-source-investigation.json` with actual SHA256 `159249cbe58cffb431f9ac9b69a68669a1edbe5518fab2109346ee5ba40c7711`. The saved value `ba61718fc3faedfa41d6b906a86344dd9a35f922fec6aa0d142376df01d73e27` instead hashes `/private/tmp/cmm-round45-mineral-independent/correction-proof.json`. The independent reviewer confirmed that mapping. Record and source-input hashes remain correct.

Preserve the saved review. Add a native successor with separate correctly referenced and hashed dossier/proof evidence, while retaining the exact original scientific F1 and issue #146 resolution. Record this provenance correction explicitly. Final publication acceptance remains pending that successor and actual final review checks.

Exact reviewed artifact hashes and the finding are preserved in the paired JSON. No scientific record, existing review or source dossier was edited by this inspection.
