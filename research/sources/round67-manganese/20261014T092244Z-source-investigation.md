# Manganese source investigation: asbolane, pyrochroite and feitknechtite

UTC: 2026-10-14T09:22:44.193932+00:00. Author: codex /root/round67_manganese (GPT-6; codex). Worktree `/private/tmp/CMMMech-expansion-round67-20261014`, trusted base `4df8fe16fc1625d789d28bb7ec727d48785c1a26`.

## Scope and selection

Three distinct mineral owners follow one newly acquired primary experiment: a source-assigned synthetic **asbolane** precursor and **pyrochroite** and **feitknechtite** assigned among its transformation products. These are not three independent replications. The complete official Buchanan thesis provides actual assay conditions, controls, phase patterns and spectral limitations. Records retain those limits instead of adding identity-only placeholders or copying constituent criticality. No criticality designation or mineral CURIE is invented.

The September 2026 IMA list identifies asbolane as grandfathered (historical year 1841, PDF 16), pyrochroite as grandfathered (1864, PDF 179), and feitknechtite as approved with notation 1968 s.p. (PDF 67). The dated original was rechecked from a retained file, while the current CNMNC homepage was fetched afresh. These dates are not fabricated approval accessions. Post 2023's monoclinic C2/m structure supersedes the old trigonal feitknechtite description in the Handbook and the thesis's historical statement that its precise structure was unknown.

## Search and deduplication

The companion JSON records all exact web queries, URLs, acquisitions, UTC times, hashes and raw boundaries. Searches covered manganese mineral names and microbial transformation, the Buchanan title/counterpart, current identity, and corrections/retractions. Only the first result set was inspected for each web query; no date/domain filter or exhaustive claim is made. The title search and Crossref first 10 bibliographic results did not identify the published asbolane counterpart. A 2022 Frontiers ferrihydrite publication is a different experiment and cannot authenticate Chapter 4 as a published journal article.

Hidden and ignored files were included in `rg --no-ignore --hidden --follow` searches of maintained records/research/reviews/history and the named round 40, 59, 65, 66 and 67 raw roots. Relevant named PDFs were decoded. Initial searches found contextual feitknechtite references but no current pyrochroite/feitknechtite owner; root additionally checked asbolane before its addition. These are scoped searches, not a machine-wide absence claim. Previously curated manganese-ore references to lithiophorite do not prove phase-specific activity.

## Primary evidence actually inspected

[Buchanan's original](https://pure.manchester.ac.uk/ws/portalfiles/portal/261215972/FULL_TEXT.PDF) is a 229-page thesis whose cover says 2021; [Manchester metadata](https://research.manchester.ac.uk/en/studentTheses/the-bioreduction-of-cobalt-and-nickel-bearing-manganese-minerals/) gives award 11 January 2022. Chapter 4 says its manuscript was in revision at ACS Earth & Space Chemistry. The chapter's scientific body, all eight main figures, two main tables, two appendix figures and two appendix tables were read, plus relevant Chapter 3 methods and copyright pages. Unrelated thesis chapters were not fully assessed.

Washed living Geobacter sulfurreducens cells from an unspecified Manchester stock were incubated with synthetic Co/Ni-bearing oxide in bicarbonate/acetate, anaerobically at 30 degrees C in darkness. The source gives stock 2 mmol/L Mn, 5 mL aliquots and final OD600 0.6, but not the added cell volume or precise final mineral concentration. Species NCBI35554 was resolved live; no PCA strain identification was assumed. No-cell mineral/acetate controls accompany supernatant ICP-MS. The limited aqueous release and retained solids are distinct from isolated recovery.

Figure 4.2 on printed page 131 assigns the precursor to asbolane, pyrochroite at 1, 17 and 72 hours, and feitknechtite at 1 and 17 hours with rhodochrosite. It contains no phase refinement or corresponding no-cell mineral patterns. Sample slurry was dried anaerobically before XRD. The phase labels are source assignments in mixed solids, with overlapping low-angle pyrochroite/feitknechtite peaks. No phase-pure yield or drying-independent identification is adopted. The 17-hour lath assignment in TEM is explicitly tentative.

Figures 4.1 and 4.4, with the spectral tables and appendix, support culture-associated mobilization and declining Mn valence, but not a compulsory crystalline intermediate or unique cytochrome mechanism. The 72-hour biological solution sample is one bottle; 24-hour replication is unspecified. Bulk spectral fits and spatially restricted SXM disagree substantially, carry stated 10% fit error, and lack 72-hour SXM. One imaged region per time was acquired. These are fitted valence fractions, not mineral abundances. Cobalt's direct biological versus indirect chemical reduction route remains unresolved.

Source errors remain explicit: tables 4.1/4.2 are printed 6.1/6.2; the 17-hour co-located manganese means differ between main table and appendix/text; region counts disagree; Appendix Table 4.2 caption says Mn but its columns are Co; enrichment acetate wording differs from the medium table; the conclusion prints Mn(VI). None is silently repaired into a quantitative pathway. Persistent bulk Mn(III) at 72 hours prevents treating lack of a labelled feitknechtite peak as completeMn(III) conversion.

[Post et al.2023](https://doi.org/10.2138/am-2022-8729) was acquired as the official 45-page accepted manuscript. Its structural methods/results/discussion, Table 1 and Figures 1–3 support the current monoclinic identity. The separate synthetic impurity phase does not establish an additional approved natural species. The complete thermal experiments and supplementary CIF were not evaluated; no additional mechanism is imported.

## Contrary evidence and access limits

Bounded title/correction/retraction searches returned no identifiable notice for the thesis chapter, not proof of absence. Discovery surfaced the original Geobacter species description's Mn(IV) negative result and later genetic Mn(IV)reduction studies; these are different stock/condition contexts, not tested replications of Buchanan's unspecified stock, and full originals were not evaluated here. The species-level record therefore cannot imply universal Mn reduction or PCA authentication.

Bargar 2005 and Mandernack 1995 are promising primary leads for feitknechtite in SG-1 spore systems, including reinterpretation as secondary abiotic products. Only discovery abstracts/passages were inspected in this pass, so no mechanism values were imported from them. The new NSR 2026 XML was acquired and screened; its products belong to existing cryptomelane/todorokite/ramsdellite owners. Complete figures/SI remain to be assessed.

## Delivery, rights and next actions

Records: `data/records/asbolane.yaml`, `data/records/pyrochroite.yaml`, `data/records/feitknechtite.yaml`; canonical CREATE histories and hashes are in the JSON. Named validation passed 3 records, 0 failures after baseline clearance. Independent scientific review and final batch gates follow this source assessment. No schema or validator change was needed.

Raw files remain outside Git at `/private/tmp/cmm-round67-manganese-research`. The thesis's author copyright statement and Handbook's all rights reserved terms were read; reading access does not authorize redistribution. IMA's retained list states CC BY-SA 3.0. Post accepted-manuscript reuse rights are not established. Only original assessments and provenance are committed.

Prioritize complete Bargar 2005/Mandernack 1995 comparison, Buchanan Chapter 6 mixed-feed assessment under the existing manganese-ore owner, and full NSR 2026 figure/SI inspection for existing owners. Seek final Buchanan asbolane publication or raw diffraction/control/spectral data to resolve the phase and table discrepancies. Prior Boothe-Lordon, Min and Bohu leads remain open. This bounded pass does not establish source exhaustion.
