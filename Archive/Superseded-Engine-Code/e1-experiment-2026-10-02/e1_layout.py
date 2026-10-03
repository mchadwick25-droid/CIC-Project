"""Prompt layouts for the E1 experiment. A world's compiled prompt is split
into its parts, and two alternative layouts are assembled from those exact
parts: the cell dossier (every record block the question's cells need, in
the compiler's own text) and the native-citation layout (the same record
blocks as API documents).

Nothing at runtime imports this module.

Structure of a compiled prompt (engine.m2.builders.build_prompt):

  header   the standing instruction sections and the ground line, then the
           world_core sections. None of these is a per-record block.
  blocks   one section per term, doctrinal witness, honest limit, story and
           demonstration, headed "... (cite as [[record.id]])".
  shared   the Gravities and Quotes lists, between the honest limits and the
           stories. They list many ids and belong to no single record, so
           they are kept under "section:<slug>" keys and carried by every
           layout.
  footer   any unkeyed sections after the last block.
"""
import re

BLOCK_HEADING = re.compile(
    r"^(?:Term: .+|Witness \(.*\)|Honest limit \(.*\)|Story|Demonstration) \(cite as \[\[([^\[\]\s]+)\]\]\)$"
)
SECTION_START = re.compile(r"^## ", re.MULTILINE)
SHARED_PREFIX = "section:"
VOICE_TYPES = ("term", "doctrinal_witness", "honest_limit", "story", "demonstration")
ALWAYS_TYPES = ("doctrinal_witness", "story")
MEANING_WIDTH = 120
NATIVE_CONTRACT = "Cite the record you drew on; the system records which document you used."

_CONTRACT_SECTION = re.compile(r"(## Citation contract\n\n)(.*?\n)(?=\n## )", re.DOTALL)
_CITE_AS = re.compile(r" \(cite as \[\[[^\[\]\s]+\]\]\)")


def _sections(prompt_text: str) -> list[tuple[str, str]]:
    starts = [m.start() for m in SECTION_START.finditer(prompt_text)]
    if not starts or starts[0] != 0:
        raise ValueError("compiled prompt does not open with a '## ' section")
    bounds = starts + [len(prompt_text)]
    return [(prompt_text[a:b].split("\n", 1)[0][3:], prompt_text[a:b]) for a, b in zip(starts, bounds[1:])]


def split_prompt(prompt_text: str) -> tuple[str, dict[str, str], str]:
    """(header, blocks, footer). header + "".join(blocks.values()) + footer is
    prompt_text exactly; blocks keeps the prompt's order."""
    sections = _sections(prompt_text)
    first = next((i for i, (heading, _) in enumerate(sections) if BLOCK_HEADING.match(heading)), None)
    if first is None:
        raise ValueError("compiled prompt has no per-record blocks")
    last = max(i for i, (heading, _) in enumerate(sections) if BLOCK_HEADING.match(heading))
    header = "".join(text for _, text in sections[:first])
    footer = "".join(text for _, text in sections[last + 1:])
    blocks: dict[str, str] = {}
    for heading, text in sections[first:last + 1]:
        match = BLOCK_HEADING.match(heading)
        key = match.group(1) if match else SHARED_PREFIX + re.sub(r"[^a-z0-9]+", "-", heading.split(" (")[0].lower()).strip("-")
        if key in blocks:
            raise ValueError(f"compiled prompt carries {key!r} twice")
        blocks[key] = text
    return header, blocks, footer


def is_shared(key: str) -> bool:
    return key.startswith(SHARED_PREFIX)


def _label(block_text: str) -> str:
    heading = block_text.split("\n", 1)[0][3:]
    return _CITE_AS.sub("", heading)


def _squash(text: str, width: int = MEANING_WIDTH) -> str:
    flat = " ".join(str(text or "").split())
    return flat if len(flat) <= width else flat[: width - 3].rstrip() + "..."


def _meaning(record: dict) -> str:
    kind = record.get("record_type")
    if kind == "term":
        return _squash(record.get("quick_meaning") or record.get("plain_meaning"))
    if kind == "honest_limit":
        return _squash(record.get("statement"))
    if kind == "story":
        return _squash(record.get("tellable_as") or record.get("text"))
    if kind == "demonstration":
        asked = next((t["text"] for t in record.get("exchange") or [] if t.get("speaker") == "participant"), "")
        return _squash(asked)
    return _squash(record.get("summary") or record.get("text"))


def index_lines(records: dict[str, dict], blocks: dict[str, str] | None = None, *, bracket: bool = True) -> list[str]:
    """One line per voice record: id, label, a short meaning, canon cells.
    With blocks given, only records that have a block are listed and the
    label is the block's own heading. Sorted by id."""
    lines = []
    for record_id in sorted(records):
        record = records[record_id]
        if record.get("record_type") not in VOICE_TYPES:
            continue
        if blocks is not None and record_id not in blocks:
            continue
        label = _label(blocks[record_id]) if blocks is not None else str(record.get("world_word") or record.get("record_type"))
        marker = f"[[{record_id}]]" if bracket else record_id
        cells = ",".join(record.get("canon_cells") or []) or "-"
        lines.append(f"- {marker} {label} | {_meaning(record)} | cells: {cells}")
    return lines


def dossier_ids(records: dict[str, dict], cells, blocks: dict[str, str] | None = None) -> set[str]:
    """Voice records whose canon_cells meet `cells`, plus every doctrinal
    witness and story. With blocks given, only records that have a block."""
    wanted = set(cells)
    chosen = set()
    for record_id, record in records.items():
        kind = record.get("record_type")
        if kind not in VOICE_TYPES:
            continue
        if kind in ALWAYS_TYPES or wanted & set(record.get("canon_cells") or []):
            chosen.add(record_id)
    if blocks is not None:
        chosen &= set(blocks)
    return chosen


def _index_section(records: dict[str, dict], blocks: dict[str, str], intro: str, *, bracket: bool) -> str:
    lines = index_lines(records, blocks, bracket=bracket)
    return "## Index\n\n" + intro + "\n\n" + "\n".join(lines) + "\n"


_INDEX_INTRO_C = (
    "Every record of our world, one line each. The full text of the records this question needs follows, "
    "each under its own heading; the records not printed in full are listed here only."
)
_INDEX_INTRO_NATIVE = (
    "Every record of our world, one line each. The full text of the records this question needs arrives "
    "as documents with the question; the records not attached are listed here only."
)


def assemble_c(prompt_text: str, records: dict[str, dict], cells) -> str:
    header, blocks, footer = split_prompt(prompt_text)
    keep = dossier_ids(records, cells, blocks)
    body = "".join(text for key, text in blocks.items() if is_shared(key) or key in keep)
    index = _index_section(records, blocks, _INDEX_INTRO_C, bracket=True)
    return header + "\n" + index + "\n" + body + footer


def replace_citation_contract(header: str) -> tuple[str, str]:
    """(header with the Citation contract body replaced, the replaced text)."""
    found = _CONTRACT_SECTION.findall(header)
    if len(found) != 1:
        raise ValueError(f"expected exactly one Citation contract section, found {len(found)}")
    replaced = found[0][1]
    return _CONTRACT_SECTION.sub(lambda m: m.group(1) + NATIVE_CONTRACT + "\n", header, count=1), replaced


def document_text(block_text: str) -> str:
    """A record block with its '(cite as [[id]])' marker removed."""
    head, sep, rest = block_text.partition("\n")
    return _CITE_AS.sub("", head) + sep + rest


def assemble_native(prompt_text: str, records: dict[str, dict], cells) -> tuple[str, list[dict]]:
    header, blocks, footer = split_prompt(prompt_text)
    keep = dossier_ids(records, cells, blocks)
    header, _ = replace_citation_contract(header)
    shared = "".join(text for key, text in blocks.items() if is_shared(key))
    index = _index_section(records, blocks, _INDEX_INTRO_NATIVE, bracket=False)
    system = header + "\n" + index + "\n" + shared + footer
    documents = [
        {
            "type": "document",
            "source": {"type": "text", "media_type": "text/plain", "data": document_text(text)},
            "title": key,
            "citations": {"enabled": True},
        }
        for key, text in blocks.items()
        if key in keep
    ]
    return system, documents


_LIST_ITEM = re.compile(r"^- \[\[([^\[\]\s]+)\]\] (.*)$", re.MULTILINE)


def assemble_native_whole(prompt_text: str) -> tuple[str, list[dict]]:
    """Today's whole-world prompt with every record as an API document: each
    per-record block, and each line of the shared Gravities and Quotes lists,
    becomes one document titled with its record id. The system prompt keeps
    the header, with the Citation contract body replaced, and the footer."""
    header, blocks, footer = split_prompt(prompt_text)
    header, _ = replace_citation_contract(header)
    documents = []
    for key, text in blocks.items():
        if is_shared(key):
            heading = text.split("\n", 1)[0][3:]
            for record_id, line in _LIST_ITEM.findall(text):
                documents.append(_document(record_id, f"{heading}\n{line}"))
        else:
            documents.append(_document(key, document_text(text)))
    if documents:
        documents[-1] = {**documents[-1], "cache_control": {"type": "ephemeral"}}
    return header + footer, documents


def _document(record_id: str, text: str) -> dict:
    return {
        "type": "document",
        "source": {"type": "text", "media_type": "text/plain", "data": text},
        "title": record_id,
        "citations": {"enabled": True},
    }


def manifest(arm: str, cells, ids, prompt_chars: int) -> dict:
    return {"arm": arm, "cells": list(cells), "dossier_ids": sorted(ids), "prompt_chars": prompt_chars}
