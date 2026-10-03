from engine.m4 import grants


def test_the_default_grant_is_the_free_allowance():
    assert grants.resolve(None, completed=3, free_cap=10, daily_cap_reached=False) == grants.TurnGrant(cap=10, facilitator_only=False)


def test_a_spent_daily_allowance_makes_the_default_grant_facilitator_only():
    assert grants.resolve(None, completed=3, free_cap=10, daily_cap_reached=True) == grants.TurnGrant(cap=10, facilitator_only=True)


def test_a_provider_decides_the_grant_from_the_count_and_the_daily_flag():
    seen = []

    def provider(completed, daily):
        seen.append((completed, daily))
        return grants.TurnGrant(cap=completed + 1)

    assert grants.resolve(provider, completed=12, free_cap=10, daily_cap_reached=True) == grants.TurnGrant(cap=13)
    assert seen == [(12, True)]


def test_a_provider_that_fails_leaves_the_free_grant():
    def broken(completed, daily):
        raise RuntimeError("down")

    assert grants.resolve(broken, completed=12, free_cap=10, daily_cap_reached=False) == grants.TurnGrant(cap=10)
    assert grants.resolve(broken, completed=12, free_cap=10, daily_cap_reached=True) == grants.TurnGrant(cap=10, facilitator_only=True)
