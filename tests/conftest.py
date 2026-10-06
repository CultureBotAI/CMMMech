"""Synthetic fixtures only; no curated scientific claims."""

import pytest


@pytest.fixture
def record():
    return {
        "id": "cmmmech:synthetic-material",
        "name": "Synthetic test material",
        "material_kind": "commodity",
        "description": "A test fixture, not a real mineral record.",
        "sources": [{"id": "fixture", "title": "Synthetic fixture",
                     "url": "https://example.invalid/source", "accessed_on": "2026-10-05"}],
        "criticality": [{"jurisdiction": "Fixtureland", "list_name": "Synthetic list",
                         "edition": "test-only", "classification": "unknown",
                         "source_ref": "fixture"}],
        "mechanisms": [{
            "id": "test_mechanism", "name": "Synthetic microbial mechanism", "process": "other",
            "description": "Synthetic claim only.", "context": "Synthetic substrate and conditions.",
            "microbial": True, "organisms": [{"id": "TEST:organism", "label": "Test organism"}],
            "evidence": [{"source_ref": "fixture", "supports": "context_only",
                          "explanation": "Used solely to exercise validation."}],
        }],
    }
