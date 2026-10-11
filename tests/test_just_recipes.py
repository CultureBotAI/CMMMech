"""Curation text must reach CLI wrappers literally, without shell reinterpretation."""

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize("recipe,prefix", [
    ("new-history", ["run", "--locked", "cmmmech", "new-history"]),
    ("validate-history", ["run", "--locked", "cmmmech", "validate-history"]),
    ("review-check", ["run", "python", "scripts/record_review.py", "check"]),
])
@pytest.mark.parametrize("arguments", [
    [],
    ["--summary", "multiword text", "--details",
     "Keep $(touch substitution-ran) and `touch backtick-ran` literal",
     "$CMM_RECIPE_TEST_VALUE", "*.yaml"],
    ["", "single' and double\" quotes", "line one\nline two\tTe"],
])
def test_variadic_recipes_preserve_arguments(tmp_path, recipe, prefix, arguments):
    just = shutil.which("just")
    assert just is not None, "Install locked dev dependencies to run recipe regressions"
    # Execute the maintained recipe through real just; replace only its receiver.
    shutil.copyfile(ROOT / "justfile", tmp_path / "justfile")
    receiver = tmp_path / "uv"
    receiver.write_text(
        "#!/usr/bin/env python3\nimport json, sys\nprint(json.dumps(sys.argv[1:]))\n"
    )
    receiver.chmod(0o755)
    (tmp_path / "glob-match.yaml").write_text("synthetic fixture\n")
    env = {**os.environ, "PATH": f"{tmp_path}{os.pathsep}{os.environ['PATH']}",
           "CMM_RECIPE_TEST_VALUE": "must not expand"}
    result = subprocess.run(
        [just, "--justfile", str(tmp_path / "justfile"), recipe, *arguments],
        cwd=tmp_path, env=env, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout) == prefix + arguments
    assert not (tmp_path / "substitution-ran").exists()
    assert not (tmp_path / "backtick-ran").exists()
