"""Deployed-artifact gates.

  deployed   the compiled prompt carries every confirmed item and the
             approved-source anchoring paragraph, and its rule counts equal
             the records; the pinned package is not stale
  citations  every record id and cic/texts path a document names resolves,
             and is the right record type for how it is cited
  probes     the probe runner tests only packages/<code>/<pin>/compiled/
             prompt.txt, and every saved probe-results file names its pin

The one artifact ever tested is the compiled prompt. assert_compiled_target
refuses everything else.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import re
from pathlib import Path

import yaml

from engine.m2.loader_stub import PackageRefused

from .common import REPO_ROOT, Finding, Report, emit, read_text, registry_entry, rel

PIN_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z")
_LEGACY_NAME = re.compile(r"permanent[_ ]?prompt|capsule", re.IGNORECASE)
_LEGACY_TREES = ("Build", "Archive")

SELF_REFERENCE_STEMS = (
    ("no invented memory", re.compile(r"no invented memory", re.I)),
    ("no explaining what kind of thing is speaking", re.compile(r"no explaining what kind of thing is speaking", re.I)),
    ("no narrating our own refusal or act of declining", re.compile(r"no narrating our own (?:act of declining|refusal)", re.I)),
    ("no 'I' smuggled in through a list of named roles", re.compile(r"smuggled in through a list of named roles", re.I)),
)
CONFIRMED_WORLD_CORE_FIELDS = ("living_traditions", "telos")
SOURCE_ANCHOR_BOUNDS = (5, 10)

_NUM_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
}
_TENS = "twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety"
_UNITS = "one|two|three|four|five|six|seven|eight|nine"
_NUM = rf"(?:\d+|(?:{_TENS})(?:[- ](?:{_UNITS}))?|{'|'.join(k for k in _NUM_WORDS if k not in _TENS.split('|') and k != 'hundred')}|hundred)"

_COUNTED_TYPES = {
    "quote": r"quotes?",
    "story": r"stor(?:y|ies)",
    "term": r"terms?",
    "gravity": r"gravit(?:y|ies)",
    "force": r"forces?",
    "figure": r"figures?",
    "doctrinal_witness": r"doctrinal[_ ]witness(?:es)?",
    "honest_limit": r"honest[_ ]limits?",
    "contested_claim": r"contested[_ ]claims?",
    "demonstration": r"demonstrations?",
}
_QUOTATION_COUNT = re.compile(
    rf"\b({_NUM})\b(?:\s+\w+){{0,6}}?\s+(?:quotes?|quotations?|records?|exist|named)\b", re.IGNORECASE
)


class ProbeTargetRefused(PackageRefused):
    """A probe or live run was pointed at something other than a compiled prompt."""


def assert_compiled_target(path) -> Path:
    """Return the resolved path when it is a compiled package prompt; raise
    ProbeTargetRefused for a legacy Permanent Prompt or Capsule file, for
    anything under Build/ or Archive/, and for any other shape. Inside the
    repository only <code>/<pin>/compiled/prompt.txt under a directory named
    packages is accepted: packages/ itself, or a package cache kept there."""
    target = Path(path).resolve()
    if _LEGACY_NAME.search(str(target.name)) or any(_LEGACY_NAME.search(part) for part in target.parts[-4:]):
        raise ProbeTargetRefused(f"{target}: a legacy prompt or capsule file is never a test target")
    if target.name != "prompt.txt" or target.parent.name != "compiled":
        raise ProbeTargetRefused(f"{target}: not a compiled/prompt.txt")
    try:
        inside = target.relative_to(REPO_ROOT).parts
    except ValueError:
        return target
    if any(part in _LEGACY_TREES for part in inside):
        raise ProbeTargetRefused(f"{target}: files under {next(p for p in inside if p in _LEGACY_TREES)}/ are never a test target")
    if not (len(inside) >= 5 and inside[-5] == "packages"):
        raise ProbeTargetRefused(f"{target}: only <code>/<pin>/compiled/prompt.txt under packages/ is a test target")
    return target


# ---- records and package access ------------------------------------------------------------------


def _parse_record(path: Path) -> dict | None:
    lines = read_text(path).splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        close = lines[1:].index("---") + 1
        record = yaml.safe_load("\n".join(lines[1:close])) or {}
    except (ValueError, yaml.YAMLError):
        return None
    return record if isinstance(record, dict) else None


def load_records(code: str, root: Path = REPO_ROOT) -> dict[str, dict]:
    base = root / "records" / code
    records: dict[str, dict] = {}
    if not base.is_dir():
        return records
    for path in sorted(base.glob("*/*.md")):
        record = _parse_record(path)
        if record and record.get("id"):
            record["_path"] = rel(path, root)
            records[record["id"]] = record
    return records


def world_codes(root: Path = REPO_ROOT) -> list[str]:
    base = root / "records"
    return sorted(p.name for p in base.iterdir() if p.is_dir() and p.name != "worlds") if base.is_dir() else []


def _by_type(records: dict[str, dict], record_type: str) -> list[dict]:
    return [r for r in records.values() if r.get("record_type") == record_type]


def resolve_pin(code: str, root: Path = REPO_ROOT) -> tuple[dict, Path, str] | None:
    entry = registry_entry(code, root)
    location = ((entry or {}).get("package") or {}).get("location")
    if not location:
        return None
    package_dir = root / location
    return entry, package_dir, package_dir.name


def _sha256(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def recompile_pinned(code: str, package_dir: Path) -> dict[str, bytes]:
    from engine.m2.checks import _compiler_version_from
    from engine.m2.compiler import compile_world

    manifest = json.loads((package_dir / "manifest.json").read_bytes())
    return compile_world(
        world_key=code,
        package_id=manifest["package_id"],
        records_commit=manifest["records_commit"],
        compiler_version=_compiler_version_from(manifest),
    )


def _prompt_text(code: str, package_dir: Path, pin_path: str) -> tuple[str | None, str, list[Finding]]:
    """The pinned package's prompt text and where it came from. The compiled
    bytes are not committed, so a missing file is recompiled in memory from
    the pin's own manifest."""
    manifest_path = package_dir / "manifest.json"
    if not manifest_path.is_file():
        return None, "", [Finding(pin_path, "k:package-missing", "the pinned package has no manifest.json")]
    prompt_path = package_dir / "compiled" / "prompt.txt"
    manifest = json.loads(manifest_path.read_bytes())
    if prompt_path.is_file():
        assert_compiled_target(prompt_path)
        payload = prompt_path.read_bytes()
        expected = (manifest.get("files") or {}).get("compiled/prompt.txt")
        found = []
        if expected != _sha256(payload):
            found.append(Finding(pin_path, "k:prompt-hash", f"compiled/prompt.txt on disk does not match its manifest hash {expected}"))
        return payload.decode("utf-8"), "read from disk", found
    return recompile_pinned(code, package_dir)["compiled/prompt.txt"].decode("utf-8"), "recompiled in memory from the pin's manifest", []


def staleness_findings(code: str, entry: dict, root: Path, pin_path: str) -> tuple[list[Finding], list[str]]:
    from engine.m2.checks import STALENESS_CHECKABLE_STATES, staleness_sweep

    if entry.get("state") not in STALENESS_CHECKABLE_STATES:
        return [], [f"staleness not checked: registry state is {entry.get('state')!r}"]
    result = staleness_sweep({code: entry}, repo_root=root).get(code) or {}
    if result.get("stale"):
        detail = result.get("reason") or "differs from records: " + ", ".join(result.get("diff") or [])
        return [Finding(pin_path, "k:stale", f"the pinned package is stale versus records ({detail})")], []
    return [], []


# ---- (k) compiled prompt content -----------------------------------------------------------------


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().lower()


def _section(prompt: str, header_prefix: str) -> str | None:
    lines = prompt.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"## {header_prefix}"):
            end = next((j for j in range(index + 1, len(lines)) if lines[j].startswith("## ")), len(lines))
            return "\n".join(lines[index + 1 : end])
    return None


def _num(token: str) -> int:
    token = token.lower()
    if token.isdigit():
        return int(token)
    parts = re.split(r"[- ]", token)
    return sum(_NUM_WORDS[p] for p in parts)


def _grandfathered() -> frozenset[str]:
    from engine.m9.enforce import GRANDFATHERED_WORLDS

    return GRANDFATHERED_WORLDS


def check_source_anchor(code: str, prompt: str, records: dict[str, dict], where: str) -> tuple[list[Finding], list[str]]:
    """The approved-source anchoring paragraph: voice_craft.source_anchor is
    set, it stands as its own section of the compiled prompt, and it is drawn
    from 5 to 10 entries (voice_craft.source_anchor_entries), each named in
    it. A grandfathered world without the paragraph gets a note; any other
    world fails."""
    from engine.m2.builders import SOURCE_ANCHOR_HEADER

    findings: list[Finding] = []
    notes: list[str] = []
    craft = next(iter(_by_type(records, "voice_craft")), None)
    anchor = (craft or {}).get("source_anchor")
    if not (isinstance(anchor, str) and anchor.strip()):
        reason = "voice_craft has no source_anchor, so the compiled prompt carries no approved-source anchoring paragraph"
        if code in _grandfathered():
            notes.append(f"source_anchor: {reason} (grandfathered world)")
        else:
            findings.append(Finding(where, "k:source-anchor", reason))
        return findings, notes
    section = _section(prompt, SOURCE_ANCHOR_HEADER)
    if section is None or _norm(section) != _norm(anchor):
        findings.append(Finding(where, "k:source-anchor", f"voice_craft.source_anchor is in the records but the compiled prompt has no '{SOURCE_ANCHOR_HEADER}' section holding it verbatim"))
    entries = [e for e in (craft.get("source_anchor_entries") or []) if isinstance(e, str) and e.strip()]
    low, high = SOURCE_ANCHOR_BOUNDS
    distinct = {_norm(e) for e in entries}
    if not low <= len(distinct) <= high:
        findings.append(Finding(where, "k:source-anchor-entries", f"source_anchor_entries names {len(distinct)} distinct entries; the anchoring paragraph is drawn from {low} to {high} Native Source Registry entries"))
    for entry in entries:
        if _norm(entry) not in _norm(anchor):
            findings.append(Finding(where, "k:source-anchor-entries", f"entry {entry!r} is not named in source_anchor"))
    return findings, notes


def check_prompt_content(code: str, prompt: str, records: dict[str, dict], entry: dict, where: str) -> tuple[list[Finding], list[str]]:
    findings: list[Finding] = []
    notes: list[str] = []
    normalized = _norm(prompt)

    core = next(iter(_by_type(records, "world_core")), None)
    for name in CONFIRMED_WORLD_CORE_FIELDS:
        value = (core or {}).get(name)
        if isinstance(value, str) and value.strip():
            if _norm(value) not in normalized:
                findings.append(Finding(where, f"k:{name.replace('_', '-')}", f"world_core.{name} is in the records but not verbatim in the compiled prompt"))
        elif name == "telos":
            notes.append("telos: world_core has no telos field and the schema defines none, so nothing can be checked")
        elif entry.get("living_tradition_flag"):
            reason = "the registry flags a living tradition but world_core has no living_traditions text, so the confirmed determination is missing from the prompt"
            if code in _grandfathered():
                notes.append(f"living_traditions: {reason}")
            else:
                findings.append(Finding(where, "k:living-traditions", reason))

    anchor_findings, anchor_notes = check_source_anchor(code, prompt, records, where)
    findings.extend(anchor_findings)
    notes.extend(anchor_notes)

    bullet = next((ln for ln in prompt.splitlines() if ln.lstrip().startswith("- [self-reference]")), None)
    if bullet is None:
        findings.append(Finding(where, "k:self-reference", "the compiled prompt has no [self-reference] note"))
    else:
        for label, pattern in SELF_REFERENCE_STEMS:
            if not pattern.search(bullet):
                findings.append(Finding(where, "k:self-reference", f"the [self-reference] note lacks the hardening rule: {label}"))

    for section_header, record_type in (("Quotes we hold", "quote"), ("Gravities", "gravity")):
        actual = {r["id"] for r in _by_type(records, record_type)}
        body = _section(prompt, section_header)
        listed = set(re.findall(r"\[\[([^\]]+)\]\]", body)) if body is not None else set()
        if body is None and actual:
            findings.append(Finding(where, f"k:{record_type}-index", f"the prompt has no '{section_header}' section but the records hold {len(actual)} {record_type} records"))
            continue
        if listed != actual:
            missing, extra = sorted(actual - listed), sorted(listed - actual)
            findings.append(Finding(where, f"k:{record_type}-index", f"'{section_header}' lists {len(listed)} ids, records hold {len(actual)}; missing {missing[:3]}{'...' if len(missing) > 3 else ''}, unknown {extra[:3]}{'...' if len(extra) > 3 else ''}"))

    quote_total = len(_by_type(records, "quote"))
    quotation = next((ln for ln in prompt.splitlines() if ln.lstrip().startswith("- [quotation]")), "")
    for match in _QUOTATION_COUNT.finditer(quotation):
        stated = _num(match.group(1))
        if match.group(1).lower() != "one" and stated != quote_total:
            findings.append(Finding(where, "k:quote-count", f"the [quotation] note states {stated} ('{match.group(0)}'), records/{code}/quote holds {quote_total}"))
    for record_type, noun in _COUNTED_TYPES.items():
        pattern = re.compile(rf"\b({_NUM})\s+(?:checked\s+|verbatim\s+)?{noun}\s+records?\b", re.IGNORECASE)
        actual_count = len(_by_type(records, record_type))
        for match in pattern.finditer(prompt):
            if _num(match.group(1)) != actual_count:
                findings.append(Finding(where, f"k:{record_type.replace('_', '-')}-count", f"the prompt states '{match.group(0)}', the records hold {actual_count}"))
    return findings, notes


def check_deployed(code: str, root: Path = REPO_ROOT, *, check_stale: bool = True) -> Report:
    report = Report("deployed")
    resolved = resolve_pin(code, root)
    if resolved is None:
        report.findings.append(Finding(f"records/worlds/{code}.yaml", "k:no-pin", "no registry entry or package.location for this world"))
        return report
    entry, package_dir, pin = resolved
    pin_path = rel(package_dir / "compiled" / "prompt.txt", root)
    records = load_records(code, root)
    if not records:
        report.findings.append(Finding(f"records/{code}", "k:no-records", "no records found for this world"))
        return report
    prompt, source, problems = _prompt_text(code, package_dir, pin_path)
    report.findings.extend(problems)
    if prompt is not None:
        report.notes.append(f"pin {pin}: prompt {source}")
        found, notes = check_prompt_content(code, prompt, records, entry, pin_path)
        report.findings.extend(found)
        report.notes.extend(notes)
    if check_stale and (package_dir / "manifest.json").is_file():
        found, notes = staleness_findings(code, entry, root, pin_path)
        report.findings.extend(found)
        report.notes.extend(notes)
    return report


# ---- (d) citations -------------------------------------------------------------------------------

_TYPE_WORDS = {
    "quote": {"quote"}, "gravity": {"gravity"}, "gravities": {"gravity"}, "term": {"term"}, "story": {"story"},
    "force": {"force"}, "figure": {"figure"}, "honest limit": {"honest_limit"}, "honest_limit": {"honest_limit"},
    "doctrinal witness": {"doctrinal_witness"}, "doctrinal_witness": {"doctrinal_witness"}, "witness": {"doctrinal_witness"},
    "contested claim": {"contested_claim"}, "contested_claim": {"contested_claim"},
    "demonstration": {"demonstration"}, "demo": {"demonstration"}, "source": {"source"},
}
_TEXT_PATH = re.compile(r"cic/texts/[\w\-./]+?\.(?:txt|xml)")


def _id_core(codes: list[str]) -> str:
    alternatives = "|".join(re.escape(c) for c in sorted(codes, key=len, reverse=True))
    return rf"(?:{alternatives})\.[a-z_]+\.[a-z0-9][a-z0-9\-]*(?:\.[a-z0-9][a-z0-9\-]*)*"


def _id_pattern(codes: list[str]) -> str:
    return rf"(?<![\w.\-]){_id_core(codes)}"


def check_citations(code: str, files: list[Path], root: Path = REPO_ROOT) -> Report:
    report = Report("citations")
    codes = sorted(set(world_codes(root)) | {code})
    loaded: dict[str, dict[str, dict]] = {}

    def records_of(prefix: str) -> dict[str, dict]:
        if prefix not in loaded:
            loaded[prefix] = load_records(prefix, root)
        return loaded[prefix]

    token = re.compile(_id_pattern(codes))
    typed = re.compile(
        r"\b(?P<word>" + "|".join(sorted((re.escape(w).replace(r"\ ", r"[ _]") for w in _TYPE_WORDS), key=len, reverse=True))
        + r")(?:_ids?)?s?(?:\s+record)?\s*[:=]?\s*[`\[(\"'“]*(?P<id>" + _id_core(codes) + ")",
        re.IGNORECASE,
    )
    for path in files:
        where = rel(path, root)
        if not path.is_file():
            report.findings.append(Finding(where, "d:file-missing", "the named document does not exist"))
            continue
        text = read_text(path)
        seen: set[tuple[str, str]] = set()

        def resolve(raw: str) -> dict | None:
            identifier = raw[:-3] if raw.endswith(".md") else raw
            return records_of(identifier.split(".", 1)[0]).get(identifier)

        for match in token.finditer(text):
            raw = match.group(0)
            identifier = raw[:-3] if raw.endswith(".md") else raw
            if ("id", identifier) in seen:
                continue
            seen.add(("id", identifier))
            if resolve(identifier) is not None:
                continue
            prefix, namespace, slug = identifier.split(".", 2)
            siblings = [
                rid for rid, rec in records_of(prefix).items()
                if rid.split(".", 2)[2] == slug
            ]
            if siblings:
                report.findings.append(Finding(where, "d:wrong-namespace", f"{identifier} does not exist; the slug exists as {siblings[0]}"))
                continue
            close = difflib.get_close_matches(identifier, [r for r in records_of(prefix) if r.split(".")[1] == namespace], n=1, cutoff=0.8)
            hint = f" (nearest: {close[0]})" if close else ""
            report.findings.append(Finding(where, "d:unknown-id", f"{identifier} is not a record{hint}"))

        for match in typed.finditer(text):
            raw = match.group("id")
            identifier = raw[:-3] if raw.endswith(".md") else raw
            record = resolve(identifier)
            word = re.sub(r"[ _]", " ", match.group("word").lower())
            wanted = _TYPE_WORDS.get(word) or _TYPE_WORDS.get(word.replace(" ", "_"))
            if record is None or not wanted:
                continue
            if record.get("record_type") not in wanted and ("type", identifier, word) not in seen:
                seen.add(("type", identifier, word))
                report.findings.append(Finding(where, "d:wrong-type", f"cited as a {word} but {identifier} is a {record.get('record_type')} record"))

        for match in _TEXT_PATH.finditer(text):
            if ("text", match.group(0)) in seen:
                continue
            seen.add(("text", match.group(0)))
            if not (root / match.group(0)).is_file():
                report.findings.append(Finding(where, "d:unknown-text", f"{match.group(0)} is not a vendored edition"))
    return report


# ---- (l) probes ----------------------------------------------------------------------------------

_RESULT_NAME = re.compile(r"phase5|phased|probe[_ ]?result|validation[_ ]attestation", re.IGNORECASE)
_NOT_RESULT_NAME = re.compile(r"review|spotcheck|spot_check|scoping|template", re.IGNORECASE)


def probe_result_files(code: str, root: Path = REPO_ROOT) -> list[Path]:
    base = root / "Build" / "worlds" / code
    if not base.is_dir():
        return []
    return sorted(
        p for p in base.rglob("*")
        if p.is_file() and p.suffix in {".md", ".json"} and _RESULT_NAME.search(p.name) and not _NOT_RESULT_NAME.search(p.name)
    )


def citation_files(code: str, root: Path = REPO_ROOT) -> list[Path]:
    """The world's build documents (its top-level markdown files, review files
    aside) and every probe-results file."""
    base = root / "Build" / "worlds" / code
    documents = [p for p in sorted(base.glob("*.md")) if not _NOT_RESULT_NAME.search(p.name)] if base.is_dir() else []
    return sorted({*documents, *probe_result_files(code, root)})


_TESTED_ARTIFACT = re.compile(r"^[\s>*_-]*tested artifact\b.*$", re.IGNORECASE | re.MULTILINE)


def tested_pins(text: str) -> tuple[set[str], bool]:
    """(pins, from_line): the pins on the file's `Tested artifact` line or
    lines, or, when it has none, every pin the file names."""
    lines = _TESTED_ARTIFACT.findall(text)
    if lines:
        return {pin for line in lines for pin in PIN_RE.findall(line)}, True
    return set(PIN_RE.findall(text)), False


def pin_not_current(text: str, where: str, current: str | None, check: str) -> list[Finding]:
    """A finding when the tested pin is not the world's current package pin.
    A `Tested artifact` line must name the current pin and no other; a file
    without one must at least name it."""
    if current is None:
        return [Finding(where, check, "the world has no current package pin to compare the tested pin with")]
    pins, from_line = tested_pins(text)
    if from_line and pins != {current}:
        return [Finding(where, check, f"tested artifact names pin {', '.join(sorted(pins)) or 'none'}; the current pin is {current}")]
    if not from_line and current not in pins:
        return [Finding(where, check, f"the file names pin {', '.join(sorted(pins)) or 'none'}, not the current pin {current}")]
    return []


def check_probe_pins(code: str, root: Path = REPO_ROOT) -> Report:
    report = Report("probes")
    package_root = root / "packages" / code
    pins = {p.name for p in package_root.iterdir() if p.is_dir()} if package_root.is_dir() else set()
    resolved = resolve_pin(code, root)
    current = resolved[2] if resolved else None
    files = probe_result_files(code, root)
    if not files:
        report.notes.append("no saved probe-results files for this world")
    for path in files:
        where = rel(path, root)
        cited = set(PIN_RE.findall(read_text(path)))
        if not cited:
            report.findings.append(Finding(where, "l:pin-missing", "the probe-results file does not name the compiled prompt pin it tested"))
            continue
        unknown = sorted(cited - pins)
        if unknown and not (cited & pins):
            report.findings.append(Finding(where, "l:pin-unknown", f"names pin {unknown[0]}, which is not a package of {code}"))
        else:
            report.findings.extend(pin_not_current(read_text(path), where, current, "l:pin-not-current"))
    return report


def runner_dry_run(code: str, root: Path = REPO_ROOT) -> Report:
    """Exercise the guard without a model call: legacy files refused, the
    current compiled prompt accepted, and the loader every battery goes
    through refuses a non-package directory."""
    report = Report("probes runner")
    base = root / "Build" / "worlds" / code
    legacy = sorted(p for p in base.rglob("*") if p.is_file() and _LEGACY_NAME.search(p.name)) if base.is_dir() else []
    for path in legacy:
        try:
            assert_compiled_target(path)
        except ProbeTargetRefused:
            continue
        report.findings.append(Finding(rel(path, root), "l:guard-accepts-legacy", "the guard accepted a legacy prompt or capsule file"))
    report.notes.append(f"{len(legacy)} legacy file(s) offered to the guard")
    resolved = resolve_pin(code, root)
    if resolved:
        target = resolved[1] / "compiled" / "prompt.txt"
        try:
            assert_compiled_target(target)
        except ProbeTargetRefused as exc:
            report.findings.append(Finding(rel(target, root), "l:guard-refuses-compiled", str(exc)))
    from engine.m4.world_loader import LazyWorldLoader

    try:
        LazyWorldLoader().load(code, package_dir=REPO_ROOT / "Build" / "worlds" / code, expected_manifest_hash="sha256:0")
    except ProbeTargetRefused:
        pass
    except Exception as exc:
        report.findings.append(Finding("engine/m4/world_loader.py", "l:loader-unguarded", f"loading a non-package directory raised {type(exc).__name__}, not ProbeTargetRefused"))
    else:
        report.findings.append(Finding("engine/m4/world_loader.py", "l:loader-unguarded", "loading a non-package directory succeeded"))
    return report


# ---- command line --------------------------------------------------------------------------------


def _json_flag(parser) -> None:
    parser.add_argument("--json", action="store_true", help="print one JSON document instead of lines")


def add_parser(subparsers) -> None:
    p = subparsers.add_parser("deployed", help="the compiled prompt carries every confirmed item, rule counts match the records, the pin is not stale")
    p.add_argument("world_code")
    p.add_argument("--no-stale", action="store_true", help="skip the staleness recompile")
    _json_flag(p)

    p = subparsers.add_parser("citations", help="every record id and cic/texts path in the named files resolves and has the right type")
    p.add_argument("world_code")
    p.add_argument("files", nargs="*", help="files to check (default: the world's build documents and every probe-results file)")
    _json_flag(p)

    p = subparsers.add_parser("probes", help="the runner tests only compiled/prompt.txt; every saved probe-results file names its pin")
    p.add_argument("world_code")
    p.add_argument("--runner-dry-run", action="store_true", help="also exercise the guard and the loader against legacy paths")
    _json_flag(p)


def run(args) -> int:
    code = args.world_code
    if args.command == "deployed":
        reports = [check_deployed(code, check_stale=not args.no_stale)]
    elif args.command == "citations":
        files = [Path(f) if Path(f).is_absolute() else Path.cwd() / f for f in args.files] or citation_files(code)
        reports = [check_citations(code, files) if files else Report("citations", [Finding(f"Build/worlds/{code}", "d:no-documents", "no build documents or probe-results files to check")])]
    elif args.command == "probes":
        from .validation import check_result_labels

        reports = [check_probe_pins(code), check_result_labels(probe_result_files(code))]
        if args.runner_dry_run:
            reports.append(runner_dry_run(code))
    else:
        raise SystemExit(f"unknown subcommand {args.command!r}")
    return emit(reports, as_json=args.json)
