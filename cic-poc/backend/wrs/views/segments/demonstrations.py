"""§5.1 segment 5 - demonstrations (demonstration records selected
against the rubric). Pruned FIRST under token pressure (lowest eviction
rank), per the universal permanent-vs-evicted split.

Voice Rebuild Phase 0.1 (2026-08-08): the selector now speaks a single
canonical score vocabulary (strong/partial/weak) and a `required` flag,
per Design §2 Layer 2 / Blueprint 0.1. Two of six worlds (Desert,
Alexandria) already score in this vocabulary; four (PAHC, Syriac, and
Hieronymian scoring in a PASS/PARTIAL verification-grade vocabulary
left over from an earlier freeze process; IJC scoring not at all) do
not - those records are Phase 2 authoring work, not a Phase 0
vocabulary translation, so this selector does not attempt to
reinterpret non-canonical scores as strong/partial/weak. Until each
world's Phase 2 pass writes fresh, canonically-scored demonstrations,
this segment selects nothing for that world - the emptiness is real
information, not a bug: assert_ready() below is what a Phase 2 build
gate calls to turn that emptiness into a hard failure at the right
moment (a world's go-live), not at every Phase 0 assembler run, which
must keep succeeding on worlds not yet rebuilt (Blueprint Checkpoint
0's "produces stable output for the other five").

One correctness note this rewrite fixes, not just reorganizes: the
prior selector's `"weak" not in scores` check treated any non-"weak"
string as passing, so PAHC/Syriac/Hieronymian's PASS-vocabulary demos
were being silently selected as if canonically strong - the review
finding that "the rubric filter is currently a no-op." Requiring
canonical vocabulary closes that gap.

Selection: canonical-vocabulary records with no 'weak' trait score, OR
any record explicitly flagged `required: true` (each world's Phase 2
build authors exactly one - its targeted demonstration, aimed at that
world's own measured failure - always included). Rank key: strong-score
count descending, then record id (deterministic; no dependency on
dict/glob ordering). Capped (default 3; a world's own assembler may
raise this to 5 once it has that many qualifying records, per Design's
3-5 range)."""
from ._common import voice

_CANONICAL_SCORES = {"strong", "partial", "weak"}


def _scores(demo: dict) -> list:
    return [t.get("score") for t in demo.get("trait_scores", [])]


def _is_canonical(demo: dict) -> bool:
    scores = _scores(demo)
    return bool(scores) and all(s in _CANONICAL_SCORES for s in scores)


def _strong_count(demo: dict) -> int:
    return sum(1 for s in _scores(demo) if s == "strong")


def _eligible(demo: dict) -> bool:
    return _is_canonical(demo) and "weak" not in _scores(demo)


def _selected(demos: dict, cap: int = 3) -> list:
    items = [demos[did] for did in sorted(demos)]
    required = [d for d in items if d.get("required") and _eligible(d)]
    ranked = sorted(
        (d for d in items if _eligible(d) and not d.get("required")),
        key=lambda d: (-_strong_count(d), d.get("id", "")))
    keep = required + ranked
    return keep[:cap]


def assert_ready(demos: dict, world_id: str = "") -> None:
    """Phase 2 build-gate call - NOT invoked during ordinary Phase 0
    assembly. Raises if a world about to ship selects zero
    demonstrations: the "hardened selector: a world selecting zero
    demonstrations fails the build" requirement (Blueprint 0.1),
    applied at go-live rather than at every assembler run."""
    if not _selected(demos):
        raise ValueError(
            f"{world_id or '(unnamed world)'}: zero demonstrations "
            "selected - no canonically-scored (strong/partial/weak, no "
            "'weak') record and no required=true record exists. This "
            "world is not ready to ship; write fresh demonstrations "
            "first (brief §7 Part A).")


def render(ctx) -> str:
    chosen = _selected(ctx.get("demonstrations", {}))
    if not chosen:
        return ""
    parts = ["How this voice actually moves, shown not described:"]
    for d in chosen:
        dialogue = voice(d.get("dialogue", ""))
        if dialogue:
            parts.append(dialogue)
    return "\n\n".join(parts) if len(parts) > 1 else ""


SEGMENT = {"name": "demonstrations", "cache_stability": "static",
           "eviction_priority": 5, "render": render,
           "sources": "demonstration records (rubric-selected: canonical "
                      "strong/partial/weak vocabulary, no weak trait "
                      "score, or required=true; cap 3, deterministic "
                      "rank by strong-count desc then record id)"}
