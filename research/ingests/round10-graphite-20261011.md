# Natural graphite: commodity acceptance and neighbouring scopes

Prepared on 2026-10-11 UTC by codex / GPT-6 / codex against trusted base
`6ea63a8c98e22fd3c6794b17c77f7909c3b851a2`. This assessment advances the
[round9 handoff](round9-graphite-handoff-20261011.md). The
[machine-readable receipt](round10-graphite-20261011.json) records searches,
acquisitions, retained-input hashes and their inspection boundaries.

## Accepted identity and designation

The new [natural-graphite record](../../data/records/natural-graphite.yaml)
denotes an origin-defined **commodity**. The inspected USGS *Mineral Commodity
Summaries 2026*, printed pp. 92–93 / PDF pp. 96–97, distinguishes commercial
natural-graphite forms and synthetic substitutes. Both pages were checked as
text and rendered images. This supports the natural/synthetic distinction but
does not turn each commercial form into a mineral species or establish a
universal battery-purity threshold. No carbon, graphite-mineral or unverified
commodity identifier is asserted.

A live check of the [older BGS landing page](https://nora.nerc.ac.uk/id/eprint/538471/)
identified OR/24/047 as superseded. Its note names OR/24/057, but the linked
[replacement landing page](https://nora.nerc.ac.uk/id/eprint/539735/) and acquired
[PDF](https://nora.nerc.ac.uk/id/eprint/539735/1/OR24059.pdf) both identify
**OR/24/059**. Use that inspected document identity. Table 1 (printed p. vii;
PDF p. 11) and Table 11 (printed p. 44; PDF p. 48) retain natural graphite in
the 2024 assessment. Both tables were visually checked. The cover says this
report does not constitute government policy; the record retains that limit.
This is a designation from the named 2024 assessment, not a claim about every
subsequent UK policy. The PDF contains 313 pages, although its internal
bibliographical reference says 235pp.; no total-page claim is copied to the
record. The earlier handoff remains a historical observation of OR/24/047.

## Explicit boundary decisions

The bounded decision set consists of the inventory proposals `graphite`,
`natural-graphite` and `graphite-battery-grade`, plus the newly accepted
natural-graphite record. It does not include a graphite mineral species or the
carbon element. The original
[EU Regulation 2024/1252](https://eur-lex.europa.eu/eli/reg/2024/1252/oj)
was checked at Annex II(v), Annex I(k) and Article 3(3). Its broad critical
graphite entry and strategic battery-grade entry are distinct, and the text
explicitly discusses synthetic graphite in the strategic scope.

| Candidate | Decision in this batch | Reason and next acceptance requirement |
|---|---|---|
| `natural-graphite` | Retain as a commodity record | Natural origin has an explicit commercial and assessment boundary; no microbial mechanism is required to support that identity. |
| `graphite` | Defer separate root; do not mark represented by natural graphite | A broad commodity can include synthetic material. A future record must explicitly define that breadth and its relation to the narrower natural commodity; it must not reuse a mineral or element ID as a commodity ID. |
| `graphite-battery-grade` | Defer separate root; do not lump with natural graphite | Product suitability and origin are different axes. A future record needs a source-defined product scope and assessment of any claimed performance or specification, without inventing a universal purity cut-off. |

These are retain/defer decisions, **not a disjoint partition** of graphite
materials: the proposed broad and qualified scopes overlap. They do not assert
that additional records are impossible or that the source inventory has been
exhausted. A separate independent category review will assess this boundary
decision together with the final record bytes.

## Microbial evidence and rejected extrapolations

The retained primary [Langwaldt and Kalapudas 2007 PDF](https://www.journalssystem.com/ppmp/pdf-79310-15375?filename=Bio-beneficiation-of-mult.pdf)
was rechecked, including methods, results, Table 6 and Figure 2. Its target was
sulfide concentration from Talvivaara black shale; graphite was an unwanted
co-floating component. Freeze-dried bacterial preparations were used in a
4-litre flotation cell. The authors report no substantial recovery/grade
improvement. Table 6's combined graphite/minerals fraction is not pure graphite
or a graphite recovery yield. This does not establish microbial purification
of the natural-graphite commodity. The PDF authorship is retained; the older
journal metadata discrepancy remains documented in round9. No strain identity
or numerical process performance is imported into this record.

Two additional primary leads concern spent batteries, whose graphite origin
must be established independently before mapping them to natural graphite:

- [Roy et al. 2023, DOI 10.1021/acssuschemeng.2c07262](https://pubs.acs.org/doi/10.1021/acssuschemeng.2c07262): publisher metadata and abstract describe regeneration of bioleaching residue with subsequent acid cleaning and calcination. The accessible publisher view exposes abstract and supplement metadata, not verified complete methods. A direct request returned HTTP 403; bounded institutional-repository/title searches did not retrieve a usable author manuscript. Keep this as a full-text acquisition priority for a spent-graphite or broader graphite scope. No reported purity, capacity or recovery figure is accepted from the abstract.
- [Roy et al. 2026, DOI 10.1016/j.cej.2026.181229](https://www.sciencedirect.com/science/article/pii/S1385894726086912): the publisher search view describes mixed-black-mass bioleaching followed by chemical/thermal graphite treatment. It displays a 1 November 2026 issue date, later than this assessment; online publication timing was not resolved. Direct acquisition returned HTTP 403. This remains an uncurated lead, with neither detailed measurements nor a natural-origin claim accepted.

A copper-bioleaching paper in which graphite is an additive
([DOI 10.3390/min10010079](https://doi.org/10.3390/min10010079)) and studies of
graphite-production wastewater were screened as different scientific questions.
They are not evidence of graphite extraction. No microbial graphite mechanism
is accepted in this batch; this is an evidence decision, not a claim that no
such process exists.

## Search, access and reuse limits

The exact web queries and bounded provider coverage are in the JSON. Searches
included purification/bioleaching, primary titles, correction/retraction terms,
and institutional manuscript routes. The returned correction searches did not
identify a matching notice; this is not an exhaustive integrity audit. An
initial unverified ACS URL did not resolve and is recorded as a rejected route,
not a citation. The correct DOI above was subsequently resolved by exact-title
search at the publisher.

The local search included hidden and ignored files and followed symlinks across
`data/records`, `research`, `reviews`, `history` and `.claude`; all 118 initial
matching lines were read. These roots contained no symlinks at the check. The
raw-artifact boundary was the cited round9 graphite directory and this round's
graphite directory, with file names and hashes inventoried. No machine-wide
absence claim is made. The new record is the first `commodity`-kind record in
this checkout as enumerated at the trusted base; other inventory proposals are
research, not pre-existing accepted records.

USGS landing-page fetching failed through the web tool; the retained primary
2026 PDF was inspected and rehashed. The UK replacement PDF and both landing
pages were freshly acquired. EU original-act text was checked through the live
official source and the retained acquisition. No claim is made to have audited
all consolidated amendments. UKRI's PDF limits copying/adaptation and permits
reasonable acknowledged extracts; the primary PDF remains outside Git.
Publisher full-text access and redistribution rights are not inferred from
abstract access. Only original curation, citation metadata and receipts are
committed, with the external raw literature retained locally.

Individual validation and actual CREATE history accompany the new record.
Final batch gates, independent record/category reviews and publication receipts
are reported separately after execution; this dossier does not pre-assert them.
