"""Phase 2 checkpoint plumbing: build a world's CANDIDATE tree, then
preflight it.

WHY THIS IS COMMITTED. The six per-world checkpoint harnesses written
during the 2026-08-08 Phase 2 pass (pahc_/ijc_/alx_/des_/syr_checkpoint1.py,
hal_checkpoint4.py) lived only in a session scratchpad, together with the
candidate trees and indices they had already built and preflighted. The
container was reclaimed and all six were lost - the checkpoints they were
blocking on had still not run. This module is the part of that work that
must not be re-lost: it reconstructs a candidate tree from committed
material alone, and asserts the same configuration facts each of those
harnesses asserted before its first API call.

WHAT A CANDIDATE TREE IS. backend/data/ is the DEPLOYED tree and is never
touched here - "data/ untouched, nothing swapped" is the standing rule
until a checkpoint is green and read. A candidate tree is a full copy of
data/ (so the five other worlds stay exactly as deployed) with ONE world's
rebuilt artifacts overlaid from wrs/views/staging/<world>/: the assembled
permanent prompt, the generated capsule, and the rewritten lexicon/story
chunks. The app is pointed at it via DATA_BASE_PATH / VECTOR_STORE_BASE_PATH,
which pydantic-settings reads straight into Settings.

Indices are rebuilt per candidate tree rather than reused, because
app/rag/retriever.py calls load_index() first and only falls back to
index_lexicon() on failure - a stale index survives a records change
silently, which is precisely the failure mode Marius's pass recorded.

Usage (from cic-poc/backend):
  python scripts/checkpoint_candidate.py --world pahc
  python scripts/checkpoint_candidate.py --world pahc --preflight-only
  python scripts/checkpoint_candidate.py --world pahc --build-indices

--build-indices requires huggingface.co egress for all-MiniLM-L6-v2
(app/rag/embeddings.py). Where the egress policy denies that host and no
model cache exists, the tree still builds and preflights; only the battery
is blocked. See the Chloe checkpoint record in
Ministry/Operations/Audits/CiC_VoiceRebuild_Blueprint_2026-08-08/.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

DEFAULT_ROOT = BACKEND / "candidates"

# world key -> world_id. Deliberately NOTHING else: the data dir name and
# the deployed prompt/capsule filenames come from app/world_manifest.py via
# Settings.get_world_config, which is the single source of truth the app
# itself reads.
#
# An earlier version of this file hardcoded those filenames in a table here
# and got Alexandria wrong - its deployed files are alex_*, not alx_*. The
# overlay wrote two stray alx_* files, left the real deployed prompt in
# place, and reported success. A checkpoint run on that tree would have
# graded the DEPLOYED voice while believing it was grading the candidate.
# That is the same silent-staleness failure the per-tree index rebuild
# exists to prevent, and the same hand-synced-list failure world_manifest.py
# was created to end. Hence: no filenames here.
WORLDS = {
    "pahc": "post-apostolic-house-church",
    "ijc": "imperial-juridical-christianity",
    "alx": "alexandria-catechetical",
    "des": "desert-monasticism",
    "syr": "syriac-edessa-nisibis",
    "hal": "hieronymian-ascetic-literary",
}


# The §5.1 permanent-prompt assembler per world. Desert's is the original
# (wrs/views/permanent_prompt.py); the other five are its per-world
# generalizations. Same modules assembly_identity.py drives.
ASSEMBLERS = {
    "des": "permanent_prompt",
    "pahc": "s62_pahc_permanent_prompt",
    "alx": "s62_alx_permanent_prompt",
    "syr": "s62_syr_permanent_prompt",
    "ijc": "s62_ijc_permanent_prompt",
    "hal": "s62_hal_permanent_prompt",
}


def assemble_prompt(key: str) -> str:
    """This world's permanent prompt as its assembler produces it NOW."""
    import importlib
    sys.path.insert(0, str(BACKEND / "wrs" / "views"))
    mod = importlib.import_module(ASSEMBLERS[key])
    importlib.reload(mod)
    prompt, _manifest = mod.assemble()
    return prompt


# ------------------------------------------------------------------ build

def build_tree(key: str, root: Path) -> Path:
    from app.world_manifest import WORLD_MANIFEST

    world_id = WORLDS[key]
    entry = next(e for e in WORLD_MANIFEST if e.world_id == world_id)
    data_dir = entry.data_dir_name
    prompt_name = entry.permanent_prompt_filename
    capsule_name = entry.world_capsule_filename

    staging = BACKEND / "wrs" / "views" / "staging" / data_dir
    if not staging.is_dir():
        raise SystemExit(f"[cand] no staging tree for {key}: {staging}")

    cand = root / key
    if cand.exists():
        shutil.rmtree(cand)
    cand.mkdir(parents=True)

    shutil.copytree(BACKEND / "data", cand / "data")
    world = cand / "data" / data_dir

    # The overlay target must already exist as a deployed file. If it does
    # not, the manifest and the tree disagree and the overlay would create a
    # file nothing reads while leaving the real one deployed - fail loudly
    # rather than reporting a success that grades the wrong voice.
    for name in (prompt_name, capsule_name):
        if not (world / name).is_file():
            raise SystemExit(
                f"[cand] FAIL - {key}: manifest names {name!r} but no such "
                f"deployed file in {world}. Refusing to write a candidate "
                f"the app would not read.")

    # THE PROMPT IS THE _S52 FILE, NOT THE _generated ONE. Every staging tree
    # carries both, and they are not two names for one thing:
    #   *_Permanent_Prompt_S52.txt        <- s62_<world>_permanent_prompt.py,
    #                                        the real SS5.1 assembly, and the
    #                                        module assembly_identity.py checks
    #   *_Permanent_Prompt_generated.txt  <- the prompt half of
    #                                        s62_<world>_capsule_prompt_views.py,
    #                                        which the SS5.1 assembler's own
    #                                        docstring records itself as having
    #                                        REPLACED ("deliberately temporary")
    # Only that script's CAPSULE half is still current, which is why the capsule
    # below is still read from *_generated.md.
    #
    # Getting this wrong is silent and expensive: an earlier version of this
    # file globbed *_Permanent_Prompt_generated.txt and ran a whole PAHC
    # checkpoint against a 1951-word superseded prompt instead of Chloe's real
    # 4106-word assembly. The cross-check that catches it is committed prose -
    # ijc's S52 is 3714 words and Marius's checkpoint record states "Assembled
    # prompt: 3,714 words".
    # ...and rather than copy that file, ASSEMBLE. The staged S52 is a
    # snapshot and can lag the records it was rendered from. (An earlier
    # version of this comment claimed PAHC's staged file was "23 words behind"
    # - that was a tokenizer artifact, wc -w vs python split disagreeing on
    # the same bytes; the 2026-08-09 audit found staging byte-identical to
    # the assembler on every world. The principle stands anyway: assembling
    # makes the candidate the records' current output BY CONSTRUCTION rather
    # than by trusting a snapshot, and reports drift loudly if it ever
    # appears.)
    prompt_text = assemble_prompt(key)
    gen_capsule = next(staging.glob("*_World_Capsule_Core_generated.md"))
    (world / prompt_name).write_text(prompt_text, encoding="utf-8")
    shutil.copyfile(gen_capsule, world / capsule_name)

    staged_s52 = next(staging.glob("*_Permanent_Prompt_S52.txt"), None)
    drift = ""
    if staged_s52 is not None:
        staged_words = len(staged_s52.read_text(encoding="utf-8").split())
        delta = len(prompt_text.split()) - staged_words
        if delta:
            drift = f"  [staged {staged_s52.name} is {-delta:+d} words - stale]"
    print(f"[cand] prompt  {prompt_name} <- {ASSEMBLERS[key]}.assemble() "
          f"({len(prompt_text.split())} words){drift}")
    print(f"[cand] capsule {capsule_name} <- {gen_capsule.name} "
          f"({len(gen_capsule.read_text(encoding='utf-8').split())} words)")

    for sub in ("lexicon_chunks", "story_chunks"):
        src = staging / sub
        if not src.is_dir():
            continue
        n = 0
        for f in sorted(src.glob("*.md")):
            shutil.copyfile(f, world / sub / f.name)
            n += 1
        print(f"[cand] {sub}: {n} rebuilt chunks overlaid")

    (cand / "vector_store").mkdir(exist_ok=True)
    print(f"[cand] tree at {cand}")
    print(f"[cand] run the battery with:\n"
          f"       DATA_BASE_PATH={cand}/data \\\n"
          f"       VECTOR_STORE_BASE_PATH={cand}/vector_store \\\n"
          f"       ANTHROPIC_API_KEY=... python scripts/<battery>.py")
    return cand


# --------------------------------------------------------------- preflight

def preflight(key: str) -> bool:
    """The configuration assertions every one of the six lost harnesses ran
    before its first API call. No network, no embeddings - this is readable
    even where the battery is blocked."""
    world_id = WORLDS[key]
    from app.config import settings

    ok = True
    wc = settings.get_world_config(world_id)
    prompt_words = len(wc.permanent_prompt_path.read_text(encoding="utf-8").split())
    capsule_words = len(wc.world_capsule_path.read_text(encoding="utf-8").split())
    print(f"[cfg] data_base_path = {settings.data_base_path}")
    print(f"[cfg] prompt words   = {prompt_words}")
    print(f"[cfg] capsule words  = {capsule_words}")
    if prompt_words == 0:
        print("[cfg] FAIL - assembled prompt is empty")
        ok = False

    from app.graph.repair_classifier import ceiling_words_map, _migrated_world_ids
    ceiling = ceiling_words_map().get(world_id)
    print(f"[cfg] ceiling        = {ceiling} (from voice_profile.native_measure)")
    if not isinstance(ceiling, int):
        print("[cfg] FAIL - no record-fed ceiling; nodes.py would use the fallback")
        ok = False
    if world_id not in _migrated_world_ids():
        print(f"[cfg] FAIL - {world_id} not migrated; no post-history guard")
        ok = False
    else:
        from wrs.views.segments.guards import POST_HISTORY_GUARDS
        own = world_id in POST_HISTORY_GUARDS
        print(f"[cfg] per-world guard export {'ACTIVE' if own else 'ABSENT (shared constant)'} "
              f"for {world_id}")
        if not own:
            ok = False

    # The retry trigger is a dict literal inside a function body in nodes.py,
    # so it is read from source rather than imported. A dead zone here is the
    # defect every world's Phase 2 pass was fixing: a ceiling that never fires.
    src = (BACKEND / "app" / "graph" / "nodes.py").read_text(encoding="utf-8")
    m = re.search(r"RETRY_TRIGGER_MULTIPLES = \{.*?\}", src, re.S)
    trigger = None
    if m:
        tm = re.search(rf'"{re.escape(world_id)}":\s*([0-9.]+)', m.group(0))
        if tm:
            trigger = float(tm.group(1))
    print(f"[cfg] retry trigger multiple = {trigger}")
    if trigger is None:
        print("[cfg] FAIL - world absent from RETRY_TRIGGER_MULTIPLES (defaults to 1.5)")
        ok = False
    elif isinstance(ceiling, int):
        dead_zone = int(ceiling * trigger) - ceiling
        print(f"[cfg] enforced threshold = {int(ceiling * trigger)}w "
              f"(dead zone {dead_zone}w wide)")
        if dead_zone:
            print("[cfg] WARN - a nonzero dead zone means over-ceiling drafts in "
                  "that band are emitted uncorrected")

    print(f"[cfg] {'PREFLIGHT GREEN' if ok else 'PREFLIGHT FAILED'}")
    return ok


def build_indices(world_id: str) -> None:
    from app.graph.nodes import get_retriever, get_story_retriever
    get_retriever(world_id)
    get_story_retriever(world_id)
    print(f"[idx] lexicon + story indices built for {world_id}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", required=True, choices=sorted(WORLDS))
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                    help="where candidate trees are written (default ./candidates)")
    ap.add_argument("--preflight-only", action="store_true",
                    help="skip the copy; assert against whatever DATA_BASE_PATH points at")
    ap.add_argument("--build-indices", action="store_true",
                    help="also build FAISS indices (needs huggingface.co egress)")
    args = ap.parse_args()

    if not args.preflight_only:
        build_tree(args.world, args.root)
        print("\n[cand] NOTE: preflight below reads DATA_BASE_PATH, which this "
              "process did not set - re-run with --preflight-only and the two "
              "env vars printed above to assert against the candidate tree.\n")

    ok = preflight(args.world)
    if args.build_indices:
        build_indices(WORLDS[args.world])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
