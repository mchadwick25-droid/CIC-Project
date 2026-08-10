# The transparency gap Mark found, measured — and what it actually is

**Mark, live site, 2026-08-09:** *"it uses complicated words but no three
level transparency or simple ways to say it."* The two words that stopped
him were **catechumen** and **Didache**.

This is the measured answer to that. It needs two decisions from him and
nothing else.

---

## 1. The finding is not what the complaint sounded like

The complaint sounded like a vocabulary problem. It is mostly a **names**
problem.

`scripts/transparency_reach.py` reads the committed checkpoint artifacts and
lists, per world, what the Representative actually said that carries no
bridge. After filtering for ordinary English, the residue is dominated not by
hard words but by **people and places a reader has never heard of**:

| world | glosses fired | unbridged names the reader met |
|---|---|---|
| Papnoute | **0 of 8 turns** | Psalter, Pachomius, Cassian |
| Albina | 1 of 8 | Bethlehem, Paula, Blaesilla, Origen |
| Marius | 3 of 8 | Milan, Ambrose, Julius, Chalcedon |
| Chloe | 4 of 8 | Corinth, Smyrna, Polycarp, Maranatha |
| Theon | 4 of 8 | Cicero, Origen |
| Yausep | 7 of 8 | Gushtazad, Barba'shmin, Aphrahat, Bardaisan, Mani, Seleucia, Ctesiphon, Simeon, Ephrem |

A reader hits *Aphrahat* or *Gushtazad* and has nothing at all. The gloss
system cannot help: it is keyed on `confirmed_glosses`, which is a
**vocabulary** table. Names were never in scope for it.

**Papnoute firing zero glosses across eight turns is the sharpest single
result in the fleet** and wants its own look regardless of what is decided
below.

## 2. The good news: the data already exists

Every world already has **figure records**, and they already carry exactly
what a bridge would say — an in-world name and a scholarly one-liner:

> `syrfig003` — names: *Jacob of Nisibis* (in-world) / *Jacob (Mar Yaqub) of
> Nisibis, bishop from c. 309* (scholarly)

Those records are already loaded into every Representative's assembled
prompt. **They have no participant-facing path.** The API returns
`citations` and `glosses_used` per turn and nothing else.

Coverage of the names above, checked one by one:

- **Already have a figure record (~65%)** — Pachomius, Antony, Bethlehem,
  Paula, Blaesilla, Milan, Ambrose, Julius, Corinth, Smyrna, Polycarp,
  Origen (Theon's), Ephrem, Aphrahat, Seleucia, Ctesiphon, Simeon.
- **Need one written** — Cassian, Chalcedon, Cicero, Origen (Albina's),
  Gushtazad, Barba'shmin, Bardaisan, Mani.
- **Not figures at all** — *Psalter* and *Maranatha* are a text and a word;
  they belong in the lexicon, not here.

So the name bridge is **mostly wiring, plus eight short records** — far
cheaper than it looked.

## 3. Decision one: build the name bridge?

It is a new participant-facing affordance, so it is Mark's call, not mine.
The shape I would build:

- A detection pass alongside `find_glosses_used`, matching figure-record
  `names[]` against the emitted turn.
- A `figures_used` payload beside `glosses_used`, same shape.
- The frontend reuses `GlossHighlight`'s machinery — same pill, different
  colour, showing the scholarly line on click.
- **Never inline in the voice.** The Representative goes on saying
  "Aphrahat" the way a person would. The bridge is the UI's job, not a
  reason to make the voice lecture — the same principle that settled the
  `inline: false` gloss case.

## 4. Decision two: the word list

Under `confirmed_glosses.py`'s own standing rule — *"reviewed and added one
at a time, per the project owner's own request"* — these are **not** written
in. They are proposed. The high-confidence candidates, after discarding what
the frequency table over-reported:

| world | term | why it is a wall |
|---|---|---|
| Chloe | **catechumen** | Mark's own catch. Looks English, is not. Her lexicon has 13 terms and none is this. |
| Chloe | **Didache** | Named repeatedly as a source with no indication it is a text. |
| Chloe | Maranatha | An Aramaic word given untranslated. |
| Papnoute | Psalter, vigils | Both said plainly, both unglossed, in a world firing zero glosses. |
| Albina | monastery, convent, senatorial, epitaph | Period-institutional vocabulary reading as modern. |
| Marius | deposed, legate | Juridical vocabulary with no in-world bridge. |
| Yausep | (words: none) | His seven-of-eight gloss rate is the fleet's best. His gap is entirely names. |

## 5. What I would not do

**Do not drive the coverage rate up.** Glossing everything produces a
Representative who lectures, which is the failure the whole report exists to
prevent. Every number here is observational, per the Goodhart rule. The list
above is a candidate set for Mark's judgement — not a backlog to burn down.

## 6. An honest note on the instrument

The first two runs of `transparency_reach.py` were wrong and I corrected them
from reading the output, not from reading the code:

1. It reported *walked*, *feels*, *gathered* as hard words — the bundled
   top-5000 list carries base forms only. Fixed with crude morphology.
2. It still reported *cannot*, *beside*, *settled* — that list is a **web**
   frequency table and simply lacks much ordinary literary English. Fixed
   with a cross-world rarity test: a word out-of-list **and** present in at
   most two of the six worlds' record corpora is world vocabulary, because
   ordinary English is ubiquitous across all six corpora and period
   vocabulary is not.

Even after both fixes the word column still carries noise (*rope*, *purse*,
*sorrow* are not walls). The **names** column is clean, which is part of why
I think the names are the real finding. Read the word list as candidates
needing a human eye; read the names list as fact.
