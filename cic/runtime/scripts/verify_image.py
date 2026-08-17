#!/usr/bin/env python3
"""Assert that a built image actually keeps the promises the build makes.

Run at the end of the Docker build, with the network refused
(HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1). Every check here corresponds
to something that would otherwise fail on a live instance, during a real
participant's turn, rather than here.

  1. Both transformer models resolve from the local cache. Without this
     the first turn downloads ~180MB from huggingface.co mid-request -
     and requirements.txt's own comment says the alternative is that
     "every turn fails in retrieval".

  2. Every world retrieves from the BAKED index, with rebuilding made
     impossible. This is the sharp one. LexiconRetriever.__init__
     (app/rag/retriever.py:71-77) wraps its index load in a bare
     try/except that falls through to index-and-save, so a missing or
     truncated index does not raise - it silently rebuilds, and the
     image looks healthy right up to the moment a 512MB box embeds a
     world's corpus inside a request. Removing that escape hatch for the
     length of this check is what turns "the indices are probably wired
     up correctly" into something a build can fail on.

  3. app.main imports, and candidate_search runs. requirements.txt was
     recovered empirically and records the failure this catches:
     rank-bm25 is imported lazily inside candidate_search(), so a
     missing copy survived app boot, /health and /api/session/start, and
     only died on the first real turn's retrieval. candidate_search is
     the call below.

Deliberately does NOT touch the Anthropic API: no key exists at build
time, and none of the above needs one.

Usage:
    python scripts/verify_image.py
"""
from __future__ import annotations

import sys
from pathlib import Path

_RUNTIME = Path(__file__).resolve().parents[1]
if str(_RUNTIME) not in sys.path:
    sys.path.insert(0, str(_RUNTIME))

_QUERY = "What was worship like?"


def _forbid_rebuilds() -> None:
    """Replace both indexers' build methods with a loud failure.

    Must run BEFORE the retrievers are imported and constructed.
    """
    from app.rag import indexer, story_indexer

    def boom(*_args, **_kwargs):
        raise AssertionError(
            "REBUILD ATTEMPTED - the baked index was not used. This is the "
            "exact failure this image exists to prevent; on a live instance "
            "it would have happened inside a participant's turn.")

    indexer.LexiconIndexer.index_lexicon = boom
    story_indexer.StoryIndexer.index_stories = boom


def main() -> int:
    _forbid_rebuilds()

    from app.rag.cross_encoder import _get_model
    from app.rag.embeddings import get_shared_embeddings

    get_shared_embeddings()
    _get_model()
    print("models: embedding + cross-encoder resolved from cache, "
          "network refused")

    import app.main  # noqa: F401  - import graph smoke test
    from app.rag.retriever import LexiconRetriever
    from app.rag.story_retriever import StoryRetriever
    from app.world_manifest import WORLD_MANIFEST

    failures = []
    for entry in WORLD_MANIFEST:
        try:
            lexicon = LexiconRetriever(
                world_id=entry.world_id).candidate_search(_QUERY, k=3)
            story = StoryRetriever(
                world_id=entry.world_id).candidate_search(_QUERY, k=2)
        except Exception as exc:                      # noqa: BLE001
            failures.append(f"{entry.world_id}: {type(exc).__name__}: {exc}")
            continue
        if not lexicon or not story:
            failures.append(
                f"{entry.world_id}: index loaded but returned nothing "
                f"({len(lexicon)} lexicon, {len(story)} story)")
            continue
        print(f"{entry.world_id}: {len(lexicon)} lexicon + {len(story)} "
              f"story from the baked index")

    if failures:
        print("\nIMAGE VERIFICATION FAILED:", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
        return 1

    print(f"\nOK - {len(WORLD_MANIFEST)} worlds serve retrieval offline "
          f"with rebuilding disabled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
