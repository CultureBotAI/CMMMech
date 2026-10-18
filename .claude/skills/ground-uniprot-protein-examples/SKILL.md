---
name: ground-uniprot-protein-examples
description: "Review CMMMech material records, construct causal graphs with GENE_OR_PROTEIN nodes, and ground mechanisms and causal nodes to live-verified UniProtKB protein examples."
---

# Ground UniProt Protein Examples in CMMMech

Use this skill when reviewing or curating `data/records/*.yaml` in `CultureBotAI/CMMMech` to add `protein_examples` (`UniProtKB:...`) to microbial mechanisms (`mechanisms[].protein_examples`) and to `GENE_OR_PROTEIN` elements of causal graphs (`causal_graphs[].nodes[].protein_examples`).

## 1. Scope & Non-Hallucination Rules

1. **Never fabricate or guess a UniProtKB accession.** Every `UniProtKB:...` accession, `entry_name`, `protein_name`, `gene_symbol`, `entry_status` (`SWISS_PROT` or `TREMBL`), `target_organism`, `reference_proteome_id`, and family/domain cross-reference (`interpro_ids`, `pfam_ids`, `ncbifam_ids`, `ec_numbers`) must be retrieved from the live UniProt REST API before writing YAML.
2. **Never cite obsolete/deleted UniProtKB entries as active accessions.** If a paper or genome annotation cites a locus whose TrEMBL entry was subsequently deleted or demoted to UniParc (for example, *Pseudomonas putida* GB-1 `mopA` / `PputGB1_3353`, former `B0KJL7`, now `UPI000164C1D1`), either:
   - Set `protein_grounding_status: UNGROUNDED` on that strain-specific `GENE_OR_PROTEIN` node and document the UniParc / locus identifier in `description`, or
   - Ground to an active, live-verified congeneric or species-level ortholog (such as *P. putida* KT2440 `UniProtKB:Q88JT6`) with `target_organism` set to the ortholog's exact `NCBITaxon` ID and an explicit `annotation_note` explaining the strain/ortholog relationship.
3. **Only microbial mechanisms (`microbial: true`) may carry `protein_examples`.** Abiotic controls or purely chemical mechanisms (`microbial: false`) must not carry `protein_examples`.

## 2. Corpus Audit Workflow

Scan `data/records/*.yaml` to identify candidate records with microbial mechanisms (`microbial: true`) or explicit gene/protein evidence:

```bash
.venv/bin/python -c '
import glob, yaml
for p in sorted(glob.glob("data/records/*.yaml")):
    doc = yaml.safe_load(open(p))
    mechs = [m for m in doc.get("mechanisms", []) if m.get("microbial")]
    if mechs:
        print(p, [m["id"] for m in mechs], len(doc.get("causal_graphs", [])))
'
```

Prioritize records where mechanism descriptions, context, or evidence mention:
- **Enzymes & oxidoreductases**: e.g., membrane-bound PQQ-dependent glucose dehydrogenase (`gdh` / `gcd`), lanthanide-dependent methanol dehydrogenase (`xoxF`), urease (`ureA`, `ureB`, `ureC`), alkaline phosphatase (`phoA`), multicopper oxidases (`mnxG`, `mcoA`, `mopA`), mercuric reductase (`merA`), fumarate reductase (`fccA`), haloacid/haloacetate dehalogenases (`dehH1`, `dehH2`), lipoteichoic acid synthases (`ltaS1`, `ltaS2`, `yqgS`, `yvgJ`).
- **Electron-transfer cytochromes**: e.g., outer-membrane decaheme cytochromes (`mtrC`, `omcA`), inner-membrane/periplasmic cytochromes (`imcH`, `cbcL`, `cymA`), cytochrome maturation proteins (`ccmC`).
- **Transporters & metallophores**: e.g., phosphate-specific ABC transporter subunits (`pstS`, `pstC`), silicic acid transporters (`SIT1`, `SIT2`), periplasmic ferric-binding protein (`fbpA`), selective lanthanide-binding proteins (`lanM` / lanmodulin).
- **Biomineralization templates**: e.g., ice nucleation protein (`inaZ`), silaffin (`SIL1`).

## 3. Live UniProt REST API Verification

Query the UniProtKB REST API (`https://rest.uniprot.org/uniprotkb/search`) by organism taxon ID (`taxonomy_id`) and gene symbol, locus tag, or protein name:

```text
https://rest.uniprot.org/uniprotkb/search?query=(taxonomy_id:243231)+AND+(gene:imcH+OR+GSU3259)&fields=accession,id,reviewed,protein_name,gene_names,organism_name,organism_id,xref_proteomes,xref_interpro,xref_pfam,ec,xref_go&format=json&size=5
```

### Selection Priority Hierarchy
1. **`SWISS_PROT` (reviewed)** entry in the exact experimental strain or species (`entry_status: SWISS_PROT`).
2. **Reference Proteome `TREMBL` (unreviewed)** entry in the exact strain or species (`entry_status: TREMBL`, with `reference_proteome_id: UP...`).
3. **Strain-matched `TREMBL`** entry when no reference proteome exists for that taxon.
4. **Explicitly annotated congeneric/species reference-proteome ortholog** when the experimental strain lacks an active UniProtKB entry (always set `target_organism` to the UniProt entry's true `NCBITaxon` ID and explain the relationship in `annotation_note`).

## 4. Schema Structure for `CausalGraph` and `ProteinExample`

Conform strictly to `src/cmmmech/schema/cmmmech.yaml`:

### Mechanism-Level `protein_examples`
Attach `protein_examples` under each relevant `mechanisms[]` entry (between `organisms` and `evidence`):

```yaml
    protein_examples:
      - uniprot_accession: UniProtKB:P27175
        entry_name: DHG_GLUOX
        protein_name: Quinoprotein glucose dehydrogenase
        gene_symbol: gdh
        entry_status: SWISS_PROT
        target_organism:
          id: NCBITaxon:442
          label: Gluconobacter oxydans
        reference_proteome_id: UP000006375
        ec_numbers:
          - EC:1.1.5.2
        interpro_ids:
          - InterPro:IPR018391
          - InterPro:IPR017511
          - InterPro:IPR002372
          - InterPro:IPR011047
          - InterPro:IPR001479
        pfam_ids:
          - Pfam:PF01011
        functional_role: >-
          Membrane-bound PQQ-dependent glucose dehydrogenase (mGDH, locus GOX0265)
          that catalyzes periplasmic oxidation of D-glucose to D-gluconic acid,
          generating organic acid biolixiviants for mineral bioleaching.
        evidence:
          - source_ref: schmitz2021
            supports: support
            explanation: >-
              Deletion or disruption of membrane-bound glucose dehydrogenase
              abrogates gluconic acid production and rare-earth bioleaching.
```

### Record-Level `causal_graphs`
Add `causal_graphs` at the root of `CriticalMineralRecord` (after `mechanisms` and before `curation_history`). Each `CausalGraph` links molecular steps from genes/proteins to chemical intermediates and mineral transformations:

```yaml
causal_graphs:
  - id: pca_akaganeite_reduction_pathway
    name: ImcH/CbcL-dependent extracellular reduction of akaganeite in Geobacter sulfurreducens PCA
    description: >-
      Causal pathway linking inner-membrane multiheme c-type cytochromes ImcH
      and CbcL in Geobacter sulfurreducens PCA to extracellular electron transfer
      and reductive dissolution/transformation of akaganeite (beta-FeOOH).
    scope: RECORD_SPECIFIC_MECHANISM
    mechanism_ref: pca_akaganeite_reduction
    nodes:
      - id: imch_cytochrome
        label: Inner-membrane cytochrome ImcH (GSU3259)
        node_type: GENE_OR_PROTEIN
        description: >-
          High-potential inner-membrane multiheme c-type cytochrome required for
          reduction of high-redox-potential Fe(III) oxides including akaganeite.
        gene_symbol: imcH
        protein_grounding_status: GROUNDED
        protein_examples:
          - uniprot_accession: UniProtKB:Q747K6
            entry_name: IMCH_GEOSL
            protein_name: Cytochrome c-type protein ImcH
            gene_symbol: imcH
            entry_status: SWISS_PROT
            target_organism:
              id: NCBITaxon:243231
              label: Geobacter sulfurreducens PCA
            reference_proteome_id: UP000000577
            interpro_ids:
              - InterPro:IPR051174
              - InterPro:IPR036280
              - InterPro:IPR005126
              - InterPro:IPR038266
            pfam_ids:
              - Pfam:PF03264
            functional_role: >-
              Transfers electrons from the menaquinone pool across the inner
              membrane during reduction of akaganeite at high redox potential.
            evidence:
              - source_ref: levar_2017
                supports: support
                explanation: >-
                  Delta-imcH mutants fail to initiate akaganeite reduction unless
                  cbcL is also active after redox potential drops.
      - id: akaganeite_fe3_reduction
        label: Extracellular Fe(III) reduction of akaganeite
        node_type: BIOLOGICAL_PROCESS
        description: >-
          Microbial extracellular electron transfer to solid akaganeite
          (beta-FeOOH), generating Fe(II) and transforming the mineral phase.
        protein_grounding_status: NOT_APPLICABLE
    edges:
      - source: imch_cytochrome
        target: akaganeite_fe3_reduction
        predicate: reduces
        relationship: >-
          Transfers electrons from the menaquinone pool to initiate extracellular
          akaganeite reduction
        description: >-
          ImcH mediates electron transfer required to initiate extracellular
          akaganeite reduction.
        evidence:
          - source_ref: levar_2017
            supports: support
            explanation: >-
              Deleting imcH prevents akaganeite reduction until low-potential
              CbcL-dependent electron transfer can operate.
```

### Mandatory Validator Invariants

1. **`CausalNode` grounding status**:
   - `protein_grounding_status` is **required** on every `CausalNode`.
   - `GENE_OR_PROTEIN` nodes must use `GROUNDED` (with non-empty `protein_examples`) or `UNGROUNDED` (with zero `protein_examples` and a non-empty `description` explaining why the locus is ungrounded).
   - Non-`GENE_OR_PROTEIN` nodes (`CHEMICAL_ENTITY`, `BIOLOGICAL_PROCESS`, `CELLULAR_STRUCTURE`, `PHENOTYPE_OR_TRAIT`, `ENVIRONMENTAL_CONDITION`, `MATERIAL_OR_PHASE`) must use `protein_grounding_status: NOT_APPLICABLE` and must not carry `protein_examples` or `gene_symbol`.
2. **`ProteinExample` taxon alignment & CURIE syntax**:
   - `target_organism.id` must match `^NCBITaxon:[0-9]+$`.
   - Whenever `target_organism.id` on a mechanism-level `ProteinExample` or on a `CausalNode.protein_examples[]` entry (whose graph has a `mechanism_ref`) is not present in the parent mechanism's `organisms[].id` set (for example, strain-level vs species-level `NCBITaxon` or a reference-proteome ortholog), `annotation_note` is **required** on that `ProteinExample` to document the taxonomic/ortholog relationship.
   - `go_terms[].id` must match `^GO:[0-9]{7}$`.
   - Duplicate `uniprot_accession` entries within the same `protein_examples` list and duplicate cross-references (`interpro_ids`, `pfam_ids`, `ncbifam_ids`, `ec_numbers`, `go_terms`) within a single `ProteinExample` are forbidden.
3. **`CausalGraph` structural integrity**:
   - `CausalEdge.predicate` is constrained to `CausalPredicateEnum`: `acts_on`, `assembles_into`, `binds`, `catalyzes`, `chelates`, `displays_on_surface`, `drives`, `incorporates_into`, `inhibits`, `modulates`, `negatively_regulates`, `nucleates`, `oxidizes`, `positively_regulates`, `produces`, `provides_electrons_to`, `reduces`, `supplies_substrate_for`, `transforms_into`, `transports`.
   - Self-loop edges (`source == target`), duplicate `(source, target, predicate)` edges, and isolated nodes (not referenced by any edge in a multi-node graph) are forbidden.
   - A `CausalGraph` whose `mechanism_ref` points to an abiotic mechanism (`microbial: false`) cannot contain biological nodes (`GENE_OR_PROTEIN`, `BIOLOGICAL_PROCESS`, `CELLULAR_STRUCTURE`, `PHENOTYPE_OR_TRAIT`).
4. **Canonical root YAML key order**:
   - Keep top-level keys ordered as: `id`, `name`, `material_kind`, `description`, `identifiers`, `criticality`, `sources`, `mechanisms`, `causal_graphs`, `curation_history`, `history_refs`.

## 5. Provenance, Rendering, and Validation Gate

Every curated record must:
1. Include any newly referenced UniProt source entry in `sources` (with `id`, `title`, `url`, `accessed_on`).
2. Append an inline `curation_history` event (`action: EDIT`) and create an append-only history sidecar via `cmmmech new-history` (appending the returned `history/records/<slug>/...` path to `history_refs`).
3. Pass all repository checks and page rendering:

```bash
.venv/bin/python -m cmmmech validate --require-records
.venv/bin/python -m cmmmech validate-history --base HEAD
.venv/bin/python scripts/render_pages.py
.venv/bin/python scripts/render_pages.py --check
.venv/bin/python -m pytest tests/test_validation.py tests/test_skill_frontmatter.py tests/test_render_pages.py -q
.venv/bin/python -m ruff check src tests scripts
```
