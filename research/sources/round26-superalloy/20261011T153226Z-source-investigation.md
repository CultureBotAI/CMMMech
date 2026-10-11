# CMM source investigation: Ni-based superalloy residue powders

## Scope and provenance

- UTC timestamp: 2026-10-11T15:32:26.242815+00:00. Researcher: Codex (GPT-6; round24_sulfuric_catalyst).
- Worktree: `/private/tmp/CMMMech-expansion-round26-20261011`; branch `curate/cmm-expansion-round26-20261011`; trusted base `d20fc229fe61a08e36a2889d89e0f4ce7c06c4a9`; [batch issue 93](https://github.com/CultureBotAI/CMMMech/issues/93).
- Outcome: **defer record creation**. Substantial primary methods text was inspected, but original figures, complete paper and supplement inventory remain unavailable. This source assessment is not an acceptance review; no record or canonical history was created.
- Candidate identity is an industrial secondary residue from superalloy bars. SAR-Ni 30167, SAR-In 32083 and SAR-Re 30168 are source stock labels, not elemental identities, mineral species or verified alloy grades. No criticality claim is assigned to the mixed residue.
- Hidden and ignored files and relevant symlinks were included using `rg --no-ignore --hidden --follow` across `data/records`, `research`, `reviews`, `history`, round25 button/frontier/blast-furnace-dust raw directories and this round's superalloy raw directory. Exact DOI, superalloy variants and all three stock codes were searched. No curated record matched in these boundaries; prior round25 research/frontier/review leads did. Unrelated home/temp trees were excluded. Receipts: `/private/tmp/cmm-round26-superalloy-raw/final-dedup-receipt.json` and `final-dedup.txt`.

## Search and acquisition log

Searches on 2026-10-11 used web search, the first returned result set and no pagination or explicit date filters. Exact queries and all HTTP acquisition receipts are preserved in the paired JSON.

| Provider/source | Exact query or URL | Inspected scope | Result/access limit |
|---|---|---|---|
| Web search | `"10.3390/pr13072157" pdf`; `"Strategies for Nickel and Cobalt Mobilisation"` | First result sets | Primary publisher, institutional metadata and later a publisher-provided ResearchGate mirror |
| Web search | `"Strategies for Nickel and Cobalt Mobilisation" site:pureportal.coventry.ac.uk`; `"Constantin2025VoR.pdf"` | First result sets | Coventry final-version link found; PDF returned 403 |
| Web search | `"processes-13-02157" pdf`; `"pr13072157" "mdpi-res"`; `"superalloy residue" bioleaching control bacteria` | First result sets | Indexed Methods and selected Results; no full local article |
| Corrections/SI | `"10.3390/pr13072157" correction OR retraction OR supplementary`; `"10.3390/pr13072157" "supplementary"`; `"Strategies for Nickel and Cobalt Mobilisation" correction erratum retraction` | First result sets | No applicable notice identified; not an exhaustive absence finding |
| Publisher | [https://www.mdpi.com/2227-9717/13/7/2157](https://www.mdpi.com/2227-9717/13/7/2157) and `/pdf`, `/htm` | Direct requests and indexed primary text | 403/429 or route inaccessible; indexed text was readable |
| Publisher CDN | `https://mdpi-res.com/d_attachment/processes/processes-13-02157/article_deploy/processes-13-02157.pdf` and `processes-13-02157-v2.pdf` | Bounded public PDF attempts | Unversioned route 403; versioned route 404 |
| Crossref | `https://api.crossref.org/works/10.3390/pr13072157` | Full metadata JSON | 200; version-of-record license, DOI, authors, date and empty update relation checked |
| ResearchGate | [Publisher-provided primary mirror](https://www.researchgate.net/publication/393495150_Strategies_for_Nickel_and_Cobalt_Mobilisation_from_Ni-Based_Superalloy_Residue_Powders_Using_a_Sustainable_and_Cost-Effective_Bioleaching_Method) | Methods 2.1–2.4, parsed Table 1, selected Results and closing statements | Text accessible; original PDF and Figure 3 image failed 403/404. No complete figure review |
| Browser | [Coventry page](https://pureportal.coventry.ac.uk/en/publications/strategies-for-nickel-and-cobalt-mobilisation-from-ni-based-super/) | Read-only final access attempt | CUA reported no available browser |

## Candidate inventory

| Candidate | Stable ID and version | Role | Evidence inspected | Decision |
|---|---|---|---|---|
| Constantin, Hall, Pourhossein and Farnaud (2025), *Strategies for Nickel and Cobalt Mobilisation from Ni-Based Superalloy Residue Powders Using a Sustainable and Cost-Effective Bioleaching Method* | [10.3390/pr13072157](https://doi.org/10.3390/pr13072157); Processes 13(7), 2157; published 7 July 2025; institutional record advertises a 21-page version of record | Primary experiment | Bibliographic/license metadata, partial primary text and flattened table; no original figure pixels | Defer until original figures, full control design and normalization are checked |
| Coventry, Crossref and ResearchGate representations | Same DOI/study | Metadata and publisher mirror | Provenance/access context | Same experiment, not independent replication |

## Source assessments

The [Coventry institutional record](https://pureportal.coventry.ac.uk/en/publications/strategies-for-nickel-and-cobalt-mobilisation-from-ni-based-super/), Crossref and [publisher mirror](https://www.researchgate.net/publication/393495150_Strategies_for_Nickel_and_Cobalt_Mobilisation_from_Ni-Based_Superalloy_Residue_Powders_Using_a_Sustainable_and_Cost-Effective_Bioleaching_Method) agree on authorship, DOI and publication date. Crossref's 9 October 2025 deposit and 18 August 2026 index dates are metadata-maintenance dates, not new experimental editions. Crossref and the mirror specify [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A later import must preserve attribution and distinguish observations from interpretation.

Methods 2.1 describes three heterogeneous residue feeds supplied by AAS Ltd., Sheffield. Approximately 35 g of each was milled at 300 rpm for 10 min using eight 20 mm stainless-steel balls, and material below 250 µm was selected. Introduction discusses production/cutting dust, while Results describes differing manufacturing origins. Exact individual origins and alloy-grade identities still need confirmation; generic alloy scrap, EAF/BOF slag, catalysts and commodity nickel must remain distinct.

Methods 2.2–2.3 identifies *A. thiooxidans* and an unresolved sulfur/iron-oxidizing consortium from Bangor's Acidophile Culture Collection. Their lixiviants were filtered at 0.2 µm before residue addition. The candidate mechanism is therefore mobilization by cell-free culture-produced reagents, not observed cells growing on or attaching to alloy. No stock accession or consortium membership is accepted from this partial investigation.

Bio-acid began at pH 1.0, Bio-ferric at pH 1.8 with 45 mM ferric iron, and their combination at pH 1.0 with 45 mM ferric iron. The initial culture medium itself was acidified with sulfuric acid. The base assay used 1% w/v residue in 100 mL, 30 °C, 130 rpm and seven days. These unequal starting acidities cannot isolate an acid-versus-ferric causal mechanism. The inspected Methods do not establish a matched chemical-acid/ferric blank; the full article must be checked before making a broader absence claim.

Equation 3 normalizes liquid metal concentration times volume to feed mass times measured feed metal content. Those feed contents come from aqua-regia analysis, yet §3.1 explicitly acknowledges incomplete digestion and residual base metals. Future yield claims must retain this operational denominator and avoid treating it as proven total-feed inventory or isolated-product recovery. The parsed Table 1 gives SAR-Re cobalt as 65.30 g/kg, while the later discussion equates a 10% change with about 7.45 g/kg Co. This apparent inconsistency needs original-table/graph adjudication; neither value is silently corrected here.

Agitation and peroxide experiments require a full figure review. Methods reports 130, 200 and 270 rpm, plus 1–7 mL of 30% peroxide added to 100 mL bio-acid, described as 100–700 mM, at 30 °C for ten days. Final-volume conventions, blank definitions, sampling compensation and uncertainties remain unchecked against the plots. Higher early-stage dissolution must be considered alongside later lower-speed counterevidence and the weaker SAR-In response. No extraction endpoints are accepted in a record from this search.

The closing statements report article-contained contributions, author inquiries for further data, joint company/university funding, and coauthor Stephen Hall's employment by the supplier. No complete raw dataset or supplement inventory was established. Any future curation must distinguish flask experiments from industrial implementation and must not inherit the paper's broad cost, emissions or sustainability assertions as demonstrated outcomes. The exact-DOI/title correction search found no applicable notice in its first result sets; empty Crossref relations do not establish universal absence.

Raw metadata and acquisition attempts are retained outside Git at `/private/tmp/cmm-round26-superalloy-raw`. The paired JSON includes timestamps, URLs, file sizes and SHA-256 hashes. Crossref JSON SHA-256: `3fdbdb41b910c3d98d85051230ed0a17aff37915bb73f3b730782ceba7e7c992`. `partial-primary-assessment.json` contains curator paraphrases of the inspected sections, not a raw experimental dataset.

## Priorities and handoff

1. Obtain the complete 21-page version of record and any supplementary files from a functioning public publisher or institutional route. Confirm version notes and record checksums.
2. Inspect every graph and Tables 1–2, matched controls, replicate definitions, incomplete digestion, stock-specific quantities, sampling corrections, peroxide conventions and the cobalt conversion discrepancy.
3. Resolve individual residue origins and culture accessions. If supported, create a narrowly scoped secondary-resource record with canonical history linked to issue 93 and independent exact-state scientific review. Do not merge these feeds into elemental nickel/cobalt records or assume the whole residue is on a criticality list.

## Limits and unresolved questions

This is a bounded assessment of a strong previously known lead, not evidence of source exhaustion. No complete PDF, original figure image, supplementary inventory, raw replicate dataset or verified strain identifier was obtained. The study appears suitable for future curation, but claim-level acceptance remains deferred. Parent reports the unchanged-base checks passed (308 tests, 3 skipped; 165 records and 186 histories). Author checks for this source-only change cover JSON parsing, report structure, paired DOI and local links; they are not record validation or scientific acceptance.
