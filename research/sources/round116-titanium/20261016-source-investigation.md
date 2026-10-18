# Titanite and lorenzenite source investigation

Investigated 16 October 2026 by codex (GPT-6), starting from trusted base
`5d3c48e255705e269096c43cf1c5508a5178ecc1` in the round116 worktree.
This dossier is a discovery/curation handoff; independent saved reviews assess
the final owners. Raw papers and acquisition/search receipts remain outside Git
under `/private/tmp/cmm-round116-titanium-research`.

## Identity, selection and deduplication

Titanite follows the explicit round115 recovery-source handoff. Lorenzenite
adds a distinct sodium titanium silicate with a complete primary natural-crystal
study. Both are mineral species, not elemental titanium, commodities or the
mixed feeds used in processing studies. No constituent criticality is inherited.

At 09:16:04 UTC, `rg --hidden --no-ignore --follow` searched titanite, sphene,
lorenzenite, ramsayite, AM72_173 and the two Gerasimova DOIs across the worktree's
records, research, reviews and history, original-main reports and the referenced
round115 recovery downloads. The 162 matching lines are retained in `dedup.txt`
(SHA256 `f9e58c412d962b179bac9ba9019b37c922f12d46e5938c4f7597960751cc2973`).
The two maintained-record matches are contextual titanite mentions in whewellite
and weddellite; their microbial oxalate observations do not establish microbial
titanite processing. Research/review matches include that context and the
explicit round115 titanite lead. No duplicate species owner was found within
these hidden/ignored-inclusive boundaries; this is not a machine-wide claim.

## Sources actually inspected

| Source | Access and inspected evidence | Disposition |
|---|---|---|
| [IMA-CNMNC September2026 list](https://cnmnc.units.it/files/editor/IMA_Master_List_(2026-09).pdf) | Fresh shared acquisition09:15:29–31 UTC and current official landing09:18:07 UTC by the borate investigator; root independently rendered/read page1 definitions, page128 lorenzenite and page218 titanite | Titanite is A, `1967 s.p.`, CaTiO(SiO4); lorenzenite is G,1901, Na2Ti2O3(Si2O6). No fabricated numbered approval IDs |
| [Gerasimova et al.2020](https://doi.org/10.3390/ma13071599) | Complete11-page original from MDPI CDN acquired during round115 at07:57:54 UTC; reused with verified hash. Complete text read; pp.3–9 rendered and visually inspected, including Figures3–9 and Tables2–4. Fresh Crossref metadata obtained09:20:50 UTC | Accept bounded hot-HCl decomposition observation for titanite-rich mixed concentrate. Preserve unclear grinding/feed sequence, two-versus-three-hour cleaning, and inconsistent analytical attribution |
| [Gerasimova et al.2018](https://doi.org/10.3390/min8100446) | Complete13-page original reused from round115; text inspected and relevant pages rendered, but root did not complete visual assessment of those figures in this round | Sulfuric route remains a research lead; no accepted2018 mechanism or numeric yield. Freshly mined rock, not automatically the2020 flotation-tail feed |
| [Sundberg et al.1987](https://msaweb.org/AmMin/AM72/AM72_173.pdf) | Complete5-page original freshly acquired09:20:50 UTC; all text and all page images inspected. Specimen/methods173–174, Tables1/3/5/6, Figures1/2 | Natural lorenzenite identity/structure; ramsayite synonym. Earlier specimen chemistry is not a fresh1987 assay |
| [AM-87-325 deposit](https://msaweb.org/MSA/AmMin/Supplemental_Data/Vol%2072%20p0173%20AM-87-325.pdf) | Actual linked target located on publisher supplementary index. Web fetch406 and direct download403 at09:23:10 UTC | Tables2/4 were not acquired; no re-refinement, raw-factor audit or complete supplementary-data inspection claimed |

Verified retained originals:

| File | Bytes | SHA256 |
|---|---:|---|
| `titanite2020.pdf` in round115 recovery raw directory | 2764878 | `31bfa918b0d1c4b7c2abbb3f8b5803875a939c1f4445a7bff4c8e3768cde50ed` |
| `titanite2018.pdf` in round115 recovery raw directory | 6383096 | `066dc1380b7b360203a1db2dfdde96fccfd6b8ea57051b847650c6e50bb7abfc` |
| `lorenzenite1987.pdf` | 373983 | `dba8bd734a9497788562e1127cb74354ed54ea71f89a9d579c926cbd7c29222a` |
| Shared fresh `ima2026-09.pdf` in round116 borates raw directory | See acquisition02.json | `2257c653491b346669ee5d38c98226a2bddbec0562a3675043730a01ca146973` |

The2020 and2018 originals state CC-BY4.0. Publisher-hosted lorenzenite access
does not establish a redistribution license. No copyrighted full text is committed.

## Adversarial scientific boundaries

The2020 study's Figure5 supports a TiO2-bearing DTK product; neither that pattern
nor Table2 composition supplies a full extraction mass balance. Approximately90%
Ti/Si extraction, fivefold improvement, waste-free processing and product-cost
claims are not accepted. The experimental charge scale and replication are
unreported. Dilute-HCl resistance and hot concentrated-HCl decomposition concern
different conditions. Pilot pigment production is reported separately and does
not establish deployment of the acid decomposition mechanism. Figure9's nm axis
conflicts with micrometre prose; no size distribution is adopted.

For lorenzenite, 778 selected/1167 measured independent reflections and R=0.026
come from the actual1987 study. Figure1/2 and Tables5/6 support the qualitative
coordination model, not a newly performed refinement. Visual inspection resolves
OCR errors: the single-crystal c parameter is14.487(2)angstrom, not14.481; no
lattice-parameter value is required in the owner. The original chemistry and
historical zirconium discrepancy are cited prior work. Identity-only scope needs
no invented processing mechanism.

## Live searches and unresolved leads

Retained web batches `r116web1.json` through `r116web6.json` document searches,
returned primary/secondary leads and access failures. Queries included exact
Gerasimova DOIs with correction/retraction; lorenzenite/ramsayite title and
Sundberg with correction/erratum; `AM-87-325`; and titanite microbial/bioleaching
dissolution. The bounded results did not establish a correction or retraction
of the accepted papers. This is not proof that no notice exists.

The microbial query returned [Izawa et al.2019](https://doi.org/10.3389/feart.2019.00315)
and the opposing biogenicity interpretation in
[Grosch and McLoughlin2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4060710/).
These are geological texture interpretations, not verified strain-specific
titanite extraction experiments. Their full methods and competing interpretations
need dedicated review before any microbial mechanism is curated. Accessory
titanite in a polymetallic bioleaching feed also does not establish its dissolution.

Further primary leads are the2011 mechanical-activation leaching paper
[10.1016/j.hydromet.2011.04.011](https://doi.org/10.1016/j.hydromet.2011.04.011),
the2019 hydrochloric route
[10.3390/min9050315](https://doi.org/10.3390/min9050315), and the2020 natural
metamict-titanite durability study
[10.1080/00223131.2020.1724205](https://doi.org/10.1080/00223131.2020.1724205).
They were not accepted from snippets. Prioritize full methods, source-specific
feed identity, analytical controls and SI before comparing yields. The next
source task is to reconcile the2020 feed/preparation and mass-balance ambiguities,
and obtain AM-87-325 through a functioning legitimate publisher route.
