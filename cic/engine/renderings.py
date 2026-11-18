"""Check the records in cic/renderings/ against the vendored files they point to.

    python cic/engine/renderings.py --check
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
RENDERINGS = ROOT / "cic" / "renderings"
MAX_SECTIONS = 40
MAX_WORDS = 25


def _lines(path):
    return (ROOT / path).read_text(encoding="utf8").split("\n")


def _squash(text):
    return re.sub(r"\s+", " ", text).strip()


def _sentences(text):
    return [s for s in re.split(r"(?<=[.!?”\"])\s+", text.strip()) if s]


def check_guide(path, errors):
    doc = yaml.safe_load(path.read_text(encoding="utf8"))
    name = path.name
    target = ROOT / doc["file"]
    if not target.is_file():
        errors.append(f"{name}: no such file {doc['file']}")
        return
    if pathlib.Path(doc["file"]).stem != path.stem:
        errors.append(f"{name}: guide is not named after its text")
    total = len(_lines(doc["file"]))
    sections = doc["sections"]
    if len(sections) > MAX_SECTIONS:
        errors.append(f"{name}: {len(sections)} sections, more than {MAX_SECTIONS}")
    previous_end = None
    for section in sections:
        start, end = section["lines"]
        where = f"{name} {start}-{end}"
        if start > end or end > total:
            errors.append(f"{where}: lines outside the file")
        if previous_end is not None and start != previous_end + 1:
            errors.append(f"{where}: does not follow the section before it")
        previous_end = end
        for field in ("covers", "notable_footnotes"):
            for sentence in _sentences(section.get(field, "")):
                if len(sentence.split()) > MAX_WORDS:
                    errors.append(f"{where}: {field} has a sentence over {MAX_WORDS} words")
        for entry in section.get("names", []):
            if not start <= entry["line"] <= end:
                errors.append(f"{where}: name {entry['name']!r} is cited outside the section")
        for entry in section.get("quoted_authors", []):
            first, last = entry["lines"]
            if not (start <= first <= last <= end):
                errors.append(f"{where}: quotation by {entry['author']!r} is cited outside the section")
    if previous_end is not None and previous_end != total and previous_end != total - 1:
        errors.append(f"{name}: the last section ends at {previous_end}, the file at {total}")


def check_passages(path, errors):
    doc = yaml.safe_load(path.read_text(encoding="utf8"))
    name = path.name
    target = ROOT / doc["file"]
    if not target.is_file():
        errors.append(f"{name}: no such file {doc['file']}")
        return
    lines = _lines(doc["file"])
    seen = set()
    for passage in doc["passages"]:
        where = f"{name} {passage['id']}"
        if passage["id"] in seen:
            errors.append(f"{where}: id used twice")
        seen.add(passage["id"])
        start, end = passage["lines"]
        held = _squash(" ".join(lines[start - 1:end]))
        if _squash(passage["original"]) not in held:
            errors.append(f"{where}: original is not the file's text at {start}-{end}")
        for fault in passage.get("scan_faults", []):
            if not start <= fault["line"] <= end:
                errors.append(f"{where}: scan fault cited outside the passage")
            elif _squash(fault["scan"]) not in _squash(lines[fault["line"] - 1]):
                errors.append(f"{where}: scan fault {fault['scan']!r} is not on line {fault['line']}")
        for field in ("rendering", "second_rendering", "rendered", "second_rendered", "reviewed"):
            if not passage.get(field):
                errors.append(f"{where}: no {field}")
        for item in passage.get("uncertain", []):
            if not (item.get("first") and item.get("second")):
                errors.append(f"{where}: an uncertain reading does not keep both renderings")


def main():
    errors = []
    guides = sorted((RENDERINGS / "guides").glob("*.yaml"))
    passages = sorted((RENDERINGS / "passages").glob("*.yaml"))
    for path in guides:
        check_guide(path, errors)
    for path in passages:
        check_passages(path, errors)
    for error in errors:
        print("FAIL", error)
    print(f"{len(guides)} guides, {len(passages)} passage files, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
