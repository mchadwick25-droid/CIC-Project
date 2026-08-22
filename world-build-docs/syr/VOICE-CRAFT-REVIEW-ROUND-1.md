# VOICE-CRAFT-REVIEW-ROUND-1 — Adversarial Review of `syr.voice.craft` (World #7, Step 5b/5d)

Reviewer: independent adversarial review thread (no part in authoring the record). Date: 2026-08-22.
Reviewed at commit `fc05dbd5` ("syr step 5b (draft, pre-review): voice_craft record"), working tree clean.

**Scope reviewed:** `records/syr/voice_craft/syr.voice.craft.md` — every compiled field (`identity`, `guard`, `characteristic_concerns[]`, `flavor_notes[].note`) and every substantive claim in its trailing body.

**Checked against:** `Redesign-Spec/CiC-Program-Spec.md` (O0–O7, the seven register statements at O2, §4.3 step 5 a–e, §5, §6); `Redesign-Spec/Artifact-1-Record-Schema.md` §4–§5; `engine/m1/schemas.py`, `engine/m1/gates.py` (`_ATTRIBUTION_FIELDS`, `gate_readability`, `FK_CEILING`), `engine/m1/fk.py`, `engine/m2/builders.py` (`build_prompt`'s real field contract); `fleet-voice/EXEMPLAR-TRANSCRIPT.md` on `origin/build/phase-1` (the governing v4 pronoun rule, read in full); the two prior worked models `alx.voice.craft` (`origin/world/alexandria`) and `pahc.craft.chloe-voice` + its Step 11 Round-1 review (`origin/claude/pahc-world-build-2oq764`); the fixture exemplar `fix.craft.vera-voice`; and this world's own approved corpus — `records/syr/world_core/syr.core.syriac.md`, all 6 `records/syr/gravity/*`, all 8 `records/syr/contested_claim/*`, all 18 `records/syr/quote/*`, all 9 `records/syr/term/*`, all 3 `records/syr/honest_limit/*`, `records/syr/source/syr.source.odes-of-solomon.md`, `records/syr/story/syr.story.simeon-martyrdom.md`, `records/syr/figure/syr.figure.aphrahat.md`, `records/worlds.yaml`, `world-build-docs/syr/SOURCE-REQUEST-MANIFEST.md`, `world-build-docs/syr/BUILD-LOG.md`, `world-build-docs/syr/LEGACY-PARTICIPANT-CARD-REFERENCE.md`, and commit `8b49ed48` (this world's own prior pronoun-rule correction). Nothing was taken on the record's own trailing-body word.

---

## Verdict — SUBSTANTIAL REVISION REQUIRED — 16 SUBSTANTIVE, 11 COSMETIC

Two things should be said before the findings, because they are the two things this step could most easily have gotten wrong, and it got both right.

**The single most important instruction of this build step is honored without a lapse.** Mar Yausep is never personified as a located individual with a biography. I checked this mechanically, not by impression: I parsed the record's YAML, extracted every compiled field, and regexed for first-person-singular tokens (`I`, `I'm`, `I've`, `I'll`, `I'd`, `my`, `me`, `mine`, `myself`). Three hits total, all inside quoted *rule examples* — `'I am a representative of Syriac Christianity'` and `'I am a teacher, not a judge'` in the self-reference note, and `That 'I' belongs to the one quoted` in the quotation note. Zero in `identity`, zero in `guard`, zero in any `characteristic_concern`. Beyond pronouns, `identity` carries four explicit anti-personification denials — "Yausep is not a biography," "He is not one located person," "No side is weighted as his own personal history," "No side is treated as foreign to him" — and that last pair is a direct, correct repair of the exact error Mark corrected on this world four commits earlier (`8b49ed48`: the "Persian-anchored (Aphrahat's side)" misreading). The frontier-biography failure mode did not happen.

**And the readability defect PAHC's own review caught did not recur.** `identity` scores **FK 6.7** (183 words, 15 sentences, 12.2 w/sentence); `guard` scores **FK 6.5** (111 words, 8 sentences, 13.9 w/sentence). PAHC's guard was FK 14.1 with a 65-word sentence. Nothing here is remotely that. `voice_craft` is correctly outside `gate_readability`'s scope, and it would pass comfortably if it were inside.

The gate battery is genuinely clean — I re-ran `gates.run_all()` over `load_world_records("syr")` + `load_fleet_records()` myself rather than trusting the record's own closing paragraph: **all thirteen gates return zero findings**, `no-build-attribution` included. The record's trailing claim on that point is correct.

But gates check structure, and every defect in this batch is in the three places gates cannot reach: **whether a compiled sentence is true against this world's own already-approved records; whether a compiled sentence stays inside the scope those records declared; and whether the capped voice layer is spending its cap on what the spec says it is for.** On all three, this record has real problems.

**Four findings are fabrication-class or caution-violating (O3; `syr.core.syriac` cautions 5 and 8) and should block sign-off on this step until corrected.** Finding 1 puts two self-authored source bodies into the compiled `Identity` section that do not exist anywhere in this world's 36 source records. Finding 12 licenses, in the compiled flavor notes, a quote category — "a martyr's own words" — that this corpus does not contain and that this build's own self-review already caught itself inventing once. Finding 9 generalizes the Persian side's persecution experience to the whole world, which `syr.core.syriac` caution 8 forbids in those words. Finding 3 tells the model, in the Guard it reads every turn, that this world's earliest witnesses *disagree* about Aphrahat's office — they do not; the earliest witness says he does not know.

The rest divides into: one scope narrowing that shrinks a six-gravity ecology to one gravity in the compiled Identity; three guard defects of honesty, exhaustiveness, and category (a modern vendoring gap voiced as a historical one); one guard omission of the two items this world's own step-5 handoff note explicitly reserved for this record; two characteristic-concern overclaims against their own gravity records' recorded findings; one structural inversion in which the per-world flavor budget is spent entirely on fleet-level register rules; one living-tradition conflation in the one line the voice is licensed to say about itself; and one build-sequence problem (5b delivered before 5a) with a now-stale registry comment.

---

## SUBSTANTIVE findings

### 1. `identity` — "the covenant order's own record" and "the persecuted Persian church's own memory" name self-authored source bodies this world does not have

**Field:** `identity` (compiled as the `## Identity` section — the model's own self-description on every turn).

> "He is drawn from Ephrem's hymnic corpus, from Aphrahat's dated Demonstrations, **from the covenant order's own record**, and **from the persecuted Persian church's own memory**, together."

**What I checked.** All 36 records under `records/syr/source/`. There is no source authored by the covenant order, and none authored by the Persian martyr-church.

- *The covenant order's own record.* `syr.contested.qyama-structure`'s own `concedes` field is explicit: *"the honest picture is a real institution whose inner constitution we mostly cannot see."* `syr.core.syriac.thinness` lists "the daughters of the covenant, whose singing is attested only through men's texts" among the world's structural silences, and `thin_topics` adds "the covenant order's existence and character are well attested; its formal internal structure is thinly and contestedly documented." `syr.limit.f5-women-own-words` states flatly: *"not one line written by one of them was kept."* The qyama is known **only** through Aphrahat addressing it (Dem. VI) and Ephrem writing about it. It left no record of its own. `SOURCE-REQUEST-MANIFEST.md` §3 confirms the nearest candidate is unusable: *"Liber Graduum: no PD English, and partly post-410 in final form — named for completeness per Doc_02 §1, not a founding source."*
- *The persecuted Persian church's own memory.* `SOURCE-REQUEST-MANIFEST.md` §3: *"**Persian martyr acts: no PD English**; Sozomen II.9–14 (vendored) is the narrative witness instead."* `syr.story.simeon-martyrdom` is sourced to `syr.source.sozomen-historia-ecclesiastica` II.9–10 — a fifth-century *Greek* ecclesiastical history written on the Roman side — and its own trailing body says the fuller Syriac acts are *"in copyright... consultable, never quoted."* The one genuinely Persian-side, in-window witness to the persecution is Aphrahat (Dem. V, XXI), and he is already named separately in the same sentence.

So of the four constituent bodies `identity` names, two are real (Ephrem, Aphrahat) and two are, as phrased, sources that do not exist. This is exactly the O3 failure the whole design exists to prevent — "the voice never invents a source" — and it sits in the highest-leverage compiled field there is. A model told it is "drawn from the covenant order's own record" has been given standing permission to speak as though a qyama-authored text were behind it.

**Severity: SUBSTANTIVE (fabrication-class).** Recommend rephrasing to what the corpus actually holds — e.g. "from what Aphrahat set down for the covenant order, and from how the Persian church's persecution was afterward remembered and written down" — so the mediation is audible rather than erased. Note that the fix must not simply delete the Persian clause: Aphrahat *is* a Persian-side in-window voice writing inside the persecution, and that is real; it is the words "own memory" that outrun it.

### 2. `identity` — the world is scoped as "this world's own whole covenant tradition," which narrows a six-gravity ecology to one of its six gravities

**Field:** `identity`, opening sentences; repeated in the trailing body ("a representative voice for this world's entire covenant tradition across its whole window").

> "Mar Yausep is a name and a role. They are given to **this world's own whole covenant tradition**."

**What I checked.** `syr.core.syriac.horizon` defines the world as *"The Syriac-speaking Christian ecology across the Roman-Persian Mesopotamian frontier, c. 200-410 CE."* `records/worlds.yaml` calls it "Syriac Christianity (Edessa/Nisibis)." The covenanted ascetic life (`syr.gravity.covenant-life`, C2) is **one** of six confirmed gravities, alongside raza/shrara method (C1, Primary), heresiological self-definition (C3), authority ambiguity (C4), Diatessaron normativity (C5), and persecution endurance (C6). Calling the whole world "the covenant tradition" makes C2 the name of the thing, which no approved record does.

This also looks like uncorrected residue from a superseded decision. `LEGACY-PARTICIPANT-CARD-REFERENCE.md` records the legacy role label as *"Mar Yausep, **Teacher of the Covenant Order**"* — and `BUILD-LOG.md` records that the role was subsequently *"revised Malpana->Deacon->Mar by Mark's own rulings,"* with `records/worlds.yaml` now carrying `role_label: Mar`. The role label dropped "of the Covenant Order"; the identity field's scope statement did not.

Compare the model this record is following: `alx.voice.craft.identity` scopes to *"the WHOLE Alexandrian-Egyptian formation ecology across the ENTIRE window."* Not to one of its gravities.

**Severity: SUBSTANTIVE (scope boundary).** The compiled Identity is the one place the world's own extent is declared to the model; it should name the ecology, not one gravity inside it.

### 3. `guard` — "Our own earliest witnesses disagree on both" is false for the Aphrahat half, and misdescribes silence as conflict

**Field:** `guard` (compiled as the `## Guard` section — read on every turn).

> "Two things we have never settled, and never claim to have settled: whether Aphrahat held a bishop's office, and in what year Jacob of Nisibis died. **Our own earliest witnesses disagree on both**, and we do not choose between them."

**What I checked.** `records/syr/contested_claim/syr.contested.aphrahat-episcopacy.md`, in full. Its `held_against` list says the opposite of "our earliest witnesses disagree":

> - "the argument rests on a narrow, largely **nineteenth-century** citation web: Wright's inference from Demonstration 14"
> - "**George of the Arabs, the tradition's own early witness, expressly disclaims certainty**"
> - "the **fourteenth-century** marginal note calling him 'bishop of Mar Mattai' is almost certainly anachronistic"
> - "no sustained twenty-first-century scholarly debate on the question was located — **claims of a 'live current debate' are themselves an overstatement**"

The shape of this uncertainty is: *the tradition never recorded it, its one early witness says he does not know, a much later marginal note guessed wrong, and a modern scholar inferred it from a document.* There is no disagreement among early witnesses to report — there is a silence, a disclaimer, an anachronism, and a modern inference. The guard converts all of that into a clean two-sided conflict, which is a more comfortable and more *quotable* state of the record than the one this world actually has. The final bullet is directly on point: this record already warns that the dispute is routinely overstated, and the guard overstates it in precisely the way warned against.

For the Jacob half the sentence is closer to true but still loose: `syr.contested.jacob-death-year` names the Chronicle of Edessa (sixth-century Syriac) for 338 against the **Chronicon Paschale** (seventh-century *Greek*, Byzantine) for 350. Neither is in-window, and one is not "ours" on any reading.

Compiled into the Guard, this instructs the model that it may say, in voice, that its own earliest witnesses disagree about whether Aphrahat was a bishop. That is an invented state of the record.

**Severity: SUBSTANTIVE (fabrication-adjacent; misstates a contested_claim record's own finding).** The honest form is nearer to: "our own tradition never recorded whether Aphrahat held a bishop's office, and the earliest witness who touches it says plainly that he does not know."

### 4. `guard` — "Two things we have never settled" reads as exhaustive and is false against this world's own corpus

**Field:** `guard`.

> "**Two things** we have never settled, and never claim to have settled..."

**What I checked.** `records/syr/contested_claim/` holds **eight** records: `aphrahat-episcopacy`, `bardaisan-nicene-floor`, `diatessaron-name`, `edessa-origins`, `jacob-death-year`, `papa-primacy`, `qyama-structure`, `rabbula-peshitta`. `syr.core.syriac` caution 10 alone holds **two dates** open, not one: *"Jacob of Nisibis's death year (338 vs 350...) **and Simeon bar Sabbae's martyrdom year (341 vs c. 344, with every chronicle date chained to it)** stay open."* Caution 3 holds the authority-structure question open *"in both directions"* — Aphrahat's office **and** how settled the hierarchy under Papa was.

A guard whose entire purpose is honest thinness should not enumerate this world's unsettled questions in a way that undercounts them by six. In a field the model reads as its standing self-instruction, "two things we have never settled" is a closed set, and a model that has internalized a closed set of two is worse-positioned on the other six than it would be with no list at all.

**Severity: SUBSTANTIVE (understates the record's own uncertainty in the field whose job is honesty about it).** If a list is kept at all, it needs "two of the questions," not "two things."

### 5. `guard` — the Odes sentence voices a modern rights/vendoring gap as a statement about this world's own record

**Field:** `guard`, closing three sentences.

> "A hymnbook some hold to be ours, the Odes of Solomon, is disputed even by those who study it closely. **We do not yet have it to quote from directly.** We say so, rather than borrow its words as though we did."

**What I checked.** `records/syr/source/syr.source.odes-of-solomon.md` and `SOURCE-REQUEST-MANIFEST.md` §2.1.

The source record's own `work` field lists the surviving witnesses: *"the Harris Syriac ms., BL Add. 14538, Greek P.Bodmer XI for Ode 11, Coptic quotations in the Pistis Sophia."* The text **survives**. What does not exist is a vendored file: `edition` reads *"J. Rendel Harris's editio princeps translation (1909; 2nd ed. 1911) is the expected public-domain English — **NOT VENDORED: no file with its own provenance header has been supplied**"*; `rights_status` reads *"pending-verification... the rights gate fails closed: NO verbatim quoting from the Odes until then."* §2.1's status line: *"Mark could not locate a copy on hand. Logged as future work — pick up whenever a copy surfaces."*

So "we do not yet have it to quote from directly" is true of **this build's file cabinet in August 2026**, and false of this world's record, which has the Odes. The word "yet" makes the reading unavoidable: it points at a future acquisition. And "borrow its words as though we did" presupposes the words are there to borrow.

This is a category collapse, and a consequential one. The two sentences before it are genuine historical unknowns; this one is a modern licensing status. Putting them in one "we" teaches the model that a rights gate and a gap in the historical record are the same kind of thing, in the one field that exists to keep the voice honest about exactly that distinction. Contrast how this world's own `honest_limit` records do it correctly — `syr.limit.f5-enslaved`: *"No enslaved person of this world left a word that was kept"* — a statement about what survives, not about what has been acquired.

**Severity: SUBSTANTIVE (build-process fact voiced as in-world fact; O3 register).** The defensible in-voice content here is the *provenance* dispute ("some hold this hymnbook to be ours; whether it is, and when and in what tongue it was made, are all disputed"). The non-quoting is a rights-gate fact and belongs in the source record, where it already is, not in the Representative's mouth.

### 6. Trailing body — the three guard items are called "load-bearing," and two of the three records cited say in terms that they are not

**Trailing body:**

> "These are **the load-bearing**, already-flagged honest limits this world's own build has surfaced repeatedly - the natural candidates for 'at most a line or two where a world's measured failure demands it' beyond the one fleet floor line, per the governing spec."

**What I checked.** The two records the sentence points at contradict it directly.

- `syr.source.odes-of-solomon.attribution_status`: *"Confidence D in the legacy registry — **no specific claim rests on the Odes alone**."* Its trailing body: *"**nothing load-bearing rests on the Odes**, and the vendoring request is OPEN with Mark."* `SOURCE-REQUEST-MANIFEST.md` §2.1 says the same twice — *"nothing load-bearing rests on them"* and *"not required for this world to proceed through step 6/7/8 later, since nothing here is load-bearing on the Odes"* — and §5 classifies it as *"future work, not open decisions... neither blocks this world's progress."*
- `syr.contested.jacob-death-year` carries `canon_cells: []` with its own explanation: *"a dating question with **no participant-facing cell**; the figure and story records carry the honest hedge,"* and its trailing body defers resolution *"if the date **ever becomes** load-bearing."* Both formulations state that it currently is not.

Only the Aphrahat-episcopacy item has a real claim on "load-bearing" — it carries `canon_cells: [F3-I]` and feeds a Tensional gravity.

**Severity: SUBSTANTIVE (the stated justification for two-thirds of the guard's per-world content is contradicted by the records it cites).**

### 7. `guard` — three stacked per-world topics, 111 words, against a cap of "at most a line or two where a world's *measured* failure demands it," with no measurement yet performed

**Field:** `guard`.

**What I checked.** Spec §4.3 step 5: *"The guard is the one fleet floor line (honest thinness over invented depth, absolutely) **plus at most a line or two where a world's measured failure demands it**,"* under the same bullet that forbids *"trait rubrics, avoid-trait catalogs, [and] stacked per-world rules."*

Measured against the fleet:

| record | guard | words | per-world topics added |
|---|---|---|---|
| `alx.voice.craft` | floor line only | 6 | 0 |
| `fix.craft.vera-voice` | floor line only, with the cap cited | ~24 | 0 |
| `pahc.craft.chloe-voice` | floor line + Ignatius single-voice dependency | ~100 | 1 |
| **`syr.voice.craft`** | floor line + Aphrahat's office + Jacob's death year + the Odes | **111** | **3** |

This is the longest guard in the fleet and the only one that stacks three separate per-world rules. Note also that PAHC signposts its single addition against the cap — *"One line further, where our own record's own measured thinness demands it"* — and this record drops that signposting and simply continues.

Separately: there is **no measured failure** to demand any of it. `BUILD-LOG.md`'s stopping point and this record's own body both confirm demonstrations (5c) and voice validation (5e) are not built. Nothing has been run, so nothing has been measured. The guard additions are pre-emptive by construction.

**Severity: SUBSTANTIVE (spec cap exceeded; the cap's own precondition is not met).** Recommend the guard be cut back to the floor line plus at most the one item with a real participant-facing cell behind it (Aphrahat's office), and revisited after 5e produces an actual measurement.

### 8. The craft record omits both items this world's own step-5 handoff note explicitly reserved for it — including the world's most safety-sensitive caution

**Fields:** `guard`, `flavor_notes[]` (by omission).

**What I checked.** `LEGACY-PARTICIPANT-CARD-REFERENCE.md`, "What this settles" section:

> "**Safety-relevant: the anti-Jewish polemical material's sensitivity and a flagged pastoral-warmth/dependency-amplifier risk — both worth carrying into step 5's craft record** and M5's safety design when that work begins."

Neither appears anywhere in this record. Meanwhile `syr.core.syriac` caution 4 is one of the sharpest cautions in the whole world_core:

> "The ANTI-JEWISH material (roughly four of Aphrahat's Demonstrations, with strands in Ephrem) is **entirely one-sided**: no Jewish counterpart survives and no internal Christian dissent from it is attested — **state that one-sidedness plainly, and never invent balancing voices**."

The corpus holds a `do-not-voice`-licensed quote for exactly this material (`syr.quote.aphrahat-anti-jewish-frame`) and a `thin_topics` entry for it. This is the one place in this world where a voice can do real harm, and the one place where "never invent balancing voices" is a live fabrication pressure with a specific shape. It is also, notably, the item the world's own handoff note named *by name* for this record.

The guard spends 111 words on two dating disputes and an unacquired hymnbook, and zero on this.

**Severity: SUBSTANTIVE (omission of the flagged item; misallocation of the guard's whole per-world budget).** If any world's "measured failure" justifies a guard line, this is the candidate — and it is the one this world's own documents already nominated.

### 9. `characteristic_concerns[4]` — the Persian side's persecution is generalized to the whole world, which `world_core` caution 8 forbids in those words

**Field:** `characteristic_concerns[4]`.

> "what endurance under a hostile crown cost, and what it did not undo"

**What I checked.** `syr.core.syriac` caution 8:

> "**PERSECUTION ASYMMETRY:** sustained state persecution (Shapur II, from the 340s) is the Persian side's experience; **Roman-side Edessa's window is largely without it — never generalize either side's experience to the whole world.**"

`syr.gravity.persecution-endurance` repeats it in its own `description`: *"**This is the Persian context's gravity**: Roman-side Edessa's window knows doctrinal rivalry, not sustained state persecution — **the asymmetry is never generalized away**."* The gravity is classified SUPPORTING, not Primary, *"Persian-concentrated - HIGH Author Gravity flagged at generation."*

`characteristic_concerns` compiles into a bare bullet list under `## Characteristic concerns` with no qualifiers available. As written, this bullet tells the model that endurance under a hostile crown is a characteristic concern of the world — the whole world, both sides, the whole window — which is the generalization caution 8 prohibits. The collision is sharpened by `identity` two fields above, which insists the voice speaks for "the Roman side and the Persian side both" and that "no side is weighted." One field says both sides equally; the next lists one side's defining experience as the world's own.

**Severity: SUBSTANTIVE (violates a named `world_core` caution and its gravity record's own scope statement).** The bullet needs the asymmetry inside it — e.g. "what endurance under a hostile crown cost on the Persian side, and what it did not undo."

### 10. `characteristic_concerns[3]` — C4's *modern reconstruction* ambiguity is presented as a lived concern of the world, which its gravity record records a FORMATION TEST **FAIL** on

**Field:** `characteristic_concerns[3]`.

> "who may be trusted to lead, and how unsettled that trust has stayed"

**What I checked.** `syr.gravity.authority-ambiguity` (C4, Tensional). Its `description` closes: *"The ambiguity is a documented condition of the record; **how it was LIVED is much thinner - a reconstruction gap named, not filled**."* Its trailing body is blunter:

> "The honest test record is carried: **FORMATION TEST FAIL** (the evidence speaks to **modern reconstruction difficulty, not to how the ambiguity was lived** - Round 2's refusal to soften a fail into a 'weak pass'), and the sharpest Confidence/Gravity Cross-Check divergence in the set: underlying facts Widely Accepted-to-Documented, **lived-experience claim Contested/Inferential-Thin - stated, never resolved by upgrading.**"

A "characteristic concern" is, by the field's own name and by how `build_prompt` compiles it, a claim about what this world *characteristically concerned itself with* — a lived-experience claim. That is precisely the claim C4 failed its formation test on, and precisely the upgrade Doc_04 Round 2 refused. This bullet performs the upgrade the gravity record spent a review round refusing.

The same record's own caution about not fabricating relations ("Recording a tension-with here would fabricate a relation the approved Doc_04 never mapped") shows how carefully this boundary was policed upstream. It is not being policed here.

**Severity: SUBSTANTIVE (upgrades a recorded formation-test FAIL into a compiled lived-experience claim).** If C4 is to be represented at all in this list, it has to be as what the record supports — that leadership ran on two footings at once and the record never resolves which held — not as a concern the world is asserted to have carried.

### 11. `characteristic_concerns[2]` — "the boundary **they** made necessary" reverses `world_core` caution 5 and C3's own finding

**Field:** `characteristic_concerns[2]`.

> "the named rivals answered by name - Bardaisan, Marcion, Mani - and the boundary **they made necessary**"

**What I checked.** `syr.core.syriac` caution 5:

> "**HERESIOLOGY SCREEN:** Ephrem's Marcion-Bardaisan-Mani triad is **boundary-building polemic that flattens three distinct systems**; it must not be read as neutral description."

`syr.gravity.heresiological-self-definition` (C3) says the same from the other side: *"The boundary is **substantially Ephrem's own rhetorical achievement** — built in the Prose Refutations, the heresy-hymns, and the very choice of the sung madrasha as the weapon — and **his triad flattens three distinct systems into one 'deception'**. Ephrem-concentrated: **Aphrahat never engages the triad by name**."* HIGH Author Gravity is flagged at generation, citing Ruani on *"Ephrem as founder of Syriac heresiology; his rhetoric **CONSTRUCTS** the boundary."*

"The boundary they made necessary" attributes the necessity to the rivals. Both records attribute the boundary to Ephrem's construction of it. The bullet adopts the polemic's own account of itself — which is the single thing caution 5 exists to stop — and does so in a compiled field, unqualified, with the Ephrem-concentration silently dropped (Aphrahat, half of this world's two anchor voices, never engages the triad at all).

Note that listing Bardaisan among "the named rivals answered" is itself correct and does not conflict with caution 1 (Named Comparandum, never a founding voice) — the problem is only "made necessary."

**Severity: SUBSTANTIVE (takes the polemic's side against a named caution).** "the boundary Ephrem built by answering them" would be true to both records.

### 12. `flavor_notes[quotation]` — "a martyr's own words" licenses a quote category this corpus does not contain, in the exact place this build already caught itself inventing one

**Field:** `flavor_notes[quotation].note` (compiled under `## Flavor notes`).

> "A named, sourced quote keeps its own first person exactly as given - Ephrem's own words, Aphrahat's own words, **a martyr's own words**."

**What I checked.** All 18 records under `records/syr/quote/`, by `speaker_or_author`:

| speaker | count |
|---|---|
| `syr.figure.aphrahat` | 7 (one `license: do-not-voice`) |
| `syr.figure.ephrem` | 5 |
| `syr.figure.bardaisan` | 1 (mediated, comparandum) |
| Chronicle of Edessa (anonymous chronicler) | 1 |
| Doctrine of Addai (the legend speaking) | 1 |
| Palladius / Sozomen / Theodoret (later outside witnesses) | 3 |

**There is not one martyr quote in this world.** Two of the three named examples in the note are real and abundant; the third names a category with zero records behind it.

This is not a hypothetical risk on this world. Three independent pieces of evidence converge:

1. `SOURCE-REQUEST-MANIFEST.md` §3: *"Persian martyr acts: **no PD English**; Sozomen II.9–14 (vendored) is the narrative witness instead."*
2. `syr.story.simeon-martyrdom.absent_detail`: *"**The exact words of the royal audiences**, the precise sequence, and the companions' speeches **are the hagiographic tradition's own shaping, not verified reporting**."* Its `retrieval.do_not_retrieve_when` names *"improvised scenes for the other named martyrs,"* and its trailing body carries the standing guard: *"the other named martyrs (Shahdost, Barba'shmin, Milles and the rest) have **NO comparable narratives available - no scenes may be improvised for them by analogy**."*
3. `BUILD-LOG.md`, "Verification discipline applied": *"two claims found to outrun the vendored attestation during self-review (a trinitarian-formula phrasing; a baptismal-imagery phrasing; **an unattested Simeon paraphrase**) were corrected to exactly-attested content before review."*

So this build has already, once, generated words for this world's martyr that the sources do not support, caught it in self-review, and removed it. The craft record now compiles an instruction naming "a martyr's own words" as a thing the voice quotes.

**Severity: SUBSTANTIVE (fabrication-class; actively invites the failure this build already committed once).** The example list should name only categories with records behind them.

### 13. `flavor_notes[quotation]` — the "unusually rich / leans unusually heavily" claim does not survive being counted

**Field:** `flavor_notes[quotation].note`, and the trailing body's justification for it.

> note: "This world's record is **unusually rich** in exactly this kind of **dated, attributed** speech..."
> body: "...because this world's answer canon **leans unusually heavily on named, dated, verbatim quotation** (18 quote records: Ephrem, Aphrahat, the Chronicle of Edessa, Bardaisan's own dialogue as comparandum) - worth stating explicitly rather than leaving implicit, per the project lead's own direct instruction this build step."

**What I checked.** Counted the built fleet by record type (`git ls-tree -r --name-only` on each world's branch):

| world | quote records | total records | quotes as share |
|---|---|---|---|
| alx | 14 | 137 | 10.2% |
| **syr** | **18** | **150** | **12.0%** |
| pahc | 6 | 137 | 4.4% |

Against the only comparable full world build, syr is 1.8 percentage points higher. That is not "unusually heavily" — it is normal for a world built to this shape.

"**Dated**" fares worse. Aphrahat's Demonstrations are genuinely dated (`syr.figure.aphrahat.dates.floruit`: *"Demonstrations 1-10 dated 336/337; 11-22 dated 344; 23 dated August 345"*) and the Chronicle entries carry Seleucid years — roughly **8 of 18**. Ephrem's five hymn quotations are not individually dated; the Abgar letter is legend by `syr.core.syriac` caution 2; and Palladius, Sozomen and Theodoret are later, non-Syriac, outside-window witnesses. The body's own enumeration silently accounts for only 14 of the 18 and omits the 4 least like "this world's own named, dated speech."

Two further problems with putting this in a compiled field at all. First, "unusually" is a *cross-world comparative* — a build-frame judgment not derivable from inside the world, in a per-world layer the spec scopes to content and light flavor (O4). Second, telling a model on every turn that its supply of dated attributed quotation is unusually rich is mild but real fabrication pressure toward reaching for quotations, and it is compiled in the same note as finding 12's phantom martyr.

**Severity: SUBSTANTIVE (the stated basis for adding a per-world note is not true as stated).** The underlying discipline — a named quote keeps its own "I" — is correct and worth keeping; only the "unusually rich" framing needs to go.

### 14. `flavor_notes[]` — the per-world flavor budget is spent entirely on fleet-level register rules; this world gets no distinguishing flavor at all

**Field:** `flavor_notes[]`, as a set.

**What I checked.** Spec §4.3 step 5 divides the labor explicitly:

> "**One fleet voice.** All Representatives share the modern General/Seeker register (the exemplar, the seven statements), **written once and maintained once**. Content comes out of the world; **the register does not.**
> **Light flavor.** A handful of natural touches per world — **a word introduced after its plain meaning, a place, a way of referring to things** — never an attempted ancient sound. The craft record is capped... **No trait rubrics, no avoid-trait catalogs, no stacked per-world rules — rule-stacks stiffen the conversation and cost prompt tokens on every turn.**"

The four notes delivered:

| segment | tag | what it actually is |
|---|---|---|
| term-introduction | plain-before-native | register (O2 statement 4) — but the only one with real world content in it |
| self-reference | stance | **fleet pronoun rule**, restated |
| quotation | named-voice-kept | **fleet rule** (exemplar v2/v4), restated |
| honest-limits | stance | **fleet rule** (O2 statement 5 / alx), restated near-verbatim |

Not one note is tagged `flavor`. There is no "a place." Compare `alx.voice.craft`, which carries a `place` note — *"The city concrete and light: the harbor, the lecture room, the villages up the river"* — and `pahc.craft.chloe-voice`, which carries three world-content notes (`correspondence`/letter-as-proof, `leadership`/unresolved-authority, `table`/table-as-belonging).

This world has conspicuous, cheap flavor available and takes none of it: Edessa's own flood-destroyed church building, the frontier city changing empires mid-window (Nisibis ceded 363), the choirs of the daughters of the covenant singing the teaching, the pearl held up to the light, the sung madrasha as argument. O4 says worlds sound like themselves through their content and light flavor. As delivered, this voice layer would sound exactly like Alexandria's minus Alexandria's place note.

The record's own body concedes the core of this — *"this is a fleet-level rule, not a syr-local invention"* — and justifies restating it because *"Artifact-2's compiler reads voice_craft field by field per world."* I verified that `build_prompt()` does read voice_craft field by field, so the mechanism claim is true; but "the compiler is per-world" is an argument for putting fleet rules in the *fleet* layer, not for copying three of them into every world's capped budget and paying for them on every turn of every world. That is the rule-stacking and token cost the cap names.

**Severity: SUBSTANTIVE (structural; inverts the spec's own fleet/world division and leaves O4 distinctness unserved).**

### 15. `flavor_notes[self-reference]` — the sanctioned self-naming line claims the living tradition, not the bounded world

**Field:** `flavor_notes[self-reference].note`.

> "ONE sanctioned exception: '**I am a representative of Syriac Christianity**.'"

**What I checked.** `records/worlds.yaml` for `syr`: `display_name: "Syriac Christianity (Edessa/Nisibis)"`, `time_window: {start: 200, end: 410}`, and — decisively — **`living_tradition_flag: true`**, with the comment: *"the Syriac churches — Church of the East, Syriac Orthodox, Eastern Catholic heirs — are living heirs."* Spec §6 requires the doorway to carry, for exactly these worlds, *"the living-tradition distinction where flagged ('this is a bounded historical reconstruction, not today's church of the same name')."*

The one line this voice is licensed to say about itself therefore claims, unqualified, to be a representative of a tradition that has living heirs today. `alx.voice.craft`'s equivalent is "I am a representative of Alexandria" — a place, bounded, with no living claimant of the name. The parenthetical half of this world's own display name, "(Edessa/Nisibis)", is exactly the bounding the line drops.

**Severity: SUBSTANTIVE (living-tradition conflation in the single highest-visibility self-naming line, on a world where the flag is set true).**

### 16. Build sequence — 5b/5d were built before 5a's identity-emergence rationale, which both the registry and the build log record as still owed; and the registry's own `state` comment is now stale

**Files:** `records/worlds.yaml` (syr entry), `world-build-docs/syr/BUILD-LOG.md`, and this record's trailing body.

**What I checked.** Spec §4.3 step 5 orders the sub-steps: *"(a) identity emergence from the records, **rationale written — Mark's checkpoint**; the name and role are the only sanctioned fabrications; (b) the small craft record..."*

Both of this world's own tracking documents say (a) has not happened. `records/worlds.yaml`, syr `representative` comment: *"**Step 5a's full identity-emergence write-up (rationale derived from the completed records) is still owed** when the voice build begins; this confirmation settles the name/role themselves, not that remaining paperwork."* `BUILD-LOG.md` "Escalation check" repeats it verbatim. I searched `world-build-docs/syr/` and `records/syr/` for any such write-up: none exists.

The craft record's trailing body enumerates the sub-steps and **omits (a) entirely**: *"This is the small craft record only (**sub-step b/d**); demonstrations (**sub-step c**) and voice validation (**sub-step e**) are not built at this step."* Every sub-step is accounted for except the missing one.

This is not bookkeeping. `LEGACY-PARTICIPANT-CARD-REFERENCE.md` reserved a specific question for 5a: *"Whether 'anchor' survives under the new spec as some non-individual sense — e.g. a compositional emphasis in which sources get cited more often, or nothing at all — **is a step-5a question to work out fresh from this build's own completed records**, not an inherited constraint."* `identity` now answers it — "No side is weighted as his own personal history" — which I think is the *right* answer, but it has been decided inside the craft record with no rationale written and no checkpoint taken.

Related and separately fixable: the registry's `state` comment now contradicts the delivered artifact — *"state: building # steps 2-4 in progress on this branch (source ecology, lexicon, ecology reconstruction, answer canon); **no voice build**, no compile, no admission."* A voice_craft record now exists. (Same class as the stale-registry finding in the PAHC precedent review.)

**Severity: SUBSTANTIVE (sequence; a Mark checkpoint bypassed, and the bypass not disclosed in the record's own account of what it is).**

---

## COSMETIC findings

### C1. `flavor_notes[term-introduction]` — the raza gloss conflates raza with shrara, in the one note whose subject is glossing accurately

> "names a thing in plain English first. **The truth a story secretly carries.** The vowed order. The one woven Gospel."

`syr.term.raza-shrara.plain_meaning`: *"Symbol and truth, held as one pair. **A raza is a thing in Scripture or in nature that shows a hidden truth - the shrara.**"* The raza is the **symbol**; the shrara is the truth. The offered plain-English gloss names only the truth-half, calls it what the pair is, narrows "a thing in Scripture or in nature" to "a story," and adds "secretly," which nothing in the term record or `world_core.formation_logic` supports ("hidden" is the term record's word, and it modifies the truth's *power*, not the manner of carrying). The other two examples are exact: "The vowed order" matches `syr.term.qyama` word for word, and "The one woven Gospel" matches `syr.term.ewangeliyon-da-mhallete.quick_meaning`.

### C2. `characteristic_concerns[0]` leads with the native word before the plain meaning

> "**reading by raza** - what a story or symbol truly carries, not only what it says on its surface"

Native word first, gloss after the dash — the reverse of O2 statement 4 and of the plain-before-native note compiled two sections below it. `alx` and `pahc` both keep their concern bullets in plain English throughout.

### C3. `identity` — one 26-word, four-clause sentence at FK 15.9 (register statement 3)

> "He is drawn from Ephrem's hymnic corpus, from Aphrahat's dated Demonstrations, from the covenant order's own record, and from the persecuted Persian church's own memory, together."

The field as a whole is FK 6.7 and needs no rescue; this one sentence stacks four parallel prepositional clauses and is the only outlier. It is the same sentence as finding 1, so it will be rewritten anyway.

### C4. `identity` — the approved three-part geography is compressed to two

> "Edessa to Nisibis, the Roman side and the Persian side both"

`syr.core.syriac.horizon` and `records/worlds.yaml` both carry three elements: Edessa, Nisibis, and the Persian-side communities / "Persian Adiabene" (`syr.figure.aphrahat.dates`: *"traditionally associated with the Adiabene region"*). Dropping the third sits oddly beside the claim in the same sentence to speak for the Persian side.

### C5. Trailing body — "five confirmed gravities"; there are six

> "characteristic_concerns are drawn directly from this world's **five confirmed gravities** (records/syr/gravity/)"

`records/syr/gravity/` holds six records, and `BUILD-LOG.md` counts "6 gravity." The sentence goes on to name C5 separately, so the intent is clear, but the stated count of the world's own confirmed gravities is wrong.

### C6. Trailing body — the claim that C5 is "folded into the raza-shrara line" is not true of the delivered text

> "the Diatessaron gravity (C5) is **folded into the raza-shrara line above it** rather than given its own bullet"

`characteristic_concerns[0]` reads "reading by raza - what a story or symbol truly carries, not only what it says on its surface." It contains nothing about the Gospel, the harmony, or narrative unity. The Diatessaron does appear in the voice layer — as "The one woven Gospel" in the term-introduction flavor note — but not where the body says it is.

### C7. Trailing body — "restates the fleet pronoun rule verbatim in substance... matching wording" overstates the fidelity

Compared word-for-word against `fleet-voice/EXEMPLAR-TRANSCRIPT.md` v4 and `alx.voice.craft`'s self-reference note, three elements are dropped: the **paired-example contrast** that carries the rule's sharpest edge (*"'I am a representative... not here to judge' is sanctioned; 'I am a teacher, not a judge' is not"* — the syr note keeps only the negative half); the scoping to **identity-collision cells**; and **"never a recurring habit."** The compression is defensible on its own terms and the rule's substance survives, but "verbatim in substance... matching wording" is not what was delivered. (See "Checked and found sound" for what the note does get right.)

### C8. Build/architecture vocabulary in compiled fields — has precedent, needs a fleet-level decision rather than a silent per-world one

Three instances, all in text a live model reads as its own instructions: `identity`'s *"the only sanctioned fabrications **this build** allows"*; `guard`'s opening *"**The one fleet floor line**, absolutely"*; and the term-introduction note's *"this world's own **term records** lead with **plain_meaning** before **world_word**"* (schema field names, verbatim). `gate_no_build_attribution` does not fire on any of them and is not designed to — its three patterns are ISO dates, "ruled by," and stale working-scope markers. All three have direct `pahc.craft.chloe-voice` precedent and one has `fix.craft.vera-voice` precedent, so this is not a syr defect; flagging it so the decision is deliberate rather than inherited, the same disposition REVIEW-ROUND-1 finding 6 took on the adjacent-field process language.

### C9. `sources: []` alongside `verification_state: verified-via-authority`

With an empty `sources` list, "verified-via-authority" names no authority. `alx.voice.craft` carries the identical combination and `gate_confidence_crosscheck` passes, so this is fleet-consistent; noted only because `pahc.craft.chloe-voice` does carry a real source entry, so the fleet is not actually of one mind here.

### C10. The role label "Mar" carries clerical freight in a world whose authority structure is deliberately open — flagged, not for this review to resolve

`syr.term.mar.plain_meaning`: *"Mar means 'my lord'. It is the Syriac title of honor set before the names of **bishops, saints, and revered teachers**."* `syr.core.syriac` caution 3 holds the authority-structure question open in both directions, and this record's own guard says the world never settled whether Aphrahat held a bishop's office. Attaching a bishops-and-saints honorific to the composite voice quietly implies a standing the world's records decline to assert about anyone. **Not a finding against this record:** name and role are Mark's per-world touchpoint (spec §4.3, "Mark's per-world touchpoints"), confirmed 2026-08-22 and carried in `records/worlds.yaml`. Raised the way the PAHC precedent review raised its upstream Identity-Decision problem — flagged for the lead, not edited by a build or review thread.

### C11. Trailing body — three appeals to unverifiable chat instruction stand in place of record citations

*"per the project lead's own explicit instruction at this build step"* (identity), *"per the project lead's own direct instruction this build step"* (quotation note), *"the three genuine thinness/contest points the project lead named directly this build step"* (guard). I cannot verify chat, and I make no finding about whether these instructions were given. What I can say is that in all three cases the *records cited alongside* the appeal do not support the compiled text (findings 6, 12, 13), and that the appeal is doing the load-bearing work. Recording it so the lead can confirm or correct what was actually asked for.

---

## Checked and found sound

A re-reviewer does not need to redo any of the following. Each was verified directly against the named artifact, not against the record's own account of itself.

**The whole-world / no-biography discipline — the single most important check.**
- Regexed all 12 compiled field values for `I`, `I'm`, `I've`, `I'll`, `I'd`, `my`, `me`, `mine`, `myself`. Three hits, all inside quoted rule examples in the self-reference and quotation notes. **Zero** in `identity`, **zero** in `guard`, **zero** in all five `characteristic_concerns`.
- Read `identity` clause by clause for any phrasing that would locate Yausep as an individual — birth, upbringing, "lived through," one side of the frontier as personal experience, a personal encounter, a room, a year. **None.** The four explicit denials are present and correctly placed: "Yausep is not a biography," "He is not one located person," "No side is weighted as his own personal history," "No side is treated as foreign to him."
- The last two are a direct and correct repair of the error Mark corrected on this world in commit `8b49ed48` (the "Persian-anchored (Aphrahat's side)" misreading that would have made Ephrem's material foreign and Aphrahat's material lived). Also correct against the fleet's own v3→v4 correction. Ephrem's and Aphrahat's material are treated symmetrically throughout.
- Third-person "he/his" for the persona in a *descriptive* field matches `pahc.craft.chloe-voice`'s use of "she/her" and is not the voice speaking.

**The v4 pronoun rule's substance.** Compared clause by clause against `fleet-voice/EXEMPLAR-TRANSCRIPT.md` on `origin/build/phase-1`, "The pronoun rule — four revisions" section. All six load-bearing elements are present and correctly stated: (1) strict we-voice always; (2) covering the world's own content **and** the voice's present-tense conversational acts alike, with the exemplar's own examples ("we must be honest," "we will not invent"); (3) exactly **one** sanctioned exception; (4) it is a naming of what the voice literally is, not an in-world role, with "I am a teacher, not a judge" named as unsanctioned and the reason given ("personifies"); (5) at most once per turn; (6) only when the participant's own question is directly about the voice's nature or judgment. C7 above records the three secondary elements dropped in compression; the rule itself is not misstated. The named-quote carve-out is correctly stated in a separate note ("That 'I' belongs to the one quoted, never to the voice itself") and correctly matches the exemplar's v2-through-v4 continuous rule.

**`gate_no_build_attribution` — the record's zero-findings claim is correct, independently re-verified.** I did not trust the closing paragraph. I re-ran `engine.m1.gates.run_all()` over `load_world_records("syr")` + `load_fleet_records()` + `records/worlds.yaml`: **all 13 gates, 0 findings.** I also re-implemented the three patterns (`_ISO_DATE`, `_RULED_BY`, `_STALE_STATUS`) independently and scanned `identity`, `guard`, every `flavor_notes[].note`, and every `characteristic_concerns[]` entry — the exact scope `_ATTRIBUTION_FIELDS["voice_craft"]` plus the two special-cased list fields. Zero hits. The record's description of that scope ("identity, guard, or the flavor_notes/characteristic_concerns fields gate_no_build_attribution actually scans for this record type") is also accurate against `engine/m1/gates.py` lines 247–333. C8 records the residual build-vocabulary that these patterns are not designed to catch.

**Readability (register statements 1–3, applied conceptually — `voice_craft` is correctly outside `gate_readability`'s scope, which covers only `term.quick_meaning`, `term.plain_meaning`, and `honest_limit.statement`).** Computed with `engine.m1.fk.fk_grade`: `identity` **FK 6.7** / 12.2 words per sentence; `guard` **FK 6.5** / 13.9 w/s; term-introduction 4.5, self-reference 7.6, quotation 9.3, honest-limits 5.6. No field approaches FK 10, let alone the FK 14.1 / 65-word-sentence defect the PAHC review caught. C3 records the single 26-word outlier sentence. Sentence architecture is otherwise short and clean throughout.

**Registry consistency (name and role).** `records/worlds.yaml` syr: `representative: {name: Yausep, role_label: Mar}`. The record uses "Mar Yausep" and never self-names in any other form. Match confirmed. The persona-provenance disclosure sentence is present and follows the established pattern — compared against `fix.craft.vera-voice` (*"name and role are the only sanctioned fabrications (spec principle 14)"*) and `pahc.craft.chloe-voice` (*"Her name and role are the only sanctioned fabrications this build allows; every quote and claim behind them belongs to this world's own surviving voices"*). syr's is a faithful adaptation, and the fixture-exemplar omission that PAHC's own review had to fix does not recur here. (Finding 16 records the separate, unrelated registry `state` staleness.)

**Window and geography against `world_core` and the registry.** "c. 200-410 CE" matches `syr.core.syriac.time_window {start: 200, end: 410}` and the registry exactly. "the Roman side and the Persian side both" matches the horizon. Formatted "c. 200-410 CE" in the world's own house style, not ISO. (C4 records the dropped third geographic element.)

**Doc_01/Doc_02 settled findings, checked individually.**
- **Strand-singular** (Doc_01 §6, one ecology, not two): honored, and honored well. "No side is weighted as his own personal history. No side is treated as foreign to him." No contradiction anywhere in the record.
- **Bardaisan as Named Comparandum, never a founding voice** (caution 1): honored. `characteristic_concerns[2]` lists him among rivals *answered*, never as a source of the world's own faith. `syr.quote.blc-one-name`'s own comparandum discipline is not undercut. (Finding 11 concerns "made necessary," a different problem in the same bullet.)
- **No post-410 smear** (caution 7): clean. No "Catholicos," no "School of Nisibis." Window correctly closed at 410.
- **The Ephrem malpana / choir-leadership overclaim** (caution 9, removed post-approval 2026-07-08): clean. Ephrem appears only as "Ephrem's hymnic corpus." No claim of personal choir leadership anywhere.
- **Jacob of Nisibis's death year held open** (caution 10): the guard states it as open and picks no side. Correct as far as it goes; findings 3, 4 and 6 concern the surrounding framing, not the holding-open itself.
- **Abgar/Addai as the community's self-understanding, not origin fact** (caution 2): not touched by this record; no contradiction introduced.

**`characteristic_concerns[0]` and `[1]` trace cleanly.**
- `[0]` "reading by raza — what a story or symbol truly carries, not only what it says on its surface" → `syr.gravity.raza-shrara-method` (C1, Primary). Substantively accurate to the gravity's `description` and to `syr.term.raza-shrara`. (C2 records the native-word-first ordering; C1 records a different, related gloss problem in the flavor note.)
- `[1]` "the covenant kept for a whole life, in the middle of an ordinary town, not away from it" → `syr.gravity.covenant-life` (C2, Primary). Excellent — matches the gravity's *"remain inside the town congregation"* and `syr.term.qyama`'s *"they did not leave for the desert. They stayed in town"* precisely, in plain English, with the desert-monasticism false friend correctly excluded.

**Record ids and statuses cited by the trailing body all exist and say what is claimed of their existence.** `syr.contested.aphrahat-episcopacy` ✓, `syr.contested.jacob-death-year` ✓, `syr.source.odes-of-solomon` ✓ with `rights_status: pending-verification` exactly as stated ✓, `world-build-docs/syr/SOURCE-REQUEST-MANIFEST.md` §2.1 ✓ (Odes, P2 · DEFERRED). All four gravity ids named in the body resolve, and the C-numbers (C1/C2/C3/C4/C6) match each record's own `name` field bracket. The "18 quote records" count is exactly right (verified by listing `records/syr/quote/`). Findings 3, 4, 5, 6, 13 concern what these records *say*, not whether they exist.

**`flavor_notes[honest-limits]`** — *"Limits are spoken as the voice's own honesty - 'we must be honest', 'we do not know.' This is never a system apology. It is never an apology at all."* Correct against `alx.voice.craft`'s equivalent note, against O2 statement 5, and against this world's own three `honest_limit` records, all of which open in exactly this register (`syr.limit.f5-women-own-words`: *"You ask what the women among us said of their own lives. We must be honest..."*). No apology framing anywhere in the corpus. Sound.

**Schema shape.** `record_type: voice_craft` with `identity` (string), `flavor_notes[]` (each `{segment, tag, note}`, `segment` and `note` required), `characteristic_concerns[]` (strings), `guard` (string) — matches `engine/m1/schemas.py` lines 245–262 exactly, `additionalProperties: False` respected. Envelope fields (`id`, `world_id`, `schema_version: 2`, `status: draft`, `register: emic`, `canon_cells: []`, `confidence` block) are all present and well-formed; `gate_schema_validation` returns 0. The five-item `characteristic_concerns` list matches alx's own five and sits inside the spec's capped-list discipline; the four `flavor_notes` sit inside alx's five. Cap *counts* are fine — finding 14 is about what the notes were spent on, not how many there are.

**Fields the record correctly did not build.** Demonstrations (5c) and voice validation (5e) are absent, which is correct for this step and correctly disclosed. No `demonstration` records exist under `records/syr/`, so no compiled exchange text was in scope for this review.

---

## Recommended disposition

Per the build-cycle discipline, findings 1–16 change substance, sourcing conclusions, or scope boundaries and cannot be applied as cosmetic fixes. Findings 1, 3, 9, 11 and 12 are corrections against this world's own approved records and cautions and should be made before this record advances. Findings 5, 6, 7, 8 and 14 are scope-and-allocation questions about what the capped voice layer is for, and are best resolved together rather than patched one at a time. Finding 16 (5a before 5b) and C10 (the "Mar" honorific) are the lead's calls, not a build or review thread's — carried here rather than resolved, on the PAHC precedent. C1–C9 and C11 can be applied directly.

Nothing here requires the record to be rebuilt. Its spine — the whole-world framing, the anti-personification discipline, the pronoun rule, the readability — is sound, and that is the part that is hardest to get right.
