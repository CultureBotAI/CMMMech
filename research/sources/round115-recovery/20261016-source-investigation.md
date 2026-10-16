# Round115 recovery-source investigation

Recorded 2026-10-16; worktree `/private/tmp/CMMMech-expansion-round115-20261016`, trusted base `f97c978dcfb98269ea46fa6a9d02a6fb0253e111`. Applied the local add-record and discover-sources skills. Raw material remains outside Git in `/private/tmp/cmm-round115-recovery-research`; no full-text redistribution is bundled.

## Selection and duplicate boundary

Selected two distinct material owners: commercial tin-copper solder (`commodity`) and spent indium-tin oxide targets (`secondary_resource`). The solder experiment used supplier-provided pieces, without documented waste origin. ITO targets are a solid feed, distinct from existing LCD glass and ITO etching-wastewater research. No criticality inheritance, organism CURIE, numerical observation cells, or industrial deployment is introduced.

Ran case-insensitive `rg --no-ignore --hidden --follow` across current `data/records`, `research`, `reviews` and original-main `reports`. The final exact pattern covered lead-free/tin-copper/Sn-Cu solder variants and DOIs `s40643-017-0173-5`, `s12010-014-0833-2`, `C7RA11976C`, `C3GC40589C`; output `dedup-solder-ito.txt` was empty before these new records. Ignored files and followed relevant symlinks were included in these bounded roots. Existing issue inventory was also searched. An earlier overbroad case-insensitive ITO regex matched the substring in capacitors and generated a large external raw result; it is superseded by exact word boundaries and is not evidence of novelty. No global home or temporary-directory absence claim is made.

## Tin-copper solder: accepted evidence and limits

[Jadhav et al. 2017](https://doi.org/10.1186/s40643-017-0173-5), *Acetic acid mediated leaching of metals from lead-free solders*, was inspected as the complete ten-page original mirrored by the German National Library at `https://d-nb.info/1147288275/34`, alongside publisher HTML. Methods pp. 2-3 establish supplier, nominal composition, cleaning, culture and chemical arms. Results pp. 6-7 and Figure 7 support metal dissolution with the reported Acetobacter preparation. Figure 8 on p. 8 was visually checked: it belongs to the separate chemical-acid experiment, not the microbial arm. No supplementary file is designated by the article; its data-availability statement says study data are included, while culture-acidity data are explicitly not shown.

The commercial sample is called Sn-Cu (63-37%) by the authors. This is preserved, not silently converted into another conventional alloy. SEM/EDS interpretation suggests a tin-rich outer layer and copper-containing interior; bulk homogeneity and the denominator for extraction percentages remain unresolved. The biological methods use 100 mg, 3 mm pieces and 4 mL culture preparation at 30 degrees C, 150 rpm and 30 h, after 24 h culture growth. Results instead call the preparation culture supernatant; cell removal and viability are unspecified. YGEA medium already includes acetic acid. Titration without shown data does not distinguish newly produced acetic acid from background/other titratable acidity. No matched uninoculated-medium or acid-only control for that preparation is specified. Triplicate sets are reported, but error-bar statistics and biological independence are undefined. Accepted support is for reported culture-associated dissolution, not isolated product recovery or a demonstrated net microbial enhancement.

[The official TISTR 102 entry](https://www.tistr.or.th/tistr_culture/cdetail.php?tno=102&type=b), successfully opened through the web tool, identifies Acetobacter pasteurianus, original No. 24 DMKU B-45, previously deposited as A. aceti. This does not authenticate the paper's culture, which is attributed to BCRC without a BCRC accession. The non-www address failed; the www authority page succeeded. No species/strain CURIE is assigned to the experiment.

The earlier Hocheng et al. 2014 DOI `10.1007/s12010-014-0833-2` remains a discovery lead. Publisher article/PDF requests returned an access HTML page rather than a full PDF; OpenAlex listed only the closed publisher and PubMed. Its abstract and the 2017 paper's discussion cannot establish the 2014 feed origin, controls or quantitative performance. The draft numerical yields and fungal/bacterial mechanisms from that lead were not accepted.

## Spent ITO targets: accepted evidence and limits

[Gu et al. 2017](https://doi.org/10.1039/C7RA11976C), *A sustainable approach to separate and recover indium and tin from spent indium-tin oxide targets*, RSC Advances 7:52017-52023, was inspected in its full seven-page original. Publisher main routes returned HTTP403, but the open-access published PDF was obtained from the identified Semantic Scholar mirror; article identity agrees with Crossref and OpenAlex. The PDF states CC BY-NC 3.0. The main text, Scheme 1, Figures 1-4 and Tables 1-4 were inspected; Table 3 and relevant figures were rendered for visual checking.

The main methods name Wako spent ITO target material; detailed service history is unavailable. The record retains that study designation with an explicit provenance limit. Sections 2.1-2.3 and 3.1-3.3 support HCl dissolution, mixed-hydrate distillation, thionyl-chloride dehydration and fractionation. Figure 4 identifies isolated solid InCl3; Table 3 reports product fractions from three roughly 5 g runs. It is defensible to distinguish product separation from solution-only leaching without accepting the claimed purities or exact recoveries. The separate 1 kg comparison in Table 4 is not a demonstrated 1 kg run.

The conventional RSC supplement route `https://www.rsc.org/suppdata/c7/ra/c7ra11976c/c7ra11976c1.pdf` returned404; a repeated attempt is recorded, not counted as an independent route. Direct publisher HTML/PDF failed403; Crossref/OpenAlex did not expose an alternative supplementary location. Thus SI is unavailable in this bounded session, not asserted nonexistent. Table S1 is needed to reconcile the main Table 1 ICP ion-labelled values versus oxide-like normalization; Table S5 underpins purity; Tables S3/S6-S8 underpin process comparisons. Main abstract, section3.3 and conclusion give different tin-recovery summaries. Exact yield/purity, normalized composition, energy/economic superiority and closed-loop reagent reuse are withheld. Table4 labels energy consumption in kW, which cannot be silently treated as energy. No microbial mechanism is inherited from references cited in the introduction.

## Notices, counterevidence and follow-up priority

Targeted live searches covered each exact DOI plus correction, retraction or corrigendum, and source-specific identity ambiguities. Returned primary article metadata and publisher content did not establish a notice for either study; this is bounded search coverage, not proof that no notice exists. Internal contradictions above are preserved in accepted records. No outside comparative recovery claims were adopted.

Priority follow-up: (1) obtain ITO SI and reconcile basis/percentages before quantitative expansion; (2) authenticate the solder culture and feed composition, and acquire the complete2014 original before comparing biological performance; (3) evaluate titanite as a separate mineral owner using acquired complete 2018 and2020 primary PDFs. Titanite has not been curated in this batch; its mixed-feed processing evidence still needs identity and phase-specific review. Existing ITO wastewater issue #265 remains distinct and unresolved. The source frontier is not exhausted.

## Retained source bytes

The following external files are reproducible evidence receipts or analysis inputs. URLs, final response types, failures and acquisition timestamps are in the acquisition receipts. PDF extraction and rendering used the standalone `/private/tmp/cmm-round97-pdf-env/bin/python`, without modifying any project environment.

| External filename | Bytes | SHA-256 |
|---|---:|---|
| `solder2017.pdf` | 1836960 | `81158339d72c15802cfcaa01990ddae25bd70c06bc62419006d08d3fd8dfd788` |
| `solder2017.txt` | 40004 | `36f62bedf61bf40cc567a41ed3bd2b3e4434c94651c1436beb75932d5e815fdc` |
| `ito2017-mirror.pdf` | 571127 | `ef21a343f4b06a8cee8d98afacd6db8eb440fff1d5cd41d2f4255fc0e5501b4a` |
| `ito2017.txt` | 33632 | `55fee2b01b6ff631c5830f7e43f45c61362c50806d947ffc3f522a1ef57feab2` |
| `acquisition1.json` | 5056 | `c44cd9a4e0ba13e32c282ffd9f9a470e9487335ae8218c25d92d147443c31cd3` |
| `acquisition2.json` | 1807 | `3ba1d43208eb7d2e88ac2e0c57c6b82bd9584d2962e1e7819c1fe1137f6fd139` |
| `ito2017-crossref.json` | 13510 | `fbbf75d707c75beb2844f28e55f7cb0ef6454887dd2fa40ab2b091664fd3b1cf` |
| `ito2017-oa.json` | 17560 | `e704fb8c6533ef9bc6bb52f7850802a55ea00761384786f7cadb11735066db4e` |
| `solder2014-openalex.json` | 17823 | `696877271e88c2d25a6b6274527250d9bd6e1f0f7d9172afb57614e47088fb20` |
| `dedup-exact.txt` | 1560 | `581921c1f958e3c7b9f0f720fec06d7000f9a04745c1c4ceee03fcaaee2bb055` |
| `dedup-solder-ito.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `r115web4.json` | 29885 | `7f2b5eaaf3d08e6bb62faf0eb3de6b49fc0e3dc1910972b2c4c94434959e8570` |
| `r115web5.json` | 31517 | `8eae2f3dd22f5d17efd8b5ea06d42f2b7783b7644b4fed3eb6ea2188204c544c` |
| `r115web6.json` | 1321 | `ac0d7b5cc54e40ed1a66f51173acc2bbfa838001c3a397ff9c6e764024e07fb8` |
| `titanite2018.pdf` | 6383096 | `066dc1380b7b360203a1db2dfdde96fccfd6b8ea57051b847650c6e50bb7abfc` |
| `titanite2020.pdf` | 2764878 | `31bfa918b0d1c4b7c2abbb3f8b5803875a939c1f4445a7bff4c8e3768cde50ed` |
