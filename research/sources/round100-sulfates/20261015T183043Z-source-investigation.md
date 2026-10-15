# Round100 sulfate source investigation

Recorded UTC: 2026-10-15T18:30:43.100510+00:00. Curator: codex (GPT-6; codex), agent `/root/round100_sulfates`.
Worktree: `/private/tmp/CMMMech-expansion-round100-20261015`. Trusted base: `b6831c1da19b475ea048baea4ba5c10b96d678af`.
This is a source assessment and curation handoff, not an independent scientific review.

## Selection and novelty

Voltaite and pertlikite provide a useful species-level comparison within a complex sulfate group. Current nomenclature and complete primary natural-crystal studies support both identities. The proposed2013 synthetic pathway remains deferred because its main methods were inaccessible; no mechanism is invented to fill that gap. Neither mineral inherits a constituent's criticality.

Before creation, scoped `rg --no-ignore --hidden --follow` searches covered records, research, reviews, history, local skills, referenced round99 sulfate downloads and this round's raw directory. Names already appeared in authority lists and handoffs; there was no accepted owner for either species. All253 state-inclusive repository issues in `/private/tmp/cmm-round100-integration-status.json` were searched by names and exact DOIs, without a match. Ignored/hidden files were included; this is not a machine-wide absence claim.

## Voltaite: accepted identity and limits

- The [September2026 IMA authority](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF230, lists grandfathered Voltaite with the Al-bearing ideal formula. The1841 value is a description year, not an approval accession. The original1841 paper was not acquired. The complete [Handbook entry](https://handbookofmineralogy.org/pdfs/voltaite.pdf) preserves an older variable Fe(III)/Al description; its Fe(III)-only calculated composition is not a new natural assay or the modern ideal formula.
- [Zhitova et al.2023](https://doi.org/10.3390/sym15122126), official14-page PDF, was read with all five figures and four tables visually checked. Section2.1 identifies Ni4225 from a1988 coal-fire pseudofumarole sample and SCCIII-14-20s from Bolshoi Semiachik. These two are labelled voltaite; the other sampled group species are not merged into this record. Figures2–3 show field context and associated halotrichite/alunogen. Single crystals are not evidence of a pure bulk feed.
- Sections2.2–3.2 and Tables1–4 distinguish EDS chemistry from structural refinement. All selected crystals were refined at293K in cubic Fd-3c; no clear symmetry lowering was seen in these samples. This does not refute all earlier synthetic-sector observations. H positions on one water type were restrained; Al-bound water hydrogen positions were not refined because of disorder. Fe oxidation states come from charge balance, water from18-molecule stoichiometry, and unpolished-sample totals were normalized to100wt.%.
- Table4 prints Ni4225 NH4/Na/K=0.11/0.07/0.82pfu, and SCCIII NH4/Na/K=0.14/0.04/0.84pfu, totaling1.00/1.02 monovalent cations. The ideal formula and full Table2 A-site occupancies imply2. Table2 Ni4225 N/K=0.365/0.635 also differs from Table4's chemical NH4/K ratio12/88. No values are doubled or silently reconciled. SCCIII Fe(II)/Mg=2.54/2.51 in Table4 is near the species boundary; uncertainty and method differences prevent claiming a universal exact composition. A focused source-clarification issue draft accompanies the raw handoff.
- CCDC/FIZ deposits2303617 and2303618 are reported on PDF12, but the attempted summary routes returned404. The default guessed MDPI supplement ZIP also returned404; that is an acquisition failure, not evidence no supplement exists. No raw-data re-refinement was run.

## Pertlikite: accepted identity and limits

- IMA PDF169 lists approved Pertlikite2005-055, distinct from cubic voltaite and magnesiovoltaite. [Ertl et al.2008](https://doi.org/10.3749/canmin.46.3.661), complete9-page original from the [RRUFF archive](https://rruff.info/doclib/cm/vol46/CM46_661.pdf), establishes the tetragonal natural species. All pages, Tables1–8 and Figures1–5 were visually checked. The [Handbook](https://handbookofmineralogy.org/pdfs/Pertlikite.pdf), revised2022-01-10, is context derived from that original, not replication.
- Original pages662–664 document museum type material from Madeni Zakh and portions of a single roughly2mm crystal used for optics/microprobe/structure; additional picked grains supplied bulk H analysis. Tetragonal I41/acd and unequal Fe/Mg site populations support the distinction. A preliminary cubic fit was possible but inferior; optical anisotropy supplies a separate observation on the material.
- Pages664–667/Table6 distinguish measured15.3wt.% water (10% relative uncertainty) from16.73wt.% estimated using the structure. The published formula combines microprobe chemistry, fitted spectral areas and refinement. Figure3/Table5 spectral proportions were not corrected for different recoil-free fractions, so they are not unqualified direct Fe oxidation-state measurements. Disordered Al-bound water prevented locating its hydrogens. Table8 explicitly notes powder/single-crystal cell values differ beyond reported precision.
- Figure3 labels the comparison specimen115035, while the text and Table5 say NMNH115034. The identity record preserves that conflict and does not count either comparison voltaite as another pertlikite replicate. The historical pyrite-decomposition suggestion is geological interpretation without a controlled reaction or microbial assay.
- Original deposited structure factors were not acquired. [COD9010669](https://www.crystallography.net/cod/9010669.cif) was inspected as an AMCSD-derived coordinate file: it carries automated hydrogen inference and a sum formula H84/O66.252, which is not substituted for the mineral's18-water formula. It is not an independent experiment or a replacement for raw structure factors.

## Deferred2013 synthesis and access accounting

[Majzlan et al., volume107/2013](https://doi.org/10.1007/s00710-012-0254-2) remains a strong lead. Crossref records online publication in2012; journal pagination is2013. Publisher PDF and full-text routes returnedHTTP200 subscription-preview HTML, including a purchase/login notice, rather than the13-page paper. Vienna/Copenhagen institutional entries supplied metadata and DOI links. No login or purchase was attempted.

The public linked673792-byte DOC supplement was obtained and text-converted; its TableS0 contains synthetic-crystal/refinement metadata, including Fe100 and substituted samples. This does not supply the missing complete synthesis methods or authorize interpreting22 samples as22 mineral species. No synthesis conditions, measurements, or phase-purity claims from unavailable main text enter the records. The misleading `.pdf` acquisition filename is explicitly marked `pdf: false` in the JSON and its extracted HTML rendering is not counted as primary full text.

## Search coverage and follow-up

Exact search strings, dates, acquisition URLs/status/content type/size/SHA256, owner/history hashes and raw-file inventory are in the paired JSON. Initial sandbox DNS errors are retained beside successful network acquisitions. Bounded correction/erratum/retraction queries and Crossref relation/update fields did not surface a linked correction for these accepted claims; this is not an exhaustive registry finding. A microbial query surfaced an unverified AMD study with particles labelled probably voltaite; no organism or causal mechanism was accepted from that snippet.

Priorities are the2013 original methods,2023 composition/CIF clarification, original pertlikite structure factors, and distinct magnesiovoltaite/ammonium-species primary descriptions. The2023 paper is a useful handoff for those future species, not automatic admission. Raw copyrighted PDFs remain outside the repository; source terms and provenance are preserved without claiming redistribution rights.

Named validation returned0:2 records checked,0 failed. Canonical CREATE histories are attached before final owner hashes. Root owns full batch checks and independent scientific reviews; this dossier does not claim those completed.
