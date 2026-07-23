"""Build-time step: pre-compute every world's FAISS indices and save them
to disk, so a freshly-built container loads pre-built indices at startup
(cheap) instead of re-embedding every lexicon/story chunk from scratch on
every single boot (the actual cause of the OOM kill on Render - loading
sentence-transformers plus embedding the full corpus for all 6 worlds
simultaneously, in the runtime instance's own limited memory, for no
reason - a fresh container throws the ephemeral vector_store/ away on
every restart anyway, so that work was always wasted).

Run once, during `docker build` (see Dockerfile), on Render's build
machine - which has much more headroom than the runtime instance does.
Uses the exact same retriever classes app/main.py's own startup lifespan
calls, so "already built" vs. "still needs building" behaves identically
here and at real startup.
"""

from app.graph.nodes import get_retriever, get_story_retriever
from app.world_manifest import WORLD_MANIFEST

if __name__ == "__main__":
    for entry in WORLD_MANIFEST:
        print(f"Building indices for {entry.world_name} ({entry.world_id})...")
        get_retriever(entry.world_id)
        get_story_retriever(entry.world_id)
    print("All world indices built.")
