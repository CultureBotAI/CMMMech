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
