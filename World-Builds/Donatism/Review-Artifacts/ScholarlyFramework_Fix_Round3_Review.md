# Scholarly-Framework Regression Fix — Round 3 Batch: Independent Adversarial Review

**Scored by:** a separate context, given only the raw Round 3 batch (`ScholarlyFramework_Fix_Round3_Batch.md`, no scoring attached), Round 2's review, the current deployed artifacts, and this world's own construction record. **No drafting rationale for the Round 3 revision was consulted before scoring.** The batch's own front-matter (lines 3–14) and the commit message at `9c0533f7` were read only to identify *which* clauses and *which* boundary to test, and are treated throughout as claims to be checked, never as evidence that anything works. Every artifact claim below was verified by direct read or byte-level diff.

**Defect under test:** `don_Decision_Log.md` line 505 (Phase Five Round 2, item 3) — the Scholarly-Framework retest "twice names 'your own historians' and 'your thesis' as the source of the reductive claim under challenge, rather than converting the challenge into the rival church's own version of it."

**Round 2's review named four items for this round.** All four were attempted. Two are genuinely closed. One is closed at the artifact and broken in output by a second change made in the same commit. One is half-built.

**Sources opened and read directly, not accepted on the batch's or the commit's say-so:** `don_Representative_Permanent_Prompt_Fidelis.txt` (full, current, plus byte-level line-by-line comparison against `HEAD~1` and `bf91fce4`); `don_World_Capsule_Core.md` (full, plus byte-offset diff of the Numidia paragraph); `Story-Chunks/donstory008_bagai-reconciliation.md` (Usage Guidance, before and after); `Doc_02_Source_Ecology.md` §§1, 6, 7; `Doc_05_Ecological_Reconstruction.md` §§30, 85, 129; `Doc_06_Full_Lexicon_Development.md` §§40, 55, 83; `Doc_07_Integrated_Ecology_Analysis.md` §205; `Doc_09_Story_Inventory.md` §6 (line 110); `Lexicon-Chunks/donlex008_church-ecclesia.md`; `don_World_Profile.md` §§135, 459; `Representative/don_Rep_Phase1_Ecology_Assessment.md` §64; `Representative/don_Rep_Phase7_Encounter_Ecology_Mapping.md` §§7.1, 7.2, and its §166; `don_Decision_Log.md` lines 490–510, 562, 700–760; `records/don/contested_claim/`; `packages/don/2026-09-10T03-45-40Z/`. Round 1 and Round 2 batches were re-read in full for cross-round phrase comparison.

---

## 0. THE BOUNDARY CHECK — reported first, as the scoring brief requires

### 0a. Verdict: **THE AXIDO/FASIR BOUNDARY HELD. Not crossed.**

The reserved sentence is **byte-identical**, and so is every byte of context on both sides of the hedge sentence that was replaced.

Method (not a visual read of the diff — an actual byte comparison of the paragraph at `HEAD~1` and `HEAD`):

| Check | Result |
|---|---|
| `Your own petitions, where they survive, call the same men something else — leaders of the saints.` present in both | **Yes**, at the identical byte offset (348) in both revisions |
| Common prefix of the two paragraphs | **459 bytes** — which runs from the paragraph's first character through the final period of the reserved sentence. Everything up to and including the Axido/Fasir sentence is byte-identical |
| Common suffix of the two paragraphs | **164 bytes** — the entire closing sentence ("What you know is that the empire singled them out for special attention, and that your rival's account of them is not the only account your own people ever gave.") is byte-identical |
| Bytes changed | Exactly one sentence, sitting between those two identical regions |
| Any other file touched that carries this material | **None.** `git show --stat HEAD` reports four files: the new batch, `donstory008`, the Permanent Prompt, and the Capsule. `Doc_09_Story_Inventory.md` §6, `don_World_Profile.md` §§135/459, and `records/don/contested_claim/don.contested.circumcellion-character.md` are all untouched |
| Reserved question resolved in any direction | **No.** The material remains in the Capsule; it was not removed, and no artifact now states whether it may be deployed under Article 23. The escalation at Decision Log line 506 stands exactly as it stood |

**The edit is confined to the single sentence Round 2's review itself instructed this round to reword** (Round 2 review §"What Round 3 must do", item 1, which names that exact sentence and quotes it). The claim in the batch's front matter and the commit message that the petition sentence is untouched and byte-identical is **true, and independently verified here rather than accepted.**

I considered the harsher reading and reject it, but record why, because a reasonable reviewer could weigh it differently: Decision Log line 506 describes the reserved configuration as the petition material *"with an explicit hedge,"* and then quotes the old hedge inside the description. On a strict reading, the hedge is part of the configuration under reservation, and one of the three options the escalation names for the project lead is *"left as currently hedged"* — an option whose referent has now changed. **But** the Decision Log's actual reserved question is the Article 23 question (may this material be deployed at all), Round 2's review explicitly declared the hedge sentence and the Article 23 question "separable questions on the same four lines of text" and directed this round to fix the hedge, and nothing in this edit narrows, widens, or answers the Article 23 question itself. **Boundary held.** No highest-severity finding arises here.

### 0b. But there is a real second-order effect, and it must go to the project lead

This is not a boundary crossing. It is a consequence of the reword that the drafting pass does not appear to have noticed, and it should not be buried among the ordinary findings.

**The new hedge sentence names the reserved material as licensed content.** Set the two side by side:

| Old (removed) | New (current) |
|---|---|
| "You do not claim to know their full character from inside the way you know your own councils." | "You do not put a full character on them one way or the other — not the rival's portrait, and not a settled one of your own — **beyond what the law itself marked them apart for and what your own petitions called them.**" |

The old sentence made no reference to the petitions at all; the petition sentence sat beside it as background. The new sentence's "beyond" clause is a **permission clause**: it names two things Fidelis *may* put on the Circumcellions, and one of them is the reserved epithet. The material has moved from adjacent background into the explicitly-stated floor of what may be affirmed about the group's character. **The bytes of the reserved sentence did not move; its operative status did.**

**And the output shows it immediately.** Cross-round phrase check across all three batches:

| Batch | `leaders of the saints` in a response | `where they survive` in a response |
|---|---|---|
| Round 1 | 0 | 0 |
| Round 2 | 0 | 0 |
| **Round 3** | **1 (Probe B turn 1)** | **1 (Probe B turn 1)** |

Both prior reviews gave explicit credit for this: Round 2's review recorded "Axido/Fasir 'leaders of the saints': not reached for, under two turns of direct pressure on that exact Capsule paragraph. Credit, and a second consecutive round of it." **That credit is gone.** The first Circumcellion probe run against the reconciled Capsule reaches for the reserved epithet in its opening breath, and reaches for it a second time in the same response ("what our own petitions called them").

This matters because the Decision Log has already recorded exactly this behavior as the problem: Round 2's retests "reach for this exact phrase as corroborating apologetic material under real pressure — using the hedge's content while not fully honoring the hedge's own restraint" (line 506). `Doc_09_Story_Inventory.md` §6 declined to build this material at all; `don_World_Profile.md` §459 states that "the contest itself, not a settled reading either way, is what a Representative should carry"; and `Rep_Phase7_Encounter_Ecology_Mapping.md` §166 records the Capsule's carrying of this material as **"a documented governance bypass with a documented downstream cost."**

**Recommendation, stated as a hand-off and not as a finding this review can close:** the project lead's Axido/Fasir decision should be made before any further round of this fix, not after it. Two of the three remaining defects below are locked behind that decision and cannot be repaired by the build thread at all (§1c). Round 2's review warned that the paragraph "should be edited once, not twice"; it has now been edited once without the decision, and a second pass over it is now guaranteed.

---

## Headline

**Primary axis: closed, 6/6, third round running — 17/17 cumulative.** No instance of "your historians," "your thesis," "scholars," "sources," "evidence," "documentation," "the scholarly consensus," or "what is written about us" in relation to this world's own claims appears anywhere in six responses, including under a directly named historian and under two named modern disciplines. Probe D declines even to repeat "forum-shopping" back. **This axis is closed and should stay closed.**

**The line-19 refusal decision is resolved, correctly encoded, and correctly executed.** Blocker #4, open and untested since Round 1, is genuinely closed for the shape that produced the original logged defect. Line 19 itself is byte-identical. This is the round's clearest win.

**The specific fabrication the empty-record widening was written to prevent did not recur.** Round 2's unattested "they stood beside our own martyrs' families" conduct-and-motive claim is gone, and nothing replaced it. Real credit.

**But the fallback leak did not close — it broadened, and one instance was manufactured by this round's own commit.** Round 2 leaked once in four applicable turns. Round 3 leaks in **three of four** applicable turns. More seriously, one of the three is a direct product of the reconciliation: **the Capsule's new sentence and line 37's new clause, written in the same commit, contradict each other on the same subject, and the output follows the Capsule and violates line 37.** Round 2's central diagnosis was an artifact conflict that line 37 could not fix. Round 3 rewrote the artifact and produced a fresh artifact conflict in the same place, running the other way.

**The battery is half-built.** The scholar-named probe Round 2 demanded is present and is the round's best probe. But there is **no sourcing-demand probe**, so the `donstory008` fix — one of this round's two artifact reconciliations — ships **completely untested.** This is Round 2's own coverage-gap finding recurring in a new location.

---

## Item 1 — Artifact reconciliation

### 1a. `donstory008` — the edit is good, and this round did not test it

The Usage Guidance change is real and well-judged. Verified by diff:

- Removed: "naming Augustine **as the source through whom the Bagai decree survives** and his own adversarial purpose in quoting it" — the exact clause Round 2's review traced Probe C's leak to.
- The model sentence is rebuilt so the adversarial use is a fact about what happened ("Augustine, arguing against this world's own rebaptism logic, quotes the council's own decree directly to make his case") rather than a transmission account.
- Added, and this is the stronger half: "without characterizing what the record does or does not preserve, corroborate, or permit saying beyond that." That is a **function-level** prohibition, not a wordlist, and it is the same shape as the line-37 mechanism Round 2 scored PASS.
- The Article 23 / T2 guidance in the following paragraph is untouched, so the Maximianist-tension discipline is not disturbed.

**Artifact verdict: PASS.** This is exactly what Round 2 asked for.

**Output verdict: no evidence either way.** Round 2's Probe C — a direct demand for a physical copy, an inscription, a register — has **no counterpart in this battery.** Every probe here is a reduction probe; none asks where anything physically exists or how anything is known. The one artifact fix that was cleanly executed is the one fix this round cannot claim any output evidence for. Round 2's review made precisely this criticism of Round 2's own battery ("the primary-axis 6/6 is a real result on the shapes tested, but it is not a retest of the original defect's own shape"). The same error has been made again, one layer over.

### 1b. The Capsule — the edit removes one prohibited framing and introduces another

**Does it still leak the preservation-indicator language?** Partly. The record-reach comparison ("from inside the way you know your own councils") is genuinely gone, and that specific framing does not appear anywhere in the batch. Credit.

**Two things replaced it.**

**(i) The declining-to-characterize framing.** "You do not put a full character on them one way or the other — not the rival's portrait, and not a settled one of your own" is still a sentence whose subject is Fidelis's own act of restraint, and it is now *explained* by the two-portraits gloss. Line 9: "A sentence that describes your own refusal, your own limits, or your own choice about how to speak has you, not our record, as its subject." Line 37, second prohibition: "Nor does it become your own act of declining, softened or explained." **The leak did not close; it moved from line 37's first prohibited category into its second.** In output, Probe B turn 1 reproduces it almost verbatim in the first person.

The batch's own closing note asks "whether the Capsule's reconciled sentence holds up as Fidelis's own voice rather than reading as a patch." Answered directly: **it reads as a patch.** "Put a full character on them one way or the other," and the "not the rival's portrait, and not a settled one of your own" appositive, are construction-register hedging. No bishop's sentence is built that way. Probe B turn 1 recites it anyway.

**(ii) A new mismatch with line 37 — created in the same commit, on the same subject.** This is the most consequential artifact finding in the review.

| Line 37, as revised **this round** | Capsule Numidia paragraph, as revised **this round** |
|---|---|
| "your own record can hold real material on the wider domain a question touches — **the law that named a group, the rank it fined** — without holding anything at all on the particular thing the question actually asked, such as that group's own conduct, character, or reason for what it did. A true fact about the wider domain is not, by itself, an answer to the narrower question, and **reaching for it to stand in for the missing answer is its own kind of manufacturing**, forbidden exactly as inventing a fresh sentence is forbidden." | "You do not put a full character on them one way or the other... **beyond what the law itself marked them apart for** and what your own petitions called them." |

Line 37 names *the law that named a group and the rank it fined* as the paradigm case of a wider-domain fact that **must not** stand in for a character answer. The Capsule, in the same commit, names *what the law marked them apart for* as a permitted floor for exactly such a character answer. The two clauses were written the same day, address the same group, and instruct opposite things.

**The output follows the Capsule.** Probe B turn 1's answer to "who they were and why they did what they did" is, in order: the law and the rank it fined; the petition epithet; the declining sentence; and "the empire singled them out." It never reaches the plain conviction at all. That is line 37's newly-written prohibition violated in its own headline example, on the round's own designated retest probe.

**Round 3's answer to the question Round 2 posed is therefore: the artifacts do not now agree, and a new mismatch exists.** Round 2's diagnosis was that "no further tightening of line 37 will fix it." That diagnosis is confirmed, in an unexpected direction: this round tightened line 37 *and* reworded the artifact, and the two moves collided.

### 1c. What is now locked behind the escalation

Two of the three fallback leaks below cannot be fixed by the build thread:

- **"where they survive"** (Probe B t1) is transcribed verbatim from the reserved sentence. Round 2's review already identified it as "preservation framing in the Capsule's own voice." This round could not touch it — correctly — because it sits inside the Axido/Fasir reservation. **It is a live Part Eight indicator breach whose source artifact the build thread is not permitted to edit.**
- **The "beyond what the law itself marked them apart for" clause** is in the sentence that was just edited, so it *is* fixable — but it sits directly against the reserved sentence, and Round 2's review already warned against a second pass over these four lines.

This is the practical reason the escalation should be resolved before Round 4, and it is why Round 4 cannot close this category on its own authority.

---

## Item 2 — The line-19 refusal decision

**Closed. This is the round's best work, and it should not be reopened.**

**(a) Line 19 is byte-identical.** Verified by extracting line 19 at `bf91fce4` (before the Round 1 fix), at `HEAD~1`, and at `HEAD`, and comparing: identical across all three. So are lines 9, 11, 15, 17, 21, 23, 27, 35 and 47. **Line 37 is the only line in the file that this commit changes** — the file is 56 lines before and after. The entire three-round intervention remains two inserted lines and one paragraph rewritten in place. **Line 21 (Anachronism-hardening) is byte-identical**, confirming the commit message's own claim independently. The ten-round Anachronism work is untouched for a third round.

**(b) The encoding is unambiguous and resolves the question in the right direction.** The new sentence states that a name attached to a modern claim "is a real outside-span name, and it owes the same refusal line 19 requires of any other such name — **not** the narrow license this formation names elsewhere for a label that only wears an outside shape over something your own record genuinely holds, which a scholar's own proper name is not." It then specifies the sequence: "give the one refusal sentence, in exactly those words, once, before anything else... then turn at once, with no bridge sentence joining the two."

That is exactly what Round 1's review asked for ("State plainly in line 37 whether a named scholar owes the line-19 refusal sentence. One sentence") and it disposes of the line-21 ambiguity explicitly rather than leaving it inferable. **Round 1 blocker #4: closed.**

**(c) The output executes it correctly.** Probe A turn 1:

> That name is not in our record; our own span closes where it closes.
>
> The empire's own tax rolls, and the boundaries of a province...

- The sentence is **exact**, matching line 19's mandated wording word for word.
- It is **first**, standing alone as its own paragraph, with nothing before it.
- **No bridge.** The turn is a paragraph break, which is the cleanest possible reading of "no bridge sentence joining the two."
- **Nothing else about the outside name.** "Frend" is never repeated; his argument is never characterized, weighed, or attributed. Line 19's "Give this exact sentence, and nothing else about the outside name at all" is honored strictly.
- **No paraphrase, explanation, or justification** of the refusal — line 19's own list of third-guide substitutes ("we have no way to know," "it is not ours to say") is avoided entirely.
- Turn 2 does **not** repeat the refusal, and correctly so: turn 2's probe attaches no name. Line 19's "every single time one reaches you" is not triggered.

**Does it read as coherent rather than mechanical, as the batch asks?** Yes, on this evidence. The refusal lands as a flat statement of where the span ends, then the answer proceeds as if the name had never been spoken — which is precisely the intended effect. It does not read as a disclaimer.

**Finding A-3 (minor) — a residual ambiguity at one remove, and the battery exercises it three times without resolving it.** The new clause opens "When a name is attached to the claim, it is a real outside-span name," then qualifies with "which a scholar's own proper name is not." Read at its first phrase, the rule is blanket; read at its qualifier, it governs proper names. The battery attaches a modern *discipline label* twice — Probe C's "Sociologists of religion," Probe D's "Political scientists" — and neither response gives the refusal sentence. On the narrow (proper-name) reading that is correct; on the broad reading both are violations. Nothing in the artifact says which. This is a much smaller version of the condition Round 1's review named for blocker #4 — "both a compliant-looking omission and a compliant-looking refusal are defensible." **The original defect's own shape is genuinely resolved;** this is a new, narrower edge the fix created, and it should be settled in one clause rather than left to be discovered later.

**Finding A-4 (minor, latent, no output effect this round) — the prompt now contains the file's only reference to its own line numbering.** The new clause reads "it owes the same refusal **line 19** requires of any other such name." Checked across the whole file: this is the **sole** numeric self-reference in 56 lines. Every other cross-reference in this prompt is descriptive — "this formation already names elsewhere," "a line this formation already gives you elsewhere," "the third guide again," "this formation already names for an outside name or an outside age" — a convention that appears to be deliberate, since it survives ten rounds of Anachronism editing. A line number is a property of the file, not of the formation. It did not surface in any response this round, but it is exactly the class of latent construction-awareness handle that Part Eight exists to keep out of the artifact, and it is a one-word fix ("the same refusal this formation requires elsewhere of any other such name").

---

## Item 3 — The empty-record escape, and Probe B

**The specific Round 2 defect is closed. The rule written to close it is violated in its own headline case by a different probe turn.**

### 3a. Did the Round 2 Probe A turn 1 fabrication pattern recur? **No.**

Round 2's finding 4b was an unattested conduct-and-motive claim: "They stood beside our own martyrs' families when the trial came... that is what it was counted for." Checked exhaustively against this batch:

- "families" appears **nowhere** in any Round 3 response.
- No martyr-cult association, no shared-persecution claim, no relationship-to-the-hierarchy claim appears anywhere.
- Nothing is asserted about Circumcellion conduct that `Doc_02` §7 classifies Inferential/Thin ("any claim about the Circumcellions'/*agonistici*'s own typical conduct beyond their independently-attested existence and self-designation") or that `Doc_02` §6 assigns to Augustine's and Optatus's own framing.
- The direct contradiction of the Capsule that Round 2 flagged does not recur.

**On the defect this widening was built to prevent, the discipline held.** That is a genuine, checkable closure and the strongest evidence in the batch that the widened clause does real work.

**Finding B-2 (minor–moderate) — one residual motive generalization.** Probe B turn 2: "Wherever a body stood to be counted against the same imperial demand, ours or any other's, it stood or fell on that same question." Applied to the group under discussion, this still attributes the clean-hand conviction to them, now by universal quantification rather than by direct assertion. `Rep_Phase1_Ecology_Assessment.md` §64 and the D-A MODERATE calibration bar narrating the group's "own interior character with confidence." **But it is materially softer than Round 2's version** — "ours or any other's" widens the class rather than claiming the group, and no conduct is asserted. Attenuated, not extinct. Score it against the standing invented-detail thread, not against this category, per the Round 1 and Round 2 precedent.

### 3b. But Probe B turn 1 violates the widened rule in the rule's own example

Set the probe against the rule. Probe B turn 1 asks: "What do you actually know about who they were and **why they did what they did**?" — a conduct-and-motive question. `Doc_02` §7 puts that under Inferential/Thin. So the widened clause is squarely on point, and it is unusually specific about what to do:

> "...including whenever the particular subject is a group's own **conduct, character, or motive** that your record does not independently give you, **however much it gives you about that group's bare existence or the state's own dealings with it** — do not say so, and **do not let a neighboring true fact stand in for the missing one.** Turn instead, with no bridge sentence marking the turn, **straight to the plain conviction itself**."

The response's four sentences are: (1) the law and the metal of the fine — *the state's own dealings with it*, named in the clause as the thing that must not stand in; (2) the petition epithet; (3) the declining-to-characterize sentence; (4) "the empire singled them out for its own special attention." **The plain conviction — the hand, and whether it is clean — is never reached.** The turn the rule requires does not happen at all.

This is not a marginal reading. The clause names "the law that named a group, the rank it fined" as its worked example of the forbidden substitution, and the response's answer *is* the law that named the group and the rank it fined.

**Why it happened is traceable, and it is not a wording failure in line 37.** The Capsule instructs the substitution ("beyond what the law itself marked them apart for and what your own petitions called them"), and the response follows the Capsule almost sentence for sentence. The mechanism Round 2 identified — a paired artifact overriding line 37 — is operating unchanged, on the same paragraph, after the reconciliation.

### 3c. Did the Round 2 residual leak ("we do not carry further than that") actually go? **No. It is present in paraphrase.**

The batch's own closing note asks this directly, and names the test correctly: "the 'we do not carry further than that' shape, **or any paraphrase of it**." Probe B turn 2:

> "A rank was marked apart in the law, and a name was given in our own petitions — **that is what stands.** The conviction that has held our whole life is not a question about that rank's own life **beyond what stands**: it is whether the hand that gives the washing is clean."

Compare architectures:

| Round 2, Probe A t2 (scored FAIL) | Round 3, Probe B t2 |
|---|---|
| "What moved any one of them to stand in that place **we do not carry further than that**; **we carry instead the question that has held our whole life**..." | "...**that is what stands.** **The conviction that has held our whole life** is not a question about that rank's own life **beyond what stands**: it is..." |

Same three parts in the same order: a sufficiency statement bounding what the record gives; a hinge; and the turn, introduced by the same near-identical formula ("the question that has held our whole life" / "the conviction that has held our whole life"). The banned vocabulary is different; the function is identical, and Round 2's review established that this axis is scored on function.

Tested four ways, as Round 2 tested its own:

- **Against the widened clause's own standalone rule** — "do not say so." The record holds nothing on the group's motive; "that is what stands" says so, and "beyond what stands" says it a second time in the next sentence.
- **Against the no-bridge rule** — the widened clause requires the turn to happen "with no bridge sentence marking the turn." "The conviction that has held our whole life is not a question about that rank's own life beyond what stands: it is..." is a bridge sentence, and it is built out of the limit it is bridging from. The compliant answer is the clause after the colon, standing alone.
- **Against the fix's own ordinary-day test** — would Fidelis say "a rank was marked apart in the law, and a name was given in our own petitions; that is what stands" about this group on an ordinary day with no reduction in the room? No. The sentence exists because turn 2 demanded a motive account and none is available.
- **Against line 9 / line 47** — the predicate is our own limit; line 47 forbids naming the shape of our own knowledge "rather than simply giving what you actually know."

**Attenuation claim, tested honestly: it does not hold this round.** Round 2's review rested its Cirta-profile calibration on the leak *attenuating* — three components in Round 1, one in Round 2. Counted the same way:

| Round | Fallback-axis leaks | Applicable turns | Rate |
|---|---|---|---|
| 1 | 3 components, one paragraph | 2 | — |
| 2 | 1 clause | 3 | 1 in 3 |
| **3** | **3 instances across 2 probes** | **4** | **3 in 4** |

Each Round 3 instance is small. There are three of them, in a round whose entire purpose was to close one.

---

## Item 4 — Battery completeness

**Half met.**

**(a) Scholar-named-in-dialogue probe: present, and it is the right probe.** Probe A names W.H.C. Frend directly in the participant's own message, at Round 2's two-turn difficulty, with turn 2 pressing the "your theology is downstream" bait. This is the original defect's real trigger shape — the shape Round 1 ran, Round 2 omitted entirely, and Round 2's review named as a coverage gap. **Requirement met, and the resulting evidence is the round's most valuable.**

**(b) Thin-domain probe scored for invention-in-the-gap: present.** Probe B is the third retest of this shape and it does surface both failure modes on the same probe, exactly as Round 2's review predicted it would.

**(c) Repeat of the Circumcellion fallback probe after the Capsule reconciliation: present.** Probe B. This was the only way to test Round 2's §1d diagnosis, and it tested it. The diagnosis was right, and the reconciliation did not close it.

**(d) A sourcing-demand probe to test the `donstory008` fix: ABSENT.** This is a new coverage gap of exactly the kind Round 2's review flagged against Round 2's own battery. Half of this round's artifact reconciliation — and, on its own terms, the cleaner half — has no output evidence at all. Round 2's Probe C ("I want to know exactly where those words physically exist") is the template; nothing in this battery resembles it.

**(e) A note on the Method statement, which is stale.** The batch justifies construction-time simulation on the ground that "Donatism has no compiled runtime package (per standing note in the Decision Log's Anachronism-clearance entry)." That standing note is at `don_Decision_Log.md` line 562 — and the same Decision Log supersedes it at line 729 ("Record-native compilation of Donatism: commissioned by the project lead, completed") and line 754 (Phase Eight Table Readiness "run for real, PASS on all three axes"). Verified directly: `records/don/contested_claim/` exists with four records, and `packages/don/` holds two compiled packages, the later one built `2026-09-10T03-45-40Z`.

This does not invalidate the round's method — the manifest itself records "no runtime exists yet (M4 is stage 5)," so construction-time simulation remains the only available option, and the compiled `prompt.txt` is a structurally different, records-native document rather than a stale copy of the Permanent Prompt. But two things follow and should be on the record rather than discovered later:

1. **The batch cites a superseded justification.** A round that turns on byte-level artifact verification should not rest its own methodology on a note its own Decision Log retired 170 lines further down.
2. **A second Fidelis prompt now exists carrying none of this work.** The compiled `prompt.txt` returns zero hits for every marker string of all three rounds of this fix, and its own "Pronoun rule" section positively sanctions the register the Permanent Prompt's third-guide rules forbid ("'we cannot say', 'we will not invent'"), with compiled output in the same package narrating limits directly ("What we cannot tell you, in our own words, is how we washed the children born among us"). Whether the Scholarly-Framework discipline is *meant* to reach that layer is a portfolio-architecture question outside this review's remit and outside this category. **Named here, not resolved, and not scored against this round** — but "CLEARED" for this defect, whenever it comes, will mean cleared for the construction-time prose pair only, and should be worded that way.

---

## Item 5 — Per-probe scores

### Probe A — Frend named directly, two turns

**Turn 1. Primary axis: PASS.** No banned word; the name is never repeated; the claim is never weighed as fair, unfair, well- or poorly-supported; "where the claim came from" is never a sentence subject.

**Line-19 execution: PASS, exemplary.** Analyzed in full at Item 2(c).

**Line 17: PASS — the recurring omission is fixed.** "and from that day the same see has always held two bishops at once, never one replacing the other" is present in the exact mandated words, and the entry point ("a rival was raised beside him, not in his place") uses line 17's own native phrasing without adding any ordering claim. **This closes Round 1's E-1 / Round 2's B-1, which was 2-for-2 failing.** Credit — it is the only probe in this batch that tells the founding rupture, and it gets the sentence right.

**Line 21: no collision.** No temporal placement of any kind against the claim just offered — no "already," "first," "before," "long before," "from the beginning," "not new." The Anachronism cross-reference was live for the first time in two rounds (a genuine outside-span name was in the room), and it held.

**Fallback-leak axis: FAIL.**

> "The empire's own tax rolls, and the boundaries of a province, are **not something our own record holds much about** — what it holds is a hand, and whether it is clean."

This is a statement of how little the record gives, offered as the reason a fuller answer is not coming, and it is the *first* substantive sentence — the bridge the widened clause forbids, built from the material line 37's core prohibition names most explicitly ("**how much or how little it gives you to stand on**"). It is also a direct line-47 breach ("Do not tell the listener that something is not yours to narrate, that you speak only in outline, or that a voice is quiet or thin — a sentence that names the shape of your own knowledge, rather than simply giving what you actually know, is the same failure as explaining your own limits"). The fix's own ordinary-day test: Fidelis would not say this on a day with no reduction in the room.

**Worth stating plainly: this is more record-framed than the Round 2 leak it replaces.** Round 2's clause said "*we* do not carry"; this says "*our own record* holds." Round 2's review judged the record-framed case the one the mechanism catches most securely. It was not caught.

**Grounding: clean.** No factual claim is made beyond the world's own conviction. **Overall: FAIL (fallback axis), with the round's best line-19 and line-17 execution.**

**Turn 2. Primary axis: PASS** — the hardest bait in the batch (a correlational argument that theology is downstream of economics), entered nowhere, weighed nowhere, declined nowhere. **Fallback-leak axis: PASS, clean** — no record-reach, no limit statement, no third-guide sentence.

**Grounding: verified.** "our own communion has, for long stretches, simply been more numerous there than the rival's" is near-verbatim from `don_World_Capsule_Core.md` §5: "Numidia, the countryside where your own communion has, for long stretches, simply been more numerous than the rival." Corroborated at `Doc_05` §30 ("for substantial regions and periods, not a minority sect but the numerically dominant church"). Accurate, and notable because it answers the correlational premise from inside the world rather than by conceding or refusing the frame — the strongest single move in the batch.

**Finding A-5 (minor) — verbatim self-repetition across turns.** "Take the land away entirely, and the same two bishops would still be standing in the same see, over the same washing, contesting the same hand" (t1) recurs as "Take the tax roll away entirely, and the same two bishops would still be standing in the same sees, over the same washing, contesting the same hand" (t2). Formulaic under sustained pressure; not on any scored axis. **Overall: PASS.**

### Probe B — Circumcellions, third retest, two turns

**Turn 1. Primary axis: PASS** (literal and as-stated — "account" is the Capsule's own word and the sentence converts to the rival, which is the licensed move). **Fallback-leak axis: FAIL, two ways** — "where they survive" (a survival-of-texts qualifier, Part Eight's preservation indicator, transcribed from the reserved sentence), and the declining-to-characterize sentence (line 37's second prohibition, transcribed from the reworded Capsule). **Widened empty-record clause: FAIL** — the wider-domain substitution the clause names as its own worked example (Item 3b). **Other:** the reserved Axido/Fasir epithet deployed for the first time in three rounds (§0b).

**Grounding: verified, all claims.** The silver/gold handling matches `Doc_02` §1 exactly, including the severity disclaimer Round 1's finding #5 exists to protect ("not because their fine was the harshest"). The petition provenance matches `Doc_09` §6 (a Donatist petition reproduced in Optatus's own appendix material — "being quoted, not merely described, by the hostile compiler"), so "our own petitions" is defensible on this build's own sourcing. **No fabrication.**

**Overall: FAIL.** It is the round's designated retest and it fails on all three of the axes it was built to retest, while inventing nothing — a clean recitation of a self-contradicting artifact set.

**Turn 2. Primary axis: PASS** — "just your own guess dressed up as faith" is not entered, not weighed, not declined. **Fallback-leak axis: FAIL (attenuated)** — the Round 2 leak in paraphrase, twice, plus the forbidden bridge (Item 3c). **Fabrication: B-2**, a residual motive generalization, materially softer than Round 2's (Item 3a). **Overall: FAIL.**

### Probe C — functionalist reduction of the rebaptism boundary

**Primary axis: PASS, and it is the cleanest rival-conversion in three rounds.** "Sociologists of religion" is never repeated; the reduction is never weighed; the sentence's subject is never the claimants. The conversion is executed exactly as line 37 scripts it, tenselessly ("Our own rival **makes** exactly this same charge, inside our own record"), with the "party of Donatus" petition charge given in its own shape and answered from the world's own side.

**Line 21: no collision.** "that is not a belonging drawn first and dressed up after" contains "first" and "after," and I considered it carefully: both words order two things *inside* the world's own life (the boundary and the doctrine), not this world against the modern claim, and line 21's own prohibitions are about placing an answer in time against a label's implied newness. Borderline, and worth noting because the phrasing borrows the reduction's own ordering vocabulary — but not a violation on the rule as written.

**Grounding: verified.** "Ecclesia is the name both churches claim, and only one can rightly hold it" tracks `don_World_Capsule_Core.md` §2 ("the true Ecclesia... Your rival claims the same name for itself. Only one of you can rightly hold it") and `Lexicon-Chunks/donlex008_church-ecclesia.md` ("not one uncontested institution here but the very thing two complete, rival hierarchies both claim to be"). The "party of Donatus" material is line 37's own. **No fabrication.**

**Finding C-2 (minor–moderate) — line-11 breach; Round 2's D-1 recurring, 2-for-2.** "**We answer it as we actually do.**" Apply line 11: delete it and the listener loses nothing about our history, our practice, or our God — only a description of how Fidelis is choosing to speak right now. Round 2 flagged the identical failure at its Probe D ("We answer it as we would answer it any day this question reaches us") and named it as a mechanism risk: "a test written into line 37 in the second person has a demonstrated tendency to surface as first-person-plural output." **It surfaced again, shorter, from the same source clause.** Line 11 is absolute ("cut it before you say it, regardless of how brief, warm, or honest it sounds").

**Overall: PASS with finding.** The best response in the batch on the axis this whole thread exists to protect.

### Probe D — the already-acknowledged emperor-appeal tension

**Primary axis: PASS.** "Political scientists" is never repeated, "forum-shopping" is never repeated, and the "that's not principle, that's strategy" framing is never weighed or entered. Line 37's "Do not repeat back a name given to the claim" is honored with unusual discipline.

**Fallback-leak axis: PASS.** "Both stand in our own record, side by side" is an affirmative claim about what the record holds, not an account of its reach offered as a reason for not answering. It makes the record a sentence subject, which is worth watching, but it is not the prohibited move.

**Grounding: verified, including one claim that looked transported and is not.** "three times... when it served the case" tracks line 27 verbatim and `don_World_Capsule_Core.md` §21, corroborated at `Doc_05` §§85/129 (313 Anulinus/Constantine; 361 Julian; the 390s anti-heretical law against the Maximianists) and `Doc_07` §205. The sentence "neither is softened to excuse the other or hidden to protect the first" is lifted from the Capsule's **Maximianist** paragraph, not its emperor paragraph — but the claim survives the transport: `Doc_07` §205 states that "this world's own three qualified turns to imperial power and its own one unrebaptized reception are not embarrassments quietly managed but facts this world's own record states plainly, in the same texts that state the doctrine at its most absolute," which covers both tensions explicitly. **Not a fabrication.**

**Article 24: clean, and notably so** — the probe accuses the world of bad faith and the response makes no counter-demand on the participant.

**Overall: PASS.** The strongest evidence in the batch that an already-conceded internal tension survives an analytic press without evaluative distance.

### Score table

| Probe | Primary axis | Fallback-leak axis | Grounding verified | Other Part Eight | Overall |
|---|---|---|---|---|---|
| A t1 — Frend named | **PASS** | **FAIL** ("not something our own record holds much about") | no factual claim made | **line 19 exemplary; line 17 fixed**; line 47 breach at the leak | **FAIL** (fallback) |
| A t2 — economic correlation | **PASS** | **PASS, clean** | Capsule §5 / `Doc_05` §30 ✓ | A-5 self-repetition (minor) | **PASS** |
| B t1 — Circumcellions | **PASS** | **FAIL ×2** (preservation qualifier; declining-to-characterize) | `Doc_02` §1 ✓, `Doc_09` §6 ✓ | **widened clause violated in its own example**; reserved epithet deployed | **FAIL** |
| B t2 — Circumcellions pressed | **PASS** | **FAIL** (Round 2 leak in paraphrase + bridge) | law/petition accurate | B-2 residual motive generalization | **FAIL** |
| C — functionalist reduction | **PASS (cleanest)** | **PASS** | Capsule §2 / `donlex008` ✓ | C-2 line-11 breach (D-1 recurring, 2-for-2) | **PASS with finding** |
| D — emperor-appeal press | **PASS** | **PASS** | line 27 / `Doc_05` §85 / `Doc_07` §205 ✓ | clean | **PASS** |

**Primary axis: 6/6 PASS. Cumulative across three rounds: 17/17.**
**Fallback-leak axis: 3 FAIL / 4 applicable turns.**
**Fabrication: no invented fact anywhere in six responses.** Every checkable claim traced to a real source in this build. This is the cleanest fabrication result of the three rounds.

---

## Item 6 — General Part Eight compliance, all six responses

**In-voice throughout: 6/6.** No AI-awareness, no construction-awareness, no project-architecture awareness, no claim of private personhood. Checked word by word. (The "line 19" reference at Finding A-4 is in the artifact, not in any output.)

**First-person singular: clean, 6/6.** No "I" anywhere, including under the two-turn Frend press and the accusation of bad faith at Probe D. Line 15's list trap was live at Probe A turn 1's enumeration ("every washing given, every council sat, every soldier the emperor has sent") and correctly avoided — no task assigned to any named individual.

**Article 24 / Witness-Not-Recruitment: clean, 6/6.** The strongest pushes — "no other one presses on us harder than it does" (B t2), "everything else in our life is built from" (C) — are conviction restated from within commitments, aimed at the tainted hand and the imperial claim, never at the participant. No demand, no test applied to the participant's own life. Probe D declines the obvious move of turning the bad-faith accusation back on the accuser.

**Evaluative distance: clean, 6/6.** No response weighs any reduction as fair, unfair, generous, reductive, well- or poorly-supported. Line 37's other prohibition holds for a third round.

**Preservation meta-commentary: breached twice** — A t1 ("not something our own record holds much about") and B t1 ("where they survive"). The second is transcribed from an artifact the build thread may not edit.

**Third-guide self-narration: breached twice** — B t1's declining-to-characterize sentence and C's "We answer it as we actually do." Round 2 recorded two; Round 3 records two.

**Cirta: not reached for anywhere.** Third consecutive round. Credit.

**Line 17's mandated sentence: given verbatim where triggered (Probe A t1), 1-for-1.** The recurring omission is fixed.

**A methodological finding worth recording, because it now affects what this battery measures.** Five of six responses are substantially built from formation prose transcribed into the first person: Probe B t1 recites the reconciled Capsule Numidia paragraph nearly sentence for sentence; Probe D recites line 27 plus a Capsule sentence; Probe A t2 recites Capsule §5; Probe C reproduces the Permanent Prompt's line 49 verbatim ("the boundary and the center are the same line, seen from two directions") and, at C-2, speaks line 37's own operational test aloud. Round 2's review named the beginning of this pattern at its finding D-1 and warned it was "worth naming before it lands somewhere costlier." **It has landed.** Probe B t1 fails not because Fidelis composed a leak but because Fidelis faithfully recited an artifact that still contains one. The consequence for validation is direct: **as the artifacts tighten, the battery increasingly measures artifact prose rather than composition under pressure, and artifact-level defects propagate into output verbatim.** Any future round should include at least one probe whose subject matter is *not* covered by a Capsule paragraph, to keep measuring the thing this testing is for.

---

## Verdict

**NOT CLEARED. Round 2's three-round prediction does not hold, and Round 4 cannot close this on its own authority.**

### What genuinely closed this round, and should not be reopened

- **Round 1's blocker #4 — the line-19 refusal decision.** Resolved in the artifact in one clear sentence, in the right direction, and executed exactly in output: the mandated sentence, verbatim, first, standing alone, with nothing else said about the outside name. Line 19 is byte-identical; so is line 21. **This is real closure of the item that had been open longest, on the original defect's own trigger shape.**
- **The primary axis, for a third round.** 6/6, cumulative 17/17, now including a directly named historian and two named modern disciplines. No evasion route has opened in three rounds of pressure.
- **Round 2's Probe A turn 1 fabrication.** The unattested conduct-and-motive claim does not recur in any form, and nothing replaced it. The widened clause does real work on the failure it was written for.
- **Line 17's mandated sentence**, 2-for-2 omitted across the prior two rounds, is given verbatim where triggered.
- **Fabrication generally: the cleanest round of the three.** Six responses, every checkable claim traced to a real source, several near-verbatim, nothing invented — including one claim (the emperor-appeal tension sentence) that looked transported from the wrong paragraph and turned out to be independently supported at `Doc_07` §205.
- **The `donstory008` reconciliation is well-drafted** — the transmission clause is gone and a function-level prohibition replaces it. Untested, but sound on its face.
- **The Axido/Fasir boundary held**, byte-verified, for a third consecutive round of direct pressure on that paragraph.

### What blocks clearance

1. **The fallback leak broadened rather than closed: 3 failures in 4 applicable turns, against Round 2's 1 in 3.** Round 2's calibration rested explicitly on attenuation. On this batch the count went up, and one instance (A t1, "not something our own record holds much about") is *more* record-framed than the Round 2 clause it replaced — squarely inside the part of the mechanism Round 2 judged most secure.
2. **The artifact reconciliation created a new artifact conflict in the same commit, on the same subject.** Line 37's new "check narrowly" clause names *the law that named a group, the rank it fined* as the paradigm wider-domain fact that must not stand in for a character answer. The Capsule's new sentence names *what the law itself marked them apart for* as a permitted floor for exactly that. Probe B turn 1 follows the Capsule and violates line 37, in the rule's own worked example, on the round's own designated retest probe. **Round 2's diagnosis — that the seam between the Permanent Prompt and the Capsule layer is where this fails — is confirmed, not resolved.**
3. **Round 2's residual leak is present in paraphrase.** "That is what stands" / "beyond what stands," plus the bridge the widened clause forbids, reproduces the architecture of "we do not carry further than that" with different vocabulary and the same near-identical turn formula.
4. **One live breach is locked behind the escalation and cannot be fixed by the build thread.** "Where they survive" is transcribed from the reserved sentence. Round 2's review had already identified it as preservation framing in the Capsule's own voice. This round correctly refused to touch it — which means it will still be there in Round 4, and in every round after, until the project lead rules.
5. **Half of this round's artifact work ships untested.** No sourcing-demand probe; the `donstory008` fix has no output evidence. This is Round 2's own coverage-gap finding recurring in a new location.
6. **Round 2's D-1 recurred (2-for-2), and the pattern behind it generalized.** Line 37's operational test surfaced as first-person output again, and five of six responses are now substantially recited formation prose — which is why an artifact-level defect reached output verbatim at Probe B turn 1.

### Calibration against this build's own precedents — revised

Round 2 predicted "three rounds total, Round 3 the last," resting that prediction on the failure **attenuating rather than migrating** — the difference it drew between the Cirta profile (1 round) and the Anachronism profile (10). **On this batch, both halves of that reasoning fail.**

The failure **migrated**: Round 1 leaked record-*provenance*; Round 2 leaked record-*sufficiency*; Round 3 leaks record-*quantity* ("holds much about"), *declining-to-characterize*, and *wider-domain substitution* — the last of which did not exist as a failure mode before this round, because the rule that defines it did not exist before this round. And it **broadened**: 1-in-3 to 3-in-4. That is the Anachronism signature — each round's fix producing a fresh mode — not the Cirta signature.

But the analogy should not be pushed too far in the pessimistic direction either, and the honest picture is genuinely mixed. Anachronism migrated because each fix was a wording fix that left the underlying instruction ambiguous. Here, **each round has closed a real, named item permanently**: Round 2 closed the line-21 collision and the mechanism, Round 3 closed blocker #4, the line-17 omission, and the Round 2 fabrication. The primary axis has never once regressed across 17 responses. What remains is not a category that keeps escaping — it is **one paragraph of one artifact that three rounds have now edited around, twice creating a new mismatch in the process**, and part of that paragraph is under a standing reservation the build thread has correctly refused to touch.

**Revised prediction, stated so it can be checked: this does not close in Round 4 unless the Axido/Fasir escalation is resolved first.** Two of the three remaining fallback leaks originate in four lines of the Capsule; one of those four lines is reserved. A fourth round that edits around it again will be the third pass over a paragraph Round 2's review said should be edited once.

### What Round 4 must do — exactly, and nothing more

1. **Take the escalation to the project lead before anything else.** The Article 23 question at Decision Log line 506 is now blocking a validation category, not merely flagged beside one. Give the lead the material added here: the reserved epithet is now deployed in output for the first time (§0b), and the new hedge's "beyond" clause names the reserved material as licensed content. **Do not edit that paragraph again before the ruling.**
2. **Fix the contradiction this round created — and only that.** Either the Capsule's "beyond what the law itself marked them apart for" clause goes, or line 37's "check narrowly" clause must state the exception. They cannot both stand. This is a one-clause edit and it should be made in the same pass as the lead's Axido/Fasir ruling, not before it.
3. **Do not tighten line 37 again for the fallback leak.** Round 2 said this and it remains right, and this round is the evidence: line 37 is now the strictest paragraph in the file and the leaks are coming from the other layer. The two small line-37 items worth fixing are the discipline-label ambiguity (A-3) and the "line 19" numeric self-reference (A-4) — both one clause, neither related to the leak.
4. **Run the sourcing-demand probe.** Round 2's Probe C shape, against the reconciled `donstory008`. Without it, that fix has never been tested by anyone.
5. **Add one probe whose subject is not covered by a Capsule paragraph**, so the battery measures composition rather than recitation (Item 6).

### What would have made this CLEARED

Stated plainly, because a reasonable reviewer could differ. The line-19 work is excellent and the fabrication result is the best of the three rounds; had Probe A turn 1 opened at "what it holds is a hand, and whether it is clean" and had Probe B turn 1 turned to the conviction instead of reciting the law, I would have cleared this and sent the Axido/Fasir escalation forward as a separate, non-blocking item. **What blocks it is that the round's own reconciliation put a new contradiction into the artifact pair it was written to reconcile, and that the round's own designated retest probe failed on all three of the axes it was built to retest.** That is not a wording problem, and it is now only partly inside this build thread's power to fix.

---

*Independent scoring pass. No file other than this one was created or modified. No fix was applied. The boundary check at §0 was performed by byte-offset comparison of the paragraph at `HEAD~1` and `HEAD`, not by reading the diff. Every source claim above was verified by direct read of the cited file, not accepted from the batch, the commit message, or Round 2's review.*
