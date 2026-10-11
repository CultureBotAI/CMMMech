# Gallium and arsenic: 2026-10-11 curation handoff

Prepared by Codex (GPT-6) in `/private/tmp/CMMMech-expansion-round2-20261011`,
based on `268498d0a9748f3a18955e35f175f67115f88b97`. This is a source dossier;
the independent structured record reviews are separate. The parent reported
the pre-change baseline: 307 tests passed, 3 skipped, 13 records and 22 history
records valid. The present source search does not establish global exhaustion.

## Selection and identity

The previous nickel dossier identified Fritze et al. (2026) as a next lead.
It supplies accessible primary methods, comparator assays and explicit limits
for two unrepresented elements. It is **one experiment**, reused for distinct
element records rather than counted as two independent confirmations. Gallium
is the target metal, while arsenic is co-mobilized and its microbial advantage
is not established. The heterogeneous hydroxide sludge remains a distinct
secondary-resource candidate, deferred from this batch.

Live authority checks on 2026-10-11:

- [ChEBI CHEBI:49631](https://www.ebi.ac.uk/chebi/CHEBI:49631): gallium atom,
  formula Ga, net charge zero. Secondary IDs are not separate elements.
- [ChEBI CHEBI:27563](https://www.ebi.ac.uk/chebi/CHEBI:27563): arsenic atom,
  formula As, net charge zero. Neither atom ID identifies experimental ions.
- [NCBI Taxonomy 930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info):
  *Acidithiobacillus thiooxidans*, species rank; DSM 14887 is listed among its
  type-strain collection identifiers. The record retains strain in context
  rather than pretending that the species ID resolves only that strain.
- [USGS Final 2025 List](https://www.govinfo.gov/content/pkg/FR-2025-11-07/html/2025-19813.htm),
  Federal Register 90:50494–50497, 7 November 2025, document 2025-19813:
  complete 60-commodity list and table inspected. Gallium and arsenic are
  included. Arsenic had been proposed for removal in the draft; the final notice
  explains its retention. Records claim this edition, not timeless status or
  that every host waste/mineral is designated.

## Search boundary and exact queries

Hidden/ignored-inclusive `rg --no-ignore --hidden` searches covered `data`,
`research`, `reviews` and `history` for `gallium|arsenic|1807986|Fritze` and the
verified element IDs. No pre-existing Ga/As element record was found in this worktree;
authority inventory entries and the nickel research lead already existed.
`find data research reviews history -type l -print` returned no symlinks.
Referenced local evidence directories searched were
`/private/tmp/cmmmech-nickel-evidence-20261011`,
`/private/tmp/cmm-expansion-authorities-20261011` and
`/private/tmp/cmm-next-eu`, including hidden and ignored text/JSON/XML files.
Those authority downloads contained prior Ga/As list mentions. Other home/temp
trees and the inaccessible original checkout were not searched; no
machine-wide novelty claim is made. New raw acquisitions are separately located
under `/private/tmp/cmmmech-gallium-arsenic-20261011`.

Web search provider: the session's web search on 2026-10-11; no date/domain
filters beyond explicit `site:` query text. Returned result sets were examined;
no subsequent result pages or citation-index census were traversed.

```text
site:ebi.ac.uk/chebi "gallium atom"
site:ebi.ac.uk/chebi "arsenic atom"
"10.3389/fmicb.2026.1807986" correction OR retraction OR erratum
"Bioleaching of GaAs" sludge control arsenic
site:ebi.ac.uk/chebi "CHEBI" "gallium atom"
site:ebi.ac.uk/chebi "CHEBI" "arsenic atom" -trichloride -molecular
"Fritze" "1807986" "Supplementary_file_1"
"Fritze" "1807986" PMCID
"10.3389/fmicb.2026.1807986" erratum correction retract
"GaAs" "thiooxidans" "abiotic" sludge
"gallium" "bioleaching" "no" "control" "arsenic"
"Bioleaching of GaAs metal hydroxide sludge" correction retraction erratum
"arsenic" "gallium" "Fritze" "contradict"
```

These bounded queries did not locate a correction/retraction notice for the
selected paper. They do not prove that none exists. The source's own controls,
material-specific limits and internal inconsistencies provide the most direct
counterevidence to overbroad interpretation. Broader search results provided
additional leads below, not verified competing outcomes on the identical sludge.

## Acquired primary evidence

Fritze MT, Haubrich F, Otto A, Schippers A and Hedrich S (2026).
**Bioleaching of GaAs metal hydroxide sludge: a biohydrometallurgical alternative
to conventional acid leaching.** Frontiers in Microbiology 17:1807986.
[DOI and publisher full text](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1807986/full).
Published 10 June 2026. PubMed identifier 42358260; PMC13290815.

The publisher HTML and
[Europe PMC XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13290815/fullTextXML)
were successfully acquired and inspected, including Methods 2.1–2.4, Tables
1–3, Results/Discussion 3.1–3.4, conclusion, data availability and references.
Figure 3 and Figure 5 images were downloaded and visually inspected, beyond
their captions and the publisher's explicitly AI-assisted alternative text.
No curve digitization or new measurements were performed. The paper's CC BY
4.0 license was inspected; original authors and publication are credited here.
Raw full text and images are outside Git. Exact URLs, byte sizes, SHA-256 and
successful UTC retrieval times are in
[the acquisition receipt](round2-gallium-arsenic-20261011-acquisition.json).

Access limits: initial sandbox CLI downloads failed DNS, then authorized
network retrieval succeeded. PubMed and PMC browser routes returned challenge
pages; they were not treated as inspected full text. Web figure calls timed
out but direct retrieval succeeded. The publisher HTML/XML names
`Supplementary_file_1.docx` but exposes no downloadable publisher URL in the
inspected markup. Europe PMC's `supplementaryFiles` endpoint timed out; the
direct PMC supplement URL returned HTML rather than DOCX despite HTTP 200.
The supplement was **not inspected**. Its Figures S1–S3 are not the basis for
curated quantitative claims. Raw data are offered by the authors in the data
availability statement; this pass did not contact authors or acquire raw
replicates. The HTML challenge is identified as such in the receipt.

## Claim map and adversarial boundaries

| Claim | Exact primary locator | Curation decision |
|---|---|---|
| Feed origin and identity | Section 2.1; Table 1 | Industrial GaAs production neutralization sludge, dried 60 degrees C for 48 h and homogenized; measured 1.21% Ga, 1.34% As by h-XRF. Not elemental Ga, crystalline GaAs feed or pure ferrihydrite. |
| Phase/speciation | Section 2.1 | Iron described as amorphous ferrihydrite; Ga association expected and As(V) association assumed. Do not assert measured arsenic oxidation state. |
| Curated biological assay | Sections 2.2–2.3; Table 2 | Type strain DSM 14887, adapted to 5% sludge; 3% w/v leaching arm, 50 mL, HBS, 1% sulfur, initial pH 1.8, 30 degrees C, 8 days, triplicate biotic assays. |
| Aluminum and acidity | Section 2.3; Table 2; Figure 2 caption | Flask-specific 12.9 mM Al, molar Al:F 1.5:1, 1 mL sulfuric acid initially. Do not substitute optimized/reactor 1.4:1. |
| Controls and analysis | Section 2.3; Figure 3 caption; Section 3.2 | Initial-pH uninoculated control and comparator acid-adjusted to biotic pH; dissolved-element ICP-MS. Simplified controls need replicated confirmation. |
| Gallium outcome | Section 3.2; Figure 3 | Reported final 94% versus 77% comparator; 86% dissolved within first day. Strong acid contribution, no isolated product or proven selective recovery. |
| Arsenic outcome | Section 3.2; Figure 3 | Reported final 68% versus 66% comparator; do not infer meaningful microbial benefit from this small difference. No arsenic redox measurement. |
| Later reactor experiments | Section 2.4; Table 3; Figures 4–6 and Section 3.3 | Inspected as context, not a second curated mechanism. One run per condition is described, no matched abiotic reactor arm; Figure 5 trajectories and wording differ from exact headline recovery values. Avoid replacing the controlled flask result with the headline. |
| Downstream recovery and deployment | Section 3.4 | Chemical precipitation is discussed from prior work and future process considerations. Lab leaching and industrial feed provenance do not demonstrate industrial microbial recovery. |

Unresolved source details preserved rather than normalized:

1. The abstract says Al:Fe while the methods, tables and discussion consistently
   use Al:F. The curated flask dose follows Table 2.
2. Section 2.3 labels inoculum 10% w/v; no silent conversion to v/v is made.
   The shaking speed of the main leaching assay is not stated there. The
   separate aluminum-optimization assay's 25 mL volume and 120 rpm must not
   be imported into the 50 mL leaching assay.
3. Section 3.2 places initial 24% arsenic at day 1; the actual Figure 3 places
   that point at day 0, with lower As at day 1. No initial As value or derived
   rate is curated. Final percentages are reported prose values; no numeric
   SD or fitted significance was invented from error bars.
4. Main methods do not resolve the sampled-liquid separation protocol for
   ICP-MS. The study calls the assay dissolved elements; this is retained as
   its analytical description rather than asserting a verified filtration size.
5. Molecular iron-reduction routes discussed through sulfur intermediates are
   interpretive here. They do not establish direct enzymatic Ga or As redox.

All percentages stay in qualified prose. The native observation schema permits
exact mg/kg concentration cells, not leaching percentages; no schema change or
conversion was needed.

## Further leads and handoff

These remain research candidates, not accepted claims or records:

- **Hydroxide sludge from GaAs wafer production:** distinct secondary-resource
  root possible from the inspected experiment; define the waste stream narrowly
  and do not inherit Ga/As commodity criticality. Deferred from this batch.
- **GaAs/GaN microbial experiments:**
  [Chung et al. 2022, DOI 10.3389/fmicb.2022.970147](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2022.970147/full),
  discovered by countersource search; publisher title/authors and abstract
  inspected. Full methods and taxon/strain identities
  still require assessment before extending gallium. The title is *Genome
  mining to unravel potential metabolic pathways linked to gallium bioleaching
  ability of bacterial mine isolates*; genomic predictions must be separated
  from measured leaching.
- **Semiconductor waste and *Cellulosimicrobium funkei*:**
  [Maneesuwannarat et al. 2016, DOI 10.1016/j.psep.2015.10.008](https://doi.org/10.1016/j.psep.2015.10.008),
  present in the inspected primary paper's references. Full text not assessed.
- **LED waste:** [DOI 10.1016/j.wasman.2018.07.010](https://doi.org/10.1016/j.wasman.2018.07.010)
  and [DOI 10.1016/j.jhazmat.2019.05.041](https://doi.org/10.1016/j.jhazmat.2019.05.041)
  are primary-reference leads for a different resource and indirect leaching
  designs; not independent support for the present sludge experiment.
- **Nickeline-bearing ore / heterotroph:** search returned a primary article,
  *Unveiling the potential of Glutamicbacter nicotiana for enhanced bioleaching
  of nickel and valuable metals from low- and high-grade nickeline ores*,
  [publisher PII S2213343724002719](https://www.sciencedirect.com/science/article/pii/S2213343724002719).
  Candidate arsenic/nickel mechanism and mineral context, with title spelling,
  taxon identity, DOI, feed phases and controls still to verify.

The next practical work is independent review of the current Ga/As record bytes,
then review-driven corrections and the full batch gates. Public acquisition of
the supplement/raw data and a controlled independent sludge replication would
resolve scientific limits; they are not prerequisites for the deliberately
narrow claims retained here.
