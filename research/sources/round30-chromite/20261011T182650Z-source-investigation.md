# Chromite source investigation and curation handoff

UTC: 2026-10-11T18:26:50.806134+00:00
Worktree: `/private/tmp/CMMMech-expansion-round30-20261011`
Trusted base: `930ce995269f0ded5df009eb5916162971eb1f58`
Curator: codex (GPT-6; codex). Independent scientific review is pending.

## Decision and identity

Created [chromite](../../../data/records/chromite.yaml) as a mineral identity with one narrowly qualified specimen-associated iron-redox observation. [IMA-CNMNC September 2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf), PDF 45, lists chromite as Fe(II)Cr2O4, grandfathered, original-description year1845; page 1 defines these columns. The unchanged official PDF was reused from its recorded same-day round29 acquisition, with its copy receipt and SHA-256 retained. No assertion that this is the latest possible edition is needed. No chromium-element criticality, commodity scope or species identifier was inherited.

## Accepted primary and experiment boundary

[Chaudhuri, Lack and Coates (2001)](https://doi.org/10.1128/AEM.67.6.2844-2848.2001), *Applied and Environmental Microbiology*67(6):2844–2848, is verified by original title page and Crossref. The institutional-hosted filename says 2000, but the original publication saysJune 2001. The complete five-page original was text-read; original pages1–4 were visually inspected, including all four figures and Table 1. The relevant observation is the Table 1 chromite row on printed 2847/PDF 4. Washed anoxic whole cells, source-named *Dechlorosoma suillum* PS, were associated with nitrate-coupled Fe(II) oxidation. [NCBI 640081](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=640081) currently labels this strain *Azospira oryzae* PS and lists the source name as a heterotypic synonym. This label mapping does not authenticate the experimental stock genomically.

Table 1 reports 9.42 mmol Fe(II) oxidized/kg mineral and 95.00% of starting Fe(II). Its footnote specifies ferrozine after 6 N HCl treatment for 24 h. The denominator is therefore operationally extraction-defined. It is not 95% bulk chromite conversion or Cr recovery. A derived consistency check, 9.42/0.95≈9.916 mmol initial assay-accessible Fe(II)/kg, is far below pure FeCr2O4 stoichiometry; this reinforces the need not to equate the assay pool with total endmember iron. No correction or alternative measurement is invented.

The nearby natural-mineral paragraph reports no Fe(II) oxidation in abiotic or no-suitable-acceptor controls, but gives no chromite-specific control values or timecourse. Specimen provenance/purity, phase composition, grain size, loading, cell density, nitrate concentration, pH, temperature, duration and replication/error metadata are absent for this arm in the inspected paper. Lattice iron cannot be distinguished from accessory or surface iron. The record preserves this limitation and does not claim direct enzymatic chromite attack, chromium speciation change, dissolution, recovery or deployment.

Figure 4 is almandine. Figures1–3 concern separate soluble-FeCl2 culture/redox/product experiments. The magnetite-containing mixed precipitate and proposed abiotic green-rust/nitrate step cannot establish chromite-to-magnetite transformation. The soluble-iron prose/caption also differ on acetate concentration; neither condition is assigned to chromite.

## Counterevidence and adjacent studies

The complete eight-page [Lack et al. (2002) follow-up](https://doi.org/10.1007/s00248-001-1061-1) was acquired legitimately from the same institutional collection and visually read, including Methods and all four figures. Its text layer has a broken character map, so page images were used. It shows that FeCl2 assays and sediment experiments depend on cell growth history and conditions, and distinguishes products of growing cultures from washed suspensions. It does not provide a new chromite-specific experiment or resolve the missing 2001 metadata; its 35/37°C, pH 6.8, triplicates or FeCl2 loadings are not transferred.

A bounded search found [Carlson et al. (2013)](https://doi.org/10.1128/JB.00058-13), whose indexed primary text discusses biological and chemical contributions to nitrate-dependent Fe(II) oxidation. Complete XML access returned HTTP 500 and other page access failed. It remains a counterevidence lead, not an independently curated chromite replication. The accepted record leaves direct enzymatic versus secondary chemical contributions unresolved.

[Hua et al. (2025)](https://doi.org/10.1038/s41467-025-57300-z), *Back to chromite as a mineralogical strategy for long-term chromium pollution control*, is deferred as an adjacent identity question. Complete main XML and ten-page original PDF are retained; Methods/text were assessed, but original figures and supplements are not fully reviewed. The reported Fe-rich spinel formula has Cr occupancy x=0–1 and is not the ideal FeCr2O4 endmember. No formal reclassification is asserted. Four supplement CDN requests failed DNS; alternative legitimate routes remain. The study's microbial wastewater and soil-microcosm claims must not be imported into a mineral-species record without resolving composition and product mixtures.

[(Bio)leaching Behavior of Chromite Tailings, 2018](https://doi.org/10.3390/min8060261) is a distinct secondary-resource lead. Complete publisher PDF is retained, but full visual/SI review is still required. Source text concerns fresh/stockpiled Sukinda beneficiation tailings and a separate concentrate, not pure chromite or lateritic overburden. Future curation should preserve phosphate-associated initial Cr(VI) release, weak P.putida effects, acidifying A.thiooxidans arms, abiotic Fe(II) reduction and sampling/time metadata. It is deferred to keep this publication batch bounded, not described as access-blocked.

## Search, deduplication and notices

The query families and every retained artifact hash appear in the paired JSON. Search results were primary-source leads, not substitutes for full methods. Exact-title correction/retraction searches and Crossref relation/update fields identified no affecting notice within the inspected results. This bounded check does not prove that none exists; a direct publisher open failed.

Hidden and ignored files were included with `rg --hidden --no-ignore --follow` in both current and original checkout `data/records`, `research`, `reviews`, and `history`. Existing explicitly referenced outside-Git research roots were also searched: 464 roots, 8 resolved symlinks, 153 raw text-hit lines. Binary text/XML inspection parsed 265 of 278 PDF/DOCX/XLSX artifacts; 13 failed or exceeded the 12-second per-artifact limit, with exact paths/errors retained. Earlier interrupted broad extraction attempts were replaced by this completed bounded run. No unrelated home-directory scan, OCR of image-only prior PDFs or other binary-format search was claimed.

No duplicate mineral record or 2001 experiment was identified within that completed boundary. Existing elemental chromium, a dunite chromite-stability hypothesis, lateritic overburden, incidental chromite in copper slag and authority-list rows were inspected as distinct scopes. Numerical substring matches in two spreadsheets were false positives. Search receipts and parser failures remain under `/private/tmp/cmm-round30-chromite-research`; the record's own newly acquired evidence was excluded from the prior-coverage search. This is a bounded novelty decision, not machine-wide absence.

## Frozen outputs and checks

- Record SHA-256: `23fcf34515df26468045f4fe7ce56001be293f89da2dc02b45a0bceb11923898`.
- CREATE sidecar: `history/records/chromite/2026-10-11T182447Z-codex-8c1177.yaml`; SHA-256`e525c40297f1d87d262e218106be00e051f70ff200c1b6b69e6513ac4200fd74`.
- Named validation: `uv run --locked cmmmech validate data/records/chromite.yaml`, exit 0, 1 record checked/0 failed.
- Parent owns the final batch and independent native review; no scientific approval is claimed here.

Original copyrighted 2001 ASM and 2002 Springer full text remains outside Git. IMA terms are CC-BY-SA 3.0; Hua 2025 is CC-BY-NC-ND 4.0. Only assessment, record and provenance hashes are maintained. No new schema behavior was required.
