"""Context windows resolved through the source record's vendored edition,
for loci that name no `cic/texts/<file>, lines N` span."""
from engine.m4 import fit_step, source_windows

NAME = "xyz01_fixture-volume.xml"
SOURCE = {"id": "w.source.vol", "record_type": "source", "edition": f"Fixture volume, vendored as cic/texts/{NAME} (div i)"}


def _fixture(tmp_path):
    filler = [f"<p>filler {n} alpha beta gamma delta</p>" for n in range(1, 41)]
    lines = (
        ['<div1 id="i" title="Book One">']
        + filler[:20]
        + ['<div2 id="i.ii" title="Chapter Two">', "<p>Before the saying there is talk of the harbour.</p>",
           "<p>The <i>light</i> of the city, he said, is the gathered church at prayer;</p>",
           "<p>and no lamp is lit for itself alone.</p>", "<p>After it the talk turns to bread.</p>", "</div2>"]
        + filler[20:]
        + ["</div1>"]
    )
    path = tmp_path / "cic" / "texts" / NAME
    path.parent.mkdir(parents=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return lines


def _record(record_type="quote", locus="Book One, ch. 2 (xyz01)", text="the light of the city, he said, is the gathered church at prayer; and no lamp is lit"):
    return {"id": "w.quote.light", "record_type": record_type, "text": text,
            "sources": [{"source_id": SOURCE["id"], "locus": locus}]}


def test_a_quote_is_found_by_its_words_and_kept_inside_its_division(tmp_path):
    lines = _fixture(tmp_path)
    (block,) = source_windows.context_blocks(_record(), {SOURCE["id"]: SOURCE}, tmp_path)
    first = lines.index("<p>The <i>light</i> of the city, he said, is the gathered church at prayer;</p>") + 1
    assert block["id"] == f"{fit_step.CONTEXT_PREFIX}w.quote.light.1" and block["file"] == f"cic/texts/{NAME}"
    assert block["lines"] == f"{first}-{first + 1}"
    assert "harbour" in block["text"] and "bread" in block["text"]
    assert "filler" not in block["text"] and "<" not in block["text"]


def test_the_locus_lines_anchor_a_story_and_a_division_id_anchors_one_with_no_lines(tmp_path):
    lines = _fixture(tmp_path)
    story = _record("story", locus="ch. 2 (xyz01 line 24)", text="")
    (block,) = source_windows.context_blocks(story, {SOURCE["id"]: SOURCE}, tmp_path)
    assert block["lines"] == "24-24" and "light" in lines[23] and "bread" in block["text"]
    by_div = _record("story", locus="ch. 2 (xyz01 div i.ii)", text="")
    (block,) = source_windows.context_blocks(by_div, {SOURCE["id"]: SOURCE}, tmp_path)
    opening = next(n for n, line in enumerate(lines, start=1) if line.startswith('<div2 id="i.ii"'))
    assert block["lines"] == f"{opening}-{opening}" and "harbour" in block["text"]


def test_an_unresolvable_record_gets_no_window(tmp_path):
    _fixture(tmp_path)
    assert source_windows.context_blocks(_record("story", locus="the whole text", text=""), {SOURCE["id"]: SOURCE}, tmp_path) == []
    assert source_windows.context_blocks(_record(), {}, tmp_path) == []
