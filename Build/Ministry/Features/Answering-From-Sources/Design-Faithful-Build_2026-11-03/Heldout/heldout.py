"""Held-out question set (Spec 5): request files, overlap check, freeze.

  python3 heldout.py requests      write requests/<world>_request.md
  python3 heldout.py overlap       check drafts/<world>_draft.yaml against the exclusion sources
  python3 heldout.py freeze        write <world>_questions.yaml and SHA256SUMS from clean drafts
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO))

from engine.m1.registry import load_registry  # noqa: E402
from engine.m3.sealed_probes import read_probe  # noqa: E402
from engine.m9.loader import read_bucket_rows  # noqa: E402

WORLDS = ["lpc", "ijc", "cappadocian", "alx", "pahc", "don", "rzg", "syr", "desert", "hal", "witt", "gallic"]
EXPECTED = {"lpc": 44, "ijc": 39, "cappadocian": 35, "alx": 34, "pahc": 30, "don": 29, "rzg": 28, "syr": 27, "desert": 25, "hal": 24, "witt": 23, "gallic": 22}
THEMES = ["belief", "practice", "people", "events", "conflicts", "daily_life", "modern_concern", "unanswerable"]
THEME_CAP = 0.25
JACCARD_LIMIT = 0.5
COVER_LIMIT = 0.75
INTRA_LIMIT = 0.6
STOP = set("a an the of to in on at for and or but is are was were be been being do does did what why how who whom which when where would could should can will you your they their them this that these those it its as by with from about i me my we our us if than then so not no any there here have has had".split())

SB = REPO / "Build/Ministry/Features/Question-Coverage/Repository"
BENCH = REPO / "engine/m4/reports/bench"
T100 = REPO / "Build/Ministry/Features/Answering-From-Sources/S3-Test100"
CANON_PROBES = REPO / "canon/sealed_probes/plaintext"


def norm(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9']+", text.lower()))


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP}


def digest(text: str) -> str:
    return hashlib.sha256(norm(text).encode()).hexdigest()


def inputs() -> dict:
    return yaml.safe_load((HERE / "tradition_inputs.yaml").read_text(encoding="utf-8"))


def short_title(work: str) -> str:
    """The title alone: no edition, scan, line, chapter or topic notes."""
    t = re.sub(r"\([^)]*\)?", " ", work)
    t = re.split(r",|;|:| — | – | - |\bCSEL\b|\bTEI\b|\bOCR\b", t)[0]
    t = re.split(r"\s+(?:from codex|in the Swedish|of \d{3,4}\b|\d+\.\d+)|\s+and the (?:Maurist|Geneva trial|council dossier|\d{3}-\d{3})|\s+and Life\b", t)[0]
    return " ".join(t.split()).strip(" .")


def shelf_works(world: str) -> list[tuple[str, str]]:
    census = load_registry()[world].get("census_id")
    seen, out = set(), []
    for row in read_bucket_rows(census):
        key = (str(row.get("author") or "").strip(), short_title(str(row.get("work") or "")))
        if key[1] and key not in seen:
            seen.add(key)
            out.append(key)
    return sorted(out)


def request_text(world: str) -> str:
    t = inputs()[world]
    n = EXPECTED[world]
    cap = int(n * THEME_CAP)
    shelf = "\n".join(f"- {a}: {w}" if a else f"- {w}" for a, w in shelf_works(world))
    return f"""# Request: {n} visitor questions for {t['name']}

You are writing questions a curious adult visitor would ask a voice from this tradition. You know only what is below. Do not look at any other file in the repository.

## The tradition
- Name: {t['name']}
- Era: {t['era']}
- Region: {t['region']}

{t['paragraph']}

## The library behind the voice (titles and authors only)
The voice answers from these works. The visitor does not know this list. Do not copy titles into questions, and do not ask about a work by name.
{shelf}

## What to write
Exactly {n} questions, in the visitor's own plain words.
- Cover the whole range: belief, practice, people, events, conflicts, daily life, what the tradition would say about a modern concern, and a few questions the tradition may not be able to answer (the visitor does not know what the library holds).
- Give each question one theme tag from: {', '.join(THEMES)}.
- No more than {cap} questions on any one theme. At least 2 modern_concern and at least 2 unanswerable.
- Vary the length: at least a fifth short (6 to 10 words) and at least a fifth long (20 to 35 words).
- Plain wording a non-native reader can follow. No leading questions: do not build the answer, a judgment or a disputed claim into the question. No quoting or paraphrasing a line from any text. No question that names a specific document, letter, sermon or passage, or hints at one.
- Ask the tradition as a whole ("your church", "your people"). Never address the voice as one named person, and never ask what "you" did on a certain date.
- Use a name, date or place only if the tradition paragraph above gives it, and only when you are sure it applies to the whole tradition.
- Modern-concern and unanswerable questions must grow out of this tradition's own subject. Avoid the stock ones: faith and science, far-off countries, rich and poor in general, predictions of the future, how many members there were.
- No questions about personal crisis, self-harm, abuse or distress.
- No two questions about the same subject, even in different words.

## Output
Write one YAML file to {HERE / 'drafts' / (world + '_draft.yaml')} as a list:
- theme: <tag>
  text: <the question>

Write only that file.
"""


def cmd_requests() -> None:
    (HERE / "requests").mkdir(exist_ok=True)
    for w in WORLDS:
        (HERE / "requests" / f"{w}_request.md").write_text(request_text(w), encoding="utf-8")
        print(w, EXPECTED[w])


def exclusion_sources() -> tuple[dict[str, list[str]], set[str]]:
    """Wordings by category (compared by word overlap) and hashes of sealed text (hash only)."""
    cats: dict[str, list[str]] = {"subquestion": [], "bench": [], "lpc106": []}
    for f, key in (("07-subquestions.yaml", "subquestions"), ("08-subquestion-splits.yaml", "splits")):
        for e in yaml.safe_load((SB / f).read_text(encoding="utf-8"))[key]:
            cats["subquestion"].append(str(e.get("canonical") or ""))
    for f in sorted(BENCH.glob("*.json")):
        for q in json.loads(f.read_text(encoding="utf-8")):
            cats["bench"].append(q if isinstance(q, str) else str(q.get("question") or q.get("text") or ""))
    sealed: set[str] = set()
    for f in sorted(CANON_PROBES.glob("*.md")):
        sealed.add(digest(read_probe(f.stem)["text"]))
    for name in ("lpc_100_questions.yaml", "lpc_106_questions.yaml"):
        for q in yaml.safe_load((T100 / name).read_text(encoding="utf-8"))["questions"]:
            if q.get("probe_id"):
                sealed.add(digest(read_probe(q["probe_id"])["text"]))
            elif q.get("text"):
                cats["lpc106"].append(q["text"])
    return cats, sealed


def overlap_score(a: set[str], b: set[str]) -> bool:
    """True when two content-word sets are near-duplicates."""
    if not a or not b:
        return False
    inter = len(a & b)
    if inter / len(a | b) >= JACCARD_LIMIT:
        return True
    return min(len(a), len(b)) >= 4 and inter / min(len(a), len(b)) >= COVER_LIMIT


def flags(questions: dict[str, list[dict]]) -> list[tuple[str, str, str]]:
    """(world, question id, reason) for each near-duplicate. Source wordings are never returned."""
    cats, sealed = exclusion_sources()
    prepared = {c: [words(t) for t in ts if t.strip()] for c, ts in cats.items()}
    out = []
    for w, qs in questions.items():
        ws = [words(q["text"]) for q in qs]
        for i, q in enumerate(qs):
            qid = q["id"]
            if digest(q["text"]) in sealed:
                out.append((w, qid, "sealed"))
            for c, sets in prepared.items():
                if any(overlap_score(ws[i], s) for s in sets):
                    out.append((w, qid, c))
            for j in range(i):
                inter = len(ws[i] & ws[j])
                if ws[i] and ws[j] and inter / len(ws[i] | ws[j]) >= INTRA_LIMIT:
                    out.append((w, qid, f"intra:{qs[j]['id']}"))
    return out


def load_drafts() -> dict[str, list[dict]]:
    out = {}
    for w in WORLDS:
        p = HERE / "drafts" / f"{w}_draft.yaml"
        if p.exists():
            rows = yaml.safe_load(p.read_text(encoding="utf-8")) or []
            out[w] = [{"id": f"{w}-h{i + 1:02d}", "theme": r["theme"], "text": " ".join(str(r["text"]).split())} for i, r in enumerate(rows)]
    return out


def cmd_rewrite_requests() -> None:
    """For each flagged question, write a request to a fresh helper to replace it on a different angle of the same theme."""
    drafts = load_drafts()
    by_world: dict[str, list[str]] = {}
    for w, qid, _ in flags(drafts):
        if qid not in by_world.setdefault(w, []):
            by_world[w].append(qid)
    for w, qs in drafts.items():
        for q in qs:
            if not q["text"] and q["id"] not in by_world.setdefault(w, []):
                by_world[w].append(q["id"])
    by_world = {w: ids for w, ids in by_world.items() if ids}
    for w, ids in by_world.items():
        qs = drafts[w]
        slots = [q for q in qs if q["id"] in ids]
        keep = "\n".join(f"- {q['text']}" for q in qs if q["id"] not in ids)
        need = "\n".join(f"- slot {q['id']}, theme {q['theme']}" for q in slots)
        body = request_text(w).split("## What to write")[0]
        text = body + f"""## What to write
These questions are already settled for this tradition:
{keep}

Write {len(slots)} NEW questions for these slots, each on a different subject from every settled question and from each other, in the visitor's plain words, one theme tag each:
{need}

Same rules as before. Do not ask about numbers of people, about faith and science, or about what happened after the tradition's end date. For an unanswerable slot, ask about something specific to this tradition that its writers would not have recorded, such as what one ordinary member felt or said in private, or a detail of daily life nobody wrote down. Plain wording, varied length, no leading question, no named work or passage, nothing about personal crisis or distress.

## Output
Write one YAML file to {HERE / 'drafts' / (w + '_rewrite.yaml')} as a list, in the slot order above:
- slot: <slot id>
  theme: <tag>
  text: <the question>

Write only that file.
"""
        (HERE / "requests" / f"{w}_rewrite_request.md").write_text(text, encoding="utf-8")
        print(w, ids)


def cmd_apply_rewrites() -> None:
    for p in sorted((HERE / "drafts").glob("*_rewrite.yaml")):
        w = p.name.split("_")[0]
        d = HERE / "drafts" / f"{w}_draft.yaml"
        rows = yaml.safe_load(d.read_text(encoding="utf-8"))
        for r in yaml.safe_load(p.read_text(encoding="utf-8")):
            i = int(r["slot"].rsplit("h", 1)[1]) - 1
            rows[i] = {"theme": r["theme"], "text": r["text"]}
        d.write_text(yaml.safe_dump(rows, allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
        p.unlink()
        print("applied", w)


def cmd_overlap() -> int:
    drafts = load_drafts()
    found = flags(drafts)
    for w in WORLDS:
        n = len(drafts.get(w, []))
        mine = [f for f in found if f[0] == w]
        print(f"{w}: drafted {n} of {EXPECTED[w]}; near-duplicates {len(mine)}")
        for _, qid, why in mine:
            print(f"  {qid}  {why}")
    return 1 if found else 0


def cmd_freeze() -> int:
    drafts = load_drafts()
    if set(drafts) != set(WORLDS):
        print("drafts missing")
        return 1
    if flags(drafts):
        print("overlap flags remain")
        return 1
    for w, qs in drafts.items():
        if len(qs) != EXPECTED[w]:
            print(w, "count", len(qs))
            return 1
        (HERE / f"{w}_questions.yaml").write_text(yaml.safe_dump([{"id": q["id"], "text": q["text"]} for q in qs], allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
    lines = [f"{hashlib.sha256((HERE / f'{w}_questions.yaml').read_bytes()).hexdigest()}  {w}_questions.yaml" for w in WORLDS]
    (HERE / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("frozen", sum(len(q) for q in drafts.values()))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "requests":
        cmd_requests()
    elif cmd == "rewrite-requests":
        cmd_rewrite_requests()
    elif cmd == "apply-rewrites":
        cmd_apply_rewrites()
    elif cmd == "overlap":
        sys.exit(cmd_overlap())
    elif cmd == "freeze":
        sys.exit(cmd_freeze())
    else:
        print(__doc__)
