# Round 15 mineral curation dossier: dittmarite and glushinskite

Prepared 2026-10-11T09:58:47.071914+00:00 by codex / GPT-6 / codex (`/root/round15_minerals`).
Base `a2e2c82f11d97982f0cc1ae6be452a42b24a0ff0`, branch `curate/cmm-expansion-round15-20261011`.
The two records and canonical CREATE sessions are uncommitted working changes;
other round 15 additions are separately owned. Independent scientific review is pending.

## Selection and identity

These candidates resolve a substrate and a product already explicit in the
[Suyamud 2020 primary experiment](https://doi.org/10.1111/1462-2920.14949).
They reuse the experiment curated under [magnesium](../../data/records/magnesium.yaml),
not two new studies. The source calls its synthetic feed struvite, but its
Methods and Figure 5D identify **dittmarite**. The post-growth phase is
**glushinskite**. This distinction adds useful phase-specific coverage.

The [IMA September 2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf)
confirms dittmarite `(NH4)Mg(PO4)(H2O)` on PDF page 58, grandfathered with original-description
year 1887; glushinskite `Mg(C2O4)(H2O)2` on page 84, redefined in a 1987 special
procedure. Page 1 explains those columns. Neither year is encoded as an approval-ID
CURIE. Elemental Mg/P, struvite, dittmarite, glushinskite and a recovered wastewater
feed remain distinct. Neither record inherits constituent criticality.

## Evidence actually inspected

The primary version-of-record PDF was newly downloaded this round, succeeding
where round 5's ordinary acquisition had returned 403. Full Methods, relevant
Results and Discussion were read. Rendered Figure 1, Table 2 and Figures 3-5 were
inspected visually, as were the two IMA rows; no raw crystallographic refit was done.

- The selected solid-medium arm uses living *Aspergillus niger* ATCC 1015,
  1% w/v mineral feed in malt extract agar, 5-mm plugs over cellophane and
  seven days at 25 C in darkness. The exact strain ID NCBITaxon:380704 was freshly
  verified in NCBI XML; its current rank is strain.
- Figure 1C's synthetic-feed clearing image is at **three days**. Figure 5's
  collected crystal patterns are at **seven days**. Crystals were extracted in
  80 C water, washed at least three times and vacuum-desiccated.
- Figure 5 compares feed diffraction controls with the post-growth glushinskite
  phase assignment, representative of at least three determinations. Figure 4
  shows Mg/C/O product EDXA. Table 2 gives the 1% synthetic-feed agar pH as
  7.06 +/- 0.01 initially and 4.09 +/- 0.45 at seven days (means +/- SD, three
  independent replicates). This pH quantity remains scoped prose, not an mg/kg cell.
- Acidification and mineral-free fungal controls do not isolate oxalate-specific
  chemistry. Amorphous debris is reported. Neither halo area nor a phase pattern
  establishes a complete-conversion fraction, pure product, isolated yield or
  industrial operation. The wastewater origin belongs only to the natural feed.

## Adverse evidence and uncurated claims

The paper's synthetic-struvite terminology is corrected through its own XRD
identification, not a guessed hydration state. The Discussion reaction expression
for magnesium and oxalate is not adopted. Source methods describe a 105 rpm liquid
culture while Figure 9 says 125 rpm; no liquid-arm results are curated here.
The stated equimolar feed preparation is not repeated as an established ratio;
only reagents, pH and physical preparation plus measured phase identity are used.
The 105 C feed oven treatment described for the liquid experiment is not silently
transferred to the selected solid-medium arm.

No affecting correction/retraction or separate supplement surfaced in the bounded
first-result searches or inspected publisher text. That is not proof of absence.
No raw diffraction dataset, independent phase purity or acid-matched causal assay
was acquired. The publisher gives first publication as 20 February 2020; PubMed
lists Epub 7 March 2020 and journal issue April 2020. Records cite the year and issue,
without pretending those metadata dates are one event.

## Search, acquisition and reuse

The [machine-readable receipt](round15-mineral-sources-20261011.json) records exact
queries/provider/date and first-result, unpaginated bounds; source URLs, acquisition
times, hashes and media types; local ignored/hidden-inclusive search boundaries;
conditions, interpretations and actual single-record validation receipts.
The raw directory is `/private/tmp/cmm-round15-mineral-raw`. All PDFs remain outside Git.
The paper and repository state CC BY, and the IMA list states CC BY-SA 3.0 on page 2.
The taxonomy XML has no license declaration and its separate reuse terms were not
assessed. This is claim curation, not a bulk licensed data redistribution.

Deduplication covered `data`, `research`, `reviews`, `history`, `.claude` and named
round 5/14/15 evidence directories using `rg --no-ignore --hidden -L`; no relevant
symlinks were present in the repository inventory. Existing mentions and study
coverage were retained. The two exact mineral roots were absent within those
checked repository bounds before creation. This is not a machine-wide absence claim.

## Handoff and validation

| Target | Canonical CREATE sidecar | Author validation |
|---|---|---|
| [glushinskite](../../data/records/glushinskite.yaml) | `history/records/glushinskite/2026-10-11T095727Z-codex-e44619.yaml` | One record checked, zero failed |
| [dittmarite](../../data/records/dittmarite.yaml) | `history/records/dittmarite/2026-10-11T095732Z-codex-93ecbd.yaml` | One record checked, zero failed |

Root's baseline terminal check passed (307 tests, three skips, 119 records,
135 histories) before authoring. Both individual validations exited zero after
sidecar attachment. These mineral additions required no schema or validator change; the separate
brine pilot led root to add `primary_resource`. Final batch gates,
manual exact-hash review coverage and independent scientific review remain the
acceptance steps; this source assessment is not their substitute.

Priority is independent review against species rows and the exact solid-media
figure/control scope. Further natural-dittmarite experiments, quantitative product
purity/recovery and liquid-arm reconciliation are future evidence work, not claims
filled into these records.
