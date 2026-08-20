"""Applies one fixtures/seeded_defects.yaml entry's mutation to an in-memory
copy of the fixture world's records. Small, closed op vocabulary (see the
comment at the top of seeded_defects.yaml): set_field, delete_field,
add_field, remove_record.
"""

_CHUNK_FEEDING_TYPES = {"term", "story", "ambient", "doctrinal_witness"}


def _parse_token(token: str):
    if token.endswith("]") and "[" in token:
        base, rest = token.split("[", 1)
        return base, int(rest[:-1])
    return token, None


def _step(obj, token: str):
    base, idx = _parse_token(token)
    obj = obj[base]
    return obj[idx] if idx is not None else obj


def _resolve_container(record: dict, path: str):
    tokens = path.split(".")
    obj = record
    for token in tokens[:-1]:
        obj = _step(obj, token)
    base, idx = _parse_token(tokens[-1])
    return (obj[base], idx) if idx is not None else (obj, base)


def _find_id_by_path(records: dict, target_path: str) -> str:
    for rid, rec in records.items():
        if rec.get("_path") == target_path:
            return rid
    raise KeyError(f"no record with _path {target_path!r} in this copy")


def apply(records: dict, defect: dict) -> None:
    """Mutates `records` (an id -> record dict, already a deep copy the
    caller owns) in place per `defect`'s mutation spec."""
    mutation = defect.get("mutation")
    if mutation is None:
        return  # the inertness-proof entry: no single mutation, handled by selftest itself

    op = mutation["op"]

    if op == "remove_record":
        rid = _find_id_by_path(records, defect["target_record"])
        del records[rid]
        return

    if defect["id"] == "distribution-health-flattened-tiers":
        for rec in records.values():
            if rec.get("record_type") in _CHUNK_FEEDING_TYPES:
                rec.setdefault("retrieval", {})["tier"] = mutation["value"]
        return

    rid = _find_id_by_path(records, defect["target_record"])
    record = records[rid]

    if op in ("set_field", "add_field"):
        container, key = _resolve_container(record, mutation["path"])
        container[key] = mutation["value"]
    elif op == "delete_field":
        container, key = _resolve_container(record, mutation["path"])
        del container[key]
    else:
        raise ValueError(f"unknown mutation op {op!r} in defect {defect['id']!r}")
