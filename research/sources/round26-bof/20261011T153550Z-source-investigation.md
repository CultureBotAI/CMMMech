# Round26 BOF steel-slag source investigation

UTC: 2026-10-11T15:35:50.368557+00:00. Trusted base: `d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9`.
Worktree: `/private/tmp/CMMMech-expansion-round26-20261011`.
Acceptance issue: [93](https://github.com/CultureBotAI/CMMMech/issues/93).

## Scope and selection

The BOF slag study provides an actual process-defined feed, full methods, culture and cell-free arms, fresh-medium controls, main figures and supplementary community/XRD evidence. It is suitable for a narrowly qualified laboratory record. Pickling sludge and brake-pad leads remain deferred because full primary experimental evidence was not acquired. EAF slag remains distinct from EAF dust and BOF slag. This assessment does not establish exhaustion of CMM identities or literature.

## Search and identity

Hidden and ignored files were included with `rg --no-ignore --hidden -L` across records, histories, reviews and research, plus the referenced round25 button/frontier raw directories and current root downloads. Exact DOI/BOF searches found no pre-existing repository record; one prior aggregate raw search contains a broad BOF mention. These bounded searches do not claim machine-wide novelty. The paired JSON preserves actual query strings, acquisition status, source hashes and raw paths.

## Primary evidence and access

[Gomes et al. 2018](https://doi.org/10.1016/j.jenvman.2018.05.056), Journal of Environmental Management 222:30-36, was read in full from the [Northumbria-hosted published PDF](https://researchportal.northumbria.ac.uk/ws/portalfiles/portal/33037200/1_s2.0_S0301479718305875_main.pdf). All main tables and figures were visually inspected. The public [publisher supplement](https://ars.els-cdn.com/content/image/1-s2.0-S0301479718305875-mmc1.docx) matches title/authors; its XML text/table and both embedded XRD images were inspected. An attempted LibreOffice PDF conversion failed, so no successful full-page supplement render is claimed. The complete original DOCX remains available locally. Main PDF SHA256 `e17a1a49ad53c878924bd967847f2823af3126ef59bcb6b9e45d1e078c22a40b`; DOCX SHA256 `0259b69187a29d2ca45796689ca3a4e1c5ffeea0d357ff24dffca1621ac24659`.

Crossref confirms DOI/title/authors and the main article's CC BY 4.0 version-of-record license. The printed online date is 23 May 2018; the September issue and metadata license-start dates are not silently substituted. Raw documents remain outside Git. A separate supplement license was not established.

## Findings retained in curation

- **Methods 2.1-2.4; Supplement Table S1:** Unresolved natural mixed community; preliminary T-RFLP assigned species and blank peak fields do not authenticate strains or isolate causal members. Reagent H2SO4 during conditioning and adaptation prevents treating all acidity as biologically generated.
- **Methods 2.4 and Figure 3a:** A/B initially below pH 1 and fresh-medium control at higher pH; independent column replication unspecified. Non-significant A versus B does not demonstrate equivalence; acid-matched causality is unavailable.
- **Table 1, Methods 2.3, Figures 1-2:** The stated 1 g/100 mL loading and feed Al 0.4 wt%, Cr 100 mg/kg, V 40 mg/kg do not reproduce the reported concentration/percentage pairings. Approximate figure readings illustrate conflict, not digitized source observations. No curator-corrected yield.
- **Table 1 and Figure 3b-d; Results 3.3:** Text Al 95/109%, Cr 84/64% and V 8/8% are A/B source-reported extractions, not validated yields. Table 1 inventory and Figure 3 cumulative Cr/V disagree. Nonzero day-zero pools, sampling corrections and total-feed digestion completeness are unresolved. Abstract Al 100% is not a substitute for 109%.
- **Table 1 and Results 3.1:** Mg 29.4 wt% cannot fall inside the cited typical 0.3-2.4% range as the prose claims; retain source-defined BOF identity without asserting typical chemistry.
- **Methods 2.1/2.4:** The coarse size is printed as 4 < size > 10 mm, not a valid bounded interval. No silent reversal.
- **Table 2; Results 3.3; Supplement Figures S1-S2:** Kinetic fits cannot distinguish reactive-core versus secondary-crust diffusion. XRD supports mixed gypsum/jarosite assignments, not pure saleable products or exclusively microbial precipitation. Modeled oxidation states are not direct speciation.
- **Methods 2.5 and Results 3.4:** Resin removal and NaOH elution are separate chemical stages. Al removal B 13% exceeds A 9%, contrary to generic A-best prose. Error definitions/elution denominators and particles >22 micrometres versus 0.22-micrometre filtration remain unresolved; no full-process yield.

The accepted claim is conditional aqueous mobilization by culture-conditioned liquid. Initial acidity and medium history differ; no unique taxon, gene or living-cell advantage is isolated. The mixed XRD products and fitted diffusion models are not purified recovery products. Resin removal and poor alkaline elution are separate chemical steps.

## Notice and contradictory-evidence coverage

Exact DOI with correction/retraction/erratum and title with contradictory leaching/recovery were searched. No matching notice appeared in the bounded returned sets. Crossref has an empty relation and no update-to entry, but the Crossmark inner frame was unavailable. This is not certification of publication status or an exhaustive absence claim. Primary comparator leads at PMC8003827 and PMC11219386 concern different feeds/chemical or environmental conditions; only search/abstract context was checked and no numerical comparison was imported.

## Deferred ingest handoff

- **Stainless-steel pickling sludge** ([10.1016/j.chemosphere.2022.134213](https://pubmed.ncbi.nlm.nih.gov/35283154/)): Crossref, PubMed primary abstract and indexed publisher preview; direct publisher 403. Public Elsevier TDM HTTP 200 contains metadata rather than full experimental text. OpenAlex metadata alone does not verify methods or a clean publication status. Next: Acquire primary methods, mineral and bacterial identity, figures, controls and quantitative definitions. MICP immobilization is not extraction; separate lysate and intact-cell arms.
- **Brake-pad manufacturing residues** ([10.1016/j.wasman.2019.02.047](https://pubmed.ncbi.nlm.nih.gov/31109564/)): Crossref, primary PubMed abstract/publisher preview; direct ScienceDirect full route 403. Source thermal/bioleaching results remain abstract-level only. Next: Acquire full pretreatment and feed identity, culture and calculation details; distinguish pre-consumer powder from spent friction pads. An unrelated aggregator retraction label was not corroborated by a publisher notice in bounded searches and is not accepted as status evidence.
- **Encapsulated-bacteria brake-pad residue bioleaching** ([10.1016/j.mineng.2016.11.010](https://doi.org/10.1016/j.mineng.2016.11.010)): Publisher preview, Crossref and author-institution bibliography. Public TDM HTTP 200 returns metadata only; no full article acquired. Next: Obtain full Vermeulen and Nicolay 2017 primary, verify DSM stocks and compare encapsulated/planktonic runs without importing an ambiguous 150% enhancement claim.
- **Steel-slag microbial carbonate modification** ([10.1016/j.jes.2020.08.023](https://pubmed.ncbi.nlm.nih.gov/33334523/)): Primary title/abstract and citations in a public 2025 review; slag route remains unresolved. Next: Acquire full primary; resolve BOF/EAF feed, treatment controls and MICP/mineral evidence before selecting a new root or extending BOF.
- **Steel-slag MICP mechanical/sulfate follow-up** ([10.1016/j.jclepro.2023.136982](https://doi.org/10.1016/j.jclepro.2023.136982)): Indexed primary title/abstract only. Next: Acquire full primary and resolve process-defined feed identity and relevant mineral transformation.
- **EAF slag culture-supernatant leaching** ([10.1016/j.chemosphere.2014.09.089](https://doi.org/10.1016/j.chemosphere.2014.09.089)): Cited in full BOF primary and earlier frontier; distinct from EAF dust. Next: Acquire and independently audit full primary before importing methods or creating an EAF-slag root.

A public 2025 steel-slag mineral-carbonation review was used only for citation discovery, with selected sections checked; it is not primary evidence for this record. No author was contacted and no restricted access was bypassed.

## Curation and review handoff

Record: `data/records/basic-oxygen-furnace-steel-slag.yaml`, SHA256 `6917cd8d71f3fad7cc25c0717e956c5d4fcf3ae6135765774f951ebdb50afb5c`. CREATE history: `history/records/basic-oxygen-furnace-steel-slag/2026-10-11T153415Z-codex-f742c3.yaml`. Named validation completed with exit 0 (one record, no failures). Independent scientific review and final batch/history/review gates follow; this author dossier is not scientific acceptance. No schema or validator change is needed.
