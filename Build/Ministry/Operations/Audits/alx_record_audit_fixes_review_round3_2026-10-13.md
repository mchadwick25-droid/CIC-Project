Review round 3, alx record audit fixes (use_note.means pass), 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS (no blocking findings; 5 non-blocking findings)

Scope: commit 323b616 (HEAD), 13 files under records/alx. It changes `use_note.means` on alx.dw.resurrection and on the terms arete, baptism, christ, fall-descent, hamartia, incarnation, logikos, metanoia, oikos, prayer, salvation and thanatos. It also changes alx.term.arete `false_friend[0]` and alx.term.hamartia `world_word`. Each new `means` was compared with the record's current plain_meaning, quick_meaning, senses and text, with its cited sources, and with alx.contested.origen-positions and alx.contested.ecology-wide-primacy. Every changed `means` was graded with `engine.m1.gates.grade_text`. All pass FK <= 10 and FRE >= 60. The lowest FRE is 60.19 (alx.dw.resurrection) and the highest FK is 9.995 (alx.term.thanatos). Each is one sentence. No `not_for`, `years`, `status`, `confidence`, `sources` or other field changed, and every file parses as YAML. Twenty unchanged records were spot-checked for a contradiction the editors missed (listed at the end). Facts were checked by grep against cic/texts/ (anf02 Clement, npnf204 Athanasius). The editors' logs (log_usenote_term.md, log_usenote_other.md) and brief were read for intent.

## Findings

1. **alx.term.fall-descent, use_note.means**
   - Old: `The world's fallenness is confessed by all, while Origen's pre-cosmic descent of souls is a disputed speculation held open.`
   - New: `We confessed that people had fallen, but it stayed open whether Origen taught a fall before the world.`
   - Source: the record's own plain_meaning ("Whether he taught it as his own view is disputed") and evidential sense ("Origen's own De Principiis carries the pre-cosmic account; whether he held it as his considered position or it reflects a later systematization ... is a genuinely disputed question"). alx.contested.origen-positions frames the contest as whether he taught these positions "as settled doctrine".
   - NON-BLOCKING. The new text drops "as his own view". It now doubts whether Origen taught the account at all, which is wider than the record's contest, since his own surviving book carries it. "Before the world" also reads less clearly than the field's "before the world began".
   - Proposed: `We confessed that people had fallen, but it stayed open whether Origen taught a fall before the world as his own view.` (FK 9.6, FRE 65.3)

2. **alx.term.arete, false_friend[0]**
   - Old: `excellence built through repeated practice, as in Aristotle`
   - New: `excellence that practice alone produces, as in Aristotle`
   - Source: Aristotle is not cited by the record and is not vendored in cic/texts/. In Nicomachean Ethics II.1 (1103a23-26) the virtues arise "neither by nature nor contrary to nature", but "we are adapted by nature to receive them, and are made perfect by habit". In VI.13 virtue of character needs practical wisdom. Aristotle did not hold that practice alone produces virtue. `false_friend` reaches the voice through engine/m4/term_glosses.py.
   - NON-BLOCKING. Adding "alone" fixes the conflict with the corrected plain_meaning, which round 1 asked for. But it pins on Aristotle a view he did not hold. The Aristotle contrast stays in `retrieve_when`, `not_for` and senses.translational, so the attribution can be dropped from the false friend without loss.
   - Proposed: `excellence that practice alone produces` (too short for the grader to score, so it was judged by reading)

3. **alx.term.agape, use_note.means (unchanged; missed contradiction)**
   - Current: `Agape meant love as the visible fruit of a soul genuinely reordered toward God and others by formation, not a feeling or an act of will.`
   - Source: the corrected senses.personal ("In the other, the act came from will alone, and we did not call it love"). Also Stromateis VI.9, inside the record's cited locus (anf02 l.47059-47061): the gnostic "associates through love with the Beloved One, to whom he is allied by free choice, and by the habit which results from training". This is the same defect the pass corrected in arete (training and will "had their part").
   - NON-BLOCKING. "Not ... an act of will" denies the will any part. Both the corrected personal sense and the cited Clement give it a part. The current field also fails the grader (FK 12.3, FRE 53.5).
   - Proposed: `Agape meant love as the fruit of a soul turned toward God and others by formation, not a feeling or an act of will alone.` (FK 9.7, FRE 69.8)

4. **alx.term.eucharistia, use_note.means (unchanged; missed claim stronger than the evidence)**
   - Current: `Eucharistia was the thanksgiving, the shared meal of bread and cup at the center of worship, forming members whether or not they could read.`
   - Source: the cited loci, Paedagogus I.6 and II.2, say nothing about literacy. alx.contested.ecology-wide-primacy `means` says formation of "the non-literate Coptic majority, is contested and confirmed only for the literate ecology". The same pass made alx.term.oikos translational say "How far it reached those who could not read is not attested". The record's corrected senses.personal claims access, not effect: "Whatever else a member could not read or argue, this was theirs".
   - NON-BLOCKING. "Forming members whether or not they could read" asserts the formation of non-readers as settled, which the world's own contested record holds open. The current field also fails the grader (FK 11.0, FRE 59.1).
   - Proposed: `Eucharistia was the thanksgiving, the meal of bread and cup at the heart of worship, open to members whether or not they could read.` (FK 10.0, FRE 66.2)

5. **Package not rebuilt after this commit (process, not wording)**
   - The newest package, packages/alx/2026-10-13T19-06-19Z, predates 323b616. It still carries the old `means` text, for example "fearless deaths" (alx.dw.resurrection), "priest, king, and prophet in one person" (alx.term.christ) and "hamartia (missing the mark)" (alx.term.hamartia, including compiled/chunks/lexicon). The live engine loads packages (engine/m4/world_loader.py), so the corrected `means` does not reach the voice until a rebuild.
   - NON-BLOCKING. Under CLAUDE.md's default actions, a package rebuild after a records/ edit is "just do it". Rebuild after findings 1-4 are applied, so that one rebuild carries everything.

## Found sound

- **Changed `means` fields (scope of 323b616):**
  - alx.dw.resurrection: the invented "fearless deaths" is gone. The text says the disciples "taught it with courage" in danger, and Athanasius's martyrs met death "without fear". The new sentence leans on the body text before it in the evidence block (engine/m2/builders.py l.263), since it does not name the resurrection itself. That is "could be stronger", not a defect.
  - arete: agrees with quick_meaning word for word and with plain_meaning ("training and the exercise of will had a part").
  - baptism: matches plain_meaning and quick_meaning ("into the new life"). The unsourced "Christ's death and rising" is gone.
  - christ: matches plain_meaning ("sent by God"). The priest-king-prophet formula, not in the cited loci, is gone. The present tense "is" is correct for who Christ is.
  - hamartia: matches plain_meaning ("more a wound than only a debt owed or a law broken"). The `world_word` change to bare "hamartia" removes the gloss the pass took out of plain_meaning. It matches other unglossed labels (arete, metanoia, logikos, oikos), and the field stays one word, as gates expect.
  - incarnation: "not to teach or model" is gone, and the field now agrees with translational ("not only to teach it from outside"). "So that we might be made God" is De Incarnatione 54, inside the cited locus. The `not_for` ("reading made God as becoming a god") still guards it.
  - logikos: keeps both Contested halves (the wider view, and whether it was Origen's own). It no longer states the cosmology as his.
  - metanoia: "change of mind" matches plain_meaning. "Not just feeling sorry" matches quick_meaning and translational ("the feeling can accompany").
  - oikos: the unsupported "where most people were formed" is gone, in line with alx.contested.ecology-wide-primacy. "Put to the test" matches senses.personal ("where that claim was tested").
  - prayer: matches plain_meaning. Stromateis VII.7 and VII.12 ("converse with God", silent prayer).
  - salvation: "and not only a not-guilty verdict" matches plain_meaning and quick_meaning. The Logos healing "from within" is the De Incarnatione account in the record's cited source.
  - thanatos: matches plain_meaning and quick_meaning, and the De Incarnatione 4-6 order (loss of the knowledge of God, completed in bodily death).
  - Tense: past for the community's beliefs throughout, present only for Christ's identity and for the present-day scholarly dispute in logikos. No hedge, contested qualifier or limit was lost except in finding 1. No new claim was added.
- **Unchanged `means`, spot-checked with no contradiction found (18):**
  - allegoria ("contested within Egypt itself" matches `not_for` and HE VII.24).
  - anastasis ("in Athanasius's account" keeps the Clement exclusion).
  - apokatastasis ("offered as inquiry whose dogmatic weight cannot be fixed" matches plain_meaning).
  - ekklesia.
  - homoousios ("contested in its own century as unscriptural": De Decretis 19-21).
  - martys (Strom. IV.4).
  - methexis and photismos.
  - son-of-god (bounded to "Nicaea's claim").
  - theosis ("the creature stays a creature").
  - eikon, nous, psyche, restoration and sophia.
  - alx.dw.original-sin ("ratified by each soul" matches "signs onto in its own living"; "without speaking of guilt at birth" kept).
  - alx.dw.was-jesus-god: "fenced that worship rather than voting in a new God" is the world's own position, not the removed attribution to Athanasius. Its substance is in De Decretis 25 (npnf204 l.28365-28367: "they did not invent them for themselves ... but spoke what they had received from their predecessors"), just outside the cited locus 19-21.
  - alx.dw.church-failure (matches the three failures the text names).
- **Observed, outside this commit:**
  - alx.term.methexis plain_meaning and means say "Not by becoming God". alx.term.incarnation means and alx.term.theosis plain_meaning quote "that we might be made God". The two are reconciled only through `not_for` ("reading made God as becoming a god"). This is consistent within each record, but a participant may hear both. Mark may want it in Open_Gaps_Tracking.
  - alx.term.baptism `not_for` ("saying the baptized come up from the water already fully formed") sits uneasily with the corrected senses.personal (Paed. I.6, "nothing was lacking to that faith"). `not_for` is outside this pass.
  - alx.term.apokatastasis carries formation_confidence "Widely Accepted" while every spoken field states it as contested. That is a build field and outside this pass.
