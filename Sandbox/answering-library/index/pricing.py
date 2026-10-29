import sys
from dataclasses import dataclass

from .catalog import REPO_ROOT

MODEL_ID = "claude-haiku-4-5-20251001"
BATCH_DISCOUNT = 0.5
BATCH_DISCOUNT_SOURCE = (
    "the vendor's published batch rate is assumed to be half the standard rate (the repo carries no batch price), "
    "and the live-test guard does not expose the batch endpoint"
)


def price_table(model_id: str = MODEL_ID):
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from engine.m8.price_tables import price_for_model

    table = price_for_model(model_id)
    if table is None:
        raise LookupError(f"no approved price for model {model_id!r} in engine/m8/price_tables.py")
    return table


@dataclass
class Usage:
    calls: float = 0.0
    fresh_input: float = 0.0
    cache_write: float = 0.0
    cache_read: float = 0.0
    output: float = 0.0
    uncached_input: float = 0.0

    def add(self, other: "Usage") -> None:
        for name in self.__dataclass_fields__:
            setattr(self, name, getattr(self, name) + getattr(other, name))

    def scaled(self, factor: float) -> "Usage":
        return Usage(**{name: getattr(self, name) * factor for name in self.__dataclass_fields__})

    def breakdown(self, table) -> dict[str, float]:
        return {
            "cache_write": self.cache_write * table.cache_write_per_token,
            "cache_read": self.cache_read * table.cache_read_per_token,
            "fresh_input": self.fresh_input * table.input_per_token,
            "uncached_small_windows": self.uncached_input * table.input_per_token,
            "output": self.output * table.output_per_token,
        }

    def dollars(self, table) -> float:
        return sum(self.breakdown(table).values())
