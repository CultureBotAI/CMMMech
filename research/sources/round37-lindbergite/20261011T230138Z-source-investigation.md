# Lindbergite source investigation

UTC: 2026-10-11T23:01:38.260866+00:00
Researcher: Codex /root/round27_eaf_slag; GPT-6; codex.
Worktree: `/private/tmp/CMMMech-expansion-round37-20261011`; trusted base `dcfbedb78bfd682ad06f2ff4517241f490e4f401`.

## Decision and maintained scope

Added [lindbergite](../../../data/records/lindbergite.yaml), SHA-256 `55f488f8f6fd8da4a7f7c63183b93d23540c6e7d19ec20424950f6afa87ac2ba`, with [CREATE history](../../../history/records/lindbergite/2026-10-11T225957Z-codex-f222f6.yaml), SHA-256 `c76f5fc967279b20ae35314f2c2f535a1f29ec459f93df64a55252f1bfd5cb0b`. Independent scientific review and final cohort gates are pending. This document is the curator's investigation, not a self-approval. The paired [JSON dossier](20261011T230138Z-source-investigation.json) preserves all 88 retained raw/derived artifact hashes, individual retrieval URLs/times, exact search queries, deduplication boundaries and validation receipts.

The accepted evidence is Ferrier et al. (2019), [DOI 10.1111/1462-2920.14591](https://doi.org/10.1111/1462-2920.14591): source-assigned lindbergite formation during *Aspergillus niger* ATCC 1015 culture with mixed natural manganese nodule powder. Its solid and liquid arms are one study. This supports a narrow mineral-formation association, without a measured lindbergite yield, complete manganese recovery or industrial deployment. No criticality is inherited from manganese.

## Identity and authority

The fresh [September 2026 IMA list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), original PDF page 126, identifies lindbergite as approved IMA 2003-029, Mn(C2O4)(H2O)2. The [MSA Handbook entry](https://www.handbookofmineralogy.org/pdfs/Lindbergite.pdf) specifies monoclinic C2/c; its complete one-page original was read and visually inspected. Formula alone cannot identify every manganese oxalate dihydrate polymorph. Falottaite, IMA 2013-044, is the distinct trihydrate on list page 67. IMA pages 1-2 were inspected for definitions and terms.

[NCBI 5061](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/5061/dataset_report) verifies the species *A. niger*. The live [ATCC 1015 catalogue](https://www.atcc.org/products/1015) verifies the strain designation, without independently authenticating the culture in the experiment. The species TaxID is not a strain identifier. No unverified external mineral identifier is asserted.

## Primary access and inspected media

Ferrier's complete publisher-version PDF was acquired legitimately from the [University of Dundee repository](https://discovery.dundee.ac.uk/ws/files/32735632/Final_Published_Version.pdf), with [Europe PMC JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6849720/fullTextXML). All 13 PDF pages, including one repository cover and 12 article pages, were visually inspected: all eight original figures and Table 1, complete methods, results and discussion. The cover labels publisher version/CC BY, but the embedded article has early pagination 1-12; Crossref/JATS verify the final 21(5):1821-1832 citation. An exact online publication day is not asserted.

Farkas et al. (2020), [DOI 10.3390/jof6040270](https://doi.org/10.3390/jof6040270), was acquired as the [original MDPI PDF](https://mdpi-res.com/d_attachment/jof/jof-06-00270/article_deploy/jof-06-00270.pdf) and [complete JATS](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7711977/fullTextXML). All 12 PDF pages, eight original figures and both tables were inspected. Each Europe PMC media archive contains eight main JPEGs and eight GIF thumbnails, not independent supplementary experiments. Neither full JATS declares supplementary-material nodes; no separate SI was identified in those artifacts, complete PDFs or the bounded search. This is an explicit search boundary, not a global absence claim.

Raw originals, receipt JSON, extracted text, original figure media and rendered pages remain under `/private/tmp/cmm-round37-lindbergite-research/raw`. The original Atencio 2004 description route on RRUFF failed with connection refused; that paper was not read. The authoritative handbook supplies the crystal-identity boundary. The 2022 [synthetic polymorph study](https://doi.org/10.3390/ijms232314734) was acquired as full JATS and its identity passages read, but its complete figures/SI were not reviewed and no biological mechanism is accepted from it.

## Accepted experiment and limitations

Ferrier's COG_MN35 powder is a mixed natural Clarion-Clipperton Zone nodule, not a pure oxide or a lindbergite feed. Table 1 gives oxide-equivalent XRF compositions; those are not metal recoveries or product yields. COG_MN12 fragment work and the delta-oafA comparison are separate experimental scopes and are not treated as direct proof of the powdered-sample lindbergite mechanism.

The solid arm uses oven-treated powder (105 degrees C, at least 48 hours), below 210 micrometres, 0.2% (w/v) in malt extract agar, a 5 mm mycelial disc and 14 days at 25 degrees C in the dark. Figures 4-5 compare inoculated and uninoculated preparations. The source assigns the new peaks to lindbergite and calcium oxalate, with quartz also present. Figure 5 reports at least three determinations without resolving biological versus analytical replication. The solid-recovery methods also state 125 rpm, incongruous with the plate description; the record retains this uncertainty rather than silently declaring static incubation.

The liquid arm uses below-90-micrometre powder, 2% (w/v) in AP1, 14 days at 25 degrees C and 125 rpm for pellet diffraction (Figures 7-8). Figure 6 photographs are at six days. Methods give a final 10^4 spores/mL inoculum, while Figure 6 says 10^6 spores/mL. AP1 contains calcium and trace manganese, without a tracer distinguishing the source of product elements. Figure 6 displays an uninoculated powder flask and Figure 7 no-mineral fungal pellets; broth clearing and pellet capture do not measure mineral recovery. Figure 8 calls the calcium co-product monohydrate whewellite, whereas the results say dihydrate. This unresolved calcium distinction is retained without treating it as a refutation of the Mn-phase assignment.

Phase identification uses powder diffraction/ICDD, without reported specimen-specific cell refinement, water-content assay, phase fraction or Mn mass balance. Agar debris underwent approximately 70 degrees C water extraction and washing followed by a week of drying; liquid pellets were also dried for diffraction. Hydration in the living culture is unmeasured. No direct oxalate assay or killed-biomass, cell-free-metabolite or acid-matched formation series establishes a unique metabolic cause. The record therefore distinguishes the source's diffraction assignment from an independently verified crystal structure and a proposed oxalate mechanism from quantified causal enhancement.

## Counterevidence and related-study boundary

Farkas 2020 uses *A. niger* CBS 140837 and synthetic hausmannite. Table 2 labels an **orthorhombic** dihydrate cell as lindbergite, inconsistent with the authoritative **monoclinic** mineral identity. The record retains this as context only, not a second accepted lindbergite-forming mechanism. Parent curation of falottaite from this study would be shared-study coverage of a distinct phase, not replication of lindbergite evidence.

Other original-source cautions are retained in the JSON assessment for downstream work: Section 3.5 gives day 20 for falottaite identification, whereas the Discussion says first detected after day 15 and misreferences Figure 5a; Figure 6 has an extra unlabelled lower curve; the methods' 20-80-degree scan range differs from the displayed range starting at 10 degrees. There is no uninoculated or pH-matched formation series. Mn and As partition data are not phase-specific yields and do not prove intracellular uptake or incorporation into a particular oxalate crystal. Section 2.4 also orders the analytical techniques differently from the explicit Section 2.5 assignments. These deficiencies are not converted into invented measurements or a universal refutation of fungal oxalate formation.

Exact-DOI correction/retraction searches returned no relevant notice in the inspected result sets; Crossref update/relation fields were empty or absent. Search queries, date and boundaries are preserved in the JSON. This bounded check does not establish that no notice exists anywhere.

## Deduplication and provenance boundaries

Before authoring, `rg --no-ignore --hidden --follow` searched current and original checkout data/research/reviews/history. A cycle-safe, symlink-following reference scan covered 2,948 corpus files, then searched 111 existing bounded referenced raw roots. Ten corpus match lines were frontier leads; 37 raw lines included IMA entries and synthetic oxalate context from the earlier moolooite investigation. No maintained lindbergite owner or accepted Ferrier/Farkas experimental mechanism was identified in that bounded corpus. The exact roots, commands, outputs and hashes are in the paired dossier.

Ignored and hidden files were included. No corpus symlink was found during the reference scan. Prior raw PDF/image binaries were not universally decoded: searches cover their existing derived text and metadata; the two current primary studies were independently read in full. No machine-wide absence or comprehensive literature review is claimed. This record is distinct from the source nodule resource and from the sibling falottaite candidate.

## Checks and handoff

The parent's fresh baseline passed before record edits: 308 tests passed, 3 skipped, 200 records and 231 histories valid, receipt `/private/tmp/cmm-round37-baseline-terminal.json`. Named validation of the new record finished at `2026-10-11T23:00:12.304709+00:00` with exit 0: one record checked, zero failed. Its log SHA-256 is `6777300de164ce1d63474b359fe110e652a101bb74c5ca509fbe3dde481e776e`. The canonical CREATE history was generated by `just new-history`, and its printed path is attached in `history_refs`; the inline event carries its own actual UTC timestamp.

The final corpus/history/review gates and independent scientific review are pending and must cover the frozen record hash above. No shared README/schema/validator/Git/GitHub change was made by this author. Potential further work is separate: independently obtain the cited Wei 2012 birnessite transformation primary, and resolve Mn-oxalate polymorph/hydration assignments from raw diffraction or a fully documented crystallographic analysis. No author contact was attempted, and no unsupported follow-up mechanism was populated.
