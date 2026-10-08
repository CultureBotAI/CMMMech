"""Exercise the real local/CI gate against an accidentally emptied corpus."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from cmmmech.cli import main


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


def test_check_rejects_a_committed_history_rewrite_against_the_ci_base(tmp_path, record, capsys):
    """A clean PR HEAD must not hide rewritten history from its reviewed base."""
    root = Path(__file__).resolve().parents[1]
    for folder in ("scripts", "src", "tests", "data/records"):
        (tmp_path / folder).mkdir(parents=True)
    shutil.copyfile(root / "scripts/check.py", tmp_path / "scripts/check.py")
    (tmp_path / "tests/test_smoke.py").write_text("def test_smoke():\n    assert True\n")
    target = tmp_path / "data/records/synthetic-material.yaml"
    target.write_text(yaml.safe_dump(record))
    assert main([
        "new-history", "--repo-root", str(tmp_path), "--slug", "synthetic-material",
        "--actor-name", "test", "--actor-type", "human", "--summary", "Synthetic check",
        "--details", "A synthetic event used only to exercise the CI baseline gate.",
    ]) == 0
    sidecar = tmp_path / capsys.readouterr().out.strip()

    def git(*args):
        return subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True,
                              text=True)

    def commit(message):
        git("add", ".")
        git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm",
            message)

    git("init", "-q")
    commit("reviewed baseline")
    baseline = git("rev-parse", "HEAD").stdout.strip()
    sidecar.write_text(sidecar.read_text().replace("Synthetic check", "Rewritten historical claim"))
    commit("committed rewrite")
    assert git("status", "--porcelain").stdout == ""
    env = dict(os.environ, PYTHONPATH=str(root / "src"), CMMMECH_HISTORY_BASE=baseline)

    def check(environment):
        return subprocess.run([sys.executable, str(tmp_path / "scripts/check.py")],
                              cwd=tmp_path, env=environment, capture_output=True, text=True,
                              check=False)

    result = check(env)
    assert "All checks passed!" in result.stdout
    assert "1 passed" in result.stdout
    assert "Checked 1 record(s); 0 failed" in result.stdout
    assert "history is append-only" in result.stdout
    assert result.returncode == 1
    # Exact control: every byte and test is unchanged, but HEAD hides the
    # already committed rewrite. This proves why CI must supply its event base.
    control = check(dict(env, CMMMECH_HISTORY_BASE="HEAD"))
    assert control.returncode == 0, control.stdout + control.stderr
