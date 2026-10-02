import hashlib
import json

from engine.m10.blind import assign_labels, scrub_draft
from engine.m10.cli import main

from .fixture_world import write

HEADER = "# Doc_10 Representative\n\n**Drafter:** Sonnet 5.5\n**Model:** claude-sonnet-5-5\nEffort: high\nDrafted by the pilot\nStatus: draft\n\n## Voice\n"
BODY = "She speaks plainly.\nThe road was long.\n"


def _drafts(tmp_path, body_a=BODY, body_b=BODY):
    s = write(tmp_path, "in/sonnet.md", HEADER + body_a)
    f = write(tmp_path, "in/fable.md", HEADER.replace("Sonnet 5.5", "Fable").replace("claude-sonnet-5-5", "claude-fable-5") + body_b)
    return s, f


def _run(tmp_path, s, f, *extra, seed="s1"):
    return main(["blind", "w", "--sonnet", str(s), "--fable", str(f), "--seed", seed,
                 "--out-dir", str(tmp_path / "out"), "--root", str(tmp_path), *extra])


def _mapping(tmp_path):
    return tmp_path / "out" / "w_Doc10_Blind_Mapping.json"


def test_same_seed_same_result(tmp_path):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f) == 0
    first = [(tmp_path / "out" / n).read_bytes() for n in ("Doc_10_A.md", "Doc_10_B.md")] + [_mapping(tmp_path).read_bytes()]
    assert _run(tmp_path, s, f, "--force") == 0
    second = [(tmp_path / "out" / n).read_bytes() for n in ("Doc_10_A.md", "Doc_10_B.md")] + [_mapping(tmp_path).read_bytes()]
    assert first == second


def test_both_orders_reachable():
    seen = {tuple(sorted(assign_labels(str(i)).items())) for i in range(40)}
    assert len(seen) == 2


def test_header_scrubbed_body_untouched(tmp_path, capsys):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f) == 0
    mapping = json.loads(_mapping(tmp_path).read_text())
    for label in "AB":
        text = (tmp_path / "out" / f"Doc_10_{label}.md").read_text()
        head, body = text.split("## Voice\n")
        assert body == BODY
        assert "Sonnet" not in head and "Fable" not in head and "claude-" not in head
        assert "**Drafter:** [withheld]" in head and "Status: draft" in head
    assert {e["kind"] for e in mapping["scrub_report"]} == {"field-scrubbed"}


def test_body_mention_fails_then_passes_unaltered_with_flag(tmp_path, capsys):
    body = "She said Sonnet wrote this.\nPlain line.\n"
    s, f = _drafts(tmp_path, body_a=body)
    assert _run(tmp_path, s, f) == 1
    out = capsys.readouterr().out
    assert "blind-body-mention" in out and f"{s}:10" in out
    assert not _mapping(tmp_path).exists()
    assert _run(tmp_path, s, f, "--allow-body-mentions") == 0
    mapping = json.loads(_mapping(tmp_path).read_text())
    assert any(e["kind"] == "mention" and e["text"] == "Sonnet" for e in mapping["scrub_report"])
    drafter = "sonnet"
    label = next(k for k, v in mapping["labels"].items() if v == drafter)
    assert (tmp_path / "out" / f"Doc_10_{label}.md").read_text().endswith(body)


def test_header_mention_outside_a_field_fails(tmp_path):
    s = write(tmp_path, "in/sonnet.md", "# Doc_10\n\nSonnet notes here\n\n## Voice\nx\n")
    f = write(tmp_path, "in/fable.md", "# Doc_10\n\n## Voice\nx\n")
    assert _run(tmp_path, s, f) == 1


def test_refuses_overwrite_without_force(tmp_path):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f) == 0
    before = _mapping(tmp_path).read_bytes()
    assert _run(tmp_path, s, f, seed="other") == 1
    assert _mapping(tmp_path).read_bytes() == before
    (tmp_path / "out" / "w_Doc10_Blind_Mapping.json").unlink()
    assert _run(tmp_path, s, f) == 1
    assert _run(tmp_path, s, f, "--force") == 0


def test_printed_checksum_matches_file(tmp_path, capsys):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f) == 0
    out = capsys.readouterr().out
    line = next(l for l in out.splitlines() if l.startswith("MAPPING CHECKSUM: "))
    assert line.split(": ")[1] == hashlib.sha256(_mapping(tmp_path).read_bytes()).hexdigest()
    assert "cost ledger" in out


def _checksum(tmp_path):
    return hashlib.sha256(_mapping(tmp_path).read_bytes()).hexdigest()


def _reveal(tmp_path, checksum):
    return main(["blind", "w", "--reveal", "--mapping", str(_mapping(tmp_path)), "--checksum", checksum, "--root", str(tmp_path)])


def test_reveal_with_right_and_wrong_checksum(tmp_path, capsys):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f) == 0
    capsys.readouterr()
    assert _reveal(tmp_path, "0" * 64) == 1
    assert "reveal-checksum" in capsys.readouterr().out
    assert _reveal(tmp_path, _checksum(tmp_path)) == 0
    out = capsys.readouterr().out
    assert "sonnet" in out and "fable" in out


def test_reveal_detects_edited_draft(tmp_path, capsys):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f) == 0
    draft = tmp_path / "out" / "Doc_10_A.md"
    draft.write_text(draft.read_text() + "edited\n")
    capsys.readouterr()
    assert _reveal(tmp_path, _checksum(tmp_path)) == 1
    assert "changed after blinding" in capsys.readouterr().out


def test_missing_input_file(tmp_path, capsys):
    s, f = _drafts(tmp_path)
    f.unlink()
    assert _run(tmp_path, s, f) == 1
    assert "does not exist" in capsys.readouterr().out
    assert not (tmp_path / "out").exists()


def test_json_output(tmp_path, capsys):
    s, f = _drafts(tmp_path)
    assert _run(tmp_path, s, f, "--json") == 0
    doc = json.loads(capsys.readouterr().out)
    assert doc["pass"] and any(n.startswith("MAPPING CHECKSUM: ") for n in doc["reports"][0]["notes"])


def test_scrub_keeps_line_endings():
    result = scrub_draft("# T\r\nModel: claude-opus-5\r\n## B\r\ntext\r\n")
    assert result.text == "# T\r\nModel: [withheld]\r\n## B\r\ntext\r\n"
