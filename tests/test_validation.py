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
                "term": {"id": "CHEBI:33198", "label": "D-gluconic acid"},
            },
        ],
        "edges": [
            {
                "source": "gdh_enzyme",
                "target": "gluconic_acid_production",
                "predicate": "RO:0002413",
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
    record["mechanisms"][0]["protein_examples"] = [_sample_protein_example()]
    record["causal_graphs"] = [_sample_causal_graph()]
    assert validate_record(record) == []


def test_causal_graph_and_protein_example_integrity_checks(record):
    record["mechanisms"][0]["protein_examples"] = [
        _sample_protein_example(),
        _sample_protein_example(),
    ]
    assert any("duplicate uniprot_accession" in e for e in validate_record(record))

    record["mechanisms"][0]["protein_examples"] = [_sample_protein_example()]
    record["mechanisms"][0]["microbial"] = False
    record["mechanisms"][0].pop("organisms")
    assert any("protein_examples require microbial: true" in e for e in validate_record(record))
    record["mechanisms"][0]["microbial"] = True

    graph = _sample_causal_graph()
    graph["mechanism_ref"] = "nonexistent_mechanism"
    record["causal_graphs"] = [graph]
    assert any("unknown mechanism_ref" in e for e in validate_record(record))

    graph = _sample_causal_graph()
    graph["edges"][0]["target"] = "missing_node"
    record["causal_graphs"] = [graph]
    assert any("unknown target node" in e for e in validate_record(record))

    graph = _sample_causal_graph()
    graph["nodes"][0]["protein_examples"] = []
    record["causal_graphs"] = [graph]
    assert any("GROUNDED node requires protein_examples" in e for e in validate_record(record))

    graph = _sample_causal_graph()
    graph["nodes"][0]["protein_grounding_status"] = "UNGROUNDED"
    record["causal_graphs"] = [graph]
    assert any("UNGROUNDED node cannot have protein_examples" in e for e in validate_record(record))

    graph = _sample_causal_graph()
    graph["nodes"][1]["protein_examples"] = [_sample_protein_example()]
    record["causal_graphs"] = [graph]
    assert any(
        "protein_examples are only permitted on GENE_OR_PROTEIN nodes" in e
        for e in validate_record(record)
    )

