"""Offline closed-schema and record-local integrity validation."""

import json
from collections import Counter
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
    for index, mechanism in enumerate(record.get("mechanisms", [])):
        if mechanism.get("organisms") and not mechanism["microbial"]:
            errors.append(f"mechanisms/{index}: organisms require microbial: true")
        references.extend((f"mechanisms/{index}/evidence/{i}", item["source_ref"])
                          for i, item in enumerate(mechanism["evidence"]))
    errors.extend(f"{path}: unknown source_ref {key}" for path, key in references if key not in sources)
    return sorted(errors)


def read_record(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.load(stream, Loader=UniqueKeyLoader)
