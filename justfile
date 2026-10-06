default:
    @just --list

check:
    uv run --locked --extra dev python scripts/check.py

test:
    uv run --locked --extra dev pytest -q

lint:
    uv run --locked --extra dev ruff check src tests scripts

validate:
    uv run --locked cmmmech validate
