"""Byte-exact access to a source file: decoding that round-trips, and a
character-index to byte-offset map that is cheap on multi-megabyte files."""
from __future__ import annotations

import hashlib
from pathlib import Path

_BLOCK = 4096


class Source:
    def __init__(self, data: bytes):
        self.data = data
        self.text = data.decode("utf-8", errors="surrogateescape")
        self._ascii = len(self.text) == len(data)
        self._cum: list[int] | None = None

    @classmethod
    def read(cls, path: Path) -> "Source":
        return cls(Path(path).read_bytes())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest()

    def byte_of(self, char_index: int) -> int:
        if self._ascii:
            return char_index
        if self._cum is None:
            t = self.text
            cum = [0]
            total = 0
            for i in range(0, len(t), _BLOCK):
                total += len(t[i:i + _BLOCK].encode("utf-8", errors="surrogateescape"))
                cum.append(total)
            self._cum = cum
        block = char_index // _BLOCK
        base = block * _BLOCK
        return self._cum[block] + len(self.text[base:char_index].encode("utf-8", errors="surrogateescape"))
