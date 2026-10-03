import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import generate_door_narration as g  # noqa: E402


class DoorEntries(unittest.TestCase):
    def test_only_admitted_worlds_with_a_representative(self):
        entries = g.door_entries()
        keys = [e["key"] for e in entries]
        self.assertIn("ijc", keys)
        self.assertNotIn("fix", keys)    # built fixture, not admitted
        self.assertNotIn("hus", keys)    # candidate, no Representative
        self.assertEqual(keys, sorted(keys))

    def test_text_is_the_conversation_door_turn(self):
        ijc = next(e for e in g.door_entries() if e["key"] == "ijc")
        self.assertIn("Marius, Deacon of the Letters of Church and Empire", ijc["text"])
        self.assertEqual(ijc["hash"], g.fingerprint(ijc["text"]))


class Plan(unittest.TestCase):
    entries = [{"key": "a", "text": "one", "hash": g.fingerprint("one")},
               {"key": "b", "text": "two", "hash": g.fingerprint("two")}]

    def test_skips_matching_fingerprint_regenerates_changed_or_missing(self):
        manifest = {"a": {"hash": g.fingerprint("one")}, "b": {"hash": "old"}}
        up, gen = g.plan(self.entries, manifest, exists=lambda k: True)
        self.assertEqual([e["key"] for e in up], ["a"])
        self.assertEqual([e["key"] for e in gen], ["b"])
        up, gen = g.plan(self.entries, manifest, exists=lambda k: False)
        self.assertEqual([e["key"] for e in gen], ["a", "b"])

    def test_force_and_only(self):
        manifest = {"a": {"hash": g.fingerprint("one")}}
        _, gen = g.plan(self.entries, manifest, force=True, exists=lambda k: True)
        self.assertEqual([e["key"] for e in gen], ["a", "b"])
        up, gen = g.plan(self.entries, manifest, only=["a"], exists=lambda k: True)
        self.assertEqual([e["key"] for e in up], ["a"])
        self.assertEqual(gen, [])


if __name__ == "__main__":
    unittest.main()
