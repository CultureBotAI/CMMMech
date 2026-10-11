# Round27 steel-slag source investigation and BOF extension

## Scope and provenance

UTC: 2026-10-11T16:15:48.133747+00:00. Researcher: Codex (GPT-6), `round27_eaf_slag`.
Base: `3f1350b24b4f6248ed2e17caade936c15af9be93`; branch `curate/cmm-expansion-round27-20261011` in `/private/tmp/CMMMech-expansion-round27-20261011`.

The assigned starting lead was EAF steel slag, DOI [10.1016/j.chemosphere.2014.09.089](https://doi.org/10.1016/j.chemosphere.2014.09.089). Its unavailable original figures keep that mechanism deferred. Following its references and related steel-slag experiments identified a complete open BOF study suitable for extending the existing record. The selection favors original methods, directly inspected figures, explicit controls and an unambiguous process-defined feed. BOF slag, EAF slag, EAF dust, ferroalloy dust and aluminium-anodizing sludge remain different resources; none inherits elemental criticality. This is a bounded investigation, not a claim that the frontier is exhausted.

Read the applicable user instructions, CLAUDE, README, record guide, native schema/validator and relevant tests, the add-record/discovery/review skills, prior round24/26 reports, and the current BOF/EAF-dust records. A `rg --no-ignore --hidden --follow` search covered the entire original checkout and the three referenced raw directories listed in the paired JSON; ignored and hidden files were included. Sixteen matching paths were retained in the outside-Git search manifest. The 2022 BOF DOI was present in prior downloaded references but had no curated claim in the baseline BOF record. No unrelated home or temporary trees were searched. An initially guessed old raw-directory name did not exist; the actual paths recorded by earlier dossiers were then used. The final search covered those resolved directories.

The parent's baseline completed with 308 passed and 3 skipped before scientific-record writes were authorized. This report is source assessment and curation provenance, not the independent scientific acceptance review.

## Search and acquisition log

All live searches were on 2026-10-11 UTC through `web.run`; first returned sets only, no date filters or pagination. The paired JSON lists every exact query, including low-specificity queries that returned unrelated DOI suffixes. Those unrelated sources were excluded. Direct public downloads used a temporary directory and preserved URL, UTC acquisition time, response type/status, size and SHA-256. No author messages, payments, credentials or access-control bypasses were used.

| Route | Inspected result | Access limit |
|---|---|---|
| Exact EAF DOI/title; publisher, PubMed, Crossref, OpenAlex | Bibliography/abstract; public indexed article transcription | Original PDF/figures unavailable; Elsevier TDM HTTP 200 was metadata only; Doczz viewer PDF HTTP 500 |
| Solisio 2002 exact title/PII/DOI; author institutional IRIS | Primary abstract identifies two distinct wastes; institutional page 11697/17964 says no files | No methods, figures or source tables acquired; TDM metadata only |
| EAF microbial-carbonation title/DOI; DTU | Author abstract and metadata for Su, Jin and Zhan 2023 | No original experimental article acquired |
| BOF 2022 title/DOI; K1-MET institution mirror | Complete 12-page publisher PDF, all methods, five figures, two tables and equation | ESI not acquired; publisher main/s1/update routes inaccessible |
| DSMZ 504/583 catalogues | Direct collection labels | Does not authenticate study cultures; DSM 583 name differs from paper |
| Exact-title/DOI correction/retraction searches; Crossref; publisher update | No matching notice identified in returned exact-study results; Crossref relation empty | Bounded coverage and inaccessible update page prevent an up-to-date certificate |

## Curated handoff awaiting independent review: a distinct experiment on existing BOF slag

[Kremser et al. 2022, Processes 10:576](https://doi.org/10.3390/pr10030576), published 15 March 2022, supplies the newly assessed experiment. The [K1-MET PDF](https://www.k1-met.com/fileadmin/user_upload/Publications/Journal_articles_open_access/Kremser_et_al._2022__BOF_slag_bioleaching.pdf) is a 12-page publisher version with an embedded version 2 update link and printed CC BY 4.0 license. Its SHA-256 is `ec418401549a081e8771f54a94fbb715b96efa71981b83b7cadf285c432a5ba1`. This round freshly downloaded the artifact; it is not a claim that the institution mirrored the latest publisher state. Full text and all relevant rendered pages 3–9 were inspected. Data-availability wording mentions ESI or author request, but a corresponding supporting-data artifact was not obtained. Public peer-review comments were inspected only as additional context, not substituted for independent review or source evidence.

The new feed came from an unnamed Austrian steelmaking company. Drying at 22°C, crushing and a 0.25–0.5 mm fraction precede the assays. The 2018 UK feed and its two mechanisms remain separate and unchanged. Table 1's mg/g concentrations characterize this specific digested feed; no composition or criticality is inherited into every BOF slag.

Methods 2.2–2.3 use living sulfur-oxidizing DSM 504 and a culture called ferridurans DSM 583. Duplicate 100 mL flasks used 14 days, 30°C and 150 rpm, 10% inoculum and 10 g/L slag. The cultures have distinct media and starting acidity, and their uninoculated controls have different final pH. Figure 3 supports conditional dissolution while retaining negligible Al in DSM 504 and V near the DSM 583 abiotic control. This does not isolate species, gene or ferric-iron causality.

Methods 2.4/Figures 1 and 4 describe laboratory 1.5 L reactors, four two-week loading cycles and replacement of two-thirds of the suspension. Remaining liquid and solids prevent treating each nominal loading as an independent clean-start experiment. Independent replicate reactors are not specified. The chemical comparator is acid-dosed water, not a matched medium. Table 2 expresses consumption using an 18 M acid volume basis while Methods describes 2 M dosing; conversion details are unavailable. High-loading DSM 504 requires more external acid than its comparator; the paper acknowledges this contribution. Higher-loading DSM 583 V extraction falls below the chemical control. Figure 4 bars also fail to sustain the prose's blanket Al>80%/Mn>50% statement. No repaired yields, digitized exact bars or complete process balance are inferred.

The displayed equation subtracts medium and inoculum contributions, but the raw inputs, dilution/sampling corrections and retained-cycle accounting are unavailable. Inspection verifies the printed equation, not every underlying calculation. No native concentration observations were added: the table uses mg/g and lacks analysis dates, and yields/removal percentages fall outside that contract.

Methods 2.7–2.8/Figure 5 use synthetic SMS-AT/SMS-AF, prepared with different metal amounts, Fe oxidation states and counterions. NaOH treatment of these 25 mL solutions, 500 rpm, 45 hours, followed by 0.2 µm filtration and ICP-MS, supports a separate nonmicrobial differential depletion assay. The experiment did not apply this step to actual BOF bioleachate. Mixed precipitates, product mass and purity were not established. The abstract/conclusion's broader recovery wording cannot turn these surrogate assays into an integrated slag-to-product yield or industrial process.

DSMZ currently names [DSM 504](https://www.dsmz.de/collection/catalogue/details/culture/DSM-504) as thiooxidans and [DSM 583](https://www.dsmz.de/collection/catalogue/details/culture/DSM-583) as ferrooxidans. The paper cites a genomic revision for ferridurans; [BacDive strain 111](https://bacdive.dsmz.de/strain/111) presents a mixture of catalogue and genome labels. No definitive species CURIE is assigned to the conflicting stock, and no accession is treated as experimental authentication.

## Deferred EAF source and a citation-identity correction

Hocheng, Su and Jadhav 2014, Chemosphere 117:652–657, is verified at DOI [10.1016/j.chemosphere.2014.09.089](https://doi.org/10.1016/j.chemosphere.2014.09.089) and [PubMed 25461931](https://pubmed.ncbi.nlm.nih.gov/25461931/). The [public indexed transcription](https://doczz.net/doc/8164782/bioleaching-of-metals-from-steel-slag-by-acidithiobacillus) exposes methods and results beyond the earlier abstract-only assessment. It describes washed EAF slag, separate culture supernatants, externally acid-adjusted ferrooxidans treatment and serial cycles, including Ni/Mo non-improvement. Those observations identify what a later original-figure audit must test; exact measurements are not imported from the transcription. The six figure images, original Table 1 layout, replication and cited prior supernatant preparation method remain unverified. Doczz redistribution authority is unknown; no transcription/full text is committed.

The 2014 introduction and some later reviews summarize Solisio 2002 as leaching Zn/Al from EAF sludge/slag. The [original Solisio abstract](https://pubmed.ncbi.nlm.nih.gov/12214978/) instead distinguishes **dust from iron-manganese-alloy production in an electric furnace** from **sludge from aluminium anodic-oxidation treatment**. DOI [10.1016/S0956-053X(01)00052-6](https://doi.org/10.1016/S0956-053X(01)00052-6) therefore identifies a promising two-feed study, not proof of an EAF steel-slag assay. Its [author-institution record](https://ricerca.univaq.it/handle/11697/17964) explicitly has no associated files. Publisher and metadata routes did not yield a full article; ResearchGate offers a request only. Both resource identities remain research leads until full methods, stock, controls, units and kinetics are acquired. They are not silently folded into the steelmaking EAF-dust record.

[Su, Jin and Zhan 2023](https://doi.org/10.1080/21650373.2022.2153283), on microbial carbonation of EAF-slag bricks, is another primary lead verified through [DTU metadata/abstract](https://orbit.dtu.dk/en/publications/improvement-in-mechanical-properties-and-microstructure-of-electr/). Its full evidence is unassessed; material transformation, enzyme attribution, abiotic carbonation, leach-test controls and product phase remain prerequisites. A manufactured brick formulation is not automatically a new root apart from its source material.

## Priorities and local artifacts

1. Independently review the changed [BOF record](../../../data/records/basic-oxygen-furnace-steel-slag.yaml), including preserved 2018 evidence and final hashes. The addendum retains the 2022 source's limitations, rather than hiding them behind overall performance claims.
2. Obtain Solisio 2002 full primary to assess two candidate new secondary resources.
3. Obtain the original EAF 2014 figures/Table 1 and referenced supernatant protocol; then reassess EAF slag curation.
4. Obtain EAF 2023 carbonation methods/figures and BOF 2022 ESI, reactor accounting and strain evidence. These are different next actions, not a declaration that no more sources exist.

Canonical EDIT history: `history/records/basic-oxygen-furnace-steel-slag/2026-10-11T161312Z-codex-27b6e0.yaml`. Inline EDIT is a separate current event. Named validation completed with `Checked 1 record(s); 0 failed`, exit 0. Final batch gates and independent scientific review are the parent's next steps; this source assessment does not claim those have completed. No schema/validator/governance files or earlier immutable history/reviews were changed.

All retained primary files, rendered pages, extraction text and acquisition logs remain outside Git in `/private/tmp/cmm-round27-eaf-slag-raw`. The paired JSON contains the exact manifest and checksums. Third-party source terms remain controlling; only project-authored assessment and evidence paraphrases are committed. The search/defer decisions are bounded and do not establish exhaustion of CMM identities or literature.
