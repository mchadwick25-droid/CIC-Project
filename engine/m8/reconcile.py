"""Monthly reconciliation (spec principle 13): what the usage log priced for
one route and month, set against the invoice line Mark types in. The ratio
is the measured factor; a drift past the tolerance is reported as a
failure, never absorbed. Reads the usage log only; makes no model call.

    python -m engine.m8.reconcile --db usage.db --month 2026-09 --route bedrock --invoice-dollars 123.45
"""
import argparse
import sys
from dataclasses import dataclass
from datetime import datetime, timezone

from engine.m8.cost import estimate_cost
from engine.m8.log_store import UsageLogStore
from engine.m8.price_tables import price_for_call, price_for_route

DEFAULT_TOLERANCE = 0.05


@dataclass(frozen=True)
class Reconciliation:
    month: str
    route: str
    calls: int
    unpriced_calls: int
    list_dollars: float
    route_dollars: float
    invoice_dollars: float
    list_factor: float | None
    route_factor: float | None
    within_tolerance: bool


def month_bounds(month: str) -> tuple[str, str]:
    start = datetime.strptime(month, "%Y-%m").replace(tzinfo=timezone.utc)
    end = start.replace(year=start.year + 1, month=1) if start.month == 12 else start.replace(month=start.month + 1)
    return start.isoformat(), end.isoformat()


def reconcile(store: UsageLogStore, month: str, route: str, invoice_dollars: float, tolerance: float = DEFAULT_TOLERANCE) -> Reconciliation:
    start, end = month_bounds(month)
    calls = unpriced = 0
    list_dollars = route_dollars = 0.0
    for record in store.read_between(start, end):
        if record.provider != route:
            continue
        calls += 1
        listed = price_for_call(record.call_kind, record.model_id)
        routed = price_for_route(record.call_kind, record.model_id, record.provider)
        if listed is None or routed is None:
            unpriced += 1
            continue
        list_dollars += estimate_cost(record.usage, listed).dollars
        route_dollars += estimate_cost(record.usage, routed).dollars
    list_factor = invoice_dollars / list_dollars if list_dollars else None
    route_factor = invoice_dollars / route_dollars if route_dollars else None
    within = route_factor is not None and unpriced == 0 and abs(route_factor - 1.0) <= tolerance
    return Reconciliation(month, route, calls, unpriced, list_dollars, route_dollars, invoice_dollars, list_factor, route_factor, within)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--db", required=True)
    parser.add_argument("--month", required=True, help="YYYY-MM")
    parser.add_argument("--route", required=True, choices=("bedrock", "anthropic"))
    parser.add_argument("--invoice-dollars", required=True, type=float)
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    args = parser.parse_args(argv)
    result = reconcile(UsageLogStore(args.db), args.month, args.route, args.invoice_dollars, args.tolerance)
    print(f"{result.month} {result.route}: {result.calls} calls, {result.unpriced_calls} unpriced")
    print(f"list price ${result.list_dollars:.2f}, route price ${result.route_dollars:.2f}, invoice ${result.invoice_dollars:.2f}")
    if result.list_factor is not None:
        print(f"invoice / list price = {result.list_factor:.3f}  (the door's invoice factor is compared with this)")
    if result.route_factor is not None:
        print(f"invoice / route price = {result.route_factor:.3f}")
    print("WITHIN TOLERANCE" if result.within_tolerance else "OUT OF TOLERANCE - the price table or the factor needs a decision")
    return 0 if result.within_tolerance else 1


if __name__ == "__main__":
    sys.exit(main())
