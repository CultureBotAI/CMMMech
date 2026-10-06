"""Exercise the real local/CI gate against an accidentally emptied corpus."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def test_check_fails_when_corpus_is_empty(tmp_path):
    root = Path(__file__).resolve().parents[1]
    for folder in ("scripts", "src", "tests", "data/records"):
        (tmp_path / folder).mkdir(parents=True)
    shutil.copyfile(root / "scripts/check.py", tmp_path / "scripts/check.py")
    (tmp_path / "tests/test_smoke.py").write_text("def test_smoke():\n    assert True\n")
    env = dict(os.environ, PYTHONPATH=str(root / "src"))
    result = subprocess.run(
        [sys.executable, str(tmp_path / "scripts/check.py")],
        cwd=tmp_path, env=env, capture_output=True, text=True, check=False,
    )
    assert "All checks passed!" in result.stdout  # Lint succeeded.
    assert "1 passed" in result.stdout  # The nested smoke suite succeeded.
    assert "Corpus is empty" in result.stdout  # Failure came from corpus validation.
    assert result.returncode == 1
