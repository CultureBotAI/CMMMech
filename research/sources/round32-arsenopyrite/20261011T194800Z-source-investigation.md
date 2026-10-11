# Arsenopyrite source investigation and curation handoff

Investigation timestamp: 2026-10-11T19:48:00Z.

Curator: codex (GPT-6; codex). This is a curator handoff, not an independent scientific review.

Working revision: `09c15cbfb7699e40ae4648b6b414784a00b488db` in `/private/tmp/CMMMech-expansion-round32-20261011`. The exact-tree baseline is documented in `/private/tmp/cmm-round32-baseline-receipt.json`; it reuses the immediately preceding successful fresh-main checks, not a new baseline run. No schema or validator change was needed.

## Decision and identity

Curate one mineral record, [arsenopyrite](../../../data/records/arsenopyrite.yaml), from the complete 2019 primary experiment. The September 2026 IMA-CNMNC list, PDF page 15, gives Arsenopyrite, FeAsS, status A and `1962 s.p.`. Page 1 defines the special-procedure field; it is not an accession invented for the record. A same-day retained copy was rechecked, not freshly retrieved. Its origin, upstream acquisition timestamp and hash are in the raw reuse receipt.

The natural high-purity specimen is distinct from elemental arsenic, dissolved As species, mixed pyrite-arsenopyrite concentrates and refractory gold ore. Neither gold content nor gold recovery is measured in this experiment. No criticality claim is inherited from an element or commodity. NCBI Taxonomy 920 was verified at its issuing service as the species Acidithiobacillus ferrooxidans; it does not establish a strain accession or identity beyond the source's species assignment.

## Search and duplicate assessment

Before record creation, `rg --hidden --no-ignore --follow --text -n -i` searched `data/records`, `research`, `reviews` and `history` in both this worktree and the original checkout. Search terms included `arsenopyrite`, `FeAsS`, `arsenopirita` and normalized DOI strings `10.3390/met9121320`, `10.3389/fmicb.2020.01773` and `10.3390/biology14050550`. There were no matches in those scientific trees at that time. This includes ignored files and follows relevant symlinks; it is not a machine-wide absence claim.

Referenced raw roots were also searched with the same flags: `/private/tmp/cmm-round30-pyrrhotite-research`, `/private/tmp/cmm-round13-mineral-raw`, `/private/tmp/cmm-next-li`, `/private/tmp/cmm-round12-aluminium-boron-raw` and `/private/tmp/cmm-round28-black-shale-research`. All existed. Eleven matching lines concern old literature references, IMA identity, search snippets or geological context; none represents the selected 2019 experiment already curated. The existing arsenic record concerns sludge co-mobilization and is not this mineral. Exact commands, output and boundaries are retained in `raw/dedup-receipt.json` and its two linked outputs. The present investigation's own newly acquired files are explicitly related versions of their respective articles, not new independent experiments.

Live web search on 2026-10-11 used these bounded queries, without date/domain filters or exhaustive pagination:

- `arsenopyrite bioleaching Acidithiobacillus primary study PMC mineral pure passivation`
- `arsenopyrite microbial oxidation Sulfobacillus mineral bioleaching full text`
- `"10.3390/met9121320" correction OR erratum OR retraction`
- `"Formation Process of the Passivating Products" supplement`
- `site.ncbi.nlm.nih.gov/Taxonomy/Browser "Acidithiobacillus ferrooxidans" "920"`
- `"arsenopyrite" "jarosite" "did not" "passivat" bioleaching`
- `"10.3390/met9121320" retracted correction erratum`
- `"arsenopyrite" "jarosite" "did not lead" passivation Sulfobacillus`
- `"10.1016/j.jmrt.2020.05.068"`

Provider results are retained in the raw search receipts. Exact-title/DOI notice queries, the selected publisher PDF/XML and Crossref works metadata revealed no correction or retraction notice in the checked material. Crossref had no `update-to` entry and an empty relation object. This is bounded evidence, not certification that no notice exists anywhere. The MDPI HTML page returned HTTP 429; the legitimate official PDF/XML routes succeeded. The complete selected XML has six figures, two numbered tables plus Appendix A's table, and no supplementary-material element or separate supplement link. The PDF likewise supplies its appendix internally. No unseen supplement is claimed as inspected.

## Selected primary experiment

Liu, Li, Zhang, Yang, Xu and Jiang (2019), *Formation Process of the Passivating Products from Arsenopyrite Bioleaching by Acidithiobacillus ferrooxidans in 9K Culture Medium*, Metals 9(12), 1320, [DOI 10.3390/met9121320](https://doi.org/10.3390/met9121320). Crossref identity agrees with the complete publisher PDF and XML, published 6 December 2019. All 11 PDF pages were read and visually inspected, including Figures 1-6, Tables 1-2 and Appendix A. The primary artifacts identify CC BY 4.0; bulk files remain outside Git.

| Contract | Verified scope and limit |
|---|---|
| Feed | Section 3.1: natural high-purity Yaogangxian, Hunan mineral; XRF Fe1.00As0.99S0.97 with Si 0.132%, Co 0.034%, Ni 0.062%. Particles over 90% below 74 micrometres; separate cubes about 15 × 15 × 5 mm. No gold assay. |
| Organism | Source-assigned A. ferrooxidans, acclimated by subculture with 10 g/L arsenopyrite for three months. Strain accession, isolation provenance and inoculum cell density are not given. Species mapping only. |
| Conditions | 250 mL flasks; 100 mL 9K medium plus 15 mL inoculum; 160 rpm, 30 °C, initial pH 1.8 adjusted with about 3 M sulfuric acid; 10 g/L particle loading. Added inoculum is not silently treated as part of a confirmed 100 mL final volume. |
| Medium | Per litre: 44.8 g FeSO4·7H2O, 3.0 g (NH4)2SO4, 0.50 g K2HPO4·3H2O, 0.1 g KCl, 0.5 g MgSO4·7H2O, 0.01 g Ca(NO3)2·4H2O. Medium-derived Fe is substantial. |
| Controls and replication | Particle time series and separate morphology experiments are reported, with plotted error bars. No explicit replicate count/error-bar definition, matched sterile kinetic series, matched-pH series, selective film-removal test or cell-contact separation assay is supplied. |
| Liquid result | Section 4.1.1/Figure 1a: reported As leaching ratio 30.4% and dissolved total As 1.3 g/L at day 19, then plateau through roughly day 23. ICP-AES measured As/Fe. The paper gives no calculation formula or sampling-volume correction; no independent yield or uncertainty is reconstructed. |
| Iron and growth | Figure 1b-d: early suspended-cell increase, Fe(II) depletion, Fe(III) rise, initial pH increase followed by decline, changing redox potential versus SHE. These support the author's ferric-regeneration interpretation without isolating the microbial increment above abiotic leaching. |
| Residue phases | Figure 2 XRD/Rietveld fitting identifies realgar, orpiment, sulfur and jarosite alongside residual arsenopyrite. Percentages are normalized phase weight fractions of washed residual solids, not absolute mineral destruction or an As balance. |
| Surface morphology | Figures 4-5/Table 1: dense As/S-rich film at 36/120 h, later porous jarosite-like deposits at 8 days. Cube surfaces were polished and cleaned with alternate 5 M HCl, methanol and water baths; post-incubation fixation/rinse/dehydration affects morphology. The source attributes cracks to drying. EDS does not independently identify molecular phases. |
| Interpretation | The source proposes early compact realgar/orpiment/sulfur-rich film inhibition, contrasting with a later porous jarosite layer. The phase attribution combines particle XRD with separate cube EDS/morphology; the inhibition mechanism is not directly isolated. |
| Thermodynamics | Figure 3, Table 2 and Appendix A: predictions/possible reactions at 25 °C, 1 atm; cultures at 30 °C. Authors acknowledge equilibrium prediction disagrees with early residue phases. Not measured reaction fluxes. |
| Outcome and scale | Laboratory arsenic mobilization and secondary-solid formation. No isolated arsenic product, gold-recovery assay, closed As balance or demonstrated industrial deployment. |

## Adversarial questions retained in the record

The text first describes nearly linear early As release as lacking an obvious passivation signal, then infers inhibition from weak response to growing cells/ferric iron. The time-course observation and the causal interpretation remain distinct. No exact constant-rate fit is imported. A later plateau is observed, but it does not uniquely identify a limiting phase or exclude loss of activity.

The As leaching ratio is not total FeAsS destruction: As-bearing secondary phases can retain arsenic. The change in fitted residue percentages is also not a mass balance. The source's reduced realgar notation As2S2 is attributed to the paper, not minted as a mineral identifier. Jarosite's presence alone does not demonstrate that it passivates; the selected study argues its later porous layer is unlikely to be the principal barrier under its conditions.

The IMA row and NCBI entry establish entity mappings only. No unreported bacterial strain or industrial application is inferred. No new schema behavior or tests are necessary for qualified prose observations.

## Other leads and contradictory evidence boundaries

- [DOI 10.3390/biology14050550](https://doi.org/10.3390/biology14050550), 2025 QBS3 study: complete Europe PMC JATS acquired and methods/results screened. It uses a different lower-purity material and A. ferriphilus QBS3. Its abstract/discussion report 79.96% versus results 79.92%; discussion repeats As(III) for the second tolerance value where other sections give As(V), and the initial stress inoculum versus plotted maximum requires checking. Figures and supplement were not fully inspected in this pass, and no values/mechanism from it were curated. The reported high extraction is not pooled with the selected 2019 assay.
- [DOI 10.3389/fmicb.2020.01773](https://doi.org/10.3389/fmicb.2020.01773), HQ0211 mixed-culture study: complete publisher PDF and Europe PMC JATS acquired; identity/methods screened. It uses cut cuboids, a mixed community and different conditions. Figures/supplement were not fully audited, so it is a deferred extension, not a second verified mechanism.
- [DOI 10.1016/j.cej.2023.145845](https://doi.org/10.1016/j.cej.2023.145845), *Effects of Fe and cost-effective media composition on arsenopyrite bioleaching by Sulfobacillus thermosulfidooxidans*: promising medium-comparison lead. The university manuscript route `https://pureportal.coventry.ac.uk/files/100490134/Pakostova2023AAM.pdf` returned HTTP 403 in one bounded attempt; no downloaded full text or verified assay claim is represented. DOI came from discovery metadata and remains to be resolved at the issuing publisher/Crossref before future curation.
- [DOI 10.1016/j.jmrt.2020.05.068](https://doi.org/10.1016/j.jmrt.2020.05.068), pyrite-assisted Sulfobacillus study: publisher abstract identifies mixed-mineral galvanic experiments and reports sulfur/jarosite clusters without passivation. This cautions against a universal phase-based mechanism; full methods/figures/SI were not acquired here and no numerical result is imported into the record. The material and organism differ from the selected assay. Full primary acquisition is the concrete next step for this comparison.
- Referenced prior pyrrhotite downloads also point to older arsenopyrite studies, including PMC201798. Those are unreviewed leads, not additional curated experiments.

## Frozen handoff and checks

Record: `data/records/arsenopyrite.yaml`, SHA-256 `c5964569b34c3bb772113634b0dde144d6f79849a36f076c7d3effb8083ccc4d`.

Canonical CREATE: `history/records/arsenopyrite/2026-10-11T194714Z-codex-d48d52.yaml`, SHA-256 `1f3458e71098d3b12d0375968fcdea2cc896428f410451b6e881186255f78dfd`. The record has a distinct inline event.

`UV_CACHE_DIR=/private/tmp/cmmmech-uv-cache UV_OFFLINE=1 uv run --locked cmmmech validate data/records/arsenopyrite.yaml` completed with exit 0: **1 checked, 0 failed**. Independent review and final cohort gates belong to the parent workflow and were pending at this handoff. No scientific approval is claimed by the curator.

Raw artifacts: `/private/tmp/cmm-round32-arsenopyrite-research/raw`. The adjacent JSON provides exact acquisition receipts, checksums and source/inspection scope. Bulk primary material and figures remain outside Git; maintained files contain the scientific assessment, not republished full texts.
