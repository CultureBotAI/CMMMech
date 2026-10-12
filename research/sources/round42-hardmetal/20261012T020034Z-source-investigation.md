# Cemented tungsten carbide scrap: source investigation

Recorded 2026-10-12T02:00:34.794797+00:00 by Codex /root/round27_eaf_slag (GPT-6; codex).
Trusted base: `a5528a4807ba14fd8088a557ad105ac10ca62965`. This is a curator's source dossier, not an independent scientific review.

## Decision and owner

Created [data/records/cemented-tungsten-carbide-scrap.yaml](../../../data/records/cemented-tungsten-carbide-scrap.yaml) as `secondary_resource`, with [canonical CREATE history](../../../history/records/cemented-tungsten-carbide-scrap/2026-10-12T015830Z-codex-71aae7.yaml). Source-described discarded rolling-mill rollers and brazed cutting tips consist of WC with Co or Co–Ni binder. They are distinct from natural tungsten minerals, tungsten-skarn-tailings and the Tatra iron-rich metal-grinding-sludge experiment. No mineral/element ID or criticality designation is inherited. The accepted scope is culture/ferric-workflow-associated binder mobilization plus a separately marked nonmicrobial chemical product-preparation step. No absolute extraction yield, microbial advantage, WC purity or industrial deployment is accepted.

## Source identity, access and rights

Chaika, Derbasova and Gavrish, printed **2013**, *Visnyk NTUU KPI, Mechanical Engineering* **3(69):125–130**, “Research division of tungsten carbide and cobalt as a result of microbiological waste destruction of tungstencobalt waste.” The complete Russian original is available from the [official article](https://journal.mmi.kpi.ua/old/article/view/29004) and [official PDF](https://journal.mmi.kpi.ua/old/article/download/29004/28484). The institutional repository [mirror](https://ela.kpi.ua/server/api/core/bitstreams/3eb5ec37-377a-41ed-916f-de08de835bcd/content) is byte-identical: SHA256 `d9f1e4def85d66c8086ebbbe5afe78c04413046cd37dcf9645735b61b93867da`. Six original pages, all three figures, six tables and eight equations were read and visually inspected. Original renders: `/private/tmp/cmm-round42-hardmetal-research/raw/primary2013-page-01.png` through `06.png`; each image is hashed in paired JSON.

The portal posting date **2014-01-07** is not substituted for the printed2013 issue year. Its declared DOI **10.20535/2305-9001.2013.69.29004** returned HTTP404 both at doi.org and Crossref on this pass. This corrects an earlier informal handoff implying resolution; the record instead cites the accessible official article. The current non-legacy publisher route also returned404. An initial sandbox acquisition failed DNS; subsequent authorized public downloads succeeded. All success/failure URLs and times are retained, including the 2015 Elsevier response that contains only coredata, not primary methods.

The inspected landing page links one Russian PDF and the full article supplies no supplementary-material pointer. This is a bounded availability statement. The portal says Creative Commons Attribution without a verified version; originals and bulk derivatives remain outside Git. Two mirrors represent one experiment, not replication.

## Experimental evidence and limitations

| Locator | Evidence assessed | Curated boundary |
|---|---|---|
| pp125–126, Fig1, Tables1–2 | Hardmetal waste shapes; two binder types; bacterial ferric-sulfate solution; liquid:solid **volume** ratio1:1 | Not mass loading or a uniform scrap grade; Table1 is elemental composition, not a complete medium recipe. |
| pp126–128, Eqs1–2, Fig2 | Continuous mixing/abrasion, ferric chemical and electrochemical attack, proposed bacterial oxidation; spent liquor ferric regeneration;7days | Source names *T. ferrooxidans* but also an association. No strain, authenticated pure culture, inoculum density, temperature, agitation rate, reactor volume, matched sterile control or replication supplied. Apparatus is deferred to2012Ref1. |
| Fig2 | Co curve rises most rapidly in first24h and slows; percent axis says **Co content** | No initial-Co or mass-balance denominator: no numerical extraction yield. pH curve approaches4, while prose highlights1.5–3 and working criterion is below4. No constant-pH claim. |
| p127, Tables3–4 | W-rich washed residue, residual Co; Co/Ni-containing liquor with someW | Relative elemental percentages do not establish complete separation or total recovery. Carbon absent; analytical normalization insufficiently described. No fully separated roller/tip outcome arms. |
| p127, conclusion | Text reports mainly hexagonalWC by DRON-4-07; Table3 W95.395%; conclusion calls WCpurity95.2% | No displayed diffraction trace/quantitative phase fraction. Relative W is not WC purity. Particle-size range/masspeak refer to2012Ref3, whose original data were not acquired. |
| pp127–129, Tables5–6, Fig3, Eqs3–8 | Ammonia/NaF iron separation and alkaline hydrazine reduction produce reported Co-rich powders | Nonmicrobial downstream treatment; no isolated masses, complete mass balance or independently displayed Co-phase analysis. Composition is not recovery yield. |
| Table5 vs Table6 | pH11 iron-removal precipitate has44.597%Co; final pH11 powder89.843%Co vs pH5 powder87.831%Co | Qualitative co-precipitation loss pathway; cannot quantify losses or infer best whole-feed recovery from product purity. Authors favorpH5. |
| p129, Table6/Fig3, conclusion, Eq7 | TextpH4.5 vs tabulated5; NaFpowder Fe1.27 vs1.373%; conclusionCo89.8 tracks pH11 not preferredpH5; Fig3 omitsNi; Eq7 fluorine/charge balance wrong | Preserve conflicts without silently repairing source or adopting a validated product/process specification. |

Fresh NCBI API and original browser HTML verify **NCBITaxon:920, Acidithiobacillus ferrooxidans** and the homotypic synonym **Thiobacillus ferrooxidans**. This is a species name mapping, not experimental strain authentication. No matched sterile ferric/acid-only/no-mixing arm separates chemical, mechanical and biological contributions. Contact-mediated oxidation is explicitly proposed by the paper, which says the mechanism remains incompletely established. Environmental/economic claims have no assessed comparative or deployment evidence.

## Deduplication and search boundaries

Before record creation, hidden/ignored-inclusive, symlink-following text searches covered `data/records`, `research`, `reviews` and `history` in both round42 and original main, plus **150 existing raw/research roots referenced by those documents**. A cycle-aware metadata scan read **3248** files. Exact roots, commands, result files, missing paths and stderr are in the paired JSON and external dedup receipts. Existing metal-grinding-sludge and tungsten-skarn-tailings were read; issue103's Han2023 mining-waste context does not identify these manufactured scraps.

The broad `WC.Co` regular expression also matched encoded strings; its raw output is not treated as evidence of experiment overlap. A subsequent precise author/DOI/URL/slug search returned no matches in the same bounded roots, with no stderr. No hardmetal/carbide record owner was found by the scoped ID query. This does not search unextracted binary PDF/image/archive content or unrelated filesystem trees and is not a machine-wide absence claim.

The paired JSON records **19 actual web queries**, provider/date, first-result coverage and all downloads. Exact-title/author and DOI notice queries returned the primary/citations, without an identified affecting notice. The absence statement is limited to those returned sets.

## Deferred leads and next actions

1. Acquire original2012 apparatus paper (Chaika/Derbasova, *Collection of Scientific Works SNUNEI*4(44):194–200) and original2012 WC-powder study (Baranov etal.,2(42):88–94) through a legitimate complete source. The present paper references them; no apparatus/particle distribution is inferred from inaccessible originals. Search also surfaced inconsistent pagination citations, so publication identity must be reconciled first.
2. DOI10.1016/j.corsci.2015.01.036, *Corrosion behavior of WC–Co hardmetals in the oil-in-water emulsions containing sulfate reducing Citrobacter sp.*, is verified metadata for a distinct corrosion experiment. Publisher API returned coredata only; full original methods/figures remain unavailable here. Abstract-level acceleration/inhibition is a useful counterevidence lead, not accepted measurements or evidence of scrap recovery.
3. GS Bavaria industrial-recycling announcements/conference abstracts are discovery leads only. No deployment, performance or product-purity claim is inherited into this record. More recent chemical/electrochemical hardmetal reports found by the survey were not curated.

## Validation and provenance

Named validation actually completed with exit0: **1 record checked,0 failed** (session84725). The baseline is explicitly reused from the freshly validated identical published base, as recorded in `/private/tmp/cmm-round42-initialization.json`; no new baseline execution is claimed. Parent owns final corpus/history/review gates. Independent scientific review is pending; this author does not self-approve.

Frozen record SHA256: `16210c05938ea5d7486a5450dcf2c7e8d04192a82fbc991bb62c1c84699ed422`. History SHA256: `7d4d6a35c27e63e87e02e3531644ef3b4a525e9bdf2a00b253f6f6219b5e25e6`. The paired JSON preserves every current raw-artifact checksum, acquisition URL/time, dedup boundary and validation receipt. No schema, validator, shared index or existing record was changed by this candidate.
