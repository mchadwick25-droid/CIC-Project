Simulated review — informational only, not an Article 31 substitute.

# lpc B-7a: independent review of the world_front and facilitator_brief records

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** claude-sonnet-5-5
- **Drafter note:** commit 1267bbcf0 ("lpc L2: B-7a world_front and facilitator_brief records drafted; claims registered") carries the Sonnet 5.5 trailer.
- **Reviewer agent:** independent Opus review subagent (fresh context, high effort; did not draft either record)
- **Drafter agent:** B-7a drafting session (commit 1267bbcf0)
- **Round:** 1
- **Truncation check, method 1:** line count and closing marker: `wc -l` on this file returns 327 lines, and `tail -n 1` returns "End of review.", both run after the last edit.
- **Truncation check, method 2:** set comparison in Python: the finding ids in the "Verdicts by finding" table equal, as a set, the finding ids used as `###` headings (B1, S1 to S11, O1 to O14); none is missing on either side.
- **Scope:** `records/lpc/world_front/lpc.front.latin-pastoral-congregational-christianity.md` and `records/lpc/facilitator_brief/lpc.facilitator_brief.latin-pastoral-congregational-christianity.md`, as committed at HEAD (both working-tree files hash identical to the HEAD blobs: 07448ead8 and 17ca0bc44). Nothing in `records/` was edited. This file is the only file written.
- **Standards read:** CLAUDE.md (Safety comes first; Source fidelity; Accessible and rigorous, including No AI tells); `Build/reference/method/CiC_Register_Bar_2026-08-29.md`; `records/syr/demonstration/syr.demo.room-for-doubt.md`; Record-Native Build Process V2.0, row B-7a and section 5; Completion Standard V1.4 (row for `world_front`, `facilitator_brief`, site JSON); Constitution V2.2 Articles 20, 23 and 29 (text rendering); `Build/reference/L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.6.docx` (text extracted; the acute-distress and harmful-dynamic triggers, and "Redirect, never refuse").
- **Fleet exemplars read:** `records/alx/world_front/`, `records/alx/facilitator_brief/`, and the `don`, `gallic` and `ijc` briefs' `pairing_guidance` (the second world's pair is `don`).
- **World material read:** `lpc.core`; all nine `honest_limit` records; every record the two files cite that bears on a checked claim (stories, forces, gravities, quotes, terms, contested claims, witnesses, voice craft); Doc_02 sections 6 to 8; Doc_09 section 7; Doc_01 sections 1 and 5 (contrast lines); `lpcctx002` and `lpcctx004`; `Representative/lpc_Rep_Phase6_Facilitator_Coordination_Round1.md`; the three partner-world records.

## Verdict

**Not ready to proceed as drafted. One blocking finding, eleven substantial, fourteen optional.** The drafting is careful and mostly faithful. Every id both files cite resolves (81 distinct ids checked against `records/`). The silence statement matches Doc_02 section 7 in the tile and the brief. No content is lifted from another world. The safety caution is right in substance. But one facilitator-facing absence claim is false against the completed world (B1). Several front claims run past the record that grounds them (S1 to S7). Two brief items take one side of a question the world holds open (S8, S9). And the pairings name their partner claims in prose without riding them, and two of the three lack the built-in cautions B-7a requires (S11).

Every finding below carries exact proposed wording. All proposed replacement texts were graded with `engine.m1.gates.grade_text`, and each clears FK 10 and FRE 60.

## Gates run

| Gate | Result |
|---|---|
| `python -m engine.m10.cli regate lpc` | PASS. 269 public fields checked; 0 hard failures in the two records. |
| Per-field grade of all 67 prose fields in the two records (`grade_text`, the gate's own scorer) | 67 of 67 clear FK 10 and FRE 60. Lowest FRE: `facilitator_brief.formation_limitations[0]` 60.52, `world_front.voices[3].text` 60.40, `facilitator_brief.world_identity` 60.57 (fragile; any edit there must be regraded). 43 of 67 sit below FK 8 (see O11). |
| `python -m engine.m10.cli citations` on both files | PASS |
| `python -m engine.m10.cli claims lpc` | PASS (110 derived, 110 registered) |
| `python -m engine.m10.cli records lpc` | PASS |
| Manual id resolution (all ids in both files, including the brief's top-level `grounded_in`, which `gate_referential` does not walk; see O12) | 81 of 81 resolve |
| 7-word n-gram overlap against every other world's records | Only fleet scaffold phrases ("For a pastor or teacher, this world offers", "It serves participants who want to") and YAML keys. No substantive text lifted. |
| Sentence length, both files | Average 15.5 words over 324 sentences. 31 sentences run past 25 words (see O1). |

## Verdicts by field

| Record | Field | Verdict | Findings |
|---|---|---|---|
| front | skim.tile | Revise | S2, O1 |
| front | orientation.story[0], [2], [5], [6], [7], [10], [11] | Pass | O1 (optional wording only on [2], [10], [11]) |
| front | orientation.story[1], [3], [4] | Pass on fact; revise wording | O1 |
| front | orientation.story[8] | Pass | none |
| front | orientation.story[9] | Revise | S4 |
| front | orientation.story[12] | Revise | S1 |
| front | orientation.story[13] | Revise | S3 |
| front | documented_stories | Pass, one title optional | O2 |
| front | voices[0].hedge | Revise | S1 |
| front | voices[1].hedge | Revise | S7 |
| front | voices[0..3].text, voices[2..3].hedge | Pass | none |
| front | floor_note | Pass | none |
| front | legacy[0] | Revise | S5 |
| front | legacy[1] | Revise | S6 |
| front | relations_summary | Pass | O1, O14 |
| front | sourcing, read_first | Pass | none |
| front | narrative.who_speaks | Pass | none |
| front | narrative.quiet | Pass (judgement call upheld) | ruling 7a |
| front | narrative.questions | Pass; one cite optional | O9, O10 |
| front | pull_quotes, glossary | Pass | none |
| front | experience_today (absent) | Omission upheld | ruling 7b |
| brief | world_identity | Pass | O8 |
| brief | formation_strengths[0], [2], [3] | Pass | none |
| brief | formation_strengths[1] | Revise | S8 |
| brief | formation_strengths[4] | Pass | O3 |
| brief | formation_limitations[0] to [5], [7], [8] | Pass | O13 |
| brief | formation_limitations[6] | Revise (blocking) | B1 |
| brief | participant_type_fit | Pass | none |
| brief | pairing_guidance | Revise | S11, O4, O5 |
| brief | cautions[0], [2], [4], [5] | Pass | none |
| brief | cautions[1] | Revise | S10 |
| brief | cautions[3] | Revise | S9 |
| brief | cautions[6] | Pass | O6 |
| brief | cautions[7] | Pass; wording optional | O7 |
| brief | living_tradition_handling | Pass | check 4 |
| brief | redirect_notes | Pass | check 5 |

## Verdicts by finding

| Id | Severity | Record and field | One line |
|---|---|---|---|
| B1 | blocking | brief formation_limitations[6] | Says the words of baptism do not survive; the world holds two spoken baptismal exchanges |
| S1 | substantial | front story[12], voices[0].hedge | "No one has fixed their date or place" claims more than Doc_02 section 7 |
| S2 | substantial | front skim.tile | "No woman's own words survive" is stronger than the limit record |
| S3 | substantial | front story[13] | "Almost no one wrote about an ordinary week" contradicts Doc_09 section 7 item 5 and the front's own read_first |
| S4 | substantial | front story[9] | The 1,798 count is a raw count over an English translation with markup |
| S5 | substantial | front legacy[0] | "The side that won every dispute" contradicts Cyprian's overturned ruling; "English texts date from the 1800s" is wrong for the 1919 Possidius |
| S6 | substantial | front legacy[1] | Drops the source's "world's own self-understanding" framing; cryptic |
| S7 | substantial | front voices[1].hedge | The later dating of the Life also moves its author away from the deacon; the hedge omits it |
| S8 | substantial | brief formation_strengths[1] | States Cyprian's side of the held-open conciliar question as the world's |
| S9 | substantial | brief cautions[3] | Drops "by his own later account" from Augustine's first phase |
| S10 | substantial | brief cautions[1] | "Datus does not comment on the silence" misdescribes Datus |
| S11 | substantial | brief pairing_guidance | Partner claims not in grounded_in; two pairings lack the ending and handoff cautions; ijc characterization overstated |
| O1 | optional | both | AI-tell and register wording |
| O2 | optional | front documented_stories[2].title | Title implies care reached persecutors |
| O3 | optional | brief formation_strengths[4] | "Eight years later" has no dated basis shown |
| O4 | optional | brief pairing_guidance | Gallic wording (folded into S11 proposal) |
| O5 | optional | brief pairing_guidance | "Donatism runs to 439 and beyond" |
| O6 | optional | brief cautions[6] | Template anchoring; otherness versus distress |
| O7 | optional | brief cautions[7] | "Speaks in his place" |
| O8 | optional | brief world_identity | Grammar of the crises sentence |
| O9 | optional | front questions F4-I cite | A closer cite exists |
| O10 | optional | cited force records | Cite text renders build narration on the site (flag only) |
| O11 | optional | both | 43 of 67 fields below FK 8; standard and engine differ |
| O12 | optional | engine | Brief `grounded_in` ids are never gated |
| O13 | optional | brief formation_limitations | Article 20 "why"; Article 23 separation |
| O14 | optional | front relations_summary | "On a Sunday" |

## Findings

### B1

**Blocking. Brief `formation_limitations[6]`.** The item says: "No fixed order of service survives. Neither do the words of baptism, or the words that restored a penitent." The second sentence is false against the completed world. `Build/worlds/lpc/lpcctx002_the-questions-at-the-water.md` carries two fixed spoken exchanges at the font. One is the question about belief ("Do you believe in eternal life and the remission of sins through the holy Church?"), from Cyprian's years. The other is the renunciation ("Do you renounce?" / "I renounce."), from Augustine's years. Both are Widely Accepted. Phase Six section 2 (the source this item draws on) lists "the renunciation formula" among what Datus can describe. It names as missing only "no fixed order of service, no consecration formula, no set catechetical curriculum". A facilitator reading the brief would tell a participant that the baptismal words are lost, and Datus would then give them. That is a false absence claim in the one record the Facilitator trusts, so it blocks. The restoration clause is consistent with `lpcctx004`, which attests the laying on of hands but no words.

Proposed wording (FK 7.8, FRE 68.7):

> The rites are argued over more than they are described. No fixed order of service survives, and the rites have not yet been read as evidence in their own right. Two short spoken exchanges at baptism are known: a question about belief, and a renunciation answered in kind. Each is attested in one bishop's years only, so neither wording should be claimed for both. A restored penitent received a hand laid on the head, but these records hold no words for that act. A request for a whole rite, word for word, goes beyond what these records can answer.

The claims register row for this unit must be re-derived after the edit (`claims lpc --bootstrap`).

### S1

**Substantial. Front `orientation.story[12]` and `voices[0].hedge`.** Both say of the pseudo-Cyprianic works: "no one has fixed their date or place". Doc_02 section 7 says something narrower: "the vendored files do not fix" their date and place. The wider claim is also not true of the scholarship Doc_02 itself cites. Monceaux places *De aleatoribus* in third-century Africa, and the Registry's row 6 note reports that two pieces are widely attributed to Novatian. The brief has it right ("The files do not fix their date or place"). The front also says "a few short works" where Doc_02 and the brief say "several".

Proposed `story[12]` (FK 7.5, FRE 68.8):

> About 130 years lie between Cyprian's death in 258 and Augustine's ordination in 391. In that time, this world's own record has no voice of a bishop speaking to his own people that can be dated and placed. The years are well documented elsewhere, mostly by the rival church of the Donatists, but this world does not borrow that record. Several short works carry Cyprian's name. The texts held here do not fix their date or place, none has been assessed, and none is drawn on. Texts cross the gap, however. Augustine reads Cyprian's council and argues with it, and Augustine's church describes itself as the same communion Cyprian led.

Proposed `voices[0].hedge` (FK 5.1, FRE 81.4):

> The claim that Cyprian was a new convert when he was chosen rests on Pontius alone. The collection of letters under his name also holds letters by other people. Several short works carry his name. The texts held here do not fix their date or place, and nothing here draws on them.

### S2

**Substantial. Front `skim.tile`.** "No woman's own words survive" is stronger than `lpc.limit.womens-own-voice`. That record says no text *written by a woman* survives, and it names Quartillosa's first-person vision, reported inside a martyr act men wrote. The brief reports Quartillosa correctly. The tile also opens with a 31-word sentence.

Proposed tile (FK 7.6, FRE 65.7):

> Between about 246 and 430 CE, Christians in Carthage and Hippo lived their faith as a congregation with a bishop who answered for it. Both cities lay on the coast of Roman North Africa. Two bishops hold this world together. Cyprian led Carthage through persecution, plague and schism. Augustine preached at Hippo, taught those preparing for baptism, and gave the sacraments to his own people. The people chose both men for office, against their wishes. When Rome forced Christians to sacrifice, some gave in, and the church answered with a public road back that was walked in stages. When its bishops disagreed, even over baptism, they argued at length and did not cast each other out. About 130 years separate the two bishops. In that time, this world's own record holds no bishop's voice to his own people that can be dated and placed. Almost everything we know comes from educated men. No text written by a woman survives, and nothing survives in the words of those who failed under persecution.

The silence sentence keeps the registered wording, so claims row `e472ad25` still applies. The tile's women and lapsed sentence is a reworded claim and needs its register row re-derived.

### S3

**Substantial. Front `orientation.story[13]`.** "Almost no one wrote about an ordinary week" contradicts Doc_09 section 7 item 5. That item says the missing story of an ordinary pastorate is "this build's, not the record's", because Possidius, *Vita* XIX to XXVII, is nine chapters of exactly that. The front's own `read_first[3]` note says the same chapters "show his ordinary work". Claims row `8f060a71` justifies the sentence only on the reading "ordinary believer", so the fix is to say that. "Seen and not heard" is also an idiom with a children's-proverb ring, and it overstates the limit record ("almost never narrate").

Proposed (FK 7.7, FRE 65.1):

> Almost everything above comes from two educated men. Women appear in the record, but almost none of them speaks in it. Those who failed under persecution were the reason for the first great crisis, and they left nothing in their own words. The same is true of the countryside, and of the Punic and Berber languages spoken beyond the two cities. Almost no ordinary believer wrote about an ordinary week. This world's own record does not answer these questions, and it does not pretend to.

### S4

**Substantial. Front `orientation.story[9]`.** "The word grace appears in them 1,798 times." The source records (`lpc.gravity.grace-and-human-incapacity`, `lpc.term.grace`, `lpc.contested.grace-pelagius-characterization`) give 1,798 as a *raw* count over the vendored 19th-century English translation, markup included, and 1,665 once markup is stripped. A participant will read the figure as Augustine's own usage, and as exact. That is false precision. What the records support without qualification is that grace is "by a wide margin, the single highest" such count.

Proposed (FK 8.9, FRE 63.8):

> Augustine's teaching on grace is the most heavily documented concern in this world. It came out of a fight with Pelagian teaching, which Augustine said held that a believer's own effort is enough. He wrote thirteen works against it, and grace is by far the most frequent key word in them. This belongs to Augustine's years only, and it is one voice in one set of books. Modern scholars ask whether Pelagius held the view Augustine describes, and no Pelagian reply survives in this world's own record to check it against.

### S5

**Substantial. Front `orientation.legacy[0]`.** Two defects. First, "each man stood on the side that won every dispute he entered". Cyprian's rebaptism ruling did not win. The same paragraph says Augustine overturned it, and `story[7]` says so too. The source force (`lpc.force.transmission-institutionally-dominant-side`) says "institutionally dominant", which the front hardened to "won". Its "every dispute" wording also deserves a record-layer look by the record's owner (flag only; not this thread's record). Second, "The English texts used here date from the 1800s" is wrong. The front's own `read_first[3]` is the Weiskotten translation of 1919, and the force says "mainly".

Proposed (FK 6.9, FRE 66.2):

> Only texts carry this world across its long silence. No line of living heirs does. Augustine read the ruling of Cyprian's council, argued with it and overturned it. He also quoted Cyprian's books, and Possidius quoted Cyprian's book on mortality. The writings of both bishops survive unusually full. The church that copied and kept them honored both men, even after it set aside one of Cyprian's rulings. Most of the English texts used here are translations made in the 1800s.

### S6

**Substantial. Front `orientation.legacy[1]`.** "This world did not feel that as an ending, and it did not feel it as nothing." The source force (`lpc.force.corpus-outliving-the-world`) frames this as "the world's own self-understanding. It is reported as such and not assessed for historical accuracy." The front drops that framing and states a feeling as fact. The sentence is also cryptic, the kind of balanced double negative the Register Bar rules out.

Proposed (FK 7.5, FRE 69.4):

> Augustine's writing later became the foundation of Western theology. By this world's own account, neither bishop wrote with that future in view. A bishop writing against a live error writes for the people in front of him and the case at hand, not for a tradition he expects to found. Even so, both men expected their writings to outlast them. Cyprian gathered and sent out his own letters, and near the end Augustine went back over his life's work and corrected it. The world's own end came from outside, with the Vandal siege in 430.

### S7

**Substantial. Front `voices[1].hedge`.** The hedge gives the two datings of the Life (259, or the end of the third century at the earliest) but not what the later one means. Doc_02 section 7 quotes Koch: the author is "a writer living at the end of the third century at the earliest, who plays the eyewitness". On that view the author is not Cyprian's deacon. World core caution 2 already says "the life that bears the name of his deacon Pontius". The hedge also states as settled one side of `lpc.contested.cyprian-death-genre` ("a reader cannot separate the facts from the pattern"). That record's `concedes` field says Pontius meets the author test and the bare facts are not in dispute.

Proposed (FK 6.6, FRE 78.0):

> Pontius wrote to praise a man already honored as a martyr. He tells Cyprian's death in the pattern of Scripture, so its details are hard to check without a second witness. The court's own record of the trial survives, but it has not been read here. Scholars date the Life to 259, or to the end of the third century at the earliest. On the later dating, the author was not Cyprian's deacon but a later writer who wrote as if he had been there.

### S8

**Substantial. Brief `formation_strengths[1]`.** "Each bishop judged for himself, and none ruled over another. A council was a room where each man said what he held." That is Cyprian's theory, stated as the world's. The world holds the conciliar axis open (world core caution 6; the brief's own `cautions[4]`; `lpc.gravity.conciliar-authority-theory`). Augustine's view was layered and correctable.

Proposed (FK 7.5, FRE 61.1):

> It serves participants who want to know who decides, and whether ordinary people had a say. The people put bishops into office by acclaim, sometimes against the man's own wishes. At Cyprian's council in 256, each bishop spoke for himself. Cyprian said no bishop should rule over another. Augustine later held that a later council could put right an earlier one. The world keeps that question open.

### S9

**Substantial. Brief `cautions[3]`.** "Augustine first opposes compulsion" drops "by his own later account", which world core caution 4 and the front's `story[8]` both keep. Whether that first phase is a real stance or a later self-presentation is exactly the question `lpc.contested.compel-coercion-development` holds open.

Proposed (FK 6.4, FRE 65.9):

> The record on state power has three phases. Cyprian never asks the state for anything. By his own later account, Augustine first opposed compulsion. Early in his time as bishop he asked for narrow legal protection, which was not granted. Later he defended wider force already in place. Do not compress this to present but late.

### S10

**Substantial. Brief `cautions[1]`.** "Datus does not comment on the silence." Datus does name it. `lpc.limit.the-silent-century` (emic) states it plainly, and the Permanent Prompt line 21 says "Across that stretch, your own congregational voice falls silent." What Datus is barred from is *explaining* the silence or filling it (world core `thinness`; Phase Six section 2). A facilitator told that Datus is silent here may step in when no step is needed. The Facilitator move is Phase Six's: only if Datus's own answer does not satisfy a participant who presses.

Proposed (FK 6.7, FRE 69.2):

> The 130 years between 258 and 391 are a silence in this world's own record. Never fill them from Donatism's record, which covers those years. Datus names the silence as a plain fact. He does not explain it, and he does not fill it. If a participant presses and his answer does not satisfy them, the Facilitator names the silence plainly, in the Facilitator's own voice.

### S11

**Substantial. Brief `pairing_guidance`.** The three partner claims exist and say what the brief says, with the exceptions below. Checked: `records/don/contested_claim/don.contested.rebaptism-boundary.md`, `records/ijc/gravity/ijc.gravity.orthodoxy-enforcement.md`, `records/gallic/contested_claim/gallic.contested.beginning-of-good-will.md`. Four defects.

1. **The pairings do not ride their partner claims.** B-7a says the pairings "ride live partner claims". None of the three ids appears in `grounded_in`, or anywhere in `records/lpc` or `Build/worlds/lpc`. `gate_referential` resolves fleet ids, so they can be cited. Add all three to `pairing_guidance.grounded_in`:
   `don.contested.rebaptism-boundary`, `ijc.gravity.orthodoxy-enforcement`, `gallic.contested.beginning-of-good-will`.
2. **The ijc and gallic pairings lack two of the three built-in cautions.** The Donatism paragraph carries all three: contemporaries-not-stages, ending-not-read-back both ways, and handoff containment. The ijc paragraph says only "The caution is the same. These are contemporaries". The gallic paragraph carries contemporaries-not-stages only. `ijc` (312 to 451) runs straight through this world's 258 to 391 silence, so the containment line matters most there.
3. **The ijc characterization overstates.** "Augustine's own defence of compulsion is one of that world's main sources." The ijc gravity's sources are Sozomen, Socrates and Hilary. Augustine's *Correction of the Donatists* appears as one illustrating quote (`ijc.quote.compelled-to-come-in`).
4. **The gallic characterization puts the contested element in the record's mouth** ("Its record holds that John Cassian argued, in reply to Augustine"). Whether Conference XIII replies to Augustine is the disputed point: the chronology is contested, and Cassian's text "says both".

Proposed ijc paragraph (FK 6.7, FRE 71.8):

> Imperial and Juridical Christianity pairs on law and force. That world's record uses Augustine's own defence of compulsion to show its central concern, the use of imperial power to enforce the faith. This world reports his three steps and neither defends nor disowns them. The same three cautions hold. These are contemporaries, and the rule of Constantine is not simply the next stage after Cyprian's world. That world runs to 451, past this world's end in 430, and neither world's later years may be used to judge the other. A participant may be sent there for that world's own account of church and state. Nothing from there may fill this world's silence between 258 and 391.

Proposed gallic paragraph (FK 8.0, FRE 65.1):

> Gallic Monastic-Ascetic Christianity pairs on grace. Its record carries a contested claim: that John Cassian, replying to Augustine, taught that a good will can sometimes begin in a person's own effort. Cassian's own text says both things, and whether he was replying to Augustine at all is disputed. He wrote in Augustine's lifetime, so he is not a later correction and Augustine is not an early draft. That world runs to 450, and neither world's later years may be used to judge the other. A participant may be sent there for Cassian's own words. Nothing from there may stand in for Pelagius, whose side this world cannot supply.

Regrade the whole `pairing_guidance.text` after the edit (it now grades FK 7.5, FRE 67.3).

### O1

**Optional. Wording (AI tells and register), read against `syr.demo.room-for-doubt` and the Register Bar.** The records are etic, so "this world" is correct here (the first-person rule binds spoken fields, not the front or the brief). The main tell is mechanical ", and" chaining: 31 sentences run past 25 words, most of them two clauses stapled together. The sample never does this. Flagged phrases, with proposed wording:

- Front `story[1]`: "when they failed, he did not treat it as a problem to manage, but carried it as a wound" (a balanced not-X-but-Y shape, with a modern management frame). Proposed: "When they failed, he felt it as his own wound."
- Front `story[1]`: "because the people were not a silent audience, and they could consent, demand and elect". Proposed: "The people could consent, demand and elect."
- Front `story[3]`: "for they had sat where everyone else sat" (the archaic "for" sounds old to sound wise). Proposed: "The lapsed were the church's own. They had sat where everyone else sat, and now they asked to come back."
- Front `story[4]`: "First came an examined entry." (a nominal chain lifted from analysis prose). Proposed: "First the person's case was examined."
- Front `story[11]` (33 words). Proposed split: "Augustine had often said that even good Christians should not leave this life without repentance. In his last illness he had short psalms of repentance copied out and hung on the wall."
- Front `relations_summary` (36 words, colon question). Proposed: "The two worlds share a province, a century and a body of texts. They answer one question in opposite ways. When a bishop disagrees past repair, does he keep communion, or build a rival hierarchy?"
- Front `story[2]`: "and he wept while they did it" is fine; the 28-word sentence can split after "ordained".
- Brief `formation_strengths[0]`: "has forgotten whose flock it is" is the drafter's paraphrase of the source's "has no Master" (`lpc.force.recurring-contest-failed-member`). Either quote the source's image or keep the plain version: "and a church that takes no one back has turned its back on its own."

### O2

**Optional. Front `documented_stories[2].title`.** "Caring for the People Who Persecute You" implies relief reached persecutors. The story's `absent_detail` says Pontius does not say whether it did. The sermon asked for love and prayer for persecutors; the relief went "to everyone". Proposed title: "Love for Enemies in a Time of Plague".

### O3

**Optional. Brief `formation_strengths[4]`.** "Executed eight years later" traces to the story record's own `modern_contrast`, so the brief is faithful. But no record dates the plague sermon (the force gives only c. 249 to 262). Proposed: "and he was executed a few years later". Flag the story's number to its owner for a dated basis (flag only).

### O4

**Optional. Brief `pairing_guidance`, gallic paragraph.** Folded into the S11 proposal.

### O5

**Optional. Brief `pairing_guidance`, Donatism paragraph.** "Donatism runs to 439 and beyond" blurs the world window (`records/worlds/don.yaml`: 311 to 439) with the later contest. Proposed: "and the Donatism world closes in 439".

### O6

**Optional. Brief `cautions[6]`.** It is correct in substance: Facilitator-only redirect, warm and unconditional, never waiting on the participant saying they are fine, consistent with FG V3.6 ("Surface, hold with genuine warmth, redirect with honesty"). Two additions would close CLAUDE.md's full rule. Proposed sentences to append: "The redirect itself follows the Facilitator's crisis template; this note shapes only its warmth. A participant who finds the road back stern is meeting this world's own otherness, not showing distress, and that alone is never a reason to redirect."

### O7

**Optional. Brief `cautions[7]`.** It is faithful to Phase Six section 3, but "an unseen voice steps in and speaks in his place" could read as the Facilitator speaking *as* Datus. Proposed: "A participant who has leaned on Datus as a named man who answers for them may feel a loss when the Facilitator's own voice steps in. That voice should be present and warm, and should not sound like a system taking over."

### O8

**Optional. Brief `world_identity`.** "Its two great crises were disputes about rites, which were who may give baptism and how the lapsed return." Proposed: "Its two great crises were disputes about rites: who may give baptism, and how the lapsed return."

### O9

**Optional. Front `narrative.questions`, cite support.** All three cites resolve to types the site compiler renders (force, force, doctrinal_witness), and all pass readability.

- F3-P ("Your church used power against Christians who disagreed. Defend that."): `lpc.force.illegal-to-established-shift` supports it. It shows the office changing from no legal standing to asking the state to act against a rival communion. The contested claim would be closer in topic, but it renders only its `claim` side, so the swap was sound.
- F6-I ("What did your people never settle?"): `lpc.force.augustine-engagement-cyprian-conciliar-acts` supports it directly.
- F4-I ("When someone wronged the community, how was it handled, and could they come back?"): `lpc.witness.answerability-as-ground` supports it only at one remove ("the road back ... is what answerability actually looks like"). `lpc.force.recurring-contest-failed-member` (canon cell F4-I, FK 7.7, FRE 61.5) answers "could they come back" head-on. Proposed: swap to it.

### O10

**Optional, flag only. Cited force records.** On the site, a cite renders its record's `description`. The two cited forces carry build narration that participants will then read: "Placing it as an inner force follows a judgement we made earlier" and "We considered whether the shift itself was one of this world's own central concerns" (illegal-to-established); "For that reason it counts as an internal force. This placement was examined and confirmed" (augustine-engagement). This is record-layer hygiene outside this thread's records, so it is flagged, not fixed.

### O11

**Optional. Readability band.** Of 67 prose fields, 43 grade below FK 8. The engine reports these and does not fail them (`regate`: "FK 8 reported"), and CLAUDE.md treats grade 8 as a floor worth staying above, not a target. Completion Standard V1.4's row reads "FK grade 8–10", which differs from the engine. That wording gap belongs to the standard's owner. No field should be rewritten to chase the number; that would be the flattening the NorthStar decision guards against. The commit before this review logs a known `fk.py` syllable defect, which may move these grades.

### O12

**Optional, engine. `gate_referential`.** `_world_front_referenced_ids` walks only `skim`, `orientation` and `narrative`. The brief's top-level units (`world_identity`, `formation_*`, `participant_type_fit`, `pairing_guidance`, `living_tradition_handling`, `redirect_notes`) are never checked, so a mistyped id there would pass. All ids resolve today (checked by hand). This is an engineering item, not this world's.

### O13

**Optional. Brief `formation_limitations`, Article 20.** The items name *whose* voices are missing: ordinary believers, women, the lapsed, rural and Punic or Berber speakers, and the non-literate. They match Doc_02 section 6 and Doc_09 section 7 items 1 to 4. Article 20 also asks *why*. Proposed sentence to add to `formation_limitations[0]`: "What survives is what drew a bishop's attention in a crisis, and that is why it survived." Items [3], [7] and [8] (Donatists, Pelagius, outsiders) are opponents or outsiders, which is Article 23 ground. They are fine as limitations, and the brief rightly never labels them marginalized voices. Keep them that way.

### O14

**Optional. Front `relations_summary`.** "This world formed them in a congregation on a Sunday." No record fixes the day, and Augustine's preaching was not Sunday-only. The records say "week after week". Proposed: "This world formed them in a congregation, week after week."

## The seven checks

**1. Facts trace to the completed world and its Native sources.** They do, apart from the findings above. The claims most at risk were checked against their records: the elections (Pontius section 5; Ep. XXXIX; Possidius IV and VIII), the libelli, "thousands of certificates daily", Celerinus and Lucian, the plague sermon, the hundred thousand sesterces (outcome unknown, as the front says), the 87 bishops of 256 (`lpc.ambient.council-assembly-scale`), the three phases on force, the Maximinus conference, the Vandal crossing of 429, the death on 28 August 430, and the psalms on the wall. **Silence statements:** the tile, `story[12]` and brief `formation_limitations[5]` all carry "no bishop's voice to his own people that can be dated and placed", limited to this world's own record, as Doc_02 section 7 requires. The brief states the class-level exception correctly, as a class and not a list ("The same holds for that whole class of works"). The front states it too broadly (S1). Over-confidence: S4, S5, S6 and S7 above.

**2. Pairings.** All three partner ids exist. The Donatism paragraph carries all three built-in cautions. Ending-not-read-back is stated both ways ("the later story of either must not be used to judge the other"), contemporaries-not-stages is stated, and handoff containment is stated ("Nothing from there may fill this world's silence between 258 and 391"). The ijc and gallic paragraphs do not carry them in full, and none of the three rides its claim through `grounded_in` (S11). No text is lifted from another world (n-gram scan above).

**3. formation_limitations and whose voices are omitted.** Honest and complete against Doc_02 section 6 and Doc_09 section 7 items 1 to 4. The brief names Quartillosa and the Paulinus and Therasia letters, which the front should match (S2). Doc_09 section 7 item 5 (the ordinary pastorate) is correctly *not* claimed as a record absence in the brief. The front's `story[13]` does claim it (S3). Article 20's "why" could be sharper (O13).

**4. living_tradition_handling.** Pass. It reports the world's own record ("Its own record calls the tradition still living, with no single named heir"). It does not assert the census value, and it does not resolve the Article 29 flag against the census `living: false` entry. Datus is kept to 246 to 430 and made unable to judge between modern churches, and the Facilitator names the distance. This is the correct non-deciding form. The census conflict is already recorded in `Step0_Movement_Scope_Confirmation.md` and the build launch prompt, and it belongs there, not in a runtime record.

**5. Safety.** Pass. `cautions[6]`: "Datus never handles real distress. The redirect belongs to the Facilitator alone ... must stay warm and unconditional, and must not wait for the participant to say they are fine." This matches CLAUDE.md, FG V3.6 (the acute-distress posture is "Surface, hold with genuine warmth, redirect with honesty"), world core caution 12, and Phase Six section 3. It also matches the live runtime Phase Six verified (`voice_event = None` on the ACUTE_DISTRESS branch). `redirect_notes` is the thin-record redirect of FG V3.6 "Redirect, never refuse" (name what is held, never invent), not a safety redirect, and it is consistent with that section. Optional closure of the template and otherness points: O6.

**6. Readability and the AI-tells read.** Regate PASS; all 67 fields clear the hard gates (table above). AI-tells: see O1. The cites under the questions support their questions; one could be closer (O9). The rendered cite text carries build narration (O10).

**7. The three judgement calls.**

*7a. `narrative.quiet` = `lpc.limit.the-lapsed-own-account`. Upheld.* It is the world-specific choice. The people the first crisis was about are the one group with no words of their own, which is what this world's formation logic turns on (Doc_09 section 7 item 3). The women's limit is the fleet's common default (alx, don, hal, syr), so here it would say less about this world. The silent-century limit is written so that Datus does not explain the silence, which makes it an awkward thing to feature. The statement is emic, plain, and grades well.

*7b. Omission of `experience_today`. Upheld.* The field is a live claim about the present and needs a `url` and a required `verified_on` (schema comment at `engine/m1/schemas.py`). No lpc record grounds a verified present-day practice or site. Worse, any present-day community named there could read as the "single named heir" the Article 29 statement says does not exist. Fleet precedent: `alx`, `don` and `ijc` also omit it. If it is ever added, it should be a verified place (for example, the excavated site at Hippo) and never a church.

*7c. Phase Six material in two brief items. Upheld as a source, with the fixes above.* The two items are `cautions[1]` (the Facilitator names the silence in its own voice; Phase Six section 2) and `cautions[7]` (the loss when the Facilitator steps in; Phase Six section 3, second caution). A third item, `formation_limitations[6]`, draws on Phase Six section 2's worship bullet. Phase Six is at Approved to proceed, and its audience is the Facilitator. That makes it a proper source for a facilitator-only brief. B-7a names the brief as the home of facilitation guidance, and the same cautions are already in world core caution 12. Using it is sound. Two of the three uses misread it: `cautions[1]` (S10) and `formation_limitations[6]` (B1). `cautions[7]` is faithful; O7 is wording only.

## Truncation check of the two records (two independent methods)

- **Method A, parsed structure.** Both files load through `engine.m1.loader.load_world_records`. All 67 prose fields end in terminal punctuation. A dangling-last-word scan flagged three fields: `participant_type_fit[2]` ("...settle that."), front `story[13]` ("...or pretend to.") and `legacy[1]` ("...siege in 430."). Each was read by hand and each is a complete sentence. None is truncated.
- **Method B, raw bytes.** Front: 332 lines, 22,729 bytes. Brief: 331 lines, 18,911 bytes. Each has exactly two `---` fences and ends with `---` and a newline. `git hash-object` on each working file equals `git rev-parse HEAD:<path>` (07448ead8 and 17ca0bc44), so the files reviewed are the committed files, byte for byte.

## What happens next

The drafter revises B1 and S1 to S11 in place, re-derives the claims-register rows for every reworded claim, reruns `regate lpc`, `claims lpc` and `citations`, and rebuilds the package. Round 2 is a targeted recheck of those fields only, against this file. By the cap, this is round 1 of 3 for these two records.

End of review.
