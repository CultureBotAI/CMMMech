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

# Create a new immutable sidecar, then attach its printed path to the record.
new-history *args:
    uv run --locked cmmmech new-history {{args}}

validate-history *args:
    uv run --locked cmmmech validate-history {{args}}

# Validate immutable structured review observations; never curate records.
review-check *args:
    uv run python scripts/record_review.py check {{args}}
