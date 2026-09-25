"""engine.m3.live_admission_run's own safety gates - never the live run
itself (that is real, billed Bedrock spend; this module must NEVER call
run() past its preflight checks). Every case here aborts via SystemExit
before loader/client construction, so none of it touches the network or
needs credentials.
"""
import math

import pytest

from engine.m3.live_admission_run import DEFAULT_MAX_USD, estimate_run_cost_usd, run


def test_default_max_usd_is_marks_ruled_three_dollars():
    """2026-09-25 ruling: the M3 live-admission ceiling is $3/run, no
    weekly or aggregate cap - --max-usd defaults to exactly this."""
    assert DEFAULT_MAX_USD == pytest.approx(3.00)


def test_omitting_max_usd_falls_back_to_the_three_dollar_ceiling():
    """The ceiling is the default itself, not an opt-in: a --worlds
    request big enough to exceed $3 aborts even when --max-usd is never
    named on the command line."""
    per_world = estimate_run_cost_usd(1)
    world_count = math.ceil(DEFAULT_MAX_USD / per_world) + 1
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        run("us-east-1", world_keys=["alx"] * world_count, authorized_by="test-harness")


def test_estimate_scales_linearly_with_world_count():
    """protocol.battery() is the same fixed battery for every world, so
    the preflight estimate should double when the world count doubles."""
    one = estimate_run_cost_usd(1)
    two = estimate_run_cost_usd(2)
    assert one > 0
    assert two == pytest.approx(one * 2)


def test_a_run_over_the_max_usd_ceiling_aborts_before_any_billed_call():
    tiny_ceiling = estimate_run_cost_usd(1) / 2
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        run("us-east-1", world_keys=["alx"], max_usd=tiny_ceiling, authorized_by="test-harness")


def test_a_blank_authorized_by_aborts():
    generous_ceiling = estimate_run_cost_usd(1) * 100
    with pytest.raises(SystemExit, match="--authorized-by is required"):
        run("us-east-1", world_keys=["alx"], max_usd=generous_ceiling, authorized_by="   ")


def test_an_unregistered_world_key_aborts_before_any_billed_call():
    generous_ceiling = estimate_run_cost_usd(1) * 100
    with pytest.raises(SystemExit, match="not a real formation world"):
        run("us-east-1", world_keys=["not-a-real-world"], max_usd=generous_ceiling, authorized_by="test-harness")
