# Tungsten–nickel–iron scrap source investigation

UTC: 2026-10-12T03:20:48.739134+00:00. Base: `3fc8b873487ed2c1c253ecf131d99e09b8b8d452`. Investigator: Codex /root/round43_hardmetal.

## Decision and identity

Create [`tungsten-nickel-iron-alloy-scrap`](../../../data/records/tungsten-nickel-iron-alloy-scrap.yaml) as a secondary resource, supported by the complete official 2011 article. Discarded W–Ni–Fe cores are distinct from elemental tungsten, cemented WC scrap, mining tailings and grinding-fluid sludge. No criticality designation is inherited. The named single-file validator passed. Independent review and final batch gates remain coordinator work.

The [official item](https://ela.kpi.ua/handle/123456789/6650) and original PDF independently establish **Baranov G.A., Gavrish M.V., Sanikovich D.D.; KPI Mechanical Engineering 63 (2011), pp. 42–46**. Publication year 2011 differs from repository accession 2014-02-11. DOI is not asserted. Baranov 2013's similar-title reference instead names SNUNEI 2011 pp. 158–165; that bibliographic conflict is retained, without assuming a second experiment.

## Primary evidence and limits

All five original pages and Figures 1–9 were visually inspected by this agent during the same-day handoff acquisition; exact retained bytes are reused, not called a new round44 PDF download. Fresh official API metadata, inventories and license were checked in this round. The [JSON dossier](20261012T032048Z-source-investigation.json) records exact queries, paths, hashes, dates and access attempts.

- Pages 43–44 identify VNZh cores, reported 90.06% W/6% Ni/3.94% Fe, and a **separate reactor** for VK8 inserts, 92% WC/8% Co. Feed percentages are source statements, without an invented assay denominator.
- Figures 1–4 support chemical/mechanical disintegration in ferric solution and separation of W-bearing powder/liquor. The source's 99.95% W assertion lacks analytical method, denominator, impurities, uncertainty and phase evidence; no validated purity or extraction yield is accepted.
- Figures 5–9 measure compacted specimen surfaces after cold pressing or additional 500°C hot pressing, followed by image filtering/segmentation. These are not loose-powder distributions. Abstract 7 nm–1 µm/90% below 400 nm, body 7 nm–3 µm and concluding hot 200–500 nm/cold 100–300 nm remain unreconciled. The target 150 Å resolution and image noise also limit lower-tail interpretation.
- The authors mention *Thiobacillus ferrooxidans* as associated with the ferric solution and propose biological spent-solution regeneration. Missing inoculum, stock, growth/redox series and matched controls prevent a demonstrated microbial-mechanism claim. `microbial:false` scopes the accepted chemical/mechanical mechanism; it does not label the entire workflow sterile.
- pH, concentration, process temperature/time, loading, speed, vessel volume and replication are unavailable. Pressing parameters are analytical preparation, not processing conditions. No industrial throughput, cost advantage or complete product mass balance is established.

## Deduplication and comparator decision

Hidden/ignored-inclusive, symlink-following scans covered current and main records/research/reviews/history, 3,412 textual artifacts during root discovery, and 159 existing referenced raw directories. Nine missing referenced paths, exact commands and every error boundary are retained in JSON. Broad and specific terms found prior hardmetal context and the deferred 2011 reference, but no accepted owner for the W–Ni–Fe scrap experiment. Unextracted binaries and unrelated home/temp directories were not exhaustively searched.

The VK8 arm belongs conceptually to the existing cemented-tungsten-carbide-scrap owner. It has no separate powder-characterization result in this paper. That owner remains unchanged; its later Chaika conditions/results are not transferred into 2011, and the 2011 W-powder results are not attributed to WC. No unnecessary EDIT history was created.

## Reuse, provenance and validation

The official inventory lists ORIGINAL, LICENSE, TEXT and THUMBNAIL, with one original 42.pdf; no separate supplement is supplied in that bounded inventory. The license is a placeholder DSpace distribution form, not an established public reuse grant. Raw PDF/text/images stay outside Git. PDF SHA256: `22b7330a2173377a7910c22c79a3e4b44b2f56336a2e481e37d23ab1a6176583`; repository MD5 and byte count match.

Record SHA256: `ffc93d35f6dba2ec9a4dd3123687ee2d35142d7c4ab0e875680bb43140cfda60`. Actual CREATE sidecar: `history/records/tungsten-nickel-iron-alloy-scrap/2026-10-12T031901Z-codex-cb1e07.yaml`. Named validation completed to exit 0: **Checked 1 record; 0 failed**. Full validation/review gates are not claimed here.

## Remaining work

Resolve the 2011 citation conflict and inspect cited 2010/2012 originals before adopting any additional experimental claims. Better microbial controls, phase/purity assays, mass balances and unpressed size measurements would be needed to strengthen this record. Notice searches were bounded; no literature-wide source exhaustion is claimed. This dossier closes this agent's assigned current curation scope rather than opening another expansion round.
