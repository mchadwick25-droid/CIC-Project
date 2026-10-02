# Step 9 — Doc_09 Story Repository — Round 1 Review (cold, adversarial)

**Scope reviewed:** 13 `records/pahc/story/*.md`, `Build/worlds/pahc/build/STORY-INDEX.md`,
`Build/worlds/pahc/build/generate_story_index.py`, plus the reciprocal `relations[]` edges added to
6 `pahc.gravity.*`, 2 `pahc.force.*`, and 1 `pahc.term.*` record. Checked against the approved
`CiC_W1_Doc09_Story_Inventory.md` and all 13 `Doc09_Story_Chunks/*.md`, and against the vendored
primary texts under `cic/texts/` (ANF vols. 1, 2, 3, 7; NPNF2 vol. 1). Reviewed at commit
`b145ce96`.

---

## Verdict — MINOR FIXES NEEDED

Seven SUBSTANTIVE findings, five of them confined to two records (`pahc.story.hermas-visions`
carries three on its own; `pahc.story.martyrdom-of-polycarp` and `pahc.story.didache-eucharist`
one each) and none of them structural. The core of this batch is genuinely strong, and I verified
the strong parts rather than assuming them. I extracted **every** quoted span from all thirteen
`text` fields (36 spans) and checked each one against the vendored file the record names: 34 are
exact. The Ignatius recension discipline holds everywhere it applies — Romans 4 (`"the pure bread
of Christ"`, the shorter-recension discriminator against the longer's `"pure bread of God"`),
Romans 5, Philadelphians 4, Smyrnaeans 8 (`"even as, wherever Jesus Christ is, there is the
Catholic Church"`, against the longer's `"where Christ is, there does all the heavenly host stand
by"`), and Magnesians 6 are all taken from the shorter column. The PARAPHRASE-ONLY discipline holds
exactly: `pahc.story.nero-scapegoating` contains **zero** quotation marks anywhere in its `text`,
and `pahc.story.mutual-aid-prisoner` quotes only its two Tertullian *Apologeticus* 39 spans (both
exact) while rendering every Lucian detail — including the Doc_09 chunk's own quoted `"no small
sums"` — as bare paraphrase. All three claimed corrections to the approved Doc_09 chunks are
real and correct, verified in both directions: MartPol 18 reads `"more precious than the most
exquisite jewels, and more purified than gold"` (chunk said "finest gold"); Magnesians 6 reads
`"assembly of the apostles"` in *both* recensions (chunk said "council"); Tertullian reads
`"drinking-bouts"` / `"boys and girls destitute of means and parents"` (chunk paraphrased
"drinking-parties" / "orphans"). The batch also silently caught two more real drifts not claimed in
the commit message — Didache 14's `"profaned"` (chunk: "defiled") and Justin's `"memoirs of the
apostles"` (chunk: "records of the apostles"). Mechanically it is clean: I re-ran
`engine.m1.gates.run_all` over `load_world_records("pahc")` + `load_fleet_records()` myself —
**all thirteen gates return zero findings across 118 records**; the index regenerates byte-identical
to the committed file; and reciprocity holds in *both* directions (the gate iterates every world
record, so its clean pass proves all 22 new edges are answered on both sides — I also confirmed the
edges by reading the diff on all nine touched gravity/force/term files). Tier classifications match
Doc_09 exactly, 7/0/1/5, **including both of Doc_09's own debated edge cases**: Story 006 stays
Tier 1 with its recurring-practice reasoning preserved verbatim in substance, and Story 007 stays
Tier 1 with its named-self-narrator-vs-hagiographic-attribution reasoning and its genre disclosure
both preserved. The Absent Stories reconciliation is accurate item by item: I mapped
`pahc.core.house-church`'s 11 items against Doc_09 §4's 12 one at a time, and the generator's
`RECONCILED_ABSENT_STORIES` cross-references match both sources on all 11; Doc_09's item 8 is
indeed a citation-housekeeping note about two Ignatius passages falling under an existing Registry
row, not an absent story, and Doc_09's own §7 Outstanding Item 2 says so itself. The
`day-under-bishop-and-presbyters` decision to drop Polycarp from `sources[]` is correct, not a
lapse: I read Doc_09's chunk 012 Story Text element by element and its Source Identification
section in full — every element traces to Ignatius (Magn. 6 / Trall. 3 / Smyrn. 8), 1 Clement 44,
Hermas *Vis.* 2.4.3, or Doc_05, and nothing anywhere in that chunk depends on Polycarp's letter.

What fails is narrower: two quotation marks around wording the vendored text does not carry, one
wrong source locus, one canon cell whose own stated justification appeals to material the record
does not contain, one confidence rating that contradicts the record's own divergence note, one
set of gravity connections dropped from Doc_09 §3 without disclosure (with a commit-message claim
that this did not happen), and one `absent_detail` contradicted by a source already in this repo.

---

## SUBSTANTIVE findings

### 1. `pahc.story.martyrdom-of-polycarp` — `"the Lord permitting"` is not in the vendored text

**File:** `records/pahc/story/pahc.story.martyrdom-of-polycarp.md`, `text` field.

The record reads: `...to keep in a fitting place, where they might gather each year, "the Lord
permitting," to celebrate the anniversary of his martyrdom...`

**What I checked:** MartPol 18 in `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`
(div1 iv, section iv, ch. xviii) reads: *"...and deposited them in a fitting place, whither, being
gathered together, as opportunity is allowed us, with joy and rejoicing, the Lord shall grant us to
celebrate the anniversary of his martyrdom..."* I then grepped the whole tag-stripped ANF vol. 1
for the string "Lord permitting" — **zero hits anywhere in the volume** (the only "permitting" hits
are "the Father permitting" at a Ps.-Ignatius passage and one unrelated Irenaeus line). The phrase
is a real rendering in *other* translations (e.g. Lightfoot's "where the Lord will permit us"), but
this record's own trailing body claims "Every quotation checked directly against
cic/texts/anf01...ch. 18," and against that edition the quotation marks are unearned. This is the
one place in the batch where a quotation mark encloses invented wording.

**Fix:** drop the quotation marks and paraphrase (`...where they might gather each year, as
opportunity allowed, to celebrate...`), or quote the edition: `"as opportunity is allowed us"`.

### 2. `pahc.story.didache-eucharist` — `"having first confessed"` drifts from Didache 14:1

**File:** `records/pahc/story/pahc.story.didache-eucharist.md`, `text` field.

The record quotes: `"having first confessed your transgressions, that your sacrifice may be pure"`.

**What I checked:** Didache 14:1 in `cic/texts/anf07_lactantius-apostolic-constitutions-didache-
liturgies.xml` (div1 viii, ch. 14 / viii.iii.xiv) reads: *"do ye gather yourselves together, and
break bread, and give thanksgiving **after** having confessed your transgressions, that your
sacrifice may be pure."* I grepped the whole stripped volume for "having first confessed" —
**zero hits**; only "after having confessed" occurs. The word "first" is inserted inside the
quotation marks. This is inherited verbatim from the Doc_09 chunk, which the record's own body
claims to have re-verified directly against ch. 14 — so this is a re-verification pass that
reported a correction on the same page (`"Maran atha"`, correctly caught) while missing a drift
three lines below it.

**Fix:** change to `"after having confessed your transgressions, that your sacrifice may be pure"`.

### 3. `pahc.story.hermas-visions` — wrong locus for the load-bearing quotation

**File:** `records/pahc/story/pahc.story.hermas-visions.md`, `sources[0].locus`.

The record cites: `"Vision 2.2 (the old woman who is the Church); Vision 2.4.3 (Clement and
Grapte)"`.

**What I checked:** in `cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`
(div1 ii), the exchange the record quotes — *"Who do you think that old woman is...?" ... "It is
the Church." ... "Because she was created first of all. On this account is she old. And for her
sake was the world made."* — is **Vision Second, Chapter IV**, i.e. *Vis.* 2.4.1, four lines above
the Clement/Grapte instruction the same record correctly cites as *Vis.* 2.4.3. Vision Second
Chapter II, which the record cites instead, is the limits-of-repentance / "filled up are the days
of repentance" material and says nothing about the old woman or the Church. Separately, the
record's clause "In a later vision she grows younger and more radiant" belongs to Vision Third and
carries no locus at all.

**Fix:** change the locus to `"Vision 2.4.1 (the old woman who is the Church); Vision 2.4.3
(Clement and Grapte); Vision 3 (the woman growing younger)"`.

### 4. `pahc.story.hermas-visions` — `canon_cells: F1-P` is a stretch, and its own justification cites material the record does not carry

**File:** `records/pahc/story/pahc.story.hermas-visions.md`, `canon_cells`, and its trailing body.

**What I checked:** F1-P's two canon questions are `_fleet.canon.f1-p-01` ("I grew up being told
doubt was sin. Was there room among your people for doubt?") and `_fleet.canon.f1-p-02` ("What did
you do when you couldn't believe what your own church taught?"). Neither is about repentance after
sin. This record's `text` contains no doubt content at all — its narrated material is the old
woman/Church revelation, the one-further-repentance-after-baptism message, and the Clement/Grapte
instruction. The body defends the tag by saying it "reinforces pahc.witness.doubt-and-asking, which
draws on the same figure's own Mandate 9 content" — but Mandate 9 is exactly what this record does
*not* cite (`sources[0].locus` is Vision 2 only), so the justification rests on content that lives
in a different record. Meanwhile `_fleet.canon.f4-i-05` ("When someone wronged the community, how
was it handled — and could they come back?") is a near-exact match to this story's actual centre,
and F4-I is already claimed by seven non-story pahc records, so reuse there is fully in keeping with
this step's stated retrieval-grounding rationale. Because these tags drive retrieval, not coverage,
a mismatched cell means this story surfaces against the wrong participant question.

**Fix:** replace `F1-P` with `F4-I` (matching `f4-i-05`), and rewrite the body sentence to name
`f4-i-05` rather than Mandate 9.

### 5. `pahc.story.hermas-visions` — `formation_confidence: Contested` contradicts its own divergence note and Doc_09 Story 007

**File:** `records/pahc/story/pahc.story.hermas-visions.md`, `confidence.formation_confidence`.

**What I checked:** Doc_09 §2 Story 007 states "**Confidence:** Widely Accepted that the text and
its visions are genuinely Hermas's own reported content / Contested on composition dating and
staging," and §5 places Stories 001–007 as ranging from Widely Accepted at the underlying-fact
level down to Contested on dating/representativeness. This record's own `divergence_note` restates
that split correctly ("Widely Accepted that the text and its visions are genuinely Hermas's own
reported content; Contested on composition dating and staging") — but then sets the scalar field to
the *lower* half of the pair. Every other record in the batch with the same shape takes the leading
value: `ignatius-guarded-journey`, `first-clement-corinthian-dispute`, `justin-sunday-gathering` and
`nero-scapegoating` all carry Widely Accepted/Contested notes and all set `Widely Accepted`;
`pliny-interrogation` and `polycarp-forwards-letters` carry Documented/Contested and both set
`Documented`; only `martyrdom-of-polycarp`, whose Doc_09 lead value genuinely *is* Contested, sets
Contested. Hermas is the sole outlier, and the downgrade propagates into the generated
`STORY-INDEX.md` catalog table, where it now reads "Contested" — the only Tier 1 story so labelled.

**Fix:** set `formation_confidence: Widely Accepted` and regenerate `STORY-INDEX.md`. (If the
downgrade is deliberate, it needs a sentence in the divergence note saying so and why it departs
from Doc_09's own rating — right now nothing discloses it.)

### 6. `pahc.story.nero-scapegoating` — Doc_09 §3's three gravity connections for Story 005 are dropped with no disclosure, and the commit message claims otherwise

**Files:** `records/pahc/story/pahc.story.nero-scapegoating.md` (`relations`), and the Step 9 commit
message; visible in `Build/worlds/pahc/build/STORY-INDEX.md`.

**What I checked:** Doc_09 §2 Story 005 lists "**Connected gravities:** Generative trigger for G01
(per Doc_08 Connection 1); background to G03, G04," and §3's rebuilt summary lists Story 005
explicitly under G01, under G03 ("background to Story 005") and under G04 ("Stories 001, 005
(background), 008"). The record declares exactly one relation — `associated-with →
pahc.force.neronian-persecution` — and no gravity relations at all. Consequently the generated
story-to-gravity summary lists G01 as `day-under-bishop-and-presbyters, first-clement-corinthian-
dispute, hermas-visions, ignatius-guarded-journey, one-eucharist-under-bishop` with
`nero-scapegoating` absent. I checked all six gravities against Doc_09 §3 line by line: G02, G05
and G07 match exactly, and Story 005 is the *only* divergence in the whole set. The commit message
states the index carries "a mechanically-derived story-to-gravity connection summary matching
Doc_09's own Section 3 table exactly" — that specific claim is false. The record's body explains
the force link ("this story is that force's own narrative form") but never mentions dropping G01,
G03 or G04, unlike `mutual-aid-prisoner`, which discloses its empty `relations` explicitly and at
length. There *is* an indirect path — `pahc.force.neronian-persecution` already declares
`associated-with → pahc.gravity.authority-consolidation` — but an undisclosed indirection is not
the same as the disclosed discipline call made for Story 013.

**Fix:** add `associated-with → pahc.gravity.authority-consolidation` to this record (with the
reciprocal edge on the gravity record, per the existing pattern), and add a body sentence stating
that Doc_09's G03/G04 "background" links are deliberately routed through
`pahc.force.neronian-persecution` rather than asserted as direct story-gravity edges. Correct the
commit-message claim in the disposition note.

### 7. `pahc.story.ignatius-guarded-journey` — `absent_detail` is contradicted by a source already in this repo

**File:** `records/pahc/story/pahc.story.ignatius-guarded-journey.md`, `absent_detail`.

The record asserts: "No source records what happened after Ignatius reached Rome, **or confirms his
death actually occurred as he anticipated it** — the letters themselves end before that point, and
no independent account of his arrival or execution survives."

**What I checked:** Polycarp, *Letter to the Philippians* ch. 9 — registered here as
`pahc.source.polycarp-philippians` (P04) and vendored at
`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`, div1 iv, section ii, four chapters above
the ch. 13 passage this same batch quotes in `pahc.story.polycarp-forwards-letters` — reads: *"...
not only in the case of the blessed Ignatius, and Zosimus, and Rufus... they are [now] in their due
place in the presence of the Lord, **with whom also they suffered**."* That is an independent,
near-contemporary witness inside this world's own Native evidentiary base that treats Ignatius's
death as accomplished. The second half of the sentence (no account of his *arrival or execution*)
stands and is a genuinely good absence; the "or confirms his death actually occurred" clause does
not. What makes this more than pedantry is that the interesting fact here is a *tension* the record
elsewhere already invokes: Phil. 9 speaks of Ignatius as having suffered while Phil. 13 asks the
Philippians for "more certain information... respecting both Ignatius himself, and those that were
with him" — which is one of the pillars of the Harrison two-letter argument that this batch's own
`pahc.story.polycarp-forwards-letters` cites by name.

**Fix:** restate as: "No source narrates Ignatius's arrival in Rome or his execution — the letters
end before that point, and no account of it survives. Polycarp's own letter speaks of him as
already having suffered (ch. 9) while elsewhere asking for news of him (ch. 13), a tension bound up
with the question of that letter's own unity."

---

## COSMETIC findings

### 8. `pahc.story.pliny-interrogation` — trailing body names the wrong prior F6-E claimants

**File:** `records/pahc/story/pahc.story.pliny-interrogation.md`, trailing body.

The body says F6-E is "the same cell already claimed by `pahc.gravity.state-pressure` and
`pahc.limit.f5-e-material-remains`." I enumerated `canon_cells` across all 118 pahc records:
`pahc.gravity.state-pressure` claims **F3-I**, and `pahc.limit.f5-e-material-remains` claims
**F5-E**. Neither claims F6-E. The actual prior F6-E claimants are `pahc.force.martyrdom-meaning`,
`pahc.gravity.martyrdom-meaning` and `pahc.term.ministrae`. The tag itself is right — `f6-e-01`
("The clearest outside account of your worship came from torturing two enslaved...") is a
near-verbatim match to this story — only the provenance sentence is wrong, and trailing bodies are
never compiled, so nothing participant-facing is affected. It does, however, misstate the batch's
own audit trail (and the same wrong pairing was carried forward into this step's own review brief).

**Fix:** replace with "already claimed by `pahc.term.ministrae`, `pahc.force.martyrdom-meaning` and
`pahc.gravity.martyrdom-meaning`."

### 9. `pahc.story.two-ways-catechumen` — locus under-cites, and the Story Text drops the Two Ways' actual moral content

**File:** `records/pahc/story/pahc.story.two-ways-catechumen.md`, `sources[0].locus` and `text`.

Doc_09 gives Story 009's source as "Didache chs. 1–7," and the chunk's Source Identification breaks
it into 1:2, 2:1–4:14 (Way of Life prohibitions and almsgiving) and 5:1 (Way of Death catalog) —
the very passage Doc_09's own round-1 review corrected. This record's locus is `"1:1-2; 7 (the
baptismal instruction)"`, yet its `text` narrates the Way of Death catalog (Didache 5) with no
locus, and it drops the whole concrete moral inventory the chunk carries (murder, adultery, magic,
abortion, exposure of infants, theft, lying, almsgiving). Since the chunk's own Formation Ecology
Connection turns on "formation beginning with a concrete, memorizable ethical schema," a Two Ways
story whose compiled `text` never says what the Two Ways contain — beyond love of God and neighbour
and the Golden Rule — is thinner than what it re-derives. Everything actually quoted is exact
(Didache 1:1 and 1:2 verified against the vendored ANF vol. 7), so this is compression, not error.

**Fix:** extend the locus to `"1:1-2; 2:1-4:14; 5:1; 7"` and restore a clause naming the
prohibitions and the almsgiving instruction.

### 10. `pahc.story.pliny-interrogation` — the contested reading of *ministrae* is dropped from the compiled text

**File:** `records/pahc/story/pahc.story.pliny-interrogation.md`, `text`.

Doc_09's chunk 004 Story Text discloses inline that *ministrae* is "a term some read as a functional
title, 'ministers' or 'deaconesses,' though this is contested." The record's `text` presents the
Latin bare. The vendored NPNF2 vol. 1 rendering of Pliny 10.96 in fact translates it interpretively
("two female slaves who were called deaconesses (*ministræ*)"), which is precisely the reading
Doc_09 flags as contested — so a reader coming to this record from the cited edition gets the
contested gloss with no caveat attached. Risk is low: the disclosure exists in `pahc.term.ministrae`
and `pahc.figure.ministrae`, and the record's body points there.

**Fix:** restore a half-clause, e.g. "called *ministrae* — a word some read as a functional title,
though that reading is contested."

---

## Checked and found sound (recorded so a re-reviewer need not redo it)

- **All 36 quoted spans** across the 13 `text` fields extracted programmatically and checked
  against the named vendored file; 34 exact. Findings 1 and 2 are the only two failures.
- **Ignatius recension discipline:** shorter recension used in every case (Rom. 4, Rom. 5, Phld. 4,
  Smyrn. 8, Magn. 6), confirmed by the ANF's parallel-column discriminators.
- **PARAPHRASE-ONLY discipline:** zero quotation marks anywhere in `nero-scapegoating.text`; only
  Tertullian quoted in `mutual-aid-prisoner.text`; the chunk's `"no small sums"` (Lucian) correctly
  removed.
- **All three claimed chunk corrections** verified true in both directions (new wording matches
  vendored; old chunk wording does not).
- **Tier classifications:** all 13 match Doc_09 (7/0/1/5); Story 006's and Story 007's specific,
  reasoned edge-case calls both preserved with their reasoning intact.
- **Gate battery:** `run_all` over `load_world_records("pahc")` + `load_fleet_records()` — zero
  findings on all 13 gates, 118 records. `narrative_tier` in range on all 13; all four
  `COMPLETION_REQUIRED` story fields present and non-empty on all 13.
- **Reciprocity:** clean in both directions (gate iterates every world record); the 22 new edges
  confirmed by reading the diff on all nine touched gravity/force/term files. Count claim of "22
  edges" is accurate.
- **Index regeneration:** `generate_story_index.py` reproduces the committed `STORY-INDEX.md`
  byte-identical; its catalog table, tier counts, No-Tier-5 check and reciprocity check all match
  the underlying records.
- **Absent Stories reconciliation:** world_core's 11 items map one-to-one onto Doc_09 §4's 12 minus
  item 8; the generator's cross-references are correct on all 11; the "never an absent STORY"
  characterisation of Doc_09 item 8 is accurate against Doc_09's own §4 item 8 and §7 Outstanding
  Item 2.
- **Polycarp omission from `day-under-bishop-and-presbyters`:** verified defensible — no element of
  Doc_09's own chunk 012 Story Text or Source Identification depends on Polycarp's letter.
- **`mutual-aid-prisoner`'s empty `relations`:** verified as the disclosed discipline Doc_09 §2
  itself requires.
- **canon_cells:** ten of the thirteen are genuine close matches (F6-E×3, F3-P, F5-P, F4-I×3, F3-I×2,
  F3-T, F5-T checked against the actual `_fleet.canon.*` question text). F1-P is finding 4;
  `justin-sunday-gathering`'s F4-I and `one-eucharist-under-bishop`'s F3-T are looser but defensible
  and each discloses its own reasoning.
- **Cross-record contradictions:** none found. The apparent Polycarp bishop/presbyter conflict
  between stories 001 and 003 is Ignatius's designation vs. Polycarp's self-designation, and both
  records disclose it.

---

## Round-2 verification (self-performed, opus not re-dispatched)

All ten findings checked directly against live file content after fixes. No agent re-dispatch —
verified via direct `Read`/`Grep`/`Bash` against the vendored corpus and the live records, per this
build's own standing precedent since Step 4 (avoiding the API-failure risk class hit by a re-
dispatched round-2 agent at that step).

1. **`martyrdom-of-polycarp` — "the Lord permitting"**: confirmed zero hits for that phrase anywhere
   in the full stripped ANF vol. 1 (`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`). `text`
   now reads `"as opportunity is allowed us,"` matching the edition's actual ch. 18 wording. FIXED
   note present in the trailing body. **CONFIRMED FIXED.**
2. **`didache-eucharist` — "having first confessed"**: `text` now reads `"after having confessed
   your transgressions,"` matching Didache 14:1 (div `viii.iii.xiv`) exactly. FIXED note present.
   **CONFIRMED FIXED.**
3. **`hermas-visions` — locus**: now reads `"Vision 2.4.1 (the old woman who is the Church); Vision
   2.4.3 (Clement and Grapte); Vision 3 (the woman growing younger)"` — the old Vision 2.2 citation
   is gone, and Vision 3 is now cited for the "grows younger" detail it actually supplies.
   **CONFIRMED FIXED.**
4. **`hermas-visions` — canon_cells**: `canon_cells:` now reads `F4-I`, not `F1-P`. The trailing body
   was rewritten to ground this in f4-i-05 ("When someone wronged the community, how was it handled
   — and could they come back?") rather than the old Mandate-9/doubt-and-asking justification, and
   documents all three corrections as a single FIXED note. **CONFIRMED FIXED.**
5. **`hermas-visions` — formation_confidence**: now reads `Widely Accepted`, matching its own
   `divergence_note` (Widely Accepted on attestation, Contested only on composition dating) and
   Doc_09 Story 007. **CONFIRMED FIXED.**
6. **`nero-scapegoating` — dropped gravity connections**: `relations[]` now carries a second edge,
   `associated-with → pahc.gravity.authority-consolidation` (G01), reciprocated — confirmed present
   on both `pahc.story.nero-scapegoating.md` (line 34) and `pahc.gravity.authority-consolidation.md`
   (line 55, in its own `relations[]` list). The trailing body now discloses, rather than silently
   drops, that the G03 (state-pressure) and G04 (martyrdom-meaning) background links are routed
   through the existing `pahc.force.neronian-persecution` relation instead of asserted as direct
   story-gravity edges — same disclosed-discipline pattern as `mutual-aid-prisoner`. Full gate
   battery (including `gate_reciprocity`, run across the complete world record set) reports clean
   after this edge was added. **CONFIRMED FIXED.**
7. **`ignatius-guarded-journey` — `absent_detail` contradicted by Polycarp *Phil.* 9**: rewritten to
   state that no source narrates the arrival/execution itself, while disclosing the ch. 9 / ch. 13
   tension directly. Both quotations re-verified fresh against
   `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`: ch. 9's `"in their due place in the
   presence of the Lord, with whom also they suffered"` (referring to Ignatius alongside Zosimus and
   Rufus) and ch. 13's `"more certain information... respecting both Ignatius himself, and those
   that were with him"` both confirmed exact. `pahc.source.polycarp-philippians` added to this
   record's own `sources[]` with locus, and the trailing body discloses that record's own
   transmission caveat (chs. 10-14 survive only via the Latin, not the Greek). **CONFIRMED FIXED**
   — and strengthened beyond the review's own suggested language by adding the source citation and
   the Latin-transmission disclosure.
8. **`pliny-interrogation` — misnamed prior F6-E claimants**: trailing body corrected to name
   `pahc.force.martyrdom-meaning`, `pahc.gravity.martyrdom-meaning`, and `pahc.term.ministrae` —
   confirmed via direct grep that all three, and only these three plus
   `pahc.force.neronian-persecution` (not claimed in the note, consistent with the review's own
   suggested wording), actually carry `F6-E` in their own `canon_cells`. **CONFIRMED FIXED.**
9. **`two-ways-catechumen` — locus and dropped moral content**: `locus` now reads `"1:1-2; 2:1-4:14
   (the Way of Life's own moral inventory and almsgiving instruction); 5:1 (the Way of Death, by
   contrast); 7 (the baptismal instruction)"`. `text` now names the Way of Life's actual
   prohibitions and the almsgiving instruction. Both restored clauses checked fresh against the
   vendored edition: ch. 2 (`viii.iii.ii`) confirms the murder/adultery/pederasty/fornication/theft/
   magic/witchcraft/abortion/false-swearing/false-witness list; ch. 4 (`viii.iii.iv`) confirms
   `"thou shalt not turn away from him that is in want, but thou shalt share all things with thy
   brother."` A duplicated sentence introduced during drafting ("The Way of Death was laid out by
   contrast..." appearing twice) was caught and removed during this same fix pass. **CONFIRMED
   FIXED.**
10. **`pliny-interrogation` — dropped `ministrae` contested-reading caveat**: `text` now reads
    `"called ministrae (a term some read as a functional title, 'deaconesses,' though this reading
    is contested)"`. **CONFIRMED FIXED.**

**Post-fix full-battery checks:**
- YAML sweep (parse + `id`-matches-filename) across all `records/pahc/*/*.md`: clean.
- Full gate battery (`run_all` against all 13 gates, fleet records, full pahc world record set):
  `ALL GATES CLEAN` — reciprocity (world-wide, not type-restricted), canon-coverage,
  no-build-attribution, and all others report zero findings.
- `STORY-INDEX.md` regenerated: 13 stories, tier counts unchanged (Tier 1: 7, Tier 2: 0, Tier 3: 1,
  Tier 4: 5), 0 non-reciprocal relations, 0 Tier-5 stories.

All 7 substantive and 3 cosmetic findings confirmed fixed against live file content. No new issues
introduced. **Disposed — approved to proceed.**
