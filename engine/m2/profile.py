"""The World Profile: a generated view over a world's records.

Sections follow Build/reference/L4-Templates/World_Profile_Template.md. Each
section draws only on the records that carry its content (world_core,
gravity, force, contested_claim, honest_limit, term, and the registry entry
for identity). A section no record carries is written as one plain line,
never with invented text. The view is not part of the compiled package.
"""
from __future__ import annotations

NOT_CARRIED = "Not carried by records."
GRAVITY_CLASSES = (("primary", "Primary"), ("supporting", "Supporting"), ("tensional", "Tensional"), (None, "Unclassified"))
SECTION_TITLES = (
    "World Identity",
    "Confirmed Gravities",
    "Formation Logic",
    "Ecological Summary",
    "Forces Summary",
    "Primary Vocabulary",
    "The World's Tensions",
    "Honest Limits",
    "Living Tradition Status",
    "Integrative Observation",
)


def _of_type(records: dict, record_type: str) -> list[dict]:
    return sorted((r for r in records.values() if r.get("record_type") == record_type), key=lambda r: r["id"])


def _text(value) -> str:
    return " ".join(str(value).split()) if value else ""


def _confidence(record: dict) -> str:
    return _text((record.get("confidence") or {}).get("formation_confidence")) or "not stated"


def _sources(record: dict) -> str:
    ids = [s.get("source_id") for s in (record.get("sources") or []) if isinstance(s, dict) and s.get("source_id")]
    return ", ".join(ids) if ids else "none recorded"


def _lines(label: str, value) -> list[str]:
    text = _text(value)
    return [f"**{label}:** {text}", ""] if text else []


def _bullets(label: str, items) -> list[str]:
    items = [_text(i) for i in (items or []) if _text(i)]
    return [f"**{label}:**", *[f"- {i}" for i in items], ""] if items else []


def _identity(records: dict, entry: dict, world_key: str) -> list[str] | None:
    core = next(iter(_of_type(records, "world_core")), {})
    window = entry.get("time_window") or core.get("time_window") or {}
    out: list[str] = []
    out += _lines("World name", entry.get("display_name"))
    out += _lines("World code", world_key)
    if window.get("start") is not None and window.get("end") is not None:
        out += _lines("Temporal scope", f"{window['start']}-{window['end']}")
    out += _lines("Geographic scope", entry.get("place"))
    out += _lines("Horizon", core.get("horizon"))
    return out or None


def _gravities(records: dict) -> list[str] | None:
    gravities = _of_type(records, "gravity")
    if not gravities:
        return None
    out: list[str] = []
    for key, label in GRAVITY_CLASSES:
        group = [g for g in gravities if g.get("classification") == key]
        if not group:
            continue
        out += [f"### {label} Gravities", ""]
        for g in group:
            out += [f"#### {_text(g.get('name')) or g['id']}", "", f"**Record:** {g['id']}", ""]
            out += _lines("Confidence", _confidence(g))
            out += _lines("Description", g.get("description"))
            out += _lines("Grounding", _sources(g))
    return out


def _formation_logic(records: dict) -> list[str] | None:
    core = next(iter(_of_type(records, "world_core")), {})
    out = _lines("Formation logic", core.get("formation_logic"))
    return out or None


def _forces(records: dict) -> list[str] | None:
    forces = _of_type(records, "force")
    if not forces:
        return None
    out: list[str] = []
    for f in sorted(forces, key=lambda r: (str(r.get("matrix_cell") or "~"), r["id"])):
        out += [f"### {_text(f.get('name')) or f['id']}", "", f"**Record:** {f['id']}", ""]
        out += _lines("Cell", f.get("matrix_cell"))
        out += _lines("Kind", f.get("kind"))
        out += _lines("Confidence", _confidence(f))
        out += _lines("Description", f.get("description"))
        linked = [r.get("target") for r in (f.get("relations") or []) if isinstance(r, dict) and ".gravity." in str(r.get("target"))]
        out += _lines("Gravity connection", ", ".join(linked))
    return out


def _vocabulary(records: dict) -> list[str] | None:
    terms = _of_type(records, "term")
    if not terms:
        return None
    out: list[str] = []
    for t in terms:
        out += [f"### {_text(t.get('world_word')) or t['id']}", "", f"**Record:** {t['id']}", ""]
        out += _lines("Plain meaning", t.get("plain_meaning"))
        out += _lines("Quick meaning", t.get("quick_meaning"))
        out += _lines("Distortion risk", t.get("distortion_risk"))
        out += _bullets("False friends", t.get("false_friend"))
    return out


def _tensions(records: dict) -> list[str] | None:
    tensional = [g for g in _of_type(records, "gravity") if g.get("classification") == "tensional"]
    claims = _of_type(records, "contested_claim")
    if not tensional and not claims:
        return None
    out: list[str] = []
    for g in tensional:
        out += [f"### {_text(g.get('name')) or g['id']}", "", f"**Record:** {g['id']}", ""]
        out += _lines("Confidence", _confidence(g))
        out += _lines("Nature", g.get("description"))
    for c in claims:
        out += [f"### Contested claim {c['id']}", ""]
        out += _lines("Claim", c.get("claim"))
        out += _lines("Confidence", _confidence(c))
        out += _bullets("Held against", c.get("held_against"))
        out += _lines("Concedes", c.get("concedes"))
    return out


def _honest_limits(records: dict) -> list[str] | None:
    core = next(iter(_of_type(records, "world_core")), {})
    limits = _of_type(records, "honest_limit")
    out = _lines("Thinness", core.get("thinness"))
    for h in limits:
        out += [f"### Honest limit {h['id']}", ""]
        out += _lines("Statement", h.get("statement"))
        out += _lines("Why the sources cannot answer", h.get("why_sources_cannot_answer"))
        out += _bullets("Nearest material", h.get("nearest_material"))
    return out or None


def _living_tradition(records: dict, entry: dict) -> list[str] | None:
    core = next(iter(_of_type(records, "world_core")), {})
    out = _lines("Living traditions", core.get("living_traditions"))
    if "living_tradition_flag" in entry:
        out += _lines("Registry flag", "true" if entry["living_tradition_flag"] else "false")
    return out or None


def _integrative(records: dict) -> list[str] | None:
    core = next(iter(_of_type(records, "world_core")), {})
    out = _lines("Integrative observation", core.get("integrative_observation"))
    return out or None


def build_profile(records: dict, entry: dict, world_key: str) -> str:
    """The profile as markdown, from the world's records and registry entry.
    Deterministic: the same inputs give the same bytes."""
    sections = (
        _identity(records, entry, world_key),
        _gravities(records),
        _formation_logic(records),
        None,
        _forces(records),
        _vocabulary(records),
        _tensions(records),
        _honest_limits(records),
        _living_tradition(records, entry),
        _integrative(records),
    )
    lines = [f"# World Profile: {_text(entry.get('display_name')) or world_key} ({world_key})", "", "Generated view over the world's records. Edit the records, not this file.", ""]
    for number, (title, body) in enumerate(zip(SECTION_TITLES, sections), 1):
        lines += [f"## Section {number}: {title}", ""]
        lines += body if body else [NOT_CARRIED, ""]
    carried = [str(n) for n, body in enumerate(sections, 1) if body]
    missing = [str(n) for n, body in enumerate(sections, 1) if not body]
    lines += ["## Section 11: World Profile Completion Status", ""]
    lines += [f"**Sections carried by records:** {', '.join(carried) or 'none'}", ""]
    lines += [f"**Sections not carried by records:** {', '.join(missing) or 'none'}", ""]
    lines += [f"**World Profile completion status:** {'COMPLETE' if not missing else 'INCOMPLETE'}", ""]
    return "\n".join(lines)
