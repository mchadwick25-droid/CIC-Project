"""The evidence pack a labeller reads for one item: each bound record as the
voice was shown it, the source passages the record rests on with their whole
division (or a marked window of it), the edition's own apparatus marked as
not-the-text, the original language where the record points to it, and the
world's lexicon risk flags.

Nothing here is summarised or paraphrased. Passages are copied from the
vendored file, tags stripped; editors' notes are kept inline and labelled.
Every block of the pack has an id, so a verdict can name the block its
quoted words come from, and code can check the words are really there.
"""
import functools
import html
import re
from pathlib import Path

from goldset.common import git_show, records_at
from engine.m1.spoken_fields import fields_with_role
from engine.prose import all_text

VOICED_FIELDS = (
    "text", "modern_rendering", "positions", "tensions", "plain_meaning", "quick_meaning", "summary",
    "description", "claim", "statement", "held_against", "concedes", "narratable", "bridge_line",
    "exchange", "result", "why_sources_cannot_answer", "senses",
)
ANSWER_FIELDS = ("absent_detail", "thin_topics", "classification")
CARD_ONLY_FIELDS = {"story": ("heart",)}
HEAD_TEXT_TYPES = frozenset({
    "term", "story", "quote", "doctrinal_witness", "honest_limit", "gravity", "force", "contested_claim", "world_core",
})
LABEL_FIELDS = ("world_word", "title", "name", "speaker_or_author", "work")

DIVISION_WHOLE_LINES = 300
WINDOW_LINES = 80
PLAIN_WINDOW_LINES = 40
PASSAGE_CHAR_LIMIT = 24_000
LEXICON_CHAR_LIMIT = 40_000

_FILE = re.compile(r"(?:cic/texts/)?\b([A-Za-z0-9_\-][A-Za-z0-9_.\-]*\.(?:xml|txt))\b")
_LINES = re.compile(r"\blines?\s+(\d+)\s*(?:[-–]\s*(\d+))?")
_LANG = re.compile(r"-(lat|grc|fra|deu|ita|spa|syr|heb|arm|cop|ara|nld|rus|swe|enm|gmh|hrv|por|pol|ces)_")
_DIV = re.compile(r"<div(\d)\b([^>]*)>|</div(\d)>")
_TITLE = re.compile(r'\btitle="([^"]*)"')
_NOTE = re.compile(r"<note\b[^>]*>(.*?)</note>", re.DOTALL)
_TAG = re.compile(r"<[^>]+>")
_QUOTED = re.compile(r"[\"'‘“]([^\"'’”]{18,})[\"'’”]")
_DIV_ID = re.compile(r"\b(?:div\s+)?((?:[ivxlc]+|[0-9]+)(?:\.(?:[ivxlc]+|[0-9]+)){2,})\b")
CITED_OPEN, CITED_CLOSE = "⟦cited⟧", "⟦/cited⟧"


def file_language(name: str) -> str:
    m = _LANG.search(name)
    return m.group(1) if m else "eng"


def loci(locus: str) -> list[tuple[str, int | None, int | None]]:
    """(file, first line, last line) for each vendored file the locus names,
    each with the line range written after it, if any."""
    out = []
    matches = list(_FILE.finditer(locus or ""))
    for n, m in enumerate(matches):
        tail = locus[m.end(): matches[n + 1].start() if n + 1 < len(matches) else len(locus)]
        lines = _LINES.search(tail[:80])
        first = int(lines.group(1)) if lines else None
        last = _full_last(lines.group(1), lines.group(2) or lines.group(1)) if lines else None
        out.append((m.group(1), first, last))
    return out


def _full_last(first: str, last: str) -> int:
    """'12746-47' writes the last line short: it means 12746-12747, and
    '1299-03' means 1299-1303."""
    if len(last) < len(first):
        whole = int(first[: len(first) - len(last)] + last)
        if whole < int(first):
            whole += 10 ** len(last)
        return whole
    return int(last)


@functools.lru_cache(maxsize=32)
def text_lines(commit: str, name: str) -> tuple[str, ...] | None:
    """The vendored file as it stood at the records' commit; None when the
    shelf did not hold it then."""
    raw = git_show(commit, f"cic/texts/{name}")
    return tuple(raw.split("\n")) if raw is not None else None


@functools.lru_cache(maxsize=32)
def divisions(commit: str, name: str) -> tuple[tuple[int, int, int, str], ...]:
    """(level, first line, last line, title) of every ThML div, 1-based lines."""
    lines = text_lines(commit, name) or ()
    stack: list[tuple[int, int, str]] = []
    out = []
    for number, line in enumerate(lines, start=1):
        for m in _DIV.finditer(line):
            if m.group(1):
                title = _TITLE.search(m.group(2) or "")
                stack.append((int(m.group(1)), number, html.unescape(title.group(1)) if title else ""))
            elif stack:
                level = int(m.group(3))
                while stack:
                    open_level, start, title = stack.pop()
                    out.append((open_level, start, number, title))
                    if open_level == level:
                        break
    return tuple(out)


def _clean(raw: str) -> str:
    raw = _NOTE.sub(lambda m: f" [editor's note: {' '.join(_TAG.sub(' ', m.group(1)).split())}] ", raw)
    raw = re.sub(r"</p>|<br\s*/?>", "\n", raw.replace("\n", " "))
    text = html.unescape(_TAG.sub("", raw))
    paragraphs = [" ".join(p.split()) for p in text.split("\n")]
    return "\n".join(p for p in paragraphs if p)


def _locate(lines: tuple[str, ...], phrase: str) -> int | None:
    words = re.findall(r"\w+", phrase.lower())[:7]
    if len(words) < 5:
        return None
    pattern = re.compile(r"\W+".join(map(re.escape, words)), re.IGNORECASE)
    joined = "\n".join(_TAG.sub("", line) for line in lines)
    m = pattern.search(joined)
    return joined.count("\n", 0, m.start()) + 1 if m else None


def _div_line(lines: tuple[str, ...], div_id: str) -> int | None:
    """The line of the ThML div whose id the locus names, when exactly one has it."""
    marker = f'id="{div_id}"'
    found = [n for n, line in enumerate(lines, start=1) if marker in line and _DIV.search(line)]
    return found[0] if len(found) == 1 else None


def passage(commit: str, name: str, first: int | None, last: int | None, phrases: list[str], div_ids: list[str] = (),
            sections: list[tuple[str, str]] = ()) -> dict:
    """One source passage: the division holding the cited lines, whole when
    short, else a window around them; the cited lines are marked."""
    lines = text_lines(commit, name)
    language = file_language(name)
    if lines is None:
        return {"file": name, "language": language, "status": "file not on the shelf at the records' commit"}
    if first is None:
        found = next((n for n in (_div_line(lines, d) for d in div_ids) if n), None) if name.endswith(".xml") else None
        how = "located by the division id the locus names"
        if found is None:
            found = next((n for n in (_locate(lines, p) for p in phrases) if n), None)
            how = "located by the quoted words in the locus or record"
        if found is not None:
            first = last = found
        else:
            from goldset.locus import resolve
            span = next((r for r in (resolve(commit, name, locus, work) for locus, work in sections) if r), None)
            if span is None:
                return {"file": name, "language": language, "status": "locus gives no line, division id, quoted words or section number found in the file"}
            first, last = span
            how = "located by the section number in the locus, through the edition's own division numbering"
    else:
        how = "lines given in the locus"
    if first < 1 or last > len(lines) or first > last:
        return {"file": name, "language": language, "status": f"locus lines {first}-{last} are outside the file ({len(lines)} lines)"}
    holding = [d for d in divisions(commit, name) if d[1] <= first and d[2] >= last] if name.endswith(".xml") else []
    if holding:
        level, start, end, title = max(holding, key=lambda d: (d[0], d[1]))
        division = f"div{level} '{title}', lines {start}-{end}"
        if end - start + 1 <= DIVISION_WHOLE_LINES:
            lo, hi = start, end
        else:
            lo, hi = max(start, first - WINDOW_LINES), min(end, last + WINDOW_LINES)
    else:
        division = "no division marked in this edition"
        lo, hi = max(1, first - PLAIN_WINDOW_LINES), min(len(lines), last + PLAIN_WINDOW_LINES)
    chunk = list(lines[lo - 1: hi])
    chunk[first - lo] = CITED_OPEN + chunk[first - lo]
    chunk[last - lo] = chunk[last - lo] + CITED_CLOSE
    text = _clean("\n".join(chunk)) if name.endswith(".xml") else "\n".join(chunk)
    truncated = len(text) > PASSAGE_CHAR_LIMIT
    if truncated:
        at = max(0, text.find(CITED_OPEN) - PASSAGE_CHAR_LIMIT // 3)
        text = text[at: at + PASSAGE_CHAR_LIMIT]
    return {
        "file": name, "language": language, "status": "ok", "how_located": how, "division": division,
        "shown_lines": f"{lo}-{hi}", "cited_lines": f"{first}-{last}", "truncated": truncated, "text": text,
    }


def _render_value(value) -> str:
    if isinstance(value, list):
        return "\n".join(f"- {_render_value(v)}" for v in value)
    if isinstance(value, dict):
        return "\n".join(f"{k}: {_render_value(v)}" for k, v in value.items())
    return " ".join(str(value).split())


def voiced_fields(record: dict) -> tuple[str, ...]:
    """The fields the pack shows for a record: the fixed list, every field the
    engine's registry of spoken fields declares for the record's type as ground
    the voice says back or heads its evidence with, and the structured fields
    the voice also receives, less the fields only the citation card shows."""
    record_type = record.get("record_type")
    declared = fields_with_role(record_type, "voice-diet", "evidence-head")
    shown = dict.fromkeys((*VOICED_FIELDS, *declared, *ANSWER_FIELDS))
    return tuple(field for field in shown if field not in CARD_ONLY_FIELDS.get(record_type, ()))


def record_block(record: dict) -> str:
    rows = [f"record id: {record['id']}", f"record type: {record.get('record_type')}"]
    for field in LABEL_FIELDS:
        if record.get(field):
            rows.append(f"{field}: {_render_value(record[field])}")
    use = record.get("use_note") or {}
    if use.get("means"):
        rows.append(f"means: {_render_value(use['means'])}")
    if use.get("not_for"):
        rows.append("not for:\n" + _render_value(use["not_for"]))
    if record.get("claim_guards"):
        rows.append("claim guards:\n" + _render_value(record["claim_guards"]))
    confidence = record.get("confidence") or {}
    if confidence.get("formation_confidence"):
        rows.append(f"formation confidence: {confidence['formation_confidence']}")
    if confidence.get("divergence_note"):
        rows.append(f"divergence note: {_render_value(confidence['divergence_note'])}")
    for field in voiced_fields(record):
        if record.get(field):
            rows.append(f"{field}:\n{_render_value(record[field])}")
    if record.get("record_type") not in HEAD_TEXT_TYPES:
        rows.append("record text:\n" + all_text(record))
    return "\n".join(rows)


def lexicon_block(records: dict, bound: set[str] = frozenset()) -> str:
    """Every term's risk flags, the terms the item is bound to first. If the
    list must be shortened, the pack says so and names how many were left out."""
    terms = [r for r in records.values() if r.get("record_type") == "term"]
    terms.sort(key=lambda r: (r["id"] not in bound, r["id"]))
    rows = []
    for record in terms:
        risk = record.get("distortion_risk") or "unstated"
        line = f"- {record.get('world_word') or record['id']} (distortion risk: {risk})"
        if record.get("false_friend"):
            line += "; must not be read as: " + "; ".join(_render_value(f) for f in record["false_friend"])
        if record.get("plain_meaning"):
            line += f"; plain meaning: {_render_value(record['plain_meaning'])}"
        rows.append(line)
    kept, size = [], 0
    for line in rows:
        if size + len(line) > LEXICON_CHAR_LIMIT:
            break
        kept.append(line)
        size += len(line) + 1
    if len(kept) < len(rows):
        kept.append(f"(list shortened: {len(rows) - len(kept)} of {len(rows)} terms not shown)")
    return "\n".join(kept)


def _source_files(record: dict, records: dict) -> list[tuple[str, int | None, int | None]]:
    found = []
    for source in record.get("sources") or []:
        locus = source.get("locus") or ""
        named = loci(locus)
        if not named:
            source_record = records.get(source.get("source_id")) or {}
            text = " ".join(str(source_record.get(k) or "") for k in ("edition", "discovery_channel", "citation"))
            files = list(dict.fromkeys(m.group(1) for m in _FILE.finditer(text)))
            lines = _LINES.search(locus)
            if len(files) == 1 and lines:
                named = [(files[0], int(lines.group(1)), _full_last(lines.group(1), lines.group(2) or lines.group(1)))]
            else:
                named = [(name, None, None) for name in files]
        found.extend(named)
    return list(dict.fromkeys(found))


def build_pack(item: dict) -> dict:
    """The pack for one item, as blocks with ids (R1, R2 ... records; P1 ...
    passages; L the lexicon)."""
    records = records_at(item["records_commit"], item["world"])
    blocks = []
    for n, binding in enumerate(item["bindings"], start=1):
        record = records.get(binding["id"])
        if record is None:
            blocks.append({"id": f"R{n}", "kind": "record", "record_id": binding["id"], "text": "NO SUCH RECORD: the voice named a record the world does not have."})
            continue
        blocks.append({"id": f"R{n}", "kind": "record", "record_id": binding["id"], "text": record_block(record)})
        phrases = [m.group(1) for s in record.get("sources") or [] for m in _QUOTED.finditer(s.get("locus") or "")]
        phrases += [m.group(1) for m in _QUOTED.finditer(str(record.get("text") or ""))]
        if record.get("record_type") == "quote" and record.get("text"):
            phrases.insert(0, str(record["text"]))
        div_ids = [m.group(1) for s in record.get("sources") or [] for m in _DIV_ID.finditer(s.get("locus") or "")]
        sections = [(s.get("locus") or "", str((records.get(s.get("source_id")) or {}).get("work") or "")) for s in record.get("sources") or []]
        for name, first, last in _source_files(record, records):
            found = passage(item["records_commit"], name, first, last, phrases, div_ids, sections)
            blocks.append({"id": f"P{len([b for b in blocks if b['kind'] == 'passage']) + 1}", "kind": "passage", "for_record": f"R{n}", **found})
    blocks.append({"id": "L", "kind": "lexicon", "text": lexicon_block(records, {b["id"] for b in item["bindings"]})})
    return {"item_id": item["item_id"], "blocks": blocks}


def located(pack: dict) -> bool:
    return any(b["kind"] == "passage" and b["status"] == "ok" for b in pack["blocks"])


def render_pack(pack: dict) -> str:
    out = []
    for block in pack["blocks"]:
        if block["kind"] == "record":
            out.append(f"[{block['id']}] BOUND RECORD\n{block['text']}")
            missing = [b for b in pack["blocks"] if b["kind"] == "passage" and b["for_record"] == block["id"] and b["status"] != "ok"]
            if missing:
                out.append(f"(Source not shown for {block['id']}: " + "; ".join(f"{b['file']}: {b['status']}" for b in missing) + ")")
        elif block["kind"] == "passage":
            if block["status"] != "ok":
                continue
            head = f"[{block['id']}] SOURCE PASSAGE for {block['for_record']}: {block['file']} (language: {block['language']})"
            head += f"\n{block['division']}; shown lines {block['shown_lines']}; cited lines {block['cited_lines']} are marked {CITED_OPEN} ... {CITED_CLOSE}"
            if block["truncated"]:
                head += "; shortened to the part around the cited lines"
            out.append(f"{head}\n{block['text']}")
        else:
            out.append(f"[{block['id']}] THE WORLD'S LEXICON RISK FLAGS\n{block['text'] or '(none recorded)'}")
    return "\n\n".join(out)


def block_text(pack: dict, block_id: str) -> str | None:
    for block in pack["blocks"]:
        if block["id"] == block_id:
            return block.get("text")
    return None
