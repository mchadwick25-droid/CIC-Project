"""Reads and surgically edits atlas-v3.html's embedded `const DATA = {...}`
object. Never reserializes the file: every write replaces only the exact
byte range of the field(s) being changed, re-indented to match the
surrounding structure, so an unrelated line never shows up in a diff.

Two prior bugs live in the corpus's own history as reasons for the care
here: a naive "field": search finds the first occurrence in an object's
text, which can be a nested occurrence (e.g. `sources` inside a
documentedStories item) rather than the object's own top-level property -
this module only ever matches a key at depth 1, directly inside the given
object. And json.dumps'ing a whole array/object back in without
re-indenting collapses it to one line, blowing up the diff against the
file's hand-formatted style - reindent_value fixes that up.
"""
import json
import re


def _skip_value(text: str, start: int) -> int:
    ch = text[start]
    if ch == '"':
        j = start + 1
        while j < len(text):
            if text[j] == '\\':
                j += 2
                continue
            if text[j] == '"':
                return j + 1
            j += 1
        raise ValueError("unterminated string")
    if ch in "[{":
        depth = 0
        j = start
        in_str = False
        while j < len(text):
            c = text[j]
            if in_str:
                if c == '\\':
                    j += 2
                    continue
                if c == '"':
                    in_str = False
            else:
                if c == '"':
                    in_str = True
                elif c in "[{":
                    depth += 1
                elif c in "]}":
                    depth -= 1
                    if depth == 0:
                        return j + 1
            j += 1
        raise ValueError("unterminated array/object")
    j = start
    while j < len(text) and text[j] not in ",}]\n":
        j += 1
    return j


def _find_top_level_key(obj_text: str, field: str):
    """(key_start, val_start) for "field" sitting directly inside obj_text's
    own outer braces (depth 1), or None. obj_text must span one full {...}."""
    i = obj_text.index("{")
    depth = 0
    in_str = False
    j = i
    n = len(obj_text)
    key_pat = f'"{field}"'
    while j < n:
        c = obj_text[j]
        if in_str:
            if c == "\\":
                j += 2
                continue
            if c == '"':
                in_str = False
            j += 1
            continue
        if c == '"':
            if depth == 1 and obj_text.startswith(key_pat, j):
                k = j + len(key_pat)
                while k < n and obj_text[k] in " \t\n":
                    k += 1
                if k < n and obj_text[k] == ":":
                    k += 1
                    while k < n and obj_text[k] in " \t\n":
                        k += 1
                    return (j, k)
            in_str = True
            j += 1
            continue
        if c in "[{":
            depth += 1
        elif c in "]}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return None


def _reindent(value, base_indent: int) -> str:
    s = json.dumps(value, ensure_ascii=False, indent=1)
    lines = s.split("\n")
    if len(lines) == 1:
        return s
    pad = " " * base_indent
    return lines[0] + "\n" + "\n".join(pad + l for l in lines[1:])


def _splice_field(obj_text: str, field: str, value) -> str:
    found = _find_top_level_key(obj_text, field)
    if found is None:
        return _insert_field(obj_text, field, value)
    key_start, val_start = found
    line_start = obj_text.rfind("\n", 0, key_start) + 1
    base_indent = key_start - line_start
    val_end = _skip_value(obj_text, val_start)
    new_str = _reindent(value, base_indent) if isinstance(value, (list, dict)) else json.dumps(value, ensure_ascii=False)
    return obj_text[:val_start] + new_str + obj_text[val_end:]


def _insert_field(obj_text: str, field: str, value) -> str:
    close_idx = obj_text.rstrip().rfind("}")
    # The closing brace's own leading whitespace (from the last newline
    # before it) has to be preserved explicitly - it sits between `before`
    # and `close_idx` and would otherwise be lost the moment `before` is
    # rstripped, leaving the closing brace unindented and every untouched
    # sibling object shifted one line in the diff.
    line_start = obj_text.rfind("\n", 0, close_idx) + 1
    closing_indent = obj_text[line_start:close_idx]
    if closing_indent.strip() == "":
        before = obj_text[:line_start]
    else:
        before, closing_indent = obj_text[:close_idx], ""
    prop_m = re.search(r"\n( +)\"", obj_text)
    if not prop_m:
        raise ValueError("cannot determine indentation for insertion")
    indent = prop_m.group(1)
    trimmed = before.rstrip()
    if not trimmed.endswith(","):
        trimmed += ","
    new_json = json.dumps(value, ensure_ascii=False, indent=1)
    lines = new_json.split("\n")
    reindented = lines[0] + ("\n" + "\n".join(indent + l for l in lines[1:]) if len(lines) > 1 else "")
    return f"{trimmed}\n{indent}\"{field}\": {reindented}\n{closing_indent}" + obj_text[close_idx:]


def _find_array_span(text: str, needle: str, from_const_data: bool) -> tuple[int, int]:
    start = text.find(needle, text.find("const DATA")) if from_const_data else text.find(needle)
    arr_start = text.find("[", start)
    depth = 0
    j = arr_start
    while j < len(text):
        c = text[j]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return arr_start, j + 1
        j += 1
    raise ValueError(f"unterminated array for {needle!r}")


def _movement_spans(text: str) -> list[tuple[int, int]]:
    arr_start, arr_end = _find_array_span(text, '"movements":', from_const_data=True)
    depth = 0
    i = arr_start
    obj_start = None
    spans = []
    while i < arr_end:
        c = text[i]
        if c == "{":
            if depth == 0:
                obj_start = i
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0 and obj_start is not None:
                spans.append((obj_start, i + 1))
                obj_start = None
        i += 1
    return spans


def read_movements(path) -> list[dict]:
    text = open(path, encoding="utf-8").read()
    arr_start, arr_end = _find_array_span(text, '"movements":', from_const_data=True)
    return json.loads(text[arr_start:arr_end])


def read_edges(path) -> list[dict]:
    text = open(path, encoding="utf-8").read()
    arr_start, arr_end = _find_array_span(text, '"edges":', from_const_data=True)
    return json.loads(text[arr_start:arr_end])


def apply_movement_updates(path, updates: dict[str, dict]) -> int:
    """updates: {movement_id: {field: new_value}}. Writes the file in place
    if anything changed. Returns the number of field values written."""
    if not updates:
        return 0
    text = open(path, encoding="utf-8").read()
    spans = _movement_spans(text)
    out = []
    last_end = 0
    field_edits = 0
    for start, end in spans:
        obj = text[start:end]
        idm = re.search(r'"id":\s*"([a-z0-9-]+)"', obj)
        mid = idm.group(1) if idm else None
        if mid not in updates:
            continue
        new_obj = obj
        for field, value in updates[mid].items():
            new_obj = _splice_field(new_obj, field, value)
            field_edits += 1
        out.append(text[last_end:start])
        out.append(new_obj)
        last_end = end
    out.append(text[last_end:])
    if field_edits:
        with open(path, "w", encoding="utf-8") as f:
            f.write("".join(out))
    return field_edits
