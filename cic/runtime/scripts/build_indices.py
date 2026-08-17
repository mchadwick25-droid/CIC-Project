#!/usr/bin/env python3
"""Build every world's FAISS indices ahead of time, so no live instance ever does.

Why this exists
---------------
`LexiconRetriever.__init__` (app/rag/retriever.py:71-77) tries to load a
saved index and, on any failure, falls through to building one from the
world's chunk files and saving it. That fallback is correct behaviour for
local development and catastrophic behaviour in production: the first
participant to open a world pays for downloading two transformer models
and embedding that world's whole corpus on a 512MB CPU box, inside the
request. That is the sequence with a recorded OOM history (render.yaml
carries the account), and app/rag/embeddings.py's own docstring names this
script as the fix that was supposed to prevent it - "build_indices.py
builds every world in a single script run". It was never carried into the
clean tree. This is it.

What it produces
----------------
Two FAISS stores per world under `settings.vector_store_base_path`
(cic/runtime/vector_store/):

    <vector_store_name>/            lexicon chunks + ambient chunks
    <vector_store_name>_stories/    story chunks

Names come from app/world_manifest.py, resolved through
settings.get_vector_store_path / get_story_vector_store_path - the same
two functions the retrievers call at load time, so the writer and the
reader cannot disagree about where a world's index lives.

Memory
------
ONE shared embedding model for the whole run (app/rag/embeddings.py).
Six worlds x two indexer types constructing their own copy is twelve
loads of the same weights, none released - the documented cause of the
build OOM that killed the fifth world. Worlds are built sequentially for
the same reason: peak memory here is one model plus one world's
documents, not six.

Exit status
-----------
Non-zero if ANY world fails. A partial index set is worse than none,
because the missing worlds silently fall back to the runtime rebuild this
script exists to prevent - the failure would not surface until a
participant hit that particular world. Fail the build instead.

Usage
-----
    python scripts/build_indices.py            build all worlds
    python scripts/build_indices.py --check    verify only, build nothing
    python scripts/build_indices.py --world desert-monasticism
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

_RUNTIME = Path(__file__).resolve().parents[1]
if str(_RUNTIME) not in sys.path:
    sys.path.insert(0, str(_RUNTIME))

from app.config import settings                          # noqa: E402
from app.world_manifest import WORLD_MANIFEST            # noqa: E402


def _warm_models() -> None:
    """Pull both transformer models into the local HF cache.

    The embedding model is loaded anyway by the indexers below. The
    cross-encoder (app/rag/cross_encoder.py) is NOT - it is only touched
    on a real retrieval - so without this it stays absent from the image
    and the first participant turn downloads ~90MB mid-request. Warming
    it here is the whole reason its download stops being a runtime event.
    """
    from app.rag.cross_encoder import _get_model
    from app.rag.embeddings import get_shared_embeddings

    get_shared_embeddings()
    _get_model()


def _build_world(entry, lexicon_indexer, story_indexer) -> tuple[int, int]:
    """Build and save one world's two indices. Returns (lexicon, story) doc counts."""
    world = settings.get_world_config(entry.world_id)

    lexicon_store = lexicon_indexer.index_lexicon(world.lexicon_chunks_path)
    lexicon_indexer.save_index(
        lexicon_store, settings.get_vector_store_path(entry.world_id))

    story_store = story_indexer.index_stories(world.story_chunks_path)
    story_indexer.save_index(
        story_store, settings.get_story_vector_store_path(entry.world_id))

    return (lexicon_store.index.ntotal, story_store.index.ntotal)


def _check_world(entry, lexicon_indexer, story_indexer) -> tuple[int, int]:
    """Load one world's two indices. Raises if either is missing or unreadable.

    Loading, not stat-ing the directory: a truncated or half-written
    index passes an existence check and fails on the first query.
    """
    lexicon_store = lexicon_indexer.load_index(
        settings.get_vector_store_path(entry.world_id))
    story_store = story_indexer.load_index(
        settings.get_story_vector_store_path(entry.world_id))
    return (lexicon_store.index.ntotal, story_store.index.ntotal)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="verify existing indices load; build nothing")
    parser.add_argument("--world", action="append", default=None,
                        metavar="WORLD_ID",
                        help="build only this world (repeatable)")
    args = parser.parse_args(argv)

    entries = list(WORLD_MANIFEST)
    if args.world:
        wanted = set(args.world)
        unknown = wanted - {e.world_id for e in entries}
        if unknown:
            print(f"unknown world id(s): {', '.join(sorted(unknown))}",
                  file=sys.stderr)
            return 2
        entries = [e for e in entries if e.world_id in wanted]

    verb = "checking" if args.check else "building"
    print(f"{verb} indices for {len(entries)} world(s) -> "
          f"{settings.vector_store_base_path}")

    if not args.check:
        print("warming transformer models (embedding + cross-encoder)...")
        _warm_models()

    from app.rag.indexer import LexiconIndexer
    from app.rag.story_indexer import StoryIndexer

    # Constructed ONCE, outside the loop, and reused for every world -
    # both of these hold the shared embedding model.
    lexicon_indexer = LexiconIndexer()
    story_indexer = StoryIndexer()

    failures: list[tuple[str, str]] = []
    results: list[tuple[str, int, int, float]] = []

    for entry in entries:
        started = time.monotonic()
        print(f"\n=== {entry.world_id} ({entry.vector_store_name}) ===",
              flush=True)
        try:
            if args.check:
                lexicon_n, story_n = _check_world(
                    entry, lexicon_indexer, story_indexer)
            else:
                lexicon_n, story_n = _build_world(
                    entry, lexicon_indexer, story_indexer)
        except Exception as exc:                      # noqa: BLE001
            failures.append((entry.world_id, f"{type(exc).__name__}: {exc}"))
            print(f"FAILED {entry.world_id}: {type(exc).__name__}: {exc}",
                  file=sys.stderr, flush=True)
            continue
        results.append((entry.world_id, lexicon_n, story_n,
                        time.monotonic() - started))

    print(f"\n{'world':34}{'lexicon':>9}{'stories':>9}{'secs':>8}")
    print("-" * 60)
    for world_id, lexicon_n, story_n, secs in results:
        print(f"{world_id:34}{lexicon_n:>9}{story_n:>9}{secs:>8.1f}")

    if failures:
        print(f"\n{len(failures)} world(s) FAILED - a partial index set means "
              f"those worlds rebuild on a live instance, which is the thing "
              f"this script exists to prevent:", file=sys.stderr)
        for world_id, reason in failures:
            print(f"  {world_id}: {reason}", file=sys.stderr)
        return 1

    total_lexicon = sum(r[1] for r in results)
    total_story = sum(r[2] for r in results)
    print(f"\nOK - {len(results)} worlds, {total_lexicon} lexicon vectors, "
          f"{total_story} story vectors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
