# Cassiterite identity and biomass-assisted electroflotation

UTC: 2026-10-12T04:42:42.467114+00:00. Researcher: Codex /root (GPT-6). Base:
`94d743a1b8bb3fe595f96e88f4cdb54a4ee72375`; branch `curate/cmm-expansion-round46-20261012`.
This dossier supports curation; an independent saved record review follows.

## Selection and identity

Cassiterite adds a distinct tin-bearing mineral and microbial-origin separation
mechanism to the current source frontier. The complete original study is
[Valdiviezo Gonzales, Huaman Pino and Torem (2013)](https://doi.org/10.1590/S0370-44672013000400016),
REM 66(4):507–512. The issue is December2013; the SciELO collection posting is
8January2014. These are different dates, not separate experiments.

The [September2026 IMA list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf)
page38 establishes Cassiterite, SnO2, statusG and year1832. Page1 defines G as
grandfathered and this year as the original-description year, not a sequential
approval ID. The mineral is distinct from tin, a commodity and the impure feed.
No inherited criticality entry or unsupported mineral identifier was added.
NCBI's [species37919](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=37919)
matches Rhodococcus opacus; it does not establish the paper's strain accession.

## Primary evidence inspected

The six-page original PDF and all original Figures1–6 were inspected visually,
including both panels of Figure5. The article has no tables. The publisher HTML,
Crossref identity, fresh IMA PDF pages1/2/38 and NCBI species entry were checked.
The acquisition and byte manifest are in the [JSON](./20261012T044242Z-source-investigation.json); raw PDFs,
images, extracted text and search responses remain outside Git at
`/private/tmp/cmm-round46-cassiterite-research`.

The paper's Methods (p508) grow the culture, harvest and wash biomass, then
sterilize it for20min at reported1atm; no viability test or sterilization
temperature is supplied. This supports a prepared microbial-origin reagent,
without metabolic activity. The original supplier is identified but no strain
accession is given. Dry mass is reported; printed cell-number equivalents
are not treated as verified live counts.

The feed is a ground/sieved Brazilian mineral sample, reported84.7% purity by
XRF without a full phase inventory. Flotation uses below37micrometre particles,
reported d50=8micrometres. Contact angles instead use106–210micrometre particles.
Methods distinguish the1L mineral-free bubble cell from the modified Hallimond
flotation apparatus. The record preserves this distinction.

Figure2 compares untreated/conditioned surface charge; Figure3 depicts
concentration/pH-dependent adhesion; Figure4 compares untreated/conditioned
hydrophobicity. Figure5 concerns bubbles without mineral. These support
surface modification while molecular forces/coagulation remain interpretations.
Figure6 reports a best plotted flotation endpoint near64.5% at the lowest
plotted dose (the text associates it with50mg/L), followed by lower outcomes
at higher doses. There is no plotted zero-biomass flotation arm. This endpoint
does not establish isolated tin yield, product grade or gangue selectivity.

## Contradictions and controls

- Both abstracts (p507) specify pH5; Results/Figure6 (p511) and Conclusions
  (p512) specify pH3. The abstract's51.4mA/cm2 is not silently combined with a
  harmonized pH recipe.
- Methods p509 specify2min conditioning; Results p511 specify5min, followed
  by6min flotation. Both remain explicit.
- The600mg/L dose is paired with3.4e14cells/mL in p508 Methods and
 34.47e12cells/mL in p510 discussion. No inferred correction or cell-count
  conversion is adopted.
- No-biomass surface/bubble comparisons differ from a matched flotation
  control. Contact-angle replication is at least3; flotation is repeated2times.
  The article does not define a detailed flotation-recovery formula or give a
  recovered-tin mass balance. No industrial deployment is inferred.

## Related sources and remaining leads

The public [2012 thesis preliminary file](https://www.maxwell.vrac.puc-rio.br/22109/22109_1.PDF)
contains13pages; only its title and English abstract were visually assessed.
Its pH5/64.5% statement and shared author/system make it a potential overlapping
source, not independent replication. The abstract also mentions quartz and a
mixed-mineral assay, but those results were not imported. The complete methods,
original figures and experiment correspondence remain to inspect. The full
110-page thesis has not been acquired or reviewed in this assessment.

A [2025 cassiterite–polymetallic sulfide bio-desulfurization paper](https://doi.org/10.3390/separations12030061)
surfaced as a discovery lead. Its full methods/figures/supplements and material
scope are not assessed here. It cannot be imported as pure cassiterite leaching
or industrial deployment from the search result. Ilmenite search results map to
existing issue104 and prior source dossiers, so they are not represented as a
new discovery or repeated unchanged access attempt.

## Search, provenance and reuse limits

The JSON records all six exact web queries and returned notice-search results.
No correction/retraction surfaced in this bounded search or inspected publisher
page; Crossref had no update-to entry and an empty relation map. No supplement
was identified in the complete article or its HTML, whose supplement-string
search was empty. Neither statement is literature-wide absence.

Deduplication included hidden/ignored files and followed relevant symlinks in
current and original records/research/reviews/history, plus166 referenced raw
directories:3548 metadata files, nine unavailable referenced roots. The eight
corpus lines were old query/provenance references or numeric false matches,
not an existing cassiterite record. Raw hits were authority/commodity/source
context and prior searches; the exact study DOI/title did not match those
bounded text artifacts. Binary PDFs/images/archives were not comprehensively
decoded by that search. The broad owner query also matched platinum and
humboldtine by substring; those are not cassiterite duplicates.

The SciELO page advertises CC BY-NC4.0, IMA page2 CC BY-SA3.0, and the thesis
preliminaries reserve reproduction rights. No full texts or images are committed.
Reading access is not treated as universal redistribution permission. Source
URLs, acquisition times, hashes, initial web-reader failures and the successful
public direct downloads are retained. Poppler was unavailable; rendering used
cached PyMuPDF outside every project checkout with `--no-project`.

## Curation handoff and actual checks

Created [cassiterite](../../../data/records/cassiterite.yaml) and canonical
[CREATE history](../../../history/records/cassiterite/2026-10-12T044022Z-codex-aeee34.yaml) with actual metadata. Named validation
passed:1record checked,0failed. No schema/validator change is needed: native
`separation` and microbial-origin inactive biomass fit the current contract.
The independent record review and batch gates remain separate requirements.
Future work should acquire the full thesis and investigate the2025 mixed ore
source, with fresh identity/experiment deduplication. No exhaustion is claimed.
