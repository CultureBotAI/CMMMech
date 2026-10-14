# Round62 secondary-resource source investigation

## Scope and provenance

- Actual UTC completion: 2026-10-14T04:40:43.504363+00:00. Investigator: Codex (GPT-6), delegated agent `/root/round61_fluorite_sources`.
- Verified base: `11a0b0f8e2714f1863304faf408da4ce0e7c5b53`; isolated worktree `/private/tmp/CMMMech-expansion-round62-20261014`, branch `curate/cmm-expansion-round62-20261014`.
- Question: identify genuinely unrepresented resource owners for spent cerium glass-polishing waste and chemically processed chromite residue, using accessible primary evidence. This is a bounded two-resource investigation, not a global source-exhaustion claim.
- Local discovery/add-record skills, source guide/report template, CLAUDE, record contract, current schema and relevant validator/tests were read. Installed and repository skill bytes matched. Root's prechange baseline passed: 317 tests, 3 skips, 278 records and 327 histories.
- Two records and canonical CREATE histories were authored after baseline success. Named validation passed for each. They remain pending independent scientific review and the coordinator's final batch gates; this dossier does not constitute their acceptance review.

## Selection and identity

1. **Chromite ore processing residue (COPR)** adds a chemical-processing waste owner distinct from existing `chromite.yaml` and `chromite-beneficiation-tailings.yaml`. The latter already explicitly excludes chemically processed residue. A complete primary article and its original supplement support a carefully bounded biogenic-reagent redox mechanism.
2. **Spent cerium-based glass-polishing slurry** adds a mixed used abrasive/glass waste owner. The accessible primary establishes actual factory waste and isolation of a ceria-rich product. Its accepted mechanism is explicitly nonmicrobial; no organism, element identifier or criticality designation is assigned to the waste.

No list-membership claim is made for either waste. Criticality authority searches were unnecessary for the chosen claims; a constituent's designation must not be inherited. No schema change was needed. Yields, oxidation-state proportions and oxide-equivalent percentages remain qualified prose rather than being forced into the schema's mg/kg concentration-cell observations.

## Hidden/ignored-inclusive deduplication

`rg --no-ignore --hidden --follow` searched repository `data`, `research`, and `reviews` for resource synonyms and both exact DOI strings before record creation. Existing matches were contextual chromite/tailings mentions, not a COPR owner, polishing-waste owner or curated experiment from either selected DOI.

Relevant earlier chromite dossiers pointed to 13 retained local research roots. Their complete hidden/ignored, symlink-following inventory contained 782 files, including 25 PDFs. Plain/binary content was searched with `rg -a`; PDF text was separately extracted with a 12-second per-file bound. Three PDFs timed out: the two retained `ima-2026-09.pdf` copies in round30-chromite and round30-pyrrhotite, and `round28-tatra-research/raw/mineralia-slovaca-1996-28-5.pdf`. These are declared extraction gaps; no assertion about all content of those PDFs is made.

The prior `(Bio)leaching Behavior of Chromite Tailings` PDF, page 21/reference 20, and retained publisher XML already cite Watts2015; the XML contains DOI `10.1016/j.apgeochem.2014.12.001`. Thus Watts is a **previously referenced publication newly acquired and curated directly**, not a claim of first discovery. No prior Janos DOI match was found within the successfully inspected bounded material. This does not cover unrelated home/temp trees. Exact commands, roots, outputs and extraction errors are retained in `dedup-repo.json`, `dedup-raw-inventory.json`, `dedup-raw-results.json` and `dedup-raw-rg.txt` beneath the raw research root.

## Search and acquisition

All 12 exact web queries, dates, provider and coverage limits are in the paired manifest. Searches used the first returned `web.run` result set, without date/domain filters or additional pagination. Primary article pages were opened at PMC, Strathprints and Wiley; query execution dates are known, while exact web-tool execution seconds were not retained. Download receipts independently provide precise UTC start/finish times, requested/final URLs, HTTP status, content type, byte count and SHA256.

- Watts primary: DOI [10.1016/j.apgeochem.2014.12.001](https://doi.org/10.1016/j.apgeochem.2014.12.001), PMID 26109747, PMCID PMC4461148; published in Applied Geochemistry 54 (2015), 27–42, online 11 December 2014. Complete 16-page final published PDF downloaded from [Strathprints](https://strathprints.strath.ac.uk/56145/1/Watts_etal_AG_2015_Biogenic_nano_magnetite_and_nano_zero_valent_iron_treatment.pdf). Crossref and primary metadata agree. The primary body was read; original pages 2–13 were visually inspected, including all nine figures and four tables. References were not all independently followed.
- Watts SI: PMC's linked DOCX returned HTTP200 HTML instead of a document. The [publisher CDN DOCX](https://ars.els-cdn.com/content/image/1-s2.0-S088329271400300X-mmc1.docx) succeeded. Its document XML text and both original TIFF figures were inspected; derived PNGs permit independent review. SI 1 is reagent XRD, SI 2 early aqueous kinetic fits. They add no independent COPR experiment. An attempted old PMC OA locator returned404; no further retry was needed.
- Species: the live [NCBI 35554 entry](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=35554&mode=Info) explicitly gives current name Geobacter sulfurreducens and rank species. Its type-strain details do not authenticate the unspecified experimental strain.
- Janos primary: DOI [10.1155/2015/241421](https://doi.org/10.1155/2015/241421), 2015 Article 241421. Wiley's indexed primary HTML was accessible via web; direct download returned403. An openly accessible [Semantic Scholar copy of the original publisher PDF](https://pdfs.semanticscholar.org/4ad8/d9ff730221af389414d2494e98c988a3c19b.pdf) succeeded. The file contains eight article pages plus one publisher advertisement. Original article pages 1–5 were visually inspected, including feed/recovery methods, Table1, and all recovery/product Figures1–3. Later degradation-performance experiments are outside the curated mechanism; their controls were inspected only to prevent assigning them to metal recovery. Crossref confirms DOI/title/year; article receipt/acceptance dates are not confused with publication year.

The Watts article explicitly states CC BY3.0; the Janos article states Creative Commons Attribution. The SI itself has no separately inspected license declaration. All raw sources, original media and derived text/renders remain outside Git at `/private/tmp/cmm-round62-secondary-research`; no raw full text is committed.

## COPR claim assessment

Sections2.3 and3.5 establish a Glasgow borehole waste-fill sample associated with Rutherglen processing. Field identification was tentative, based on pale granular appearance and high-pH yellow leachate, followed by XRF/XRD characterization of a mixed cementitious residue. The groundwater was sampled at a different Glasgow site. Table4's3.8wt%Cr is an XRF tabulation without loss-on-ignition correction, not a field-wet concentration or chromite phase fraction. XRD did not detect remnant chromite; that is not proof of absolute absence.

Sections2.1 and2.8 separate biological reagent production from residue treatment. Geobacter produced magnetite from ferrihydrite, after which the particles were washed three times to remove cells. Complete sterility was not demonstrated. The duplicate COPR batches used25g field-moist residue,50mL water,120mL bottles,N2,20°C and100days. Doses were percentages of wet COPR; pH stayed12.5–12.9. No-addition controls and synthetic nZVI comparators constrain attribution, but no viable-versus-killed-cell experiment was performed in the waste.

Figures7–8 and Sections3.5–3.6 support aqueousCr(VI) below the1µM detection limit with5/10%biogenic magnetite within one day, against approximately1.3mM in untreated controls. Day50 XANES fits indicate26%of totalCr asCr(VI) in the control and7%with either5/10%BnM. The4–7%range in the abstract includes the synthetic nZVI arms; it must not be assigned wholesale to BnM. These fits are neither whole-residue mass percentages nor recovery yields. The initial alkaline extraction estimated7%Cr(VI), versus26%by XANES; both are retained with the authors' incomplete-extraction interpretation. A unique crystallineCr(III) product was not resolved.

The subsequent air challenge began after100days and continued for another100days (Sections2.9/3.7,Figure9). All BnM arms remobilized some aqueousCr(VI); the authors describe higher-dose increases as less than10%of originalCr(VI). Oxidation ofCr(III) and changed solubility of residualCr(VI) remain alternative explanations. Consequently, broad stability language is narrowed; no complete detoxification or indefinite field stability is accepted. The separate groundwater tests show passivation, oxygen inhibition and incomplete electron utilization, while Section4 identifies possible injection/clogging obstacles. Neither living-microbe field remediation nor isolated chromium recovery is demonstrated.

## Polishing-slurry claim assessment

Sections2.1–2.4, Table1 and Section3 concern actual Dioptra waste from Cerox-based optical polishing, collected over six months, rather than fresh reagent CeO2. The partially dewatered slurry retained about50%water. Table1's dry oxide-equivalent values show a silica-rich mixed feed and a ceria-rich product retaining lanthanum and minor impurities. The recovered92.8wt%CeO2-equivalent value is not92.8%recovery or elemental-Ce purity.

The study reports acid/peroxide digestion, separation of undissolved solids, carbonate precipitation and calcination to an isolated oxide product. Original Figures1–3 show solid-product morphology, thermal behavior and ceria-type diffraction. The authors report approximately70%cerium yield in the digestion step and negligible downstream losses, but do not provide recovery-stage replication, uncertainty or a closed mass balance. These remain approximate author-reported outcomes. No acid-only/peroxide-omission control resolves individual reagent contributions. The B-400 reagent-derived comparator and degradation blanks/duplicates control later product-performance assays, not waste recovery.

The carbonate precursor lacked a single fully resolved composition. A fluorite-type CeO2 crystal structure does not mean the CaF2 mineral fluorite. The waste is compositionally variable, and its historical richer predecessor must not be substituted for the present feed. No industrial deployment or microbial involvement is claimed.

## Corrections, counterevidence and deferred leads

Exact DOI/title correction/retraction queries identified no correction notice in the returned sets; both acquired Crossref records lack an `update-to` relation. This is a bounded check, not proof that no notice exists anywhere. Internal control/null, assay-disagreement, incomplete-reduction, passivation and remobilization evidence was actively preserved.

Potential extensions were not used as accepted evidence: the 2015 Pd-biomagnetite COPR-leachate study ([PMC4394151](https://pmc.ncbi.nlm.nih.gov/articles/PMC4394151/)) is a separate aqueous experiment needing its own full inspection; DOI [10.1016/j.scitotenv.2023.163192](https://doi.org/10.1016/j.scitotenv.2023.163192) surfaced as a primary abstract about reductant interference in alkalineCr(VI) assays, but its complete methods were not acquired. These leads reinforce the need for exact analytical scope; no unavailable measurements were imported. Cerium microbial searches returned chemical-recovery sources and work on other Ce substrates, not a verified microbial experiment on this exact spent-polishing feed. That is a bounded search result, not biological impossibility.

## Handoff and checks

- Created `data/records/chromite-ore-processing-residue.yaml` and `data/records/spent-cerium-glass-polishing-slurry.yaml`, each with an actual-time inline CREATE and canonical sidecar. Paths/hashes and exact creation/validation commands are in the manifest.
- Both named `uv run --locked cmmmech validate <path>` checks passed, one record checked and zero failed each. No schema, validator, test, README, generated pages or governance files were changed by this investigator.
- Independent scientific review must assess the final record/history hashes, distinguish BnM synthesis from in-waste growth, preserve wet-dose and fitted-speciation denominators, and keep the chemical polishing recovery explicitly nonmicrobial. Root coordinates final full-corpus gates and publication.
- Future priorities: characterize other COPR origins and actual field performance separately; obtain transparent recovery mass balances and replicate datasets for polishing waste; inspect any proposed microbial polishing study in full before extending that record. Raw source availability and source coverage beyond the named routes remain open.
