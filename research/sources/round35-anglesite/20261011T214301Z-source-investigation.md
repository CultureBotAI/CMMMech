# Anglesite source investigation

UTC: 2026-10-11T21:43:01.725065+00:00

Researcher: Codex `/root/round27_eaf_slag` (GPT-6; codex), author of this record and the preceding galena curation. This is a research/curation dossier, not an independent scientific review.

Worktree: `/private/tmp/CMMMech-expansion-round35-20261011`. Branch: `curate/cmm-expansion-round35-20261011`. Trusted base: `f83cf867a38c470b4347f721d9ea9370c3019eaf`. The exact-base successful round34 postmerge baseline is reused through `/private/tmp/cmm-round35-baseline-reuse.json`; no baseline rerun is claimed. Applicable local add-record and discover-sources skills, source guide/template, CLAUDE, README, record documentation, schema, relevant validator/tests and nearby records were read.

## Decision and identity boundary

Create [anglesite](../../../data/records/anglesite.yaml) as a mineral species with a bounded product-phase observation. The [September 2026 IMA original](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF page 11, lists anglesite as Pb(SO4), grandfathered status G, original-description year 1832; pages 1–2 explain the notation and terms. This is distinct from elemental lead, galena, a dissolved ion, a reagent whose phase has not been checked, and a mixed resource. No criticality claim or mineral CURIE is invented.

The complete [Pacholewska 2004 primary](https://www.journalssystem.com/ppmp/Bioleaching-of-galena-flotation-concentrate,79494,0,2.html), *Physicochemical Problems of Mineral Processing* 38:281–290, identifies anglesite in residues of a natural galena-rich concentrate. The same experiment is already represented from the substrate perspective in [galena](../../../data/records/galena.yaml); it is not a second independent replication. Product identity and the chemical-control result make this limited additional mineral owner useful. Existing galena and seafloor-massive-sulfides records remain unchanged.

## Deduplication and acquisition boundaries

Before creating the record, `rg --no-ignore --hidden --follow` searched identity, DOI and study-title variants across `data/records`, `research`, `reviews` and `history` in both this worktree and the original checkout. The exact invocation/output is retained in `dedup-corpus.{json,txt}`. There were 112 matching lines, including existing galena/SMS context; no separate anglesite owner was found within those declared roots. This claim includes ignored/hidden text and followed symlinks, not the entire machine.

Referenced primary-download directories searched were:

- `/private/tmp/cmm-round20-nodule-raw`
- `/private/tmp/cmm-round21-crusts-raw`
- `/private/tmp/cmm-round22-pv-raw`
- `/private/tmp/cmm-round22-sulfides-raw`
- `/private/tmp/cmm-round33-pyrite-research`
- `/private/tmp/cmm-round34-galena-research`
- `/private/tmp/cmm-round34-galena-root-review`

Resolved-directory cycle prevention was used while following links. All 16 encountered PDF paths were text-extracted without error (15 distinct contents, because the IMA copy repeats); the text and all local searchable content were included in the second ignored/hidden/follow search. That search returned 82 lines. Images and other binary archives are not asserted text-searchable. Dependency cache and unrelated prior gate logs were excluded from the primary-download scope. Exact commands, roots, extraction hashes and outputs are in the paired JSON/retained dedup receipts. No previously downloaded full Weijma2002 paper was found within these bounds.

The 10-page Pacholewska PDF was originally obtained from the [official PDF route](https://www.journalssystem.com/ppmp/pdf-79494-15546?filename=Bioleaching+of+galena.pdf) on 2026-10-11 at 21:01:57–21:01:59Z, HTTP 200, 1,682,267 bytes, SHA-256 `9a0a9d6a4df1e2c42cc369aa8e17d7d35c47f2da29b5b0dc674901725eae4925`. This round reuses/rechecks those exact bytes; it does not claim a new PDF download. The current landing page, NCBI species response, Crossref and WUR metadata were newly fetched at 21:37:46–21:37:47Z. `raw/acquisition-1.json` records URLs, actual times, statuses and hashes. IMA's original is also reused: SHA-256 `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973`; prior acquisition/reuse receipts are preserved.

The complete primary text was reread. Original PDF pages 3, 5 and 6 (all three tables and relevant methods), pages 7–9 (all three figures), and IMA pages 1, 2 and 11 were visually inspected this round. All ten Pacholewska pages were visually inspected during the preceding same-day galena work; all ten current renders are retained. There is no claim of a second fresh visual read of every page. No SI was linked in the retained main/landing or found in the bounded exact-title supplement query; this is not universal proof of absence. No DOI was verified for Pacholewska2004.

## Primary observations and adverse interpretations

- **Feed and organism:** approximately 80% galena with hydrocerussite, marcasite, sphalerite, pyrite, gypsum and quartz from ZGH Boleslaw, Poland. Listed approximate phases total about 101%; Table 1 reports 69.3% Pb. Source isolate F3-02 came from ferruginous mineral water at Piwniczna-Lomnica. [NCBI taxon 920](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=920) verifies the current *Acidithiobacillus ferrooxidans* species name, not the isolate identity or a strain accession.
- **Conditions:** modified 2K sulfate medium contained (g/L) (NH4)2SO4 3, KCl 0.1, MgSO4·7H2O 0.5, Ca(NO3)2 0.01, K2HPO4 0.5 and FeSO4·7H2O 9.84. Culture was not lead-adapted. Nominal pH 2 and Fe(II) 2.0 g/L differ from Table 2 initial pH 2.2 and 2.159 g/L. Assays used 300 mL flasks, reported 5% w/v feed, 100 mL solution plus 10 mL culture, 25 °C and 130 rpm; the final-volume basis is unclear. Sampling extended to 384 h. Sterile-labelled controls are present, but sterilization details and biological replicate counts are not given.
- **Phase endpoint:** p. 286 and Figure 1 identify anglesite in both arms at 288 h. Inoculated residue: approximately 40% anglesite, 43% galena; control: approximately 25% anglesite, 62% galena. Other phases remain. These are approximate proportions of different residues with an unspecified phase-quantification procedure and uncertainty. They are neither fractions of initial Pb converted nor absolute product masses or isolated yields. Cu-Kalpha XRD was used on a Philips PW3710 (40 kV, 35 mA); cell dependence and a direct enzymatic crystallization mechanism were not established.
- **Chemical comparator:** Table 2 gives 288 h pH 2.7 versus 3.4, Eh 560.8 versus 286.5 mV against Ag/AgCl, and Fe(II) 0 versus 1.113 g/L (inoculated/control). This is compatible with indirect culture-associated oxidation but does not isolate cell effects at matched solution chemistry. Dissolved Pb is 0.0021 versus 0.0022 g/L at 288 h and 0.0019 versus 0.0021 g/L at 384 h. There is no demonstrated dissolved-lead advantage. Medium sulfate and other feed sulfur minerals prevent assigning product sulfate exclusively to galena oxidation.
- **Operational sulfur ratio:** Table 3 labels 100 × residue sulfate-S/(total-S minus sulfate-S) as sulfur conversion. Its 288 h entries, 47.99% versus 27.25%, are not an initial-feed mass balance. The operational difference term does not independently identify all residual sulfur phases. At 96 h the control's 2.70/16.10 implies approximately 16.77%, whereas 18.05% is printed; at 192 h 2.72/15.07 implies approximately 18.05%, whereas 16.73% is printed. These calculations diagnose source inconsistency, not replacement measurements. No corrected conversion value is adopted. The abstract's twofold characterization is approximate (47.99/27.25 ≈ 1.76); the source's no-further-change wording at 384 h overstates a plateau because its ratio rises to 49.78%.
- **Microscopy and passivation:** Figures 2–3 show coatings and cell-like objects in dried/gold-coated specimens. Morphology does not authenticate F3-02 or identify every coating chemically. Anglesite/possible sulfur passivation is the author's interpretation; film permeability and a separately varied causal coating effect were not measured. It is not asserted for all media. The synthetic-PbS arm develops pH about 5–5.4, retains Fe(II) (0.555 g/L at 384 h), lacks observed colonies and has a reported chemical PbSO4 coating; it is not a matched low-pH null for the natural concentrate.

## Reduction lead and unresolved evidence

[Weijma et al., DOI 10.1021/bp025523k](https://doi.org/10.1021/bp025523k), *Biotechnology Progress* 18(4):770–775 (2002), is verified by Crossref, WUR and publisher metadata. PMID 12153311 agrees with the 2002 issue; the later Wiley platform date 2008-09-05 is not the experiment's publication year. WUR exposed a DOI access link and abstract, not a complete manuscript. The DOI/ACS web routes failed, and official Wiley landing/PDF acquisition returned HTTP 403; its web-readable landing supplied metadata/abstract only. These bounded failures are preserved. No access restriction was bypassed and identical failures were not retried.

The 2002 paper is **deferred**, with no abstract-derived measurements, organism assignment, kinetics, product yield or industrial claim copied into the record. Complete methods, feed phase/origin, community identity, controls, figures and any SI are required. The related [2008 sulfate-reduction article](https://www.sciencedirect.com/science/article/abs/pii/S0304386X08001990) is also discovery-only; no DOI is guessed and no abstract quantities are accepted.

Further context is explicitly not accepted mechanism evidence: the existing Saito2015 SMS study (DOI 10.2473/journalofmmij.131.627) needs a separately scoped product reassessment; the [UNESP Garcia1997 repository route](https://repositorio.unesp.br/entities/publication/ce145ca6-c12f-4787-a9dc-ab4ddd9900ff) exposed search metadata but timed out on open; and a [BGI2010 report](https://www.bgi.uni-bayreuth.de/includes/download.php?file=%2Fresearch%2Fannual_report%2F2010%2FBGI+Annual+Report+2010.pdf) search excerpt is a possible passivation counterexample, not an inspected original here. No quantitative results from these leads are adopted.

## Search and notice log

Provider: `web.run`, 2026-10-11, returned first result sets; no exhaustive pagination. Exact queries:

- `"10.1021/bp025523k" full text`
- `"Biological conversion of anglesite" lead sulfate Weijma`
- `"bp025523k" pdf Weijma`
- `"Biological Conversion of Anglesite" filetype:pdf`
- `"Bioleaching of galena flotation concentrate" correction erratum retraction`
- `"Anglesite" "IMA" PbSO4 mineral`
- `"bp025523k" "pdf" site:edepot.wur.nl`
- `"bp025523k" correction retraction erratum`
- `"Bioleaching of galena flotation concentrate" "supplement"`
- `"Pacholewska" "2004" "galena" correction erratum retraction`
- `"anglesite" "galena" "abiotic" bacteria passivation`

No relevant correction, erratum or retraction was identified in these bounded results or fresh publisher metadata. This is not a universal notice-absence claim. Accessed abstracts were used to route acquisition and identify gaps, not to establish curated experimental quantities. Raw primary artifacts remain outside Git; no article redistribution license is inferred. IMA page 2 states CC BY-SA 3.0.

## Curation and validation handoff

- Record: [anglesite.yaml](../../../data/records/anglesite.yaml), SHA-256 `5bc650c2efb91ffc664d20a8c3b6967b88e7959ebcc0cd6a19837f201d5d2303`.
- Canonical CREATE: [history sidecar](../../../history/records/anglesite/2026-10-11T213956Z-codex-692a3f.yaml), SHA-256 `f414af073b328ccad402913af7009e28612bcc28144b7dc8ffd9bad172f92c7e`. Helper event at 21:39:56Z; separate inline CREATE at 21:41:35Z, actor codex/GPT-6/codex.
- Named validation completed with exit 0: `Checked 1 record(s); 0 failed.` Log: `/private/tmp/cmm-round35-anglesite-research/named-validation.log`, SHA-256 `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`.
- Independent exact-state scientific review and final cohort gates remain parent-owned and pending at this save. This dossier does not approve its author's own record.
- [Paired JSON](20261011T214301Z-source-investigation.json) pins source URLs, receipt details, bounded search/dedup and every retained evidence/receipt hash. Raw storage: `/private/tmp/cmm-round35-anglesite-research`.

Next priorities are an independent review of this narrow product record and lawful acquisition of complete reduction studies before any recovery claim or second mechanism is considered. No schema, validator, test, criticality or existing-record amendment was required.
