import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from access_ledger import Ledger, Sku, connect, init_schema


@pytest.fixture
def conn(tmp_path):
    c = connect(tmp_path / "ledger.db")
    init_schema(c)
    return c


@pytest.fixture
def ledger(conn):
    return Ledger(conn)


@pytest.fixture
def catalogue():
    return {"pack_small": Sku(units=4, amount_cents=1000, currency="usd"), "pack_large": Sku(units=10, amount_cents=2000, currency="usd")}
