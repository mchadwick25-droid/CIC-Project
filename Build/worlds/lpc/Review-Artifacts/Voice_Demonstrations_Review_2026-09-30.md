Simulated review — informational only, not an Article 31 substitute.

# lpc B-7 voice record and demonstrations: independent review

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Reviewer agent:** independent B-7 voice-and-demonstrations reviewer (fresh context, high effort; read nothing of the drafting sessions)
- **Drafter agent:** B-7 conversion session (commit 9410f0880, voice record) and record-native compilation session (commit f8ad3f993, the three demonstrations)
- **Round:** 1 (review of a B-7 record set; not a document revision round)
- **Truncation check, method 1:** line count and closing line: `grep -cE '^### (B|S|O)[0-9]+ ' ` on this file returns 24 finding headings, and `tail -n 1` returns "End of review.", both run after the last edit.
- **Truncation check, method 2:** set comparison in Python: the finding ids in the summary table (24) equal, as a set, the ids of the `###` finding sections (24); none is missing on either side. The four reviewed records were checked the same two ways: each file's byte count on disk equals `git cat-file -s HEAD:<path>`, and each parses as YAML with every spoken field ending in terminal punctuation.
- **Scope:** `records/lpc/voice_craft/lpc.craft.datus-voice.md`; `records/lpc/demonstration/lpc.demo.compel-three-phase.md`, `lpc.demo.font-twice-answered.md`, `lpc.demo.road-back-examined.md`.
- **Standards read:** Record-Native Build Process V2.0 (Section 6 row B-7; the Doc_10 Craft/Focus bar (a)–(e); the voice-perspective principle); `CiC_Register_Bar_2026-08-29.md`; `CiC_Representative_Naming_Role_Discipline_2026-09-08.md`; exemplars `records/alx/voice_craft/alx.voice.craft.md` and `records/syr/demonstration/syr.demo.room-for-doubt.md`; CLAUDE.md (fabrication, AI tells, safety); `Doc_02_Source_Ecology.md` §6–§7; Source Registry rows 1, 2, 4, 7, 13, 19, 43, 192.
- **Verdict:** the voice record passes every mechanical B-7 condition and is a real conversion, not a copy. It carries four fidelity or scope defects that need wording fixes (S8–S11). The demonstrations do not pass: two blocking findings on `compel-three-phase`, and substantial fidelity and craft findings on the other two.

## Gates run directly

| Check | Result |
|---|---|
| `python -m engine.m10.cli records lpc` | PASS |
| `python -m engine.m10.cli regate lpc` | PASS. One note on these files: `lpc.demo.road-back-examined` participant turn 2, FRE 52.9, "not a regression, already failed at the base" (O8). |
| `gate_readability` (voice_craft + demonstration only) | 1 finding: the same participant turn, FRE 52.9. Every voice_craft field: FK 3.3–8.3, FRE 67–88. Representative turns: FK 6.7–8.8, FRE 67–79. |
| `gate_voice_craft_prompt_budget` | 0 findings. 822 of 900 words (identity 154, guard 157, flavor notes 198, concerns 106, source_anchor 207). |
| `gate_voice_perspective` | 0 findings. No "this world" or it-chain in any spoken field. |
| `observe_outside_help_guard` | The guard carries distress-comparison language. |
| `source_anchor_entries` | 8 entries, each verbatim in `source_anchor`; all 8 Registry rows are Native. |
| `tools/check_live_commentary.py --surface records` | 0 hits in the four files. |
| `deployed lpc --no-stale` (informational) | FAIL, `k:no-pin`: the world has no package yet. Expected at this stage. |

## Source anchor: each image against the vendored text

| Anchor phrase | Vendored location | Result |
|---|---|---|
| shepherd chiefly wounded in the wound of his flock; wail with the wailing | ANF05 `anf05_hippolytus-cyprian-caius-novatian.xml` l. 43727–43729 (De Lapsis) | verbatim |
| certificate must designate by name those whose penitence is seen | ANF05 l. 29946–29947, `div3 id="iv.iv.x"`, Epistle X | close paraphrase; locus cited as "Epistle XV" (S11) |
| the people's suffrage and God's judgment | ANF05 l. 32373, `iv.iv.xxxix`, Epistle XXXIX: "your suffrage and God's judgment" | faithful; the letter is addressed to the people |
| chosen bishop by the favour of the people | ANF05 l. 27818–27819 (Pontius, Life 5): "by the judgment of God and the favour of the people" | faithful; drops the judgment of God (O1) |
| no one of us sets himself up as a bishop of bishops | ANF05 l. 56871–56872 (Seventh Council, preface) | faithful paraphrase |
| ordained man keeps the sacrament of conferring baptism after leaving the unity | NPNF104 l. 10829–10830, `v.iv.iii.i` (On Baptism I.1.2) | verbatim core |
| their longing expectation is a prayer for him | NPNF106 l. 9398, `vii.iii`, Sermon I [LI Ben.] | verbatim |
| no one should be coerced ... overcame that view | NPNF101 l. 38247–38253, `vii.1.XCIII-p59`, Letter XCIII §17 | words faithful; "we first held" misattributes (S8) |
| all who hear rejoice and clamour; compulsion and constraint | `possidius_vita-augustini_weiskotten1919.txt` l. 2136, 2142–2143 | faithful; vendored spelling "clamored" (O2) |

The identity's two framing facts trace to the world's records: Cyprian the trained rhetorician made bishop by acclamation (`lpc.figure.cyprian`, `lpc.force.congregational-acclamation-overriding-preference`, Doc_01 §2), and Augustine's death during the siege of Hippo (Possidius). No invented family, age, personal history or anecdote appears in any of the four records. No record gives a voice to 258–391.

## Summary of findings

| id | severity | record | subject |
|---|---|---|---|
| B1 | blocking | compel-three-phase | Opens with another canon question and does not answer it |
| B2 | blocking | compel-three-phase | States the Contested claim as settled |
| S1 | substantial | compel-three-phase | "asked a magistrate ... not even granted" misstates Letter 185 |
| S2 | substantial | font-twice-answered | "We hold both" contradicts the G6 record and the practice |
| S3 | substantial | font-twice-answered | Cryptic register, fleet-stock phrasing, builder closing line |
| S4 | substantial | road-back-examined | Misreads Epistle X; timeless present across the whole world |
| S5 | substantial | road-back-examined | Coined closing lines; a probe transcript promoted to exemplar |
| S6 | substantial | all three demos | Same closing move three times; "we hold both" twice |
| S7 | substantial | demonstration set | No Center-Personal demonstration |
| S8 | substantial | voice record | Letter XCIII: one bishop's opinion recast as "we" |
| S9 | substantial | voice record | Silence statements broader than Doc_02 §7 |
| S10 | substantial | voice record | "a century apart" is wrong and inconsistent |
| S11 | substantial | voice record | Epistle numbering and a request turned into a rule |
| O1 | optional | voice record | Pontius: keep "the judgment of God" |
| O2 | optional | voice record | Possidius spelling |
| O3 | optional | voice record | Self-naming line: trigger condition and plainness |
| O4 | optional | voice record | "another attraction" is cryptic |
| O5 | optional | voice record | Guard repeats the anchor's closing sentences |
| O6 | optional | voice record | "nothing ... thinner still" |
| O7 | optional | demonstrations | Provenance narration and probe tags in bodies |
| O8 | optional | road-back-examined | Participant turn below FRE 60 |
| O9 | optional | demonstrations | No story is told |
| O10 | optional | process | Drafting model for Doc_10 material |
| O11 | optional | voice record | Persona name in a world record |

## Blocking

### B1 compel-three-phase: opens with another canon question and does not answer it

The record's `canon_question_id` is `_fleet.canon.f3-p-02` ("Your church used power against Christians who disagreed. Defend that."), and `canon_cells` is F3-P. The participant's first turn is the verbatim text of `_fleet.canon.f6-p-05` ("The people who taught me the faith turned out to be hypocrites. Did that happen among you?"). The representative answers "Not exactly the shape of it" and moves straight to coercion. The participant has named a personal hurt. The answer neither acknowledges it nor answers it. That fails Focus and Register statement 1 (answer the actual ask first), and a demonstration is the voice's model of exactly that.

Root cause: `Open_Gaps_Tracking.md` (the entry on the canon-closure rework round, citing the canon-closure pull request of 2026-09-25) records that this demo's id and cell were retagged from f6-p-05/F6-P to f3-p-02/F3-P. The exchange itself was never re-authored. Fix the exchange, not the tag. The F3-P content fits the record's sources and gravity.

**Proposed wording**, participant turn 1: "Your church used power against Christians who disagreed. Defend that."

Representative turn 1 (this also closes B2 and S1):

> Yes, in our later years we did. We will tell you how it happened, in order. One of our bishops, Augustine, moved on this question in three stages. We only know the first stage from his own later telling. By that account, he first held that no one should be forced into the church. Only words, only argument. Later he and his fellow bishops asked the emperors for a narrow measure. It would fine the rival church's clergy, but only where our people had already suffered violence from them. Their envoys did not get it, because a broader law had already been passed. Later still, he defended compulsion at length. What would you want to ask him first?

(118 words, FK 5.2, FRE 76.9.) The proposed turns in this review score below the FK 8 band floor. That floor is reported, not failed. The drafter should join sentences where the rhythm allows, without adding content.

### B2 compel-three-phase: states the Contested claim as settled

Turn 1 closes: "What moved between his first stand and his last was real -- we do not pretend it was nothing." `lpc.contested.compel-coercion-development` (formation_confidence Contested) holds open exactly this question: was it "a genuine change of mind" or "a retrospective self-presentation"? Every attestation of the first stage reaches us only through Letter XCIII §17, written after the later position was argued. The demo's own `divergence_note` says the exchange "is not resolved in either direction by this demonstration". The spoken text resolves it. That breaks CLAUDE.md ("Never present a disputed claim as settled") and Craft bar (d): a demonstration drawing on a Contested record carries an audible hedge in the record's own wording. The term record's wording is "an early opinion, by later account".

**Proposed wording:** delete the closing sentence. Carry the hedge as in B1's turn: "We only know the first stage from his own later telling. By that account, he first held ...". Turn 2 already has "by his own account" and keeps it (S1 proposal below).

## Substantial

### S1 compel-three-phase: "asked a magistrate ... It was not even granted"

Letter 185 §25–26 (NPNF104 `div3 id="v.vi.ix"`, l. 19624–19635) says something different. A council (401, per the editor's note) decreed that the measure "should be sought in preference from the emperors", and envoys were sent. Augustine was "one" of "certain of the brethren". The envoys "could not obtain what they had undertaken to ask" because "a law had already been published" that went further. "He asked a magistrate" gets both the petitioner and the addressee wrong. "It was not even granted" suggests a refusal, when it was overtaken by a broader law. The Permanent Prompt line 21 has the missing sentence ("A broader law reached the same end first"). The demo dropped it.

**Proposed wording** is in B1's turn 1. Turn 2, which also tells the story Letter XCIII actually gives (O9):

> We do not call it plainly right, and we do not disown it. By his own account, words did not change his mind. What he saw did. His colleagues pointed to his own town. It had once stood wholly with the rival church. Fear of the emperors' laws brought it over to us. Afterward, he wrote, it hated its old error so much that you would hardly believe it had ever shared it. Other towns were named to him too. That is the case that moved him, and we tell it as his reason. We do not ask you to accept it from us.

Source: NPNF101 l. 38253–38259 ("there was set over against my opinion my own town, which, although it was once wholly on the side of Donatus, was brought over to the Catholic unity by fear of the imperial edicts ... it would scarcely be believed that it had ever been involved in your error. There were so many others which were mentioned to me by name").

### S2 font-twice-answered: "We hold both" contradicts the record

To "So which one do you actually believe?" the representative answers "We hold both". `lpc.gravity.sacramental-ordination-validity` says: "The question persists across both phases even as the answer changes." It also says that Augustine's ruling "decides whether Donatist clergy are received back in their own orders or ordained again". On Baptism I.1.2 (NPNF104 l. 10838) says returning clergy "are certainly not ordained again". The world did not hold both answers at once. It answered one way, then the other, and kept communion with the first man. The Capsule's instruction is not to *adjudicate* ("You do not resolve which of your own voices was right"). That is different from claiming to believe both at once.

**Proposed wording**, representative turn 2:

> Our practice changed, and we will not hide that. In Cyprian's day, our council baptized such people again. By Augustine's day, we received them without a second baptism. Their clergy were not ordained again. Augustine argued at book length that Cyprian's ruling was wrong. Yet he never put Cyprian outside our communion for it. So we do not tell you one of them was ours and the other a stranger. Both are ours.

### S3 font-twice-answered: cryptic register, stock phrasing, builder closing line

- "when the hand that fills it comes from outside the one church" is a metaphor standing in for the plain question (who baptizes). "font" is never given its plain meaning first (Register Bar: plain meaning first, the world's word after, as a label). "for either answer to be true only in argument" cannot be parsed on one reading.
- "and we are not going to pretend that is easier than it sounds" and "What we can tell you is what" appear word for word in `pahc.demo.lament-suffering` and `desert.demo.lament-suffering`. That is fleet-wide assistant cadence, the AI tell CLAUDE.md names.
- The closing sentence ("Everything else we hold rests on the answer to that question being real") is the Permanent Prompt line 35's builder-authored aphorism, which the record body itself says was "quoted here exactly". Craft bar (b): no closing on a line presented as quotable in its own right.
- "so we bring the person to the water again" puts a past ruling in the present tense.

**Proposed wording**, representative turn 1:

> One question above all: is a baptism real when it is given outside the one church? We answered it twice, in two of our own voices, about a century and a half apart. The answers are opposites. Cyprian and his council held that nothing valid is given outside. So they baptized such a person again. Augustine held that something real is given even there. But it does the person no good until they come inside. So we brought them in, and let what they already carried begin to work. Both men asked in earnest. Neither could leave it unanswered.

Turn 2: as S2.

### S4 road-back-examined: misreads Epistle X; timeless present across the whole world

"Their name is set down. Not hidden, not quietly forgotten -- set down, so the congregation knows exactly who is walking this road and why." The record body names Epistle X (ANF05 l. 29940–29948) as the grounding. There, Cyprian asks the *martyrs* to "designate by name in the certificate" the persons they commend, against petitions for "Such a one with his friends". It is a request to the bishop, not a public roll. The public visibility of the road back is grounded elsewhere (`lpc.term.reconciliation-penitential-discipline`: "A failure that happened in public cannot be undone in private"). But the naming does not exist "so the congregation knows".

Also, the participant asks in the past tense ("how was it handled"). The answer is a timeless present that speaks for the whole 246–430 world. `lpc.gravity.penitential-discipline` says the concern "holds directly for Cyprian's phase" and "does not continue under its own name" into Augustine's.

**Proposed wording**, representative turn 1, closing on a real, sourced quote instead of a coined line (see S5):

> In Cyprian's years, many gave way under persecution, and the road back was slow and public. A martyr might write asking peace for someone. Cyprian insisted the letter name that person. He would not accept 'such a one with his friends.' Then came the waiting. The bishop watched and weighed the person's change, and he answered for weighing it rightly. Peace was not granted just because someone felt moved to grant it. At the end, the people who had seen the failure received the person back, together, in the open. Cyprian asked the martyrs to name only 'those whom you yourselves see, whom you have known, whose penitence you see to be very near to full satisfaction.'

### S5 road-back-examined: coined closing lines; a probe transcript promoted to exemplar

- Turn 1 closes "A door with no examination behind it is no door at all. It is just a room nobody ever really left." Turn 2 closes "We call it being known well enough that your homecoming means something to the very people who watched you leave." Both are self-composed lines presented as quotable (Craft bar (b)).
- "has no Master either" is the Doc_05 §2.1 inhabited-voice coinage (also in `lpc.force.recurring-contest-failed-member` and Doc_08). It is builder text, not a source. The capital-M "Master" is never explained to the participant.
- "no door at all" appears in both turns. The syr exemplar's second turn "builds on the first turn without repeating a sentence of it".
- Provenance: 117 of turn 1's and 138 of turn 2's seven-word runs match `Representative/lpc_Rep_Phase5_Boundary_Testing_Round1.md` word for word, and the body says "No word of either representative turn is altered from the original." A generated probe answer, coinages included, has become the exemplar the voice learns from. That is circular. `sources[]` names the gravity "used directly", not the transcript.

**Proposed wording**, participant turn 2 and representative turn 2:

> That sounds like they have to prove they've changed before you trust them. Isn't real forgiveness meant to have no conditions?

> We argued that question among ourselves, and we never found one answer that kept everything true. Some would take back no one who had sacrificed. We would not follow them. Others offered a quick road back with no waiting. We refused that too. A church that takes everyone back at once makes the peace of the table mean nothing. A church that takes no one back forgets whose flock it is. So the door is real, and it opens. But the person who walks through has been seen to change, not only claimed it. We did not call that proving yourself to us. We called it penitence, seen by the people who watched you fall.

(The Novatianist and Felicissimus positions are from `lpc.gravity.penitential-discipline`'s description.)

### S6 all three demonstrations: one closing move three times; "we hold both" twice

Every exchange ends on the same stance: tension held, neither side chosen. compel: "We do not say it was self-evidently right, and we do not disown it either". font: "We do not resolve which of our own voices was right" and "We hold both". road-back: "we have never found the single answer that settles it" and "So we hold both." Craft bar (c) forbids near-verbatim repetition across demonstrations. Register statement 7 forbids repeating across answers. Three exemplars that all model one move teach the voice a tic. The rewrites above differ: compel ends on the source's own reason, font on the practice change, road-back on penitence seen by the people. No further wording is needed beyond S1–S5.

### S7 demonstration set: no Center-Personal demonstration

Craft bar (a) is written against "the demonstration answering the canon's Center-Personal cell". The launch prompt's bar names "direct Center-Personal answer" first. lpc has three demonstrations (F3-P, F6-I, F4-I). None answers `_fleet.canon.c-p-01` ("How did you come to believe in Jesus?"). The Register Bar's base conditions speak of "the six conversational demos". The C-P cell is closed by `lpc.witness.grant-me-chastity-but-not-yet` (Confessions VIII), so the material exists. **Proposed action:** add one C-P demonstration that answers in its first sentence and tells the Confessions VIII scene rather than summarising it (Craft bar (a), (e)). Per the process table, Fable authors it. This review proposes no wording for it, because new authorship belongs to the drafter.

### S8 voice record, source_anchor: one bishop's opinion recast as "we"

"In Letter XCIII, we first held that no one should be coerced, until the cases laid before us overcame that view." Letter XCIII §17 reads "originally my opinion was", overcome by "these instances which my colleagues have laid before me". The first opinion was Augustine's against his colleagues, not the community's. The we-voice here gets the facts wrong. It also flattens the very disagreement the identity promises to "keep visible".

**Proposed wording:** "In Letter XCIII, one of our bishops first held that no one should be coerced, until the cases his colleagues laid before him overcame that view."

### S9 voice record: silence statements broader than Doc_02 §7

The guard says "From 258 to 391 no ordinary voice of ours survives." The identity says "our own voice falls silent". Doc_02 §7 limits the silence to the Registry's Native rows ("The silence claim holds for the Native rows only"). It states an open, class-level exception: pseudo-Cyprianic works (rows 6, 194) that speak as a bishop to his people, "whose date and place the vendored files do not fix". It also names an unassessed sermon (row 229/266) that "may sit inside the interval". The guard's next sentence names the class, but "survives" has already denied it. "no fixed date or hand" should match Doc_02's "date and place".

**Proposed wording**, guard: "From 258 to 391 no ordinary voice of ours survives that we can date and place. A few works carry Cyprian's name, but no one has fixed their date or place. We draw on none of them." Identity: "Between Cyprian's death and Augustine's ordination, about 130 years, we hold no voice of our own that we can date and place." (Guard becomes 166 words, FK 5.4. The budget stays under 900.)

### S10 voice record: "Twice, a century apart"

Cyprian's council met in 256 (the vendored heading says 258). On Baptism is c. 400 (Registry row 13). That is about 145 years. The font demonstration says "a century and a half apart". The Permanent Prompt says "a century apart" (l. 19), "across a century" (l. 63) and "a century and a third" (l. 37). The G6 record says "decades apart". This field compiles into every turn.

**Proposed wording:** "Twice, about a century and a half apart, we answered what a font gives outside the church, and the answers were opposite." The Permanent Prompt and G6 wording is outside this review's scope. It is flagged for the drafter to register in `Open_Gaps_Tracking.md`.

### S11 voice record: Epistle numbering, and a request turned into a rule

`sources[0].locus` says "Epistle XV (the certificate that names a person)". The vendored ANF05 edition numbers this letter Epistle X (`div3 id="iv.iv.x"`, l. 29836). Its Epistle XV is "To Moyses and Maximus" (l. 30248). The road-back demonstration already cites Epistle X. The "XV" is probably the Oxford/Hartel number, but the record cites the vendored file. The anchor's "the certificate must designate by name those whose penitence is seen" also turns Cyprian's plea ("I beg you that you will designate") into a rule, and drops whose sight counts.

**Proposed wording**, locus: "Epistle X in the vendored ANF numbering (div iv.iv.x; the certificate that names a person) and Epistle XXXIX (the people's suffrage), Registry row 1". Anchor sentence: "In Cyprian's Epistles, a martyr's certificate is to designate by name those whose penitence the martyrs see, and a bishop's office stands on the people's suffrage and God's judgment." (With S8, O1 and O2 applied, source_anchor is 220 words, FK 8.8, FRE 67.7. The total stays under 900.)

## Optional

### O1 voice record: Pontius, keep "the judgment of God"

**Proposed wording:** "In Pontius's Life of Cyprian, a man is chosen bishop by the judgment of God and the favour of the people." (Pontius l. 27818.) The pairing is the world's own. Row 1's Epistle XXXIX pairs the same two.

### O2 voice record: Possidius spelling

The vendored Weiskotten text reads "clamored" (l. 2136). **Proposed wording:** "all who hear rejoice and clamor".

### O3 voice record: the self-naming line

The self-reference note says "One plain line may name what speaks, once only". It leaves out the trigger the Permanent Prompt l. 17 gives ("When someone asks you plainly what you are"), which the alx exemplar also carries. **Proposed wording:** "One plain line may name what speaks, only when someone asks what we are, and once only. Then we return to we." The line itself ("the flock kept, and the flock that keeps its own") is a balanced-rhetoric shape the Register Bar names. alx's line is plain ("I am a representative of Alexandria."). Changing it changes the Permanent Prompt too, so it is Mark's call, not the drafter's.

### O4 voice record: "another attraction"

"Some of our own drift toward another attraction" does not say what the attraction is. The source does: Sermon I (row 19, NPNF106 l. 9398–9399), "the day of the public shows has dispersed many from hence, for whose salvation I exhort you to share my great anxiety". **Proposed wording:** "Beside it sits a plainer worry. Some of our own slip away to the public shows. We ask those still with us to share that worry."

### O5 voice record: guard repeats the anchor

The guard's "Our images come only from what formed us ... however well its words might fit." (about 45 words) repeats source_anchor's closing two sentences, and "a more vivid hand that argued against us" is cryptic. B-7 asks for redundant framing to be cut. **Proposed action:** delete those two guard sentences. The anchor already carries the guard against borrowed images.

### O6 voice record: "nothing ... thinner still"

After "Those who fell left us nothing in their own words", "thinner still" cannot follow nothing. **Proposed wording:** "Those who fell left us nothing in their own words. We hold little from the countryside and its languages."

### O7 demonstrations: provenance narration and probe tags in bodies

The bodies narrate history ("trimmed to stand alone ... No word of either representative turn is altered from the original"), and the tags carry test outcomes (`probe-12-retest-pass`, `probe-14-confirmed-pass`). `check_live_commentary.py` finds nothing, and `Open_Gaps_Tracking.md` leaves pre-existing body commentary in these two files to Mark's ruling (OG-14). Noted only. Any re-authoring under B1–S5 should replace the bodies with a plain statement of scope and sources.

### O8 road-back-examined: participant turn below FRE 60

Participant turn 2 scores FRE 52.9 (`gate_readability`). regate reports it as pre-existing. The S5 wording (FK 4.2, FRE 83.4) clears it.

### O9 demonstrations: no story is told

Craft item 3 says storytelling is part of craft. None of the three exchanges tells a scene. The S1 turn 2 wording tells Letter XCIII's town. The S4 turn 1 wording carries Cyprian's "such a one with his friends".

### O10 process: drafting model for Doc_10 material

Commit 9410f0880 (voice record) is co-authored by Sonnet 5.5. The demonstrations came from commit f8ad3f993 (Sonnet 5). The process table assigns Doc_10's "voice and demonstrations" to Fable. Noted for the caller. Not a content finding.

### O11 voice record: persona name in a world record

The identity opens "Datus is a name and a role, Bishop of the Kept Flock." The alx exemplar says the name and role "never appear in world records, this one included". The fleet is split (syr, desert, don, rzg and pahc name the persona), so this is not a finding against lpc. It is a fleet-level question.

## What passes

- B-7 mechanics: budget 822/900; every field FK ≤ 10; 8 anchor entries, each named verbatim, all from Native rows; the anchor's images trace to the vendored texts (table above).
- Hard conversion: no field copies the Permanent Prompt's museum-guide paragraphs (l. 7–15). The identity, guard and notes condense l. 3–5, 19–21, 41–43 and 51 in the alx style.
- Distress-comparison guard: present, in the world's own idiom ("is somebody's", "as we would hear one at our door"), inside the voice and period. It does not point to outside help. No demonstration handles distress, and none makes the Representative a crisis responder.
- Voice perspective: first person plural throughout. No "this world" or "it" for the community in any spoken field.
- Naming discipline: no backstory, family, age or anecdote. The identity states "He is not a biography and not one man."
- 258–391: no record invents a voice for the interval, and the rival church's record is excluded as Doc_02 §7 requires. S9 fixes the scope wording only.
- Grep-clean against the record store: the longest overlaps with other lpc records are seven-word runs ("we do not resolve which of our own", `lpc.witness.answerability-as-ground`; "people who watched the failure are the", `lpc.term.reconciliation-penitential-discipline`). None is a lifted passage. The real overlaps are with the Permanent Prompt, the Capsule and the Phase 5 transcript (S3, S5).

End of review.
