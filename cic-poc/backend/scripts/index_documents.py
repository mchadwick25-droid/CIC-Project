#!/usr/bin/env python3
"""One-time script to index lexicon documents into FAISS vector store."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import settings
from app.rag.indexer import LexiconIndexer


def index_world(world_id: str, indexer: LexiconIndexer) -> bool:
    """Index a single world's lexicon documents."""
    try:
        world_config = settings.get_world_config(world_id)
    except ValueError as e:
        print(f"Error: {e}")
        return False

    lexicon_path = world_config.lexicon_chunks_path
    vector_store_path = settings.get_vector_store_path(world_id)

    print(f"\n--- {world_config.name} ({world_id}) ---")

    if not lexicon_path.exists():
        print(f"  Skipping: Lexicon path does not exist: {lexicon_path}")
        return False

    # Count files
    files = list(lexicon_path.glob("*.md"))
    print(f"  Found {len(files)} lexicon files in {lexicon_path}")

    if len(files) == 0:
        print("  Skipping: No lexicon files found")
        return False

    # Index documents
    print("  Indexing documents...")
    vector_store = indexer.index_lexicon(lexicon_path)

    # Save index
    print("  Saving vector store...")
    indexer.save_index(vector_store, vector_store_path)
    print(f"  Index saved to: {vector_store_path}")

    return True


def main():
    """Index all lexicon documents for all worlds."""
    print("=" * 60)
    print("CiC POC - Lexicon Indexer (Multi-World)")
    print("=" * 60)

    # Create indexer
    indexer = LexiconIndexer()

    # Index all configured worlds
    worlds = settings.worlds
    success_count = 0
    skip_count = 0

    for world_id in worlds:
        if index_world(world_id, indexer):
            success_count += 1
        else:
            skip_count += 1

    print()
    print("=" * 60)
    print("Indexing complete!")
    print(f"  Worlds indexed: {success_count}")
    if skip_count > 0:
        print(f"  Worlds skipped: {skip_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
