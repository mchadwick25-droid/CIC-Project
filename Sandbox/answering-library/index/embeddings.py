from typing import Protocol, Sequence


class Embedder(Protocol):
    model_id: str

    def embed_passages(self, texts: Sequence[str]) -> list[list[float]]: ...

    def embed_query(self, text: str) -> list[float]: ...
