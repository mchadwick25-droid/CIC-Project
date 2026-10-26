# CO-LPC-3 spoken-field corrections: recheck, round 2

- **Reviewer:** Claude Opus 5.5 (claude-opus-5-5), the whole pass. No other model was used at any point.
- **Date:** 2026-10-24.
- **Authority:** "Cap ruling: lpc CO-LPC-3, a second recheck after its six P1 findings" (System Hub Decision Log). The project lead's two rulings are in the last entry of `lpc_Decision_Log.md`: answerability stays Inferential-Thin with every sentence hedged; G3's Formation test is scoped to disagreement over practice among bishops in communion, and G3 stays Primary.
- **Scope:** the uncommitted diff on top of `b6bc6f88` (54 files), checked against the prior findings in `CO-LPC-3_Spoken_Corrections_Recheck.md` (Part 1 N1–N10, Part 2 N-1–N-12). Round 1 is committed, so the working-tree diff is exactly the round-2 change.
- No repo file was changed except this one.

Abbreviations: ANF05 = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`; POSS = `cic/texts/possidius_vita-augustini_weiskotten1919.txt`; NPNF101 = `cic/texts/npnf101_augustine-confessions-letters.xml`; NPNF214 = `cic/texts/npnf214_seven-ecumenical-councils.xml`.

## Method

- I read every changed line as a word diff.
- I read each cited source line in `cic/texts/` myself.
- I checked every quotation in the changed lines against the vendored text.
- I ran `python -m engine.m10.cli regate lpc`, and I graded every changed record field and every changed Prompt and Capsule paragraph with `engine.m1.gates.grade_text`.
- I ran the six edited generators in a scratch copy of the tree, outside the repo. I compared their output with the working-tree records, field by field after parsing.
- I swept the Prompt, Capsule, World Profile, chunk folders, Docs, `Representative/` and `records/lpc` for each corrected claim. I left out the Phase 5 transcripts, `lpc_Gapped_Formation_Precedent.md`, review artifacts and logs.

## 1. The six prior P1s

| Prior P1 | Status | Check |
|---|---|---|
| Part 1 N1: answerability-as-ground, hedges | **Fixed** | Every sentence that voices the synthesis now carries an emic hedge: "our answer is", "We see", "to us", "As we see it", "In our eyes", "what we take ourselves to be", "As we understand ourselves". The sentences left flat are Documented facts, not the synthesis. One is that a man will be asked what became of his people (Ep. LXVI §4). The others are the two opposite answers on the font, and that Augustine judged Cyprian wrong but never put him outside. "Our own bishops disagree" now scopes the communion sentence. The rating stays Inferential-Thin, as ruled. Readability: positions[0] FK 8.3 / FRE 66.4; positions[1] 7.7 / 70.1; tensions[0] 9.0 / 63.1; text 7.1 / 69.5. |
| Part 1 N2: celerinus story `modern_contrast` | **Fixed** | "gives it in the martyrs' name. Yet his own reply says each case is to be set before the bishop" matches ANF05:30699–30700 ("grant it in my name") and 30730–30731. The claim_guard holds: neither usurper nor hero. FK 8.4 / FRE 64.1. |
| Part 1 N3: celerinus story `text` paragraph 3 | **Fixed** | "He asked that the two women have peace, 'the case being set forth before the bishop, and confession being made.'" The quotation is word for word (ANF05:30730–30731). "These" in "not only these may have peace" follows straight after Numeria and Candida, so the reading is fair. A new claim_guard forbids telling the grant without the condition. The story chunk `lpcstory005` carries the same sentence. |
| Part 1 / Part 2 N-3: road-back quotation | **Fixed** | "'such a one with his friends'" is word for word (ANF05:29941–29942, "Such a one with his friends;"). The body note is updated. |
| Part 2 N-1: Doc_04 G3 Formation, and Capsule :19 | **Fixed in Doc_04; new problem in the Capsule** | See the judgement below, and R2-1. |
| Part 2 N-2: Prompt "held whole" and unscoped "never separate" | **Fixed** | Prompt :29 now reads "The one episcopate is undivided. Each bishop holds his part of it for the whole", which is true to De Unitate 5 (ANF05:42290). "Disagreement with a colleague" scopes the rule, and the next sentences set its limit at the 418 condemnation. Chunk `lpclex014` (Quick Meaning and World Hearing), World Profile :534 and Capsule :61 are aligned. |

**Doc_04 G3 and the 418 anathema.** The Formation entry now says "Passes, within a stated scope". It names the counter-instance (NPNF214:36418–36445, canon CIX, "Synod against the heresy of Pelagius and Celestius"). It says why the anathema falls outside the scope: a council judged a teaching heresy, which is not a disagreement over practice between bishops in communion. It also says why G3 stays Primary: its other tests rest on rebaptism and the Donatist schism. This is honest, not special pleading. The limit is stated openly, in the test where it bites, and is not hidden or redefined away. The gravity record, the World Profile and the Prompt now carry the same scope. It would be stronger still if it cited the distinction Augustine himself draws: Cyprian's view came before a plenary council had settled the question. That is advisory only. The summary table at Doc_04 :160 still says "Passes all six" with no scope (R2-3).

## 2. The Permanent Prompt and the World Capsule Core

I read every changed line. Each one is a clear instruction, and each matches the corrected records.

- **Prompt :19, :29, :37, :63** ("nearly a century and a half"): correct for 256 to c. 400.
- **Prompt :21** ("pastoral voice"; "as your own later account gives them"): no wider than the honest_limit and C-11 records.
- **Prompt :29:** see N-2 above. "Teaching your councils judged false was another matter: in your later years, African councils condemned what the Pelagians taught" is true at source (NPNF214, canon CIX) and forbids nothing Documented. "You hold your rule against separation knowing, from your own record, what it costs when it breaks" adds no new fact.
- **Prompt :31** ("baptize the person in the church, for the first time"): true to Cyprian's own view that the first washing was no baptism.
- **Prompt :35:** the confessors' claim to "ask peace" matches the corrected confessor-claim record.
- **Prompt :41, :59** ("Where he is a colleague", "between colleagues"): correctly scoped.
- **Capsule :11, :21, :31, :61, :63, :69, :81:** aligned with the records, with no added claim.
- **Capsule :19:** carries a new problem. See R2-1.
- **Readability.** These are governing texts, not spoken fields, so I report and do not fail them. Prompt :29 improved from FK 10.6 / FRE 56.7 to 9.4 / 59.3. Capsule :63 improved from 12.0 / 57.2 to 8.1 / 72.3. Capsule :81 slipped from 10.9 / 57.1 to 11.3 / 54.8 when "among colleagues" was added. That is advisory.

## 3. The sweep and the deliberate non-changes

**The people's part in receiving the penitent back.** This covers "received at the end by the very people who watched the failure" in Capsule :17 and :59, Prompt :27, road-back turn 1, `term.reconciliation`, `lpclex003` and `lpcctx004`. **Accepted.** Ep. LIV §15 (ANF05:35073–35081) has Cyprian persuading the people to "consent to receive" the returning, and the people murmuring when unfit men come back. Ep. IX (ANF05:29826–29827) has the lapsed "plead their cause both before me and before the confessors themselves and before the whole people". The people's part is attested. The bishop's laying-on of hands is not denied anywhere. Citing Ep. IX beside Ep. LIV §15 would be stronger. That is advisory.

**Prompt :19, "a century and a third later".** **Accepted.** Here the measure is from the end of Cyprian's tenure (258) to Augustine's own office (presbyter 391, bishop 395). That is 133 to 137 years, and it matches world_core's "133 years from 258 to 391". It measures a different interval from the font answers. Capsule :11 ("two cities a century and a third apart") is the same case.

**world_core formation_logic, "a boundary that disagreement does not breach".** **Not accepted. P2 (R2-4).** `formation_logic` is a voice-diet field (`engine/m1/spoken_fields.py`), so this text reaches the voice. Two paragraphs later the record says "communion among bishops, kept whole when they disagree", which is scoped. The summary sentence, though, is the unscoped C-27 claim that the project lead's ruling narrowed. The fix is four words.

**"across a century" (Doc_06 :59; sesterces chunk :29).** **Accepted.** These are construction prose, not voice, and the gap is more than a century.

**Sweep results.** The Prompt, the Capsule and `records/lpc` are clean of every corrected claim, apart from R2-1 and the two record items in R2-4 and R2-10. The World Profile, the chunks and the Docs still carry several corrected claims (R2-6 to R2-11). None of these sites is voice material that the engine reads. `engine/m2/profile.py` builds the profile from records, not from these files. So they are P2. But the ruling ordered a sweep of the World Profile and chunks, and that sweep is incomplete.

## 4. P2s from the prior round

| Prior P2 | Status |
|---|---|
| N4 Lucian bridge_line and dates.display | Applied. FK 6.1 / FRE 75.3. |
| N5 certificates, Ep. XVI condition | Applied in divergence_note and senses.evidential. "we have granted peace" and "in your estimation" are word for word (ANF05:30385–30387). |
| N6 only-son locus and body note | Applied. Both quotations are at POSS:2942–2950. |
| N7 Augustine bridge_line | Applied. It matches POSS:1813–1815 ("brought him to the bishop to be ordained"). |
| N8 marriage tensions[0] | Applied. FK 7.4 / FRE 65.3. |
| N9 grant-me-chastity | Applied. |
| N10 heresy "a century and a half" | Applied. |
| N-4 World Profile :392 | Applied. "whether in books, letters, or treatises" renders Knoll's "siue in libris siue in epistulis siue in tractatibus" (Retr. Prologus). |
| N-5 "water again" | Applied at every site. None remain. |
| N-6 "a century and a third" for the font answers | Applied at every listed site, and swept into Doc_05, the Rep phases, `lpclex006` and the World Profile. |
| N-7 Prompt :21 and Doc_02 §7 | Applied. |
| N-8 Prompt :41 | Applied. |
| **N-9 Caution 2** | **Not applied, and not recorded as deferred** (R2-5). |
| N-10 force locus | Applied. "acquainted with the Punic language" is at NPNF101:54466–54467. |
| N-11 Doc_02 / Doc_04 | Applied. The Doc_02 :49 replacement now reads wrongly (R2-2). |
| N-12 s28 docstring | Applied. |

**Other edits found by the sweep, checked:**
- `lpclex001`, `004`, `005`, `006`, `008`, `011`, `012`, `013`, `015`, `016`, `017`, `018` and `019` are aligned with their corrected records.
- In `lpclex013`, "when experience brings to light what was hidden" fits On Baptism II.3.4.
- In `lpclex012`, "answers for it to Christ" fits the 256 preface.
- `lpcstory003`, `004` and `007` are fine. `007` ("taught that even good Christians must repent before death") matches POSS:4917–4920.
- `lpcstory005` ("tells Lucian of his own confession") matches ANF05:30553–30559 ("when I also was in such a purple confession").
- Doc_03, Doc_05, Doc_07, Doc_09 and the Rep Phase 1–4 and 7 edits are correct.
- The "thousands of certificates" wording in `lpclex019` is Cyprian's own sentence in ANF (ANF05:30204), so it is not a leftover.

## 5. Spoken fields

- `regate lpc`: **PASS**. 162 public-facing fields, 94 new or edited since base, no regression.
- Every changed spoken field scores FK ≤ 9.0 and FRE ≥ 63.1. The lowest are answerability tensions[0] (9.0 / 63.1) and the celerinus `modern_contrast` (8.4 / 64.1).
- Lucian `dates.display` (FRE 40.1) is not a graded field. It was already failing at base, and it improved.
- Every quotation in the changed lines is word for word against the vendored text.
- No AI tells. The answerability record now hedges in four sentences out of four in positions[1]. It reads as the world's own way of owning a reading, not as assistant filler, but it sits at the edge. Advisory only.

## 6. Generators

I ran `wb_lpc_s21`, `s22`, `s24`, `s25`, `s27` and `s28` in a scratch copy. All 16 changed records match the generator output field for field, `canon_cells` aside, and every body matches. The generators emit the corrected text.

Pre-existing drift, outside this round: `wb_lpc_s2z_canon_closure.py:541` still emits an old `lpc.limit.apostolic-origin-undefended` statement, "Each bishop holds the whole of it, not a share". It was not edited here, and its text was already out of step with the record before CO-LPC-3. It should be realigned or marked superseded. That is advisory.

## New findings

**R2-1 · P1 · Capsule :19: a contested point stated as settled, in voice-governing text.**
- The sentence: "Rebaptism, the sharpest such disagreement, tested it, and it held."
- The problem: the rule is now scoped to "bishops in your own communion". Within that communion, the world's own Cyprian dossier holds Firmilian's charge against Stephen of Rome. It says Stephen received the African bishops sent as envoys "not … even to the speech of an ordinary conference", and that "not only peace and communion, but also a shelter and entertainment, were denied to them" (ANF05:40044–40054; also 40019–40022, "you cut yourself off from so many flocks"). The original terms review made `term.communion` P1 on this same evidence.
- "It held" is true of this world's own bishops: Cyprian did not break with Stephen, and Augustine did not put Cyprian outside. It is not established for the communion as a whole.
- The wording came from the round-1 recheck's own proposal. The drafter applied it as given.
- Proposed Capsule :19, the sentence replaced: "Rebaptism, the sharpest such disagreement, tested it, and your own bishops kept it."

**R2-2 · P2 · Doc_02 :49 (Augustine's Transmission History): the N-11 replacement reads wrongly in this place.**
- It now reads "as the literature of the side that became canonical, which kept Cyprian even where it judged him wrong, on rebaptism (Donatism, Manichaeism, Pelagianism)". The list of Augustine's three controversies now seems to gloss "rebaptism", and a clause about Cyprian sits in Augustine's entry.
- Proposed: "as the literature of the side that became canonical in the three controversies he engaged (Donatism, Manichaeism, Pelagianism) — the same tradition that kept Cyprian even where it judged him wrong, on rebaptism —"

**R2-3 · P2 · Doc_04 :160 summary table: G3 still "Passes all six" with no scope.**
- Proposed cell: "Passes all six (Formation within a stated scope: disagreement over practice among bishops in communion; the 418 anathema falls outside it)".

**R2-4 · P2 · "a boundary that disagreement does not breach", unscoped, in a voice-diet field.**
- Sites: `records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.md` :128 (formation_logic), its generator `wb_lpc_s21.py`, Doc_07 :162, and Rep Phase 7 :44 (a quotation of Doc_07, which follows it).
- Proposed: "And there is a boundary that disagreement among bishops in communion does not breach."

**R2-5 · P2 · Prior N-9 (Caution 2) neither applied nor tracked.**
- `world_core` cautions :272–274 still say "Never describe the church's history of those years from this world's own collection". That also bars Augustine's own later view of those years, such as `lpc.witness.constantine-did-not-corrupt`.
- Proposed: apply the N-9 text ("…from this world's own collection, except as Augustine's own later view, given as his and dated to when he wrote it."), in the record and in `wb_lpc_s21.py`. If the drafter judged this not plain, enter it in `Open_Gaps_Tracking.md` instead.

**R2-6 · P2 · Preaching "weekly / to the baptized" and the invented "bury" (term.preaching and term.the-flock P1s) remain outside the records.**
- World Profile :172. Replace "come every week since to be preached at by the same voice that will bury them" with "come again and again since to be preached at by the same voice".
- Doc_05 :352. Replace "after that you come every week and are preached at by the same voice that will bury you" with "after that you come again and again and are preached at by the same voice".
- `lpclex001` :35. Replace "The weekly preaching exists" with "The regular preaching exists".
- `lpclex009` :18. Replace "the weekly address to the baptized" with "the regular address to the gathered church".
- `lpclex008` :12 (aliases) and `Lexicon_Deployment_Index.md` :21. Replace "the weekly address" with "the regular address".
- `lpclex008` :39. Replace "weekly, in person" with "again and again, in person".
- World Profile :176 and :200, Doc_05 :167, Doc_07 :46, Rep Phase 2 :16 and Rep Phase 4 :37. Replace "weekly preaching" with "regular preaching".
- Doc_05 :263. Replace "the weekly sermon to the baptized" with "the regular sermon to the gathered church".
- Rep Phase 4 :58. Replace "The weekly return to preaching" with "The regular return to preaching".

**R2-7 · P2 · Communion "survives sharp disagreement", stated flat (the term.communion P1).**
- Doc_03 :54. Replace "treated in this world's own corpus as a status that survives sharp disagreement" with "a status Cyprian held should survive sharp disagreement".
- Doc_05 :114. Replace "and it survives sharp disagreement between those who hold it (**G3**)" with "and Cyprian held that it should survive sharp disagreement between those who hold it (**G3**)".
- Rep Phase 3 :35. Replace "that survives sharp disagreement" with "that Cyprian held should survive sharp disagreement".

**R2-8 · P2 · Doc_06 :75 keeps the certificates P1 wording.**
- Replace "The written request a confessor sends the bishop asking that a named lapsed person be received back" with "A confessor's letter for a lapsed person, which asks for peace or says it is granted".

**R2-9 · P2 · "silence in its own record" (C-6) in three Docs.**
- Doc_08 :23 and Doc_09 :23. Replace "a 133-year silence in its own record" with "a 133-year silence in its own pastoral voice".
- Doc_01 :173. Replace "a silence in this world's own record" with "a silence in this world's own pastoral voice".
- Also: World Profile :26 (Temporal scope) now says "congregational voice" where every other site says "pastoral voice". Align the wording.

**R2-10 · P2 · `lpc.witness.apostolic-succession-of-bishops` retrieval `prefer_instead` :48 keeps "each bishop holds the whole office, not a share" (the-one-episcopate P1).**
- Proposed: "participant wants the one-episcopate's own doctrine that the episcopate is one, each part of it held by each bishop for the whole -- that is Cyprian's own ecclesiology…". Carry the same change into its generator, if a current one emits it.

**R2-11 · P2 · World Profile :544 keeps "characteristically over his own reluctance" (term.suffrage P2).**
- Replace "characteristically" with "sometimes".

### Advisory (not counted)
- Ground the G3 scope in Augustine's own line between a question before and after a plenary council (On Baptism II.4).
- Cite Ep. IX (ANF05:29826–29827) beside Ep. LIV §15 for the people's part in reception.
- Capsule :81 readability slipped (FK 11.3 / FRE 54.8).
- The `wb_lpc_s2z` drift (section 6).
- The round-1 advisories on the sesterces `retrieve_when` and confessor-claim `citation_specificity` are still open.
- "A century and a third later, the emperors could be asked" (Doc_08 :179, `lpc.force.illegal-to-established-shift` :42, `wb_lpc_s25.py`, World Profile :378, Rep Phase 4 :100) measures a different interval, 258 to c. 400. "Nearly a century and a half" would be closer.

## Counts

- **Prior P1s: 6.**
  - Fixed: 6.
  - New problem from a fix: 1. The N-1 Capsule wording brought R2-1.
- **Prior P2s: 16** (Part 1 N4–N10, Part 2 N-4–N-12).
  - Applied: 15.
  - Not applied: 1 (N-9).
  - One applied fix reads wrongly in its new place (N-11 → R2-2).
- **Deliberate non-changes judged: 4.**
  - Accepted: 3 (the people's part in reception, Prompt :19, "across a century").
  - Not accepted: 1 (formation_logic, R2-4).
- **New findings: P0 0, P1 1 (R2-1), P2 10 (R2-2 to R2-11).**
- Readability: regate PASS. Every changed spoken field passes.
- Quotations: all word for word.
- Generators: all 16 changed records reproduce.

VERDICT: Substantial revision required
