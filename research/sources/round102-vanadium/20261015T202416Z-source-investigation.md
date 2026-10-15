# Round 102 source investigation: pascoite and navajoite

UTC 2026-10-15T20:24:16.185953+00:00; curator GPT-6 (`/root/round100_vanadium`). **Curated source dossier, pending independent scientific review.** This document is not an acceptance artifact.

## Scope and selection

Worktree `/private/tmp/CMMMech-expansion-round102-20261015`; trusted base `1c2a3bb043c4bd267a3d911d0e77b029c742689e`. Pascoite ranks first because the complete 2005 structural study supports a clear current species identity. Navajoite follows with complete 1955 characterization and 1990 reassessment, retaining mixed-specimen and dependent-chemistry limits. Both records use `material_kind: mineral`; no mechanisms, criticality designations, external CURIEs, or concentration observations are inferred. No schema or validator change is needed.

Baseline passed before owner writes; exact receipt path/hash is in the paired JSON. Hidden and ignored files were included and relevant symlinks followed across maintained data/research/reviews/history/docs, cited round99/100/101 raw directories, the main checkout's ignored archived handoff, and the current 261-issue title/body snapshot (comments excluded). `dedup-before-curation.json` records the actual command and matching paths; no species owner matched before creation. This is bounded coverage, not machine-wide or full-comment absence.

## Sources and inspection

The [September 2026 IMA-CNMNC list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) supplies the current names/formulas: pascoite `[Ca3(H2O)17]V5+10O28`, G/1914 on PDF page 167; navajoite `(V5+,Fe3+)10O24·12H2O`, G/1954 on page 153. Both exact rows were visually reread. The official homepage was reopened, and its indexed result still advertised this edition. The same-day downloaded PDF was hash-rechecked, not presented as another fresh acquisition. G means grandfathered; historical years are not numbered approvals. License: CC BY-SA 3.0, PDF page 2.

### Pascoite: original and newly acquired deposits

The complete [Hughes, Schindler and Francis (2005) original](https://www.rruff.net/doclib/cm/vol43/CM43_1379.pdf), DOI [10.2113/gscanmin.43.4.1379](https://doi.org/10.2113/gscanmin.43.4.1379), was inspected in the preceding same-day handoff, hash-rechecked, and its methods/model/figures/tables reread here. Harvard specimen 91449 from Minasragra, Peru is a natural single-crystal study (p. 1380/Table 1), not a bulk-ore or recovery experiment. Tables 2–3/Figures 1–2 describe disordered calcium coordination and hydrogen bonding; pp. 1383–1384 compare C2/C2/m and document constrained hydrogen refinement. Average Ca1 coordination does not impose identical local geometry. The printed comparative Table 5/Figure 3 does not establish controlled dehydration.

**New in this round:** the [official MAC depository](https://www.mineralogicalassociation.ca/wordpress/depository/) links [download 1821](https://mineralogicalassociation.ca/wordpress/?wpdmdl=1821) and [download 1822](https://mineralogicalassociation.ca/wordpress/?wpdmdl=1822). Both were acquired with exact receipts. The first is actually DOCX despite its MS_Word label and local `.doc` filename; its full XML table contains 23 non-hydrogen atom rows plus uncertainties, closely corresponding to printed Ueq values. The O(131) deposit entry (0.07442) differs slightly from printed O13A (0.0743(3)); no exact table-equivalence is asserted. The FCF contains 2844 unique HKL rows, matching article Table 1's total, and matching cell parameters/C2/m header. All supplied status flags are `o`; this does not mean all rows pass the separate paper significance threshold. The FCF header reports F000=698.00; this value was not used as a composition or atom-count assertion. No structure was re-refined.

The article calls deposits Tables 4/5; the official files call them **Table 5 thermal parameters and Table 6 structure factors**. The printed article's Table5 is a third, comparative table. Preserve those labels rather than silently renumbering them. These files are dependent data from the same 2005 experiment. Their access supersedes the prior handoff's unavailability statement; the historical handoff stays unchanged.

The [1966 IUCr issue index](https://journals.iucr.org/q/issues/1966/09/00/index.html) freshly confirms DOI 10.1107/S0365110X66002974 and a title containing 16H2O, whereas the 2005 reference list prints 17H2O. Current identity follows the IMA row and inspected 2005 original. The 1966 full text and 1914 original remain unavailable after the prior bounded attempts; no detailed results from those originals were imported.

### Navajoite: specimen and study dependence

The complete [Weeks, Thompson and Sherwood (1955) original](https://msaweb.org/AmMin/AM40/AM40_207.pdf) was inspected with all six page renderings, including enlarged chemical preparation/analysis pages 209–210. The selected natural material retains impurities and possible substitution; original chemistry does not prove a pure endmember. The historical formula and tentative diffraction Tables 2–3 must not replace current identity. Natural corvusite oxidation was inferred, while storage-related water loss lacked controlled humidity/kinetics. No microbial process follows from either observation.

The complete [Evans and Hughes (1990) original](https://msaweb.org/AmMin/AM75/AM75_508.pdf), all 14 pages previously inspected, was hash-rechecked with focused enlarged rereading of pp. 517–519/Table 7. New diffraction concerns USNM 106900 with explicitly uncertain type status; two lines were attributed to probable bokite, and other nominal specimens were reidentified. Its empirical formula reuses Sherwood (1955) chemistry. C2/m cell indexing is not an atomic-structure solution. Table 6 belongs to bokite. The 1953 USGS report and 1954 Science announcement document the same discovery; Ross (1959) remains secondhand here. None supplies another independent recovery experiment.

## Search, provenance and reuse

The paired JSON contains all six current exact queries, original acquisition times/URLs and current recheck times/hashes, source identities, exact locators, retained rendered-page hashes, current issue-snapshot boundary, and fresh deposit metadata. First returned search sets revealed no affecting formal correction/retraction; this is not an exhaustive negative finding. Official original/revision evidence takes precedence over secondary discovery snippets.

Primary PDF hashes: 2005 `37810bbe390b3c792008357523dc42882842ac6f6514361a2b05438752f64bf5`; 1955 `4aedf9f980d77905da53499b738fdd76e01e626026de56994739f89fa4ee453d`; 1990 `c6605aa475f9c1e6542095c20b5f62361a2664d64e994b143b7a8826cdf3d1f8`. Fresh thermal DOCX `afb3d6e4b4c2b8583dd50349c0860cc9c8cbf6f2b3ec166a1d390927ae780089`; FCF `268dec775597c353b3550e7df79b2a172e4cb8a16b11142e63a527222af3bf53`.

Article/deposit-specific redistribution licenses were not established. Full texts, bulk tables and returned web excerpts remain outside Git. Reading access is not redistribution permission. No automated importer or model regeneration is proposed.

## Checks and handoff

Both owner files passed their actual named validators after canonical CREATE history attachment (2 checked, 0 failed); commands, UTC times, output and exit codes are retained in the JSON/raw receipt. Scientific acceptance remains pending independent peer review and coordinator batch gates. Future priorities are the missing 1914/1966 originals and any properly characterized new navajoite structural work. Neither missing access nor a valid YAML structure is evidence of a microbial mechanism.
