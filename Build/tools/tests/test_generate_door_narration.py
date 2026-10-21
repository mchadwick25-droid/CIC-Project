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


class ApprovedRunGate(unittest.TestCase):
    paid = ["--voice-id", "v", "--model", "m", "--output-format", "mp3_44100_64", "--settings-json", "{}", "--force"]

    def run_main(self, extra):
        def no_network(*a, **k):
            raise AssertionError("network call attempted")
        saved_urlopen, saved_key = g.urllib.request.urlopen, g.os.environ.get("ELEVENLABS_API_KEY")
        saved_entries = g.door_entries
        g.door_entries = lambda: [{"key": "a", "text": "hello", "hash": g.fingerprint("hello")}]
        g.urllib.request.urlopen = no_network
        g.os.environ["ELEVENLABS_API_KEY"] = "placeholder-not-a-key"
        try:
            with self.assertRaises(SystemExit) as caught:
                g.main(self.paid + extra)
            return str(caught.exception)
        finally:
            g.urllib.request.urlopen = saved_urlopen
            g.door_entries = saved_entries
            if saved_key is None:
                g.os.environ.pop("ELEVENLABS_API_KEY", None)
            else:
                g.os.environ["ELEVENLABS_API_KEY"] = saved_key

    def test_without_an_approved_run_it_stops_before_any_request(self):
        self.assertIn('--approved-run "<name>" is required', self.run_main([]))

    def test_without_a_char_cap_it_stops_before_any_request(self):
        self.assertIn("--char-cap <n> is required", self.run_main(["--approved-run", "r"]))

    def test_over_its_cap_it_stops_before_any_request(self):
        self.assertIn("over its --char-cap of 1", self.run_main(["--approved-run", "r", "--char-cap", "1"]))

    def test_unit_check_accepts_a_run_within_its_cap(self):
        g.require_approved_run("r", 100, 100)


if __name__ == "__main__":
    unittest.main()
