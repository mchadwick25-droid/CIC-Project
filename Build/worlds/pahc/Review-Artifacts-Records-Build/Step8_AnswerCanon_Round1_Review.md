# Step 8 — Answer Canon — Round 1 Review (cold, adversarial)

**Scope reviewed:** 17 `records/pahc/doctrinal_witness/*.md`, 6 `records/pahc/quote/*.md`,
`Build/worlds/pahc/build/ANSWER-CANON-INDEX.md`, `Build/worlds/pahc/build/generate_answer_canon_index.py`.
Reviewed at commit `40e47c8e`.

---

## Verdict — REVISION REQUIRED (targeted, not structural)

Six SUBSTANTIVE findings, each confined to one or two named fields in six records; the other
seventeen records in the batch verify clean. The mechanical layer is genuinely sound: I re-ran the
full gate battery myself (`engine.m1.gates.run_all` over `load_world_records("pahc")` +
`load_fleet_records()`) — **all thirteen gates return zero findings**; all 28 cells classify
`substantive` or `honest_limit` with no blanks and no double-honest_limit; the index regenerates
byte-identical to the committed file; all nine relation edges touching this batch reciprocate,
verified by hand and not by trusting the gate; all six `license` values are `verbatim` and all four
`speaker_or_author` values resolve to real approved `pahc.figure.*` records. Every one of the six
`quote.text` fields is exact against the vendored primary text, and the two Ignatius quotes are
correctly taken from the **shorter** recension (Trallians 9 verified as the first of the parallel
pair; To Polycarp 5 verified by its "according to God" / "according to the Lord" recension
discriminator, with the ANF's own "as in the longer recension" footnote confirming which column is
which). The `jesus-as-god` decision not to formalize "our God" as a quote record checks out —
"our God" is present in the **shorter** recension of Ephesians (salutation and chs. 7, 18), Romans
(salutation, twice), Smyrnaeans 10, and the To Polycarp 8 closing, so the record's hedge is honest
rather than a cover for a weak claim. Barnabas's registered scope is respected exactly (the only
mentions in the batch are in `reading-scripture`'s body, saying why it is *not* cited).

What fails is content, in participant-facing compiled prose: two verifiable factual errors
(`jesus-as-god`'s "Trinity comes from a council"; `god-and-argument`'s "no council ever met in our
time"), one invented action attributed to a real named outsider (`outsider-view` has Pliny going to
check the meal), one source-locus that does not carry the claim it is cited for plus a use-discipline
breach (`hard-texts` on Marcion), one binding source caveat dropped in three records (the Didache
representativeness limit), and one cross-record contradiction (`scholarly-standing` vs
`how-we-know` on direct apostolic contact). All six are narrow enough to fix in-field without
re-opening any approved record.

---

## SUBSTANTIVE findings

### 1. SUBSTANTIVE — `pahc.witness.jesus-as-god`: "Trinity" is attributed to a council. It is not, and the word is attested inside this world's own window and region.

**File:** `records/pahc/doctrinal_witness/pahc.witness.jesus-as-god.md`
**Fields:** `text` (a compiled field), `confidence.divergence_note`.

The `text` says: *"We do not have a word for what you call the Trinity - that word comes from a
gathering that happened after our own time closed."* The `divergence_note` says the same:
*"the term itself belongs to a council after this world's own close."*

Both are wrong on two counts:

- **No council coined it.** The Nicene creed does not use the word; `trinitas` is Tertullian's
  (c. 213), and Greek τριάς is earlier still.
- **It is attested inside this world's own window and one of its own three regions.** Theophilus of
  Antioch, *To Autolycus* II.15, uses τριάς c. 180 CE — inside 70–200 and inside Antioch/Syria.
  This is not an outside reference-work fact I am importing: it is in **this build's own vendored
  corpus**, and the ANF editor flags it in a footnote on the page.

**What I checked:** grepped the tag-stripped `cic/texts/anf02_hermas-tatian-athenagoras-theophilus-
clement-alexandria.xml` for "Trinity"; the Theophilus passage reads *"are types of the Trinity,
Τριάδος. [The earliest use of this word "Trinity." … he says, illustrating an accepted word, not
introducing a new one.]"*, and the volume's own index carries "Trinity, the, 101. or Triad, 101.
first use of the word, 101." I also confirmed `pahc.core.house-church`'s caution 10 does **not**
make this claim — it lists church councils as out-of-window, but says nothing about the word's
origin. The record invented the council attribution.

The record's *substantive* position is fine and should survive: this world's own six primary voices
never use the word, and developed conciliar Trinitarian doctrine is later. Only the etymology is
wrong.

**Suggested fix:** in `text`, replace *"that word comes from a gathering that happened after our own
time closed"* with something that claims only what is true of *these* voices — e.g. *"none of us
reaches for that word, and none of us works out how calling Jesus God fits together with calling the
Father God."* Mirror the same correction in `divergence_note` (drop "belongs to a council"; keep
"this world's own texts never use the word").

---

### 2. SUBSTANTIVE — `pahc.witness.god-and-argument`: "No council ever met in our time … that belongs to a later world than ours" contradicts this build's own approved anti-Montanist source row.

**File:** `records/pahc/doctrinal_witness/pahc.witness.god-and-argument.md`
**Fields:** `text`, `positions[1]`; aggravated by `retrieval.retrieve_when` ("participant asks about
church councils").

`positions[1]`: *"No council ever gathered in this world's own window to decide a question about God
— **that whole mechanism belongs to a later world.**"* `text`: *"No council ever met in our time to
settle a question like that - **that belongs to a later world than ours.**"*

The narrow claim (no council decided a question about God's nature in-window) is defensible. The
unqualified second clause is not. `records/pahc/source/pahc.source.anti-montanist-fragments.md` —
already approved in this build — says in its own `work` field *"the synodical opposition of Asia
Minor's churches"* and in its body *"the New Prophecy was live, Phrygian, spreading, and **contested
by synods of Asia Minor bishops right at this world's closing edge**."* The conciliar mechanism
therefore exists inside this world's window, in one of its three core regions, on the testimony of a
source this build registered for exactly that purpose.

This matters more than usual because F1-I contains `f1-i-03`, *"What did the councils in your time
decide, and why did it matter so much?"* — and this record is the one routed to answer council
questions. A participant asking that question is currently told the mechanism did not exist.

**What I checked:** read `pahc.source.anti-montanist-fragments` in full; confirmed the underlying
testimony directly in the vendored `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml`
(HE V.16.10: *"the faithful in Asia met often in many places throughout Asia to consider this
matter,"* with McGiffert's note *"That synods should early be held to consider the subject Montanism
is not at all surprising… many such met during these years"*); and read all four F1-I canon questions.
I also confirmed the record is faithfully restating `pahc.core.house-church` caution 10, which lists
"church councils" as an out-of-window trap — so the tension originates upstream. I am **not**
recommending re-opening world_core; caution 10's point (no ecumenical, doctrine-deciding council)
stands. The fix belongs in this record, which turns caution 10 into an unqualified participant-facing
denial.

**Suggested fix:** keep the true claim, drop the absolute. E.g. *"No gathering of ours ever met to
settle a question about God's own nature — that kind of deciding belongs to a later world. Toward the
very end of our time, churches in Asia did meet, often and in many places, over the new prophecy
among them; but that was about whether to receive a movement, not about what God is."* Then add a
`relations` edge to `pahc.contested.rivals-undefeated` (reciprocated), which already holds that
material.

---

### 3. SUBSTANTIVE — `pahc.witness.hard-texts`: the Marcion content is not carried by its cited locus, and it breaches the Tertullian row's own USE DISCIPLINE.

**File:** `records/pahc/doctrinal_witness/pahc.witness.hard-texts.md`
**Fields:** `sources[1].locus`, `positions[1]`, `text`, `confidence.divergence_note`.

**(a) The locus does not carry the claim.** The record cites
`pahc.source.tertullian-adversus-marcionem` at *"1.19 (Marcion's own rejection of the Jewish
scriptures' God as a harsher, different figure)"*, and on that basis asserts in `text` that Marcion
*"found the God of those older writings different enough from the Father that Jesus showed that he
threw out those scriptures entirely and **kept only a shortened Gospel and Paul's own letters**."*

*Adversus Marcionem* I.19 is about the **dating** of Marcion's god (115 years after Tiberius) and the
law/gospel separation. It contains neither the "harsher God" characterization nor anything about a
trimmed Gospel or Pauline corpus. The harsher/evil-Creator characterization is I.2 ("Marcion, Aided
by Cerdon, Teaches a Duality of Gods; How He Constructed This Heresy of an Evil and a Good God");
the canon claim is not in Book I at all.

**What I checked:** read I.19 in full and I.2 in full in the tag-stripped
`cic/texts/anf03_tertullian.xml`; then keyword-scanned the entire span of Book I (indices 1306932–
1434883 of the stripped file) for `Gospel of Luke`, `expunge`, `mutilat`, `curtail`, `Epistles of
Paul`, `apostle Paul` — zero hits for all of them.

**(b) Use-discipline breach.** `pahc.source.tertullian-adversus-marcionem`'s body says the row is
*"Usable for the disclosure obligation … **never as a fair statement of what Marcionites themselves
believed in their own words.**"* `pahc.contested.rivals-undefeated` — the record `hard-texts` is
related to — concedes *"This build cannot recover how Marcion, Valentinian, or Montanist teaching
actually sounded in its own adherents' own words - only through later, hostile paraphrase."* The
`text` field nonetheless states Marcion's own theology and canon flatly, with no hedge that this
reaches us through an opponent writing after this world's close. The trailing body acknowledges the
discipline; the compiled field does not honor it.

**Suggested fix:** two moves, both cheap. (i) Re-locus: cite `pahc.source.irenaeus-adversus-haereses`
at Book I, ch. 27 — verified directly in `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`
(*"declaring Him to be the author of evils, to take delight in war… he mutilates the Gospel which is
according to Luke… he dismembered the Epistles of Paul"*), which carries **both** halves of the
claim, is a registered source, and is licensed by its own USE DISCIPLINE for exactly this
rival-movement disclosure; optionally add Tertullian I.2 alongside. (ii) Add the hostile-witness
hedge into `text` in emic register — e.g. *"what reaches you about him comes from people who wrote
against him, so take it as their account of him, not his own."*

---

### 4. SUBSTANTIVE — `pahc.witness.outsider-view`: an action Pliny never performed, and a phrase attributed to him that is not his translator's wording.

**File:** `records/pahc/doctrinal_witness/pahc.witness.outsider-view.md`
**Fields:** `text`, `tensions[0]`.

`text`: *"He had to **go check** it was, **in his own words**, ordinary and harmless."*
`tensions[0]`: *"a meal **he had to confirm** was harmless."*

Against the vendored text of Pliny 10.96 (McGiffert's note to Eusebius HE III.33, in
`cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml`):

- Pliny **checked nothing** about the meal. The description is what the *lapsed* deponents affirmed
  ("Moreover, they affirmed that this was the sum of their guilt or error; that they had been
  accustomed to come together on a fixed day before daylight…"). The parenthesis "(which is not the
  characteristic of a nefarious superstition)" is a gloss on their report, not the record of an
  inspection. The one investigative act Pliny reports is the interrogation under torture — and it
  concerns "the truth" in general, not the meal.
- "**ordinary and harmless**" is not "in his own words." The vendored English is **"a meal, common
  yet harmless."** The batch's own `pahc.source.pliny-letters` row quotes that phrasing correctly
  three times.

This is the same class of defect the Step 7 round-1 review caught at Finding 6 (Pliny recast as an
eyewitness to a meeting place). The record's own body quotes the passage accurately; the drift is
only in the two participant-facing fields.

**Related, and flagged rather than silently reproduced:** `text`'s *"Part of what he learned, though,
came from two enslaved women he had tortured to get it"* and `tensions`' *"it was extracted partly
from two enslaved women under torture."* Pliny's own text attributes the entire description
(pre-dawn meeting, hymn, oath, meal) to the deponents in the preceding sentence, and reports that the
torture yielded **"nothing except a superstition depraved and immoderate."** This framing is not
invented by this batch — it is inherited verbatim in substance from the approved
`pahc.source.pliny-letters` body (*"The most granular detail was extracted from two enslaved women,
called ministrae, under torture"*), and the fleet's own `f6-e-01` embeds the same reading. I am not
asking Step 8 to fix an approved row unilaterally, but this should get a disposition decision rather
than another pass-through: the vendored text does not support "the most granular detail" coming from
the torture.

**Suggested fix (this record):** *"He wrote down that the meal was, in his words, common and harmless
— nothing worse than that."* And in `tensions`, replace "a meal he had to confirm was harmless" with
"a meal he was satisfied was harmless." Then raise the source-row framing separately.

---

### 5. SUBSTANTIVE — the Didache representativeness limit, declared "binding on every record citing this row," is dropped in three witnesses.

**Files:** `records/pahc/doctrinal_witness/pahc.witness.hard-texts.md`,
`pahc.witness.outside-our-community.md`, `pahc.witness.prayer-and-struggle.md`.

`pahc.source.didache`'s body: *"REPRESENTATIVENESS LIMIT, carried from Doc_02 §1.1 and **binding on
every record citing this row**: this reads as one community's church-order manual (plausibly
Syrian); there is no evidence Rome or Asia Minor knew or used it. **It must not be silently
generalized to network-wide practice.**"* `pahc.core.house-church` caution 5 says the same
("never generalized to network-wide practice").

All three records generalize it to the whole world's practice, in compiled `text` and in `positions`,
with no caveat anywhere in the record:

- `hard-texts` `text`: *"When **we ourselves** taught a new member, though, it usually was not through
  the harder stories at all."* `positions[2]`: *"**new members were most often taught** through the
  Two Ways."*
- `outside-our-community` `text`: *"**the way we taught someone new** was stark: two roads…"*
  `positions[1]`: *"**this world's own catechesis** (the Two Ways)."*
- `prayer-and-struggle` `positions[1]`: *"On forgiveness, **this world's own practice** was communal."*
  `text`: *"**our own practice** was not something worked out alone."*

The batch demonstrably knows the rule: `pahc.witness.scholarly-standing` states the single-manuscript
problem explicitly, and the Step 4 lexicon review confirms `pahc.term.two-ways` and
`pahc.term.prophetes` both carry the "one community's manual" caveat in their senses. So this is
inconsistency within the batch, not a shared misreading.

**What I checked:** read `pahc.source.didache` in full; verified Didache 1:1–2, 9:2, 14:1–3 directly
in `cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` (all wording accurate —
this is a scope finding, not a quote finding); grepped the three records for any representativeness
hedge (none).

**Suggested fix:** one clause per record, in-voice, e.g. *"— at least in the community whose manual
we still have; whether Rome or the churches of Asia taught it this way, we cannot tell you"* — plus a
matching sentence in each record's `tensions[]`. `hard-texts` and `outside-our-community` can also
lean on `pahc.source.barnabas` 18–20, which this build registered *precisely* to license the claim
that the Two Ways schema circulated more widely than one redaction — the one Barnabas claim in scope,
currently unused.

---

### 6. SUBSTANTIVE — `pahc.witness.scholarly-standing` contradicts `pahc.witness.how-we-know` on direct apostolic contact.

**Files:** `records/pahc/doctrinal_witness/pahc.witness.scholarly-standing.md` (`text`) vs
`records/pahc/doctrinal_witness/pahc.witness.how-we-know.md` (`text`, `tensions`,
`confidence.divergence_note`).

`scholarly-standing` `text` closes: *"We read what the apostles wrote alongside **what we still
received directly from them** - no settled edge yet."*

`how-we-know` `tensions`: *"**None** of this world's own primary voices claims direct personal contact
with an eyewitness to Jesus himself - **the chain is always at least one remove.**"* Its `text`:
*"none of us saw him ourselves… they in turn appointed others to carry it forward **when they
themselves were gone**."* And `pahc.core.house-church`'s horizon frames the whole world as *"The
generations **after** the apostles' deaths."*

"Received directly from them" is the one formulation the rest of the batch is at pains to rule out.
Note that the sibling record handling the same substance gets it right:
`pahc.witness.scripture-and-testimony` says *"what could still be received directly from **apostolic
testimony**"* — a chain, not a person.

**Suggested fix:** align with the sibling — *"We read what the apostles wrote alongside the apostolic
testimony still handed on among us — no settled edge yet."*

---

## COSMETIC findings

### 7. COSMETIC — `pahc.quote.justin-reasonable-livers`: an ellipsis marking an elision that does not exist, on a `license: verbatim` record.

The quote reads *"We have been taught that Christ is the first-born of God**...** and we have declared
above…"*. The vendored text (`anf01`, 1 Apol 46) reads *"first-born of God**,** and we have declared
above"* — nothing is omitted. On a verbatim-licensed field, a false ellipsis is a small but real
precision defect; the rest of the quote is exact. **Fix:** restore the comma.

### 8. COSMETIC — `pahc.quote.ignatius-marriage-bishop`: unmarked head-truncation on a `license: verbatim` record.

The vendored shorter recension of To Polycarp 5 reads *"**But it** becomes both men and women…"*; the
quote silently drops "But" and recapitalizes to *"It becomes…"*. Standard editorial practice, but this
record's four siblings all mark their elisions with "…". Recension discipline itself is **correct
and verified** (the "according to God" reading is the shorter column; the longer reads "according to
the Lord"). **Fix:** either restore "But" or add a body note.

### 9. COSMETIC — `pahc.witness.coming-to-belief`: dropped auxiliary inside a quoted phrase.

`positions[0]` quotes *'a flame kindled in my soul'*; the vendored Dialogue 8 reads *"a flame **was**
kindled in my soul."* The partner `pahc.quote.justin-flame-kindled` has it exactly right, so this is a
transcription slip in the summary field, not a misreading. (`positions[]` is not compiled by
`build_prompt()`, which is why this is cosmetic rather than substantive.) **Fix:** restore "was".

### 10. COSMETIC — `pahc.quote.hermas-doubting`: `speaker_or_author` attributes the Shepherd's speech to Hermas, with nothing in the record saying so.

The vendored Mandate 9 opens *"**He says to me**, 'Put away doubting from you…'"* — the speaker is the
Shepherd; Hermas is the one addressed. The partner witness gets this exactly right (*"One of us,
Hermas, was **told** plainly"*), but the quote record says nothing about it, and
`engine/m2/builders.py::build_coverage_json` promotes `speaker_or_author` into a per-cell `figures`
list, so the mis-voicing risk is real downstream. The authorial-voice convention (as used for
`pahc.figure.church-of-rome` on the 1 Clement quote) is defensible; the silence is the problem.
**Fix:** one line in the body, and/or change `locus` to "Mandate 9 (the Shepherd's instruction to
Hermas)".

### 11. COSMETIC — relation edges on the two dating-adjacent witnesses point at the wrong contested_claim.

`pahc.witness.scholarly-standing` declares `associated-with → pahc.contested.martyrdom-polycarp-dating`,
but its content never mentions the Martyrdom of Polycarp; it *does* discuss the Didache's
single-manuscript problem, yet declares no edge to `pahc.contested.didache-dating`. Conversely
`pahc.witness.apostolic-practice` names `pahc.contested.didache-dating` in its `divergence_note` prose
with no relation edge at all. Both reciprocate correctly as written, so no gate fires — this is a
retrieval-graph accuracy point. **Fix:** add `didache-dating` edges (reciprocated) on both; keep or
drop the martyrdom edge on the basis of whether the record will be extended to mention it.

### 12. COSMETIC — `pahc.witness.how-we-know` `divergence_note` shortens a quoted phrase.

The note reads *a 'living voice' testimony (Papias)*; the vendored McGiffert rendering (and the
record's own `tensions` field, which is correct) is *"the living and abiding voice."* **Fix:** match
the `tensions` wording or drop the quotation marks.

### 13. COSMETIC — `generate_answer_canon_index.py` computes only the `empty` case but prints a claim covering both defect cases.

`blank = [c for c in cells if canon.classify_cell(c, recs)["status"] == "empty"]`, and when that list
is empty the index prints *"Every fleet canon cell now has at least one substantive record … **or
exactly one honest_limit**."* A `multiple_honest_limit` cell would satisfy the code's test and make
the printed sentence false. It cannot happen today (F5-E is the only honest_limit cell and it is
singular — verified), and the M1 gate catches it independently, so there is no live risk. **Fix:**
treat any status not in `{"substantive", "honest_limit"}` as a defect in the comprehension. Otherwise
the generator is correct: I diffed a fresh run against the committed file and it is byte-identical,
and its cell computation calls `canon.classify_cell` directly rather than re-deriving the rule.

---

## Verified clean (checked, nothing found — recorded so the next round need not repeat it)

1. **Gate battery.** All 13 gates zero findings, run by hand over the live record set.
2. **All six `quote.text` fields, verbatim against the vendored primary texts.** 1 Clement 42
   (`anf01` ii.ii.xlii, exact including the elided sentence); Hermas Mandate 9 (`anf02` ii.iii.ix —
   each retained clause is contiguous, as the body claims); Ignatius Trallians 9 and To Polycarp 5
   (both shorter recension, discriminators checked); Justin Dialogue 8 (`anf01` viii.iv.viii, exact);
   Justin 1 Apol 46 (exact apart from Finding 7).
3. **Ignatius recension discipline** — no longer-recension material anywhere in the batch.
4. **The `jesus-as-god` no-quote-record decision holds.** "our God" verified in the shorter recension
   of Ephesians (salutation, 7, 18), Romans (salutation ×2), Smyrnaeans 10, To Polycarp 8 closing —
   so "in how he opens his letters, and in how he closes them" is supported, and no stronger hedge is
   needed than the one the record already carries.
5. **Barnabas scope guard** — nothing in the batch cites Barnabas at all, including its typology.
6. **All other quoted material** verified against the vendored texts: 1 Clement 44 ("blamelessly
   served the flock" / "removed some men of excellent behaviour"), 47, 49; Justin 1 Apol 67 ("as long
   as time permits"), 59 ("Plato's obligation to Moses" — the creation-account chapter, exactly as
   claimed); Didache 1:1–2, 9:2, 14:1–2; Hermas Mandate 4 (separation, no remarriage, take her back,
   "man and woman are to be treated exactly in the same way", "there is but one repentance") and
   Similitude 2 (elm/vine, "rich in intercession", "nourishes"); Pliny 10.96 as quoted in the
   `outsider-view` body (exact).
7. **canon_cells accuracy.** Every one of the 23 claims read against the actual `canon_question` text.
   No stretches found — including the one I expected to fail: `outside-our-community`'s divorce
   material under **F6-T** is a genuine match to `f6-t-03` ("What did your people hold about a
   marriage ending…"), not a stray. `outsider-view` answers all three F3-E questions; `reading-scripture`
   all three F2-I; `scholarly-standing` three of four F2-E.
8. **Reused-cell justification.** F1-I, F4-E and F6-I each verified as substantively closed by the
   witness's own content (not merely tagged) — the doctrinal_witness carries participant-facing answer
   material the gravity/force/contested_claim record does not.
9. **Reciprocity, by hand.** All 9 outbound and all 9 inbound edges enumerated and matched
   individually; no one-sided edge.
10. **Voice discipline.** Mechanical scan of all 17 `text` fields for third-person world-description,
    first-person singular, named in-world role labels, ISO dates, "Mark", "ruled", "WORKING SCOPE" —
    zero hits. The only third-person pronouns are legitimate referents (the apostles, the texts).
11. **Schema/licensing.** All 6 licenses `verbatim`; all `speaker_or_author` values resolve to
    approved figure records; `confidence-crosscheck` satisfied on every Documented record.
12. **Coverage.** 28 cells, 0 blank, 1 honest_limit cell (F5-E) claimed by exactly one record — the
    batch's headline claim is true.

---

## Round-2 verification

Performed by this build thread directly (Read/Grep/Bash, plus fk_grade re-checks and a fresh
independent re-verification of the two vendored-corpus grep results the round-1 review's own
Findings 1 and 3 rest on), not re-dispatched as a second agent - the same precaution taken at Steps
4-7: check each fix against live file content, don't trust a fix-list summary.

**All 6 SUBSTANTIVE findings, fixed and verified:**

1. `jesus-as-god` - the false "comes from a council"/"belongs to a council" etymology is removed from
   `text` and `divergence_note`; the record now says only that none of this world's own six primary
   voices reaches for the word, without claiming the word itself is later or conciliar. Grepped the
   live YAML fields directly (not just the trailing body) - zero remaining live occurrences of the
   council claim outside the FIXED-note describing the correction.
2. `god-and-argument` - the unqualified "that whole mechanism belongs to a later world" is now scoped
   to "a question about God's own nature"; added the anti-Montanist synod content (Asia Minor churches
   meeting repeatedly near this world's own close, over the New Prophecy, not over God's nature) to
   `positions`, `text`, and `sources[]`; added a reciprocated relation to `pahc.contested.rivals-
   undefeated`. Confirmed the reciprocal edge exists on both records.
3. `hard-texts` - re-sourced from the wrong locus (Tertullian, Adv. Marc. 1.19, which does not carry
   the "harsher God"/trimmed-canon claims) to Irenaeus, Adv. Haer. I.27, verified directly against the
   vendored text myself (confirmed both the "author of evils... contrary to Himself" and "mutilates the
   Gospel... dismembered the Epistles of Paul" phrases are present verbatim at that locus). Added the
   hostile-witness hedge inline in `positions`, `tensions`, and `text` ("what reaches you about him
   comes from his opponents, not from him"), not only in the trailing body as before. Also folded in
   the Didache representativeness fix (see #5).
4. `outsider-view` - corrected the invented "he had to go check" action and the misattributed "in his
   own words, ordinary and harmless" phrase (the vendored English is "common yet harmless," and the
   whole description is what Pliny's deponents affirmed to him, not what he personally verified).
   Reworded `positions`, `tensions`, and `text` to attribute the description to testimony Pliny
   recorded, not inspection he performed. The round-1 reviewer's separate, out-of-scope concern about
   the already-approved `pahc.source.pliny-letters` row's own "most granular detail... under torture"
   framing is flagged in this record's own trailing body as a question for the Step 10 final summary,
   not resolved unilaterally.
5. Didache representativeness limit - added a hedge clause (verified present in `positions`, `tensions`,
   and `text`) to all three records the review named: `hard-texts` ("at least one of our own
   communities... we cannot promise you every household"), `outside-our-community` ("at least one of
   our own communities... we do not know how far that teaching reached"), and `prayer-and-struggle`
   ("in at least one of our own communities... we do not know how far this specific practice
   reached").
6. `scholarly-standing` vs `how-we-know` - "what we still received directly from them [the apostles]"
   replaced with "the apostolic testimony still handed on among us," matching the sibling record
   `scripture-and-testimony`'s own correct phrasing (a chain, not a person). Re-read both `how-we-know`
   and `scholarly-standing` side by side to confirm no remaining contradiction.

**All 7 COSMETIC findings, fixed and verified:**
- 7: `justin-reasonable-livers` - false ellipsis restored to the vendored comma ("first-born of God,
  and we have declared").
- 8: `ignatius-marriage-bishop` - restored the sentence-initial "But" silently dropped from To Polycarp
  5's shorter recension.
- 9: `coming-to-belief` `positions[0]` - restored "was" ("a flame was kindled in my soul").
- 10: `hermas-doubting` - `speaker_or_author` corrected from Hermas (who is addressed) to a descriptive
  string identifying the Shepherd (who speaks) as the actual voice, since no separate Shepherd figure
  record exists to cite; `locus` updated to say so explicitly.
- 11: relation edges retargeted - `scholarly-standing` and `apostolic-practice` now both point to
  `pahc.contested.didache-dating` (their actual content) rather than `martyrdom-polycarp-dating` (which
  neither discusses); all four resulting edges verified reciprocated by hand.
- 12: `how-we-know`'s `divergence_note` "living voice" corrected to "living and abiding voice," matching
  the record's own (already-correct) `tensions` field and the vendored Papias wording.
- 13: `generate_answer_canon_index.py`'s coverage check broadened from an `if blank` test to a
  `classify_cell` status check covering all three possible statuses, so a future `multiple_honest_limit`
  cell (a real gate-level defect) can no longer be silently reported as "every cell covered."

**Additional self-caught fix during verification:** two records (`hard-texts`, `god-and-argument`) grew
past FK grade 10 as a side effect of the fixes above (10.3 each) - not gate-enforced for
`doctrinal_witness.text`, but inconsistent with this build's own practice of keeping every
participant-facing text field under the same FK-10 ceiling used elsewhere. Trimmed both to shorter
sentences (10.3 -> 8.5 and 10.3 -> 7.8 respectively) without changing content.

**Regression checks:**
- Full YAML parse sweep: all 105 pahc record files parse cleanly, including an id/filename match check.
- Full gate battery: clean on all 13 gates, including canon-coverage (0 blank cells, unchanged from
  before this fix pass) - no regressions.
- Regenerated `ANSWER-CANON-INDEX.md`; diffed against the pre-fix version - only the content changes
  from the fixes above and the new defect-check line, no drift.

**Verdict: All 6 SUBSTANTIVE and all 7 COSMETIC findings LANDED CORRECTLY, confirmed against live file
content (including a fresh independent re-verification of the two vendored-text loci the review's own
findings rested on) and a clean re-run of the full gate battery. Step 8 ready for disposition.**
