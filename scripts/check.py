"""The same bounded offline gate for local runs and CI."""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for command in (
    [sys.executable, "-m", "ruff", "check", "src", "tests", "scripts"],
    [sys.executable, "-m", "pytest", "-q"],
    [sys.executable, "-m", "cmmmech", "validate", "--require-records"],
    [sys.executable, "-m", "cmmmech", "validate-history", "--base",
     os.environ.get("CMMMECH_HISTORY_BASE", "HEAD")],
):
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        raise SystemExit(result.returncode)
