import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import align_tree_narration as a  # noqa: E402

TEXT = "Polycarp was an old man.\n\nThe governor threatened him with fire.\n\nHis letter survives."


def heard(words_and_times):
    return [(a.norm(w), t) for w, t in words_and_times]


SPOKEN = heard([
    ("Polycarp", 0.1), ("was", 0.5), ("an", 0.7), ("old", 0.8), ("man", 1.0),
    ("The", 3.0), ("governor", 3.2), ("threatened", 3.8), ("him", 4.2), ("with", 4.4), ("fire", 4.6),
    ("His", 7.0), ("letter", 7.3), ("survives", 7.8),
])


class ParagraphStarts(unittest.TestCase):
    def test_each_paragraph_starts_where_its_first_word_is_heard(self):
        self.assertEqual(a.paragraph_starts(TEXT, SPOKEN), [0.0, 2.85, 6.85])

    def test_a_misheard_first_word_falls_back_to_the_next_heard_word(self):
        spoken = [(w if w != "his" else "is", t) for w, t in SPOKEN]
        self.assertEqual(a.paragraph_starts(TEXT, spoken)[2], 7.15)

    def test_a_paragraph_whose_opening_is_not_heard_gives_no_times(self):
        cut = [(w, t) for w, t in SPOKEN if t < 7.0] + heard([("and", 7.0), ("so", 7.2), ("on", 7.4), ("we", 7.6)])
        self.assertIsNone(a.paragraph_starts(TEXT, cut))

    def test_a_recording_of_other_words_gives_no_times(self):
        self.assertIsNone(a.paragraph_starts(TEXT, heard([("Something", 0.0), ("else", 0.5), ("entirely", 1.0)])))

    def test_a_single_paragraph_needs_no_times(self):
        self.assertIsNone(a.paragraph_starts("One paragraph only.", heard([("One", 0), ("paragraph", 0.3), ("only", 0.6)])))

    def test_times_must_rise(self):
        swapped = [(w, 9.0 if w == "his" else t) for w, t in SPOKEN]
        self.assertEqual(a.paragraph_starts(TEXT, swapped)[2], 8.85)
        backwards = [(w, 1.0 if w == "his" else t) for w, t in SPOKEN]
        self.assertIsNone(a.paragraph_starts(TEXT, backwards))


if __name__ == "__main__":
    unittest.main()
