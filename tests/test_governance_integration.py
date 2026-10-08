"""Native integration stays strict without editing the canonical payloads."""

import re
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_governance_pin_is_one_immutable_commit():
    pin = (ROOT / "scripts/.vendored_canon_ref").read_text(encoding="ascii")
    assert re.fullmatch(r"[0-9a-f]{40}\n", pin)


def test_canonical_style_exception_is_limited_to_the_governed_validator():
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    lint = config["tool"]["ruff"]["lint"]
    assert lint["select"] == ["E4", "E7", "E9", "F", "I"]
    assert lint["per-file-ignores"] == {
        "scripts/validate_id_label_correspondence.py": ["E741"],
    }


def test_ci_requires_both_native_and_canonical_gates():
    workflow = yaml.load(
        (ROOT / ".github/workflows/validate-strict.yaml").read_text(encoding="utf-8"),
        Loader=yaml.BaseLoader,
    )
    triggers = workflow["on"]
    assert triggers["pull_request"] == ""
    assert triggers["push"] == {"branches": ["main"]}
    assert triggers["merge_group"] == {"types": ["checks_requested"]}
    job = workflow["jobs"]["validate-strict"]
    assert "if" not in job
    assert "continue-on-error" not in job
    steps = job["steps"]
    assert [step["run"] for step in steps if "run" in step] == [
        "uv sync --locked --extra dev",
        "uv run --no-sync python scripts/check.py",
        "bash scripts/check_vendored_sync.sh",
    ]
    for step in steps:
        assert "if" not in step
        assert "continue-on-error" not in step
        if step.get("uses", "").startswith("actions/checkout@"):
            assert "ref" not in step.get("with", {})
            assert step["with"]["persist-credentials"] == "false"

