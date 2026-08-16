"""Shared embedding model - loaded once, reused by every world's indexer.

LexiconIndexer and StoryIndexer each used to construct their own
HuggingFaceEmbeddings("all-MiniLM-L6-v2") instance. With 6 worlds x 2
indexer types built in one process (build_indices.py builds every world
in a single script run), that's the identical model loaded into memory 12
separate times, never released - the actual cause of the Render build
OOM-killing partway through the 5th world. One shared instance fixes it.
"""

from langchain_huggingface import HuggingFaceEmbeddings

_embeddings: HuggingFaceEmbeddings | None = None


def get_shared_embeddings() -> HuggingFaceEmbeddings:
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
    return _embeddings
