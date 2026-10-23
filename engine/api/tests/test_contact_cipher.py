"""The contact file, sealed with the real cipher: what its bytes hold, and what opens it."""
import pytest

from engine.accounts.contacts import ContactStore
from engine.api.contact_cipher import ContactCipher, ContactKeyError, PreviousContactKey, parse_previous

SECRET = "c" * 40
OTHER = "d" * 40


def test_a_sealed_address_opens_with_its_key_and_context_only():
    cipher = ContactCipher(SECRET)
    blob = cipher.encrypt("ada@example.org", "contacts|acct1")
    assert cipher.decrypt(blob, "contacts|acct1") == "ada@example.org"
    assert cipher.decrypt(blob, "contacts|acct2") is None
    assert ContactCipher(OTHER).decrypt(blob, "contacts|acct1") is None


def test_two_seals_of_the_same_address_differ():
    cipher = ContactCipher(SECRET)
    assert cipher.encrypt("ada@example.org", "c") != cipher.encrypt("ada@example.org", "c")


def test_a_changed_blob_does_not_open():
    cipher = ContactCipher(SECRET)
    blob = cipher.encrypt("ada@example.org", "c")
    prefix, _, body = blob.partition(":")
    flipped = body[:-4] + ("AAAA" if not body.endswith("AAAA") else "BBBB")
    assert cipher.decrypt(f"{prefix}:{flipped}", "c") is None
    for junk in ("", "c1", "c1:", "c1:!!!", "zz:abcd", "nonsense"):
        assert cipher.decrypt(junk, "c") is None


def test_a_previous_key_still_opens_old_rows_and_new_rows_use_the_current_key():
    old = ContactCipher(SECRET, key_id="c1")
    blob = old.encrypt("ada@example.org", "c")
    rotated = ContactCipher(OTHER, key_id="c2", previous=[PreviousContactKey("c1", SECRET)])
    assert rotated.decrypt(blob, "c") == "ada@example.org"
    assert rotated.encrypt("x@example.org", "c").startswith("c2:")


def test_keys_must_be_long_distinct_and_apart_from_the_other_keys():
    with pytest.raises(ContactKeyError):
        ContactCipher("short")
    with pytest.raises(ContactKeyError):
        ContactCipher(SECRET, other_secrets=(SECRET,))
    with pytest.raises(ContactKeyError):
        ContactCipher(SECRET, key_id="C1")
    with pytest.raises(ContactKeyError):
        ContactCipher(SECRET, previous=[PreviousContactKey("c1", OTHER)])
    with pytest.raises(ContactKeyError):
        ContactCipher(SECRET, previous=[PreviousContactKey("c2", SECRET)])
    assert parse_previous("c1:" + SECRET + ", c2:" + OTHER)[1].key_id == "c2"
    with pytest.raises(ContactKeyError):
        parse_previous("no-colon")


def test_the_contact_file_holds_no_address_in_the_clear(tmp_path):
    store = ContactStore(str(tmp_path / "c.db"), ContactCipher(SECRET))
    for i in range(50):
        store.put(f"acct{i}", f"person{i}@example.org")
        store.put_pending(f"acct{i}", f"new{i}@example.org")
    store.forget("acct0")
    store._c.close()
    data = (tmp_path / "c.db").read_bytes()
    assert b"example.org" not in data and b"person" not in data and b"new1" not in data
    assert SECRET.encode() not in data


def test_a_deleted_contact_leaves_no_bytes(tmp_path):
    store = ContactStore(str(tmp_path / "c.db"), ContactCipher(SECRET))
    store.put("acct1", "ada@example.org")
    blob = store._c.execute("SELECT blob FROM contacts").fetchone()[0]
    store.forget("acct1")
    store._c.execute("VACUUM")
    store._c.close()
    assert blob.encode() not in (tmp_path / "c.db").read_bytes()


def test_no_column_in_the_contact_file_names_a_person(tmp_path):
    import re
    store = ContactStore(str(tmp_path / "c.db"), ContactCipher(SECRET))
    columns = [r[1] for (t,) in store._c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
               for r in store._c.execute(f"PRAGMA table_info({t})")]
    assert set(columns) == {"account_id", "key_id", "blob"}
    assert not [c for c in columns if re.search(r"address|email|mail|name", c)]
    store.close()
