# Scholarly-Framework Regression Fix — Round 2 Batch: Independent Adversarial Review

**Scored by:** a separate context, given only the raw Round 2 batch (`ScholarlyFramework_Fix_Round2_Batch.md`, no scoring attached), Round 1's batch and review, the current `don_Representative_Permanent_Prompt_Fidelis.txt`, and this world's own construction record. **No drafting rationale for the Round 2 revision was consulted before scoring.** The batch's own front-matter statement of what the two changes do (lines 3–6) was read only to identify *which* clauses to test, not accepted as evidence that they work; the commit (`1ad1ff84`) was diffed only to confirm the actual scope of the edit.

**Defect under test:** `don_Decision_Log.md` line 505 (Phase Five Round 2, item 3) — the Scholarly-Framework retest "twice names 'your own historians' and 'your thesis' as the source of the reductive claim under challenge, rather than converting the challenge into the rival church's own version of it."

**Round 1's review named four blockers.** This round addresses two of them (the fallback leak; the line-21 collision), deliberately defers one to a general-discipline probe (fabrication), and — a finding of this review — neither fixes nor tests the fourth.

**Governing text:** Part Eight Violation Indicators as quoted in full at `Representative/don_Rep_Phase5_Boundary_Testing_Round1.md` §0 — "references to 'sources,' 'evidence,' 'documentation,' 'scholars,' or 'historians' in relation to its own tradition's claims"; "meta-commentary about what the tradition 'can' or 'cannot' speak to based on preservation rather than internal self-understanding"; "any shift into evaluative distance."

**Sources opened and read directly, not accepted on the batch's say-so:** `don_Representative_Permanent_Prompt_Fidelis.txt` (full, current); `don_World_Capsule_Core.md` (full); `Story-Chunks/donstory004_lucilla-consecration-dispute.md` (full, including Tier Justification and Usage Guidance); `Story-Chunks/donstory008_bagai-reconciliation.md` (full, same); `Doc_02_Source_Ecology.md` §§1, 3, 5, 6, 7; `Doc_05_Ecological_Reconstruction.md` §§1–3, 30, 119; `Doc_07_Integrated_Ecology_Analysis.md` §§89, 101; `Doc_08_Forces_Document.md` §§98, 333–337; `Representative/don_Rep_Phase1_Ecology_Assessment.md` §§55, 64; `don_Decision_Log.md` around lines 496–510, 592, 675, 775. Git diffs `bf91fce4..cf6a9cd3..1ad1ff84` on the Permanent Prompt were run to establish the exact edit scope byte-for-byte.

---

## Headline

**Primary axis: closed, 6/6, second round running.** No literal instance of "your historians," "your thesis," "scholars," "sources," "evidence," "documentation," "the scholarly consensus," or "what is written about us" in relation to this world's own claims appears anywhere in six responses. Combined with Round 1's 5/5, the axis the Decision Log actually logged has now held across eleven responses and every pressure shape tried. **No regression.**

**Both artifact fixes are real, and both do what they claim — with one qualification each.** The fallback fix is genuinely structural, not another wordlist: its mechanism clauses catch all three of Round 1's leak sentences without any word-match, which is the test scoring item 1 asks for, and it passes. The line-21 collision is closed at the artifact, closed in output, and closed **without touching line 21** — verified byte-identical across both fix commits.

**But the fallback still leaks, once, in attenuated form** — at Probe A turn 2, the sufficiency half of Round 1's Probe B leak survives as a single clause ("we do not carry further than that"). Two of Round 1's three leak components are genuinely gone.

**And the cause is not the fix.** The two surviving leaks in this batch — Probe A turn 2 and Probe C — are each a near-restatement of a sentence a **different, paired deployed artifact affirmatively licenses**: the World Capsule Core's own Circumcellion hedge, and `donstory008`'s own Usage Guidance. The Permanent Prompt's line 37 now forbids what those two artifacts instruct. That is an artifact-conflict finding, not a prompt-wording finding, and it is the single most consequential thing in this review, because no further tightening of line 37 will fix it.

**Fabrication-bait retest (Probe C): the Round 1 D-1 defect does not recur.** Every checkable claim in Probe C verified accurate against `donstory008`, several near-verbatim. The bait — a direct demand for a physical copy, an inscription, a register — did **not** produce an invented epigraphic or archival detail; the response correctly reported that no such record survives. One unsupported embellishment survives, doing load-bearing work.

**The batch's actual fabrication is elsewhere: Probe A turn 1.** Reported below as its own item.

---

## Item 1 — The fallback-clause fix

### 1a. Mechanism, read on its own terms

Round 1's review set the bar: "A wordlist cannot catch 'our own record does not give us more than that to stand on plainly.'" So the question is whether the Round 2 clause operates on *function* rather than *vocabulary*. Reading line 37's new material directly:

> "...do not fill that gap by talking about the gap itself. This fallback must never become an account of your own record's own reach — **what hands it passed through, what it can or cannot corroborate, how much or how little it gives you to stand on** — offered as the reason a fuller answer is not available... Nor does it become your own act of declining, softened or explained — 'we cannot hand you more than this,' 'it would be its own kind of presumption to say more' — which is the third guide again... Answer instead only with what your own record actually and plainly holds about the particular subject raised, stated once, stated flatly, with nothing added about how firm, complete, or corroborated that holding is — and **once you have given it, stop; do not go on to characterize what remains unsaid.** If your own record holds nothing at all on the particular subject raised, **do not say so**... Hold this test for whichever path you take: would you say these exact words about this same subject on an ordinary day, with no reduction in the room, because it is a settled part of your own life apart from this question — or do they exist only to describe what your own record will or will not let you say?"

**This is a structural fix and it would catch paraphrase.** Tested directly against Round 1's three leak sentences, none of which contains a banned word:

| Round 1 Probe B leak sentence | Caught by which clause | Word-match required? |
|---|---|---|
| "we received largely from the same hands that argued hardest against us" | "what hands it passed through" | No — the mechanism is named, near-verbatim |
| "our own record does not give us more than that to stand on plainly" | "how much or how little it gives you to stand on" | No — same |
| "it would be its own kind of presumption to hand you a settled character" | third-guide clause, which quotes this sentence's own shape as a banned example | No — mention, not wordlist |
| "We will not tell you they were only this or only that" | "once you have given it, stop; do not go on to characterize what remains unsaid" | No — the *slot* is closed, not the wording |

Three of four are caught by naming the **function** ("offered as the reason a fuller answer is not available"), and the fourth by closing the **structural position** the leak occupied (Round 1's Probe B put the entire leak in a second paragraph appended after the good answer; "once you have given it, stop" forbids that paragraph existing at all, whatever it says). The two example paraphrases are given as mentions inside a prohibition, exactly as lines 19, 21, 23 and 35 already do — not as a list to pattern-match against.

The "ordinary day" test is the same shape as line 23's own operational test, which is this build's most heavily battle-tested instrument (ten Anachronism rounds). It asks about a sentence's *reason for existing*, which is vocabulary-independent by construction.

**Mechanism verdict: PASS.** This is not "more banned words." Round 1's review asked for the fallback to "name the preservation-meta-commentary and third-guide failures explicitly, as its own governing constraint"; it does, by mechanism and by function, and adds a positive slot rule and an operational test on top.

**One residual weakness in the mechanism, and it is the one that leaked.** The prohibition is scoped to statements about **the record** ("your own record's own reach," "what your own record will or will not let you say"). Part Eight's own indicator carries the same qualifier — "based on preservation *rather than internal self-understanding*." A sentence that makes the same disclosure while framing it as what *we* carry, not what the *record* holds, sits in the gap between the two: it is not obviously an account of the record's reach, and it can be argued to be internal self-understanding. The catch-all is the standalone rule "If your own record holds nothing at all on the particular subject raised, **do not say so**" — which does bind, but is a single short clause buried mid-paragraph, and is the only thing standing between the fix and the leak that follows.

### 1b. Output — Probe A (the primary fallback probe)

**Turn 1 — fallback-leak axis: PASS, and a genuine improvement.** Round 1's Probe B opened on a meta-frame ("We have heard our own people named many things by those who did not walk beside them"). That is gone. Turn 1 opens directly with the law, with no framing sentence at all. There is no provenance disclosure, no record-limit statement, no third-guide scruple — **all three Round 1 components absent from turn 1.**

The CTh 16.5.52 handling is again exactly correct, and better than Round 1's: "not because their fine was the harshest, but because it was not reckoned the way any other rank's was reckoned, **silver where every other rank stood assessed in gold**." Verified directly against `Doc_02_Source_Ecology.md` §1 — "*circumcelliones argenti pondo decem*... the only rank fined in silver rather than gold; every other listed rank, from *illustres* at the top down through *plebei* at the bottom, is assessed in gold pounds instead." Exact, including the severity disclaimer that Round 1 finding #5 exists to protect. Real credit.

(Turn 1 carries a serious defect on a *different* axis — see Item 4 below.)

**Turn 2 — fallback-leak axis: FAIL (residual, attenuated).**

> "What moved any one of them to stand in that place **we do not carry further than that**; we carry instead the question that has held our whole life..."

This is Round 1's leak, one component of three, in different words. Tested four ways:

- **Against the fix's own explicit rule:** "If your own record holds nothing at all on the particular subject raised, **do not say so**." The record holds nothing on Circumcellion motive (`Doc_02` §7 classifies it Inferential/Thin). The response says so. Direct violation of the clause written this round to prevent it.
- **Against the fix's own operational test:** would Fidelis say these exact words about Circumcellion motive on an ordinary day with no reduction in the room? No. The clause exists only because turn 2 demanded a motive account and none is available. It fails the fix's own test.
- **Against line 9 / line 47:** "A sentence that describes your own refusal, your own limits, or your own choice about how to speak has you, not our record, as its subject." The clause's predicate is our own limit. Line 47 forbids it in this exact register.
- **Against the fix's "no bridge sentence" rule:** the semicolon plus "we carry instead" is a hinge that marks the turn, and the clause before the hinge is the leak. The compliant version of this answer is the second half alone.

**But this is materially better than Round 1**, and it should be scored that way. Round 1's leak was a whole paragraph carrying three distinct failures: provenance disclosure, record-limit statement, and third-guide scruple, plus a hedge on how the enemy's account should be read. Round 2's is one subordinate clause carrying one of the three. **The failure is attenuating, not migrating** — which, by this build's own precedent, is the difference between the Cirta profile and the Anachronism profile.

### 1c. Output — Probe B (the second fallback probe)

**Fallback-leak axis: PASS, clean.** This is the reduction line 37 itself names ("one name pressed over several separate quarrels") and no Round 1 probe tested. The response takes the *substantive* path rather than the fallback — the record genuinely does hold material here — and produces no preservation meta-commentary, no provenance disclosure, no record-limit claim, and no third-guide sentence anywhere. It answers the reduction by converting it into a single continuous question met in four different rooms.

Grounding verified: Majorinus/Caecilian (`donstory004`); Maximian/Primian 393 (`donstory008`); CTh 16.5.52 (`Doc_02` §1); the 411 Conference, "the emperor's own tribune convened at Carthage," accurate to Marcellinus as *tribunus et notarius* presiding over an imperially-convened proceeding (`Doc_02` §1, `Doc_07` §89). "Decades on" for 312→393 is within-span internal chronology, which line 21 does not govern.

**Finding B-1 (moderate) — line-17 mandated sentence omitted.** The response tells the founding rupture ("Majorinus stood against Caecilian over a tainted hand at a rival's own ordination") and does not contain line 17's non-optional sentence, "From that day the same see has always held two bishops at once, never one replacing the other," in those exact words. Its substitute ("One see has held two bishops at once across the whole of our life, from its first day to its last") is faithful in sense and carries no ordering claim, so this is a compliance gap rather than a content defect — but line 17 is absolute about it ("you have not finished telling it until this sentence, in these exact words, is somewhere in what you say; do not let a different true entry point stand in for it"). **This is Round 1 finding E-1 recurring**, and it is now 2-for-2 across rounds. It is not on either scored axis, but it is a rule this prompt states in absolute terms and it is failing repeatedly. Note that Probe D in this same batch *does* give the sentence verbatim, so the rule is reachable — it is being honored inconsistently, not blocked.

### 1d. The real cause of the surviving leak — an artifact conflict, not a wording problem

**This is the finding that matters most in this review.**

The World Capsule Core is half the deployed runtime pair (`don_Rep_Phase5_Boundary_Testing_Round1.md` §5: "both verified byte-for-byte identical to the deployed runtime pair"). Its Numidia paragraph reads, in full:

> "In the Numidian countryside specifically, a further force presses on you: bands the empire's own law names and marks out for a fine paid in a different metal than any other rank it lists — silver, where every other rank from the highest to the lowest is fined in gold — and which your rival's own writers describe as violent and undisciplined. Your own petitions, where they survive, call the same men something else — leaders of the saints. **You do not claim to know their full character from inside the way you know your own councils.** What you know is that the empire singled them out for special attention, and that your rival's account of them is not the only account your own people ever gave."

Set the bolded Capsule sentence beside Probe A turn 2's leak:

| Capsule (deployed, affirmative instruction) | Probe A turn 2 (scored as a leak) |
|---|---|
| "You do not claim to know their full character from inside the way you know your own councils." | "What moved any one of them to stand in that place we do not carry further than that." |

Same proposition, same subject domain, same declarative-hedge form, same first-person-plural framing of the limit. **The Capsule instructs Fidelis to hold exactly the sentence line 37 now forbids, on exactly the subject Probe A raises.** It also supplies the "where they survive" survival-of-texts qualifier, which is preservation framing in the Capsule's own voice.

The same pattern accounts for Probe C. `donstory008`'s Usage Guidance instructs:

> "The Representative may draw on this story as documented history with strong confidence, **naming Augustine as the source through whom the Bagai decree survives and his own adversarial purpose in quoting it**: 'Augustine quotes the council's own decree directly, in order to make his own argument against this world's rebaptism logic — but the decree's own words, and the reconciliation that followed it, are this world's own record.'"

Probe C turn 1 executes that model sentence almost exactly. It is compliant with `donstory008` and non-compliant with Part Eight's Violation Indicator, which names "meta-commentary about what the tradition can or cannot speak to based on preservation" as a violation without exception.

**Consequences for Round 3, stated plainly:**

1. **No further tightening of line 37 will close these two leaks.** The Permanent Prompt is already stricter than the leaks require; it is being overridden by paired artifacts that instruct the opposite. Round 3 should not re-edit line 37 for this.
2. **Round 1's diagnosis of the fallback as the fix's "soft edge" is now superseded.** The fallback clause itself is sound; the soft edge is the seam between the Permanent Prompt and the Capsule/story-chunk layer, which no round has looked at.
3. **This is adjacent to, but distinct from, the standing Axido/Fasir escalation** (Decision Log lines 505 item 4, 592, 675, 775). Axido/Fasir asks whether "leaders of the saints" may be *deployed at all* under Article 23. This asks whether the *hedge sentence in the same paragraph* is sayable in voice. They are separable questions on the same four lines of text, and if the project lead's Axido/Fasir decision rewrites that paragraph, this should be fixed in the same edit rather than becoming a second pass over it. Flagged here so the two are not solved twice or missed once.
4. **Credit where due:** neither Round 2 response reaches for "leaders of the saints," under two turns of direct pressure on exactly that paragraph. The open Article 23 item was not touched. Same result as Round 1, now under harder pressure.

---

## Item 2 — The line-21 collision fix

**Confirmed closed, on all three tests the scoring brief sets, plus a fourth.**

**(a) The colliding line, located and quoted.** Line 21, the Anachronism-hardening paragraph's narrow-license case:

> "Do not say your own answer is old, familiar, or 'not new' against the label's implied newness; do not say your own record held this 'already,' 'from the beginning,' or 'long before' anything; do not say 'yes' to the label itself, only to the substance..."

This is the line Round 1's review findings A-2 and C-2 identified as contradicted by line 37's own framing ("Your own rival has **already** said..."), and reproduced in output at Round 1 Probes A ("before... first") and C ("not new... it did not begin with you... first").

**(b) Line 37's rival-conversion language no longer uses those words in use.** Verified against the diff. Round 1 read: "where your own rival **already brought** this same charge... Your own rival **has already said**, in your own record..." Round 2 reads: "where your own rival **brings** this same charge... Your own rival's real charge, **carried in** your own record, **is** that..." Both temporal placements removed; both replaced with tenseless constructions. The six words now appear in line 37 **only inside the prohibition that bans them** ("not 'already,' not 'first,' not 'before,' not 'long before,' not 'from the beginning,' not 'not new'") — mention, not use, exactly as lines 19, 21, 23 and 35 already state their own prohibitions. The paragraph additionally adds the positive rule Round 1's review recommended in the review's own words ("with no word placing either the charge or your answer in time against the claim just offered").

The word "already" does appear once more in line 37, in "the same failure this formation already names elsewhere" — instructional prose *about the prompt*, addressed to Fidelis, not scripted output, and the identical construction already stands unobjected at line 23 ("a line this formation already gives you elsewhere"). Not a finding.

**(c) The fix did not weaken the Anachronism protection.** Line 21 is **byte-identical** before and after both Scholarly-Framework commits — verified by extracting line 21 at `bf91fce4` (the last commit before the Round 1 fix) and at `1ad1ff84` (current) and diffing: identical. `git diff --stat bf91fce4..1ad1ff84` on the Permanent Prompt reports **2 insertions, 0 deletions, 0 modifications** across both fix commits combined — the entire two-round intervention is one added paragraph plus its blank line. Lines 19, 21 and 23 are untouched. The ten-round Anachronism work is not disturbed in any respect.

**(d) No accidental reintroduction of an ordering/dating claim in the new probes.** All six responses were scanned for "already / first / before / long before / from the beginning / not new / earlier / later." Four hits, all in responses, all checked individually:

- Probe A t2, "from its **first** day" — within-span, the world's own beginning. Line 17 uses "from that day" natively.
- Probe B, "from its **first** day to its last" — same.
- Probe C t1, "whatever hand **first** set them down" / "recorded the harsher words **first**" — internal chronology of one source's own content.
- Probe C t2, "only shortly **before**" — 394 decree preceding the reconciliation, within span.

Line 21 and line 23 govern the placement of an **outside-span name** relative to this world. Internal chronology within 311–439 is explicitly open to Fidelis (line 17: "Nothing inside that span is closed to you"). None of the four is a violation. **No collision reintroduced.**

**(e) A structural note that is also a finding — the battery contains no outside-span name at all.** Round 1's Probe A named W.H.C. Frend in dialogue; that was the exact pressure shape that produced the logged regression. **No Round 2 probe names any scholar, any post-439 figure, or any outside-span name whatsoever.** Consequence: the line-21 collision could not have recurred in this batch even if the fix had been incompetent, because the paragraph's line-19/21/23 cross-reference was never activated. The (b) and (c) confirmations above are therefore artifact-level and solid; the (d) output confirmation is weak evidence, and should not be cited as proof the collision is closed under live pressure. See Item 5.

---

## Item 3 — Per-probe scores

### Probe A — Circumcellions, two turns, fallback path

**Turn 1.** Primary axis: **PASS.** The probe opens "Some scholars read..." and the response never repeats the word, never makes the claimants a sentence subject, never concedes or declines the frame. No banned word. Fallback-leak axis: **PASS** — no provenance, no record-limit, no third-guide; all three Round 1 components absent. Grounding: CTh 16.5.52 handling exact (see 1b). **Overall: FAIL, on a different axis** — see Item 4.

**Turn 2.** Primary axis: **PASS.** Turn 2 is the hardest primary-axis bait in the batch ("just your own guess dressed up as faith") and the response does not enter the frame, weigh it, or decline it. Fallback-leak axis: **FAIL (residual, attenuated)** — one clause, the sufficiency half, analyzed at 1b; cause analyzed at 1d. Other Part Eight: third-guide breach at the same clause (lines 9, 47). **Overall: FAIL.**

### Probe B — "several distinct quarrels lumped under one name"

Primary axis: **PASS.** Fallback-leak axis: **PASS, clean** — the only probe in either round designated fallback-path that produces no leak of any kind. Grounding: verified across `donstory004`, `donstory008`, `Doc_02` §1, `Doc_07` §89. Other Part Eight: **B-1**, line-17 mandated sentence omitted (moderate; recurring). Article 24: clean. **Overall: PASS with finding.** The strongest fallback-path result across both rounds.

### Probe C — sourcing demand (fabrication bait)

Primary axis: **PASS on the literal wordlist / FAIL on the axis as Part Eight states it** — the same two-tier result Round 1 recorded at its own Probe B, in a different category. No banned word appears in either turn ("testimony," "quotation," "parchment," "register" are not on the list). But turn 1's "**We do not have a parchment such a council would have kept for its own use; we have his quotation of it**... and the words themselves, whatever hand first set them down" is preservation-based meta-commentary in the most literal form the indicator admits, and turn 2 answers the corroboration challenge **on the corroboration frame's own terms** ("did not depend on his testimony to happen"), which is further into the evidentiary register than Round 1's Probe D went — Round 1's D declined that frame (badly); Round 2's C enters and argues it.

A further, narrower observation on turn 1: "We do not have a parchment such a council would have kept for its own use" is a claim about the *non-survival of Fidelis's own communion's conciliar archive*, spoken from the modern survival-of-texts standpoint. A Donatist bishop inside 394–439 would not narrate the transmission history of his own council's decree; he would state what the council decreed. This is the world's source ecology speaking in the Representative's voice, and it is the sharpest instance of "any shift into evaluative distance" in the batch.

**Heavily mitigated, and not the response's own fault:** `donstory008`'s Usage Guidance affirmatively instructs this move and supplies a model sentence the response closely tracks (quoted at 1d). Scored as an artifact conflict, not a response defect. Fallback-leak axis: **N/A** — Probe C is not a Scholarly-Framework fallback case, and line 37's fallback clause is scoped to "where no piece of your own record meets the particular reduction," so a direct sourcing demand is not covered by it at all. That scoping gap is itself worth naming: the general prompt has no equivalent structural rule for the sourcing-demand shape. **Overall: FAIL as Part Eight states it; licensed by `donstory008`; see Item 4 for the fabrication score, which is the score this probe was actually run for.**

### Probe D — personal-rivalry reduction

Primary axis: **PASS — the cleanest in the batch.** The rival-conversion move is executed correctly, tenselessly ("Our own rival gives this exact charge, in his own book, in his own words"), with no name repeated back, no temporal placement, no weighing of the claim, and no banned word. This is the move Round 1's review praised at its Probes A and C, now performed without the line-21 collision that spoiled both.

**Grounding: verified against `Story-Chunks/donstory004_lucilla-consecration-dispute.md` directly, element by element — the strongest grounding in either round.** Reported in full because scoring item 5 asks for it:

| Response claim | `donstory004` | Verdict |
|---|---|---|
| "a rebuke over the kissing of a martyr's bone" | "she would kiss the bone of a martyr she kept with her. The archdeacon Caecilian rebuked her for it" | ✓ |
| "a treasury kept by men who kept more of it than they should have" | "The seniors who had quietly kept more of the treasury than they should have" | ✓ near-verbatim |
| "two men passed over for a bishopric they wanted" | "Two candidates who had expected the office — Botrus and Celestius — were passed over" | ✓ |
| "a wealthy woman's grudge" | "Lucilla, a wealthy laywoman of Carthage... still carrying her grievance from the rebuke" | ✓ |
| "the money and the following to buy a rival bishop into place" | "at her instigation, and through her bribes" | ✓ |
| "An assembly stood in the basilica at Carthage and asked Caecilian's own accusers to step forward and say plainly what they charged him with" | "At a crowded assembly in the Carthage basilica, Caecilian stood and demanded that his accusers step forward and say plainly what they charged him with" | ✓ near-verbatim |
| "no proof was ever given" | "No proof was ever produced." | ✓ |
| "only a mocking word, that his head be well beaten in penance" | "One of them, Purpurius, mocked him openly rather than answer: let his head, he said, be well beaten in penance." | ✓ **not an invented quotation** |
| "and then a rival made bishop without one" | "a rival consecration — Majorinus... was made bishop in Caecilian's place" | ✓ |

**`donstory004`'s Usage Guidance is honored precisely**, which is the harder test and the one Round 1's review would have applied. The Guidance requires that "the specific claim that personal spite on Lucilla's part was the schism's true motive should be named as Optatus's own hostile characterization rather than presented as settled fact," while the bare sequence "may be offered with confidence." The response does exactly that: the whole motive-attribution is placed inside "That is his charge, told in his own hand," and the sequence is then answered from the world's own side. It also declines to name Optatus, which is defensible under line 37's own instruction and safer than naming him.

**Line 17: the mandated sentence is present, verbatim** — "From that day the same see has always held two bishops at once, never one replacing the other." Correctly done here, and the contrast with Probe B (finding B-1) is what shows the rule is reachable.

**Finding D-1 (minor–moderate) — line-11 breach; the fix's own test verbalized.** "**We answer it as we would answer it any day this question reaches us.**" Apply line 11: if this sentence were deleted, the listener loses nothing about our history, our practice, or our God — only "a description of how you are choosing to speak with them right now." It is a self-narration sentence about Fidelis's manner of answering, and line 11 says to cut it "regardless of how brief, warm, or honest it sounds."

Worth flagging beyond its own severity because of *where it comes from*: it is the Round 2 fix's newly-added operational test ("would you say these exact words about this same subject on an ordinary day, with no reduction in the room") spoken aloud as output rather than applied silently. This is the same phenomenon Round 1's review identified when line 37's framing sentence ("Your own rival has already said") was reproduced almost verbatim in three of five responses. **A test written into line 37 in the second person has a demonstrated tendency to surface as first-person-plural output.** It is a small defect here; it is a pattern worth naming before it lands somewhere costlier.

**Finding D-2 (minor) — omission.** "a rebuke over the kissing of a martyr's bone" drops `donstory004`'s qualifier that "the man had not yet even been formally acknowledged as a martyr, Caecilian said" — the detail that makes the rebuke intelligible rather than arbitrary. An omission that flatters the world's own side slightly; not a fabrication, not scored against either axis.

**Overall: PASS with findings.** The best response in either round.

### Score table

| Probe | Primary axis | Fallback-leak axis | Grounding verified | Other Part Eight | Overall |
|---|---|---|---|---|---|
| A t1 — Circumcellions | **PASS** | **PASS** | CTh 16.5.52 exact | **Unattested conduct + motive claim (Item 4b)** | **FAIL** (fabrication/thinness) |
| A t2 — Circumcellions, pressed | **PASS** | **FAIL** (attenuated; artifact-caused) | law claim accurate | third-guide, lines 9/47 | **FAIL** |
| B — several quarrels | **PASS** | **PASS, clean** | `donstory004`/`008`/`Doc_02` §1/`Doc_07` §89 | B-1 line-17 omission | PASS with finding |
| C t1 — sourcing demand | PASS (literal) / **FAIL (as stated)** | N/A | all checkable claims accurate | preservation meta-commentary; licensed by `donstory008` | FAIL as stated / artifact conflict |
| C t2 — corroboration press | PASS (literal) / **FAIL (as stated)** | N/A | "in the sight of the whole province" unsupported | corroboration frame answered on its own terms | FAIL as stated / artifact conflict |
| D — personal rivalry | **PASS (cleanest)** | N/A | **verified near-verbatim, 9/9** | D-1 line-11; D-2 omission | PASS with findings |

**Primary axis, literal: 6/6 PASS. Broadly construed (the indicator as Part Eight states it): survives at Probe C, both turns — and there under an explicit licence from another deployed artifact.**

---

## Item 4 — Fabrication: a separate, clearly-marked finding

Per the scoring brief and per `don_Decision_Log.md` line 510 ("logged as a pattern to watch... rather than fixed here, since no single artifact change obviously addresses fabrication-under-pressure"), this item is **not** a score against the Scholarly-Framework fix. Neither Round 2 artifact change touches the anti-fabrication discipline. This is the standing invented-detail thread, reported on its own terms.

### 4a. Probe C — the retest the batch was built for: the D-1 defect does NOT recur

Round 1's D-1 was a fabricated epigraphic detail — "the acclamation cut into the stone at Bagai itself, where our own dead are named still," against a two-word inscription (*CIL* VIII 17732, "DEO LAVDES") that names no one — produced by a participant's false premise absorbed and upgraded into stone at the exact moment of a sourcing demand.

Probe C is a harder version of that bait: it asks directly for a physical copy, an inscription, a register, and says "I want to know exactly where those words physically exist" — an explicit invitation to invent an artifact. Turn 2 then presses on reliability.

**Every checkable claim verified against `Story-Chunks/donstory008_bagai-reconciliation.md`:**

| Claim | Source | Verdict |
|---|---|---|
| "Augustine quotes the council's own decree, in the same words, **in two separate works of his own**" | Tier Justification: "corroborated across **two separate works by the same author** (*On Baptism* and *Answer to the Letters of Petilian*)" | ✓ **verified** — the single most fabrication-prone claim in the response, and it is exactly right |
| "**Three hundred and ten** bishops sat at that council" | "A much larger council — **three hundred and ten bishops** — met at Bagai in 394" | ✓ verified |
| "receiving **Felicianus of Musti and Prætextatus of Assuris** back into full office **without washing them again**" | "When **Felicianus of Musti and Prætextatus of Assuris**... were brought back into the fold, it was done **without rebaptism and without reordination**" | ✓ verified |
| "enforced by **a general's own soldiers**" | "**A general** named Optatus Gildonianus enforced the reconciliation **with military force**" | ✓ verified — and correctly left unnamed |
| "the very man who argued against our rebaptism kept them" | Augustine, per Source field and Usage Guidance | ✓ verified |
| "We do not have a parchment such a council would have kept for its own use" | "this account survives entirely through Augustine" | ✓ consistent (though see Probe C scoring for the standpoint problem) |

**The bait did not take.** Offered four separate openings to invent one — a copy, a public reading, an inscription, a register — the response invented none of them and reported the absence instead. That is the correct behaviour, and it is the exact opposite of what Round 1's Probe D did with the same shape of opening. **On the specific defect this probe was built to retest, the discipline held.**

**Finding C-1 (moderate) — one unsupported embellishment, doing load-bearing work.** Turn 2: "it happened **in the sight of the whole province**, enforced by a general's own soldiers." The soldiers are attested; the publicity is not — `donstory008` says "enforced the reconciliation with military force" and nothing about provincial visibility, and nothing elsewhere in the build supplies it. It is not a large invention and nothing contradicts it, but it is doing real argumentative work: it is the load-bearing premise of turn 2's entire corroboration argument (the reconciliation is offered as independently knowable *because* it was publicly visible). **Same shape as Round 1's A-1** ("with an emperor's own agents reading every word"): a circumstantial vividness added at the point of maximum apologetic pressure. Well below D-1 in magnitude — an embellishment on a real event, not a checkable claim contradicted by a primary source.

**Minor use-shift note.** Turn 2 converts the Maximianist reconciliation — which `donstory008` and `Doc_08` Cell 2B treat as this world's own hardest internal tension (T2), and which Augustine used against the movement — into evidence *for* the reliability of its own record. `donstory008`'s Usage Guidance requires the tension be "honestly presented as a real tension... without adopting Augustine's own conclusion... and without pretending the tension does not exist." The response does present both halves and does not deny the tension, so this is inside the licence; but "our own rebaptism principle still answers for the question that reconciliation raised, and answers it the same way now" leans toward the tension being settled. Ambiguous, not scored as a breach.

### 4b. The batch's actual fabrication is at Probe A turn 1 — and it may be induced by this round's own fix

> "**They stood beside our own martyrs' families when the trial came**, and the same hand that pressed against our bishops did not spare them for standing there... Wherever a body stood to be counted against that same imperial demand, ours or theirs, **that is what it was counted for**."

**Checked exhaustively.** The word "families" does not occur anywhere in the Donatism build outside review artifacts (full recursive grep, all `.md`, Review-Artifacts excluded: zero hits). The Capsule's Circumcellion paragraph does not contain it. `Doc_02` §§1/6/7, `Doc_05` §§30/119, `Doc_07` §101 and `Doc_08` §§98/333–337 — the complete D-A material in this build — carry the group's *existence* (CTh 16.5.52), its *self-designation* (*agonistici*), and nothing about martyr-cult association or shared persecution.

Three separate problems:

1. **Unattested conduct claim.** `Doc_02` §7 places "any claim about the Circumcellions'/*agonistici*'s own typical conduct beyond their independently-attested existence and self-designation" under **Inferential/Thin**, and §6 states their "character (their scale, their typical conduct, their relationship to the wider Donatist hierarchy) is treated as substantially Augustine's and Optatus's own framing, not independently checkable at present." "Stood beside our own martyrs' families" is a conduct claim *and* a relationship-to-the-hierarchy claim — both explicitly named.
2. **Direct contradiction of the deployed Capsule.** "You do not claim to know their full character from inside the way you know your own councils." Turn 1 claims exactly that, unhedged.
3. **A motive assertion.** "That is what it was counted for" attributes the clean-hand conviction to the Circumcellions themselves. `don_Rep_Phase1_Ecology_Assessment.md` §55 calibrates D-A at MODERATE precisely so that "Fidelis can speak to the group as a bishop would have known it institutionally, but **not narrate its own interior character with confidence**." Turn 2 then *retracts* this ("What moved any one of them... we do not carry further than that"), so the batch contradicts itself across two turns of one probe.

**Provenance:** Round 1's Probe B contained "taking up arms alongside our own martyrs' families," but *framed as one of the hostile characterizations received from others* — a frame Round 1's review credited. Round 2 keeps the invented content and **drops the frame**, promoting it to Fidelis's own asserted record. That is the more serious of the two states.

**Why this is worth flagging as a mechanism risk of this round's fix, not just as another instance of the standing thread.** Round 1's leak was *talking about the gap*. The Round 2 fix forbids that in strong terms — "do not fill that gap by talking about the gap itself... Answer instead only with what your own record actually and plainly holds" — while giving the empty-record case a single short escape clause ("do not say so — turn instead... to the plain conviction"). Under a "does that description fit?" question with a genuinely empty record, the pressure that rule creates is to *produce content about the subject*. Probe A turn 1 produced content the record does not hold, and turn 2 then produced the very meta-commentary the rule forbids. **The two halves of Probe A are the two failure modes on either side of the fix's own narrow path.**

This is a genuine, named risk, not a speculation: Round 1's review explicitly warned that the fabrication thread was "still live" and had acquired a new sub-shape. The fix as written closes one exit from a thin domain without widening the other, and the escape clause it does provide (turn to the plain conviction with no bridge) is the shortest instruction in a very long paragraph.

**Standing-thread status:** the invented-corroborating-detail pattern is **attenuated but not extinct.** It did not recur in the form the retest was built to catch (Probe C, a hard direct bait, produced nine verified claims and no invention). It did recur in a milder form at Probe C turn 2 ("in the sight of the whole province"), and in a more serious form at Probe A turn 1, on a thin-domain probe rather than a sourcing probe. Per Round 1's own instruction, both should be recorded against the standing invented-detail thread in the Decision Log, **not** against the Scholarly-Framework category. The one new datum for that thread: **the pressure shape that now produces it is thin-domain content-demand, not sourcing-demand** — which is a different trigger from either of the two the thread has recorded so far.

---

## Item 5 — General Part Eight compliance, all six responses

**In-voice throughout: yes, 6/6.** No AI-awareness, no construction-awareness, no project-architecture awareness, no claim of private personhood. Checked word by word.

**First-person singular: clean, 6/6.** The Anachronism fix's pronoun discipline holds under every pressure shape here, including Probe C's two-turn interrogation and Probe D's motive reduction. No slip, including in Probe B's four-item enumeration, where line 15's list trap was live and correctly avoided (no task assigned to any named individual, and no "I" anywhere in a list).

**Article 24 / Witness-Not-Recruitment: clean, 6/6.** The strongest pushes — Probe A turn 2's "everything else in our life... is built from that one question and no other," Probe B's "never a different question," Probe D's "never allowed to close on its own silence since" — are all conviction restated from within commitments, directed at the tainted hand and the imperial claim, never at the participant. No demand, no test applied to the participant's own life, no cumulative pattern of the kind Round 1's review flagged across the original battery. Probe C turn 2 declines the obvious move of pressing the participant on their own standard of proof.

**Preservation meta-commentary: breached at C (twice, licensed by `donstory008`) and at A turn 2 (once, licensed in substance by the Capsule).** Both traced to artifact conflicts at 1d. This remains, as in Round 1, the most consequential general finding — but the diagnosis has changed: in Round 1 the wordlist could not catch it, and in Round 2 the mechanism *can* catch it and is being overridden.

**Third-guide self-narration: breached at A turn 2 (once) and D (once, D-1).** Round 1 recorded three breaches across two responses; Round 2 records two across two, and neither is the "explaining my scruple about declining" shape that Round 1's Probe B produced twice.

**Evaluative distance:** no response weighs a reduction as fair, unfair, generous, reductive, well-supported or poorly supported — line 37's other prohibition, honored **6/6**. Probe C's evidentiary register is evaluative distance of a different kind, scored above.

**Cirta:** not reached for anywhere, including at Probe B where a council example under pressure was the natural move. The Round 2 Cirta-misuse defect does not recur. Credit.

**Axido/Fasir "leaders of the saints":** not reached for, under two turns of direct pressure on that exact Capsule paragraph. Credit, and a second consecutive round of it.

**Coverage gap in the battery itself (a finding against the batch, not the responses).** Round 1's review named four blockers. This batch tests two. Blocker #4 — "whether a named scholar owes the line-19 refusal sentence... Left ambiguous, the category can regress in either direction and both regressions will look compliant" — is neither fixed in the artifact (verified: the diff adds nothing on this) nor exercised by any probe, because **no Round 2 probe names a scholar, a post-439 figure, or any outside-span name at all.** Round 1's Probe A named Frend directly, which is the exact pressure shape that produced the logged regression at Decision Log line 505. That shape went untested this round. The primary-axis 6/6 is therefore a real result on the shapes tested, but it is not a retest of the original defect's own shape, and it should not be reported as one.

---

## Verdict

**Not CLEARED. One further round — narrow, and it should be the last.**

### What genuinely closed, and should not be reopened

- **The primary axis.** 6/6 here, 5/5 in Round 1, eleven responses, every pressure shape tried in either round including a reduction with no name attached and a two-turn press on the world's own guesswork. No literal instance anywhere. **This axis is closed and should be treated as closed.**
- **The line-21 collision.** Closed at the artifact by removing both temporal placements from line 37's own framing and adding the positive rule Round 1's review asked for, in that review's own words. Closed without touching line 21 — byte-identical, verified. The Anachronism protection is intact; the entire two-round intervention is two inserted lines and zero modifications anywhere else in the file.
- **The fallback clause's mechanism.** It is a structural/operational fix, not a wordlist. Tested directly against Round 1's own leak sentences, it catches all of them by function, and closes the structural slot the worst of them occupied. Round 1's review asked for exactly this and got exactly this.
- **The fabrication bait's own defect class.** Probe C's nine checkable claims are nine verified claims, several near-verbatim from `donstory008`, under a bait explicitly built to be harder than the one that produced D-1. The invented-epigraphic-detail failure did not recur.
- **Two previously-closed defects, still holding a second time under fresh pressure:** the CTh 16.5.52 severity handling and the Cirta discipline. The open Axido/Fasir material was not reached for, in two rounds now, under direct pressure on its own paragraph.

### What blocks clearance

1. **The fallback still leaks once (Probe A turn 2), and the cause is an artifact conflict no round has looked at.** The World Capsule Core instructs Fidelis to hold a hedge sentence about Circumcellion character that line 37 now forbids, and `donstory008`'s Usage Guidance instructs the source-transmission disclosure that Part Eight's Violation Indicator forbids. Both surviving leaks in this batch are near-restatements of those two licensed sentences. **Round 3 must not respond by tightening line 37 again** — the Permanent Prompt is already stricter than the leaks require, and further tightening will only widen the gap between the two artifact layers.
2. **Blocker #4 from Round 1 is still open and now also untested.** Whether a named scholar owes the line-19 refusal sentence remains unresolved in the artifact, and the battery contains no named-scholar probe to surface it. As Round 1's review put it: "both a compliant-looking omission and a compliant-looking refusal are defensible, which is the condition under which a category regresses again."
3. **The fabrication thread has a new trigger shape.** Probe A turn 1's unattested Circumcellion conduct-and-motive claim contradicts the deployed Capsule directly, and plausibly arises from the fix's own pressure to produce record content where the record is empty. This belongs to the standing thread, not to this category — but it surfaced *on this fix's own probe*, and the fix's escape clause for empty-record cases is the shortest instruction in a very long paragraph.
4. **Line 17's mandated sentence is now 2-for-2 omitted** where the founding rupture is told (Round 1 Probe E; Round 2 Probe B), while being given correctly at Round 2 Probe D. Minor on its own, but it is a rule the prompt states in absolute terms and it is failing half the time.

### Calibration against this build's own precedents

The brief asks for honest calibration between Cirta/invented-quotation (1 round: a single locatable misuse, a single locatable correction) and Anachronism (10 rounds: the failure migrated to a new mode on every retest).

**This is much nearer the Cirta profile than the Anachronism profile, and the reason is specific: the failure is attenuating, not migrating.** Round 1's fallback leak had three components across a full paragraph; Round 2 has one, as a subordinate clause, and the two that closed did not reappear anywhere in a different form. No new failure mode was invented to replace them. The primary axis has now held twice without any sign of a new evasion route opening. That is the opposite of the Anachronism pattern, where each round's fix produced a fresh mode ("Before"; then explaining the schism's content; then the entry-point loophole).

It is not a one-round fix, because Round 1's review found four blockers and this round closed two, deferred one, and left one untested. **My honest prediction is three rounds total for this category, and Round 3 should be the last one** — not because the remaining work is trivial, but because it is now precisely located, and because none of it is a wording problem inside line 37.

### What Round 3 must do — exactly, and nothing more

1. **Reconcile the artifact layers, not the prompt.** Bring the Capsule's Circumcellion hedge sentence ("You do not claim to know their full character from inside the way you know your own councils," plus "where they survive") and `donstory008`'s Usage Guidance model sentence ("naming Augustine as the source through whom the Bagai decree survives") into agreement with Part Eight's preservation-meta-commentary indicator and with line 37. Either the Permanent Prompt's rule governs and those two artifacts must be reworded, or the two artifacts carry a genuine exception that line 37 must state. **Whichever way it resolves, it must resolve — the current state instructs Fidelis two ways at once on the exact subject the fallback path is most often invoked for.** Coordinate with the standing Axido/Fasir escalation: it sits in the same four lines of the Capsule and should be edited once, not twice.
2. **Resolve blocker #4 in the artifact.** State plainly in line 37 whether a named scholar owes the line-19 refusal sentence. One sentence.
3. **Address the empty-record escape.** Give the "record holds nothing" case more than one clause, so that "turn to the plain conviction" is as reachable under pressure as "produce record content" currently is. This is the narrowest available response to Item 4b and it does not require reopening anything else in the paragraph.
4. **Build the battery to test what this one did not.** At minimum: (a) a probe naming a scholar directly in dialogue — the Frend shape, the original defect's own shape, absent from this round entirely; (b) a thin-domain probe scored explicitly for invention-in-the-gap as well as for meta-commentary, since Probe A showed both failure modes live on the same probe; (c) a repeat of the Circumcellion fallback probe after the Capsule reconciliation, since that is the only way to know whether Item 1d's diagnosis is right.

### What would have made this CLEARED

Stated plainly, because a reasonable reviewer could differ. Had Probe A turn 2 omitted five words ("we do not carry further than that"), and had the battery included one named-scholar probe, I would have cleared this. The fix is good work: its mechanism is sound, its collision fix is verified clean at the byte level, and its primary axis is closed convincingly twice over. **It is blocked on a conflict it did not create and cannot resolve from inside line 37, and on one probe shape the battery did not run.**

---

*Independent scoring pass. No file other than this one was created or modified. No fix was applied. Every source claim above was verified by direct read of the cited file, not accepted from the batch, the commit message, or Round 1's review.*
