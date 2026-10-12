# Rhodochrosite source investigation

Recorded at 2026-10-12T14:06:23.683537Z by codex (GPT-6; codex).
Trusted scientific base: `d88bd5c0f89f9f2fcd80debfd9bd3a2b1a7786a5`.

## Disposition and identity

Curated `data/records/rhodochrosite.yaml`, with a real CREATE sidecar, for independent scientific review. The accepted scope is laboratory formation during MR-1 reduction of synthetic colloidal Mn(IV) oxide. The owner is the mineral species, not elemental Mn, mixed manganese ore, a carbonate group, or the synthetic oxide feed. No criticality, natural-ore extraction yield or industrial claim is imported. IMA September 2026 page 185 lists Mn(CO3), status A and `1962 s.p.`; page 1 defines special procedure notation. No fabricated numbered IMA identifier is assigned. Handbook occurrence context is natural; its unit-cell and powder pattern values are explicitly synthetic and are not recast as measurements of natural specimens.

## Original evidence and access

Johnson et al. (2016), DOI `10.1021/acs.est.5b04834`, is complete in the coauthor's Caltech-hosted typeset pre-pagination PDF (11 pages A-K), not claimed to be a locally inspected final 4248-4258 issue layout. All pages, main Figures 1-3, graphical abstract, Table 1 and equations were read and visually inspected. The original supporting PDF is complete (16 pages, Tables S1-S3 and Figures S1-S7), and all pages/graphics/tables were inspected. Its MD5 `a71bc1821e0904640eb0bc546896eb4f` matches the freshly retrieved CaltechAUTHORS inventory. Source files, extracted text and original-page renders are under `/private/tmp/cmm-round59-mineral-research/raw`; the paired JSON pins all artifact bytes and acquisition receipts.

Initial Python HTTPS acquisition of the author PDF failed certificate verification; system curl subsequently succeeded with normal TLS verification, without disabling certificate checks. The old NCBI OA endpoint returned a 404 HTML body retained under the initial filename `johnson2016.xml`; it is not main-text XML evidence. The local PMC HTML response is a reCAPTCHA challenge despite HTTP 200 and was not used as acquired full text. No challenge bypass was attempted. The complete author PDF and SI resolved the evidence need. The IMA PDF is an exact reuse of the prior official September 2026 artifact, re-inspected after a fresh issuing-site link check; it is not described as a new PDF download.

## Claim and control assessment

The one-litre nitrogen-maintained experiment uses approximately 6.3 mM synthetic colloidal oxide and 20 mM lactate with no added phosphate, initially adjusted to pH 8. MR-1 precultivation at 25-30 degrees C is distinguished from an unspecified reaction temperature. Cell paste was resuspended in LB; final cell abundance, exact modified-M1 recipe and stock authentication are not reconstructed. The current NCBI entry 211586 names MR-1 and has formal rank `no rank`; its strain-name scope does not authenticate that experimental culture.

Main Figure 2B plus original SI S4-S5 establish a rhodochrosite-assigned crystalline product. Collected solids were air-dried and mostly examined by XRD 3-4 weeks later, while in-situ XAS supplies complementary phase/redox evidence. Sole crystalline product is not phase-pure recovered solid. The 73/27 terminal standard fit (approximately 75/25 in the figure caption) is a spectral mixture; the subsequent unit contribution of its combined internal endmember in Table S2 is not 100% rhodochrosite recovery. Fit selection and approximately 10% typical component uncertainty are retained. SI S1 covers more than five hours of no-cell oxide/lactate exposure without perceptible spectral change; it is not a killed-cell, full-duration or DIC/pH-matched precipitation control.

High phosphate instead produces a Mn(II)-phosphate-assigned phase, and limited lactate leaves Mn(IV) and a feitknechtite-like component. Separate sulfide/Fe(II) arms yield no observed carbonate under their low-DIC conditions; the authors explicitly allow abiotic carbonate formation when solution chemistry differs. Neither unique biosignature nor an enzyme-specific intermediate is claimed. Inorganic-carbon production is a mechanism interpretation, not an independently quantified DIC result in this study. Table S3 is from separate, slower solution assays, not a simultaneous phase mass balance. Main Figure 2B labels one product 11-26-15 while SI S2 labels it 11-26-13; the discrepancy is retained without inventing replicate dates.

## Deduplication and bounded searches

Read-only `rg --hidden --no-ignore --follow` covered records, research, reviews and history in the round59 worktree and original Documents checkout. Both returned 39 broad match lines with no errors. Referenced research/raw/source roots were extracted from those reports: 221 roots, 197 accessible and 24 missing, explicitly listed in the JSON. Binary suppression was retained; there was no OCR or machine-wide absence claim. The first broad raw search completed with 7712 lines, including excessively long minified/base64-bearing lines and false positive hexadecimal fragments for the short search term `12029`. A subsequent file-list/excerpt search uses the full relevant DOI suffixes and titles and avoids that ambiguity; a memory-heavy attempt to reparse the broad output was stopped and is not represented as successful analysis.

The refined study search found nine files, all attributable to references to the separate Tang fungal-dissolution paper or earlier search logs, rather than the Johnson experiment. No maintained rhodochrosite species owner or Johnson2016 experiment was identified in this declared boundary. Existing `manganese-ore.yaml` preserves a different 2026 mixed-feed Figure 11/prose conflict (DOI 10.1007/s42461-026-01506-2), and `iron-ore-tailings.yaml` shares that older source; neither is the Johnson synthetic-oxide experiment. The new owner does not resolve or overwrite those findings. The current study's Caltech thesis chapter is related work, not an independent replicate.

Bounded web queries included rhodochrosite microbial reduction/formation, the exact Johnson DOI and title, supporting information, and DOI plus correction/retraction/erratum. Crossref and primary publisher/institutional metadata identified no affecting correction in the returned results; this is not an exhaustive notice guarantee. Tang et al. DOI 10.1111/1462-2920.12029 is a useful distinct fungal oxidative-dissolution frontier, found in existing bibliography but not curated here: its complete primary/SI remain to be acquired and inspected. A 2020 abiotic photogeochemical rhodochrosite study (PMC7502741) is a separate potential comparison, not accepted assay evidence here.

## Validation and review handoff

Named command `uv run --locked cmmmech validate data/records/rhodochrosite.yaml` passed, one record checked and zero failed. Actual receipt: `/private/tmp/cmm-round59-mineral-research/named-validation.json`. The parent's exact-base fresh baseline is reused through its initialization receipt; no new baseline execution is claimed. No schema, validator, shared index, generated site or existing scientific record was changed by this contribution. Final independent review and batch gates are coordinated separately by the parent.

Record SHA256: `53ed811ebc346a2e8fdfa05bdd672be07c0c39a7f9bb32e2449ef10921517f50`.
CREATE sidecar: `history/records/rhodochrosite/2026-10-12T140249Z-codex-1fba4c.yaml`; SHA256 `4d47675f96366422af7c406bc912317ce5116b149ad67db636667d401289e000`.

## Raw retention

Copyrighted originals remain outside Git. Repository artifacts contain analysis, precise locators and hashes rather than reproduced articles. Acquisition failures and historical raw reuse are retained explicitly. Raw text extraction and contact sheets are derived reading aids; original PDFs remain the source authority.
