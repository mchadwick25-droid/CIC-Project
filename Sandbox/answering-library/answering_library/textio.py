"""Byte-exact access to a source file: decoding that round-trips, and a
character-index to byte-offset map that is cheap on multi-megabyte files."""
from __future__ import annotations

import hashlib
from bisect import bisect_right
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

    def char_of(self, byte_index: int) -> int:
        """Character index of a byte offset; the offset must fall on a character boundary."""
        if self._ascii:
            return byte_index
        self.byte_of(0)
        cum = self._cum
        block = max(0, bisect_right(cum, byte_index) - 1)
        block = min(block, len(cum) - 2)
        base = block * _BLOCK
        remaining = byte_index - cum[block]
        index = base
        while remaining > 0 and index < len(self.text):
            remaining -= len(self.text[index].encode("utf-8", errors="surrogateescape"))
            index += 1
        if remaining != 0:
            raise ValueError(f"byte offset {byte_index} is not on a character boundary")
        return index
