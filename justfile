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

# Render the browsable site under pages/ from the corpus.
render *args:
    uv run python scripts/render_pages.py {{args}}

# Fail if pages/ is out of step with the corpus
render-check:
    uv run python scripts/render_pages.py --check

embed-dry:
    uv run python scripts/embed_records.py --dry-run

embed *args:
    python3 scripts/embed_records.py {{args}}

embed-map:
    python3 scripts/embed_map.py && uv run python scripts/render_pages.py

# Create a new immutable sidecar, then attach its printed path to the record.
[positional-arguments]
new-history *args:
    uv run --locked cmmmech new-history "$@"

[positional-arguments]
validate-history *args:
    uv run --locked cmmmech validate-history "$@"

# Validate immutable structured review observations; never curate records.
[positional-arguments]
review-check *args:
    uv run python scripts/record_review.py check "$@"
