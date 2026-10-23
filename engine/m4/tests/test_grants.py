from engine.m4 import grants


def test_the_default_grant_is_the_free_allowance():
    assert grants.resolve(None, completed=3, free_cap=10) == grants.TurnGrant(cap=10)


def test_a_provider_decides_the_grant_from_the_count():
    seen = []

    def provider(completed):
        seen.append(completed)
        return grants.TurnGrant(cap=completed + 1)

    assert grants.resolve(provider, completed=12, free_cap=10) == grants.TurnGrant(cap=13)
    assert seen == [12]


def test_a_provider_that_fails_leaves_the_free_grant():
    def broken(completed):
        raise RuntimeError("down")

    assert grants.resolve(broken, completed=12, free_cap=10) == grants.TurnGrant(cap=10)
