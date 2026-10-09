"""Synthetic concentration cells exercise censoring, provenance and source fidelity."""

import copy

import pytest

from cmmmech.validation import read_record, validate_record


@pytest.fixture
def observation_record(record):
    record["mechanisms"][0]["observations"] = [{
        "id": "synthetic_cell",
        "source_ref": "fixture",
        "source_table": "synthetic_concentrations.csv",
        "source_sample_id": "synthetic_abiotic_0",
        "source_column": "element_ppm",
        "raw_value": "2.75",
        "analyte": {"id": "TEST:element", "label": "Synthetic test element"},
        "material_form": "Synthetic dissolved analyte; oxidation state unassigned.",
        "sampled_fraction": "Filtered synthetic working solution.",
        "study_arm": "abiotic",
        "result_status": "measured",
        "value": 2.75,
        "unit": "mg/kg",
        "analyzed_on": "2026-10-05",
        "sampled_on": "2026-10-01",
        "sampling_source_locator": "synthetic_samples.csv, exact SampleID, Date column",
        "context": "Synthetic ICP-OES result; this control is not evidence of microbial causality.",
    }]
    return record


def observation(record):
    return record["mechanisms"][0]["observations"][0]


def below_detection(record):
    item = observation(record)
    item["result_status"] = "below_detection"
    item["raw_value"] = "-0.025"
    item.pop("value")
    item["detection_limit"] = 0.025
    return item


def test_abiotic_control_can_be_bound_to_microbial_mechanism(observation_record):
    assert observation_record["mechanisms"][0]["microbial"] is True
    assert validate_record(observation_record) == []


def test_existing_record_needs_no_observations(record):
    assert validate_record(record) == []


def test_source_negative_encoding_is_a_limit_not_a_measurement(observation_record):
    item = below_detection(observation_record)
    assert validate_record(observation_record) == []
    item["result_status"] = "measured"
    item["value"] = item.pop("detection_limit")
    assert any("negative encoding" in error for error in validate_record(observation_record))


def test_reported_zero_is_supported_without_imputing_censored_zero(observation_record):
    item = observation(observation_record)
    item["raw_value"] = "0"
    item["value"] = 0
    assert validate_record(observation_record) == []
    item["raw_value"] = "-0.025"
    assert validate_record(observation_record)


def test_numeric_source_token_is_preserved_with_scientific_notation(observation_record):
    item = observation(observation_record)
    item["raw_value"] = "2.750E+00"
    assert validate_record(observation_record) == []


def test_large_finite_integer_does_not_overflow_float_coercion(observation_record):
    item = observation(observation_record)
    item["value"] = 10**400
    item["raw_value"] = str(item["value"])
    assert validate_record(observation_record) == []


def test_unrepresentable_source_exponent_fails_without_crashing(observation_record):
    observation(observation_record)["raw_value"] = "1e9999999999999999999999"
    assert any("cannot represent numeric source value" in error
               for error in validate_record(observation_record))


def test_censored_limit_comparison_does_not_round_source_mantissa(observation_record):
    item = below_detection(observation_record)
    item["detection_limit"] = 0.025
    item["raw_value"] = "-0.025000000000000000000000000000000000001"
    assert any("does not match" in error for error in validate_record(observation_record))


@pytest.mark.parametrize("status,missing,extra", [
    ("measured", "value", "detection_limit"),
    ("below_detection", "detection_limit", "value"),
])
def test_result_states_require_only_their_own_numeric_field(
    observation_record, status, missing, extra
):
    item = below_detection(observation_record) if status == "below_detection" else observation(
        observation_record
    )
    value = item.pop(missing)
    assert any(f"requires {missing}" in error for error in validate_record(observation_record))
    item[missing] = value
    item[extra] = value
    assert any(f"forbids {extra}" in error for error in validate_record(observation_record))


@pytest.mark.parametrize("status,field,value", [
    ("measured", "value", -1),
    ("below_detection", "detection_limit", 0),
    ("below_detection", "detection_limit", -0.025),
    ("measured", "value", float("nan")),
    ("measured", "value", float("inf")),
    ("measured", "value", float("-inf")),
    ("below_detection", "detection_limit", float("nan")),
    ("below_detection", "detection_limit", float("inf")),
    ("below_detection", "detection_limit", float("-inf")),
])
def test_invalid_numeric_results_fail_cleanly(observation_record, status, field, value):
    item = below_detection(observation_record) if status == "below_detection" else observation(
        observation_record
    )
    item[field] = value
    assert validate_record(observation_record)


@pytest.mark.parametrize("literal", [".nan", ".inf", "-.inf"])
def test_yaml_nonfinite_results_do_not_escape_validation(tmp_path, observation_record, literal):
    import yaml

    text = yaml.safe_dump(observation_record).replace("value: 2.75", f"value: {literal}")
    path = tmp_path / "synthetic.yaml"
    path.write_text(text)
    assert validate_record(read_record(path))


@pytest.mark.parametrize("status,raw", [
    ("measured", "2.74"),
    ("below_detection", "-0.024"),
    ("below_detection", "0.025"),
    ("below_detection", "0"),
])
def test_source_value_and_curated_result_must_agree(observation_record, status, raw):
    item = below_detection(observation_record) if status == "below_detection" else observation(
        observation_record
    )
    item["raw_value"] = raw
    assert validate_record(observation_record)


@pytest.mark.parametrize("field,value", [
    ("unit", "mg/L"),
    ("result_status", "not_reported"),
    ("study_arm", "unknown"),
    ("raw_value", -0.025),
    ("raw_value", ".nan"),
    ("raw_value", "<0.025"),
    ("value", "2.75"),
    ("value", True),
    ("value", None),
    ("analyzed_on", "2026-02-30"),
    ("sampled_on", "not-a-date"),
    ("unexpected", "closed schema"),
    ("effect_size", 0.2),
    ("recovery_percent", 99),
    ("source_sample_id", "  "),
    ("material_form", ""),
    ("sampled_fraction", ""),
    ("context", ""),
])
def test_observation_contract_is_closed_and_typed(observation_record, field, value):
    observation(observation_record)[field] = value
    assert validate_record(observation_record)


def test_analyte_identity_is_closed(observation_record):
    observation(observation_record)["analyte"]["unexpected"] = "not allowed"
    assert validate_record(observation_record)


@pytest.mark.parametrize("field", [
    "id", "source_ref", "source_table", "source_sample_id", "source_column", "raw_value",
    "analyte", "material_form", "sampled_fraction", "study_arm", "result_status", "unit",
    "analyzed_on", "context",
])
def test_observation_needs_traceable_sample_context(observation_record, field):
    observation(observation_record).pop(field)
    assert validate_record(observation_record)


def test_empty_observation_list_does_not_claim_data_coverage(observation_record):
    observation_record["mechanisms"][0]["observations"] = []
    assert validate_record(observation_record)


def test_observation_source_must_exist_and_support_this_mechanism(observation_record):
    item = observation(observation_record)
    item["source_ref"] = "absent"
    assert any("unknown source_ref" in error for error in validate_record(observation_record))
    source = copy.deepcopy(observation_record["sources"][0])
    source["id"] = "absent"
    observation_record["sources"].append(source)
    errors = validate_record(observation_record)
    assert not any("unknown source_ref" in error for error in errors)
    assert any("this mechanism's evidence" in error for error in errors)


def test_observation_ids_are_unique_across_mechanisms(observation_record):
    mechanism = copy.deepcopy(observation_record["mechanisms"][0])
    mechanism["id"] = "different_mechanism"
    mechanism["observations"][0]["source_sample_id"] = "different_sample"
    observation_record["mechanisms"].append(mechanism)
    assert any("duplicate observation id" in error for error in validate_record(observation_record))


def test_different_id_does_not_duplicate_a_source_cell(observation_record):
    other = copy.deepcopy(observation(observation_record))
    other["id"] = "different_id"
    observation_record["mechanisms"][0]["observations"].append(other)
    assert any("duplicate source concentration cell" in error
               for error in validate_record(observation_record))
    other["analyzed_on"] = "2026-10-06"
    assert validate_record(observation_record) == []


def test_sample_date_can_be_unknown_but_not_replaced_with_analysis_date(observation_record):
    item = observation(observation_record)
    item.pop("sampled_on")
    item.pop("sampling_source_locator")
    assert validate_record(observation_record) == []
    item["sampled_on"] = "2026-10-01"
    assert any("supplied together" in error for error in validate_record(observation_record))
    item.pop("sampled_on")
    item["sampling_source_locator"] = "synthetic date provenance"
    assert any("supplied together" in error for error in validate_record(observation_record))


def test_sampling_cannot_follow_analysis(observation_record):
    observation(observation_record)["sampled_on"] = "2026-10-06"
    assert any("cannot be after" in error for error in validate_record(observation_record))
