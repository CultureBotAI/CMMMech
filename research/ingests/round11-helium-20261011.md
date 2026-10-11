# Round 11 helium evidence assessment

Accepted target: [Helium](../../data/records/helium.yaml), `cmmmech:helium`,
`material_kind: element`. This is an identity-and-dated-designation record;
**no microbial mechanism is accepted**. It is not a claim that all possible
biological interactions with helium have been excluded. Acceptance is tracked
in [issue 44](https://github.com/CultureBotAI/CMMMech/issues/44).

## Identity, authority and conceptual boundaries

Live [ChEBI:30217](https://www.ebi.ac.uk/chebi/CHEBI:30217) identifies
**helium atom**, formula He, charge zero. Its helium-3 and helium-4 children
are isotope-specific entities, not alternative identifiers for this element
record. No grade, gas reservoir or isotope-specific identifier is borrowed.

The [original Regulation (EU) 2024/1252](https://eur-lex.europa.eu/eli/reg/2024/1252/oj/eng),
11 April 2024, published 3 May 2024, **Annex II Section 1(p)** directly lists
helium among critical raw materials. The curated jurisdiction is the European
Union and the edition is this original act. This does not establish current
status in every jurisdiction or designate every helium-bearing resource.
No `not_listed` claim is made about any other list.

[USGS Mineral Commodity Summaries 2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf),
**printed pp. 96–97 / PDF pp. 100–101**, was re-read as retained primary
commodity context, including page images. It distinguishes commercial helium
grades, helium-3 production and geological gas resources. These distinctions
support record boundaries; the production statistics are not imported as
microbial evidence or native concentration observations. The rare-gas air
separation paragraph is not transferred wholesale to helium.

## Search and evidence decisions

The accompanying [JSON receipt](round11-helium-20261011.json) records exact
queries and acquisition hashes. Web searches used the listed literal queries,
no date restriction, and selected returned leads; there was no exhaustive
pagination or literature census. The initial authority-oriented result set was
not separately retained; later provider result strings are retained outside Git.

| Lead | Inspection and decision |
|---|---|
| [DOE, In Situ Air Stripping Using Horizontal Wells, April 1995, OSTI 7093](https://www.osti.gov/servlets/purl/7093) | Full 31-page scan acquired; title, setup at PDF p. 8, performance at PDF p. 11/printed p. 7, and analytical context at PDF p. 26 checked. The performance page was visually inspected. Helium is an inert tracer of injected-gas communication; the separately discussed microbial activity concerns contaminant removal. The plotted helium recovery is not microbial helium extraction. Excluded as a helium mechanism. |
| [NASA CR-140806](https://ntrs.nasa.gov/api/citations/19750002635/downloads/19750002635.pdf) and [Schneider et al. 2011](https://arxiv.org/abs/1105.2207) | Returned excerpts/abstract describe helium plasma sterilization or separation of plasma components. Microbial recovery means organism survival/counting in the NASA context. Scope mismatch; no methods or measurements imported. |
| [LLNL/Ames microbe-bead research news](https://www.ameslab.gov/news/llnl-researchers-turn-microbe-beads-increase-us-supply-rare-earth-metals) | Helium ion microscopy occurs in image captions; the recovery target is rare earth material. Discovery-only scope exclusion, not primary mechanism evidence. |
| [Kryachko and Voordouw 2014](https://doi.org/10.1016/j.ibiod.2014.08.013) | Returned abstract concerns oil recovery with gas/pressure context, not verified microbial helium recovery. Full methods not admitted. |
| [Gakkel Ridge plume study, 2024](https://doi.org/10.3389/fmicb.2024.1473822) | Returned abstract/excerpt compares microbial hydrogen/methane processes with helium isotope tracing. Deferred context lead; no helium metabolic claim or numerical result imported. |
| [Fu et al. 2025](https://doi.org/10.1021/acs.iecr.4c02843) and [2022 direct helium recovery repository manuscript](https://api.research-repository.uwa.edu.au/ws/portalfiles/portal/189408049/May_et_al._2022_Direct_helium_recovery.pdf) | Pressure-swing gas separation leads, not demonstrated microbial mechanisms. Full method review for a separately scoped abiotic process remains possible; no performance claims imported here. |

Local novelty checks used `rg --no-ignore --hidden --follow` over
`data/records`, `research`, `reviews`, `history` and `.claude`, searching helium
and its ChEBI identity. The 23 returned lines were authority/frontier proposals,
not an existing accepted helium record. The named roots had no symbolic links
in the inspected inventory. Cited raw-source checks covered text/HTML/JSON/Markdown
under `/private/tmp/cmm-next-eu` and
`/private/tmp/cmm-expansion-authorities-20261011`, including hidden/ignored files
and following relevant links (39 matching lines). The retained USGS PDF was
separately read and rehashed. These are bounded searches, not machine-wide
absence claims or a claim that unconverted binary text was searched by ripgrep.

## Provenance, limits and follow-up

Successful live acquisitions: ChEBI, EUR-Lex and OSTI on 11 October 2026. The
USGS PDF was already retained from round 9 and was **reinspected, not freshly
downloaded**. Hashes and exact local paths are in the JSON receipt. Full text,
page renders and raw provider results stay outside Git. USGS/DOE government
materials are retained as public research context; ChEBI, EUR-Lex and publisher
content retain their source terms. No redistribution license is inferred for
third-party papers or provider excerpts.

No journal mechanism claim is accepted, so this record has no journal-specific
correction/retraction conclusion. The original legal edition is explicit;
this review does not certify all subsequent amendments or all current lists.
Further helium work should assess a specifically evidenced process, distinguish
feed gas from product and verify full methods before adding a mechanism.

Canonical CREATE history was produced with `just new-history` using the actual
codex / GPT-6 / codex actor, with its own inline event. The helper's first attempt
before the target file existed failed without a sidecar; the subsequent call
succeeded. Independent review and final batch gates are recorded separately.
