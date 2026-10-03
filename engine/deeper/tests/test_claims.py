import pytest

from engine.deeper.claims import CLAIM_TTL_SECONDS, ClaimStore, valid_reference

REF = "r4nd0m-r3f3r3nc3_ABCDEF"


class Clock:
    def __init__(self):
        self.now = 1_800_000_000.0

    def __call__(self):
        return self.now


@pytest.fixture
def clock():
    return Clock()


@pytest.fixture
def store(tmp_path, clock):
    s = ClaimStore(str(tmp_path / "claims.db"), clock=clock)
    yield s
    s.close()


def test_a_claim_can_be_read_again_within_the_hour(store, clock):
    assert store.put(REF, ["AAAA"])
    assert store.get(REF) == ["AAAA"]
    clock.now += CLAIM_TTL_SECONDS - 1
    assert store.get(REF) == ["AAAA"]


def test_a_claim_is_gone_after_the_hour(store, clock):
    store.put(REF, ["AAAA"])
    clock.now += CLAIM_TTL_SECONDS
    assert store.get(REF) is None


def test_purge_deletes_expired_rows_only(store, clock):
    store.put(REF, ["AAAA"])
    clock.now += 1800
    store.put("another-reference-123", ["BBBB"])
    clock.now += 1800
    assert store.purge() == 1
    assert store.get(REF) is None
    assert store.get("another-reference-123") == ["BBBB"]


def test_batch_codes_round_trip_in_order(store):
    store.put(REF, ["AAAA", "BBBB", "CCCC"])
    assert store.get(REF) == ["AAAA", "BBBB", "CCCC"]


def test_a_replay_never_overwrites(store):
    assert store.put(REF, ["AAAA"])
    assert not store.put(REF, ["ZZZZ"])
    assert store.get(REF) == ["AAAA"]


def test_unknown_or_malformed_reference_reads_nothing(store):
    assert store.get("x" * 20) is None
    assert store.get("short") is None
    assert store.get(None) is None
    assert store.get("has space in it!!") is None


def test_put_refuses_a_bad_reference_or_no_codes(store):
    with pytest.raises(ValueError):
        store.put("short", ["AAAA"])
    with pytest.raises(ValueError):
        store.put(REF, [])


def test_valid_reference():
    assert valid_reference(REF)
    assert not valid_reference("a" * 15)
    assert not valid_reference("a" * 65)
    assert not valid_reference("a?b" * 8)


def test_an_expired_row_does_not_shadow_a_new_claim_on_the_same_reference(store, clock):
    store.put(REF, ["OLD1"])
    clock.now += CLAIM_TTL_SECONDS
    assert store.put(REF, ["NEW1"])
    assert store.get(REF) == ["NEW1"]


def test_a_live_row_still_blocks_a_second_put(store, clock):
    store.put(REF, ["OLD1"])
    clock.now += CLAIM_TTL_SECONDS - 1
    assert not store.put(REF, ["NEW1"])
    assert store.get(REF) == ["OLD1"]


def test_no_plain_code_stays_on_disk_after_the_purge(tmp_path, clock):
    path = tmp_path / "claims.db"
    s = ClaimStore(str(path), clock=clock)
    secret = "ZZZZYYYYXXXXWWWWVVVV"
    s.put(REF, [secret])
    clock.now += CLAIM_TTL_SECONDS
    s.purge()
    s.close()
    leftovers = [p for p in tmp_path.iterdir() if p.name.startswith("claims.db")]
    assert leftovers == [path]
    assert secret.encode() not in path.read_bytes()
