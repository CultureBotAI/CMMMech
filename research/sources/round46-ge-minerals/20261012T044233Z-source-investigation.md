# CMM source investigation: alburnite and zincobriartite

UTC: 2026-10-12T04:42:33.303279+00:00
Researcher: Codex (GPT-6; codex), `/root/round43_hardmetal`
Worktree: `/private/tmp/CMMMech-expansion-round46-20261012`
Base: `94d743a1b8bb3fe595f96e88f4cdb54a4ee72375`

## Scope and provenance

Two distinct natural mineral species are curated with bounded identity evidence. They are neither elemental germanium nor generic ore feeds. No criticality designation, microbial mechanism, industrial deployment, yield or unverified quantitative observation is imported. The parent reused the immediately completed published-base checks and coordinates final batch gates and independent review; this dossier does not claim those outcomes.

The hidden/ignored-inclusive, symlink-following deduplication searched current and original checkouts' records, research, reviews and history, plus 166 existing referenced raw/evidence/research roots. It read 3,548 metadata files; nine cited roots were missing and are named in the paired JSON. It found prior IMA rows and round45 boundary mentions, with no prior owner ID for either species. Text-bearing extensions were searched; no claim of decoding every binary PDF or unrelated machine directory. A separate accidentally broad `/private/tmp` instruction-file search was interrupted and is not used as absence evidence. No relevant instruction file exists at the directly checked worktree/ancestor AGENTS paths; user global rules and local CLAUDE/skills apply.

## Candidate inventory and evidence

| Source | Acquired and inspected | Claim-level decision |
|---|---|---|
| [IMA September2026](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Fresh complete PDF; definitions/license and rows visually checked (pp1–2,6,241). Same bytes as round45. | Approved **Alburnite Ag8GeTe2S4,2012-073** and **Zincobriartite Cu2ZnGeS4,2015-094**. This is mineral nomenclature, not criticality. |
| [CNMNC Newsletter15,2013](https://doi.org/10.1180/minmag.2013.077.1.01) | Complete12-page official original; scope p1 and entire alburnite entry p10 visually checked. | Original identity/type locality at Cârnicel vein, Roşia Montană. No detailed assay or structure refinement inferred. |
| [CNMNC Newsletter29,2016](https://doi.org/10.1180/minmag.2016.080.080) | Complete7-page official original; extracted text and pp199,202,203 visually checked. | Zinc analogue of briartite, Kipushi type provenance, BM1967,271. Historical mixed formula remains separate from current endmember. January2016 approval heading and February2016 publication differ from the proposal-ID prefix2015. |
| [CNMNC Newsletter90,2026](https://doi.org/10.5194/ejm-38-231-2026) | Complete5-page official PDF; pp231,233–234 visually checked. | On28April2026 the Commission still lists zincobriartite among approved minerals lacking a full description. This is not discreditation; September2026 still lists it approved. |
| [Săbău et al.,2016](https://igr.ro/wp-content/uploads/2019/10/2016_RJMD_vol_89_1-2.pdf) | All six article pages93–98 (=PDF97–102), Figures1–5 and Table1 read/viewed. | Qualified disputed occurrence and analytical correction, described below. |
| [Tămaş et al.,2014](https://doi.org/10.2138/am.2014.4557) | Public author-posted text partly inspected; prior Crossref metadata rechecked. Full original PDF and graphics not acquired. | Deferred analytical/structural expansion; formal identity independently supported by2013 original announcement. |

## Scientific qualifications

The 2016 Măgura study used a polished chalcopyrite-rich vein specimen, optical microscopy and SEM-EDS. It reports an arsenic-bearing phase as alburnite, yet p97 expressly leaves unresolved whether it shares alburnite symmetry or is a distinct phase. Nonstoichiometric EDS with excess silver therefore does not become a confirmed alburnite composition in the record. Figure4 shows the claimed phase's mineral association; Table1 concerns other associated tellurides. These observations are neither a biological assay nor a recovery experiment.

The same paper corrects its authors'2015 sulfotelluride report: charge compensation in an earlier SEM produced spurious contributions from neighboring chalcopyrite. This is **not** an erratum to Tămaş2014. All five graphics and the table were inspected to avoid accepting the title or abstract without the limiting conclusions. Structural resolution of the disputed phase remains a future evidence need.

The 2022 Handbook zincobriartite compilation was previously acquired and rechecked. It retains the mixed formula and blank chemistry/occurrence fields and incorrectly labels its p203 source Newsletter30. The official original explicitly says **Newsletter29**. No Handbook field is used as an independent experiment, and historical briartite grains are not reassigned en masse.

## Search, acquisition, supplements and reuse

Exact queries, provider, date, first-page coverage, raw artifact hashes and direct acquisition receipts are in the paired JSON and external `search-log.json`. Searches included correction/retraction/supplement terms and relevant historical naming. No specific correction of the2014 original was established by the bounded returned results; this is not an exhaustive absence claim.

The DeGruyter route returned emptyHTTP202; a malformed ResearchGate download link returned404, while its corrected public profile path returned403. No bypass was attempted. A fresh2014 Crossref request returned429, so prior metadata is labelled reused. Complete2014 graphics and any supplements remain unavailable. No supplement pointer was identified in the inspected approval entries or2016 article; no claim is made about unsearched repositories.

IMA lists CC BY-SA3.0Unported; Newsletter90 lists CC BY4.0. Open reuse terms were not verified for the older newsletters/2016 Romanian paper. Full originals, extracted text, images and web results remain outside Git at `/private/tmp/cmm-round46-ge-minerals-research`. Source URLs, timestamps and SHA256 values are recorded. No redistribution permission is inferred from reading access.

## Curation and validation

- `data/records/alburnite.yaml` — SHA256`bb980057adbe887790f25c5a357824179470eba8ca1ae21caab24473c7d50c1a`.
  Canonical CREATE: `history/records/alburnite/2026-10-12T044046Z-codex-1643ca.yaml` — SHA256`f2e7df84e1ee88f36bce99cc3b9b4e5f8a1e4e6210e8cc3435461176a38413a7`.
- `data/records/zincobriartite.yaml` — SHA256`b06ce6857cd85a53e1c2c11d4f414552ea9c57146b9f7d3f9e46a54718411782`.
  Canonical CREATE: `history/records/zincobriartite/2026-10-12T044102Z-codex-93d91f.yaml` — SHA256`77ddbe573fc354306233945e2734b485b533b06fa045c84b6b647c6d6ab06866`.

Named validation actually completed with exit0: `uv run --locked cmmmech validate data/records/alburnite.yaml data/records/zincobriartite.yaml` → **Checked2 records;0failed**. No schema/validator/code change was needed. Each owner has a separate canonical CREATE history and actual UTC inline event. This source dossier does not substitute for the independent native reviews.

## Priorities and limits

1. Acquire the complete2014 alburnite original and relevant supplements through a legitimate available route before importing its detailed chemistry or calculated/experimental structural values.
2. Follow zincobriartite's full-description publication status beyond the dated April2026 warning and inspect its actual methods before expanding beyond identity.
3. Seek primary structural resolution of the disputed arsenian Măgura phase; do not assume the2016 title settles identity.

No existing record was edited by this agent. Other agents' parallel owners remain under their authorship. The frontier is open and this bounded assessment does not claim exhaustive mineral or microbial coverage.
