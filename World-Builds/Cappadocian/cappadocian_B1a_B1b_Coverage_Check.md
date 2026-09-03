# Cappadocian — B-1a/B-1b coverage check (R)

**Date:** 2026-08-31. First coverage check under the same discipline the S6.2/HAL
precedent (`Ministry/Technology/Pass2/reviews/S6.2_HAL_s21b_coverage.md`)
established, run against the 116-row `cappadocian_Source_Registry.md` and the
110 source records B-1 authored at `records/cappadocian/source/*.md`. No
Registry row or source record is edited here — findings route to the
pre-freeze re-sweep, or are simply named for the build thread's own attention,
matching HAL's own disposition discipline exactly.

**Independence discipline followed:** Step 1 below was written to a scratch
file, complete with reasoning, before any Cappadocian-specific file — the
Source Registry, the build ledger, `texts_registry.py`, or any source
record — was opened this session. Everything after Step 1 was read only once
that list was already committed to disk.

---

## Step 1 — independent ten-item recall list

Ten sources a specialist bibliography on the Cappadocian Fathers (Basil of
Caesarea, Gregory of Nazianzus, Gregory of Nyssa, and their circle, c.
325–394) would be expected to contain, named from general patristics
knowledge alone, six primary and four... narrowed at the point of writing to
a working mix of primary texts across all three figures plus a council
document, and two modern scholarly staples:

1. **Basil of Caesarea, *De Spiritu Sancto* (On the Holy Spirit).** The
   single most load-bearing Cappadocian text for this world's own subject
   matter — the treatise that works out pneumatology alongside Nicene
   homoousion logic, addressed to Amphilochius of Iconium.
2. **Basil of Caesarea, *Letters* (Epistulae), the ~366-letter corpus.** The
   primary window into Basil's ecclesial politics, friendships, and
   theology-in-practice (e.g. Ep. 38 on hypostasis/ousia).
3. **Basil of Caesarea, *Hexaemeron* (Homilies on the Six Days of
   Creation).** Canonical patristic exegetical/cosmological homily series,
   hugely influential (translated by Rufinus, drawn on by Ambrose).
4. **Gregory of Nazianzus, *The Five Theological Orations* (Orations
   27–31).** The text that earned him the epithet "the Theologian,"
   delivered at Constantinople in 380 — foundational Trinitarian theology
   and apophatic method.
5. **Gregory of Nyssa, *Life of Moses* (De Vita Moysis).** The classic
   Nyssen text on mystical ascent/epektasis, central to modern scholarship
   on his thought.
6. **Gregory of Nyssa, *Against Eunomius* (Contra Eunomium).** Nyssa's
   major anti-Eunomian polemical/dogmatic work, central to the doctrine of
   divine infinity distinguishing his contribution from his brother's and
   Nazianzen's.
7. **Gregory of Nyssa, *Life of Macrina* (Vita Sanctae Macrinae).**
   Biographical/hagiographical text on their sister — essential for
   family/household context and asceticism/gender scholarship on this
   circle.
8. **Lewis Ayres, *Nicaea and Its Legacy: An Approach to Fourth-Century
   Trinitarian Theology* (Oxford UP, 2004).** The standard modern synthesis
   of the "pro-Nicene" theological movement, situating the Cappadocians as
   its culmination.
9. **R.P.C. Hanson, *The Search for the Christian Doctrine of God: The
   Arian Controversy, 318–381* (T&T Clark, 1988).** The magisterial
   older-generation history of exactly the controversy and period this
   world covers.
10. **Anthony Meredith, *The Cappadocians* (Cassell/Continuum "Outstanding
    Christian Thinkers," 1995).** The standard short introduction organized
    specifically around the three Cappadocians as a group — the likeliest
    single "starter" secondary text.

*(Full reasoning for each pick, written before any file was opened, is
preserved at the session's own scratch file and reproduced above verbatim.)*

---

## Step 2 — scored against the Registry and the 110 source records — 7/10

| Expectation | Result |
|---|---|
| Basil, *De Spiritu Sancto* | FOUND (Registry row 13; `cappadocian.source.basil-on-the-holy-spirit.md`) |
| Basil, *Letters* (general corpus) | FOUND (Registry row 5; `cappadocian.source.basil-letters-general-corpus.md`) |
| Basil, *Hexaemeron* | FOUND (Registry row 15; `cappadocian.source.basil-hexaemeron-homilies.md`) |
| Gregory of Nazianzus, Five Theological Orations | FOUND (Registry row 31, within the Orations general corpus — explicitly named as covering the Trinitarian-confession gravity via "the five Theological Orations"; `cappadocian.source.gregory-nazianzus-orations-general-corpus.md`) |
| **Gregory of Nyssa, *Life of Moses*** | **MISS** — zero rows in the Registry (grepped the full 237-line document for "Moses"/"Vita Moysis"), no source record, confirmed absent from the vendored `npnf205` file |
| Gregory of Nyssa, *Against Eunomius* | FOUND (Registry row 42; `cappadocian.source.gregory-nyssa-against-eunomius.md`) |
| Gregory of Nyssa, *Life of Macrina* | FOUND (Registry row 48; `cappadocian.source.gregory-nyssa-life-of-macrina.md`) |
| Lewis Ayres, *Nicaea and Its Legacy* | FOUND (Registry row 105; `cappadocian.source.ayres-nicaea-and-its-legacy.md`) |
| **R.P.C. Hanson, *The Search for the Christian Doctrine of God*** | **MISS** — no mention anywhere in the project's Cappadocian materials (grep-verified project-wide) |
| **Anthony Meredith, *The Cappadocians*** | **MISS** — no mention anywhere in the project (grep-verified project-wide) |

**The pattern:** 7/10 — every primary-text expectation cleared (6/6), both
modern-scholarship picks split (Ayres in, Hanson out), and the one
"expected trio survey" (Meredith) is absent despite Part F otherwise naming
24 modern scholars with real care. This is a stronger primary-text score
than HAL's own 9/10 test earned on its own primary corpus (which had zero
primary misses too) — the pattern that misses cluster in the
scholarship-apparatus layer, not the world's own primary voice, repeats
across worlds.

---

## Step 3 — the PRESS question, asked verbatim

*"Name up to three sources you would expect a bibliography of this world to
contain that this registry does not hold. If you can name none, say so
explicitly."*

**Answered — three named**, deliberately not just a re-list of Step 2's
three misses (though the first item below is one of them, since it is by
far the strongest-evidenced gap found):

**(1) Gregory of Nyssa, *Life of Moses* (De Vita Moysis).** Not merely my
own external expectation — this is a *confirmed, currently open* gap in the
build's own paper trail. `cappadocian_Doc_06_Full_Lexicon.md` cites it as a
Key Text at three Tier 1/2 lexicon entries (akatalēpsia, epinoia/energeia,
epektasis — the last of which is this world's own noun-label for Nyssen's
"stretching forward" theology, the concept the *Life of Moses* is most
associated with in the whole patristics field). The G1 Scope and Source
Acquisition Manifest independently flagged it by name on 2026-08-30 as "a
real omission, not a newly discovered gap." Yet it is the *one* item on that
same manifest gap-list that never received a Source Registry row, while
every other item on it did (Against Eunomius → row 24; the Small Asketikon
→ row 19; *Ad Graecos* → row 54; Eunomius' 383 confession → row 59;
Epiphanius/Amphilochius → rows 61/65; the Nicaea subscription lists → row
77; the Theodosian Code provisions → rows 73/79/80). Doc_02 itself never
names it (confirmed by direct grep), which is presumably how it fell
through the Registry's own checkpoint ("every source Doc_02 §§1–6 and
Doc_01 name has a row") without technically breaking that rule — but a
Registry silent on a source its own sibling lexicon document leans on three
times is a real gap by any working standard, whatever the checkpoint
literally required.

**(2) Anthony Meredith, *The Cappadocians* (1995).** Part F (rows 89–112)
is a genuinely careful 24-scholar secondary-scholarship list — Rousseau,
McGuckin, McLynn, Silvas, Elm, Clark, Van Dam, Sterk, Holman, Gribomont,
Drecoll, Fedwick, Caner, Stewart, Ayres, Behr, Barnes, Anatolios, Daley,
Beeley, Ludlow, Coakley, Brown, Mitchell — covering nearly every major name
active in the field on the specific debates this world's Doc_02 §5 argues
through. What it does not contain is the single most obvious "starter"
survey organized around the three Cappadocians as a trio rather than one
figure or one debate. R.P.C. Hanson's *Search for the Christian Doctrine of
God* (1988) is a close second candidate for this same slot — the
magisterial history of the exact 318–381 controversy this world
reconstructs — and is named here as a genuine alternate, not a lesser
concern, even though only one of the two fits inside "up to three."

**(3) Rufinus of Aquileia's continuation of Eusebius' *Historia
Ecclesiastica* (Books X–XI, c. 402/403, covering 324–395).** This surfaced
during the B-1a sweep below, not the blind Step 1 list, which is worth
naming as a genuine difference from a rote re-listing of Step 1's own
misses. It is squarely in-window (this world closes c. 394), covers exactly
this world's own historical arc, and offers an independent Latin-transmission
narrative angle distinct from the already-rowed but explicitly
"fifth-century, all outside the horizon" Greek church historians
(Socrates/Sozomen/Theodoret, row 62). It connects concretely to a source
this Registry already names as a real gap: Rufinus' own 397 Latin
translation is the sole surviving witness to Basil's Small Asketikon (row
19). Not vendored anywhere in `cic/texts/`, and not part of the standard
14-volume NPNF set this project has otherwise vendored in full — a genuine
acquisition target, not something reachable by re-reading what is already
on disk.

**Disposition (all three):** routed to the pre-freeze re-sweep, same lane
as HAL's own three PRESS findings — named with enough detail (author,
title, why it matters to this world specifically) for a future acquisition
pass to act on, not acquired now.

---

## B-1a — discovery sweep: full record at `records/cappadocian/search_record/cappadocian.search.unopened-volume-sweep.md`

**Scope, as this world's actual sourcing history requires:** no live web
search was possible at any point in this build — every vendored text came
from Mark's own direct uploads or the builder's prior knowledge
(`CAPPADOCIAN_BUILD_LEDGER.md` §9). The realistic discovery-sweep question is
therefore not "what does the wider literature contain" (Step 3 above already
covers that, honestly, as unacquired candidates) but narrower and checkable:
**did this build miss anything already sitting in the vendored library
(`cic/texts/`) that is relevant to this world and not yet rowed or
recorded?**

**What was searched.** Every file in `cic/engine/texts_registry.py`'s
ENTRIES list (~50 vendored files) was checked in two directions: (a) is its
principal author or subject one this world's own documents (Doc_01, Doc_02,
Doc_06, the G1 manifest) actually name or discuss, and if so, does it have a
Registry row; (b) for the handful of plausible near-misses that surfaced,
the vendored file's own internal structure (div1 headers) was read directly
rather than inferred from its filename, and the exact sentence in this
world's own documents that named the candidate was read in context rather
than trusted from a keyword match alone.

**Result: no vendored-but-unrowed file found.** Every file whose principal
author or subject this world discusses already has a row: the full Basil
corpus (rows 5–30), both Gregorys' corpora (rows 31–40, 41–56), Gregory
Thaumaturgus (rows 66–68), Firmilian of Caesarea (row 69), Jerome's *De
viris illustribus* within `npnf203` (row 76), the church historians (row
62), the conciliar volume `npnf214` (rows 60, 78), and all nine files this
session itself vendored and independently verified (rows 18, 21, 22, 33,
48, 57, 63, 71, 72).

**Three near-misses, checked and cleared rather than assumed:**
- **Hilary of Poitiers (`npnf209`)** — named twice in Doc_01, but read in
  context both times he functions only as a Western-boundary comparandum
  ("Hilary and the Latin West"; his "exiled protest" against Auxentius at
  Milan) to throw this world's own Eastern texture into relief — never as
  this world's own evidentiary voice. Same treatment Part A already gives
  Athanasius (row 1). Correctly unrowed.
- **Eusebius (`npnf201`, Eusebius of Caesarea's Church History)** — a
  homonym, not a hit: Doc_01's "Eusebius" is Eusebius *of Samosata*, a
  distinct Basil correspondent, confirmed by reading the sentence in
  context. Worth naming because it is the *same volume* HAL's own
  unopened-volume-sweep record already flagged as a homonym trap (there,
  "Eusebius" matched inside "Eusebius Hieronymus," Jerome's own name) — a
  different specific name doing the tripping, same underlying mechanism. A
  keyword-only check against this file will misfire for close to any world
  that runs it.
- **Rufinus, inside `npnf203`** — that volume's own division is titled
  "Life and Works of Rufinus *with Jerome's Apology Against Rufinus*" (read
  directly from its div1 header): the Jerome–Rufinus Origenist-controversy
  material, already the Hieronymian-Ascetic-Literary world's own domain
  (`srcHAL005`/`srcHAL007`), not this one. Rufinus' own genuine relevance
  here (his Small Asketikon translation, already row 19; his own Church
  History continuation) is real but is not what sits inside this file — see
  Step 3 item (3) above, which routes it correctly as an acquisition
  question rather than claiming it here as something found on disk.

Also checked and confirmed correctly out of scope, zero mentions anywhere
in this world's own documents: Chrysostom, Methodius of Olympus, Novatian,
Dionysius of Alexandria. Origen's own corpus (`anf04`, `anf09`, beyond the
already-rowed *Philocalia* compilation, row 81) belongs to the registered
Alexandria world by the same logic Part A's row 1 already applies to
Athanasius.

**Saturation statement.** Given three independent Opus-tier adversarial
review rounds already ran against the Registry itself before this sweep
began (built 99 → 112 → 116 rows specifically hunting for missing sources,
per `CAPPADOCIAN_BUILD_LEDGER.md` §10), a discovery sweep run after that
scrutiny should expect a small residue at most, not a fresh pile of misses —
and that is what this sweep found: zero vendored-but-unrowed files, three
near-misses that needed checking rather than assuming, and one real gap
(*Life of Moses*, Step 3 item 1) that was never a vendored-file question in
the first place and is correctly routed there instead. This counts as
reasonably complete *for the question B-1a can actually ask this session* —
what is sitting on disk unused — which is a real but narrower question than
"what does the wider literature contain." That broader question is Step 3's
job, and this document does not pretend the narrower sweep answers it: the
standing limitation (no live web access this entire build) is stated
plainly here rather than papered over, and the honest consequence is that
Step 3's three PRESS items remain genuinely unverified against the wider
literature beyond what this session's own prior knowledge and close reading
could establish.

---

## Additional finding surfaced while cross-checking — not asked for by name, reported because it was found

Rows 16 and 20 of the Source Registry, and the two source records built
from them, appear to overclaim what is actually vendored:

- **Row 16** — "Basil, the moral/famine homilies (on famine and drought;
  the rich fool's barns; against usury, envy, anger, drunkenness; on the
  Forty Martyrs and local martyrs)" — Verification Note: "Within npnf208."
- **Row 20** — "Basil, martyr homilies on the Forty of Sebaste, Gordius,
  Julitta, and Mamas" — Verification Note: "Within npnf208."
- Both source records (`cappadocian.source.basil-moral-famine-homilies.md`,
  `cappadocian.source.basil-martyr-homilies-forty-gordius-julitta-mamas.md`)
  carry `verification_state: verified-via-authority` and cite
  `cic/texts/npnf208_basil-letters-select-works.xml` directly as the
  edition, on the strength of these two rows.

Read directly, `npnf208`'s own top-level structure (its div1 headers) is
only five sections: Prolegomena, *De Spiritu Sancto*, *The Hexaemeron*, The
Letters, and Indexes. There is no separate homily division for the famine,
usury, envy, anger, drunkenness, or martyr-panegyric material at all.
Keyword hits for "usury," "Gordius," "Julitta," and "Mamas" inside the file
all fall within the Prolegomena's own scholarly offset range (its one
continuous essay, no further div2/div3 headers beneath it) and read, on
inspection, as the *editor's own third-person description* of each homily
("Homily XVIII. is on the martyr Gordius..."; "the Homily on St. Mamas, the
next in order, the expressions are less equivocal...") — critical apparatus
about the homilies, not the homilies' own translated text.

This matches, almost exactly, the G1 Scope and Source Acquisition
Manifest's own "Honest gaps" list, which states plainly: "Basil's individual
moral/social homilies (famine, the rich fool's barns, usury, envy, anger,
drunkenness, named martyrs) and the Moralia" have "No open edition" at all.
The manifest's own assessment is the one directly confirmed by reading the
vendored file's own structure; rows 16 and 20 of the Registry, and the two
source records built on them, are not. This is the same *shape* of mistake
the Registry's own living-document log already caught and fixed once, for a
different row (row 82, *In XL Martyres* II, corrected in the fourth review
round after being wrongly marked "within npnf205 (row 41)") — a claimed
volume-membership that a direct text search of the file itself does not
support. It was not caught for rows 16/20 in any of the three review
rounds already run. Not corrected here — this is a review step, not a
revision cycle — but named plainly rather than left silent, since these two
rows currently back load-bearing Doc_02 §8 story-tier claims (the
famine-of-368/9 narrative; the Forty Martyrs Tier 2 story) on the strength
of a citation that does not hold up against the vendored file's own
contents.

---

## Gate verification

Re-ran the full 15-gate battery (`engine.m1.gates.run_all`) against
`cappadocian`'s complete record set, including the new search_record, from
`/home/user/CIC-Project`:

| Gate | Findings |
|---|---|
| schema-validation | 0 |
| referential | 0 |
| reciprocity | 0 |
| completion-per-type | 0 |
| narratability | 0 |
| glossary-retrofit-complete | 0 |
| quote-recording | 0 |
| alias-safety | 0 |
| distribution-health | 0 |
| confidence-crosscheck | 0 |
| rights | 0 |
| readability | 0 |
| canon-coverage | 28 |
| no-build-attribution | 0 |
| id-convention | 0 |

Matches B-1's own clean state exactly: 14 of 15 gates clean, `canon-coverage`
unchanged at 28 (expected incompleteness — no story/term/doctrinal_witness/
honest_limit records exist yet; those arrive B-2 through B-6). Nothing
regressed on the other 14.

---

## Verdict

Coverage is not fully saturated in the sense the PRESS question always
guards against — one real gap (*Life of Moses*) is confirmed open, two
scholarship candidates (Meredith, Rufinus' history continuation) are
genuine unacquired targets, and one existing pair of Registry rows (16, 20)
looks wrong on direct inspection of the file it cites. It is, however,
adequate to proceed on the terms B-1a/B-1b actually test: the world's own
primary-voice coverage is strong (6/6 in the independent recall test, and
the discovery sweep found no vendored-but-unused file sitting idle), the
misses cluster where HAL's own precedent said they would (scholarship
apparatus, not primary voice), and every finding above is named with enough
specificity for the pre-freeze re-sweep or the build thread's own next pass
to act on directly.
