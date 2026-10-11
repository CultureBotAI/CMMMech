# Silver curation dossier

Prepared 2026-10-11 UTC by Codex (GPT-6), curator agent `/root/cmm2_silver`.
This dossier supports `data/records/silver.yaml`; it is not its independent
scientific review. Base: `268498d0a9748f3a18955e35f175f67115f88b97` in
`/private/tmp/CMMMech-expansion-round2-20261011`.

## Selection and local coverage

Silver is an unrepresented element candidate in the existing authority
inventory (`research/sources/expansion-authorities/20261011T040103Z.*`).
The selected primary experiment offers a named strain, defined media,
no-cell and no-silver controls, X-ray diffraction, electron microscopy,
and a concentration-dependent growth limit. This is stronger evidence for
Ag(I) transformation than a color change alone.

Before addition, searched `data`, `research`, `reviews`, and `history` using
`rg --no-ignore --hidden -n -i 'silver|CHEBI:30512|AG259|law.*2006'` over
YAML/Markdown/JSON. Hits were the authority candidate inventory, not an
existing silver record. After drafting, searched the same scope for the
selected DOI and accession; the only matches were this new record/dossier.
Hidden and ignored files were included. The search boundary
is this worktree and this task's download directory; it does not establish
absence in inaccessible original worktrees or unrelated local downloads.

## Search log and acquisition

Live web searches on 2026-10-11 UTC, default first result set, no date/domain
filters and no subsequent pagination:

- `silver Shewanella oneidensis MR-1 nanoparticles silver controls XRD primary study full text`
- `silver Pseudomonas stutzeri AG259 crystalline nanoparticles 1999 full text controls`
- `"Impact of Silver(I) on the Metabolism of Shewanella oneidensis" correction retraction`
- `"Shewanella" "silver" "abiotic" nanoparticles Wang 2010 chloride`
- `"10.1128/JB.01277-09" correction erratum retraction`
- `"Impact of Silver(I)" "30" "pH"`
- `"Light-induced reduction of silver ions" "Shewanella" DOI`
- `"Formation of nanoscale elemental silver particles via enzymatic reduction by Geobacter sulfurreducens"`

Opened primary/authority pages rather than relying on discovery snippets:

- [Wang et al., primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2812967/),
  DOI [10.1128/JB.01277-09](https://doi.org/10.1128/JB.01277-09).
  Journal issue: February 2010; online publication: December 11, 2009.
- [ChEBI silver atom](https://www.ebi.ac.uk/chebi/CHEBI:30512): Ag, net charge 0.
- [NCBI MR-1](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=211586&mode=Info):
  taxon 211586 names the MR-1 entry (rank `no rank`), not a species-wide result.
- [US final 2025 notice](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm):
  silver in the complete 60-commodity list and the page 50497 table.

Web-tool PMC and PubMed opens returned browser challenges; Europe PMC full-text
XML failed with HTTP 500 on normal network retrieval. A legitimate direct
PMC HTML retrieval succeeded and contained complete article methods/results,
not a challenge page. The publisher abstract/full-text routes were variable;
the retained inspected full text is the PMC article. The initial restricted
shell network attempt failed DNS; an approved retry acquired public pages.
All outcomes, UTC times, resolved URLs, media types, sizes and SHA-256 hashes
are in `round2-silver-20261011-acquisition.json`. Raw files are outside Git at
`/private/tmp/cmm-round2-silver-20261011/`.

The article states copyright 2010 American Society for Microbiology; no
redistribution license was established. Full text and figures are not committed.
Only independently phrased factual curation and acquisition metadata are retained.
The inspected article HTML contained no supplementary-material link (link/text
search); this is bounded article-page coverage, not a universal absence claim.

## Evidence checked and claim boundaries

Read the complete Methods, relevant Results, Discussion and captions. Visually
inspected the original Figure 2 growth plot, Figure 3 XRD patterns and Figure 4
TEM image. No values were digitized or recalculated from the images.

| Proposed field/claim | Primary locator and interpretation |
|---|---|
| Organism | Methods, Bacterial strains and medium: MR-1 from the Manchester University Geomicrobiology Group collection. NCBI independently resolves its strain-level entry. |
| Biomass and medium | Growing cultures in defined medium containing chloride/phosphate, lactate and fumarate. pH 7.6 is a pre-sterilization adjustment, not a monitored constant assay pH. |
| Exposure conditions | Silver ion treatment: 10 mL inoculum into 80 mL medium; nominal AgNO3 exposure range 1-400 micromolar; 30 degrees C, dark, anaerobic handling; six biological replicates stated generally. Initial absolute cell concentration was not supplied in that protocol. |
| XRD arm | XRD analysis separately says 1 L, 100 micromolar AgCl, 30 degrees C without agitation for 24 h. It includes a cell-free comparison and centrifugation/water washing/anaerobic drying. Retain the AgCl-versus-AgNO3 discrepancy instead of silently reconciling the starting feed. |
| Solid phase | Results, Analysis of silver precipitates; Figure 3 A/B: control material has peaks assigned AgCl and Ag3PO4; the incubated culture sample has Ag peaks. This supports Ag(0) formation, without a quantitative phase fraction, purity or recovery yield. |
| Cell association | Figure 4 A/B/C: no-Ag control lacks the exposed-cell electron-dense particles. TEM location is consistent with surface-associated particles at the lower dose and greater intracellular accumulation at the higher dose. The record does not infer per-particle oxidation state from TEM contrast. |
| Dose limitation | Results, Impact of silver on growth; Figure 2: nominal 100 micromolar delays growth and 400 micromolar shows no growth. Growth was monitored by protein because precipitates interfere with turbidity. |
| Abiotic chemistry | Results report precipitation before inoculation and lower solution Ag(I) than nominal loading after no-cell incubation. This prevents interpreting nominal salt input as a free-ion dose or solution loss as exclusively microbial reduction. |
| Molecular cause | Discussion proposes cytochromes/flavins by analogy; the selected experiment does not establish a necessary reductase or energy-conserving silver respiration. |
| Scale | Laboratory cultures only. No ore/waste treatment, isolated recovered-product yield, or industrial deployment is demonstrated. |

Two additional internal inconsistencies were examined and not propagated as
facts: the abstract says doubling time decreases at the high dose, while the
Results report its increase (about 7.5 to 24 h); Methods call the inoculum
early exponential after about 40 h, whereas Discussion calls it late log.
The record reports delayed growth and the explicit inoculation volumes without
inventing a harmonized growth-phase label. The exact stated XRD starting salt
remains unresolved. No source correction was located in these bounded
title/DOI web queries or inspected primary-page notices; this is not an
exhaustive retraction-database search.

## Follow-up sources and search limits

- Klaus et al. (1999), DOI `10.1073/pnas.96.24.13611`, PMID 10570120 / PMC24112:
  primary discovery lead for *Pseudomonas stutzeri* AG259 silver-based crystals.
  Search results report multiple phases including Ag and Ag2S. Methods were
  not fully reviewed here; do not treat this as independent confirmation of
  a pure elemental-silver product or as a new elemental identity.
- PMID 35654200 (2022), *Effect of metal cations on antimicrobial
  activity and compartmentalization of silver in Shewanella oneidensis MR-1
  upon exposure to silver ions*: abstract-level lead for cation-dependent
  uptake and toxicity. It limits simplistic transfer across media, but its
  full methods were not acquired and no mechanism claim was imported.
- Law et al. (2008), *Formation of nanoscale elemental silver particles via
  enzymatic reduction by Geobacter sulfurreducens*, cited by the selected
  primary article and resolved to [PMC2583489](https://pmc.ncbi.nlm.nih.gov/articles/PMC2583489/):
  a future mechanistic extension for the existing silver identity, pending
  full primary and causal-control review. The discovery result highlights
  chloride-dependent bioavailability, consistent with retaining medium scope.
- *Light-induced reduction of silver ions to silver nanoparticles in aquatic
  environments by microbial extracellular polymeric substances (EPS)*,
  Water Research (2016), publisher discovery result: a different light/EPS
  system, not a direct contradiction of the selected dark culture experiment.
  Full methods and product identity remain unreviewed here.

No global search exhaustion is asserted. Candidate discovery, counterevidence
checks, identity confirmation, and record acceptance are separate steps. The
current schema represents the accepted qualitative transformation; micromolar
doses and growth results remain qualified prose, not `mg/kg` observations.

## Validation and review handoff

The parent reported the clean baseline before record writes: 307 passed,
3 skipped, 13 records and 22 histories valid. Single-record validation passed
with zero failures; history validation against the base passed with 26 sessions
and zero errors in the concurrent worktree. The separate CREATE session is
`history/records/silver/2026-10-11T042045Z-codex-c38021.yaml`, attached before
review. Silver record SHA-256 at handoff:
`61c5fde88f4f19b5c2bcd65b5ead39ead21fd315c208436052b29a1503b4536c`.
The reviewer should challenge the starting-salt
discrepancy, phase interpretation, growth-direction conflict, and proposed
enzyme/industrial claims rather than assuming a validator pass proves science.
