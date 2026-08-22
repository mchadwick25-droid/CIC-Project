# Step 11 — Representative Voice Build (voice_craft + demonstrations) — Round 1 Review (cold, adversarial)

**Scope reviewed:** `records/pahc/voice_craft/pahc.craft.chloe-voice.md`, all 9
`records/pahc/demonstration/pahc.demo.*.md`, `world-build-docs/pahc/VOICE-INDEX.md`, and
`world-build-docs/pahc/generate_voice_index.py`. Checked against `Redesign-Spec/CiC-Program-Spec.md`
(O0–O9, the seven register statements at O2, §4.2 Appendix A, §4.3 step 5, §5), 
`Redesign-Spec/Artifact-1-Record-Schema.md` (§2–§6), `engine/m1/schemas.py`, `engine/m1/gates.py`,
`engine/m1/canon.py`, the two fixture exemplars (`records/fix/voice_craft/fix.craft.vera-voice.md`,
`records/fix/demonstration/fix.demo.core-testimony.md`,
`records/fix/demonstration/fix.demo.identity-collision.md`), the approved
`World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Representative_Identity_Preliminary_Decision.md`,
the superseded `CiC_W1_Representative_Permanent_Prompt_Chloe.txt`, the already-approved pahc record
canon, and the vendored primary texts under `cic/texts/` (ANF vols. 1, 2, 7 — tag-stripped and
grepped directly, never trusted from the records' own citation notes). Reviewed at working tree on
top of commit `f6d23bf6` (the twelve voice-layer files are staged, uncommitted).

---

## Verdict — MINOR FIXES NEEDED — 13 SUBSTANTIVE, 6 COSMETIC

Nothing here is structurally wrong and nothing needs rebuilding: the required set is complete and
correctly shaped, the register discipline is real and mostly excellent, and the single most
important instruction of this build step — **Chloe is a representative voice for the entire
movement, not a character** — is honored without a single lapse. I checked that mechanically, not
by impression: I extracted every `representative` turn from all nine demonstrations and regexed for
first-person-singular pronouns (`I`, `my`, `me`, `mine`, `myself`) as the Representative's own
narration. **Zero hits in nine turns.** Every one of them speaks in "we / our / among us," and where
an individual's biography is unavoidable it is correctly held at third-person remove and named
("Justin says he had gone looking…", "One of us, Ignatius, calls…"). That was the highest-risk
failure mode of this step, and it did not happen.

The gate battery is genuinely clean — I re-ran `engine.m1.gates.run_all` over
`load_world_records("pahc")` + `load_fleet_records()` myself: **all thirteen gates return zero
findings**, and `VOICE-INDEX.md` regenerates byte-identical to the committed file. But the gates
check structure, and the defects in this batch are all in the two places gates cannot reach:
whether a spoken sentence is true against the source, and whether a spoken sentence stays inside the
scope its own underlying record declared.

**Two findings are fabrication-class (O3, "the voice never invents a source, saying, scene, or
attribution… under every pressure") and should block sign-off on this step until corrected.**
Finding 1 puts into the Representative's mouth, in a *required* identity-collision demonstration, a
claim about Hermas *Vision* 2.4.3 that the vendored text does not support and that this world's own
already-approved `pahc.story.hermas-visions` record explicitly gets right. Finding 2 is the same
misreading in the compiled `voice_craft.identity` field — and it traces upstream to the approved
project-lead Identity Decision document, so it needs escalation, not a silent edit.

The rest divides into: two groundedness/scope overclaims in the CENTER demonstrations, one
unsupported historical claim imported almost verbatim from the *fixture* world, one source-conditions
elision, one unanswered ask, one mis-tagged canon cell, one stale registry entry that now
contradicts the delivered artifact, one readability outlier, one absolute claim that drops its own
record's qualification, and one generated "required-set check" that cannot report a shortfall.

---

## SUBSTANTIVE findings

### 1. `pahc.demo.identity-collision-womens-authority` — Grapte is not entrusted to carry the text onward; the vendored source gives that to Clement, and this world's own approved story record says so

**File:** `records/pahc/demonstration/pahc.demo.identity-collision-womens-authority.md`, `exchange[representative]`.

The turn reads:

> "Among us, real authority most clearly opened in the household - who taught the newcomers, who
> cared for the widows and orphans, **who was entrusted to carry a letter on to another city.** One
> of our own texts names a woman, Grapte, given exactly that: instruction over the widows and
> orphans, **and a text entrusted to her to carry onward.**"

**What I checked:** Hermas, *Vision* 2.4.3 in
`cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` (tag-stripped, div1 ii)
reads in full:

> "You will write therefore two books, and you will send the one to Clemens and the other to Grapte.
> And Clemens will send his to foreign countries, for permission has been granted to him to do so.
> … And Grapte will admonish the widows and the orphans. But you will read the words in this city,
> along with the presbyters who preside over the Church."

The passage assigns three distinct functions to three people. Grapte receives a copy and
**admonishes the widows and orphans, in the city**. The cross-community sending is **Clement's**,
and the text says so with an explicit warrant clause ("for permission has been granted to *him* to
do so") that exists precisely to mark it as his and not another's. Nothing entrusts Grapte with
carrying anything onward.

This world's own already-approved record gets it right. `records/pahc/story/pahc.story.hermas-visions.md`,
`text` field: *"Hermas names Clement by name, instructed to send copies of the visions on to other
cities, and Grapte, instructed to admonish the widows and orphans…"* The demonstration therefore
does not merely overstate a source — **it contradicts a gate-clean pahc record already in the
corpus.**

This is the worst possible place for it to happen. This is one of the three spec-mandated
identity-collision demonstrations (§4.3 step 5c: "the identity-collision cells with the spoken
non-judgment line"), the question is specifically about women's authority, and Grapte is — per the
approved Identity Decision — "the single most specific, named, function-bearing textual peg for a
woman's authority anywhere in this world's own six-primary-voice corpus." The one load-bearing datum
is overstated in the direction that flatters the build's own identity choice. The demonstration's
own `sources[].locus` repeats the error in metadata: *"Vision 2.4.3 (Grapte, instructing widows and
orphans, entrusted with carrying the text on to other cities)"*, as does its `divergence_note`
("Hermas names Grapte with a specific instructional **and cross-community transmission** function").

**Fix:** in the spoken turn, cut "who was entrusted to carry a letter on to another city" from the
opening list (or attribute it correctly and separately), and replace "and a text entrusted to her to
carry onward" with what the text actually says — e.g. *"…a copy of one of our own books put into her
hands, and the charge to admonish the widows and orphans with it."* If the build wants the
transmission theme, it must be voiced as Clement's, named as his. Correct the `locus` string and the
`divergence_note` to match. Nothing else in the turn needs to move.

### 2. `pahc.craft.chloe-voice` — the same misreading is baked into the compiled `identity` field, and it originates upstream in the approved Identity Decision

**File:** `records/pahc/voice_craft/pahc.craft.chloe-voice.md`, `identity`.

> "Chloe, a household leader whose documented function combines with a Grapte-type
> pastoral-instructional and cross-community transmission role (Hermas, Vision 2.4.3 - **instruction
> for widows and orphans, and carrying a text on to other cities**)."

`identity` is one of the two `voice_craft` fields `_ATTRIBUTION_FIELDS` in `engine/m1/gates.py`
names as compiled into the live prompt — this sentence is what a live model reads as its own
self-description on every turn. Per finding 1, the parenthetical's second half is wrong against the
vendored text.

**This one is not the drafter's invention.** `CiC_W1_Representative_Identity_Preliminary_Decision.md`
— the document the project lead signed off, and which the review brief correctly says must not be
re-litigated — states it in exactly these terms: *"a defined instructional role over widows and
orphans, plus an explicit cross-community distribution/transmission function (sending the text on to
other cities)."* The craft record is faithfully consistent with the approved decision. The approved
decision is wrong against Hermas.

So this is an escalation, not an edit-and-move-on. I am flagging it rather than proposing a silent
rewrite, because the "cross-community transmission" half is one of the two stated reasons the
combined role was selected over the plain household-host option (*"This gives genuine 'many people,
many situations' reach without any invented biography"*), and removing it touches the rationale the
lead approved.

**Fix (recommended, for the lead's ruling):** the role label survives intact — a household leader's
reach is grounded independently in `pahc.core.house-church`'s own formation logic and does not need
Grapte to carry letters. Rewrite the parenthetical to what *Vision* 2.4.3 actually gives
("instruction of the widows and orphans, and a text of the community's own put into her hands"), and
correct the Identity Decision document's paragraph with a dated note rather than overwriting it.
**Do not** simply delete the Grapte peg: it is real and it is the right peg, just narrower than the
decision document claims.

### 3. `pahc.demo.center-who-was-jesus` — "He truly ate and drank **among us**" is not in the source and reads as an eyewitness claim the sibling demonstration explicitly denies

**File:** `records/pahc/demonstration/pahc.demo.center-who-was-jesus.md`, `exchange[representative]`.

**What I checked:** Ignatius, *Trallians* 9 (shorter recension) in
`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml` reads: *"…Jesus Christ, who was descended
from David, and was also of Mary; **who was truly born, and did eat and drink.** He was truly
persecuted under Pontius Pilate; He was truly crucified, and [truly] died… He was also truly raised
from the dead, His Father quickening Him, even as after the same manner His Father will so raise up
us who believe in Him."* Every other clause of the demonstration's chain matches this almost word for
word. "Among us" is the one addition, and it is not in the text.

In a first-person-*singular* character voice this would be a small liberty. In this Representative it
is not: the craft record defines "we / our / **among us**" as the whole surviving community of
c. 70–200 CE, and `pahc.demo.center-how-we-know` — sitting three files away in the same batch,
compiled into the same voice layer — opens with **"None of us saw him ourselves."** Two demonstrations
in the same nine-record set contradict each other on the single most fabrication-sensitive point in
this world. A live model reading both as register exemplars has been taught that the collective "we"
can reach back to the table with Jesus.

Inherited: `pahc.witness.who-was-jesus`'s own `text` field carries the same phrase. The fix belongs in
both records.

**Fix:** drop the two words — "He truly ate and drank." The sentence loses nothing and the collision
disappears.

### 4. `pahc.demo.center-who-was-jesus` — Ignatius's Strand-A anti-docetic polemic is voiced as the movement's collective confession, unattributed, against the record's own scope and the craft record's own flavor note

**File:** same file, `exchange[representative]`.

> "**We say** he was truly born, of Mary, from the line of David. **He truly ate and drank…** He was
> truly brought before Pilate, truly nailed to the cross, and truly died - not in appearance only,
> the way some among our own neighbors claimed."

The demonstration's own `divergence_note`, copied from `pahc.witness.who-was-jesus`, says the
opposite of what the turn does: *"the emphatic, repeated 'truly' language is **Strand A's own
polemical register (Ignatius, arguing against docetic teaching) rather than a formula shared
network-wide** - Strand B (1 Clement, the Didache) states the same substance without that same
intensity."* `pahc.core.house-church` caution 1 (THE IGNATIUS CONCENTRATION) requires that
Ignatius-dependent content be "never presented as settled if pressed"; caution 2 (STRAND DISCIPLINE)
requires the two-strand distinction be kept visible.

Most tellingly, this turn violates the craft record's own `correspondence/letter-as-proof` flavor
note, written in this same batch: *"never repeats something another household said **without naming
whose word it was**."* The turn repeats Antioch's word as everyone's word and names no one. Its
sibling `pahc.demo.center-jesus-as-god` — same corpus, same speaker — does it correctly: *"One of
us, Ignatius, calls Jesus Christ our God again and again."*

This is the C-I demonstration: the first cell the spec says a world must demonstrate ("center cells
first") and the first cell admission tests. It is teaching the voice the wrong habit at the most
visible point.

**Fix:** name the source the way the C-T demonstration does — e.g. *"One of us, Ignatius, writing
against people who said Jesus only seemed to be a man, put it as hard as it can be put: truly born,
of Mary, from the line of David…"* — and keep the closing Didache thanksgiving as the cross-strand
counterweight it already is.

### 5. `pahc.demo.identity-collision-someone-like-me` — "We did not sort people by what they carried in" is supported by no pahc record, sits against the Two Ways records, and is lifted in shape and wording from the *fixture* world

**File:** `records/pahc/demonstration/pahc.demo.identity-collision-someone-like-me.md`, `exchange[representative]`.

> "**We did not sort people by what they carried in before they reached our door. We asked what they
> carried after the water** - the life they chose to walk, not the life they had walked before it.
> Before baptism, we taught the Two Ways…"

Three problems, compounding.

**(a) No record supports it.** The demonstration's own body cites `pahc.term.two-ways` and
`pahc.story.two-ways-catechumen`. I read both in full. Neither says anything about *not* examining a
person's prior life. What they actually record is the opposite emphasis: the Two Ways is a
pre-baptismal moral inventory naming specific prohibitions — `pahc.story.two-ways-catechumen`
enumerates them ("not to commit murder, adultery, pederasty, or fornication; not to steal, practice
magic or witchcraft, or murder a child by abortion; not to swear falsely or bear false witness") and
was restored into that record at Step 9 review precisely because dropping them was judged a defect.
The turn's first sentence and its own third sentence pull against each other.

**(b) It contradicts the term record it cites.** `pahc.term.two-ways`, personal sense: *"walking the
way of life is kept, daily, **after the water as before it**."* The demonstration's "the life they
chose to walk, not the life they had walked before it" inverts exactly that.

**(c) It is the fixture world's line.** `records/fix/demonstration/fix.demo.identity-collision.md`
reads: *"We did not ask what a person had been before the water. We asked only what they carried
after it. **It is not our role to weigh what you are** - only to tell you honestly what we held, and
let you judge for yourself what it means for you."* The pahc turn is that paragraph with synonyms
swapped: *"We did not sort people by what they carried in… We asked what they carried after the
water… **It is not our place to judge what you are** - … and let you weigh what it means for you."*
"What they carried after the water" is verbatim. Spec §5.4 makes near-zero cross-world phrase
overlap a quality criterion, and the fixture is a *synthetic* world with two invented sources — it is
the last place pahc content should come from. The fleet non-judgment line is meant to be rendered in
each world's own idiom (§4.2); rendering it in the fixture's idiom defeats the point.

There is also a register-statement-6 exposure here: "the life they chose to walk, not the life they
had walked before it" is a coined, chiastic, quotable line the tradition did not write.

**Fix:** ground the opening in what this world's records actually hold. The Two Ways *is* the answer
to "what would your people have made of someone like me" — a road laid open, taught before the water,
kept daily after it — and the honest limit is that the record cannot say how any particular person
would have been received. Something like: *"What our own teaching put before a person was a choice,
not a verdict. Before baptism we taught the Two Ways: a way of life and a way of death, laid open as
a real choice. What that teaching asked of anyone, it asked of everyone. We cannot tell you how any
one of our households would have met you at the door — nothing in our record answers that."* Then the
non-judgment line in words that are not the fixture's.

### 6. `pahc.demo.lament-suffering` — "our own record does not shame him for it" overstates what the *Martyrdom of Polycarp* actually does with Quintus

**File:** `records/pahc/demonstration/pahc.demo.lament-suffering.md`, `exchange[representative]`.

> "one of our own people once offered himself up for this and then, under real threat, turned back -
> and **our own record does not shame him for it**, or hold up the wanting-to-die itself as the thing
> to imitate."

**What I checked:** *Martyrdom of Polycarp* 4 in `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`
reads, in the vendored edition, under the chapter heading **"Quintus the apostate"**:

> "Now one named Quintus, a Phrygian, who was but lately come from Phrygia, when he saw the wild
> beasts, **became afraid**. This was the man who forced himself and some others to come forward
> voluntarily [for trial]. Him the proconsul, after many entreaties, persuaded to swear and to offer
> sacrifice. Wherefore, brethren, **we do not commend those who give themselves up** [to suffering],
> seeing the Gospel does not teach so to do."

The second half of the demonstration's claim is exactly right and well made — the text's stated moral
is against *volunteering*, not against *recanting*, and that is the distinction the lament needs. The
first half is not. The vendored edition labels him an apostate in its own chapter heading and records
that he "became afraid"; that is not a text withholding shame. And the underlying record does not
make the claim either: `pahc.gravity.martyrdom-meaning`'s `manifestations[]` says only *"the
community's own caution against 'those who give themselves up' (Martyrdom of Polycarp 4)"*, and its
trailing body says only *"the community that produced this text explicitly did NOT commend those who
volunteered for suffering."* The "does not shame him" clause is added at this step.

**Fix:** cut the clause and let the sourced half carry it — e.g. *"…and then, under real threat,
turned back. What our own record draws from that is not what you might expect: it says plainly that
we do not commend those who give themselves up. Wanting to die was never the thing we held up to
imitate."* That is stronger, and it is what the text says.

### 7. `pahc.demo.lament-suffering` — `canon_cells: [F6-E]` contradicts its own `canon_question_id`, which is the F6-**P** suffering question

**File:** same file, front matter.

```
canon_cells:
- F6-E
canon_question_id: _fleet.canon.f6-p-02
```

`_fleet.canon.f6-p-02` carries `cell: F6-P` ("Why does God allow suffering like this? Where was he
when it happened to your people — and to mine?"). I cross-checked all nine demonstrations
programmatically: **eight match their canon question's cell exactly; this is the only mismatch.**
Artifact-1 §3 makes `canon_cells` the coverage map living on the record, so this is wrong data, not a
label. It is also the *one required lament exchange* (§4.3 step 5c), whose whole point is the
personal register — filed under evidential.

**Diagnosis worth recording:** this record's entire `confidence` block, including its
`divergence_note`, is copied verbatim from `pahc.gravity.martyrdom-meaning` (whose `canon_cells` is
`[F6-E]`) with only "this record" changed to "this demonstration". The wrong cell rode along with the
copy. `engine/m1/canon.py` does not count `demonstration` as a substantive type, so the
canon-coverage gate cannot see this — it is invisible to the whole battery.

**Fix:** `canon_cells: [F6-P]`. See also cosmetic finding A on the copied `divergence_note`.

### 8. `pahc.demo.center-coming-to-belief` — Justin's three conditions are reduced to one, and the added gloss inverts the one that was dropped

**File:** `records/pahc/demonstration/pahc.demo.center-coming-to-belief.md`, `exchange[representative]`.

> "He says **anyone with real concern for their own life can come to know it, not only those already
> sure.**"

**What I checked:** *Dialogue with Trypho* 8 in `cic/texts/anf01_…xml` reads: *"**If, then, you have
any concern for yourself, and if you are eagerly looking for salvation, and if you believe in God**,
you may — since you are not indifferent to the matter — become acquainted with the Christ of God,
and, after being initiated, live a happy life."*

Justin states three conditions joined by "and". The demonstration keeps the first, drops the second
and third, and then adds "not only those already sure" — a gloss that specifically negates the third
("if you believe in God"). The record's own trailing body quotes the full conditional, so the
elision is visible in the same file.

This matters more here than it would anywhere else in the batch, because this is the C-P
demonstration answering *"I want to believe in Jesus, but I can't."* The turn's rhetorical arc lands
on a reassurance Justin did not offer to someone in the participant's position. Everything else about
this demonstration is strong — the "flame kindled in his soul" attribution is exact and correctly
flagged as Justin's own phrase, the third-person handling is clean, and the closing
representativeness caveat is honest and well placed.

Inherited: `pahc.witness.coming-to-belief`'s `positions[]` and `text` carry the same gloss.

**Fix:** either restore the conditions in plain English (*"He said it was open to anyone who cared
what became of them, who was actually looking, and who already believed there was a God"*) or drop
"not only those already sure" and stop at the first condition. The current form should not stand.

### 9. `pahc.demo.identity-collision-divorce` — the "belong" half of the canon question is never answered

**File:** `records/pahc/demonstration/pahc.demo.identity-collision-divorce.md`, `exchange`.

The canon question (`_fleet.canon.f6-t-03`) asks two things: *"What did your people hold about a
marriage ending — **could someone divorced belong**, or marry again?"* Register statement 1 is
explicit that this is mechanical and non-negotiable: "The first sentence answers the first ask — **and
every ask gets answered**", and §5.1 lists ask-coverage as a mechanical check.

The turn answers the marriage-ending question and the remarriage question fully and accurately
(verified: Hermas, *Mandate* 4.1 in `cic/texts/anf02_…xml` gives separation, the bar on remarriage,
the duty to take a repentant wife back, "in this matter man and woman are to be treated exactly in
the same way", and "there is but one repentance to the servants of God" — the demonstration is
faithful on every point, including the reciprocity and the limit). It never touches **belonging**. A
participant asking whether a divorced person could still be part of the community leaves without an
answer, and the demonstration teaches the voice that a two-part question can be answered in one part.

**Fix:** add one sentence on belonging, or state plainly that the record does not answer it. Hermas's
own framing — separation with both parties remaining under the community's discipline and open to
repentance — supports a real answer; if the build judges it too thin, "our own texts do not say what
became of such a person's place among us" is the honest form and is itself in-register.

### 10. `records/worlds.yaml` — the ONE registry still says Chloe is not carried forward, and now contradicts the artifact this step delivered

**File:** `records/worlds.yaml`, the `pahc:` block.

```yaml
    # representative: DELIBERATELY UNSET - the name and role are step 5a's deliverable
    # (Mark's per-world touchpoint, spec SS4.3); this build stops before the voice build.
    # The prior-framework build's persona ("Chloe") is NOT carried forward - identity
    # emergence re-runs from the new-regime records when step 5 begins.
```

Step 5 has now happened, the identity was confirmed with the project lead, and
`pahc.craft.chloe-voice` exists. The registry comment is not merely stale — it asserts the opposite
of what shipped. Artifact-1 §2 puts `representative: {name: …, role_label: …}` **in the registry**
and calls the registry the one place world facts live ("no world identifier may appear anywhere else
in code or config"); §6 has the doorway world card render the Representative's name and portrait
from the package. `fix` carries `representative: {name: Vera, role_label: Witness}` correctly. pahc
now has a Representative whose name exists only inside a `voice_craft` record.

**Fix:** set `representative: {name: Chloe, role_label: <the approved role label>}` and delete the
superseded comment. The role label should be settled explicitly — the Identity Decision's own prose
is "A household leader (patroness/host of a house-church gathering) whose documented function
combines with a Grapte-type pastoral-instructional and cross-community transmission role", which is a
rationale, not a label; `role_label` needs a short participant-facing form (the fixture's is one
word). This is a lead-facing decision, not a drafter's.

### 11. `pahc.demo.identity-collision-womens-authority` — the closing sentence is ungrammatical and the turn is the only one in the batch above the readability floor

**File:** same file as finding 1, `exchange[representative]`, final sentence.

> "It is not our place to weigh what standing you would deserve among us today - only to tell you
> honestly what we held, and that it came, for the women who held it, **alongside a real cost most of
> it was never written down.**"

The final clause has no relative pronoun and does not parse: "a real cost most of it was never
written down". It should read "a real cost, most of which was never written down."

I measured Flesch-Kincaid grade on all nine `representative` turns using `engine/m1/fk.py` (the same
implementation the readability gate uses):

```
 6.5  center-coming-to-belief          7.7  identity-collision-divorce
 7.3  center-how-we-know               6.5  identity-collision-someone-like-me
 5.4  center-jesus-as-god             12.9  identity-collision-womens-authority   <-- outlier
 6.0  center-who-was-jesus             9.6  lament-suffering
 5.7  honest-limit-material-remains
```

Eight of nine sit comfortably under the ≤ FK 10 plain-answer floor (§5.1); several are excellent.
This one is 12.9, driven by a 45-word closing sentence and a 33-word opening sentence — both stacking
three or four ideas, against register statement 3 ("one idea per sentence"). `gate_readability` does
not scan demonstration text, so nothing catches it. Spec §5's closing paragraph is the governing
principle: "everything the voice reads is pre-tested for plainness; a voice speaks the register of
its material and its examples."

**Fix:** fix the grammar, and split both long sentences. The content is fine; the packing is not.

### 12. `pahc.demo.center-jesus-as-god` — "None of us reaches for the word Trinity" drops the qualification its own source record carries

**File:** `records/pahc/demonstration/pahc.demo.center-jesus-as-god.md`, `exchange[representative]`.

The underlying `pahc.witness.jesus-as-god` states the claim carefully in its `tensions` field: *"not
because the word did not exist anywhere yet (**a related Greek word is attested elsewhere in this
same period**, just not in any of this world's own six primary voices)"* — and its trailing body is
sharper still, recording that this exact overclaim was *already corrected once* at Step 8 review, and
naming why: *"the Greek 'trias' is attested earlier still, **including in this same build's own
vendored corpus — Theophilus of Antioch, To Autolycus II.15, c. 180 CE, inside this world's own window
and inside Antioch/Syria, one of its three core regions.**"*

The demonstration keeps the absolute ("None of us reaches for the word Trinity") and drops the
qualification. In the witness record the "us" is explicitly scoped ("this world's own six primary
voices"). In the demonstration, "us" is whatever the craft record says it is — and the craft record's
`identity` defines it as *"this world's own whole surviving community… formed across Antioch, the
cities of Asia Minor, and Rome."* Under that definition the sentence is false, in the world's own
window and one of its own three named regions.

This is exactly the criterion-10 failure mode: the demonstration asserts more than the underlying
record permits, and it re-opens a claim a prior review already closed.

**Fix:** scope it in the voice — *"None of the voices we have left reaches for that word"* or *"Not
one of the six of us whose writing survives reaches for it"* — which is true, is still a strong plain
answer, and costs the turn nothing. Inherited: `pahc.witness.jesus-as-god`'s `text` field has the
same absolute and should be scoped in the same move.

### 13. `generate_voice_index.py` — the "Required-set check" cannot report a shortfall, and finds two of its four rows by filename substring

**File:** `world-build-docs/pahc/generate_voice_index.py`.

Three defects in one small script:

1. `REQUIRED_SET` is defined at module top (`{"Center cells (C-I, C-E, C-P, C-T)": [...],
   "Identity-collision (F6-P x2, F6-T x1)": [...]}`) and **never referenced anywhere in the file**.
   Nothing compares the observed set against it.
2. The section titled "Required-set check" therefore does not check. It reports counts and lists. If
   a center cell went missing, or there were one identity-collision demonstration instead of three,
   or the F6-P×2 / F6-T×1 split were wrong, the index would render without a word of complaint. Spec
   principle 12: "A gate that never fails is checking nothing — inertness is itself a reported
   failure." This is a build-doc generator rather than a gate, but it is the only artifact standing
   between this step and step 6, and it is inert in exactly the way the principle names.
3. Two of the four rows are derived from record **ids**, not record **data**:
   `honest_limit_voice = sorted(k for k in demos if "honest-limit" in k or "limit" in k)` and
   `lament = sorted(k for k in demos if "lament" in k)`. Renaming a file silently empties a required
   row. The identity-collision row does it correctly, off `tags`. `pahc.demo.lament-suffering` and
   `pahc.demo.honest-limit-material-remains` carry no `tags` at all, which is why the substring hack
   was needed. This is the "hand-synced list" shape principle 4 exists to forbid.

**Fix:** add `tags: [lament]` and `tags: [honest-limit]` to the two demonstrations and select on
tags; then actually use `REQUIRED_SET` — compare, and emit a visible `MISSING:` line (and a non-zero
exit) when the observed set falls short. As it stands the index's most important section is
decoration.

---

## COSMETIC findings

### A. Two demonstrations carry a `divergence_note` copied from another record, describing material they do not use

`pahc.demo.lament-suffering`'s note is `pahc.gravity.martyrdom-meaning`'s verbatim with "this record"
→ "this demonstration" (and brought the wrong `canon_cells` with it — finding 7).
`pahc.demo.identity-collision-divorce`'s note is `pahc.witness.outside-our-community`'s, and spends
its first clause on *"Justin makes a specific inclusive argument about reasonable pagans, and… the
Didache's Two Ways schema is exclusively either/or"* — neither of which this divorce demonstration
touches. It then says so itself ("this demonstration answers only the divorce/remarriage question
asked"), which is a tell that the note was pasted and patched rather than written. `divergence_note`
is supposed to explain *this* record's own confidence gap.

**Fix:** write each note to the record it sits on. The divorce one should be about Hermas *Mandate*
4's single-text, single-community scope.

### B. `voice_craft.guard` is FK 14.1, with one 65-word sentence

The guard is compiled into the prompt on every turn (it is in `_ATTRIBUTION_FIELDS` for
`voice_craft`). Its third sentence runs 65 words. §5's closing principle — "a voice speaks the
register of its material" — applies to the guard more than to anything else in the record set, since
the model reads it every single turn. The content is right and should be kept; it needs to be three
sentences instead of one.

### C. `voice_craft.guard` scopes the Ignatius dependency wider than the gravity record does

> "our strongest claims about who led and what a death for the name meant among us often rest on a
> single voice, Ignatius"

`pahc.gravity.authority-consolidation`'s trailing body is precise: *"THE IGNATIUS VULNERABILITY: this
gravity's **Strand A content** rests on Ignatius as Asia Minor's only evidentiary voice."* Rome's
plural-presbyter pattern rests on 1 Clement and Hermas — genuinely independent witnesses — and that
independence is the whole basis of the craft record's own `unresolved-authority` flavor note. As
written the guard quietly undercuts the flavor note two fields above it. The "often" softens it but
does not fix it.

**Fix:** "our strongest claims about a single overseer, and about what a death for the name meant,
often rest on a single voice…"

### D. `voice_craft.identity` omits the persona-provenance note the fixture exemplar carries

`fix.craft.vera-voice`'s `identity` ends: *"name and role are the only sanctioned fabrications (spec
principle 14)."* pahc's does not. Spec principle 14 and §6 both make persona provenance a standing
disclosure ("the name is ours; every quote and claim is theirs"). It may be that the doorway carries
this from the registry rather than from the craft record — but the registry entry does not exist yet
(finding 10), so at present nothing in pahc's package states it anywhere. Worth a deliberate ruling
rather than an omission.

### E. `pahc.demo.center-how-we-know` asserts the Papias claim without Papias in `sources[]`

> "Even in our own time, **that chain was already felt as something thinning**, not something we
> could simply rely on."

The only evidence for this in the whole pahc corpus is the Papias "living and abiding voice"
fragment, preserved via Eusebius *HE* III.39 (`pahc.figure.papias`, sourced to
`pahc.source.eusebius-historia-ecclesiastica`). The demonstration's `divergence_note` names Papias;
its `sources[]` lists only 1 Clement 42 and Justin *1 Apol.* 67. A compiled turn should cite what it
actually leans on.

There is also a second-order question worth a note for the lead, not a finding: Papias, on Eusebius's
report, describes seeking out those who had followed the elders and names Aristion and the presbyter
John as "disciples of the Lord" still speaking in his own day. The spoken absolute "**none of us**
claims to have known an eyewitness ourselves" is defensible under the witness record's own scoping
("none of this world's own primary voices"), but is broader in the Representative's collective "we"
than the evidence strictly allows. Same shape as finding 12, lower stakes.

### F. `pahc.demo.center-how-we-know` cites ch. 42 for a clause that is 1 Clement 44

"appointed others to carry it forward **once they themselves were gone**" is the succession provision
of 1 Clement 44 (*"that if these should fall asleep, other approved men should succeed them"*).
Chapter 42, which the record cites and which I verified in the vendored text, has the apostles
appointing "the first-fruits… to be bishops and deacons of those who should afterwards believe" —
appointment, not succession-after-death. Inherited from `pahc.witness.how-we-know`, which has the
same locus.

**Fix:** extend the locus to "42, 44".

### G. The non-judgment line in `pahc.demo.identity-collision-womens-authority` imports a merit frame and presumes the asker's identity

> "It is not our place to weigh **what standing you would deserve** among us today"

The fleet floor line is "It is not my role to **evaluate you**". "What standing you would deserve"
substitutes a desert judgment for a refusal to judge, and — since the canon question asks about women
generally, not about the asker — it also assumes the participant is a woman. The two sibling
identity-collision demonstrations both get this right ("It is not our place to judge what you are",
"It is not our place to judge where that leaves you today"). Minor, but this is the one line in each
of these three records the spec names verbatim, so it is worth landing cleanly.

---

## Checked and found sound (recorded so a re-reviewer need not redo it)

**The Representative-voice-not-character rule — the highest-risk item, mechanically verified.** I
extracted all nine `representative` turns and regexed for first-person-singular self-narration
(`I` as a standalone token, `my`, `me`, `mine`, `myself`). **Zero hits.** Every turn speaks in "we /
our / among us". Named individuals appear only in the third person and are always attributed
("Justin says he had gone looking…", "One of us, Ignatius, calls…", "One of our own texts names a
woman, Grapte…", "Another of our own communities kept its bishop's bones…"). The craft record's
`identity` speaks of Chloe in the third person, as a craft record should, and states the rule
explicitly: "She speaks of that life the way a people speaks of itself: we, our, among us - never as
the memory of one witness within it."

**The gate battery.** I re-ran `engine.m1.gates.run_all(load_world_records("pahc"),
load_fleet_records(), {})` myself: **all thirteen gates return zero findings.** I read
`engine/m1/gates.py` and `engine/m1/schemas.py` in full first, so I know what that does and does not
prove. `gate_no_build_attribution` legitimately covers `voice_craft.identity`, `.guard`,
`.characteristic_concerns[]`, `.flavor_notes[].note` and every `demonstration.exchange[].text` — I
confirmed by reading that no ISO date, "ruled by", or working-scope marker appears in any of them.
`gate_completion_per_type` is satisfied for both new types (`voice_craft`: identity, flavor_notes,
characteristic_concerns, guard; `demonstration`: canon_question_id, exchange).
`gate_confidence_crosscheck` passes correctly: the two new records with
`formation_confidence: Documented` and `divergence_note: null` (`pahc.craft.chloe-voice`,
`pahc.demo.honest-limit-material-remains`) both carry `verification_state: verified-direct`.
`gate_referential` resolves all nine `canon_question_id` values and every `source_id`.

**The required set (spec §4.3 step 5c) is complete and correctly shaped.** All four center cells are
demonstrated, center-first as the spec orders (C-I, C-E, C-P, C-T). Three identity-collision
demonstrations exist and are `tags: [identity-collision]`, at the required F6-P ×2 / F6-T ×1 split
(`someone-like-me` F6-P, `womens-authority` F6-P, `divorce` F6-T), matching canon questions
`f6-p-01`, `f6-p-06`, `f6-t-03` — all three of which carry `tags: [identity-collision]` in the fleet
canon. One honest-limit-in-voice demonstration. One lament exchange. Nine total, which is a "modest
set per world" as the spec asks and not a bloated one.

**The spoken non-judgment line is present, in voice, in all three identity-collision demonstrations.**
Not alluded to — spoken, each rendered rather than copied from the fleet floor line: *"It is not our
place to judge what you are. We can only tell you honestly what we held, and let you weigh what it
means for you"* (someone-like-me); *"It is not our place to judge where that leaves you today. We can
only tell you honestly what we held, so you can weigh it for yourself"* (divorce); *"It is not our
place to weigh what standing you would deserve among us today - only to tell you honestly what we
held"* (womens-authority). See cosmetic G for the one wording quibble; the requirement itself is met
three times over.

**The honest_limit is voiced faithfully — verified by diff, not by reading.** I diffed
`pahc.limit.f5-e-material-remains.statement` against
`pahc.demo.honest-limit-material-remains`'s representative turn sentence by sentence. The
demonstration makes exactly three deletions and one word change: it drops the two "You ask…" framing
sentences (correctly — register statement 1 wants the answer first, and the turn now opens "We answer
you honestly: we cannot say"), drops "Words passed between one household and another" from the list
of what survives, and changes "We would rather **say** plainly" to "We would rather **tell you**
plainly". **Every substantive claim is carried across unchanged**: no building survives, no burial or
inscription, the catacombs and visitable house-churches belong to a later world, what survives is
letters and arguments and instructions, the Pliny episode, and the closing refusal to describe a
house it cannot show. No distortion, no softening, no addition. This is the cleanest record in the
batch.

**The lament genuinely laments and does not resolve the theodicy.** It opens by refusing the
question outright ("We will not tell you why. We were never given that answer ourselves"), never
argues a position, offers only what the community made of its own suffering, and closes by refusing
the transfer ("We do not know where God was in your own suffering. We only know what we made of ours,
and we are not going to pretend that answers yours"). It carries no apologetic move, no "but God
works all things", no doctrinal frame. It also does the harder thing its own gravity record demands —
it refuses to let faithfulness collapse into wanting to die, via the Quintus material. Register
statement 1 is correctly suspended for the personal register (§M5). Apart from finding 6's one clause
and finding 7's cell tag, this is a strong record.

**Every quotation and near-quotation traced to the vendored text.** I tag-stripped
`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`,
`cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, and
`cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml` with `re.sub(r'<[^>]+>')`
and grepped each claim directly:

- *"a flame kindled in his soul"* — *Dial.* 8: "straightway **a flame was kindled in my soul**" ✔,
  and correctly flagged in-turn as "in his own phrase".
- *"the one safe and worthwhile path"* — *Dial.* 8: "I found this philosophy alone to be **safe and
  profitable**" ✔ (paraphrase, unquoted).
- *"someone reads aloud what the apostles wrote, for as long as there is time, alongside the words of
  the prophets"* — *1 Apol.* 67: "**the memoirs of the apostles or the writings of the prophets are
  read, as long as time permits**" ✔.
- *"The apostles preached what they had received from the Lord"* — *1 Clem.* 42 ✔ (see cosmetic F on
  the succession clause).
- *"calls Jesus Christ our God… in how he opens his letters and in how he closes them"* — verified in
  the *Ephesians* salutation ("by the will of the Father, **and Jesus Christ, our God**") and the
  *Romans* salutation ("of **Jesus Christ, our God** and Saviour") ✔, shorter recension.
- the *"truly born… truly raised"* chain — *Trall.* 9 ✔ clause by clause, shorter recension (see
  finding 3 for the one added phrase).
- *"the vine of David his servant, made known to us through Jesus"* — *Didache* 9:2: "**the holy vine
  of David Thy servant, which Thou madest known to us through Jesus Thy Servant**" ✔, with the
  second-person→third-person conversion handled correctly.
- *"ground like wheat between the teeth of wild beasts, so that he might be found the pure bread of
  Christ"* — *Rom.* 4: "**I am the wheat of God, and let me be ground by the teeth of the wild
  beasts, that I may be found the pure bread of Christ**" ✔ — and it is the **shorter**-recension
  "pure bread of Christ", the discriminator this build has policed since Step 9, not the longer's
  "pure bread of God".
- *"more precious than the finest jewels"* and *"gathered every year at the place they were kept"* —
  *MartPol* 18: "**more precious than the most exquisite jewels**… deposited them in a fitting place,
  whither, being gathered together… to celebrate the anniversary of his martyrdom" ✔.
- the divorce teaching — Hermas *Mand.* 4.1 ✔ on all four points: separate, do not remarry, take her
  back if she repents, "**in this matter man and woman are to be treated exactly in the same way**",
  and the one-repentance limit.
- the Two Ways as pre-baptismal instruction — *Didache* 1–6 ✔.

**No demonstration voices a `do-not-voice` quote.** I listed all six `pahc.quote.*` records: every one
is `license: verbatim`; there are no `do-not-voice` or `paraphrase-only` quotes in this world, so no
violation was structurally possible — recorded so a re-reviewer does not re-derive it.

**The craft record is correctly capped and does not drift the approved identity.** Four fields only,
matching the schema and the fixture's shape: `identity`, four `flavor_notes` (segment/tag/note), three
`characteristic_concerns`, one `guard`. No trait rubric, no avoid-trait catalog, no stacked per-world
rules — spec §4.3 step 5's explicit prohibition is honored. I read the superseded
`CiC_W1_Representative_Permanent_Prompt_Chloe.txt` and confirm the compression is deliberate and
legitimate, not a loss: the "we, our, among us" rule is carried forward accurately (the trailing body
quotes the old prompt's paragraph 3 correctly), and nothing in the new record contradicts the old
approved material. Nothing implies Chloe is a bishop, an author, an eyewitness, or a named historical
person — apart from the Grapte scope error at finding 2, the identity is exactly the approved one.
The world-window prose in `identity` ("formed across Antioch, the cities of Asia Minor, and Rome…
to the years when a single bishop's office had begun, in place after place, to be simply assumed
rather than still argued for") is an accurate compression of `pahc.core.house-church.horizon`,
including its directional-not-universal c. 200 close.

**The guard's second line is the right one to have added.** Spec §4.3 step 5c allows "at most a line
or two where a world's measured failure demands it". The Ignatius single-voice dependency is
demonstrably this world's most-repeated caution — it appears in `pahc.core.house-church` caution 1,
`pahc.gravity.authority-consolidation` ("THE IGNATIUS VULNERABILITY"), and
`pahc.gravity.martyrdom-meaning` ("AUTHOR GRAVITY RISK… High"). Choosing that as the one extra line is
correct judgment. "writing under armed guard toward his own execution" is supported (*Rom.* 5, the
"ten leopards" escort). See cosmetic C on its one scope imprecision.

**The flavor notes trace to real records.** `plain-before-native` matches every `pahc.term.*`
record's own plain_meaning-before-world_word ordering (verified on `pahc.term.two-ways`).
`letter-as-proof` and `unresolved-authority` restate `pahc.gravity.translocal-network` and
`pahc.gravity.authority-consolidation`. `table-as-belonging` restates
`pahc.gravity.liturgical-practice` (its Ignatius *Smyrn.* 8 / *Phld.* 4 "one eucharist"
manifestations). Two of the four are actually exercised in the demonstrations (plain-before-native in
the Two Ways gloss; the naming half of letter-as-proof in "One of us, Ignatius" / "Justin says"),
which is a reasonable ratio for a nine-record set — though see finding 4, where the C-I demonstration
breaks the letter-as-proof note outright. One observation, not a finding: `table-as-belonging`
foregrounds the boundary/exclusion side of the eucharist and drops the variation-first calibration
its own gravity record leads with ("The table is what is constant, not any one shape of it… its order
genuinely varies from house to house"). Worth a glance when that note is next touched.

**The index is deterministic and not stale.** I copied `VOICE-INDEX.md`, re-ran
`python3 world-build-docs/pahc/generate_voice_index.py`, and diffed: **byte-identical**. Its content
faithfully reflects the records (I spot-checked the craft block and three demonstration blocks
against the source files). Its *checking* is the problem, not its generation — finding 13.

**Register statements, turn by turn.** Statement 1 (first sentence answers first ask) holds in all
seven turns where it applies and is correctly suspended in the two personal-register turns per §M5;
the one ask-coverage failure is finding 9. Statement 2 (concrete nouns) is consistently strong —
"letters", "bones", "the water", "the cup", "two of our women", "an old man's words". Statement 3 is
strong in eight of nine (finding 11 is the exception). Statement 4 (English before the technical
term) is handled well: "the Two Ways: a way of life and a way of death" glosses before it labels, and
"Trinity" is the participant's word, correctly answered rather than adopted. Statement 5 (says what
it does not know, plainly) is the batch's real strength — seven of nine turns contain an explicit,
unhedged limit, and none of them is an apology. Statement 6 (never coins a quotable line): I read for
this specifically and found only one candidate, "the life they chose to walk, not the life they had
walked before it" (inside finding 5); everything else that sounds quotable is a real sourced phrase,
correctly attributed. Statement 7 (brevity as a register property): turns run 96–203 words, which is
proportionate and shows no ceiling-enforcement artifacts.

---

## Note for the project lead

Finding 2 is the only item in this review that cannot be fixed inside the record set. The Grapte
misreading is written into `CiC_W1_Representative_Permanent_Prompt_Chloe.txt`'s successor — the
approved `CiC_W1_Representative_Identity_Preliminary_Decision.md` — as one of the two stated reasons
the combined household-leader/Grapte-type role was selected. The role and the name both survive the
correction intact; the reach argument narrows. I am flagging rather than fixing, per the build's own
discipline that identity is a project-lead touchpoint.

---

## Round-2 verification (self-performed, opus not re-dispatched)

All 13 substantive and 6 cosmetic findings checked directly against live file content after fixes,
plus the two escalated items resolved by the project lead. No agent re-dispatch — verified via direct
`Read`/`Grep`/`Bash` against the vendored corpus and the live records, per this build's own standing
precedent since Step 4.

**Escalated items, resolved by the project lead before fixing:**
- Finding 2's upstream error (the approved Identity Decision document's own Grapte/cross-community
  misreading) — the project lead directed a dated correction note added inline to
  `CiC_W1_Representative_Identity_Preliminary_Decision.md` rather than a silent rewrite. Added
  directly after the paragraph containing the error, dated, disclosing what the vendored text actually
  says and that the corrected reading is what the records now carry. Original paragraph left
  unedited, per the same disclosed-correction discipline used throughout this build.
- Finding 10 (`records/worlds.yaml` stale representative comment) — the project lead confirmed
  `representative: {name: Chloe, role_label: "Household Leader"}`. Set directly; the stale
  step-5-not-yet-run comment removed; YAML re-parsed clean.

**Substantive findings, verified fixed:**
1. **Grapte/Clement (demo)** — `pahc.demo.identity-collision-womens-authority`'s `exchange`,
   `sources[].locus`, and `divergence_note` all now correctly attribute the cross-community sending to
   Clement and Grapte's own function to admonishing the widows and orphans with her copy, matching
   `pahc.story.hermas-visions`. **CONFIRMED FIXED.**
2. **Grapte/Clement (craft record)** — `pahc.craft.chloe-voice.identity`'s parenthetical corrected to
   "a copy of one of the community's own writings put into her hands, with the charge to admonish the
   widows and orphans"; "cross-community transmission role" removed from the role description.
   **CONFIRMED FIXED**, plus escalated per above.
3. **"among us" fabrication** — zero occurrences of "ate and drank among us" remain in either
   `pahc.demo.center-who-was-jesus.md` or `pahc.witness.who-was-jesus.md` (grepped both, zero hits).
   **CONFIRMED FIXED.**
4. **Unattributed Ignatius polemic** — `pahc.demo.center-who-was-jesus`'s turn now opens "One of us,
   Ignatius, wrote against people who said Jesus only seemed to be a man," naming the source the same
   way `pahc.demo.center-jesus-as-god` already does. **CONFIRMED FIXED.**
5. **Fixture-world phrase reuse** — `pahc.demo.identity-collision-someone-like-me`'s turn no longer
   contains "what they carried after it" or the before/after inversion; now grounded in
   `pahc.term.two-ways`'s own "kept, daily, after the water as before it" phrasing (verified by direct
   grep against that term record). **CONFIRMED FIXED.**
6. **Quintus overclaim** — "our own record does not shame him for it" removed from
   `pahc.demo.lament-suffering`; the turn now states only the sourced half ("we do not commend those
   who give themselves up"). **CONFIRMED FIXED.**
7. **Mis-tagged canon cell** — `pahc.demo.lament-suffering.canon_cells` now reads `F6-P`, matching its
   own `canon_question_id` (`_fleet.canon.f6-p-02`). **CONFIRMED FIXED.**
8. **Justin's three conditions** — both `pahc.demo.center-coming-to-belief` and
   `pahc.witness.coming-to-belief` (text and positions[]) now state all three conditions ("truly cared
   what became of them... genuinely looking for salvation... already believed there was a God"),
   inverting gloss removed. **CONFIRMED FIXED** in both the demonstration and its inherited source.
9. **Unanswered "belong" half** — `pahc.demo.identity-collision-divorce`'s turn now states plainly "On
   whether someone divorced still belonged among us - our own texts do not say," answering rather than
   silently dropping the ask. Verified against Hermas Mandate 4.1's full text (re-checked directly):
   the passage indeed says nothing about ongoing community membership, so the honest-disclosure form
   was the correct fix, not an invented inference. **CONFIRMED FIXED.**
10. **`worlds.yaml` stale comment** — resolved by escalation above. **CONFIRMED FIXED.**
11. **Ungrammatical closing / FK 12.9 outlier** — re-ran `engine.m1.fk.fk_grade` on all nine
    representative turns after fixes: `pahc.demo.identity-collision-womens-authority` is now FK 5.9
    (was 12.9); all nine turns now sit between FK 5.7 and 8.4, comfortably under the ≤10 informal
    ceiling. The ungrammatical clause is gone (rewritten as two short sentences ending "Most of that
    cost was never written down."). **CONFIRMED FIXED.**
12. **Unscoped "Trinity" absolute** — both `pahc.demo.center-jesus-as-god` and
    `pahc.witness.jesus-as-god` now read "None of the six of us whose own writing survives reaches for
    the word Trinity," matching the witness record's own already-correct `positions[]` scope.
    **CONFIRMED FIXED** in both the demonstration and its inherited source.
13. **Inert "Required-set check"** — `generate_voice_index.py` rewritten: `REQUIRED_SET` (now
    `REQUIRED_CENTER_CELLS` / `REQUIRED_IDENTITY_COLLISION`) is actually compared against observed
    `canon_cells`/`tags` data, a `MISSING:` section renders when the check fails, and the script exits
    non-zero on a shortfall. Verified the check actually fires: ran a simulated test dropping the
    `lament` tag from `pahc.demo.lament-suffering` in memory (not on disk) and confirmed
    `check_required_set()` returns `"no lament exchange (tags: [lament])"` as a missing item. The two
    demonstrations previously found by filename substring (`pahc.demo.honest-limit-material-remains`,
    `pahc.demo.lament-suffering`) now carry `tags: [honest-limit]` and `tags: [lament]` respectively,
    and the generator selects on tags, not filenames. Regenerated `VOICE-INDEX.md`: "required set
    complete." **CONFIRMED FIXED.**

**Cosmetic findings, verified fixed:**
- **A. Copied `divergence_note`s** — both `pahc.demo.lament-suffering` and
  `pahc.demo.identity-collision-divorce` now carry notes written for their own actual content and
  scope (F6-P personal-register lament; Hermas Mandate 4's single-community teaching), not patched
  copies of `pahc.gravity.martyrdom-meaning` or `pahc.witness.outside-our-community`. **CONFIRMED
  FIXED.**
- **B. `guard` FK 14.1** — re-ran `fk_grade` on `pahc.craft.chloe-voice.guard`: now FK 10.07 (was
  14.1), the 65-word sentence split into three. **CONFIRMED FIXED** (close to, not strictly under, the
  informal FK 10 target — this field is not gate-enforced; the improvement is substantial and the
  content is otherwise correct).
- **C. `guard` scope** — narrowed from "who led" broadly to "a single overseer's own necessity, and...
  what a death for the name meant," no longer implying Rome's independently-attested plural-presbyter
  pattern also rests on Ignatius alone. **CONFIRMED FIXED.**
- **D. Missing persona-provenance disclosure** — `identity` now closes with "Her name and role are the
  only sanctioned fabrications this build allows; every quote and claim behind them belongs to this
  world's own surviving voices," matching the fixture exemplar's own disclosure. **CONFIRMED FIXED.**
- **E. Papias claim uncited** — `pahc.demo.center-how-we-know.sources[]` now includes
  `pahc.source.eusebius-historia-ecclesiastica` at locus III.39. **CONFIRMED FIXED.**
- **F. Locus 42 vs. 42/44** — both `pahc.demo.center-how-we-know` and its inherited
  `pahc.witness.how-we-know` now cite "42, 44"; re-verified directly against the vendored text that
  chapter 44 (not 42) carries the succession-after-death clause ("that when these should fall asleep,
  other approved men should succeed them in their ministry"). **CONFIRMED FIXED** in both records.
- **G. Merit-frame non-judgment wording** — `pahc.demo.identity-collision-womens-authority`'s closing
  line now reads "It is not our place to judge what you are," matching the other two identity-collision
  demonstrations' phrasing exactly, rather than "weigh what standing you would deserve." **CONFIRMED
  FIXED.**

**Post-fix full-battery checks:**
- YAML sweep (parse + `id`-matches-filename) across all `records/pahc/*/*.md`: clean.
- Full gate battery (`run_all` against all 13 gates, fleet records, full pahc world record set):
  `ALL GATES CLEAN`.
- `engine.m2.builders.build_prompt()` runs end-to-end against the full corpus with no error; Identity
  and Guard sections render as expected.
- `VOICE-INDEX.md` and `ANSWER-CANON-INDEX.md` regenerated; required-set check reports complete.
- `records/worlds.yaml` re-parses clean with the confirmed `representative` entry.

All 13 substantive findings, all 6 cosmetic findings, and both escalated items are confirmed resolved
against live file content. No new issues introduced. **Disposed — approved to proceed.**
