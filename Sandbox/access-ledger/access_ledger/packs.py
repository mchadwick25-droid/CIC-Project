"""The pack catalogue sold at launch."""
from .stripe_events import Catalogue, Sku

PACKS: Catalogue = {
    "pack_5": Sku(units=5, amount_cents=700, currency="usd"),
    "pack_13": Sku(units=13, amount_cents=1500, currency="usd"),
    "pack_30": Sku(units=30, amount_cents=3000, currency="usd"),
}

PRODUCT_NAMES: dict[str, str] = {
    "pack_5": "5 conversations",
    "pack_13": "13 conversations",
    "pack_30": "30 conversations",
}


def price_per_conversation_cents(sku: Sku) -> float:
    return sku.amount_cents / sku.units
