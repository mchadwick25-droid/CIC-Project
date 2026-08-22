# VOICE-CRAFT-REVIEW-ROUND-2 — Re-review of `syr.voice.craft` after the Round 1 revision

Reviewer: independent adversarial review thread, no part in authoring either version of the record and no part in Round 1. Date: 2026-08-22.
Reviewed at commit `2310a007`, working tree clean. Revision under review: `92af019a` ("syr voice_craft round 2: fix all 16 substantive findings from round-1 review"); prior version `fc05dbd5`.

**Method.** The current record was read cold first, on its own terms, and every factual element in it written down before the Round 1 checklist was opened. Each of Round 1's 16 substantive findings was then re-verified by re-deriving the *new* claim against the cited records directly — not by checking that the old phrases were gone. The mechanical checks (pronoun scan, gate battery, FK, schema) were re-run from scratch rather than taken from Round 1 or from the revision's own commit message. Governing context re-read independently: `Redesign-Spec/CiC-Program-Spec.md` (O1–O7, §4.3 step 5 a–e), `Redesign-Spec/Artifact-1-Record-Schema.md` §4–5, `engine/m1/gates.py` (`_ATTRIBUTION_FIELDS`, `gate_readability`), `engine/m1/schemas.py`, `engine/m2/builders.py` (`build_prompt`'s real field contract), `fleet-voice/EXEMPLAR-TRANSCRIPT.md` on `origin/build/phase-1` (the full four-revision pronoun section, v4 the governing rule), `alx.voice.craft` on `origin/world/alexandria`, `pahc.craft.chloe-voice` on `origin/claude/pahc-world-build-2oq764`, and this world's own corpus — `syr.core.syriac`, all 6 gravities, all 8 contested claims, all 18 quotes, the Odes source record, the flood story, the frontier and transmission force records, two doctrinal-witness records, `records/worlds.yaml`, `SOURCE-REQUEST-MANIFEST.md`, `LEGACY-PARTICIPANT-CARD-REFERENCE.md`, `BUILD-LOG.md`.

---

## Verdict — MINOR FIXES NEEDED — 1 finding half-fixed, 4 new substantive, 5 new cosmetic

All sixteen of Round 1's substantive findings are materially addressed, and the four that were fabrication-class or caution-violating (1, 3, 9, 12) are cleanly and correctly fixed against the actual records — I re-derived each rather than pattern-matching. Nothing fabrication-class remains anywhere in the compiled fields. The spine Round 1 cleared is intact: the whole-world/no-biography discipline still holds mechanically, the gate battery is still 13/13 clean, readability is still comfortable at field level.

The revision does not clear, though, for four reasons that are more than cosmetic:

1. **Finding 8 is half-fixed.** The anti-Jewish safety item was added — well, and accurately. The *second* item the same handoff sentence reserved for this record, the pastoral-warmth/dependency-amplifier risk, is still absent and, unlike 5a and the "Mar" honorific, is not disposed of or even mentioned. The record and its commit message both claim all sixteen are fixed.
2. **The revision dropped a compiled discipline it did not need to drop.** The `honest-limits` flavor note — which Round 1 explicitly verified as sound — was removed on a stated cap rationale that does not hold, and no fleet-level record carries the rule it contained. `syr`'s compiled prompt no longer has it; `alx`'s does.
3. **One new compiled-field scope slip.** The new `place` note's "within living memory" asserts a speaking-present that the `identity` field two fields above explicitly denies.
4. **The trailing body makes two false claims about where things are recorded** — the same class of problem Round 1's C11 flagged, in new form.

None of these require a rebuild, and none touch the record's substance against the corpus except (3). This is a short fix list, not another revision round.

---

## Disposition — Round 1's 16 SUBSTANTIVE findings

**1. `identity` — fabricated source bodies. FIXED.** Re-derived from scratch rather than checking the old phrases were gone. The new sentence names three bodies and each holds: *"Ephrem's hymnic corpus"* (`syr.source.ephrem-nisibene-hymns`, `ephrem-hymns-on-faith-pearl`, real); *"Aphrahat's dated Demonstrations — including what Aphrahat set down for the covenant's own life"* (`syr.source.aphrahat-select-demonstrations.work` lists "VI Of Monks (the bnay qyama teaching)"; `syr.gravity.covenant-life` calls Dem 6 "practical instruction to an order already established" — written *for* the covenant, which is exactly the mediation Round 1 said had to become audible, and `syr.contested.qyama-structure`'s "inner constitution we mostly cannot see" is no longer contradicted); *"how the persecution under Shapur was afterward remembered and told"* (`syr.gravity.persecution-endurance` sources it to Sozomen II.9–14; `SOURCE-REQUEST-MANIFEST.md` §3 confirms "Persian martyr acts: no PD English"). Round 1's caveat that the fix must not simply delete the Persian clause is honored — Aphrahat, the in-window Persian-side witness writing inside the persecution, is still named in the same sentence. No self-authored body is claimed.

**2. `identity` — scope narrowed to one gravity. FIXED.** "this world's own whole covenant tradition" → "this world's own whole Syriac Christian tradition." Checked against `syr.core.syriac.horizon` ("The Syriac-speaking Christian ecology across the Roman-Persian Mesopotamian frontier, c. 200-410 CE") and `records/worlds.yaml` `display_name: "Syriac Christianity (Edessa/Nisibis)"`: the new label names the ecology, not C2. It is not a different overclaim — the immediately following sentence bounds it to "the entire window, c. 200-410 CE - Edessa, Nisibis, and the Persian communities beyond them," which is the horizon's own three-part extent. See NEW-8 for a residual consistency point about the word "tradition."

**3. `guard` — Aphrahat "disagree" misstatement. FIXED.** Checked word for word against `syr.contested.aphrahat-episcopacy`. New text: *"Our own tradition never recorded whether Aphrahat held a bishop's office; the one early witness who touches it says plainly that he does not know, and we do not pretend otherwise."* The record's `concedes` says "this world's records never resolve it - any statement of his office beyond 'unknown' outruns the evidence" (→ "never recorded"); `held_against` says "George of the Arabs, the tradition's own early witness, expressly disclaims certainty" (→ "the one early witness... says plainly that he does not know" — the record's own definite singular, and no longer "ours," which is what made the old wording false). The invented two-sided conflict is gone; so is the possessive "our own earliest witnesses" that made an eighth-century witness in-window.

**4. `guard` — exhaustiveness overclaim. FIXED.** "Two things we have never settled" is gone entirely; the guard now enumerates nothing. It names one open question as an example without any closed-set framing, so it cannot undercount the eight `contested_claim` records or caution 10's two open dates.

**5. `guard` — Odes rights-gate-as-history. FIXED.** The Odes sentences are gone from the guard, and the word "Odes" appears nowhere in any compiled field. Confirmed the rights-gate fact still lives where it belongs (`syr.source.odes-of-solomon.rights_status`, `SOURCE-REQUEST-MANIFEST.md` §2.1).

**6. Trailing body — false "load-bearing" claim. FIXED.** The claim is gone, and the body now states the opposite correctly, quoting the two records' own words ("nothing load-bearing rests on the Odes"; "a dating question with no participant-facing cell"). I also re-scanned all twelve compiled field values for any other build-process or modern-licensing fact voiced as history: none. The single guard item retained is correctly justified as the one with a real cell — `syr.contested.aphrahat-episcopacy.canon_cells: [F3-I]` verified.

**7. `guard` — cap exceeded. FIXED.** Recounted independently: **99 words, two per-world topics** (Aphrahat's office; the anti-Jewish material's one-sidedness), against 111 words / three topics before. Fleet comparison recomputed from the branches: `alx` 6 words / 0 topics, `pahc` 102 words / 1 topic. syr is no longer the fleet's longest guard, and two additions is inside a defensible reading of "at most a line or two." The addition is now signposted ("One thing further, said as plainly:"), matching pahc's own practice, which Round 1 noted was missing. Two things worth the lead's eye: the cap's stated *precondition* — "where a world's **measured** failure demands it" — is still not met, since 5c and 5e remain unbuilt, and the record acknowledges this in the body but keeps both items anyway; and both retained items have independent warrants Round 1 itself supplied (a participant-facing cell; the world's own handoff nomination), so this reads as a reasonable reconciliation of findings 7 and 8 rather than a bypass.

**8. Missing anti-Jewish safety flag. HALF FIXED — see NOT-FIXED-1 below.** The anti-Jewish half is fixed, and the wording is accurate. Checked against `syr.core.syriac` caution 4 and `syr.quote.aphrahat-anti-jewish-frame` directly: *"our own argument against the Jews, kept in some of our own letters, survives entirely one-sided. No answering voice from them was kept, and we do not invent one to balance it."* — "entirely one-sided" is caution 4's own phrase; "no answering voice from them was kept" matches "no Jewish counterpart survives" and the `thin_topics` entry "the Jewish side of Aphrahat's polemical exchange is unrecorded"; "we do not invent one to balance it" matches "never invent balancing voices." "Letters" for the Demonstrations is this world's own vocabulary (`syr.figure.aphrahat.bridge_line`: "the Persian sage whose dated letters survive"). The guard *describes* the material and never voices it, which is exactly what the do-not-voice quote record's own body requires. Two small narrowings noted at NEW-9. The **second** reserved item is not addressed at all.

**9. `characteristic_concerns[4]` — Persian-side generalization. FIXED.** Checked against caution 8 and `syr.gravity.persecution-endurance.description` directly. New bullet: "what endurance under a hostile crown cost **on the Persian side**, and what it did not undo." The qualifier caution 8 demands is inside the bullet, where the compiled bare-list format gives it no other place to live; "a hostile crown" is the gravity's own phrase. The collision Round 1 named — `identity` saying both sides equally, the next field listing one side's experience as the world's — is resolved.

**10. `characteristic_concerns[3]` — FORMATION TEST FAIL upgraded. FIXED, and I gave this the extra scrutiny it was worth.** New bullet: "leadership resting on two footings at once - office and vow - with the record never settling which held." The question is whether "resting on two footings at once" itself smuggles back a lived-experience claim. It does not, and here is why, checked against the gravity's own text rather than against Round 1's suggested wording: `syr.gravity.authority-ambiguity.description` states the two-footing structure as fact — *"vowed-ascetic standing (the covenant's charismatic pathway) and episcopal office run alongside each other"* — and then classifies exactly that as *"a documented condition of the record."* `syr.gravity.covenant-life`'s own body independently names it — *"the covenant's charismatic standing is one of the **two legitimation pathways** in C4."* So "two footings — office and vow" is a claim about the documented structure of legitimation, at the confidence the record's `held_against`-equivalent supports, and it is the half the FORMATION TEST FAIL explicitly leaves standing. What the FAIL refuses is a claim about *how the ambiguity was lived*; the bullet makes no such claim — it says the record never settled which footing held, which is a statement about the record, not about anyone's experience. Contrast the old bullet, "who may be trusted to lead, and **how unsettled that trust has stayed**," which asserted a persisting condition of trust inside the world. The upgrade is genuinely undone. One honest oddity worth naming rather than hiding: a documented-condition statement is a slightly awkward tenant of a field literally named "characteristic concerns," but Round 1 endorsed exactly this resolution and the alternative — dropping C4 from the list — would leave a Tensional gravity unrepresented.

**11. `characteristic_concerns[2]` — boundary attribution reversal. FIXED.** Checked against caution 5 and `syr.gravity.heresiological-self-definition` directly. "the boundary **they made necessary**" → "the boundary **built by answering them**." The necessity is no longer attributed to the rivals; the building is attributed to the answering, which is the gravity's own account ("substantially Ephrem's own rhetorical achievement — built in the Prose Refutations..."). Residual, minor and noted rather than charged: the passive construction still leaves the Ephrem-concentration unnamed, where Round 1's suggested "the boundary Ephrem built by answering them" would have carried it. This is mitigated because `build_prompt` compiles `world_core.cautions` in full, so caution 5's own "Ephrem's Marcion-Bardaisan-Mani triad is boundary-building polemic" reaches the model verbatim. Listing Bardaisan among rivals answered remains correct against caution 1.

**12. `flavor_notes[quotation]` — phantom martyr quote. FIXED.** Re-grepped `speaker_or_author` across all 18 quote records myself: Aphrahat 7 (one `do-not-voice`), Ephrem 5, Bardaisan 1, Chronicle of Edessa 1, Doctrine of Addai 1, Theodoret 1, Sozomen 1, Palladius 1. **Zero martyr quotes**, confirmed independently; the one quote mentioning martyrs (`syr.quote.aphrahat-persecuted-litany`, Dem XXI.22) is Aphrahat's own voice listing scriptural figures, not a martyr's words. The note now names only "Ephrem's own words, Aphrahat's own words" — the two categories with real records behind them — and adds a correct new clause, "no quote is invented to fill a silence the record itself leaves open."

**13. `flavor_notes[quotation]` — false "unusually rich" claim. FIXED.** The comparative is gone from the compiled note entirely, which resolves both halves of the finding (the false claim, and the presence of a cross-world comparative in a per-world layer). The body retains the comparison only as the *reason for dropping it*, and I recomputed it: alx `records/alx` = 137 records / 14 quotes = 10.2%; syr = 150 records / 18 quotes = 12.0% (151/18 = 11.9% counting this record). The body's figures are exact. "Dated" is also gone from the note, which resolves the 8-of-18 problem.

**14. `flavor_notes[]` — no flavor-tagged note, no place note. FIXED.** A `{segment: place, tag: flavor}` note now exists, modeled on alx's. I checked every factual element in it against this world's own records rather than accepting it:
- *"A city wall a flood once broke"* — `syr.story.edessa-flood-201.text`: "the waters beat on the western wall; **the wall gave way**." Grounded.
- *"A fortress traded from one empire to another"* — `syr.core.syriac.horizon`: "Nisibis, **Roman fortress-city from 298 until ceded to Persia in 363**"; `syr.force.two-empires-frontier`: "Roman fortress from 298, surrendered in 363, its Christians evacuating to Roman territory." Grounded ("traded" is loose for a treaty cession, but not wrong).
- *"Hymns and letters crossing a border no one in this world chose"* — grounded in three places: `syr.dw.f5-p-cost-distance` ("**the same songs and letters traveling the roads**"), `syr.dw.f3-t-one-church` ("across every border it knew"), and `syr.force.two-empires-frontier` ("a political line **its participants did not choose**"). The last clause is near-verbatim from the force record.
- *"within living memory"* — **not grounded, and it introduces a problem.** See NEW-3.
The note is otherwise a real, cheap, world-specific flavor gain and does what §4.3's "a place" example asks.

**15. `flavor_notes[self-reference]` — living-tradition conflation. FIXED, both halves.** "I am a representative of Syriac Christianity" → **"I am a representative of Edessa and Nisibis, not here to judge you."** On the living-tradition half: `records/worlds.yaml` carries `living_tradition_flag: true` with named living heirs; the new form names two places with no living claimant of the name and matches the registry's own bounding parenthetical "(Edessa/Nisibis)" exactly. On the paired-contrast half — checked against `fleet-voice/EXEMPLAR-TRANSCRIPT.md` v4 on `origin/build/phase-1`, read in full: the exemplar's own sanctioned line is *"I am a representative of Alexandria, not here to judge you"*, and `alx.voice.craft` states the pair as "'I am a representative... not here to judge' is sanctioned; 'I am a teacher, not a judge' is not." The syr note now carries **both** halves — the positive form inside the sanctioned exception itself, the negative form named and refused with the reason given ("personifies"). Also re-verified all six load-bearing v4 elements survive: strict we-voice always ✓; covering the world's content *and* the voice's present-tense conversational acts, with the exemplar's own two examples ✓; exactly one exception ✓; a naming of what the voice literally is, never an in-world role ✓; at most once per turn ✓; only when the participant's question is directly about the voice's nature or judgment ✓. Two secondary elements from C7 are still compressed out ("identity-collision cells", "never a recurring habit") — but the body no longer claims otherwise, which is what C7 actually asked for.

**16. 5a bypass, stale registry. FIXED — disclosed rather than omitted.** The record's opening paragraph now states it plainly: *"Sub-step (a), the formal identity-emergence rationale write-up, is likewise not built here and remains genuinely owed... this record does not resolve that gap."* It is also carried in the body's numbered list of items flagged for the lead rather than resolved, which is the correct disposition on the PAHC precedent. The registry half is fixed: `records/worlds.yaml`'s syr `state` comment now reads "step 5 voice build begun (voice_craft record drafted and under independent review) - demonstrations (5c), voice validation (5e), and compile/admission not yet begun," and the stale "no voice build" clause is gone. Verified the change landed in `92af019a`, the same commit, as the body claims. The `representative` comment still correctly carries "Step 5a's full identity-emergence write-up... is still owed." Two accuracy problems in *how the body cites this* are recorded at NEW-2 and NEW-7; the disclosure itself is honest and is what the finding asked for.

---

## Disposition — Round 1's 11 COSMETIC findings

**C1. raza/shrara gloss conflation. FIXED.** "The truth a story secretly carries" → "**A sign that carries a hidden truth**." Checked against `syr.term.raza-shrara.plain_meaning` ("A raza is a thing in Scripture or in nature that shows a hidden truth - the shrara... The raza is bound to the truth it shows. It even **carries** some of that truth's hidden power"). The gloss now names the symbol-half as the subject, not the truth-half; "sign" is a fair plain-English rendering of "a thing in Scripture or in nature"; "carries" is the record's own verb; "story" and "secretly" are both gone. The other two examples remain exact against `syr.term.qyama` and `syr.term.ewangeliyon-da-mhallete.quick_meaning`.

**C2. Native word before plain meaning in `concerns[0]`. FIXED.** "reading by raza - what a story..." → "what a story or symbol truly carries beneath its surface, not only what it plainly says." Plain English throughout; no native word. Verified the body's supporting claim: alx's five and pahc's three concern bullets are all plain English.

**C3. 26-word / FK 15.9 outlier sentence in `identity`. FIXED-BUT-NEW-ISSUE.** The sentence was rewritten (it had to be, for finding 1) but got longer, not shorter: **33 words, FK 18.0**, with a mid-sentence em-dash parenthetical stacking a third clause. See NEW-5.

**C4. Three-part geography compressed to two. FIXED.** "Edessa to Nisibis, the Roman side and the Persian side both" → "Edessa, Nisibis, and the Persian communities beyond them." Matches `syr.core.syriac.horizon`'s three elements and `records/worlds.yaml`'s `place` ("Edessa, Nisibis, Persian Adiabene").

**C5. "five confirmed gravities"; there are six. FIXED.** The sentence is gone from the trailing body; no gravity count is stated anywhere.

**C6. False "C5 folded into the raza-shrara line" claim. FIXED.** The sentence is gone. C5 is now represented only by "The one woven Gospel" in the term-introduction note, and nothing claims otherwise.

**C7. "restates the fleet pronoun rule verbatim in substance... matching wording" overstated. FIXED.** The overclaiming sentence is gone. Its replacement is accurate and appropriately hedged: the paired contrast "is now stated alongside the negative half, matching the fleet rule... **more completely than the first draft did**" — which is exactly true and does not claim completeness.

**C8. Build/architecture vocabulary in compiled fields. PARTIALLY FIXED.** One of the three instances is gone (`identity`'s "the only sanctioned fabrications **this build allows**" → "the only sanctioned fabrications **here**"). Two remain: `guard`'s opening "The one fleet floor line, absolutely" and the term-introduction note's "lead with **plain_meaning** before **world_word**" (schema field names verbatim). Consistent with C8's own disposition — it flagged these as a fleet-level decision with direct pahc/fix precedent, not a syr defect — so leaving them is defensible; the revision simply does not say it decided anything. No disposition needed from this thread either.

**C9. `sources: []` with `verification_state: verified-via-authority`. NOT FIXED (by design).** Unchanged, and identical to `alx.voice.craft`. `gate_confidence_crosscheck` passes. Fleet-consistent; noted only, as in Round 1.

**C10. The "Mar" honorific's clerical freight. FIXED (correct disposition).** Carried in the body's numbered list flagged for the project lead, with `syr.term.mar`'s own "bishops, saints, and revered teachers" quoted and caution 3 cited, and explicitly not resolved by the build thread. This is the disposition Round 1 asked for.

**C11. Three appeals to unverifiable chat instruction. FIXED.** All three original appeals are gone (the identity paragraph, the quotation note's, and the guard's). One appeal remains, and it is better handled than the three it replaces: it is quoted verbatim ("Use it as-is; this step is compressing it into the voice_craft schema, not reopening it"), it is inside the numbered list explicitly flagged for the lead, and — the point C11 actually turned on — no compiled text depends on it, so no record citation is being substituted for. Two *new* trailing-body accuracy problems of the same family are recorded at NEW-2 and NEW-7.

---

## NOT FIXED

### NOT-FIXED-1. Finding 8's second reserved item — the pastoral-warmth / dependency-amplifier risk — is still absent, and is the one flagged item the record does not dispose of

`LEGACY-PARTICIPANT-CARD-REFERENCE.md`, "What this settles":

> "**Safety-relevant: the anti-Jewish polemical material's sensitivity *and a flagged pastoral-warmth/dependency-amplifier risk* — both worth carrying into step 5's craft record** and M5's safety design when that work begins."

The legacy card's own `facilitator_cautions` states it concretely: *"This Representative was deliberately built with real pastoral warmth, which the construction record itself flags as a plausible dependency/confidant-substitution amplifier - watch for escalating, exclusive-attachment patterns across sessions, not only single-turn distress."*

The revision added the first item. The second appears nowhere in the record — not in `guard`, not in `flavor_notes`, not in `characteristic_concerns`, and not in the trailing body, which does not mention it even to defer it. Meanwhile the body opens its guard-rebuild paragraph by describing the anti-Jewish item as "**the** one item [the legacy reference] explicitly reserved for this exact record," which is not what that sentence says — it reserved two.

There is a genuinely good argument that this one belongs in M5 rather than here: O5 assigns dependency dynamics to the safety layer, the same handoff sentence names M5 as a destination, and §4.3's cap forbids trait rubrics, which is close to what a warmth-modulation instruction would become. That argument was available and would have been a fine answer. What is not fine is silence — this is the one item in the whole record that is neither carried nor flagged, while the commit message and the body both assert that all sixteen findings are fixed.

**Severity: SUBSTANTIVE (omission of a named safety item, undisclosed, in a record whose own body discloses two other open items correctly).** Recommend a one-sentence disposition in the trailing body — carried, or routed to M5 with the reason — rather than a guard line.

---

## NEW findings — not traceable to Round 1

### NEW-1. `flavor_notes[place]` — "within living memory" asserts a speaking-present that `identity` explicitly denies

> "A fortress traded from one empire to another, **within living memory**."

Nisibis was ceded in 363 (`syr.core.syriac.horizon`; `syr.force.two-empires-frontier`). The window runs to 410. "Within living memory" therefore locates the voice's speaking-now somewhere in roughly 363–410 — a forty-seven-year slice of a two-hundred-and-ten-year window.

Two fields above, `identity` says the opposite in terms: *"This voice speaks for the entire window, c. 200-410 CE"* and *"He is not one located person."* `alx.voice.craft`'s place note, which this one is modeled on, is purely spatial and carries no temporal anchor at all: *"The city concrete and light: the harbor, the lecture room, the villages up the river."*

This is a small phrase, but it is in a compiled field, it is the kind of thing a model will reach for in voice, and it re-opens — in miniature — the exact question this build step is most careful about: whether the Representative has a standpoint in time. Nothing else in the record does this; I checked every compiled sentence for a temporal deictic and this is the only one.

**Severity: SUBSTANTIVE (scope boundary — the compiled `place` note contradicts the compiled `identity` field on the voice's temporal extent).** Fix is one clause: drop "within living memory," or replace it with something the whole window can say ("a fortress that changed empires inside this world's own years").

### NEW-2. Trailing body — "the disposition of each is logged in `VOICE-CRAFT-REVIEW-ROUND-1.md` and `BUILD-LOG.md`" is false of both files

> "REVISION NOTE (round 2...): every substantive finding below is fixed in this version; **the disposition of each is logged in world-build-docs/syr/VOICE-CRAFT-REVIEW-ROUND-1.md and world-build-docs/syr/BUILD-LOG.md**, not restated in full here."

I checked both. `VOICE-CRAFT-REVIEW-ROUND-1.md` is the Round 1 review — it was written before the fix and logs *findings*, not dispositions; it contains no record of what was done about any of them. `BUILD-LOG.md` contains nothing about the voice-craft review at all: it is titled "steps 1–4," its stopping-point line still says no voice_craft work was done, and its "Review round" section is about the separate 150-record corpus review (`REVIEW-ROUND-1.md`). `git show --stat 92af019a` confirms the revision commit touched only two files — the record and `records/worlds.yaml`. `BUILD-LOG.md` was not updated.

So the sentence points a reader at two files for information neither of them holds, in order to justify not restating it. This is the C11 pattern in a new form: an appeal doing load-bearing work that the cited artifacts do not support. The mitigating fact is that the body *does* in practice narrate the dispositions in the paragraphs that follow — the claim is unnecessary as well as false.

**Severity: SUBSTANTIVE (a sourcing claim in the record's own account of itself, contradicted by the artifacts it names).**

### NEW-3. Trailing body — "BUILD-HANDOFF/BUILD-LOG both already say so" is false of BUILD-HANDOFF

> "...remains genuinely owed - records/worlds.yaml's own representative comment and **BUILD-HANDOFF**/BUILD-LOG both already say so..."

`records/worlds.yaml`'s `representative` comment says so ✓. `BUILD-LOG.md`'s escalation check says so ✓ (line 37, verbatim). But there is no `BUILD-HANDOFF` in `world-build-docs/syr/`; the only file of that name in the repo is `Redesign-Spec/BUILD-HANDOFF.md`, and grepping it for "syr" or "Syriac" returns **nothing** — it does not mention this world at all.

**Severity: COSMETIC (a citation to a document that does not discuss the thing cited; the underlying claim is independently true from the other two sources).**

### NEW-4. The `honest-limits` flavor note was removed on a rationale that does not hold, and no fleet record carries the rule it contained

The first draft's fourth note — *"Limits are spoken as the voice's own honesty - 'we must be honest', 'we do not know.' This is never a system apology. It is never an apology at all."* — was deleted. Round 1 verified it as sound in its "Checked and found sound" section. The body's stated reason:

> "The honest-limits note from the first draft **was dropped to make room within the capped budget** - it restated O2 statement 5 and guard's own opening line near-verbatim and added no per-world content."

Two problems.

*The budget claim is not true.* `alx.voice.craft` carries **five** flavor notes; syr carried four before the revision and carries four now. Adding `place` would have made five — exactly alx's count, and inside the discipline Round 1 explicitly cleared ("Cap counts are fine — finding 14 is about what the notes were spent on, not how many there are"). No room needed making.

*The redundancy claim is only half true, and the half that is false is the load-bearing half.* O2 statement 5 says "It says what it does not know, plainly" — it says nothing about apology. The guard's opening line says "What our own record does not answer, we say so plainly" — again, nothing about apology. **"Never a system apology, never an apology at all" is carried by neither.** And it is not carried at the fleet level either: `records/_fleet/` holds only `canon_question` (86) and `modern_term` (1) records — there is no fleet voice record — and `build_prompt()` compiles `voice_craft` per world. `fleet-voice/EXEMPLAR-TRANSCRIPT.md` names `alx.voice.craft` itself as the rule's owner ("the same apology-voice `alx.voice.craft` already forbids elsewhere"), and the exemplar is a document, not a compiled record.

Net effect: `alx`'s compiled prompt forbids apology-voice; `syr`'s no longer does. On a world whose entire voice layer is built around speaking honest limits — three `honest_limit` records, a `thinness` field full of silences, a guard whose subject is what the record does not hold — the apology-voice failure mode is more live here than on most worlds, not less.

**Severity: SUBSTANTIVE (removes a compiled discipline from this world's prompt; the stated justification for the removal does not hold).** Recommend restoring the note as a fifth, or — the better structural answer, and the one finding 14 was really pointing at — raising it as a fleet-layer question rather than deleting it per-world.

### NEW-5. `identity`'s one long sentence got longer: 26 words / FK 15.9 → 33 words / FK 18.0

Computed with `engine.m1.fk.fk_grade`, sentence by sentence across every compiled field. The replacement for C3's outlier:

> "He is drawn from Ephrem's hymnic corpus and Aphrahat's dated Demonstrations — including what Aphrahat set down for the covenant's own life — and from how the persecution under Shapur was afterward remembered and told."

33 words, FK 18.0, three clauses with a parenthetical interrupting between the second and third. It is the only sentence in the record above FK 12 and the only one above 25 words; the next longest is 24 words at FK 9.5. The field as a whole is fine (FK 7.0) and `voice_craft` is correctly outside `gate_readability`'s scope, so nothing fails — but register statement 3 is "one idea per sentence," and the revision moved away from it while fixing the fabrication in the same sentence.

**Severity: COSMETIC.** Splits cleanly in two at the second dash.

### NEW-6. Trailing body — the quote-speaker enumeration is closed with "only" and omits three of the eighteen

> "there is not one martyr quote among this world's 18 quote records (**only** Ephrem, Aphrahat, the Chronicle of Edessa, the Doctrine of Addai, and the Bardaisan comparandum dialogue are actually attested)"

By my own grep of `speaker_or_author` across all 18: that list covers 15. The other three are `syr.quote.palladius-hospitaller`, `syr.quote.sozomen-melodies`, and `syr.quote.theodoret-gnats` — later, non-Syriac, outside-window witnesses, all real and all attested. The word "only" turns an incomplete enumeration into a false closure claim. This is the same shape as Round 1's finding 13, which caught the previous body accounting for 14 of 18; the count improved and the closure word made it worse. The conclusion it supports (zero martyr quotes) is correct — I verified it independently.

**Severity: COSMETIC (trailing body; the compiled note is correct).**

### NEW-7. `BUILD-LOG.md`'s stopping-point line is now stale in exactly the way `records/worlds.yaml`'s was

> BUILD-LOG.md, line 5: "**Stopping point (by instruction):** full content canon complete; **no** voice_craft, demonstration, compile, or admission work."

A `voice_craft` record now exists, has been through two review rounds, and the revision explicitly corrected the identical staleness in `records/worlds.yaml`'s `state` comment in the same commit. This one was not touched. Same class as Round 1's finding 16 registry half, one file over.

**Severity: COSMETIC (build documentation, not a record; nothing compiled depends on it).**

### NEW-8. `identity` keeps "Syriac Christian tradition" — the same label family the revision removed from the self-naming line for living-tradition reasons

The revision's own rationale for finding 15 is that "Syriac Christianity" as a bare label "reads as a claim on the LIVING tradition." That reasoning was applied to the spoken self-naming line and not to `identity`, which still reads "They are given to this world's own whole **Syriac Christian tradition**."

The risk is much lower here and I am not claiming it is wrong: `identity` is descriptive scaffolding rather than a line the voice says aloud; "this world's own" bounds it; and the very next sentence pins the window and the three-part geography. `syr.core.syriac.horizon`'s own noun is "ecology," and `worlds.yaml`'s `place` field says "The Syriac-speaking ecology..." — so "ecology" was available and would have been both more exact and consistent with the fix next door. Raising it so the inconsistency is a decision rather than an oversight.

**Severity: COSMETIC.**

### NEW-9. Two small narrowings inside the new anti-Jewish guard sentence

Both checked against caution 4 and both mitigated, but worth recording so they are deliberate:

- *Scope of the material.* Caution 4: "roughly four of Aphrahat's Demonstrations, **with strands in Ephrem**." The guard says "kept in some of our own letters" — true of the Demonstrations (`syr.figure.aphrahat.bridge_line` calls them "letters"), but it implies containment and drops Ephrem.
- *Scope of the one-sidedness.* Caution 4 has two limbs — "no Jewish counterpart survives **and no internal Christian dissent from it is attested**." The guard covers the first only.

Mitigation, verified in `engine/m2/builders.py`: `build_prompt()` emits `world_core.cautions` in full as its own `## Cautions` section, so caution 4 reaches the model verbatim, both limbs and the Ephrem strands included. The guard is a pointer, not the sole carrier, and the guard's cap makes compression appropriate. No change needed unless the lead wants the Ephrem half surfaced.

**Severity: COSMETIC.**

---

## Checked and found sound

Each verified directly this round against the named artifact, not carried over from Round 1 and not taken from the revision's own account of itself.

**The whole-world / no-biography discipline — re-verified mechanically, from scratch.** Parsed the record's YAML, extracted all eleven compiled field values (`identity`, `guard`, four `flavor_notes[].note`, five `characteristic_concerns[]`), and regexed each for `\b(I|I'm|I've|I'll|I'd|my|me|mine|myself)\b`. **Three hits, all inside quoted rule examples** — two in the self-reference note (`'I am a representative of Edessa and Nisibis, not here to judge you'`, `'I am a teacher, not a judge'`) and one in the quotation note (`That 'I' belongs to the one quoted`). **Zero in `identity`. Zero in `guard`. Zero in all five `characteristic_concerns`. Zero in the new `place` note.** Read `identity` clause by clause again for any phrasing that would locate Yausep as an individual — birth, upbringing, "lived through," one side of the frontier as personal experience, a room, a year: none. All four explicit denials survive the rewrite intact ("Yausep is not a biography," "He is not one located person," "No side is weighted as his own personal history," "No side is treated as foreign to him"), which is the direct repair of the error corrected on this world at `8b49ed48` and of the fleet's own v3→v4 correction. NEW-1 is the single temporal-standpoint slip and is in the `place` note, not in the persona framing.

**Gate battery — re-run, not trusted.** `engine.m1.gates.run_all()` over `load_world_records("syr")` + `load_fleet_records()` + `load_registry()`: **all 13 gates, 0 findings** — schema-validation, referential, reciprocity, completion-per-type, narratability, quote-recording, alias-safety, distribution-health, confidence-crosscheck, rights, readability, canon-coverage, no-build-attribution. The record's closing paragraph claims exactly this and is correct.

**Readability — recomputed with `engine.m1.fk.fk_grade`.** `identity` **FK 7.0** (184 words); `guard` **FK 8.4** (99 words); term-introduction 3.9, self-reference 7.6, quotation 8.4, place 5.1; concerns 7.7–11.2 on 16–18-word fragments. Every field is far below the FK 14.1 / 65-word-sentence defect the PAHC review caught. `voice_craft` is correctly outside `gate_readability`'s scope (which covers `term.quick_meaning`, `term.plain_meaning`, `honest_limit.statement` only — confirmed in `engine/m1/gates.py` lines 201–216). NEW-5 is the one sentence-level regression.

**Schema validity — re-verified against `engine/m1/schemas.py` lines 245–262.** `record_type: voice_craft` with `identity` (string), `flavor_notes[]` of `{segment, tag, note}` with `segment`/`note` required and `additionalProperties: False`, `characteristic_concerns[]` (strings), `guard` (string). The new `{segment: place, tag: flavor}` note conforms (`tag` is a free string). Envelope fields all present and well-formed. `gate_schema_validation`: 0.

**Registry consistency.** `records/worlds.yaml` syr: `representative: {name: Yausep, role_label: Mar}`; the record uses "Mar Yausep" and never self-names otherwise. Window "c. 200-410 CE" matches `time_window {start: 200, end: 410}` exactly, in the world's house style rather than ISO. `place` matches the identity field's three-part geography. The persona-provenance disclosure sentence survives the revision intact.

**`build_prompt`'s real field contract.** Re-read `engine/m2/builders.py`: it emits `## Identity` from `craft.identity`, then `world_core`'s Horizon/Formation logic/Thinness/**Cautions**, then `## Guard`, `## Characteristic concerns` (bare bullets, no qualifiers available — which is why finding 9's in-bullet qualifier matters), `## Flavor notes` (`- [segment] note`), then terms, witnesses, honest limits, stories, demonstrations. Quotes are **not** compiled into the prompt, so the `do-not-voice` licensing of `syr.quote.aphrahat-anti-jewish-frame` is enforced outside this record — the quotation note naming "Aphrahat's own words" as a quotable category does not bypass it.

**Doc_01/Doc_02 settled findings, re-checked against the rewritten text specifically.** Strand-singular (one ecology, not two): honored, unchanged. Bardaisan as Named Comparandum (caution 1): honored — `concerns[2]` still lists him among rivals *answered*, never as a source of the world's faith. No post-410 smear (caution 7): clean — no "Catholicos," no "School of Nisibis"; the new place note's 363 cession is in-window. Ephrem malpana/choir overclaim (caution 9): clean — Ephrem appears only as "Ephrem's hymnic corpus"; no choir-leadership claim anywhere, including in the new place note where "hymns crossing a border" could easily have drifted there and did not. Abgar/Addai as self-understanding not origin fact (caution 2): not touched. Caution 10's held-open dates: the guard no longer touches Jacob's death year at all, so nothing can misstate it.

**`characteristic_concerns[0]` and `[1]` re-traced.** `[0]` "what a story or symbol truly carries beneath its surface, not only what it plainly says" → `syr.gravity.raza-shrara-method` (C1, Primary) and `syr.term.raza-shrara`; accurate, and now plain-English-first. `[1]` "the covenant kept for a whole life, in the middle of an ordinary town, not away from it" → `syr.gravity.covenant-life` (C2) and `syr.term.qyama`'s "they did not leave for the desert. They stayed in town"; unchanged from the first draft and still the strongest bullet in the list, with the desert-monasticism false friend correctly excluded.

**Every record id and figure cited in the trailing body resolves and says what is claimed of it.** `syr.gravity.covenant-life` ✓, `syr.contested.qyama-structure` ("inner constitution we mostly cannot see", quoted exactly) ✓, `syr.core.syriac` cautions 3/5/8 ✓ (each quoted accurately), `syr.gravity.heresiological-self-definition` ("substantially Ephrem's own rhetorical achievement", exact) ✓, `syr.gravity.authority-ambiguity` ✓, `syr.source.odes-of-solomon` ("nothing load-bearing rests on the Odes", exact) ✓, `syr.contested.jacob-death-year` ("a dating question with no participant-facing cell", exact) ✓, `syr.contested.aphrahat-episcopacy.canon_cells: [F3-I]` ✓, `syr.term.mar` ✓, `SOURCE-REQUEST-MANIFEST.md` §3 ("Persian martyr acts: no PD English", exact) ✓, `LEGACY-PARTICIPANT-CARD-REFERENCE.md`'s safety sentence ✓ (quoted accurately, though truncated at the point where it names the second item — see NOT-FIXED-1), `records/worlds.yaml`'s `living_tradition_flag` comment ✓ (quoted exactly), `fleet-voice/EXEMPLAR-TRANSCRIPT.md` v4 ✓. The 18-quote count, the 150-record census, and the alx 14/137 comparison are all exact — recomputed by `git ls-tree` on `origin/world/alexandria` and by direct file count here.

**Guard structure against the fleet, recounted.** `alx` 6 words / 0 per-world topics; `pahc` 102 words / 1; `syr` now **99 words / 2**, signposted. syr is no longer the fleet's longest guard and no longer the only one stacking three rules. The fleet floor line ("honest thinness over invented depth") is present and correctly placed first.

**Fields correctly not built.** No `demonstration` records exist under `records/syr/`; 5c and 5e remain unbuilt and are correctly disclosed as such, now alongside 5a.

---

## Recommended disposition

Six items to apply, none requiring a new draft:

- **NOT-FIXED-1** — add a one-sentence disposition of the dependency-amplifier item (carried, or routed to M5 with the reason). Substantive.
- **NEW-1** — drop or rephrase "within living memory" in the `place` note. Substantive, one clause, and the only compiled-content change on this list.
- **NEW-2** — remove or correct the "disposition of each is logged in..." sentence. Substantive.
- **NEW-4** — restore the `honest-limits` note as a fifth, or raise it as a fleet-layer question; do not leave it silently deleted. Substantive.
- **NEW-3, NEW-5, NEW-6, NEW-7, NEW-8, NEW-9** — cosmetic; applicable directly per the build-cycle discipline.
- **C8, C9** — no action; fleet-level or fleet-consistent, as Round 1 held.

The two items flagged for the project lead (5a's owed write-up; the "Mar" honorific) are correctly flagged and are not this thread's to resolve.

The work Round 1 asked for was done, and done by re-deriving against the records rather than by patching phrases — the four fabrication-class and caution-violating findings in particular are properly fixed, and finding 10, the subtlest of the sixteen, is fixed correctly rather than superficially. What this round found is a short tail: one half-finished fix, one small compiled-field slip introduced by an otherwise good addition, one sound element removed for a reason that does not hold, and a trailing body that once again describes its own paperwork more confidently than the paperwork supports.
