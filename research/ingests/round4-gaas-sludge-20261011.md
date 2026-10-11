# GaAs-production hydroxide sludge: 2026-10-11 curation dossier

Prepared by Codex (GPT-6; Codex) in
`/private/tmp/CMMMech-expansion-round4-20261011`, based on
`c081a749cd63feafcc25414f5ad006d1f78f1e36`. The parent confirmed the pre-change
baseline before record creation: 307 tests passed, 3 skipped, 21 records and
30 histories valid. This dossier records research and curation, not a
self-review or an independent replication.

## Selection, identity and deduplication

The round-three frontier and
[round-two Ga/As dossier](round2-gallium-arsenic-20261011.md) deferred this
specific waste stream. Accessible primary characterization and controlled
leaching data now support a distinct `secondary_resource` root,
`cmmmech:gaas-production-hydroxide-sludge`. Its published process is more useful
than an identity-only record, provided causal and deployment claims remain
bounded. The gallium and arsenic element records already curate constituent
outcomes from the **same experiment**; three records must not be counted as
three independent studies.

The feed is the neutralization sludge from industrial GaAs wafer production,
with material supplied by Freiberger Compound Materials GmbH according to the
acknowledgments. It is not crystalline GaAs powder, elemental Ga/As, pure
ferrihydrite or a universal semiconductor-waste composition. No suitable
resource-specific external ID is asserted. No criticality entry is inherited
from the constituent elements, and omission does not assert that a complete
criticality list excludes this resource.

Before writing, hidden- and ignored-inclusive searches covered `data`,
`research`, `reviews` and `history` in this worktree:

```sh
rg --no-ignore --hidden -l -i 'GaAs|1807986|gallium.*hydroxide|hydroxide.*sludge' data research reviews history
find data research reviews history -type l -print
```

Matches were the existing Ga/As element records, their reviews and dossiers,
the nickel lead and frontier/publication reports; no existing maintained
sludge resource record was found within those roots. The symlink search
returned none. Referenced raw evidence under
`/private/tmp/cmmmech-gallium-arsenic-20261011` was also searched using
`rg --no-ignore --hidden` over JSON, XML, HTML and text files; it contains the
same study and receipt. This is a scoped deduplication result, not a claim
about every home directory or external database. Prior Ga/As records and
their accepted round-two scientific reviews were read before curation.

## Verified sources and acquisition

**Fritze MT, Haubrich F, Otto A, Schippers A and Hedrich S (2026).**
*Bioleaching of GaAs metal hydroxide sludge: a biohydrometallurgical alternative
to conventional acid leaching.* Frontiers in Microbiology 17:1807986.
[Publisher full text](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1807986/full),
[DOI](https://doi.org/10.3389/fmicb.2026.1807986). Published 10 June 2026;
PMID 42358260, PMC13290815. Publisher identity and main text were rechecked
live on 2026-10-11. Retained Europe PMC XML was rehashed and independently
read, especially Sections 2.1–2.3, Tables 1–2, Section 3.2, Section 3.4,
acknowledgments, data availability and license. Figures 2 and 3 were visually
inspected, beyond captions and the publisher's AI-assisted alternative text.

[NCBI Taxonomy 930](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=930&mode=Info)
was checked live on 2026-10-11: *Acidithiobacillus thiooxidans*, species rank,
with DSM 14887 among the type-strain collection labels. The organism CURIE
is species-level; DSM 14887 remains experimental strain context.

The source carries [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
in its inspected XML permissions. Raw source bytes remain outside Git;
only attributed curation and provenance are committed. Source/derived file
hashes and retrieval receipts are in
[the machine-readable companion](round4-gaas-sludge-20261011.json). Reused
round-two HTML/XML/Figure 3 acquisitions retain their original retrieval
times; a round-four recheck is not relabeled as a new download.

**Access improvement:** Figure 2 and the Europe PMC
[`supplementaryFiles` archive](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13290815/supplementaryFiles)
were acquired successfully in this round after an initial sandbox DNS failure.
The valid ZIP contains `Supplementary_file_1.docx` (1,049,659 bytes), unlike
the earlier HTML challenge returned under that filename. The DOCX text was
extracted and read. Its embedded Figures S1–S3 were matched to captions via
document relationships; the embedded SVG versions were rendered on a white
background and visually inspected. The entire DOCX page layout was not
rendered. No curve digitization, numerical SD estimation or raw-replicate
reanalysis was performed. Prior immutable review reports correctly describe
their earlier failed-access state and have not been rewritten.

The supplement contains plots and captions, not the missing sampled-liquid
separation protocol or raw ICP-MS replicates. The data-availability statement
offers raw data on author request; no author was contacted and no raw
replicate dataset was acquired.

## Claim map and selected process

| Claim | Primary locator | Curation decision |
|---|---|---|
| Resource origin | Section 2.1; acknowledgments | Neutralization sludge from industrial GaAs wafer manufacture, supplied for this study; no assertion about all semiconductor wastes. |
| Measured composition | Table 1; Section 2.1 | Handheld XRF: Si 32.81%, Fe 6.97%, Ga 1.21%, As 1.34%, P 0.27%, Ca 1.83%. Separate ion-selective electrode assay: fluoride 0.538%. Retain reported percent basis without inventing dry-weight normalization or phase fractions. |
| Phase and valence | Section 2.1 | Authors describe amorphous ferrihydrite; arsenate association is assumed and Ga association expected. No newly measured As valence or pure mineral root follows. |
| Feed preparation | Section 2.1 | Dried 60 degrees C for 48 h, then mortar-homogenized. |
| Organism and biomass | Sections 2.2–2.3 | Living sulfur-oxidizing type-strain DSM 14887 cultures, adapted to 5% w/v sludge with Al. No strain-specific taxon ID invented. |
| Selected assay | Section 2.3; Table 2; Figures 2–3 | 3% w/v sludge, 50 mL working volume, HBS medium, 1% elemental sulfur, initial pH 1.8, 30 degrees C, 8 days. This is not the 25 mL/120 rpm aluminum-optimization assay. |
| Initial acid and Al | Section 2.3; Table 2 | 1 mL sulfuric acid initially; 12.9 mM Al, molar Al:F 1.5:1, added before inoculum to counter fluoride inhibition. Acidity is not attributed entirely to microbes. |
| Replication and comparators | Section 2.3; Figure 3 caption | Biotic setups triplicate; uninoculated initial-pH negative control and separate acid-adjusted comparator. Equivalent independent replication of all abiotic arms is not established. |
| Assay and endpoint | Section 2.3; Section 3.2; Figure 3 | Source calls the ICP-MS assay dissolved elements. Final leaching fractions: Ga 94%, As 68%, Fe 73%, versus acid-adjusted Ga 77%, As 66%, Fe 62%. Each denominator is that element's leaching yield, not total sludge or isolated product. |
| Iron reduction | Section 3.2; Figure 2c | Dissolved ferrous iron increases but ferric iron remains. No direct Ga/As redox or identified molecular catalyst is demonstrated. |
| Higher-load counterevidence | Supplementary Figure S2 | Separate 5% assay ends at 11 days with biotic As leaching below its acid-adjusted comparator. This visibly precludes a universal microbial-enhancement claim; no exact value is read from pixels or loading-only cause inferred. |
| Downstream process and scale | Section 3.4 | Chemical processing is faster and handles higher loading in the cited comparison. Silica removal, further iron reduction and precipitation remain process-development issues here, not proof of selective microbial product isolation or industrial bioleaching operation. |

The native quantitative-observation contract is exact concentration cells in
mg/kg. These composition and leaching percentages remain qualified prose;
no schema change or inferred unit conversion was needed.

## Contradictions, alternative explanations and unresolved details

1. Rapid gallium dissolution is mostly acid-driven: Section 3.2 reports 86%
   leached by day 1. The authors call their abiotic controls simplified and
   explicitly request replicated confirmation of microbial facilitation.
   Figure 2 shows nonidentical pH histories despite acid adjustment. A
   statistically proven microbial increment is not claimed for any element.
2. The 3% As endpoint difference is small; the 5% supplementary arm even has
   lower final biotic As leaching. Neither observation supports a uniform
   microbial benefit. Different arm duration and loading prevent attributing
   this difference solely to solids concentration.
3. Abstract Al:Fe conflicts with methods/results Al:F. The flask-specific
   Table 2 value is 1.5:1; the separate optimization/reactor 1.4:1 value is
   not substituted. The supplement's Figure S1 supports the optimization
   context, but no optimum is promoted to a universal ratio.
4. Section 2.3 labels inoculum 10% w/v. Its unusual basis is preserved, not
   silently corrected to v/v. Main-assay shaking speed and sampled-liquid
   separation protocol remain unresolved. The optimization assay's 120 rpm
   is not borrowed.
5. Section 3.2 places initial 24% arsenic at day 1, whereas Figure 3 places
   it at day 0. It also describes pH 1.8 on day 4, unlike Figure 2a's plotted
   trajectory. Neither inconsistent time-specific value is curated. Initial
   pH 1.8 is the methods' prescribed starting condition, not a digitized
   measurement for every flask/timepoint.
6. Source phase association and sulfur-intermediate explanations are partly
   interpretive. The record does not promote them into measured mineralogy,
   arsenic valence, enzyme causality or selective product formation. Source
   yield percentages are retained without inventing uncertainty, significance
   or a full mass balance.

## Bounded correction and conflicting-source search

Session web search on 2026-10-11 inspected first returned result sets, with
no date/domain filters and no further result-page traversal:

```text
"10.3389/fmicb.2026.1807986" correction retraction erratum
"GaAs" "hydroxide sludge" bioleaching control fluoride
"Fritze" "1807986" "Supplementary_file_1"
```

No affecting correction/retraction notice was identified in those returned
sets; this is not proof that none exists. The source's own controls, source
inconsistencies and newly inspected Figure S2 are the most direct evidence
against overgeneralization. Searches surfaced a related fluoride paper and
an earlier conference contribution, not a verified independent replication
of the same controlled sludge assay:

- Fritze and Hedrich (2026), *Fluoride toxicity and mitigation strategies in
  acidophilic bioleaching microorganisms*,
  [DOI 10.1007/s00253-025-13677-x](https://doi.org/10.1007/s00253-025-13677-x),
  PMC12831704. Candidate background lead; full methods not assessed here.
- Fritze and Hedrich (2024), *Bioleaching of Gallium from Metal Hydroxide Sludge
  Produced as a Waste Product During GaAs Wafer Production*, proceedings
  contribution, pp. 1013–1015. Experiment overlap and full evidence require
  inspection before counting it as independent support.

## Curation, checks and handoff

Created `data/records/gaas-production-hydroxide-sludge.yaml`, its separate
inline creation event and canonical sidecar
`history/records/gaas-production-hydroxide-sludge/2026-10-11T045526Z-codex-51d3db.yaml`
with actual Codex/GPT-6/Codex metadata. The record passed single-file validation
(one record, zero failures). The companion records the final SHA-256. Parent
coordination owns corpus/history/batch gates, independent scientific review
and authorized publication; none is claimed as completed by this dossier.

Remaining scientific work: obtain raw measurements and independent replicated
pH-controlled comparisons; clarify inoculum basis, sampling/separation and
main-assay shaking; assess batch variability and measured phase/speciation;
test full downstream mass balance and product purity. Existing Ga/As reviews
can cite this newly accessible supplement during a future substantive review,
without rewriting their historical acquisition limitations. No claims need
to be broadened to use the present evidence.
