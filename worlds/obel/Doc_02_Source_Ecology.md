# Doc_02 — Source Ecology

**World: The Old Believers** (`the-old-believers`, file-code `obel`)

**Status: Draft, Round 1 — pending review.**

**Built together with:** `obel_Source_Registry.md` (the Registry — the
same pass, per the Source Registry Template V1.0's own instruction not to
build these as two separate steps).

**Built from:** `Doc_01_World_Identification_Boundaries_Orientation.md`
(this world's own approved boundary); `worlds/_cross-world/dossiers/
the-old-believers_Source_Readiness_Dossier.md`; `cic/corpus-map/
the-old-believers.yaml`; the `python -m engine.m9.cli holdings obel`
report run this session; `python cic/engine/corpus_index.py --entry
the-old-believers` searches run this session; and this world's own two
vendored files, read in full.

---

## 0. The library as it actually stands — recount

**This is this project's first Slavic/Russian-Orthodox-schism world.**
Before this pass, nothing was vendored for it (independently re-confirmed
this session: `cic/corpus-map/the-old-believers.yaml` did not exist;
`worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_
Dossier.md` did not exist; a name/title scan of `cic/corpus-map/
WORKS.yaml` and `AUTHOR-IDS.yaml` for "Avvakum," "Nikon," "Solovetsky,"
"Old Believer," and "raskol" returned no hits).

This session vendored two files, both bearing on the same single work —
Avvakum's autobiography — in two languages:

1. `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` — the
   1924 Hogarth Press first English translation (Jane Harrison & Hope
   Mirrlees, preface D. S. Mirsky). 155pp. Verbatim-ready.
2. `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`
   — the same work in its own original language (Old East Slavic/early
   Russian, ISO 639-3 `orv`). Second-witness-only.

**This is a genuinely thin library — one work, two witnesses to it — and
this document says so plainly rather than pad the ecology narrative to
sound fuller than the evidence supports.** Everything below is scaled to
what this library can actually settle; §16 names, at length, what it
cannot.

---

## 1. Primary Voices

### 1.1 Avvakum Petrov (Archpriest Avvakum, c. 1620/21-1682) — the
movement's central and, in this library, only inside voice

Avvakum is present in exactly one work, in two language witnesses: his
own autobiography (*Zhitie*, "Life"), written c. 1673 at Pustozersk. This
is a first-person narrative covering his own ministry, his decade of
Siberian exile (1653-1663) under voevoda Afanasy Pashkov, his return to
Moscow, his final imprisonment, and — within the narrative itself — his
own direct account of disputing the corrected rite before the Eastern
patriarchs at the Chudov Monastery (p. 120, quoted in full at Doc_01 §9).
**Own-voice flag: whole work is Avvakum's own first-person voice**, with
one structural exception the file itself discloses: a footnote at p. 33
states "In the original manuscript this is in the writing of Epiphanius"
— i.e., the autobiography's own manuscript tradition records that at
least one passage was physically written by Avvakum's confessor
Epiphanius, at Avvakum's own dictation or instruction, not by Avvakum's
own hand. This document treats the whole work as Avvakum's own voice
(the content is consistently first-person and self-authored in
substance) but discloses this single noted exception rather than imply
uniform manuscript authorship throughout.

**Quotable passages, exact loci** (English file; page numbers are the
file's own printed pagination, confirmed against the nearest preceding
page-marker line):

| Passage | Locus | Quotability | Own-voice/opponent-voice |
|---|---|---|---|
| Opening dedication: "Avvakum, archpriest, was bidden by the monk Epiphanius... to write down my life" | p. 32 | Verbatim-ready | Own-voice (Avvakum, with the p. 33 manuscript-authorship caveat noted above) |
| The Markovna passage: "How long, archpriest, are these sufferings to last?" / "Markovna! till our death" | p. 80 | Verbatim-ready | Own-voice (both Avvakum's own narration and his wife Anastasia Markovna's quoted speech, as reported by Avvakum) |
| The Chudov Monastery dialogue (two/three fingers; "Nikon, the wolf, together with the devil...") | p. 120-121 | Verbatim-ready | Mixed in one passage: the Eastern patriarchs' own words are quoted by Avvakum as opponent-voice, directly followed by Avvakum's own reply as own-voice — **flag this passage's own internal voice-switch explicitly if quoted**, do not attribute the patriarchs' words to Avvakum or vice versa |
| Closing devotional passage ("...When we die, then shall this be read...") | p. 155 (file's own last page, "THE END") | Verbatim-ready | Own-voice |

**Quotable passage, exact locus** (Russian original file — no internal
page numbers; located by exact string search against the vendored file):

| Passage | Locus | Quotability | Own-voice/opponent-voice |
|---|---|---|---|
| Opening declaration on plain speech vs. "philosophical verses" | First paragraph of the vendored file (verified by direct string search, 2026-09-25) | **Second-witness-only** (per the transcription-lineage caveat, Registry R2) | Own-voice |

**Author Gravity Assessment (five dimensions, per the Expanded
requirement), preliminary — Doc_04's own work is authoritative:**

- **Transmission history**, named as its own dimension per the Source
  Registry Template §50: the English translation (1924) is one specific
  editorial choice among what could have been rendered differently; the
  original-language witness is a modern (undated) crowd transcription of
  uncertain critical-edition lineage (Registry R2; `Open_Gaps_Tracking.md`
  entry 6) — **this world's whole evidentiary base currently rests on a
  transmission chain with a real, disclosed weak link**, not a
  clean, single-hop primary artifact.
- **What becomes over-visible because this source survives:** Avvakum's
  own voice, his own sufferings, and his own theological framing of the
  dispute (§Doc_01 §9) dominate this world's current evidentiary base
  totally, because it is the only inside voice this library holds.
- **What becomes under-visible:** every other voice in this world —
  Nikon's own reasoning (this library holds none of his own words); the
  Solovetsky petitioners' own case in their own words (not yet vendored);
  the priestless/bezpopovtsy theological argument in its own mature form
  (Pomorian Answers, not yet vendored); any woman's own words in her own
  voice (Boyarynia Morozova is named in the census but no primary text of
  hers, or about her in period language, is vendored); Evfrosin's
  internal dissent against self-immolation, in his own words (not yet
  vendored). **This is a severe single-source asymmetry, named plainly
  per §11 (Source Asymmetry Assessment).**

### 1.2 Opponent voices — present only inside Avvakum's own quotation

The Eastern patriarchs and Nikon himself are not vendored as independent
voices. The only words attributed to them in this library are Avvakum's
own quotations of them (p. 120, above) — **reported opponent-speech,
inside an own-voice narrative, never a source in its own right.** Any
future document quoting "what the patriarchs said" must attribute it as
Avvakum's own report of their words, not as an independently sourced
patriarchal statement.

### 1.3 Lay and non-founder voices

None vendored. Boyarynia Feodosia Morozova (named in the census as
numerically central to the priestless communities' own memory) has no
primary text in this library. This is a named gap (§12).

---

## 2. Secondary Voices

Two works are cited, at the census's own confidence level, and are
**not** vendored (secondary scholarship is not vendored into
`cic/texts/`, per project convention — Registry R3, R4):

- Robert O. Crummey, *The Old Believers and the World of Antichrist*
  (1970/2011) — the Vyg community and the Russian state; the standard
  English-language monograph on this movement.
- Georg B. Michels, *At War with the Church* (1999) — reconstructs the
  early schism from the state's own archives, and is specifically noted
  (census) as complicating the movement's own self-narrative of early
  coherence — a genuine methodological check this document flags for
  Doc_05/Doc_07's own use: **do not read Avvakum's own account, or any
  later Old Believer martyrology, as an uncontested historical record of
  the schism's own early years** without Michels's own corrective in
  view.

A reference-level work (*Cambridge History of Christianity* vol. 5, the
Dixon chapter) is cited at low confidence (Registry R5) with its own
chapter-numbering inconsistency disclosed rather than resolved this pass.

---

## 3. Author Gravity — cross-check against corpus-map

`cic/corpus-map/the-old-believers.yaml` (generated this session,
`corpus_map_merge.py --write-only avvakum`, `--check` clean) carries two
rows, both `role: tradition`, `confidence: assigned`:

- `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` — "The
  Life of the Archpriest Avvakum by Himself"
- `avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`
  — "Zhitie protopopa Avvakuma, im samim napisannoe (original-language
  text)"

Both rows carry `source_file`, `role`, and `confidence` per the corpus-map
schema as `corpus_map_merge.py` actually emits it today (its own `_KEEP`
tuple: `work, author, source_file, locus, role, confidence, note`).
**Corrected, self-review:** an earlier pass of this document claimed
`row_id`/`voice_of` were simply "not a field this schema currently
emits... consistent fleet-wide, not a gap specific to this world" — true
as far as it went, but incomplete in a way worth stating precisely
rather than leaving it sounding like a settled non-issue.
`cic/corpus-map/fixture-synthetic.yaml`'s own header discloses that
`row_id`, `voice_of`, `locus_ids`, and `documented_exchange` are real,
named, in-progress schema fields ("CM-1/CM-2/CM-4/CM-8") that "real
buckets don't carry yet" — a live migration a separate "corpus-map's own
thread builds... for real data," currently proven only against synthetic
fixture data, not yet rolled out to any real world's own bucket. **This
means V1.8 §2's own explicit requirement ("corpus-map rows with
`row_id`, corrected `role` and `voice_of`") is not something this
document's own drafting choices can satisfy structurally** — the tooling
that would carry it does not yet write it for any real world, this one
included. This document meets V1.8's own functional intent the only way
currently available: recording own-voice/opponent-voice directly in
prose (§1.1's table above), not in the corpus-map YAML's own row fields.
Logged as `Open_Gaps_Tracking.md` entry 9 — a cross-world tooling gap,
not a finding this build thread can close, and not this world's own
defect.

---

## 4. Institutional Evidence

None vendored. The 1666-1667 Moscow council's own acts and anathemas, and
the state's own 1685 persecution decrees, are named in the census but not
independently verified against a primary source this pass (Doc_01 §2.1,
§2.3; `Open_Gaps_Tracking.md` entry 2).

---

## 5. Holdings disposition (R13, per V1.8)

`python -m engine.m9.cli holdings obel` was run this session before this
document's own review (output captured in the build log). Result: 140
vendored files fleet-wide, of which this world's own two new files both
show `no coverage entry` — **a library-tooling gap, not a finding about
this world's own sources.** The holdings tool's own `corpus_tier` logic
(`engine/m1/cross_world.py`) reads a separate, legacy, hand-maintained
COVERAGE table that has never included this world (it predates this
world's own corpus-map bucket entirely) — its own module docstring
already names this exact relocation as known, disclosed, deliberately
unattempted remainder work, not something this thread's own scope covers.
**No file this run was marked `not yet assessed` or `in scope, unread`**
(the two tiers V1.8 requires an individual Doc_02 line for) — every file
fell into `by design` (2), `out of window` (93, this world not among
them, per the tool's own separate window logic), or `no coverage entry`
(45, including this world's own two files). Per V1.8's own rule ("Files
marked 'no coverage entry' are a library gap, not the drafter's job; list
their count and leave them"), this document lists the count (45) and
leaves them, rather than attempt the separate relocation project the
module's own docstring already defers.

---

## 6. Thin-evidence map

| Question | Evidence in this library | Confidence |
|---|---|---|
| Why did the schism happen? (Nikon's corrections; the anathema) | Avvakum's own narrative frames this but does not narrate the council itself | Widely Accepted (secondary-corroborated, not primary-verified) |
| Was self-immolation the movement's own uncontested practice? | Avvakum's own approving epistles are named (census) but not vendored; Evfrosin's dissenting tract is named but not vendored | Contested — genuinely thin, both sides of the internal argument currently un-vendored |
| What was daily communal/liturgical life actually like in a priestless community? | Nothing vendored | Inferential-Thin — no evidence in this library at all |
| Women's own voice/experience | Nothing vendored (Morozova named, not sourced) | Inferential-Thin |
| The Solovetsky monks' own self-understanding, in their own words | Not vendored | Inferential-Thin |
| The mature priestless (bezpopovtsy) theological argument | Pomorian Answers named, not vendored | Inferential-Thin |

---

## 7. Edition and original-language notes

| Work | Primary text (this world's evidentiary language) | Cross-check | Relationship disclosed |
|---|---|---|---|
| Avvakum's *Life* | English (1924 Harrison & Mirrlees) — this project's evidence language | Original-language (Wikisource, undated transcription) | **Not page-for-page aligned** — the original's own opening rhetorical declaration (plain speech vs. philosophical verses) does not appear at the equivalent point in the English translation as vendored (Doc_01 §4; `Open_Gaps_Tracking.md` entry 5). Any future quotation drawing on both witnesses for the "same" passage must confirm they are in fact the same passage, not assume translation-alignment. |

Per `cic/texts/INTAKE.md`'s 2026-09-25 ruling (a clean public-domain
original can be primary evidence regardless of language, credibility and
truth deciding primacy rather than language): this document treats the
English 1924 translation as this world's primary quotable text
(verbatim-ready, its own transcription lineage fully traceable to a
specific, dated, rights-clean first edition) and the Russian original as
a second witness (not yet verbatim-ready, pending the transcription-chain
verification named at `Open_Gaps_Tracking.md` entry 6) — not because of
language, but because the English file's own provenance is currently the
more fully verified of the two.

---

## 8. Cross-world overlaps and pairs

None found. `cic/corpus-map/PAIRS.yaml` was not modified this pass — no
pairing candidate was identified with any other world's own corpus.
Doc_01 §5, §8 already state this finding; this document confirms it
independently from the library side rather than merely repeat Doc_01's
own claim.

---

## 9. Material and archaeological sources

Not consulted this pass. The census's own `legacy` field (icon-painting
styles, znamenny chant, manuscript practices preserved in Old Believer
communities) is the only lead on record, and is not independently
verified against a material-culture source (Doc_01 §4). Named here as a
real, optional line per V1.8, not filled in.

---

## 10. Missing Voices Assessment (Constitution Article 20)

- **Women.** Boyarynia Feodosia Morozova is named repeatedly (census; the
  documented-stories record) as numerically central to the priestless
  communities' own memory, and as a specific, named martyr (starved to
  death, 1675) — but no primary text by her or about her in period
  language is vendored in this library. This is named as a real,
  unresolved gap, an affirmative duty under Article 20, not passed over.
  A verified acquisition lead exists (the Tale of Boyarynya Morozova,
  17th-century, public domain by date) but was not successfully
  downloaded this session (a Wikimedia Commons fetch returned an HTTP 429
  rate-limit; see the Source Readiness Dossier's own "Verified acquisition
  leads" framing — this is a live lead, not closed).
- **Ordinary believers, priestless communities' own daily life.** Nothing
  vendored (§6).
- **The movement's own internal dissent (Evfrosin against
  self-immolation).** Named, not vendored (§1.1, §6; Registry R9,
  flagged for priority acquisition).

---

## 11. Source Asymmetry Assessment

This world's current library is a maximal case of founder/single-voice
asymmetry: one man's own autobiography, in two language witnesses of the
same work, is the entire primary-source base. This is disclosed
explicitly, not softened: **any claim about "the movement's" own
experience, belief, or practice beyond what Avvakum's own text can settle
should be treated as Contested or Inferential-Thin until this library
grows**, regardless of how confidently the census or secondary
scholarship states it.

---

## 12. Forces Lens Applied to Source Ecology (Forces Framework V1.1 §4,
Step 2)

Preliminary. The library's own shape already suggests which forces are
evidenced and which are asserted: the initiating force (refusal of
liturgical correction, Doc_01 §7) is directly evidenced in Avvakum's own
words; the ongoing force (suffering/testimony under persecution) is
directly evidenced; the contested ending-force candidate (self-immolation
as final refusal) is currently evidenced only by the census's own
secondary characterization, not by either side's own primary voice in
this library — a genuine caution for Doc_08's own six-cell matrix, not a
finding this document resolves.

---

## 13. Confidence Calibration and Propagation

Every confidence tag used in Doc_01 and this document follows the
project's five-level `formation_confidence` vocabulary (Documented /
Widely Accepted / Dominant Modern Reconstruction / Contested /
Inferential-Thin). No claim in either document is presented as settled
where this library's own evidence is thin or contested (§6). Death-toll
figures for self-immolation incidents are Contested and must stay so in
every later document unless a primary source independently settles a
specific figure.

---

## 14. Disposition of Doc_01's open items

Doc_01 §10, §12 name five open items. This document does not resolve any
of them (that is not Doc_02's own job at this stage) but confirms each is
correctly carried to `Open_Gaps_Tracking.md` (entries 1-6) rather than
silently dropped.

---

## 15. Open items carried forward (new, from this pass)

Added to `Open_Gaps_Tracking.md`:

- Entry 6 (transcription-chain verification for the Russian-original
  file) — new this pass.
- Entry 7 (V1.8 merge state) — new this pass, a housekeeping/process
  finding, not a content gap.
- Entry 8 (review-tooling limitation) — new this pass, disclosed
  plainly.
- Entry 9 (`row_id`/`voice_of` not yet emitted by the real corpus-map
  tooling, a fleet-wide gap) — new this pass, found on self-review of
  §3's own first draft; disclosed plainly rather than left implying a
  settled non-issue.

No item from Doc_01 is re-opened or narrowed here; all five carry forward
unchanged.

---

## 16. Disposition and escalation check

**Escalation check:** not a Representative identity decision; not a
portfolio-level or cross-world decision (Doc_01 §2.2 already declined to
re-litigate the Era 8 portfolio boundary, and this document does not
either); not a governance/methodology change (the V1.8-not-merged finding,
`Open_Gaps_Tracking.md` entry 7, is a housekeeping gap, not a disputed
process question — flagged, not escalated); this is Round 1, so no
three-round unresolved tension applies. **No escalation category
applies.**

**Self-assessment against the task's own bar** ("a church-history
professor would be impressed"): this document is honest about being thin
rather than impressive-sounding. Given the actual state of this world's
library — one work, two witnesses, vendored for the first time this
session — the more defensible professional posture is exactly this one:
name what the evidence actually supports, flag every place it does not,
and resist the temptation to borrow the census's own confident prose
register for claims this library cannot yet independently back.

---

## 17. Document log

- Round 1 draft, 2026-09-25, this build thread, together with
  `obel_Source_Registry.md`.
- Round 1, self-review fix applied directly (cosmetic — a precision
  correction, not a change to any claim's substance, confidence rating,
  sourcing conclusion, or scope boundary): §3's characterization of the
  `row_id`/`voice_of` gap corrected from "not a gap specific to this
  world" (true but incomplete) to name the actual, disclosed, in-progress
  fleet-wide migration responsible for it (`Open_Gaps_Tracking.md`
  entry 9).
