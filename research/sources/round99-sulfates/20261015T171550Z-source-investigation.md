# Round99 sulfate source investigation

Recorded UTC: 2026-10-15T17:15:50.061136+00:00. Curator: codex (GPT-6; codex), agent `/root/round99_sulfates`.
Worktree: `/private/tmp/CMMMech-expansion-round99-20261015`.
Trusted base: `beb757591995399e079d8892e8e27f8130f6bc5c`.
This is a source assessment/curation handoff, not the independent scientific review.

## Scope and novelty

Selected **kornelite** for a well-characterized chemical synthesis and a separately qualified microbial-culture phase observation, and **quenstedtite** for natural-crystal identity with two primary refinements. These extend the ferric-sulfate comparison without equating different hydrate species or adopting a constituent's criticality. No schema change is needed.

Before owner creation, `rg --no-ignore --hidden --follow` searches covered records, research, reviews and relevant round97/98/99 raw sulfate directories, with material names and DOI/AY5 terms. Hidden and ignored files were included; unrelated machine directories were excluded. Existing owners included ferricopiapite, paracoquimbite, rhomboclase, melanterite, rozenite and szomolnokite; candidate names already occurred in authority lists and contextual discussions, but there was no kornelite or quenstedtite record owner. The Ackermann2009 paper is already cited by paracoquimbite and represents a shared study with a different preparation, not independent replication. Its conference abstract and journal article are not independent datasets.

## Accepted evidence and boundaries

### Kornelite

- [September2026 IMA list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF115, lists grandfathered kornelite and its six coordinated plus1.75 channel-water formula. Pages1–2 explain fields/terms. The [Handbook entry](https://handbookofmineralogy.org/pdfs/kornelite.pdf) retains a historical7–8-water range. No approval accession is invented from1888.
- [Ackermann etal2009](https://doi.org/10.2138/am.2009.3179), full9-page original re-inspected from round98 local download:2.5g amorphous ferric sulfate in1.17mL water;75°C closed-vessel treatment48h plus9days; opening/cooling yields kornelite after initial ferricopiapite assignment. Table1/PDF2, Figure1a/PDF3 and Tables2/4 support the crystalline product. The sequence does not resolve dissolution/reprecipitation versus solid-state conversion, and has no product recovery balance.
- Hydration is explicitly method dependent: TG plateau choices7.47/7.98 total waters; single-crystal channel models1.71(5)/1.75(5), powder1.55(2). Channel ordering remains unresolved. Figure2's prose calls events exothermic whereas the plot has an upward endothermic direction and prominent downward features; no thermal pathway/threshold is curated. Table6's6.53 water coefficient conflicts with the6.75 implied by the adopted formula/Table5, so enthalpy values are excluded. Figure6 is an entropy-sensitive illustration, not an accepted measured field. The supplement attempt returned406; raw-coordinate reproducibility is not claimed.
- [Karnachuk etal2021](https://doi.org/10.3390/microorganisms9122558), official11-page PDF plus original3-page supplement acquired. Sections2.1–2.4, Figures5–6 andS1–S3 were examined. Mixed XRD traces label kornelite at pH7/day2; pH6/days3–4; pH6.5/days2/4; pH5.5/days1–2. Later traces do not retain the labels, which is not a quantitative disappearance result. Broad backgrounds, other phases, no phase-specific refinement or water assay, unspecified oxygen/drying workup and absent sterile mineralogical controls require a **provisional culture-associated assignment**. Fe/S imaging does not prove ferric sulfate. The later pH arms share a semibatch history, not independent fresh inoculations. FigureS2 weak peak assignments coexist with prose calling those phases unpronounced. No clinical conclusion or isolated recovery is accepted.
- [NCBI876](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=876) was checked live: current species label Desulfovibrio desulfuricans. The ID does not authenticate AY5; the original study supplies that isolate attribution. Database/reference diffraction numbers are not mineral-species IDs.

### Quenstedtite

- IMA PDF181 lists grandfathered quenstedtite, Fe(III)2(SO4)3(H2O)9·2H2O. The [Handbook](https://handbookofmineralogy.org/pdfs/quenstedtite.pdf) preserves10–11water historical descriptions.1889 is a date, not an approval number.
- [Thomas, Robinson and Fang1974](https://msaweb.org/AmMin/AM59/AM59_582.pdf), all5pages visually inspected: a Chilean specimen with unknown exact locality;1136 reflections before33 extinction-affected reflections excluded, final1103/R0.085. Full interlayer-water occupancy fits better than half occupancy; nine coordinated plus two interlayer waters are supported for that crystal. The cited older water-loss assays are not new assays of the selected crystal. The paper retains possible lower occupancy and calls for heating work to establish a lower hydration limit. Table2 is the printed reflection listing; no re-refinement was run. OCR misreads the first-page date as1971, but the image, volume59 and acceptance line establish1974.
- [Westland2012 Queen's MSc thesis](https://hdl.handle.net/1974/7411),161-page PDF acquired; relevant sections2.2.1/2.2.5–2.2.7/2.3.1.2/2.4, figures/tables, and printed CIF metadata/checkCIF inspected. This is a separate natural Alcaparrosa sample bought from a dealer, with romerite and surface grains attributed to gypsum. It is an MSc thesis, not a journal experiment. Table2.12 gives180(2)K, P-1,3147 independent reflections,34restraints/307parameters and R1=0.0412 for observed reflections. The original1974 and2012 samples/temperatures remain distinct.
- The thesis comparison Table2.11 gives alpha95.633/gamma93.745, conflicting with85.633/83.745 in Table2.12 and AppendixD. Main text names SMART CCD1000 whereas CIF names APEX-II CCD. No reconciled cell or instrument value is silently invented. AppendixD specifies geometric H-site location and mixed H treatment, not unconstrained direct measurement of all hydrogens. Section2.3.1.2 says O10W is less tightly bonded, while Figure2.14's caption says more tightly; that detailed relative ordering is not accepted. AppendixE checkCIF explicitly lacks structure factors and cannot perform its complete tests; a B alert concerns formula-element ordering. No independent raw-data refinement is claimed.
- The proposed romerite-to-quenstedtite transition in section2.4 is a structural hypothesis, with no observed controlled reaction. No mechanism is curated.

## Provenance, access and reuse

The paired JSON contains exact URLs/timestamps, remote status/content types, SHA256/size, raw artifact inventory, and original versus reused provenance. Initial sandbox DNS failures are retained alongside successful network acquisitions. PMC direct HTML returned a browser challenge despiteHTTP200; that file is not counted as full text. The official MDPI PDF and supplement supplied the inspected source. The Queen's handle redirected to its current Scholaris repository; the title page dates August2012 and repository metadata September4,2012, neither a new experiment.

Raw PDFs/screenshots remain under `/private/tmp/cmm-round99-sulfates-research`, with the previously acquired Ackermann original under round98. No copyrighted full texts are committed. Handbook is all-rights-reserved, IMA states distribution terms, MDPI statesCC-BY4.0; no raw redistribution license is invented for MSA originals or the thesis.

## Bounded search and counterevidence coverage

Live web queries were run on2026-10-15; only returned result sets were inspected, without exhaustive index pagination. Primary authority/DOI and publisher/repository routes supplemented them. No linked correction was surfaced in these bounded results; this is not proof that no correction exists. Exact queries:

- `quenstedtite crystal structure primary paper pdf Fe2 SO4 3 11H2O`
- `kornelite Ackermann 2009 3179 correction synthesis`
- `voltaite crystal structure natural synthetic primary mineral 2024`
- `"Thomas" "quenstedtite" "582" pdf`
- `"kornelite" "3179" pdf`
- `"quenstedtite" correction retraction structure hydrogen 2012`
- `"quenstedtite" "new phases" "2012"`
- `"kornelite" "2009" "erratum"`
- `"quenstedtite" "1974" correction retraction`
- `site:qspace.library.queensu.ca Westland "quenstedtite"`
- `"kornelite" "microbial" precipitation`
- `"quenstedtite" bacteria formation bioleaching`
- `"Robin" "Westland" "2012" thesis queens`
- `"New phases in the hydrous ferric sulfate system"`
- `"microorganisms9122558" PMC`
- `"10.3390/microorganisms9122558" correction retraction`
- `"AY5" "kornelite" correction oxidation`
- `"Westland" "Quenstedtite" correction erratum`
- `"10.2138/am.2009.3179" corrigendum retraction`

## Handoff and remaining priorities

1. Independent adversarial review of both frozen owners and canonical CREATE history, especially mixed-culture phase labels and thesis metadata discrepancies. Root runs the full corpus/history/native-review gates.
2. Seek raw diffraction and matched sterile/workup controls before upgrading the AY5 association to a causal formation mechanism. No extra organism/clinical outcome is inferred.
3. Retrieve Ackermann depositAM-09-052; inspect the2011 phase-boundary original (ScienceDirectPIIS000925411100132X),2012 DOI10.2138/am.2012.3927 and2025 DOI10.1029/2024JE008867 with their supporting data before extending stability claims. Abstracts and datasets linked to an article are not replication.
4. Acquire [voltaite2013 original](https://doi.org/10.1007/s00710-012-0254-2) and supplement. Metadata describes22 substituted synthetic samples; separate species/solid-solution scope from pertlikite before creating an owner.
5. Obtain corrected quenstedtite thesis metadata/raw structure factors, and experimental evidence for hydration/romerite transformation. Current narrow identity remains supported.

Individual validation: `uv run --locked cmmmech validate data/records/kornelite.yaml data/records/quenstedtite.yaml` returned0:2records checked,0failed. Both canonical CREATE sidecars are attached before the paired JSON hashes. Final independent reviews and batch gates are separate artifacts; this dossier does not claim them completed.
