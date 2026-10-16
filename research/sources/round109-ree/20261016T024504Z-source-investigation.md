# Round 109 REE source investigation

UTC: 2026-10-16T02:45:04.310136+00:00. Researcher: codex, GPT-6, codex, `/root/round104_ree`.

Worktree: `/private/tmp/CMMMech-expansion-round109-20261016`. Branch: `curate/cmm-expansion-round109-20261016`. Trusted base: `a11e47d1c90806e056bd60610a0edd2cf77813a9`.

The two accepted curation candidates are distinct kozoite-(La) and kozoite-(Nd) mineral species. Full primary descriptions and the fresh September 2026 IMA list support identity. Nd adds directly measured natural-material thermal gas release; La adds a separately scoped synthetic formation arm from a known 2025 study. Named validation passed two records with zero failures. Independent scientific review and final batch checks remain pending; this source assessment is not an acceptance review.

## Identity and primary evidence

| Owner | Authority | Primary evidence | Scope |
|---|---|---|---|
| `kozoite-la` | IMA:2002-054, list p116 | Miyawaki et al. 2003, DOI10.2465/jmps.98.137, complete5pp | Natural La/Nd zoned aggregate, calculated volatiles and powder-only structure |
| `kozoite-nd` | IMA:1998-063, list p116 | Miyawaki et al. 2000, DOI10.2138/am-2000-0724, complete6pp | Natural mixed-REE mineral and He TG-DTA/GC-MS experiment |
| La formation arm | Species identity separate from synthetic phase assignment | Terribili et al. 2025, DOI10.1021/acs.cgd.4c01168; official SI .s001 | 35 °C solution aging; fitted crystalline phase fractions, not metal recovery |

The La original was freshly acquired from J-STAGE as a scan; all five page images, four figures and two tables were visually checked. Publisher metadata explicitly separates 2003 publication from 2004 online release and lists zero supplementary materials. La Crossref returned429, while publisher DOI/HTML and the original succeeded. The Nd original was freshly acquired from RRUFF; all six pages, six figures and four tables were inspected. Fresh Crossref and publisher metadata establish the 2000 publication independently of later online dates. No separate Nd supplement was identified in checked article/metadata. Raw full papers are outside Git; public reading access does not establish redistribution permission.

The 2025 article, XML and official eight-page SI reuse exact prior-round108 downloaded bytes; they were not freshly downloaded this round. Methodspp946–948, Table1, Figures1 and8, discussionpp957–959 and all eight SI page images were re-inspected. The paired JSON records original provenance, licenses, local artifacts and SHA256 digests.

## Claim boundaries and contradictions

La original chemistry uses four La-domain analyses and includes Nd/Ca. Carbonate, hydroxyl and water contents were calculated because carbon/hydrogen could not be measured; the total with calculated volatiles is101.19wt%. The natural zoned aggregate is distinct from the2025 synthetic material. The35°C arm used40mL50mMcarbonate plus40mL50mMLa solution in static sealed reactors. Table1/Figure1b agree on kozoite18wt%at24h,54wt%at192h and100wt%of quantified crystalline phases at360h. No amorphous fraction, elemental mass balance, metal-product yield or35°C replication uncertainty is supplied. The proposed dissolution-recrystallization explanation is an interpretation; model solubilities use Nd phases because La-kozoite data were unavailable.

The separate80°C72h La endpoint differs between Table1(93/7kozoite/tengerite) and Figure1d(94/6). Existing issue#428 covers this and other2025 discrepancies; these endpoints are excluded from this mechanism. During author accuracy checking a preliminary comparison mistakenly read Figure1a's8h label as815h; this was withdrawn before review freeze. Table1 and Figure1a agree at8h. No new ambient discrepancy is alleged, and the external correction receipt preserves the pre-freeze correction.

Nd natural chemistry is mixed, including Nd0.85La0.61 on a two-cation basis. He heating at20°C/min from room temperature to900°C gave first endotherm485°C/16.07wt%loss withCO2+H2O, and second716°C/9.89wt%loss withCO2only. The assigned gas amounts sum to21.87wt%CO2and4.09wt%H2O, distinct from elemental-analysis equivalents21.10and5.44. The source calls them comparable but supplies no uncertainty resolving the difference. The~5mg portions belong to elemental analysis, not a stated thermal aliquot. No heated-residue phase, separated Nd product, industrial operation or microbial cause is established.

No criticality designation is inherited from La or Nd. There is no fabricated organism, strain or enzyme. The current schema accommodates these observations without change, using `process: other`, `microbial: false` and qualified prose; thermal/phase percentages do not enter the mg/kg concentration-observation contract.

## Search coverage, access and next actions

Hidden and ignored files were included with `rg --no-ignore --hidden --follow` across W/main records, research, reviews, histories, ignored main reports and cited raw roots90/92/107/108. Existing Ce-lanthanite context mentions kozoite-type material but does not own La or Nd kozoite. The2025 DOI is reused intentionally; the35°C solution arm differs from the existing La dry-heating/water-rehydration arm. Binary PDFs were inventoried and inspected separately. This is a bounded deduplication, not a machine-wide absence claim. The141open issue titles/bodies were scanned; comments were excluded.

Exact dated queries, filters, returned-results limits, acquisition failures and successful checksum receipts are in the paired JSON and external query artifacts. Initial default-network DNS failures and La Crossref429 were retained. No affecting notice or supportable exact-species microbial experiment was identified in returned bounded searches; absence is not universal. Known blocked routes#397/#405/#406 were not repeated, and#421's2015 supplement/timing problem remains unresolved.

Next actions, in order:

1. Independent native scientific reviews and coordinator final batch/history/review gates for these exact owners.
2. A bounded source follow-up for Nd thermal/elemental discrepancy, calibration/replication and residue identity before adding product claims; draft remains external for coordinator publication.
3. Continue existing#428 for2025 source inconsistencies without duplicating it or pooling experimental arms.
4. Consider complete primary review of synthetic structure leads DOI10.1524/zkri.2007.222.7.326 (Fersman PDF route) and2019Z.Naturforsch74b59–70 (DNB route). These were metadata/abstract leads only this round; no results are imported.

Canonical CREATE sidecars and inline events carry actual codex/GPT-6 metadata and times. Final named validation is recorded at `/private/tmp/cmm-round109-ree-research/named-validation.json`. No publication, global-gate completion or independent review is claimed here.
