"""SS5.1 segment 1 - Identity & register: the deployed prompt's proven
voice prose (craft blocks; paras 1,2,7-12,17 per prompt_coverage.py's
map - speaking model, register rules, native measure, witness stance)."""
from .craft import DESERT_CRAFT

_PARAS = (1, 2, 7, 8, 9, 10, 11, 12, 17)


def render(ctx) -> str:
    blocks = {b["para"]: b["text"] for b in DESERT_CRAFT
              if b["segment"] == "identity_register"}
    return "\n\n".join(blocks[p] for p in _PARAS if p in blocks)


SEGMENT = {"name": "identity_register", "cache_stability": "static",
           "eviction_priority": 1, "render": render,
           "sources": "voice_profile (speaking_model, identity, native_measure, traits) via craft paras 1,2,7-12,17 (coverage-mapped)"}
