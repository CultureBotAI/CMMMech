# Round38 mimetite source investigation

UTC: 2026-10-11T23:33:30.347850+00:00

Author: codex (GPT-6; codex), /root/round27_eaf_slag. This is a curation source dossier, not an independent scientific review.

## Scope, selection and state

The isolated branch is `curate/cmm-expansion-round38-20261011` at trusted base `f3d674806df8f5fd7925e46f1dcfec70cace706a`. The source handoff justified one distinct mimetite mineral owner. The complete original publisher text and phase-identification images support a bounded laboratory association; model-only extensions to other minerals are excluded. Criticality is unrecorded.

The author created [mimetite.yaml](../../../data/records/mimetite.yaml) and [its canonical CREATE session](../../../history/records/mimetite/2026-10-11T233210Z-codex-16866e.yaml). Their frozen SHA-256 values are `c9e5d430d0f060e0e8cb4539f9bcec86168d657f07682a9b8c420ecec2e858a2` and `959c816087566564530ded75718c7916022e3d9728b739f09ac1459269c7f935`. The inline change event is separate from the sidecar. No existing record or shared file was edited.

## Search and prior coverage

The refreshed search used `rg --no-ignore --hidden --follow` over new-worktree and original-checkout records, research, reviews and history, then 115 referenced raw roots. Directory traversal tracked inodes to avoid cycles. The two maintained-text matches were the same prior frontier lead in each checkout, not accepted mimetite records. Earlier raw hits were authority entries, references or metadata. The pyromorphite record was read; its Topolska/Kato studies address distinct phosphate-mineral experiments. Binary contents were not universally decoded, and no machine-wide absence is asserted.

Exact query strings, date, returned-set limits, file inventories, roots and result hashes are retained in the paired JSON. The investigation used exact DOI/PMC, title, PDF, supplement, mineral-identity and correction/erratum/retraction searches. This is a bounded search, not a systematic review. Initial discovery was completed before round38 authoring; its immutable outside-Git handoff and current-pass receipts are hashed separately.

## Evidence inventory

| Source | Role and inspected material | Curation use |
|---|---|---|
| [IMA September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Reused same-day official PDF; original p144 row, definitions/terms | Mimetite, Pb5(AsO4)3Cl, grandfathered, 1832 |
| [Handbook of Mineralogy](https://handbookofmineralogy.org/pdfs/mimetite.pdf) | Original one-page PDF and render | Independent identity corroboration |
| [Ceci et al. 2015](https://doi.org/10.1128/AEM.00726-15) | Complete claim-bearing publisher HTML, Figures 1–3, Table 1 image and Table 2 HTML | One primary culture experiment; modeled extensions are context only |
| [NCBI 5061](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/5061/dataset_report) | Fresh same-day authoritative JSON | Species identity only |
| [ATCC 201373](https://www.atcc.org/products/201373) | Fresh same-day catalogue HTML | Explicit culture designation |

The record locates accepted observations and limitations at the source's Methods, Results, Figures 1–3 and Tables 1–2. It retains the natural-feed impurities, incomplete Methods formula, biomass-versus-mineral denominator, differing statistical procedures, spatial pH uncertainty, model caption/unit conflicts and unshown preliminary measurements. No measured recovery percentage, arsenic fate or independent causal pathway is asserted. Main text, mirrors and images belong to one experiment, not independent replications.

## Access, notices and reuse

Publisher HTML was available through the read-only web tool even though direct HTML/PDF requests returned 403. The retained publisher-web JSON files are tool-returned text, not downloaded raw HTML. All three original figure JPEGs and Table 1 were acquired from links exposed by the publisher. Europe PMC XML returned 500; its apparent media download is a 296-byte XML error, **not a ZIP or supplement**. Direct PMC returned a challenge. Dundee supplied repository metadata, and Sapienza's bitstream was restricted; neither establishes main-PDF access.

No supplementary-material link was identified in the complete publisher page, but the failed media route cannot prove universal SI absence. The bounded notice search returned no corrective notice; Crossref has no update relation. DOI 10.1128/AEM.01803-15 was checked as an editorial spotlight, not misclassified as a correction. Online-publication dates differ between metadata presentations; the record uses the verified 2015 volume/issue/pages without asserting a precise online date.

Copyrighted originals remain in `/private/tmp/cmm-round38-mimetite-research/raw`, with reused IMA provenance under `/private/tmp/cmm-round37-lindbergite-research/raw`. ASM copyright/non-commercial TDM metadata and Handbook access are not a CC redistribution grant. The paired JSON pins 26 current raw artifacts and 4 reused artifacts, including URLs/times/checksums in acquisition receipts. No original source text or image is vendored here.

## Checks and remaining work

Fresh parent baseline `just check` passed before writing: 308 passed, 3 skipped in 115.37 s; 203 records and 234 histories valid. The baseline receipt and its log hash were verified. Author-side named validation passed: `uv run --locked cmmmech validate data/records/mimetite.yaml`, 1 checked, 0 failed. The CREATE helper completed successfully, and all recorded raw hashes were reverified. Full cohort gates and independent exact-state review remain the coordinator's next steps; this dossier does not claim those are complete.
