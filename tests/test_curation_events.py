"""Inline provenance is optional, but accepted events have a strict contract."""

import pytest

from cmmmech.validation import validate_record


@pytest.fixture
def event_record(record):
    record["curation_history"] = [{
        "timestamp": "2026-10-08T02:00:00Z",
        "curator": "synthetic-test",
        "action": "review",
        "summary": "Synthetic validation fixture; no scientific review performed.",
    }]
    return record


def test_existing_records_need_no_inline_history(record):
    assert "curation_history" not in record
    assert validate_record(record) == []


@pytest.mark.parametrize("timestamp", [
    "2000-01-01T00:00:00Z", "2026-10-08T02:00:00.123Z", "2099-12-31T23:59:59+00:00",
])
def test_valid_inline_events_are_accepted(event_record, timestamp):
    event_record["curation_history"][0]["timestamp"] = timestamp
    assert validate_record(event_record) == []


@pytest.mark.parametrize("timestamp", [
    "1999-12-31T23:59:59Z", "2206-08-22T12:00:00Z", "2026-02-30T12:00:00Z",
    "2026-10-08", "2026-10-08T02:00:00", "not-a-date", None,
])
def test_bad_inline_timestamps_fail_native_validation(event_record, timestamp):
    event_record["curation_history"][0]["timestamp"] = timestamp
    assert any("curation_history/0/timestamp" in error for error in validate_record(event_record))


@pytest.mark.parametrize("field", ["timestamp", "curator", "action", "summary"])
def test_inline_events_require_complete_provenance(event_record, field):
    del event_record["curation_history"][0][field]
    assert validate_record(event_record)


@pytest.mark.parametrize("field", ["curator", "action", "summary"])
def test_inline_event_text_cannot_be_blank(event_record, field):
    event_record["curation_history"][0][field] = "  "
    assert validate_record(event_record)


def test_inline_events_are_closed(event_record):
    event_record["curation_history"][0]["unexpected"] = "not allowed"
    assert validate_record(event_record)


@pytest.mark.parametrize("history", [[], {}, "not-a-list", None])
def test_present_inline_history_requires_events(record, history):
    record["curation_history"] = history
    assert validate_record(record)
