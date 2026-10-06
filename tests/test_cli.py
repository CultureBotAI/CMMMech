import pytest
import yaml

from cmmmech.cli import main


def test_empty_corpus_is_explicit(tmp_path, monkeypatch, capsys):
    (tmp_path / "data/records").mkdir(parents=True)
    monkeypatch.chdir(tmp_path)
    assert main(["validate"]) == 0
    assert "Corpus is empty" in capsys.readouterr().out
    assert main(["validate", "--require-records"]) == 1


def test_validate_is_read_only(tmp_path, record):
    path = tmp_path / "record.yaml"
    path.write_text(yaml.safe_dump(record))
    before = path.read_bytes()
    assert main(["validate", str(path)]) == 0
    assert path.read_bytes() == before


def test_nested_yml_files_are_validated(tmp_path, record):
    folder = tmp_path / "nested"
    folder.mkdir()
    record["unexpected"] = True
    (folder / "record.yml").write_text(yaml.safe_dump(record))
    assert main(["validate", str(tmp_path)]) == 1


def test_duplicate_record_ids_are_rejected(tmp_path, record, capsys):
    for name in ("one.yaml", "two.yaml"):
        (tmp_path / name).write_text(yaml.safe_dump(record))
    assert main(["validate", str(tmp_path)]) == 1
    assert "duplicate record id" in capsys.readouterr().out


def test_repeated_path_is_not_a_duplicate_record(tmp_path, record):
    path = tmp_path / "record.yaml"
    path.write_text(yaml.safe_dump(record))
    assert main(["validate", str(path), str(tmp_path)]) == 0


@pytest.mark.parametrize("content", [b"name: [", b"\xff\xfe", b"id: a\nid: b\n", b"null\n"])
def test_bad_input_returns_failure(tmp_path, content):
    path = tmp_path / "bad.yaml"
    path.write_bytes(content)
    assert main(["validate", str(path)]) == 1


def test_missing_path_is_not_an_empty_corpus(tmp_path):
    with pytest.raises(SystemExit) as exc:
        main(["validate", str(tmp_path / "missing")])
    assert exc.value.code == 2
