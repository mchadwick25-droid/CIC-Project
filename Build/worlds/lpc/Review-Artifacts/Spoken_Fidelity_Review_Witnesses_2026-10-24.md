# Source-fidelity review: lpc, spoken fields, batch A

Reviewer: Claude Opus 5.5 (claude-opus-5-5), independent review. Date: 2026-10-24.
Scope: the 45 fields listed in `spoken_A.txt`, across 18 `records/lpc/doctrinal_witness/` records. No repo file was changed.

Method: I read every sentence of every field in scope. I checked each one against the record's own `sources[].locus`, reading the cited lines in `cic/texts/` myself. Where a claim was true but its support lay outside the cited locus, I name the vendored file and line. I scored every proposed text with the project's own scorer (`engine.m1.gates.grade_text`), applying all of a field's proposed edits together. Every proposal lands at FK 10 or below and FRE 60 or above. The one exception is a field that already failed before any edit; for that field (communion-over-separation `text`) I give a full rewrite that passes.

File abbreviations:
- `anf05` = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`
- `npnf101` = `cic/texts/npnf101_augustine-confessions-letters.xml`
- `npnf102` = `cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml`
- `npnf103` = `cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml`
- `npnf104` = `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`
- `npnf107` = `cic/texts/npnf107_augustine-homilies-john-soliloquies.xml`
- `poss` = `cic/texts/possidius_vita-augustini_weiskotten1919.txt`

---

## 1. lpc.witness.almsgiving-quenches-sin

**A1. text. P1 (unsupported claim).**
- Sentence: "We did not teach that wealth itself was shameful. We taught what it was for."
- Problem: no cited passage says this, and the treatise leans the other way. Cyprian quotes "Sell your goods, and give alms" and "If thou wilt be perfect, go and sell that thou hast" (§7). He also quotes 1 Tim 6, "they who will be rich fall into temptation and a snare" (§10). Saying "we did not teach that wealth was shameful" puts a reassuring claim in the world's mouth that the source does not make.
- Evidence: anf05:47510 (§7, "Sell ... your goods"); anf05 §10 (1 Tim vi. 7–10); anf05:47689 (§13, "Divide your returns with the Lord your God; share your gains with Christ").
- Proposed: "He told them plainly what it was for. They were to share their gains with Christ and with the poor."

**A2. text. P2 (loose paraphrase).**
- Sentence: "Cyprian wrote a whole treatise addressed to believers who had money."
- Problem: the treatise is addressed to "beloved brethren" as a whole (§1). Only from §9 onward does it turn to people who have estates.
- Evidence: anf05:47316 (§1 opening); §§9–14 (anf05 ~47560–47710).
- Proposed: "Cyprian wrote a whole treatise on almsgiving, and much of it speaks to believers who had money."

**A3. text and positions[0]. P2 (loose paraphrase).**
- Sentences: text: "He pictured at least one of them directly as 'a wealthy and rich matron in Christ's Church.'" positions[0]: "He pictured at least one of them directly, as ..."
- Problem: Cyprian addresses a type in the second person ("And you who are a wealthy and rich matron..."). "At least one of them" suggests a real, particular woman, which the text does not say. The quotation itself is word for word. Note that a footnote there says some manuscripts omit "in Christ's Church".
- Evidence: anf05:47709–47711.
- Proposed (both fields): "He even spoke straight to one kind of member, \"a wealthy and rich matron in Christ's Church.\""

**A4. text. P2 (slightly wider than source).**
- Sentence: "...he was refusing the one remedy left to him."
- Problem: Cyprian calls the remedy "works of justice and mercy". He also says prayers and fasting avail less without almsgiving, but he does not make almsgiving the only remedy left. The nearest wording, "God can be appeased by almsgiving alone", glosses one Isaiah passage.
- Evidence: anf05:47316ff (§1), anf05:47417 (§4), anf05:47463 (§5).
- Proposed: "...he was refusing the remedy God had given for sin after baptism."

Readability with all edits: text FK 6.8 / FRE 70.1; positions[0] FK 4.5 / FRE 82.6.

## 2. lpc.witness.answerability-as-ground

**B1. text. P1 (a contested point stated as settled, and contrary to the source).**
- Sentence: "We have answered the font question itself twice, oppositely, and we hold both answers rather than choose between them."
- Problem: the later voice did choose. Augustine judged Cyprian's reasons "truth-like rather than true". He held that "a plenary Council has confirmed" the custom against rebaptism, and he set "the holy Catholic Church" against Cyprian's view. What he did not do was put Cyprian outside the Church's unity. Saying that "we hold both answers" misstates the source.
- Evidence: npnf104:12157, 12168, 12997.
- Proposed: "We have answered the font question twice, in opposite ways. Our later bishop judged the earlier answer wrong. But he never put the man who gave it outside our communion."

**B2. text. P1 (misattribution: one bishop's view put in the collective "we").**
- Sentence: "The font is never a small question ... because whether the water we give is really given rests on whether we can be trusted with what was placed in our care."
- Problem: this is Cyprian's position, that baptism given outside the Church is no baptism. Augustine, the world's second voice, explicitly denied it. For him, Christ's baptism "is necessarily holy, however polluted and unclean its ministers may be". Putting the claim in the "we" erases the world's own central disagreement.
- Evidence: npnf104:11733; npnf104:12718.
- Proposed: "The font is never a small question, however plainly someone asks about it." (Cut the "because" clause. B1 then follows and gives the disagreement honestly.)

**B3. text, positions[0], positions[1]. P2 (missing locus; synthesis presented flat).**
- Sentences: "That is the one fact everything else grows out of", "Everything else we hold grows out of that one root", "A council without it would be an argument no one is actually responsible for", and similar.
- Problem: none of the three sources has a file or line locus. The record's own `divergence_note` says this unity reading is "this build's own synthetic judgment ... not an independently-attested claim". Yet the fields state it as the world's settled self-understanding, under `formation_confidence: Documented`. The core image is supportable, so give it loci. The "one root" framing should be read as the world's emphasis, not as a documented doctrine.
- Evidence that can be cited: anf05:37345–37360 (Ep. LXVI, quoting Ezek 34, "I will require my flock at their hands", and Cyprian's application to bishops); anf05:43727 (On the Lapsed, "it is the shepherd that is chiefly wounded in the wound of his flock").
- Proposed: add these loci to `sources[]`. In positions[0], soften "That is the one fact everything else grows out of" to: "We see everything else growing out of that one fact." No other text change.
- Record-level note (outside field scope): `formation_confidence: Documented` sits badly with a `divergence_note` that calls the claim synthetic.

Readability with B1 and B2: text FK 8.0 / FRE 65.3.

## 3. lpc.witness.apostolic-succession-of-bishops

**C1. text and positions[0]. P2 (attribution looser than the source).**
- Sentences: "Augustine did it most directly." / "Augustine wrote against a Donatist presbyter..."
- Problem: Letter LIII is sent jointly by "Fortunatus, Alypius, and Augustin".
- Evidence: npnf101:29650–29652.
- Proposed: text: "Augustine, writing with two fellow bishops, did it most directly." positions[0]: "Augustine and two fellow bishops wrote against a Donatist presbyter..."

**C2. text. P2 (loose paraphrase of a list).**
- Sentence: "He counted back from the present bishop of Rome, Anastasius, through Damasus, Liberius, Julius, and so on."
- Problem: Anastasius's own predecessor in the list is Siricius, and Marcus stands between Julius and Sylvester. Going "through Damasus" straight from Anastasius skips the immediate predecessor. Note too that the letter lists the names forward from Linus, after saying "we reckon back till we reach Peter".
- Evidence: npnf101:29697–29707.
- Proposed: "He counted back from the present bishop of Rome, Anastasius, through Siricius, Damasus, Liberius, and on down the list."

Checked and sound: "Linus, Peter's own successor" ("The successor of Peter was Linus", npnf101:29701). "In this order of succession no Donatist bishop is found" is word for word. The Petilian chairs, with "fills to-day" for Rome and "sits today" for Jerusalem, match npnf104:16912. Both Cyprian quotations match anf05:31259 and anf05:37558. The earlier invented detail ("named by Peter himself") is gone.

Readability: text FK 7.9 / FRE 60.1; positions[0] FK 8.7 / FRE 60.4. Both are thin margins.

## 4. lpc.witness.baptism-traced-to-the-apostles

**D1. text and positions[0]. P2 (framing at odds with the source).**
- Sentences: "...to the apostles by name, not only from a general belief." / "...by name, not just by general conviction."
- Problem: Augustine names no apostle. His ground is exactly a belief drawn from custom ("rightly believed", "rightly held"). The record's own tension says so. "By name ... not ... general belief" points the listener the wrong way.
- Evidence: npnf104:12163–12164; npnf104:12631.
- Proposed: positions[0]: "Augustine says plainly that two of our practices came down from the apostles." text: "Augustine traced two of our practices back to the apostles in plain words."

Checked and sound: both quotations are word for word, and the infant-baptism context is confirmed (npnf104:12622).

## 5. lpc.witness.blamed-for-the-worlds-troubles

**E1. text and positions[0]. P2 (missing locus for a true claim).**
- Sentence: "A Roman official named Demetrianus..."
- Problem: in the cited lines, Demetrianus's office comes only from the modern editor's Argument ("the Proconsul of Africa"). That identification is not Cyprian's. Cyprian's own text shows him judging and torturing Christians, which supports "official", but only in §§12–13, outside the cited §§1–3.
- Evidence: anf05:45610 (editor's Argument); anf05 §§12–13 (~45960–45975, "You set on foot tedious tortures").
- Proposed: no text change. Add the §§12–13 lines to the locus.

Checked and sound: "many around him believed the same thing" matches "very many are complaining" (anf05 §2). The charge matches §3.

## 6. lpc.witness.communion-over-separation

**F1. positions[1]. P1 (misattribution, and a loose paraphrase of a formula).**
- Sentence: "Underneath the disagreement sits a belief neither of us ever gave up: the one episcopate is undivided, held whole by each bishop rather than parceled out between colleagues."
- Problem: "neither of us" assigns Cyprian's De Unitate formula to Augustine as well. No cited source shows that. The formula itself reads "The episcopate is one, each part of which is held by each one for the whole", which is not "held whole by each bishop". The record also gives no locus.
- Evidence: anf05:42290–42291.
- Proposed: "Underneath the disagreement sits a belief our earlier bishop wrote down plainly. \"The episcopate is one, each part of which is held by each one for the whole.\" For him, that is why a bishop could differ from a colleague without breaking communion." (FK 7.3 / FRE 68.3)

**F2. text and positions[0]. P2 (overstatement; a causal synthesis stated as fact).**
- Sentences: "separating over a disagreement is the one thing our own life has organized itself never to repeat, because we have already watched what that costs" / "...the one thing we have organized our whole life never to do again" / "We hold our rule against separation because we already know..."
- Problem: "the one thing ... our whole life" is hyperbole. The causal link to Felicissimus and Novatian is Doc_07's synthesis, which the record's own `divergence_note` discloses. The primary text gives a plainer rule: "judging no man, nor rejecting any one from the right of communion, if he should think differently from us".
- Evidence: anf05:56869–56871.
- Proposed: see the full rewrites below.

**F3. text. P2 (missing loci for true claims).**
- Sentence: "a deacon's own faction opened a rival congregation while our bishop was kept away in hiding, and ... a rival bishop was set up at Rome over a disputed election."
- Problem: no locus is given. "Rival congregation" rests on an editor's footnote ("probably in some church or congregation assembled by Felicissimus"). Cyprian's own words are "Another altar cannot be constituted ... Whosoever gathereth elsewhere, scattereth".
- Evidence: anf05:32237–32306 (Ep. XXXVII, Felicissimus excommunicated during Cyprian's absence); anf05:32273 (editor's note); anf05:32480–32481 (Ep. XXXIX); anf05:33217–33218 (Novatus "appointed his attendant Felicissimus a deacon"); anf05:32654ff (Ep. XLI, Cornelius and the Novatian party).
- Proposed: add these loci. Use "gathered apart" for "opened a rival congregation".

**Readability (existing defect, not a fidelity finding):** all three fields fail the gate as they stand: text FK 12.7 / FRE 53.2; positions[0] FK 12.4 / FRE 55.7; positions[1] FK 12.6 / FRE 44.9. Sentence-level fixes alone leave text and positions[0] failing, so I give full rewrites. They contain no new claims.

Proposed text (FK 6.7 / FRE 72.6):
> We can argue that a colleague's ruling was wrong, at length, and still keep him at our table. One of our bishops said so when he opened the council that would settle the hardest question in the room. No bishop, he said, sets himself up as a bishop of bishops. None forces a colleague to obey. Every bishop has his own proper right of judgment. At that same council, he said we judge no one, and reject no one from communion, for thinking differently from us. A century and a half later, another of our bishops argued at book length that the ruling made that day was wrong. He never once put the man who made it outside our communion. In our own first years, we had seen separation from the inside. A deacon's faction gathered apart while our bishop was away in hiding. In those same years, a rival bishop was set up at Rome over a disputed election. We do not pretend those separations never happened. We hold our rule against separation knowing, from our own record, what it costs when it breaks.

Proposed positions[0] (FK 6.7 / FRE 75.6):
> We can argue that a colleague's ruling was wrong, at length, and still keep him at our table. One of us said so when he opened the council that would settle the hardest question in the room. No bishop, he said, sets himself up as a bishop of bishops. None forces a colleague to obey, since each has his own proper right of judgment. He added that we judge no one, and reject no one from communion, for thinking differently from us. A century and a half later, another of us argued at book length that the ruling made that day was wrong. He never once suggested that the man who made it stood outside our communion. Disagreement, in our own life, is not a reason to separate.

Checked and sound: the paraphrase of the 256 preface (anf05:56872–56876). Augustine did not place Cyprian outside the Church's unity (npnf104:12997).

## 7. lpc.witness.confessor-claim-vs-regulated-peace

**G1. positions[0] and text. P1 (claim contrary to its own locus).**
- Sentences: positions[0]: "...gave him standing to ask that a named person, one who had failed the same test he had passed, be received back into the congregation at once." text: "...a survivor of interrogation carried a claim of his own: that his own suffering gave him standing to ask that a named person ... be received back into the congregation at once."
- Problem: in the cited Epistle X, the confessors themselves asked that peace be granted "as soon as with the end of the persecution we should have begun to meet". It was certain presbyters who admitted the lapsed at once, and Cyprian rebukes them for it. The naming also runs backwards. Certificates often read "Let such a one be received to communion along with his friends", and Cyprian had to ask the confessors to name people. A blanket "peace to all" also appears, in Lucian's letter. "A named person ... at once" fits none of these.
- Evidence: anf05:29876–29884 (Ep. X §1); anf05:29935–29945 (Ep. X §4); anf05:29984–29988 (Ep. XI, the martyrs "requesting that their wishes may be examined"); anf05:30700–30703 (Lucian: "have given peace to all").
- Proposed positions[0]: "In our earliest years, a confessor's suffering carried a claim of its own. Those who had held firm under questioning, and suffered for it, asked that some who had failed the same test be given peace. We took that claim in earnest. It was not a pretense, and it was not treated as nothing." (whole field FK 5.4 / FRE 80.3)
- Proposed text, first sentence: "In our earliest years, those who had confessed Christ and suffered for it made a claim of their own. Their suffering, they held, gave them standing to ask peace for some who had failed the test they passed."

**G2. text. P1 (claim wider than the source).**
- Sentence: "...a name set down, examined, weighed, and received at the end by the very people who watched the failure."
- Problem: Cyprian says the wishes will be "looked into in your presence, and with your judgment". The people examine and judge. Reception itself comes through the laying on of hands "by the bishops and clergy". "Received by the very people who watched the failure" adds a detail the source does not give.
- Evidence: anf05:29986–29988; anf05 Ep. X §1 (~29883, "before hands were placed upon the repentant by the bishops and clergy").
- Proposed: "...a name set down, then examined before the whole congregation and with its judgment."

Readability: text before FK 10.5, which already fails. With G1 and G2 it scores FK 7.8 / FRE 73.1.
Also: neither source carries a file or line locus. Ep. X sits at anf05:29836–29945. "The white-robed cohort" is at anf05:43654.

## 8. lpc.witness.constantine-did-not-corrupt: clean
All quotations are word for word (npnf104:17670, 17721). The Rome and Arles appeal and the basilica rulings are at npnf104:17722–17723. City of God V.25 matches, including Jovian and Gratian (npnf102:11099–11126).

## 9. lpc.witness.days-before-the-sun: clean
City of God XI.7 matches (npnf102:20392–20404). "Highly mendacious" and "not 6000 years" are word for word (npnf102:22597–22598).

## 10. lpc.witness.grant-me-chastity-but-not-yet

**J1. text. P1 (claim wider than the source).**
- Sentence: "You want to believe and cannot. One of our own knew exactly that condition..."
- Problem: Augustine's two cited moments are, first, praying for chastity "but not yet", and second, finding the truth "certain" while the burden still pressed. The second is the reverse of being unable to believe. "Exactly that condition" claims a fit the source does not support.
- Evidence: npnf101:12746–12748; npnf101:12760–12763.
- Proposed: "You want to believe and cannot. One of our own knew a trouble close to that, and he wrote it down himself, from before he was received among us."

**J2. positions[1]. P2 (interpretive comparison).**
- Sentence: "That later moment came separately, and it was worse, not better."
- Problem: the source gives no comparison. It reports "an horrible shame".
- Evidence: npnf101:12765–12766.
- Proposed: "That later moment came separately, and it brought him, in his words, \"an horrible shame.\""

Checked and sound: "Grant me chastity and continency, but not yet" is word for word.

## 11. lpc.witness.heard-for-salvation-not-for-wish

**K1. text. P1 (claim wider than the source).**
- Sentences: "Augustine drew a rule from this, one he did not confine to Paul alone. ... A prayer God does not answer as we asked is not, on this teaching, a prayer God failed to hear."
- Problem: the rule Augustine draws covers "the saints": "The saints are in all things heard unto salvation". In §7 he gives the opposite case, the devil, "heard for his will, not heard for salvation". The last sentence extends the rule to every prayer by anyone ("we").
- Evidence: npnf107:15215, 15218, 15222.
- Proposed: "Paul was heard for salvation, Augustine taught, even though he was not heard according to his wish. He made this a rule for the saints, not for Paul alone. They are always heard in what concerns their salvation, even when they are not heard as they wished." (FK 5.8 / FRE 77.0)

Checked and sound: "My grace is sufficient for thee: for strength is made perfect in weakness." is word for word.

## 12. lpc.witness.marriage-a-threefold-good

**L1. text and positions[0]. P2 (missing locus).**
- Sentence: "...against those who thought praising virginity meant condemning it."
- Problem: this rests on the translator's preface, not on Augustine's own text in the cited §§7 and 32. The preface says the treatise answered what remained of Jovinian, and was written so that Augustine's praise of virginity would not be taken as condemning marriage.
- Evidence: npnf103:32366–32383 (editor's preface).
- Proposed: no text change. Add the locus and mark it as the editor's note.

**L2. text. P2 (unsupported comparison).**
- Sentence: "That third good he pressed hardest."
- Problem: no cited passage ranks the three goods.
- Evidence: npnf103:33682–33684; npnf103:32710–32716.
- Proposed: "Of that third good he wrote this."

Checked and sound: the offspring / faith / sacrament triad, and the paraphrase of "a matter of a certain sacrament ... not made void even by separation".

## 13. lpc.witness.restless-heart-and-the-unrepentant-enemy

**M1. positions[0]. P2 (interpretive gloss beyond the source).**
- Sentences: "He did not treat the restlessness as a flaw to manage. He treated it as the shape of what a person is, until it finds what it was made for."
- Problem: Confessions I.1 gives only the sentence itself. The gloss is fair in spirit, but it is not in the source.
- Evidence: npnf101:3889–3890.
- Proposed: "On his telling, the restlessness comes from being made for God. It lasts until the heart finds its rest in him."

Checked and sound: the quotation is word for word. The Enchiridion 73 paraphrase, both standards, matches npnf103:22396–22421.

## 14. lpc.witness.scripture-above-councils

**N1. positions[1]. P2 (loose paraphrase).**
- Sentence: "He would not keep a practice merely because it was old and widespread."
- Problem: Cyprian speaks of "custom, which had crept in among some". "Widespread" is not his word.
- Evidence: anf05:39326–39328.
- Proposed: "He would not keep a practice merely because it was custom."

Checked and sound: the paraphrase of On Baptism II.3.4 (npnf104:11301–11304).

## 15. lpc.witness.the-only-son-and-the-trinity

**O1. text. P1 (unsupported detail).**
- Sentence: "Later a whole Arian people, standing outside our own gates, thought us wrong about it too."
- Problem: Possidius ch. 28 says that "Vandals and Alans, with some of the Gothic tribe" besieged Hippo. He does not name their creed, and he records no dispute over the Trinity. The only Arian label in the vendored file is the 1919 editor's introduction, about Geiseric. "A whole Arian people ... thought us wrong about it" is a claim no cited text makes.
- Evidence: poss:3982, poss:4079–4084 (siege); poss:472–477 (editor: "the Arian Geiseric").
- Proposed: cut that sentence and fold the Maximinus sentence into O2 (below).

**O2. text. P2 (ambiguous; locus not used).**
- Sentence: "An Arian bishop disputed it in his own lifetime."
- Problem: "his" has no clear antecedent. The cited Possidius locus gives the name, the place and the witnesses.
- Evidence: poss:2942–2945.
- Proposed (replacing both sentences): "An Arian bishop, Maximinus, disputed it with Augustine at Hippo, before many witnesses."

**O3. text. P2 (interpretive claims beyond the locus).**
- Sentences: "For us, Jesus being God and the Trinity are not two questions but one." / "This is the ground that everything else in our own creed stands on."
- Problem: Enchiridion 56 says the creed moves from the Son to the Spirit, "thus completing the Trinity". It then places the Church "subordinate to the Trinity, as the house to Him who dwells in it". It does not say "everything else in our creed stands on" this.
- Evidence: npnf103:21852–21868.
- Proposed: "For us, Jesus being God and the Trinity belong to one confession." / "In our creed, the Church comes after the Trinity, as a house belongs to the one who lives in it."

Readability with all edits: FK 6.9 / FRE 68.1.

## 16. lpc.witness.the-pattern-we-are-modelled-on: clean
Enchiridion 53 matches closely (npnf103:21778–21800), including "not merely in a mystical sense, but in reality".

## 17. lpc.witness.tradition-tested-by-apostolic-warrant

**Q1. text. P1 (factual misstatement).**
- Sentences: "In this dispute itself, neither test traces the road back, or the teaching before the water, to a named apostolic origin. Elsewhere, Augustine does trace two other practices of ours ... The other is refusing to baptize again a person already baptized among heretics."
- Problem: not rebaptizing is the very practice in this dispute, not an "other" one. In the cited V.23 Augustine traces it, here, to apostolic tradition: "the custom, which is opposed to Cyprian, may be supposed to have had its origin in apostolic tradition".
- Evidence: npnf104:13139–13141; compare npnf104:12163–12164.
- Proposed: "In this very dispute, Augustine used his test on one practice. He held that not baptizing again someone baptized among heretics came down from the apostles. Elsewhere he said the same of baptizing infants. Neither test traces the road back, or the teaching before the water, to the apostles."

**Q2. text. P2 (overstatement).**
- Sentence: "He held the opposite."
- Problem: Augustine also tests by Scripture ("What truth has declared, that we follow"). His test differs from Cyprian's, but it is not simply the opposite.
- Evidence: npnf104:12168–12169.
- Proposed: "He used a different test."

**Q3. positions[0]. P2 (misleading label).**
- Sentence: "Writing against a rival bishop's own claimed tradition..."
- Problem: Stephen was bishop of Rome and Cyprian's colleague in communion, not a rival claimant to a see.
- Evidence: anf05:39103–39112; npnf104:13136.
- Proposed: "Writing against the tradition claimed by Stephen, bishop of Rome, he asked:"

Checked and sound: "Whence is that tradition? ..." matches anf05:39112–39115.

## 18. lpc.witness.violence-commanded-not-cruel

**R1. text and positions[0]. P2 (loose paraphrase).**
- Sentence: "...he was, in his own words, 'much disturbed' by one question."
- Problem: Confessions III.7.12 lists three questions: where evil comes from, whether God has a body, and whether men with many wives who killed were righteous. "At which things I ... was much disturbed" covers all three.
- Evidence: npnf101:5890–5894.
- Proposed: "...'much disturbed' by questions like this one."

**R2. text and positions[0]. P2 (overstatement).**
- Sentence: "...a Manichaean who raised exactly this same charge"
- Problem: Faustus's Book XXII charges deal with Moses and the patriarchs. They are close in kind, not the same question word for word.
- Evidence: npnf104:8100–8160.
- Proposed: "...a Manichaean who pressed the same kind of charge"

**R3. text. P2 (unsupported motive).**
- Sentence: "Our bishop did not answer this way because he thought little of it."
- Evidence: none.
- Proposed: "He did not stop at that answer."

**R4. text. P2 (phrase in quotation marks not in the source's wording).**
- Sentence: "And 'turn the other cheek' asks first for an inward disposition."
- Problem: the vendored text reads "turn to him the left also", and the answer is "not a bodily action, but an inward disposition". "Asks first" softens Augustine's "not ... but".
- Evidence: npnf104:8151–8152.
- Proposed: "And Christ's command to turn the other cheek asks for an inward disposition, not a bodily action."

Checked and sound: "showed not ferocity but obedience" and "acted not in cruelty, but in righteous retribution, giving to all what they deserved" are word for word (npnf104:8160–8161). The Abraham contrast matches §73. The two orders and the martyrs match §76 (npnf104:8152–8153).

---

## Fields checked clean (17)

- almsgiving-quenches-sin: positions[1]
- confessor-claim-vs-regulated-peace: positions[1]
- constantine-did-not-corrupt: text, positions[0]
- days-before-the-sun: text, positions[0]
- grant-me-chastity-but-not-yet: positions[0]
- heard-for-salvation-not-for-wish: positions[0]
- restless-heart-and-the-unrepentant-enemy: text, positions[1]
- scripture-above-councils: text, positions[0]
- the-only-son-and-the-trinity: positions[0]
- the-pattern-we-are-modelled-on: text, positions[0], positions[1]
- violence-commanded-not-cruel: positions[1]

## Counts

- Fields in scope: 45. Clean: 17. With at least one finding: 28.
- **P1: 11.** A1 (1); B1, B2 (2); F1 (1); G1 positions[0] and text (2); G2 (1); J1 (1); K1 (1); O1 (1); Q1 (1).
- **P2: 33.**
- Existing readability failures: communion-over-separation text, positions[0] and positions[1]; confessor-claim-vs-regulated-peace text. Full-field rewrites that pass are given in sections 6 and 7.
