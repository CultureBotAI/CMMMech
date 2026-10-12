# Oil-sands froth-treatment-tailings source investigation

UTC: 2026-10-12T07:42:05Z

Author: codex (GPT-6; codex), `/root/round27_packaging`. This is the curator's evidence handoff, awaiting independent review.

Trusted base: `98e787e8d61593797aef1ed29840b2315a0cc6e5`. Worktree: `/private/tmp/CMMMech-expansion-round50-20261012`.

## Material and accepted scope

[data/records/oil-sands-froth-treatment-tailings.yaml](../../../data/records/oil-sands-froth-treatment-tailings.yaml) is one `secondary_resource` owner for naphtha-process froth-treatment residue, represented by Plant 6 at the Mildred Lake Settling Basin. It is distinct from Ti/Zr mineral species, elemental commodities, underlying straight coarse tailings, fluid fine tailings and petroleum coke. No criticality, reserve, deployment or isolated metal yield is inferred. Frozen SHA-256: `0a7ce5b2525c4e3e5a4250d048262ecb4511bc1b7098e8d27241cf081c4d5fed`.

Canonical CREATE: [history/records/oil-sands-froth-treatment-tailings/2026-10-12T074034Z-codex-b65c8b.yaml](../../../history/records/oil-sands-froth-treatment-tailings/2026-10-12T074034Z-codex-b65c8b.yaml), SHA-256 `93b96ee1dfe220869ced5686487223e6924a77c983038aa3f6c7bb2b335030b4`; a separate actual-time inline event is attached. Named validation passed one record with zero failures. Initial draft validation found unsupported `doi` keys; those were removed before freeze while verified DOI URLs remained. No schema change was needed.

## Primary evidence and access

- [Ferry et al. 2025](https://doi.org/10.1186/s12932-025-00106-1): complete 18-page publisher PDF reused byte-for-byte from round49; its complete text, Figures1–6 and Tables1–2 now inspected. Original linked DOCX supplement was newly downloaded; Methods, TableS1 and all eight original figures inspected. This completes the earlier handoff's outstanding graphical/SI work.
- [Lindsay et al. 2019](https://doi.org/10.1016/j.apgeochem.2019.02.001): complete 39-page accepted manuscript newly acquired from the official University of Saskatchewan repository; six original figures and Table1 inspected. Repository MD5 matched local bytes. Original publisher DOCX supplement newly acquired and both tables/all five images inspected. Accepted-manuscript status is retained; this is not a claimed publisher typeset PDF.
- [Balaberda et al. 2026](https://doi.org/10.1016/j.chemosphere.2025.144800): complete 13-page article reused from round49 and its repository MD5 independently matched. The issue year2026 and online date12December2025 are distinct source dates. All seven original figures and graphical abstract inspected. Newly acquired original DOCX includes TextsS1–S2, TablesS1–S6 and nine original figures, all assessed. Official NCBI efetch verifies [PRJNA1363209](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1363209); reads were not reanalyzed.

DOCX tables and text were read from original XML cells and original embedded graphics were extracted unchanged for visual inspection. LibreOffice whole-document conversion exited134; no successful converted-layout inspection is claimed. The original TIFF figure was rasterized solely for display. All source files and extraction provenance remain outsideGit under `/private/tmp/cmm-round50-ftt-research`. Fresh acquisition receipts and prior-round reuse are separate in the paired JSON. ScienceDirect denials and unsuccessful guessed extensions are recorded; no restricted access was bypassed.

## Assays, controls and quantitative boundaries

Ferry's six columns represent three weathering states, each washed/unwashed, with one column per condition. The reported treatment is 0.05M sulfuric acid, pH approximately1.5, about0.33PV/day, after DI-water saturation. Column dimensions are10cm by6cm internal diameter. Endpoints differ in throughput (75.0–117.8PV); no common duration, independently replicated columns or inoculated/sterile comparison is reported. Major-element and trace-element filtration used0.45 and0.2micrometer membranes. Cumulative release is normalized to solid mass, not initial recoverable metal or isolated products. The mechanism is `microbial: false` to describe chemical treatment, without asserting sterile environmental material.

Lindsay supports processing origin, mineral mixtures and potential acid generation. Its solvent-washed specimens and static mineralogical/chemical measurements do not establish microbial extraction. Balaberda is a separate field survey:119community samples,80chemistry,48mineralogy,36combined correlations, without interval replicates. Relative16S abundances and inferred ecological roles remain `context_only`; they do not demonstrate active sulfate reduction, methane production or metal recovery. No strain accession is fabricated from environmental taxonomic labels.

Common site and shared authors do not make these three papers independent replications of one assay. Their samples and questions are not pooled into one grade, yield or time course.

## Preserved conflicts and counterevidence

### ferry2025

- Reported influent 0.05 M H2SO4 and approximately pH 1.5 retained without recalculating either value.
- Six conditions are not six replicated columns; throughput differs (117.8,110.0,99.3,85.6,77.9,75.0 PV). Table S1 pore-volume column lacks a printed unit; no unit invented.
- Results page 5 assigns early Ni/Co maxima to non-/partially weathered columns, whereas Figure 3 high early Co pulse is in highly weathered material. No treatment-specific 2250 micrograms/L Co maximum adopted.
- As cumulative release in Figure S7 is greater in unwashed NW/PW, a retained exception to the broad washing-enhances-release interpretation.
- NP-1 and NP-2 are higher after washing, but Table 2 ABA-derived NP-3 decreases (15 to10;13 to12). These different methods are not interchangeable.
- Bitumen absence in washed splits is assumed. No biological control, replicated column error estimates or isolated product yield.
- XRD weight percentages are relative phase abundances; modeled saturation indices do not identify every hypothesized phase. Al hydroxides explicitly not detected by XRD.
- Main discussion describes less than1wt% phyllosilicates in some samples despite larger summed Table1 phase values; no quantitative phyllosilicate generalization adopted.

### lindsay2019

- Methods pipeline samples date2013/2016, Results and SI TableS1 label2015 fresh samples, FigureS4 caption2013. No unified fresh-sample date imposed.
- Abstract sulfide/carbonate means differ from Results. No unified grade imported.
- SI TableS1a is headed quantitative XRD but lists elemental chemistry. K/P/Mn means and some medians/ranges have inconsistent scales. The Zr row says zircon, although symbolZr denotes element.
- FigureS5 caption says dV50, but original axes label dV10. Main particle-size prose gives micrometer mean but millimeter upper range. No size statistic adopted.
- Zr above the analytical limit in10/18samples was estimated from XRD for statistical analysis. Monazite/xenotime hosts are inferred from correlations, not directly established new mineral owners.
- Pyrite EPMA omits below-detection values from Figure5; apparent textures and associations are not an observed microbial formation experiment.

### balaberda2026

- Unbalanced 119-community/80-geochemistry/48-mineralogy coverage;36complete combined-correlation observations, without independent interval replicates.
- Supplement TextS1 explicitly treats unmeasured naphtha samples as non-detects, then substitutes half detection limits. These are not measured zeros or verified absences.
- Main/Texts/Tables differ in TypeII/III ANOVA labels; TextS2 says Tukey while FigureS4 caption says Sidak. No unqualified inferential p-value adopted.
- Significant group-dispersion differences and first two microbial ordination axes totaling8.9% constrain interpretation.
- Genus plots include highest-resolved higher-rank annotations;16S abundances do not authenticate isolates or prove their metabolic function.
- Source language about active sulfur cycling exceeds direct16S evidence; final discussion calls for functional genes/transcripts/flux verification. Methane not measured.

## Deduplication and notice search

The exact dedup receipt searches `data/records`, `research`, `reviews` and `history` in both current worktree and original checkout, with `rg --no-ignore --hidden --follow`. It inspected3874textual metadata files to resolve bounded cited raw directories, then searched181existing referenced roots. Nine referenced roots were unavailable and are listed in the JSON; text-bearing extensions were searched, not semantic contents of every unextracted binary. No existing FTT owner was found within these stated bounds. Source hits were earlier frontier/handoff/acquisition references, not an existing curated experiment. This is not a machine-wide absence claim.

Fresh DOI/title and correction/retraction queries returned no applicable notice in the bounded first result sets inspected. Exact queries/responses and failed routes are retained. The source's stronger ecological language is counterbalanced by its explicit functional-validation gap; no abstract-only mechanism is accepted.

## Validation, rights and review handoff

Named validation: exit0,1checked/0failed, receipt `/private/tmp/cmm-round50-ftt-research/named-validation.json`. Initial baseline is the disclosed reuse of the exact unchanged fresh-main gate in `/private/tmp/cmm-round50-initialization.json`; parent final cohort gates and independent review remain separate.

The raw manifest pins148files with size/SHA-256 at `/private/tmp/cmm-round50-ftt-research/raw-manifest.json`. The paired JSON includes every hash, URL/access timestamp available, bounded search scope and local target/history hashes. Ferry and Balaberda state CC BY-NC-ND4.0; no broader rights are inferred for Lindsay. Originals and graphics remain outsideGit, with factual summaries and locators maintained here.

Ready for root's independent scientific review of the frozen resource; this handoff is not self-approval. Further microbial experiments, broad resource valuation and sequence reanalysis are outside this bounded addition.
