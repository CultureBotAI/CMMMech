"""Offline closed-schema and record-local integrity validation."""

import json
import math
from collections import Counter
from decimal import Decimal, DecimalException
from functools import lru_cache
from importlib.resources import as_file, files
from pathlib import Path

import yaml
from jsonschema import FormatChecker
from jsonschema.validators import validator_for
from linkml.generators.jsonschemagen import JsonSchemaGenerator


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise yaml.constructor.ConstructorError(
                    None, None, "duplicate or non-string mapping key", key_node.start_mark
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


@lru_cache(maxsize=2)
def schema_validator(filename: str, top_class: str):
    resource = files("cmmmech").joinpath(f"schema/{filename}")
    with as_file(resource) as path:
        schema = json.loads(JsonSchemaGenerator(
            str(path), top_class=top_class, not_closed=False, include_null=False
        ).serialize())
    validator = validator_for(schema)
    validator.check_schema(schema)
    return validator(schema, format_checker=FormatChecker())


def record_validator():
    return schema_validator("cmmmech.yaml", "CriticalMineralRecord")


def _observation_errors(observation, path: str) -> list[str]:
    """Validate a source cell without treating a censoring boundary as a measurement."""
    errors = []
    below_detection = observation["result_status"] == "below_detection"
    required = "detection_limit" if below_detection else "value"
    forbidden = "value" if below_detection else "detection_limit"
    if required not in observation:
        errors.append(f"{path}: {observation['result_status']} requires {required}")
    if forbidden in observation:
        errors.append(f"{path}: {observation['result_status']} forbids {forbidden}")

    try:
        raw = Decimal(observation["raw_value"])
    except DecimalException:
        errors.append(f"{path}/raw_value: cannot represent numeric source value")
        return errors
    if below_detection and raw >= 0:
        errors.append(f"{path}/raw_value: below_detection requires negative limit encoding")
    elif not below_detection and raw < 0:
        errors.append(f"{path}/raw_value: measured concentration cannot use negative encoding")

    for field in ("value", "detection_limit"):
        if field not in observation:
            continue
        value = observation[field]
        if isinstance(value, float) and not math.isfinite(value):
            errors.append(f"{path}/{field}: must be finite")
        elif field == "detection_limit" and value <= 0:
            errors.append(f"{path}/{field}: must be positive")
        elif field == required and Decimal(str(value)) != (
            raw.copy_abs() if below_detection else raw
        ):
            errors.append(f"{path}/{field}: does not match raw_value and result_status")

    has_sample_date = "sampled_on" in observation
    if has_sample_date != ("sampling_source_locator" in observation):
        errors.append(f"{path}: sampled_on and sampling_source_locator must be supplied together")
    if has_sample_date and observation["sampled_on"] > observation["analyzed_on"]:
        errors.append(f"{path}/sampled_on: cannot be after analyzed_on")
    return errors


def validate_record(record) -> list[str]:
    errors = [
        f"{'/'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in record_validator().iter_errors(record)
    ]
    if errors:
        return sorted(errors)

    for section in ("sources", "mechanisms"):
        counts = Counter(item["id"] for item in record.get(section, []))
        errors.extend(f"{section}: duplicate id {key}" for key, count in counts.items() if count > 1)
    history = record.get("history_refs", [])
    if len(set(history)) != len(history):
        errors.append("history_refs: duplicate history reference")
    sources = {source["id"] for source in record["sources"]}
    references = [(f"criticality/{index}", item["source_ref"])
                  for index, item in enumerate(record.get("criticality", []))]
    observation_ids = set()
    source_cells = set()
    for index, mechanism in enumerate(record.get("mechanisms", [])):
        if mechanism.get("organisms") and not mechanism["microbial"]:
            errors.append(f"mechanisms/{index}: organisms require microbial: true")
        references.extend((f"mechanisms/{index}/evidence/{i}", item["source_ref"])
                          for i, item in enumerate(mechanism["evidence"]))
        evidence_sources = {item["source_ref"] for item in mechanism["evidence"]}
        for number, observation in enumerate(mechanism.get("observations", [])):
            path = f"mechanisms/{index}/observations/{number}"
            references.append((path, observation["source_ref"]))
            if observation["source_ref"] not in evidence_sources:
                errors.append(f"{path}: source_ref must occur in this mechanism's evidence")
            if observation["id"] in observation_ids:
                errors.append(f"{path}: duplicate observation id {observation['id']}")
            observation_ids.add(observation["id"])
            cell = tuple(observation[field] for field in (
                "source_ref", "source_table", "source_sample_id", "source_column", "analyzed_on"
            ))
            if cell in source_cells:
                errors.append(f"{path}: duplicate source concentration cell")
            source_cells.add(cell)
            errors.extend(_observation_errors(observation, path))
    errors.extend(f"{path}: unknown source_ref {key}" for path, key in references if key not in sources)
    return sorted(errors)


def read_record(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)
