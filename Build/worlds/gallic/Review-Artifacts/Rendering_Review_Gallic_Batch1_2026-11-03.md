# Rendering Review: gallic quote records, batch 1 (28 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 28 `gallic.quote` records.

## Method

Each record's `sources[].locus` names a vendored file and line span. Twenty-seven sit in `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`; one (Augustine) sits in `cic/texts/npnf105_augustine-anti-pelagian-writings.xml`. For every record the edition lines were read directly. A script stripped `<note>…</note>` and other tags, unescaped entities, rejoined line-end hyphens, folded whitespace (including U+00A0) and normalised curly quotes, then tested whether the record's `text` occurs verbatim. The tight span given below is the smallest run of lines that still contains the whole quote. The rendering was then read clause by clause against the edition text, with the surrounding lines read for speaker, referents and hedges. Sentence lengths were counted by hand, word by word, on every sentence that looked long (hyphenated compounds count as one word). Each rendering was also checked against the record's `confidence.divergence_note` and `use_note.not_for`.

## Results

**28 records: 26 PASS, 2 FAIL (1 P1, 1 P2).**

Text check: 27 pass; 1 fails on letter case only (`castor-anxious-for-egyptian-institutions`, see its row). The text-check result does not change the rendering verdict.

| Record id (gallic.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| abundance-of-power-not-granted-as-bishop | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 4038-4043 | pass | all clauses; "he said" keeps the reported frame; longest 25 | PASS |
| allegiance-to-antiquity-not-a-few | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16668-16672 | pass | all clauses; "not a few / but antiquity" contrast kept across sentences; longest 21 | PASS |
| aloof-from-assemblies-of-bishops | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5217-5219 | pass | all clauses; "sixteen years" and "synod" kept; longest 18 | PASS |
| antiquity-and-the-fathers-unanimous-decision | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16668-16672 (locus says 16667-16671) | pass | all clauses; "unanimous" as "one shared decision"; longest 23 | PASS |
| apostolic-authority-in-martin-alone | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 1563-1565 | pass | all clauses; "degenerate submissiveness" as "debased submission"; "in Martin alone" kept; longest 17 | PASS |
| archebius-carried-off-to-panephysis | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 36807-36825 | pass | all clauses incl. the parenthesis; thirty-seven years kept; longest 20 | PASS |
| archebius-see-the-old-men | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 36829-36839 | pass | all clauses; "I think" kept; pearl of the Gospel kept; longest 19 | PASS |
| augustine-in-darkness-on-predestination | cic/texts/npnf105_augustine-anti-pelagian-writings.xml, line 20836 | pass | all clauses; Phil. 3:15 citation and its condition kept; longest 22 | PASS |
| believed-everywhere-always-by-all | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 12185-12190 | pass | all clauses; everywhere/always/by all and the three tests kept; "consent" as "agreement"; longest 13 | PASS |
| benjamin-relied-on-his-own-judgment | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 28106-28110 | pass | "for" now explains the wrong clause (see below) | FAIL P2 |
| brictio-called-by-demons-on-the-rock | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5289-5299 | pass | "I believe" no longer governs "being conscious" (see below) | FAIL P1 |
| brictio-horses-and-slaves | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5299-5305 | pass | all clauses; "accused by many" kept as accusation, not fact; longest 20 | PASS |
| brictio-returns-and-repents | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5323-5330 | pass | all clauses; "I believe" kept on the demons' expulsion; longest 15 | PASS |
| brictio-tirade-and-martins-restraint | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5305-5319 | pass | all clauses; "as I believe" kept; "he said" frames Brictio's claims; longest 19 | PASS |
| cassian-adapts-egypt-to-gaul | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16515-16534 | pass | all clauses; Egypt/Palestine and Pontus/Mesopotamia kept; longest 23 | PASS |
| cassian-archebius-expelled-from-monastic-system | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 36820-36825 (locus says 36807-36823) | pass | all clauses; indirect speech kept; longest 26 (about 25, not a fail) | PASS |
| cassian-clothes-kept-until-excellence-of-progress | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 18678-18681 | pass | all clauses; "kept until", not kept for good; longest 23 | PASS |
| cassian-refuses-to-weave-a-tale-of-miracles | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16502-16515 | pass | all clauses; "seen them fulfilled" kept; eight faults kept; longest 25 | PASS |
| castor-anxious-for-egyptian-institutions | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16433-16435 | FAIL (case only: record "Since"; edition "since", lower case after "—") | all clauses; "your province", not all Gaul; longest 14 | PASS |
| chaeremon-grace-requires-our-effort | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 38200-38207 | pass | all clauses incl. "sometimes even to require"; "sometimes" kept; longest 21 | PASS |
| chaeremon-three-stages-of-grace | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 38601-38624 | pass (space before ")" is where the edition's note sits) | all three stages and their free-will limits; Isa. 7:9 kept; longest 24 | PASS |
| conferences-received-into-their-cells | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 42312-42325 (locus says 42305-42325) | pass | all clauses; "after a fashion" as "in a way"; "almost unknown in this country" kept; longest 21 | PASS |
| council-over-rashness-and-ignorance | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 12218-12220 | pass | all clauses; "if such there be" kept; longest 21 | PASS |
| customs-delivered-to-us-by-the-fathers | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16444-16446 | pass | fragment rendered as fragment; "delivered ... by the Fathers" kept; 19 words | PASS |
| deserter-from-his-service | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 23521-23524 (locus says 23518-23524) | pass | all clauses; 2 Tim. 2:4 phrase kept in quotation marks; longest 23 | PASS |
| devil-incites-desire-for-holy-office | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 26944-26947 | pass | all clauses; "pretext" as "excuse"; ordination not called evil; longest 17 | PASS |
| egyptian-sackcloth-utterly-disapproved | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 16651-16660 (locus says 16650-16663) | pass | all clauses; both grounds (conspicuous, unsuited to work) kept; longest 21 | PASS |
| europe-will-not-yield-having-only-martin | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 5408-5411 (locus says 5398-5411) | pass | all clauses; "justly proud" concession kept; "only Martin" as "Martin alone"; longest 15 | PASS |

## Failed renderings: corrected text

**benjamin-relied-on-his-own-judgment (FAIL P2).** In the edition, "for he forsook the desert" explains "what sort of an end" his life had, and "who ... relied on his own judgment" identifies the man. The rendering makes the reliance a free-standing sentence and puts "For" right after it. Leaving the desert then reads as the proof that he relied on his own judgment, not as the end he came to.

Corrected rendering:

> And you surely remember this man, who stubbornly and persistently relied on his own judgment rather than on the traditions of the Elders. You remember what kind of end his life came to. For he left the desert and went back to the empty philosophy of this world and to earthly vanities.

**brictio-called-by-demons-on-the-rock (FAIL P1).** In the edition, "being conscious how great frenzy of spirit they had excited within him" sits inside Gallus's "I believe they perceived...". The rendering splits it off as "They knew how great a frenzy of spirit they had stirred up in him." That states the demons' knowledge as plain fact and drops the speaker's hedge from it. "From there" is also an addition the edition does not make.

Corrected rendering:

> Again, one day, he had sat down on that wooden seat of his, which you all know. It stood in the small open yard around his dwelling. He saw two demons sitting on the high rock that hangs over the monastery. Then he heard them call out, in eager and joyful voices, ‘Come here, Brictio, come here, Brictio.’ I believe they saw the wretched man coming from far off, knowing how great a frenzy of spirit they had stirred up in him. There is no delay. Brictio rushes in, in utter fury. There, full of madness, he spews out a thousand insults against Martin.
