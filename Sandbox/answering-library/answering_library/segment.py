"""Segment one source file into addressable passages with their layers, and
classify how well the file's own markers divided it.

passage_id   cic:<filename>:<division_locus>#<NN>, NN the 1-based position
             of the passage inside its division, two digits or more.
ordinal      the same position as an integer.
byte range   half-open range of the first to the last token of the passage
             in the source file.
"""
from __future__ import annotations

import re
from bisect import bisect_left, bisect_right
from dataclasses import dataclass

from . import curation as cu
from . import markup as mu
from . import ocr, passages, plain, speaker
from .langscript import filename_codes, infer_default_language, language_of, script_of
from .textio import Source

CLEAN_MIN_DIVISIONS = 3
CLEAN_MAX_OVERSIZE = 0.10
CLEAN_MIN_COVER = 0.80
CLEAN_MIN_SEQUENTIALITY = 0.6
CLEAN_MIN_UNIQUE = 0.8
SHORT_FILE_WORDS = 1500
_HEADER_LANGUAGE = re.compile(r"^Language:\s*([a-z]{3})\b", re.M)


@dataclass
class UDiv:
    stream: str
    start: int
    end: int
    locus: str
    title: str
    apparatus: bool
    origin: str


class _Identity:
    def raw_pos_start(self, i: int) -> int:
        return i

    def raw_pos_end(self, j: int) -> int:
        return j


def distribution(values: list[int]) -> dict:
    if not values:
        return {"min": 0, "p10": 0, "median": 0, "p90": 0, "max": 0}
    v = sorted(values)

    def q(p):
        return v[min(len(v) - 1, int(p * (len(v) - 1) + 0.5))]

    return {"min": v[0], "p10": q(0.10), "median": q(0.5), "p90": q(0.90), "max": v[-1]}


def codes_for(filename: str, raw: str) -> list[str]:
    codes = filename_codes(filename)
    if codes:
        return codes
    m = _HEADER_LANGUAGE.search(raw[:6000])
    if m and m.group(1) in {"lat", "grc", "fra", "deu", "rus", "ita", "spa", "ces", "pol"}:
        return [m.group(1)]
    inferred = infer_default_language(raw[min(len(raw) // 5, 200000):])
    return [inferred] if inferred else []


def _header_chars(raw: str) -> int:
    lines = raw[:60000].split("\n")
    end = plain.mk.header_end(lines)
    return sum(len(ln) + 1 for ln in lines[:end])


def _unique(divs: list[UDiv]) -> None:
    seen: dict[str, int] = {}
    for d in divs:
        n = seen.get(d.locus, 0) + 1
        seen[d.locus] = n
        if n > 1:
            d.locus = f"{d.locus}~{n}"


def _markup_divisions(doc: mu.MarkupDoc) -> list[UDiv]:
    main_len, notes_len = len(doc.main.text), len(doc.notes.text)
    bounds = doc.boundaries
    divs: list[UDiv] = []
    if not bounds:
        return divs
    if bounds[0].main_pos > 0 and doc.main.text[:bounds[0].main_pos].strip():
        divs.append(UDiv("main", 0, bounds[0].main_pos, "front", "", True, "front"))
    if bounds[0].note_pos > 0 and doc.notes.text[:bounds[0].note_pos].strip():
        divs.append(UDiv("notes", 0, bounds[0].note_pos, "front/notes", "", True, "note"))
    for k, b in enumerate(bounds):
        nm = bounds[k + 1].main_pos if k + 1 < len(bounds) else main_len
        nn = bounds[k + 1].note_pos if k + 1 < len(bounds) else notes_len
        if doc.main.text[b.main_pos:nm].strip():
            divs.append(UDiv("main", b.main_pos, nm, b.locus, b.title, b.apparatus, "marker"))
        if doc.notes.text[b.note_pos:nn].strip():
            divs.append(UDiv("notes", b.note_pos, nn, f"{b.locus}/notes", b.title, True, "note"))
    return divs


def _subsplit(divs: list[UDiv], texts: dict[str, str]) -> list[UDiv]:
    out = []
    for d in divs:
        text = texts[d.stream]
        if d.origin in ("marker", "front", "note") and len(text[d.start:d.end].split()) > plain.SUBSPLIT_WORDS:
            for a, b in plain.pack_chars(text, d.start, d.end):
                out.append(UDiv(d.stream, a, b, f"{d.locus}/line{text.count(chr(10), 0, a) + 1}", d.title,
                                d.apparatus, "sub" if d.origin != "note" else "note"))
        else:
            out.append(d)
    return out


def classify_markers(word_counts: list[int], body_words: int, families: list[dict], markup: bool,
                     unique_share: float = 1.0) -> tuple[str, dict]:
    n = len(word_counts)
    over = sum(w for w in word_counts if w > plain.OVERSIZE_WORDS)
    tiny = sum(1 for w in word_counts if w < plain.TINY_WORDS)
    covered = sum(word_counts)
    evidence = {
        "divisions": n,
        "words_per_division": distribution(word_counts),
        "oversize_divisions": sum(1 for w in word_counts if w > plain.OVERSIZE_WORDS),
        "oversize_word_share": round(over / covered, 4) if covered else 0.0,
        "tiny_division_share": round(tiny / n, 4) if n else 0.0,
        "covered_word_share": round(covered / body_words, 4) if body_words else 0.0,
        "marker_patterns": families,
        "unique_locus_share": round(unique_share, 4),
        "short_file": body_words < SHORT_FILE_WORDS,
    }
    if n == 0:
        evidence["not_clean_because"] = ["no divisions found"]
        return "none", evidence
    reasons = []
    if n < CLEAN_MIN_DIVISIONS:
        reasons.append(f"fewer than {CLEAN_MIN_DIVISIONS} divisions")
    if evidence["oversize_word_share"] > CLEAN_MAX_OVERSIZE:
        reasons.append("oversize divisions hold more than 10% of marked text")
    if unique_share < CLEAN_MIN_UNIQUE:
        reasons.append("division addresses repeat")
    if not markup:
        numeric = [f for f in families if f["family"] != "caps"]
        if evidence["covered_word_share"] < CLEAN_MIN_COVER:
            reasons.append("markers cover under 80% of the text")
        if not numeric:
            reasons.append("only all-caps headings")
        elif any(f["sequentiality"] < CLEAN_MIN_SEQUENTIALITY for f in numeric):
            reasons.append("numbering not sequential")
        if evidence["tiny_division_share"] >= 0.5:
            reasons.append("half the divisions are under 30 words")
    evidence["not_clean_because"] = reasons
    evidence["clean_if_caps_headings_counted"] = reasons == ["only all-caps headings"]
    if not reasons:
        return "clean", evidence
    if n >= 2:
        return "partial", evidence
    return "none", evidence


@dataclass
class Curated:
    curation: cu.Curation
    resolved: cu.Resolved
    measure: dict
    work: str


@dataclass
class Plan:
    src: Source
    codes: list[str]
    markup_mode: bool
    streams: dict
    embedded: list[int]
    divs: list[UDiv]
    cls: str
    evidence: dict
    summary: dict
    furniture_words: int
    curated: Curated | None = None


AUTO = object()


def _fallback_class(measure: dict) -> str:
    return "partial" if measure["marker_divisions"] >= 2 else "none"


def _curated_plan(entry, src: Source, cur: cu.Curation) -> Plan:
    raw = src.text
    if entry.suffix == ".xml" or mu.looks_like_markup(raw):
        raise cu.CurationError(f"{cur.path.name}: curation applies to plain-text files only")
    lines = raw.split("\n")
    res = cu.resolve(cur, lines)
    work = "\n".join(" " * len(ln) if i in res.furniture else ln for i, ln in enumerate(lines))
    offsets = res.line_offsets
    divs = [UDiv("main", offsets[d.start], offsets[d.end], d.locus, d.title, d.apparatus, d.origin)
            for d in res.divisions]
    for e in cur.speakers:
        if e["state"] == "known" and e["voice"] not in entry.authors:
            raise cu.CurationError(f"{cur.path.name}: speaker voice '{e['voice']}' is not an author of {entry.filename}")
    m = cu.measure(res)
    reasons = cu.failures(m)
    _unique(divs)
    words = [d.words for d in res.divisions if d.origin != "header" and d.words > 0]
    evidence = {
        "divisions": m["divisions"],
        "words_per_division": distribution(words),
        "oversize_divisions": len(m["oversize_divisions"]),
        "covered_word_share": m["covered_word_share"],
        "unique_locus_share": round(1 - len(m["repeated_loci"]) / m["divisions"], 4) if m["divisions"] else 0.0,
        "rule_hits": res.rule_hits,
        "not_clean_because": reasons,
    }
    summary = {"mode": "plain", "furniture": {"lines": len(res.furniture), "words": res.furniture_words,
                                              "kinds": res.furniture_kinds},
               "curation": {"file": cur.path.name, "sha256": cur.sha256, "status": cur.status,
                            "curator": cur.curator, "scheme": cur.scheme}}
    codes = [cur.language] if cur.language else codes_for(entry.filename, raw)
    cls = "curated" if not reasons else _fallback_class(m)
    return Plan(src, codes, False, {"main": (work, _Identity())}, [], divs, cls, evidence, summary,
                res.furniture_words, Curated(cur, res, m, work))


def plan(entry, source: Source | None = None, curation=AUTO) -> Plan:
    """Divisions of one file. curation is AUTO (the file's curation, if it has an
    applicable one), None (heuristic markers only) or a Curation to apply."""
    src = source or Source.read(entry.path)
    cur = cu.for_file(entry.filename) if curation is AUTO else curation
    if cur is not None:
        return _curated_plan(entry, src, cur)
    raw = src.text
    codes = codes_for(entry.filename, raw)
    markup_mode = entry.suffix == ".xml" or mu.looks_like_markup(raw)

    streams: dict[str, tuple[str, object]]
    embedded: list[int] = []
    summary: dict = {"mode": "markup" if markup_mode else "plain"}
    furniture_words = 0

    if markup_mode:
        head_end = _header_chars(raw)
        doc = mu.parse(raw, head_end)
        embedded = doc.embedded
        streams = {"main": (doc.main.text, doc.main), "notes": (doc.notes.text, doc.notes),
                   "header": (raw, _Identity())}
        divs = _markup_divisions(doc)
        if head_end:
            divs.insert(0, UDiv("header", 0, head_end, "header", "", True, "header"))
        if divs:
            marker_words = [len(doc.main.text[d.start:d.end].split()) for d in divs
                            if d.stream == "main" and d.origin == "marker" and not d.apparatus]
            body_words = sum(marker_words)
            marker_args = (marker_words, body_words, [{"family": "markup-div", "n": len(marker_words),
                                                       "sequentiality": 1.0}], True)
            extra = {"apparatus_divisions": sum(1 for d in divs if d.stream == "main" and d.origin == "marker" and d.apparatus)}
        else:
            scheme = plain.analyse(doc.main.text)
            divs = [UDiv("main", d.start, d.end, d.locus, d.title, d.apparatus, d.origin) for d in scheme.divisions]
            if head_end:
                divs.insert(0, UDiv("header", 0, head_end, "header", "", True, "header"))
            streams["main"] = (scheme.work, doc.main)
            marker_args = (scheme.marker_division_words, scheme.body_words, scheme.families, False)
            extra = {}
            furniture_words = scheme.furniture_words
            summary["furniture"] = {"lines": len(scheme.furniture_lines), "words": furniture_words,
                                    "kinds": scheme.furniture_kinds}
        texts = {k: v[0] for k, v in streams.items()}
        extra["notes_stream_words"] = len(doc.notes.text.split())
        marker_loci = [d.locus for d in divs if d.origin == "marker" and d.stream == "main"]
        divs = _subsplit(divs, texts)
    else:
        scheme = plain.analyse(raw)
        streams = {"main": (scheme.work, _Identity())}
        divs = [UDiv("main", d.start, d.end, d.locus, d.title, d.apparatus, d.origin) for d in scheme.divisions]
        marker_args = (scheme.marker_division_words, scheme.body_words, scheme.families, False)
        extra = {"candidate_families": scheme.candidates}
        furniture_words = scheme.furniture_words
        summary["furniture"] = {"lines": len(scheme.furniture_lines), "words": furniture_words, "kinds": scheme.furniture_kinds}

    if not markup_mode:
        marker_loci = [d.locus for d in divs if d.origin == "marker"]
    unique_share = len(set(marker_loci)) / len(marker_loci) if marker_loci else 1.0
    cls, evidence = classify_markers(*marker_args, unique_share=unique_share)
    evidence.update(extra)
    _unique(divs)
    return Plan(src, codes, markup_mode, streams, embedded, divs, cls, evidence, summary, furniture_words)


def _speaker(cur, line, entry, d, ptext, words, embedded):
    override = cu.override_for(cur.speakers, line) if cur and not d.apparatus else None
    if override:
        return {"state": override["state"], "voice": override["voice"]}
    return speaker.classify(entry.filename, entry.authors, d.title, ptext, words, d.apparatus, embedded)


def segment(entry, vocab: ocr.Vocabulary | None = None, source: Source | None = None,
            curation=AUTO) -> tuple[list[dict], dict]:
    p = plan(entry, source, curation)
    src, codes, markup_mode, streams, embedded, divs = p.src, p.codes, p.markup_mode, p.streams, p.embedded, p.divs
    cls, evidence, summary, furniture_words = p.cls, p.evidence, p.summary, p.furniture_words
    raw = src.text
    cur = p.curated.curation if p.curated else None
    line_starts = p.curated.resolved.line_offsets if p.curated else None
    records: list[dict] = []
    for d in divs:
        text, mapper = streams[d.stream]
        spans = passages.token_spans(text, d.start, d.end)
        if not spans:
            continue
        words = [text[s:e] for s, e in spans]
        script_hint = script_of(" ".join(words[:300]))
        flags = passages.strengths(words, script_hint)
        cuts = passages.cut_points(len(words), flags)
        first = 0
        for nn, last in enumerate(cuts, start=1):
            ptext = " ".join(words[first:last])
            cs, ce = spans[first][0], spans[last - 1][1]
            rs, re_ = mapper.raw_pos_start(cs), mapper.raw_pos_end(ce)
            script = script_of(ptext)
            lang = language_of(ptext, script, codes)
            line = bisect_right(line_starts, cs) - 1 if cur else 0
            override = cu.override_for(cur.languages, line) if cur else None
            if override:
                lang = override["language"]
            emb = (bisect_right(embedded, ce) - bisect_left(embedded, cs)) if embedded and d.stream == "main" else 0
            parts = ocr.components(ptext, lang, script, vocab, text[cs:ce])
            records.append({
                "passage_id": f"cic:{entry.filename}:{d.locus}#{nn:02d}",
                "file": entry.filename,
                "division_locus": d.locus,
                "division_title": d.title,
                "ordinal": nn,
                "text": ptext,
                "word_count": last - first,
                "language": lang,
                "script": script,
                "apparatus": d.apparatus,
                "speaker": _speaker(cur, line, entry, d, ptext, last - first, emb),
                "ocr_score": ocr.score(parts),
                "byte_start": src.byte_of(rs),
                "byte_end": src.byte_of(re_),
                "row_ids": entry.row_ids,
                "worlds": entry.worlds,
            })
            first = last

    if p.curated:
        check = cu.verify(records, src, p.curated.work, furniture_words)
        reasons = cu.failures(p.curated.measure) + cu.verify_failures(check)
        evidence["not_clean_because"] = reasons
        evidence["completeness"] = check
        cls = "curated" if not reasons else _fallback_class(p.curated.measure)
    summary.update({
        "language_source": "filename" if filename_codes(entry.filename) else ("inferred" if codes else "default-eng"),
        "language_codes": codes,
        "class": cls,
        "evidence": evidence,
        "source_sha256": src.sha256,
        "source_bytes": len(src.data),
        "independent_word_count": (len(raw.split()) if not markup_mode
                                   else len(re.sub(r"<[^>]*>", " ", raw).split())),
        "independent_word_count_lower": len(re.sub(r"<[^>]*>", "", raw).split()) if markup_mode else None,
        "furniture_words": furniture_words,
    })
    return records, summary
