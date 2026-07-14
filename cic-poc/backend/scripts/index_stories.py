#!/usr/bin/env python3
"""One-time script to index story chunks into FAISS vector store."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import settings
from app.rag.story_indexer import StoryIndexer


def index_world(world_id: str, indexer: StoryIndexer) -> bool:
    """Index a single world's story chunks."""
    try:
        world_config = settings.get_world_config(world_id)
    except ValueError as e:
        print(f"Error: {e}")
        return False

    story_path = world_config.story_chunks_path
    vector_store_path = settings.get_story_vector_store_path(world_id)

    print(f"\n--- {world_config.name} ({world_id}) ---")

    if not story_path.exists():
        print(f"  Skipping: Story chunks path does not exist: {story_path}")
        return False

    files = list(story_path.glob("*.md"))
    print(f"  Found {len(files)} story files in {story_path}")

    if len(files) == 0:
        print("  Skipping: No story files found")
        return False

    print("  Indexing stories...")
    vector_store = indexer.index_stories(story_path)

    print("  Saving vector store...")
    indexer.save_index(vector_store, vector_store_path)
    print(f"  Index saved to: {vector_store_path}")

    return True


def main():
    """Index all story chunks for all worlds."""
    print("=" * 60)
    print("CiC POC - Story Indexer (Multi-World)")
    print("=" * 60)

    indexer = StoryIndexer()

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
