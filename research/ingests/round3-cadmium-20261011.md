# Cadmium curation dossier

Prepared 2026-10-11 UTC by Codex (GPT-6), delegated cadmium curator, against
`5892e9a0aca54ef3f45d2ce87a6dcfb80d1569da` in the round3 worktree. This dossier
supports `data/records/cadmium.yaml`; it is not its independent acceptance review.
Download receipts and previous-artifact provenance are in the adjacent JSON.

## Selection, identity and dated designation

Cadmium extends the earlier authority inventory with an element whose microbial
solid product has direct spectroscopy evidence. The chosen experiment supports
a deliberately limited immobilization claim. More ambitious recovery claims
would require additional controls and product accounting.

The ChEBI authority resolves `CHEBI:22977` to cadmium atom, formula Cd, net
charge zero. It identifies the element, not dissolved Cd(II), CdCl2, CdS, a
mineral species, or a waste stream. NCBI575 currently has the species label
*Klebsiella planticola* and lists *Raoultella planticola* as a homotypic synonym.
The record uses this species mapping and does not invent an exact strain ID.

The official Ministry of Mines PDF was previously acquired on 2026-10-11;
this pass rehashed the same 52-page artifact and independently read PDF pages
1,11,40. Page40 was rendered and visually checked: Chapter9, printed page32,
item4 is Cadmium. The launch notice independently dates release to28June2023.
This is the June2023 committee's final30-material list, not an assertion about
the separately constituted statutory24-material schedule or the latest law.
No criticality is inherited by the experimental compounds.

## Primary scientific evidence checked

[Sharma et al.2000](https://doi.org/10.1128/AEM.66.7.3083-3087.2000),
Applied and Environmental Microbiology66:3083-3087, PMID10877810, PMC92115.
The publisher main text was read in full through the web tool, including growth
medium, transformation, comparisons, conclusions, accession declarations and
references. Figures2-3 were separately downloaded and visually inspected.
Their acquisition hashes are retained; no raw figure is committed.

The accepted record preserves the Cd-1 culture, anaerobic salt-medium context,
late-stationary biomass, two spectroscopic methods and the separately amended
sulfide assay. Figure2 shows the Cd-containing biomass fit against CdS and
cadmium-free biomass spectra. Figure3 retains both sulfur and oxygen ligand
contributions. These comparisons support the narrow solid-associated claim;
they do not justify phase-pure CdS, a specific mineral polymorph, enzymatic
causality, cellular localization, complete capture, or recovery yield.

The methylene-blue result has a sulfide basis. Washing addresses the reported
thiosulfate interference but does not itself prove a complete cadmium mass
balance. The record keeps the primary paper's uncertainty and missing matched
cell-free comparison explicit. Its general growth tests, species comparisons,
and inoculum conditions must not silently supply missing timing or temperature
for the characterized precipitation samples. The assay concentrations remain
prose because the current observation schema requires source cells in mg/kg.

The publisher declares an ATCC accession with questionable formatting and a
16S accession AF175281. NCBI nucleotide access failed in this pass; neither is
promoted to a verified strain identifier. The source's cross-study superiority
claims are not adopted. Environmental origin and suggested applications are
not industrial deployment evidence.

## Search, duplicate and access coverage

Local search used `rg --no-ignore --hidden` within records, research, reviews
and history, matching `cadmium`, `22977`, `3083-3087.2000` and `PMC92115` across
YAML, Markdown and JSON. Before this addition it found the authority inventory
and remaining-priority mentions, with no existing cadmium record or selected
study in those files. Ignored and hidden files were included. The cited India
download and this task's evidence directory were inspected; unrelated home and
temporary trees are outside the duplicate claim. An overbroad temporary-tree
instruction search was interrupted and is not absence evidence.

Live web searches on2026-10-11 used these exact queries, first returned result
sets without complete pagination, followed by the relevant primary sources:

1. `cadmium biosorption dead bacterial biomass controls open access cadmium precipitation primary study microbial`
2. `cadmium microbial sulfide precipitation control cadmium recovery full text PMC`
3. `site.ebi.ac.uk/chebi "cadmium atom"`
4. `"A New Klebsiella planticola Strain" "doi"`
5. `"A New Klebsiella planticola Strain" "correction" OR "retraction"`
6. `"Klebsiella planticola" "Cd-1" cadmium contradictory precipitation`
7. `"10.1128/AEM.66.7.3083-3087.2000" correction retraction`
8. `"Klebsiella" "Cd-1" "abiotic" cadmium`
9. `"AF175281" "Cd-1"`

No affecting correction/retraction was identified in the returned relevant
results or inspected publisher text. This is a bounded check, not an exhaustive
absence claim. Publisher-page searches found no supplementary-material label
or correction label in the returned main-text representation; no nonexistent
supplement is claimed to have been checked. The main text's control limitations
are preserved instead of fabricating a separate refutation.

PMC main pages challenged; EuropePMC XML requests for PMC92115 and the separate
engineering lead PMC92330 returned HTTP500. EuropePMC article view was
unavailable. An initially guessed ASM DOI was inaccessible and was discarded;
the correct DOI was verified at the publisher. The correct publisher full text
was available through the web tool, but an ordinary local HTML request was403.
Its linked PDF route failed through the web tool. Figure downloads succeeded
and were recognized as images. All local successes/failures are in the JSON.

## Deferred leads and follow-up

- [Pagnanelli et al.2010](https://doi.org/10.1016/j.biortech.2009.12.009):
  source distinguishes SRB biosorption and precipitation. Only the publisher
  abstract/preview was inspected; full methods and assays are needed before
  adding a second mechanism.
- [Live/dead rhizobacterial biomass study2018](https://doi.org/10.1039/C8RA06758A):
  search returned a primary full-text route. Inspect biomass treatment, blank
  controls, taxonomy accessions, capacities and competing explanations before
  curation; no claims from it enter this record.
- PMC92330, engineered sulfate-reduction pathway: useful alternative lead but
  XML access failed. No uninspected performance or expression data are adopted.

Independent review should challenge the distinction between spectroscopy and
the separate sulfide-assay condition, the assay basis, missing matched abiotic
comparison, species versus strain resolution, and historical list scope.
No schema change is demonstrated by this record.

## Curation state

Canonical CREATE sidecar:
`history/records/cadmium/2026-10-11T043443Z-codex-9ca538.yaml`.
The record contains a distinct inline CREATE event and the sidecar reference.
Independent scientific review and batch acceptance remain the parent workflow's
responsibility; this dossier does not claim they have already passed.
