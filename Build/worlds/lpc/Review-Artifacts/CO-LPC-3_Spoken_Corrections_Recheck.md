# CO-LPC-3 spoken-field corrections: recheck

- **Reviewers:** two independent Opus 5.5 passes, one per part, over the uncommitted CO-LPC-3 diff.
- **Scope:** every prior finding in the three `Spoken_Fidelity_Review_*_2026-10-24.md` files, and every changed line.

## Part 1: witness, term, story, figure and quote records

Reviewer: Claude Opus 5.5 (claude-opus-5-5), the whole pass. Date: 2026-10-24. Independent recheck under the Cap ruling "Cap ruling: lpc change order CO-LPC-3, one recheck of the spoken-field corrections" (System Hub Decision Log, 2026-10-24).
Scope: the uncommitted `git diff` in `records/lpc/doctrinal_witness/`, `term/`, `story/`, `figure/` and `quote/` (46 files). I checked only what changed, against the two prior reviews. No repo file was changed.

Method: I read every changed line as a word diff. I read the cited `cic/texts/` lines myself for each fix. I checked every quotation in the changed lines against the vendored text with a whitespace- and markup-normalised search. I ran `python -m engine.m10.cli regate lpc`. I also scored every changed field with `engine.m1.gates.grade_text`, including fields that regate does not treat as public-facing.

Abbreviations: ANF5 = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`; NPNF101/103/104/105/107 = the matching `cic/texts/npnf10x_*.xml`; POSS = `cic/texts/possidius_vita-augustini_weiskotten1919.txt`.

### Readability

- `regate lpc`: **PASS**. 162 public-facing fields checked, 94 new or edited, no regression.
- All changed fields in the prior scope (text, positions, plain_meaning, quick_meaning, bridge_line, tellable_as, modern_rendering) score FK ≤ 10 and FRE ≥ 60. The thinnest margins are answerability-as-ground positions[0] (FK 9.3 / FRE 61.9) and apostolic-succession text (FK 7.9 / FRE 60.1).
- There is one regression outside regate's field list: marriage-a-threefold-good `tensions[0]` went from FK 9.4 / FRE 61.8 to FK 11.3 / FRE 56.8. See N8.
- The edited `senses.*`, `modern_contrast` and sesterces `text` fields that fail were already failing at base. The sesterces `modern_contrast` moved from FRE 59.6 to 58.5, still a fail. These are not counted.

---

### Prior findings, review A (witnesses): 11 P1, 33 P2

| ID | Sev | Record / field | Status | Note |
|---|---|---|---|---|
| A1 | P1 | almsgiving text | Fixed | "share your gains with Christ" is word for word (ANF5:47690), in a passage addressed to a rich man. A §13 locus was added. |
| A2 | P2 | almsgiving text | Fixed | positions[0] was aligned too. |
| A3 | P2 | almsgiving text, positions[0] | Fixed | Quote matches ANF5:47709. |
| A4 | P2 | almsgiving text | Fixed | |
| B1 | P1 | answerability text, tensions | Fixed | Matches NPNF104:12157, 12168, 12997 ("in whose entirety he remained"). |
| B2 | P1 | answerability text | Fixed | The "because" clause was cut. |
| B3 | P2 | answerability loci / positions[0] | Fixed, **new problem** | All four new loci check out (ANF5:43726, 37350; NPNF104:12153–12169, 12993–12999). The softening was applied. But the rating is now Inferential-Thin while several sentences stay flat. See N1. |
| C1 | P2 | apostolic-succession text, positions[0] | Fixed | Letter LIII is from "Fortunatus, Alypius, and Augustin" (NPNF101:29650). |
| C2 | P2 | apostolic-succession text | Fixed | Siricius, Damasus, Liberius counted back from Anastasius is right (NPNF101:29704–29708). |
| D1 | P2 | baptism-traced text, positions[0] | Fixed | |
| E1 | P2 | blamed-for locus | Fixed | §§12–13 at ANF5:45938–45992 show Demetrianus torturing Christians. |
| F1 | P1 | communion-over-separation positions[1] | Fixed | The formula is word for word (ANF5:42290). "We read that as the reason…" is a declared reading, which is acceptable. |
| F2 | P2 | communion-over-separation text, positions[0] | Fixed | The causal link is now in the divergence_note, not stated as fact. |
| F3 | P2 | communion-over-separation loci | Fixed | Ep. XXXVII at 32239, XXXIX at 32348, XLI at 32655 ("has appointed a bishop for itself", 32679), XLVIII at 33151 (Felicissimus, 33217). All headings confirmed. |
| F-read | — | communion-over-separation, 3 fields | Fixed | FK 6.7 / 6.7 / 7.6. |
| G1 | P1 ×2 | confessor-claim positions[0], text | Fixed | Matches Ep. X §1 (ANF5:29880–29884). |
| G2 | P1 | confessor-claim text | Fixed | Ep. XI is addressed to "his brethren among the people who stand fast". "Whole congregation" is a little wide but within the reviewer's own proposal. Advisory only. |
| G-read | — | confessor-claim text | Fixed | FK 7.7 / FRE 73.6. |
| J1 | P1 | grant-me-chastity text | Fixed, **new problem** | The new clause reads ambiguously. See N9. |
| J2 | P2 | grant-me-chastity positions[1] | Fixed | "an horrible shame" is at NPNF101:12766. |
| K1 | P1 | heard-for-salvation text, tensions | Fixed | Matches NPNF107:15218 ("The saints are in all things heard unto salvation"). |
| L1 | P2 | marriage locus | Fixed | The editor's preface is marked as the editor's. |
| L2 | P2 | marriage text, tensions | Fixed, **new problem** | tensions[0] now fails readability. See N8. |
| M1 | P2 | restless-heart positions[0] | Fixed | |
| N1 | P2 | scripture-above-councils positions[1] | Fixed | |
| O1 | P1 | only-son text | Fixed | The "whole Arian people" sentence is gone. An editor-intro locus was added for the tension's Vandal/Arian line (POSS:468–477). |
| O2 | P2 | only-son text | Fixed | Name, place and witnesses match POSS:2942–2945. |
| O3 | P2 | only-son text | Fixed | Matches Enchiridion 56. |
| Q1 | P1 | tradition-tested text | Fixed | The body note was aligned too. |
| Q2 | P2 | tradition-tested text | Fixed | |
| Q3 | P2 | tradition-tested positions[0] | Fixed | |
| R1 | P2 | violence text, positions[0] | Fixed | |
| R2 | P2 | violence text, positions[0] | Fixed | |
| R3 | P2 | violence text | Fixed | |
| R4 | P2 | violence text, tensions | Fixed | "not a bodily action, but an inward disposition" is at NPNF104:8152. |

### Prior findings, review B (terms, stories, figures, quote): 20 P1, 23 P2

| Record / field | Sev | Status | Note |
|---|---|---|---|
| figure.augustine bridge_line | P2 | Fixed, **new problem** | "The people … made him a presbyter" is wider than the source. See N7. |
| figure.celerinus bridge_line | P1 | Fixed | Matches ANF5:30556–30580. |
| figure.cyprian bridge_line | P2 | Fixed | |
| figure.lucian bridge_line | P1 | Fixed, **new problem** | "Three" and "never met" are gone. The grant is now stated without Lucian's own condition. See N4. |
| figure.pontius bridge_line | P1 | Fixed | The "stayed through exile" point is fixed too. |
| figure.possidius bridge_line | P2 | Fixed | "almost forty years" is at POSS:5059. |
| quote.ancient-venom modern_rendering | P2 | Fixed | One word changed; the rest is untouched. |
| story.celerinus tellable_as | P1 | Fixed, **new problem** | tellable_as is sound. The rewritten `modern_contrast` misstates the confessors' authority. See N2 and N3. |
| story.hundred-thousand-sesterces tellable_as | P1 | Fixed | |
| story.numidicus tellable_as | P1 | Fixed | The text now reads "adding a presbyter to our clergy" (Ep. XXXIV body). No "ordain" is left. |
| story.the-plague-and-the-enemies tellable_as | P1 | Fixed | ANF5:27967 and 27991 ("to all men, not to those only who are of the household of faith"). |
| story.the-psalms-on-the-wall tellable_as | P1 | Fixed | POSS:4919–4922. modern_contrast was aligned too. |
| story.the-death-of-cyprian tellable_as | P2 | Fixed | Text "first" removed too. The other 40 changed lines are whitespace only (`git diff -w`). |
| term.bishop-of-bishops plain, quick | P2 ×2 | Fixed | senses.informational aligned. |
| term.certificates plain, quick | P1 ×2 | Fixed, **new problem** | The fields themselves are sound and leave the tension open ("Who decides is what we argued over"). The new divergence_note and evidential lines shorten Ep. XVI. See N5. |
| term.communion plain | P1 | Fixed | |
| term.communion quick | P2 | Fixed | |
| term.compel plain, quick | P2 ×2 | Fixed | |
| term.confessor plain, quick | P2 ×2 | Fixed | |
| term.grace plain, quick (locus) | P2 ×2 | Fixed | Locus quote at NPNF105:10082. |
| term.heresy plain, quick | P1 ×2 | Fixed, **new problem** | The edited plain_meaning keeps "a century apart". See N10. |
| term.libellatici plain | P2 | Fixed | |
| term.libelli plain, quick | P1 ×2 | Fixed | De Lapsis 27 (ANF5:44357–44363). senses.informational aligned. |
| term.plenary-council plain | P2 | Fixed | |
| term.preaching plain, quick | P1 ×2 | Fixed | senses and catechesis prefer_instead aligned. |
| term.reconciliation plain, quick (locus) | P2 ×2 | Fixed | Ep. IX is word for word apart from the ANF footnote "Exomologesis" (ANF5:29768–29773). The passage is about "smaller sins", which is fine for a process locus. |
| term.schism plain (locus) | P2 | Fixed | ANF5:42694, 42700. |
| term.schism quick | P2 | Fixed | |
| term.suffrage plain, quick | P2 ×2 | Fixed | |
| term.the-flock plain | P1 | Fixed | "buries" is gone. Letter CXXVI added (NPNF101:44504). The source_id exists. |
| term.the-flock quick | P2 | Fixed | |
| term.the-one-episcopate plain, quick | P1 ×2 | Fixed | Locus quote at ANF5:42290. senses aligned. |
| Out of scope 1: celerinus story text "in Carthage" | — | Fixed | |
| Out of scope 2: lucian dates.display "sister" | — | Fixed | The condition is still absent (N4). |
| Out of scope 3: numidicus dates.display "ordained" | — | Fixed | The body note was aligned too. |
| Out of scope 4: sesterces "Numidian towns" | — | Fixed | "captive among barbarians" is in the letter body (ANF5:36046). absent_detail was aligned. |

**Every prior finding is fixed.** Six fixes brought a new problem with them, listed below.

---

### Points the brief asked about

**answerability-as-ground, Documented → Inferential-Thin.** I accept the rating. The divergence_note calls the unity reading "this build's own synthetic judgment", and Inferential-Thin is no more settled than the world core's Dominant Modern Reconstruction.

The hedges are incomplete, though. `CiC_Record_Native_World_Build_Process_V2.0.md` §0 says an Inferential-Thin claim "keeps its own hedge and is never voiced as settled fact". Several sentences still voice it flat. See N1.

There is an alternative: rate the record Dominant Modern Reconstruction, to match `lpc.core` exactly, and keep the text as it is. I recommend keeping Inferential-Thin and completing the hedges.

**the-only-son, Possidius locus.** The brief says Possidius says only "Arian bishop". That premise is incomplete. Possidius ch. 17 also says that the conference records show "what the Catholic Church maintains and teaches regarding the divine Trinity" (POSS:2948–2950). So the Trinity is the subject in his own text. What he does not say is "held specifically over". The locus also cites only line 2942, where the Trinity line is 2949. See N6 (P2). The text field itself is sound.

**Story claim_guards and tiers.**
- All seven stories keep their tiers and tier justifications unchanged.
- The death-of-cyprian cloth difference is still told as a difference.
- The sesterces guard against currency conversion still holds.
- The celerinus guard "must not resolve the confessor-authority tension by presenting the confessors as either usurpers or heroes" is breached by the new `modern_contrast`. See N2.

**Lucian's condition (ANF5:30726–30732).** Lucian writes: "the case being set forth before the bishop, and confession being made, I ask that not only these may have peace". Even the confessors' general letter grants peace only to those whose conduct is satisfactory "in your estimation" (Ep. XVI, ANF5:30386).

So, yes: corrected records do now misstate the confessors' authority without the condition.
- Celerinus story `modern_contrast` is changed, and states it as an alternative to the bishop: N2, P1.
- Celerinus story `text` paragraph 3 is unchanged, and its reply "granted what was asked … on whose authority he answered": N3, P1.
- Lucian bridge_line and dates.display are changed: N4, P2.
- Certificates divergence_note and senses.evidential are changed: N5, P2.

These records are sound on this point: confessor-claim (the confessors "ask peace"), term.certificates plain and quick ("asks for peace, or grants it. Who decides is what we argued over"), and term.confessor.

---

### New findings

**N1. P1. lpc.witness.answerability-as-ground: Inferential-Thin claim still voiced as flat fact (text, positions[0]).**
- Flat sentences:
  - "We are held together because we are answerable."
  - "Take the answerability away, and each of these becomes a separate rule…"
  - "The road back … is not a formality; it is what answerability actually looks like in practice."
  - "…because the disagreement itself is carried inside the one bond we are both answerable to."
- Problem: these state the build's synthesis, which the record now rates Inferential-Thin, as settled self-description. That is the "confidence-tag flattening" defect named in the method document (§0 and its defect list).
- Proposed positions[0] (FK 9.8 / FRE 60.2):
  > We are not held together because we are pure, and not because we are right about every hard question we argue. As we understand ourselves, we are held together because we are answerable. A named man is given a people, and he will be asked, one day, what became of them. We see everything else growing out of that one fact: the road back for someone who has failed, the font that either gives or withholds until a person comes home, the disagreement we carry without breaking over it. Take the answerability away, and to us each of these becomes a separate rule we argue about. Leave it in place, and they are one conviction, seen from several sides.
- Proposed text (FK 6.8 / FRE 70.6):
  > We are held together, first, by one plain fact: a particular people has been placed in a particular man's care, and he will be asked what became of them. That is not a title he carries apart from the people it names. It is the whole shape of what a bishop is. We see everything else we hold growing out of that one root. The road back for someone who has failed is not a formality. To us, it is what answerability looks like in practice. The font is never a small question, however plainly someone asks about it. And when we disagree, sharply, even across a whole century, we do not put each other outside the table over it. As we see it, the one bond we both answer to holds the disagreement inside it. We do not pretend this makes every hard question easy. We have answered the font question twice, in opposite ways. Our later bishop judged the earlier answer wrong. But he never put the man who gave it outside our communion. Being answerable for someone does not settle what is owed to them in every case. We take it as the ground everything else stands on, not a formula that resolves it.
- The alternative is set out above: rate it Dominant Modern Reconstruction to match the core, with no text change. That is a confidence-vocabulary call for the project lead if preferred.

**N2. P1. lpc.story.celerinus-writes-to-lucian `modern_contrast` (changed line): the confessors' grant is set against the bishop without Lucian's condition.**
- Sentence: "Here one confessor asks another, who is in prison, for peace, and the other grants it."
- Problem: the field contrasts this with "a bishop's own authority … the only channel". It presents the confessor route as working apart from the bishop. Lucian's own reply sets each case "before the bishop, and confession being made" (ANF5:30730). This resolves the tension the record's own claim_guard forbids resolving. "someone failed under pressure" is also ungrammatical.
- Proposed (FK 8.4 / FRE 64.1; the field also passes, where it failed before):
  > A modern listener may expect a bishop's authority to be the only channel by which someone who failed under pressure could be restored. Here one confessor asks another, in prison, for peace, and the other gives it in the martyrs' name. Yet his own reply says each case is to be set before the bishop. Cyprian's own dossier keeps both letters rather than hiding them.

**N3. P1. lpc.story.celerinus-writes-to-lucian `text` paragraph 3 (unchanged line, same record): the same omission, in the told story.**
- Sentences: "Lucian's reply … granted what was asked." / "…named the martyrs on whose authority he answered, and signed off exhausted…"
- Problem: the told story gives the grant and the martyrs' authority, and leaves out Lucian's own condition. This was not introduced by CO-LPC-3. I report it because the brief asked whether any corrected record misstates the point. N2 cannot be fixed cleanly while the told text still says the opposite.
- Proposed paragraph 3 (FK 7.2 / FRE 70.7; quotations word for word, ANF5:30704–30740):
  > Lucian's reply came back from the prison, and it granted what was asked. Before it did, it said what the prison had been like: by the emperor's command they "were ordered to be put to death by hunger and thirst, and were shut up in two cells, that so they might weaken us by hunger and thirst." Then: "But now we have attained the brightness itself." He greeted Numeria and Candida, and named the martyrs on whose authority he answered. He also set a condition: peace would come "the case being set forth before the bishop, and confession being made." He signed off exhausted, greeting others "whose names I have not written, because I am already weary. Therefore they must pardon me."

**N4. P2. lpc.figure.lucian bridge_line and dates.display: the grant without the condition.**
- Sentence: "He granted peace to Numeria and Candida, two women he knew well."
- Problem: the condition is missing. Also, "(shall have peace)" beside the two names is the ANF editor's insertion (ANF5:30713–30716).
- Proposed bridge_line (FK 6.1 / FRE 75.3):
  > A confessor who answered from a prison cell. He and others there had been ordered to die of hunger and thirst. He sent peace to Numeria and Candida, two women he knew well, once each case was set before the bishop.
- Proposed dates.display tail: "…who replied to Celerinus from prison, granting peace to Numeria and Candida once their case was set before the bishop (Ep. XXI; lpc.story.celerinus-writes-to-lucian)"

**N5. P2. lpc.term.certificates-letters-of-peace divergence_note and senses.evidential (changed lines): Ep. XVI quoted without its condition.**
- Sentence: "…one general letter of theirs to Cyprian, which says 'we have granted peace' (Epistle XVI)".
- Problem: the letter grants peace to those whose account is satisfactory "in your estimation", meaning Cyprian's (ANF5:30386). The locus quotes it in full. The two prose lines cut it.
- Proposed (both places): "…one general letter of theirs to Cyprian (Epistle XVI), which says 'we have granted peace' to all whose conduct has been satisfactory 'in your estimation'…"

**N6. P2. lpc.witness.the-only-son-and-the-trinity, Possidius locus and body note.**
- Problem: "held specifically over the doctrine of the Trinity" is stronger than Possidius's wording. The line range misses the Trinity line.
- Proposed locus: "Chapter 17, the conference at Hippo with Maximinus, 'a bishop of these Arians'; its records show 'what the Catholic Church maintains and teaches regarding the divine Trinity' -- verified directly against cic/texts/possidius_vita-augustini_weiskotten1919.txt, lines 2942-2950"
- In the body note, change "held specifically over the Trinity" to "whose records, he says, set out the Church's teaching on the Trinity".

**N7. P2. lpc.figure.augustine bridge_line.**
- Sentence: "The people seized him and made him a presbyter while he wept."
- Problem: the people laid hands on him and "brought him to the bishop to be ordained" (POSS:1808–1816). Valerius ordained him; the people did not.
- Proposed (FK 6.3 / FRE 71.3):
  > Our bishop at Hippo. The people seized him and brought him to be made a presbyter while he wept. Later they pressed him into the bishop's office over his own refusal. He spent his last days weeping over psalms of penitence, while an army lay outside the walls.

**N8. P2. lpc.witness.marriage-a-threefold-good tensions[0]: readability regression.**
- Problem: the L2 edit took the field from FK 9.4 / FRE 61.8 to FK 11.3 / FRE 56.8. regate does not grade `tensions`, but the field is voice material.
- Proposed (FK 7.4 / FRE 65.3; no claim changed):
  > Of the third good, he wrote that a marriage compact is entered into as a kind of sacrament. It is not undone even by separation. So long as the husband lives, a wife who marries another while separated from him still commits adultery. This is not a teaching about attendance at a wedding. It is a teaching about what marriage itself is and what it binds.

**N9. P2. lpc.witness.grant-me-chastity-but-not-yet text: ambiguous new clause.**
- Sentence: "…and he wrote it down himself, from before he was received among us."
- Problem: it can be heard as saying he wrote it before his baptism. The Confessions were written years after it, as positions[0] says.
- Proposed (whole field FK 7.5 / FRE 77.9): "One of our own knew a trouble close to that, before he was received among us. Years later he wrote it down himself."

**N10. P2. lpc.term.heresy plain_meaning (edited field): "a century apart".**
- Problem: the record's own senses say "a century and a half later". Cyprian's council of 256 and Augustine's On Baptism of about 400 are about 145 years apart.
- Proposed (FK 6.9 / FRE 74.7):
  > For us, this word raises one sharp question: whether a baptism given outside our one church counts at all. We answer it twice, in two different ways, a century and a half apart.

### Advisory (not counted)
- The sesterces `retrieve_when` still says "obligation to strangers". This is not voiced, but it is the framing the fix removed.
- lpc.figure.numidicus bridge_line is FK 10.2. It is unchanged, already failing at base, and reported by regate as not a regression.
- confessor-claim still has `citation_specificity: B`, though both loci now carry line ranges.
- Every quotation in the changed lines matched the vendored text, except two where the only gap is an ANF footnote inside the quoted span: Ep. IX "Exomologesis" and Ep. XX "purple".

### Counts
- Prior findings rechecked: review A 11 P1 + 33 P2; review B 20 P1 + 23 P2; plus 4 out-of-scope errors. **All fixed.**
- Fixes that brought a new problem: 6 (B3, J1, L2, figure.augustine, figure.lucian, story.celerinus), plus certificates and heresy, where new or edited lines in a fixed record carry an issue.
- **New findings: P0 0, P1 3 (N1, N2, N3), P2 7 (N4–N10).**
- Readability: regate PASS. Every changed in-scope spoken field passes. One out-of-regate regression (N8).

## Part 2: other record types, documents, the Representative prompt and generators

Reviewer: Claude Opus 5.5 (claude-opus-5-5), the whole pass. Recheck of change order CO-LPC-3 under "Cap ruling: lpc change order CO-LPC-3, one recheck of the spoken-field corrections". Scope: the uncommitted `git diff` in `records/lpc/` (ambient, world_core, voice_craft, demonstration, force, gravity, honest_limit, contested_claim, source), the changed documents under `Build/worlds/lpc/`, and `Build/worlds/lpc/scripts/`. Prior findings: `Build/worlds/lpc/Review-Artifacts/Spoken_Fidelity_Review_Other_Types_2026-10-24.md` (C-1 to C-40). No repo file was modified. Every source line cited below was read in `cic/texts/` during this pass.

Short names: ANF05, NPNF101, NPNF104, NPNF105, SENT, CTH as in the prior review.

### Mechanical checks

- `python -m engine.m10.cli regate lpc`: **PASS**. 162 fields, 94 new or edited, no regression. Every edited in-scope field was also scored one by one: all are FK 3.9 to 9.2 and FRE 60.2 to 87.9. The weakest are `sacramental-ordination-validity` (FRE 60.2) and `illegal-to-established-shift` (FRE 60.3). The Datus prompt's changed paragraph scores FK 8.0 / FRE 69.4. The Capsule's changed paragraph scores FK 9.2 / FRE 64.4. Several fields fall below FK 8. That is reported, not failed.
- `python -m engine.m10.cli claims lpc`: **PASS**, with 98 registered and 3 UNVERIFIED (completed below).
- **Generators.** The six changed scripts were run in a scratch copy of the tree, and their output was compared with the working-tree records by parsed field. For every in-scope record type, the output matches the corrected records apart from YAML line-wrapping. An AST comparison with string contents blanked shows no logic change. `s21`, `s24`, `s25` and `s27` are identical. `s22` adds one `src(11, ...)` entry (`lpc.term.the-flock`). `s28` adds eight `(source_id, locus)` tuples inside `src()` calls. The only other differences are `canon_cells` on part-1 record types, which the separate canon-closure script sets. They are not CO-LPC-3 changes.

### Prior findings

| Finding | Sev | Status | Note |
|---|---|---|---|
| C-1 council scale | P1 | **Fixed** | "From three provinces", the eighty-seven sentences, the two absent bishops' vote, and the presbyters, deacons and "plebis maxima parte" match SENT:105-109 and SENT §83 (Natalis). The locus is corrected. |
| C-2 two cities | P2 | **Fixed** | "Outside Rome." The locus now says it restates Doc_01 §2. The Capsule line 9 is also fixed. |
| C-3 admin objects | P2 | **Fixed** | |
| C-4 Caution 2 | P1 | **Fixed**, with one new P2 (N-9) | It now bars "the church's history of those years" and allows Augustine's own account of 386-391. The silence is "held as Contested" with the Morin reason. Sentences are 23 words or fewer. |
| C-5 Caution 5 | P1 | **Fixed** | CTH:7095 (XVI.5.21, "denis libris auri", 392). CTH:7185-7195 (XVI.5.52, gold by rank, issued at Ravenna under Honorius and Theodosius, 412). The council is "dated 401 only by an editor's note" (NPNF104 endnote 2521). "In gold by rank" leaves out the Circumcellions' silver fine. That is acceptable for a caution, and no finding is raised. `lpc.source.augustine-correction-of-the-donatists` is corrected the same way. Its quotation "we carried our point... envoys were sent to the court of the Count" is word for word (NPNF104 Letter 185 §25). |
| C-6 horizon | P2 | **Fixed** in record | The sister wording "a silence in your own record" remains in the Datus prompt line 21 and Doc_02 §7 line 122 (N-7). |
| C-7 interval | P2 | **Fixed** in record | Not carried to the Capsule (lines 19, 69), the prompt (lines 29, 37) or World Profile line 598 (N-6). |
| C-8 thinness | P2 | **Fixed** | |
| C-9 road back | P1 | **Fixed** | "never withheld forever from one who truly walks it" matches ANF05:33961-33969. The council refuses only those who "do not repent, nor give evidence of sorrow", and only when they beg in sickness. The fix is no wider than the source. The Capsule carries the same wording, and generator `s27` emits it. |
| C-10 reasoning note | P2 | **Fixed** in record | Not carried to prompt line 41 (N-8). |
| C-11 compel turn 1 | P1 | **Fixed** | "By his own later account", "he and his colleagues in council asked the emperors" and "not even granted" match NPNF104 Letter 185 §25-26 ("certain of the brethren, of whom I was one", "sought in preference from the emperors", "our envoys could not obtain"). "He tells it as a change of mind. We report it as he tells it" leaves the contested question open. Prompt and Capsule carry the same fix. |
| C-12 compel turn 2 | P1 | **Fixed** | Matches NPNF101:38245-38262 (Letter XCIII §17): "not by the words of those who controverted it, but by the conclusive instances to which they could point", his own town "once wholly on the side of Donatus", "so many others which were mentioned to me by name". |
| C-13 font | P2 | **Fixed** in record | "Bring the person to the water again" remains in Capsule lines 21 and 69, prompt line 31 and World Profile line 594 (N-5). |
| C-14 road back named | P1 | **Fixed**, with a new P1 (N-3) | The invented purpose is gone. The new quoted phrase is not word for word. |
| C-15 force silence | P1 | **Fixed** | Labelled Contested and scoped to the pastoral voice. Doc_08 2B-4 is aligned. |
| C-16 "overturned" | P2 | **Fixed** | Also fixed in Doc_08 2B-4. |
| C-17 Retractationes | P1 | **Fixed** in record and Doc_08 | Matches Knoll, Retr. lines 92 and 13731 ("praeter epistulas et sermones"). World Profile line 392 still reads "reviewed his own works — whether in books, letters, or treatises". That is the plan stated at Retr. line 1511, told as if it were done (N-4). |
| C-18 thirteen letters | P2 | **Fixed** in record and Doc_08 | World Profile line 392 still says "forwarded his own correspondence for the record" (N-4). |
| C-19 De Pudicitia locus | P2 | **Not fixed, carried** | Carried as OG-64: there is no source record for De Pudicitia. Accepted as carried. |
| C-20 Donatist schism | P2 | **Fixed** | |
| C-21 emperors | P2 | **Fixed** | Doc_08, World Profile and Phase 4 are aligned. |
| C-22 Punic | P1 | **Fixed**, with a new P2 (N-10) | The drafter is right that "Punic" in Letter LXXXIV is an editor's emendation. NPNF101:35996 endnote 2081: "The text here gives latinâ". Letter CCIX §3 (NPNF101:54466-54469) supports the new sentence: "acquainted with the Punic language", for Fussala, "a small town" (castellum, line 54444). "Country town" is fair. "Latin was not every hearer's tongue" is a fair inference and no wider. The record's `sources` is empty and does not cite CCIX (N-10). |
| C-23 short notice | P2 | **Fixed** in record, Doc_01 and Doc_08 | Doc_02 §1 line 39 still says "on short notice" (N-11). |
| C-24 formulas | P2 | **Fixed** | "Gave both formulas of conciliar authority the councils they speak about" is accurate, though stiff. |
| C-25 transmission | P1 | **Fixed** | Record, Doc_02 §6, Doc_08 2B-5 and §6, and the World Profile are aligned. Doc_02 §6 cites On Baptism II.3-4, which is NPNF104:11303 (div v.iv.iv.iii), and that checks. Doc_02 §1 line 49 still says "the doctrinally and institutionally victorious party's literature on every dispute he engaged" (N-11). |
| C-26 Vandal date | P2 | **Not fixed, carried** | Carried as OG-64. The drafter found that Prosper enters the crossing under the consuls of 427. The record still states 429 as fact, and that is now a known open discrepancy. Accepted as carried. |
| C-27 collegial communion | P1 | **Fixed in record and Doc_04; not carried to the Capsule or prompt** | See N-1 and N-2. |
| C-28 De Pudicitia locus | P2 | **Not fixed, carried** | As C-19. |
| C-29 Pelagian claim | P1 | **Fixed** | Record, Doc_01 §6, Doc_04 Candidate 7, the World Profile and the claims row are aligned. NPNF105:7780-7785 (On Nature and Grace 59) confirms that Augustine sets out the claim. |
| C-30 Possidius | P2 | **Fixed** | |
| C-31 "without a break" | P2 | **Fixed** | |
| C-32 vernacular | P2 | **Fixed** | Doc_08 §5, Phase 2 and Layer 3 are aligned. |
| C-33 interval | P2 | **Fixed** | Doc_04 Candidate 6 is aligned. |
| C-34 "break" | P2 | **Fixed** in record | Doc_04 line 114 still says "the entire Stephen/Cyprian rupture" (N-11). |
| C-35 one episcopate | P1 | **Fixed in record, chunk Quick Meaning and World Profile brief; not carried to prompt line 29 or the chunk's World Hearing** | See N-2. |
| C-36 superlative | P1 | **Fixed** | |
| C-37 Punic speakers | P2 | **Fixed** | |
| C-38 130 years | P2 | **Fixed** | The prompt line 21 is aligned. |
| C-39 women loci | P2 | **Partly fixed** | The Ep. XXXIV locus is added and checked at ANF05:32095-32110. The Passio has no source record, so it is carried as OG-64. Its locus already sits in `why_sources_cannot_answer`. Accepted. |
| C-40 Albina | P2 | **Fixed** | |

Tally: 33 fixed, 1 partly fixed and accepted (C-39), 3 not fixed but carried in OG-64 and accepted (C-19, C-26, C-28). Of the 33 fixed, 6 are fixed in their own record but not carried to sister sites (C-7, C-10, C-13, C-27, C-35, and C-17/C-18 in the World Profile). Those gaps are raised below as N-findings.

### Special-attention items

- **Caution 2.** The narrowing works as intended, and the silence is labelled Contested. A residual ambiguity is raised as N-9 (P2).
- **Caution 5 and the source record.** Both are correct at source (see C-5).
- **Voice_craft "not withheld forever from one who truly walks it".** Correct against Ep. LI §23 (see C-9).
- **Compel demonstration.** Correct against Letter 185 §25-26 and Letter XCIII §17. The prompt line 21 "You report the stages as they actually ran" leans toward settling the contested question (N-7).
- **Punic sentence.** The move to Letter CCIX §3 is right and is supported (see C-22).
- **Doc_02 §6, Doc_04 and Doc_08.** Doc_02 §6 and Doc_08 are correct. **Doc_04's G3 Formation test does not still "Pass" as written** (N-1).
- **Datus prompt.** The changed paragraph (line 21) is accurate and readable. Unchanged lines in the same file still carry claims that CO-LPC-3 corrected elsewhere (N-2, N-5 to N-8).
- **Generators.** Clean (see Mechanical checks). The `s28` module docstring still quotes the old Capsule wording and the invented "in one place, on one day" (N-12).

### New findings

**N-1 · P1 · Doc_04 Candidate 3 Formation "Passes" next to an unreconciled counter-instance; the Capsule still states the universal claim**
- `Build/worlds/lpc/Doc_04_Gravity_Discovery.md` line 60 now names the 418 anathema but still reads "Passes" without saying why the counter-instance does not defeat the test. The counter-instance is checked at source (`npnf214`, African Code canon CIX). As written, the verdict is wider than its evidence.
- `Build/worlds/lpc/lpc_World_Capsule_Core.md` line 19 still says: "Every hard disagreement your own life has produced has tested this rule. None has broken it." That is the C-27 claim, and the Capsule feeds the Representative.
- Judgement: the test can still pass once its scope is stated. The scoped gravity is disagreement over practice among bishops in communion. Its other tests rest on rebaptism and Donatism, so the Primary classification need not change. Whether it stays Primary under the narrowed scope is the build thread's call, and an escalation if it is disputed.
- Proposed Doc_04 line 60: "- **Formation:** Passes, within a stated scope. Over rebaptism, the sharpest dispute between them, neither bishop breaks fellowship with a fellow bishop. The grace dispute shows the limit: the African council of 418 anathematized the Pelagian positions (`npnf214`, African Code canon CIX). This gravity shapes disagreement over practice among bishops in communion. It does not reach a teaching a council judged heresy."
- Proposed Capsule line 19, last two sentences: "Rebaptism, the hardest disagreement among your own bishops, tested this rule, and it held. Teaching your councils judged false was another matter. In your later years, African councils condemned what the Pelagians taught."

**N-2 · P1 · The Datus prompt still teaches "held whole" (C-35) and an unscoped "never separate" (C-27)**
- Prompt line 29: "The one episcopate is undivided, held whole by each bishop rather than parceled out between colleagues." This is the reading C-35 found contrary to De Unitate 5 (ANF05:42288-42291: "each part of which is held by each one for the whole"). The same reading remains in `Lexicon-Chunks/lpclex014_the-one-episcopate.md` line 47 (World Hearing, which now contradicts the chunk's own corrected Quick Meaning) and World Profile line 534 (distortion note).
- Prompt line 29 also says: "Disagreement, in your own life, is not a reason to separate." That is C-27 unscoped, in the voice Datus speaks from.
- Proposed prompt line 29, replacing the last two sentences and the "Disagreement" sentence:
  - "Disagreement with a colleague, in your own life, is not a reason to separate."
  - "The one episcopate is undivided. Each bishop holds his part of it for the whole. That is exactly why disagreeing with a colleague can never mean stepping outside all of it."
- Proposed chunk line 47: "Neither. A single office, one and undivided, each part of it held by each bishop for the whole, which makes both equality among bishops and the seriousness of separation follow from the same conviction."
- Proposed World Profile line 534: replace "held whole by each holder" with "each part of it held by each bishop for the whole".

**N-3 · P1 · Road-back demonstration: quotation not word for word**
- `records/lpc/demonstration/lpc.demo.road-back-examined.md` turn 1: "Not a vague 'this man and his friends'". The source says "Such a one with his friends" (ANF05:29941-29942, Ep. X §4).
- The record body's last paragraph ("The exchange text itself does not quote the letter directly") is now stale.
- Proposed text: "Their name is set down. Not a vague 'such a one with his friends', but one person, by name, whose change someone has actually seen."
- Proposed body: "The exchange quotes one phrase of the letter, 'such a one with his friends', word for word."

**N-4 · P2 · World Profile line 392 keeps C-17 and C-18 in the paragraph CO-LPC-3 edited**
- "Augustine, near the end of his life, reviewed his own works — whether in books, letters, or treatises" states the plan at Retr. line 1511 as if it were done. Retr. lines 92 and 13731 show he did not reach the letters and sermons.
- Proposed text: "Cyprian sent thirteen of his own letters to Rome to give account of what he had done, and returned a suspect letter for collation on suspicion of alteration; Augustine, near the end of his life, set out to review his works 'whether in books, letters, or treatises' with a certain judicial severity, and reached his books but not his letters and sermons (*Retractationes*, Prologus; `Source_Registry.md` row 209)."

**N-5 · P2 · "Water again" (C-13) remains in the Representative-facing texts**
- Capsule lines 21 and 69, prompt line 31, World Profile line 594.
- Proposed text, at each site: replace "bring the person to the water again" with "baptize the person in the church, for the first time".

**N-6 · P2 · "A century and a third" for 256 to c. 400 (C-7) remains**
- Capsule lines 19 and 69, prompt lines 29 and 37, World Profile line 598.
- Proposed text: "Nearly a century and a half later" and "nearly a century and a half apart".

**N-7 · P2 · Datus prompt line 21: two residues**
- "It is a silence in your own record" is wider than the pastoral-voice finding (C-6). Proposed text: "it is a silence in your own pastoral voice".
- "You report the stages as they actually ran" settles the question C-11 left open. Proposed text: "You report the stages as your own later account gives them".
- Doc_02 §7 line 122 has the same "silence in this world's own record" wording.

**N-8 · P2 · Datus prompt line 41: "inside a bond neither of you is willing to break" (C-10 not carried)**
- Proposed text: "usually against someone who actually disagrees with you. Where he is a colleague, you argue inside a bond neither of you is willing to break."

**N-9 · P2 · Caution 2 reaches Augustine's own later writing about 258-391**
- "Never describe the church's history of those years from this world's own collection" also bars Augustine's own later accounts of those years. One example is his answer about Constantine in `lpc.witness.constantine-did-not-corrupt`.
- Proposed text: "Never describe the church's history of those years from this world's own collection, except as Augustine's own later view, given as his and dated to when he wrote it."

**N-10 · P2 · `lpc.force.inherited-latin-theological-vocabulary` cites no locus for its new Documented sentence**
- The record has `sources: []`. Proposed fix: add `lpc.source.augustine-general-correspondence`, locus "Letter CCIX §3, a Punic-speaking bishop sought for Fussala". No text change.

**N-11 · P2 · Upstream documents still carry three corrected claims**
- Doc_02 §1 line 39: "on short notice" (C-23).
- Doc_02 §1 line 49: "victorious party's literature on every dispute he engaged" (C-25).
- Doc_04 line 114: "the entire Stephen/Cyprian rupture" (C-34).
- Proposed text: delete "on short notice". Replace the second with "the literature of the side that became canonical, which kept Cyprian even where it judged him wrong, on rebaptism". Replace the third with "the entire Stephen/Cyprian dispute".

**N-12 · P2 · `scripts/wb_lpc_s28.py` docstring (lines 138-147) still quotes the superseded wording**
- It quotes the old Capsule wording ("the empire's own capital in the west") and "this many named men, in one place, on one day" (C-1, C-2).
- Docstring only; nothing emitted. Proposed text: quote the current Capsule line ("outside Rome") and "a bare scale fact (eighty-seven sentences, with presbyters, deacons and people present)".

### Claims rows

| id | status | confidence | source | check | file | claim |
|---|---|---|---|---|---|---|
| 9ff94551 | JUDGEMENT | Widely Accepted | cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml; cic/texts/npnf105_augustine-anti-pelagian-writings.xml; records/lpc/contested_claim/lpc.contested.grace-pelagius-characterization.md | Read at source. The Donatist half: Augustine quotes and answers Petilian, "What we look for is the conscience of the giver to cleanse that of the recipient" (Answer to Petilian I.1-2, npnf104 lines 15368-15376). The Pelagian half: Augustine puts to Pelagius "Why do you affirm that man without the help of God's grace is able to avoid sin?" (On Nature and Grace 59, npnf105 lines 7780-7785). The claim now says Augustine attributes it, which matches the contested_claim record. "Sole determinant" is the document's own synthesis of both refusals, not a string-searchable fact. | Doc_01_World_Identification_Boundaries_Orientation.md | For Augustine, Donatist separatism's claim that a sacrament's validity depends on the personal purity of the minister administering it, and, on a different axis, the claim Augustine attributes to Pelagian anthropology, that a person's own moral effort is sufficient without grace — in both cases a refusal to let one factor (a minister's own purity; a believer's own unaided will) become the sole determinant of the church's or the soul's own standing. |
| 5e176079 | JUDGEMENT | Contested | Build/worlds/lpc/Doc_02_Source_Ecology.md; Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md; cic/texts/npnf101_augustine-confessions-letters.xml | A binding instruction, not a claim about the record. It rests on Doc_02 section 7 (line 122): no assessed pastoral voice for 258-391, qualified to what this build has assessed, and Contested because the nine tractatus in Morin 1917 are unread (OG-54). The same caution allows Augustine's own account of 386-391 (Confessions IX.vi.14, npnf101 lines 13731-13732). Open point: as worded, it also reaches Augustine's own later writing about those years, for example records/lpc/doctrinal_witness/lpc.witness.constantine-did-not-corrupt.md (recheck N-9). | lpc.core.latin-pastoral-congregational-christianity.md | Never describe the church's history of those years from this world's own collection. |
| 98b506cd | JUDGEMENT | Widely Accepted | cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml; cic/texts/npnf105_augustine-anti-pelagian-writings.xml; cic/texts/possidius_vita-augustini_weiskotten1919.txt; Build/worlds/lpc/Doc_02_Source_Ecology.md | Compared the three crossings at source. On Baptism argues Cyprian's council acts across seven books (npnf104 lines 10756-15292, 254 lines naming Cyprian). The anti-Pelagian works cite Cyprian on grace in a few chapters (npnf105 line 20912, Testimonies III.4). Possidius quotes De Mortalitate once (Weiskotten lines 3877-3878). 'As much' is a reading of scale, not a count. The silence clause follows Doc_02 section 7 (line 122) and is labelled Contested. | lpc.force.augustine-engagement-cyprian-conciliar-acts.md | No other force carries as much of the world's formation logic across the 133 years between the two phases, which this build has assessed as a silence in the world's pastoral voice (Contested). |

### Counts

- Prior findings: 40 (15 P1, 25 P2).
  - Fixed: 33.
  - Partly fixed and accepted: 1 (C-39).
  - Not fixed but carried in OG-64 and accepted: 3 (C-19, C-26, C-28).
  - Not fixed and not carried: 0.
  - All 15 prior P1s are fixed in their own records.
  - C-27 and C-35 were not carried to the Capsule or the Datus prompt; that gap is raised as N-1 and N-2.
- New findings: 12. **P0: 0. P1: 3** (N-1, N-2, N-3). P2: 9 (N-4 to N-12).
- Claims rows: 3 completed, all JUDGEMENT.
- Regate: PASS. Claims: PASS. Generators: emit the corrected text. No logic change beyond `src()` and source tuples.

## Combined

All prior P1s are fixed in their own records. New findings: 0 P0, 6 P1 (Part 1 N1 to N3, Part 2 N-1 to N-3), 16 P2.

VERDICT: Substantial revision required
