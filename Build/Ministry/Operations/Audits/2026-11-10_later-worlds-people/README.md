# P2-G3b, the later-worlds people: the clean count — 2026-11-10

Mark's answer D a (Decision-Log 2026-11-10, "The people list ruled; P2-G3 applied as data release
29") held back the people the P2-G3 later-worlds count found. The count was to be re-run with
namesakes checked and the editions' own notes left out, and the clean list put to Mark. This folder
is that re-run. **Read only: no census, data release or live file was changed.** The list waits for
Mark's pick at https://claude.ai/artifact/AGVVFoi57c6gNtDtVoyADC.

## The rule

Decision-Log 2026-11-09, "People on the map": a person is named in at least 5 distinct passages in
each of at least 2 later traditions' own-voice texts. Then ruling 14's test (Decision-Log
2026-11-06, item 14): a party in their own right, with writing of their own or a recorded position,
who founded no lasting movement, with own words read as answer C (2026-11-10).

## How the count was made

| step | what | people |
|---|---|---|
| inputs | P2-G3's alias list (`../2026-11-10_agreed-entries/counts/aliases_all.json`), 1,236 rows | 1,136 after merging one person under two spellings (`scripts/group.py`; only Theoderic/Theodoric merged) |
| raw re-run | ripgrep over the 1,209 files shelved as role `tradition` (`scripts/tally2.py`) | 119 pass on the aliases P2-G3 counted; 195 with the ambiguous one-word aliases let back in |
| editorial mask | XML `<note>` text and apparatus divs (corpus_structure's own patterns), closing indexes, index and contents lines; a mention counts only inside the row's locus where it names lines or a div (`scripts/mask.py`, `scripts/tally3.py`) | 166, less the 23 person entries |
| pass 1 | Sonnet checkers read up to 10 mentions per tradition, top three traditions, and labelled each same person, editorial, namesake or unclear (`Verify_Brief.md`, `round1/`) | 13 pass, 27 with one tradition |
| pass 2 | aliases pass 1 found only on other people dropped; one strict rule (the mention must lie inside the shelved work); fresh mentions for every tradition not yet at 5, and a strict recheck of the batch that had used a looser rule (`Verify_Brief_Round2.md`, `round2/`) | 36 pass; Ephraim the Syrian is the shipped Ephrem entry, so 35 |
| drafting | Sonnet drafted each row: home, dates, own words, founder, quotes (`Drafting_Brief.md`, `drafts/draft_d*.json`) | 12 include, 23 hold |
| review round 1 | three Opus reviewers reopened every counted passage (`Review_Brief.md`, `reviews/Review_Round1_r*.json`): 3 blocking, 18 substantial, 65 minor | 32 pass |
| revision | Sonnet applied every finding (`Revision_Brief.md`, `drafts/revised_v*.json`) | |
| review round 2 | Opus, targeted recheck of what changed (`Review_Round2_Brief.md`, `reviews/Review_Round2.json`): 0 blocking, 3 substantial, 7 minor | 32 pass |
| coordinator fixes | round 2's findings applied (`coordinator_fixes.json`) | 14 include, 18 hold, 3 out |

Final rows: `final_rows.json`. The page is built by `page/build.py` from `page/template.html`.
Two review rounds of the three allowed; no blocking finding was left open.

## The three that fell out at review

- **Theodoret of Cyrrhus** and **Eunomius of Cyzicus**: the traditions that named them began while
  they were alive. The input's `last_year` was the year a people row gives (the bishop's
  accession, an active year), not the death. Theodoret died 457 or 458 and both counted traditions
  start in 451; Jerome's De viris illustribus (392) says Eunomius "is said to be still living".
- **Mar Aba I**: his counted Malech passages lie in the Persia chapter, outside both shelves' loci.

A `last_year` that is too early can only let a tradition in, never shut one out, so the flaw makes
false passes only. Every remaining candidate's counted traditions were checked against the
person's death: all start after it, except that Basilides' death is unknown (held anyway).

## Questions put to Mark (with recommendations)

- **A. Founders who pass by this route** (Priscillian, Valentinus, Mani, Novatian, Hilarion,
  Apollinaris, Valdes, Francis, Zwingli): a, hold (recommended); b, take those whose own words are
  held (Novatian, Apollinaris, Zwingli); c, take all nine.
- **B. Words written for or with them** (Paula's letter issued in her name, Pamphilus's joint
  Apology, Tauler's hearers' notes): a, answer C as written, Paula and Pamphilus in, Tauler held
  (recommended); b, hold all three; c, take all three.
- **C. Both traditions resting on one book** (Constantius II, Basilides): a, hold (recommended);
  b, count shelves as written.

Taking every recommendation gives 14 person entries: Polycarp of Smyrna, Methodius of Olympus,
Pamphilus, Lactantius, Constantine, Paula, Basil of Caesarea, Gregory of Nazianzus, Patrick,
Justinian, Bede, Gregory VII, Innocent III, Hugo Grotius.

## Known limits

- Ambiguous one-word aliases were searched but read in context; a namesake alias dropped after pass
  1 may hide a real mention, so a count can be low, never high.
- Pass 1 sampled 10 mentions per tradition. Pass 2 read fresh mentions only for candidates still in
  reach; the 25 people with one tradition at 5 (listed on the page) and those with fewer were not
  read exhaustively.
- Several counts rest on a later author quoting an earlier text (Eusebius quoting Irenaeus, Nikon
  quoting a gloss) or on a work now credited to someone else (pseudo-Methodius in Liguori and
  Nikon). The rule counts a naming; Methodius of Olympus's Russian count is exactly 5 on this
  reading.
- The first build of `consolidated.json` keyed contexts by an id that repeats across candidates,
  so the drafters saw some wrong refs; `scripts/consolidate.py` was fixed and the reviewers worked
  from the corrected refs.

No model was called outside this conversation. No recording, no paid run.
