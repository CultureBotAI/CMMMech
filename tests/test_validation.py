import copy

import pytest
import yaml

from cmmmech.validation import read_record, record_validator, validate_record


def test_valid_combined_record(record):
    assert validate_record(record) == []


def test_material_does_not_require_microbes(record):
    record.pop("mechanisms")
    record.pop("criticality")
    assert validate_record(record) == []


def test_primary_resource_supports_microbial_separation_without_criticality(record):
    record.update(
        id="cmmmech:synthetic-geothermal-brine",
        name="Synthetic geothermal brine fixture",
        material_kind="primary_resource",
        description="A synthetic example of a natural geological fluid feed.",
    )
    record.pop("criticality")
    record["mechanisms"][0].update(
        process="separation",
        description="Synthetic impurity removal, without isolated lithium recovery.",
        context="Hypothetical laboratory assay; this fixture is not scientific evidence.",
    )
    assert validate_record(record) == []
    record.pop("mechanisms")
    assert validate_record(record) == []
    record["material_kind"] = "primary-resource"
    assert any("material_kind" in error for error in validate_record(record))


def test_nonmicrobial_recovery_is_supported(record):
    mechanism = record["mechanisms"][0]
    mechanism["microbial"] = False
    mechanism.pop("organisms")
    mechanism["process"] = "recovery"
    assert validate_record(record) == []


@pytest.mark.parametrize("path,value", [
    (("unexpected",), "not allowed"),
    (("sources", 0, "unexpected"), "not allowed"),
    (("criticality", 0, "unexpected"), "not allowed"),
    (("mechanisms", 0, "evidence", 0, "unexpected"), "not allowed"),
    (("name",), "  "),
    (("id",), "wrong-namespace"),
    (("material_kind",), "unsupported"),
    (("sources",), []),
    (("sources", 0, "url"), "javascript:alert(1)"),
    (("sources", 0, "accessed_on"), "2026-02-30"),
    (("criticality", 0, "edition"), ""),
    (("criticality", 0, "classification"), "always"),
    (("mechanisms", 0, "context"), ""),
    (("mechanisms", 0, "microbial"), "true"),
    (("mechanisms", 0, "evidence"), []),
    (("mechanisms", 0, "evidence", 0, "supports"), "unverified-value"),
])
def test_schema_rejects_invalid_data(record, path, value):
    node = record
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    assert validate_record(record)


@pytest.mark.parametrize("field", ["id", "name", "material_kind", "description", "sources"])
def test_required_root_fields(record, field):
    record.pop(field)
    assert validate_record(record)


@pytest.mark.parametrize("section", ["sources", "mechanisms"])
def test_duplicate_nested_identifiers(record, section):
    record[section].append(copy.deepcopy(record[section][0]))
    assert any("duplicate id" in error for error in validate_record(record))


def test_unknown_criticality_source(record):
    record["criticality"][0]["source_ref"] = "missing"
    assert any("unknown source_ref" in error for error in validate_record(record))


def test_unknown_mechanism_source(record):
    record["mechanisms"][0]["evidence"][0]["source_ref"] = "missing"
    assert any("unknown source_ref" in error for error in validate_record(record))


def test_organisms_need_explicit_microbe_flag(record):
    record["mechanisms"][0]["microbial"] = False
    assert any("microbial: true" in error for error in validate_record(record))


@pytest.mark.parametrize("text", [
    "id: first\nid: second\n",
    "source:\n  id: first\n  id: second\n",
    "source: &source {id: first}\nother: {<<: *source, id: second}\n",
    "1: invalid-key\n",
    "!!python/object/apply:os.system ['false']\n",
])
def test_ambiguous_or_unsafe_yaml_is_rejected(tmp_path, text):
    path = tmp_path / "record.yaml"
    path.write_text(text)
    with pytest.raises(yaml.YAMLError):
        read_record(path)


@pytest.mark.parametrize("value", [None, [], "text", 1])
def test_non_record_documents(value):
    assert validate_record(value)


def test_schema_is_closed_and_packaged():
    assert record_validator().schema["additionalProperties"] is False


def _sample_protein_example():
    return {
        "uniprot_accession": "UniProtKB:P27175",
        "entry_name": "DHG_GLUOX",
        "protein_name": "Quinoprotein glucose dehydrogenase",
        "gene_symbol": "gdh",
        "entry_status": "SWISS_PROT",
        "target_organism": {"id": "NCBITaxon:442", "label": "Gluconobacter oxydans"},
        "reference_proteome_id": "UP000006375",
        "ec_numbers": ["EC:1.1.5.2"],
        "interpro_ids": ["InterPro:IPR018391"],
        "pfam_ids": ["Pfam:PF01011"],
        "functional_role": "Catalyzes periplasmic oxidation of D-glucose to D-gluconic acid.",
        "evidence": [
            {
                "source_ref": "fixture",
                "supports": "support",
                "explanation": "Synthetic test grounding.",
            }
        ],
    }


def _sample_causal_graph():
    return {
        "id": "test_causal_graph",
        "name": "Synthetic causal pathway",
        "description": "Synthetic causal graph for testing validation.",
        "scope": "RECORD_SPECIFIC_MECHANISM",
        "mechanism_ref": "test_mechanism",
        "nodes": [
            {
                "id": "gdh_enzyme",
                "label": "Membrane-bound glucose dehydrogenase (Gdh)",
                "node_type": "GENE_OR_PROTEIN",
                "gene_symbol": "gdh",
                "protein_grounding_status": "GROUNDED",
                "protein_examples": [_sample_protein_example()],
            },
            {
                "id": "gluconic_acid_production",
                "label": "Gluconic acid production",
                "node_type": "CHEMICAL_ENTITY",
                "protein_grounding_status": "NOT_APPLICABLE",
                "term": {"id": "CHEBI:33198", "label": "D-gluconic acid"},
            },
        ],
        "edges": [
            {
                "source": "gdh_enzyme",
                "target": "gluconic_acid_production",
                "predicate": "produces",
                "relationship": "provides_input_for",
                "description": "Gdh oxidizes glucose to gluconic acid.",
                "evidence": [
                    {
                        "source_ref": "fixture",
                        "supports": "support",
                        "explanation": "Synthetic edge evidence.",
                    }
                ],
            }
        ],
    }


def test_valid_causal_graphs_and_protein_examples(record):
    record["mechanisms"][0]["organisms"] = [
        {"id": "NCBITaxon:442", "label": "Gluconobacter oxydans"}
    ]
    record["mechanisms"][0]["protein_examples"] = [_sample_protein_example()]
    record["causal_graphs"] = [_sample_causal_graph()]
    assert validate_record(record) == []


def test_causal_graph_and_protein_example_integrity_checks(record):
    record["mechanisms"][0]["organisms"] = [
        {"id": "NCBITaxon:442", "label": "Gluconobacter oxydans"}
    ]
    record["mechanisms"][0]["protein_examples"] = [
        _sample_protein_example(),
        _sample_protein_example(),
    ]
    assert any("duplicate uniprot_accession" in e for e in validate_record(record))

    # Divergent target_organism requires annotation_note
    pe_divergent = _sample_protein_example()
    pe_divergent["target_organism"] = {"id": "NCBITaxon:83333", "label": "Escherichia coli K-12"}
    record["mechanisms"][0]["protein_examples"] = [pe_divergent]
    assert any("not in mechanism organisms requires annotation_note" in e for e in validate_record(record))
    pe_divergent["annotation_note"] = "Ortholog from reference proteome."
    assert validate_record(record) == []

    # Invalid target_organism CURIE prefix and invalid/duplicate GO terms or cross-references
    pe_bad_curie = _sample_protein_example()
    pe_bad_curie["target_organism"] = {"id": "CHEBI:12345", "label": "Not a taxon"}
    pe_bad_curie["go_terms"] = [
        {"id": "GO:0008150", "label": "biological_process"},
        {"id": "GO:0008150", "label": "biological_process"},
        {"id": "CHEBI:111", "label": "bad go term"},
    ]
    pe_bad_curie["pfam_ids"] = ["Pfam:PF01011", "Pfam:PF01011"]
    record["mechanisms"][0]["protein_examples"] = [pe_bad_curie]
    errs = validate_record(record)
    assert any("must be an NCBITaxon CURIE" in e for e in errs)
    assert any("duplicate GO term id" in e for e in errs)
    assert any("must be a 7-digit GO CURIE" in e for e in errs)
    assert any("pfam_ids: duplicate value" in e for e in errs)

    record["mechanisms"][0]["protein_examples"] = [_sample_protein_example()]
    record["mechanisms"][0]["microbial"] = False
    record["mechanisms"][0].pop("organisms")
    assert any("protein_examples require microbial: true" in e for e in validate_record(record))
    record["mechanisms"][0]["microbial"] = True
    record["mechanisms"][0]["organisms"] = [
        {"id": "NCBITaxon:442", "label": "Gluconobacter oxydans"}
    ]

    graph = _sample_causal_graph()
    graph["mechanism_ref"] = "nonexistent_mechanism"
    record["causal_graphs"] = [graph]
    assert any("unknown mechanism_ref" in e for e in validate_record(record))

    # Abiotic mechanism_ref with biological/GENE_OR_PROTEIN causal nodes is rejected
    abiotic_mech = copy.deepcopy(record["mechanisms"][0])
    abiotic_mech["id"] = "abiotic_control"
    abiotic_mech["microbial"] = False
    abiotic_mech.pop("organisms", None)
    abiotic_mech.pop("protein_examples", None)
    record["mechanisms"].append(abiotic_mech)
    graph = _sample_causal_graph()
    graph["mechanism_ref"] = "abiotic_control"
    record["causal_graphs"] = [graph]
    assert any(
        "biological or GENE_OR_PROTEIN nodes require microbial mechanism_ref" in e
        for e in validate_record(record)
    )
    record["mechanisms"].pop()

    graph = _sample_causal_graph()
    graph["edges"][0]["target"] = "missing_node"
    record["causal_graphs"] = [graph]
    assert any("unknown target node" in e for e in validate_record(record))

    # Self-loop and duplicate edge checks
    graph = _sample_causal_graph()
    graph["edges"].append(
        {
            "source": "gdh_enzyme",
            "target": "gdh_enzyme",
            "predicate": "modulates",
        }
    )
    graph["edges"].append(copy.deepcopy(graph["edges"][0]))
    record["causal_graphs"] = [graph]
    edge_errs = validate_record(record)
    assert any("self-loop edge on node gdh_enzyme" in e for e in edge_errs)
    assert any("duplicate edge gdh_enzyme -> gluconic_acid_production (produces)" in e for e in edge_errs)

    # Disconnected node check
    graph = _sample_causal_graph()
    graph["nodes"].append(
        {
            "id": "orphan_node",
            "label": "Orphan node",
            "node_type": "CHEMICAL_ENTITY",
            "protein_grounding_status": "NOT_APPLICABLE",
        }
    )
    record["causal_graphs"] = [graph]
    assert any("disconnected node orphan_node has no incident edges" in e for e in validate_record(record))

    graph = _sample_causal_graph()
    graph["nodes"][0]["protein_examples"] = []
    record["causal_graphs"] = [graph]
    assert any("GROUNDED node requires protein_examples" in e for e in validate_record(record))

    graph = _sample_causal_graph()
    graph["nodes"][0]["protein_grounding_status"] = "NOT_APPLICABLE"
    graph["nodes"][0]["protein_examples"] = []
    record["causal_graphs"] = [graph]
    assert any(
        "GENE_OR_PROTEIN node requires GROUNDED or UNGROUNDED protein_grounding_status" in e
        for e in validate_record(record)
    )

    graph = _sample_causal_graph()
    graph["nodes"][0]["protein_grounding_status"] = "UNGROUNDED"
    record["causal_graphs"] = [graph]
    errs = validate_record(record)
    assert any("UNGROUNDED node cannot have protein_examples" in e for e in errs)
    assert any("UNGROUNDED node requires description explaining ungrounded status" in e for e in errs)

    graph = _sample_causal_graph()
    graph["nodes"][1]["protein_grounding_status"] = "UNGROUNDED"
    graph["nodes"][1]["gene_symbol"] = "illegal_gene"
    graph["nodes"][1]["protein_examples"] = [_sample_protein_example()]
    record["causal_graphs"] = [graph]
    errs = validate_record(record)
    assert any(
        "non-GENE_OR_PROTEIN node requires NOT_APPLICABLE protein_grounding_status" in e
        for e in errs
    )
    assert any(
        "protein_examples are only permitted on GENE_OR_PROTEIN nodes" in e
        for e in errs
    )
    assert any(
        "gene_symbol is only permitted on GENE_OR_PROTEIN nodes" in e
        for e in errs
    )


def test_optional_ima_symbol_and_polymorph_or_grade_slots(record):
    record["ima_symbol"] = "Aka"
    record["polymorph_or_grade"] = "beta-FeOOH"
    assert validate_record(record) == []

    record["ima_symbol"] = "   "
    assert validate_record(record)
    record["ima_symbol"] = "Aka"
    record["polymorph_or_grade"] = ""
    assert validate_record(record)


@pytest.mark.parametrize(
    "predicate",
    ["solubilizes", "dissolves", "hydrolyzes", "degrades"],
)
def test_dissolution_and_solubilization_causal_predicates(record, predicate):
    record["mechanisms"][0]["organisms"] = [
        {"id": "NCBITaxon:442", "label": "Gluconobacter oxydans"}
    ]
    graph = _sample_causal_graph()
    graph["edges"][0]["predicate"] = predicate
    record["causal_graphs"] = [graph]
    assert validate_record(record) == []


def test_source_title_conciseness_and_assay_prose_guardrail(record):
    """Source.title must remain bibliographic and not embed empirical assay dumps (cmmmech-infra-0010)."""
    record["sources"][0]["title"] = (
        "Synthetic Paper (2026); EPMA Table 1 reports Nb2O5 44.12 wt.% (0.98 apfu) "
        "and single-crystal refinement wR2 = 0.054, GOF = 1.08."
    )
    errs = validate_record(record)
    assert any("contains embedded empirical assay/refinement metrics" in e for e in errs)

    record["sources"][0]["title"] = "Synthetic Paper (2026) " + ("A" * 1005)
    errs_long = validate_record(record)
    assert any("exceeds maximum bibliographic length" in e for e in errs_long)


def test_top_level_section_ordering_guardrail(record):
    """Top-level sections must preserve canonical evidence/mechanism/history ordering (cmmmech-infra-0010)."""
    misordered_mech = {
        "id": record["id"],
        "name": record["name"],
        "material_kind": record["material_kind"],
        "description": record["description"],
        "mechanisms": record["mechanisms"],
        "sources": record["sources"],
        "criticality": record["criticality"],
    }
    errs_mech = validate_record(misordered_mech)
    assert any("mechanisms must appear after sources" in e for e in errs_mech)
    assert any("mechanisms must appear after criticality" in e for e in errs_mech)

    misordered_history = copy.deepcopy(record)
    misordered_history["history_refs"] = ["history/records/synthetic-material/2026-10-07T120000Z-tester-123abc.yaml"]
    misordered_history["curation_history"] = [
        {
            "timestamp": "2026-10-07T12:00:00Z",
            "curator": "tester",
            "action": "audit",
            "summary": "Synthetic audit",
        }
    ]
    errs_hist = validate_record(misordered_history)
    assert any("history_refs must appear after curation_history" in e for e in errs_hist)




