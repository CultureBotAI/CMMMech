# Theisen sludge source investigation

## Scope and provenance

UTC: 2026-10-12T01:57:42.900719+00:00; researcher: Codex / root. Base `a5528a4807ba14fd8088a557ad105ac10ca62965` on `curate/cmm-expansion-round42-20261012`. Other curators are preparing birnessite, hardmetal and lithium-mineral work; this investigation changes no accepted record. It follows the local source-discovery and add-record skills.

The question was whether germanium-bearing mineral or secondary-resource evidence could support a distinct owner. Theisen sludge is the promising secondary-resource lead. Its copper-shale-smelter origin distinguishes it from a mineral species, generic steel blast-furnace dust and copper slag. These are provisional identity boundaries for subsequent curation, not an accepted material record. Criticality lists and industrial deployment were not assessed.

## Search and acquisition

The [machine-readable manifest](20261012T015742Z-source-investigation.json) preserves the exact 14 queries, actual acquisition timestamps/checksums, returned-result limits and deduplication commands. Searches used web.run on 2026-10-12 without date filters; site constraints occur explicitly in two queries. Metadata routes were Crossref, OpenAlex, PubMed, the UFZ institutional publication page, Wiley and Oxford Academic. These related representations are one study, not independent evidence.

Ordinary downloads of Crossref, OpenAlex and [UFZ's publication record](https://www.ufz.de/index.php?en=20939&pub_id=17391) succeeded. ResearchGate and Wiley direct requests returned 403. Indexed author-uploaded text was visible, but its complete original PDF was not acquired. Wiley's linked supplementary DOCX also returned 403. UFZ's shareable link reached a JavaScript/robot-verification page; no challenge was bypassed. The current [Oxford Academic article](https://academic.oup.com/jambio/article/120/6/1520/6717229) and its supplementary-data entry both resolved to the publisher's purchase/abstract view. No unchanged denied endpoint was repeatedly retried.

## Candidate inventory and assessment

| Candidate | Verified identity / role | Evidence inspected | Decision |
|---|---|---|---|
| Klink, Eisen, Daus, Heim, Schlömann and Schopf, 2016 | DOI [10.1111/jam.13142](https://doi.org/10.1111/jam.13142); *Journal of Applied Microbiology* 120(6):1520–1530; PMID 27005888; primary bioleaching candidate | Publisher/institutional bibliographic records, abstract, partial indexed author text; no complete original graphics or SI | Defer all mechanism/quantity curation |
| Klink et al., 2015 | DOI [10.4028/www.scientific.net/AMR.1130.321](https://doi.org/10.4028/www.scientific.net/AMR.1130.321); potential companion experiment | Publisher metadata and indexed excerpts | Resolve study overlap before counting independent evidence |
| Eisen et al., 2016 poster | [Author-hosted conference item](https://www.researchgate.net/publication/306105080_Preliminary_Studies_on_Mineral_Specific_Bioleaching_of_Theisen_Sludge) | Indexed text only | Acquire original poster and distinguish its experiment |
| Lehmann, Daus and Reemtsma, 2019 | DOI [10.1016/j.chroma.2019.01.061](https://doi.org/10.1016/j.chroma.2019.01.061); analytical germanium speciation | Bibliographic lead only | Later follow-up; does not establish the main bioleaching result |

The main study concerns acidophilic cultures and laboratory flask/reactor treatments. The next curator must check its Table 1 feed characterization, Table 2 solution measurements, Figures 1–3, and supplementary Table S1/Figures S1–S9 against the actual methods. Do not import abstract percentages or fold changes without the loading, sampling and denominator basis. The reported GenBank KU569322 accession remains unverified in this pass and is not an accepted taxon/strain mapping. Dissolved-metal outcomes do not establish separated-product recovery.

Version dates differ: Wiley labels 23 March 2016 as “First published”; Crossref gives `published-online` as 25 April 2016; Oxford displays 1 June 2016 with the June issue. These receipts do not establish which date corresponds to an accepted manuscript or another manuscript version. Preserve the provider labels and leave their version relationship unresolved instead of treating them as separate studies. Independent review finding `CMMMech.theisen.source-version-date` is tracked in [issue #139](https://github.com/CultureBotAI/CMMMech/issues/139). The source carries 2016 Society for Applied Microbiology copyright; redistribution permission was not established. Raw acquired files remain outside Git. There is no downloaded experimental dataset or data dictionary to assess.

The exact-DOI correction/retraction and topic contradiction searches found related primary leads in the returned sets, but did not establish any specific formal notice. Crossref's retrieved relationship fields contain no update relation. This bounded observation does not certify absence of notices or conflicting results. Organic-compound inhibition and differences between flask and reactor conditions require direct primary assessment; secondary discussion is insufficient.

## Deduplication and limits

`rg --no-ignore --hidden --follow` searched current and original checkouts' data, research, reviews and history, then 133 available cited raw roots. The scientific-tree search had no matches for Theisen/its queried DOIs or the two germanium-mineral names at that observation time. Existing raw text hits concerned germanite/renierite authority lists. The manifest explicitly lists nine missing referenced raw directories. Unextracted binary/PDF-image text was not proven absent; this is not a machine-wide search. No duplicate Theisen owner was identified in the complete current corpus, but an unavailable download cannot be ruled out.

## Priorities and handoff

1. Obtain the full 2016 primary and relevant original graphics/SI through a legitimate institutional or author route; preserve version, URL and hashes. Do not contact an author without authorization to send that message.
2. Confirm the sludge identity and provenance, culture membership and strain accession, pretreatment, control viability, pH/temperature/loading, sampling, replication, dissolved versus solid accounting and contradictions. Reconcile indexed provenance/date discrepancies against originals.
3. Compare the 2015 report and 2016 poster for shared experiments. Review speciation/downstream studies separately; do not combine different feeds or laboratory stages into a recovery claim.
4. If evidence supports curation, create a `secondary_resource` owner with scoped sources/mechanisms, canonical CREATE history and independent scientific review. Otherwise retain this research deferral. No schema change is demonstrated.

No record validation is claimed for this source-only dossier. Germanite and renierite remain uncurated discovery leads; their identity and microbial evidence were not fully assessed. The source frontier is open.
