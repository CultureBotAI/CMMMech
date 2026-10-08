"""Record validation and append-only curation history."""

import argparse
from pathlib import Path

import yaml

from cmmmech.validation import read_record, record_validator, validate_record


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="cmmmech")
    commands = parser.add_subparsers(dest="command", required=True)
    from cmmmech.history import add_commands, validate_references

    add_commands(commands)
    validate = commands.add_parser("validate", help="validate YAML records without modifying them")
    validate.add_argument("paths", nargs="*", type=Path)
    validate.add_argument("--require-records", action="store_true")
    args = parser.parse_args(argv)
    if args.command != "validate":
        return args.handler(args)
    record_validator()
    selected = args.paths or [Path("data/records")]
    paths = set()
    for path in selected:
        if not path.exists():
            parser.error(f"path does not exist: {path}")
        if path.is_dir():
            paths.update(p.resolve() for p in path.rglob("*")
                         if p.is_file() and p.suffix in {".yaml", ".yml"})
        else:
            paths.add(path.resolve())
    if not paths:
        print("0 records; schema checked. Corpus is empty.")
        return int(args.require_records)

    failed = 0
    identifiers = {}
    for path in sorted(paths):
        try:
            record = read_record(path)
            errors = validate_record(record)
            if not errors:
                errors.extend(validate_references(record, path, Path.cwd()))
        except (OSError, UnicodeError, yaml.YAMLError) as exc:
            errors = [str(exc)]
        if not errors:
            identifier = record["id"]
            if identifier in identifiers:
                errors = [f"duplicate record id {identifier}; also in {identifiers[identifier]}"]
            else:
                identifiers[identifier] = path
        if errors:
            failed += 1
            for error in errors:
                print(f"ERROR {path}: {error}")
    print(f"Checked {len(paths)} record(s); {failed} failed.")
    return int(failed > 0)
