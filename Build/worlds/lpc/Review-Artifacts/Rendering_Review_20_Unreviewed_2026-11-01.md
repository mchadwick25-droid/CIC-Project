# Rendering Review: lpc quote records (20 unreviewed + 8 unsettled)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-01
- **Branch read:** `claude/lpc-rendering-log` (no record edited)
- **Subject:** the `text` and `modern_rendering` of 28 `lpc.quote` records in `records/lpc/quote/`: the 20 renderings never reviewed, and 8 added by the coordinator. The 8 had been reviewed before, but either with no clear verdict on the rendering or with a fix applied and never re-read. They include `thirteen-letters-sent-to-rome` after its round-2 wording fix and `no-repentance-is-too-late` after the 'secured' to 'provided for' change.

## Method

1. **Quote text, verbatim.** Each record's `text` was compared with the first vendored file named in `sources[].locus`, at the cited lines. Two independent methods were used:
   - **Method A (Python).** Read the lines, strip `<note>…</note>` and all other tags, unescape entities, rejoin words hyphenated across lines, fold all Unicode whitespace, then run a substring test.
   - **Method B (shell).** `sed -n a,bp`, then `sed` to turn non-breaking spaces into plain spaces, `perl` to strip notes and tags and rejoin hyphenated words, `tr -s` to fold whitespace, then `grep -F`.

   Range tightness was also tested. Dropping the first cited line must lose the opening words, and dropping the last cited line must lose the closing words. So each range starts on the line holding the passage's first word and ends on the line holding its last.

   One note on Method B: the first run failed on two ANF passages, `a-dreadful-plague-broke-out` and `good-done-to-all-not-only-the-household`. The cause was a non-breaking space (U+00A0) at a line end in the XML, which plain `tr` does not fold. With that whitespace folded, both pass. The record text itself was correct.
2. **Rendering rule.** Each rendering was checked clause by clause against the text, and against the Latin wherever the locus cites it:
   - every clause rendered, nothing added;
   - one thought per sentence;
   - no sentence past about 25 words (counted by script and by hand);
   - no word whose modern sense misleads;
   - the world's hedges and reported-speech frames kept.
3. **Guards.** The rendering and text were checked against `use_note.not_for` and `claim_guards`.

## Sources checked

- `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml` (ANF English: Pontius, Cyprian's Epistles, To Demetrianus)
- `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` (Hartel's Latin of Pontius)
- `cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt` (Hartel's Latin of the Epistles)
- `cic/texts/cyprian_ad-demetrianum-lat_hartel1868-csel3-tei.txt`
- `cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` (Acta Proconsularia)
- `cic/texts/possidius_vita-augustini_weiskotten1919.txt` (English and facing Latin)
- `cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml` and `cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt` (Enchiridion)
- `cic/texts/npnf101_augustine-confessions-letters.xml` (Confessions)
- `cic/texts/npnf108_augustine-exposition-psalms.xml` and `cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt` (Enarrationes)

## Results

**28 records: 22 PASS, 6 FAIL (2 P1, 4 P2).** All 28 texts pass both verbatim methods, and every cited range is tight.

| Record id (lpc.quote.…) | Text check (A / B / range) | Rendering check | Verdict |
|---|---|---|---|
| a-dreadful-plague-broke-out | pass / pass (NBSP folded) / tight | all clauses; 'put out their own people' follows suos and exponere; longest sentence 24 | PASS |
| a-hundred-thousand-sesterces | pass / pass / tight | all clauses; nothing added; no modern-money figure | PASS |
| a-standard-bearer-of-the-sect | pass / pass / tight | the sentence's last two charges lose their reported frame; last sentence joins two thoughts | **FAIL P1** |
| because-i-am-already-weary | pass / pass / tight | all names kept; 'his family' for cum suis is not misleading here | PASS |
| chosen-while-still-a-neophyte | pass / pass / tight | sacerdotium, neophytus, nouellus and generosa indoles rendered per the divergence note; longest 23 | PASS |
| christ-redeemed-in-our-captive-brethren | pass / pass / tight | 'who abides and dwells in us' correctly given to Christ (Latin ipse qui manet); Galatians kept as quotation | PASS |
| good-done-to-all-not-only-the-household | pass / pass (NBSP folded) / tight | 'Tobias must forgive' and 'he must rightly grant' read as obligation; the Latin ignoscat and concedat are 'let him' | **FAIL P2** |
| grief-and-not-without-tears | pass / pass / tight | all clauses | PASS |
| grieve-with-me-for-my-sister | pass / pass / tight | 'a death of the spirit' guards not_for; the hedge 'as seems clear to us' is kept | PASS |
| he-covered-his-eyes-with-his-own-hand | pass / pass / tight | faithful to the Latin; does not merge with Pontius | PASS |
| he-slept-with-his-fathers | pass / pass / tight | 'as it is written' and the quotation marks are kept; longest 23 | PASS |
| o-blessed-people-of-the-church | pass / pass / tight | 'whoever' (quicumque) turned into the factual 'some'; 'as his envoy' leaves unclear whose | **FAIL P2** |
| penitents-in-peril-of-sickness-should-be-assisted | pass / pass / tight | single clause rendered whole; 'peace' is the world's own term, used across sibling renderings | PASS |
| shut-up-in-two-cells | pass / pass / tight | 'partly … and partly' and 'we all … for everyone' reshape a confused clause into a crisp claim the text does not make | **FAIL P2** |
| thank-offerings-for-the-very-good | pass / pass / tight | three outcomes kept distinct; 'they do not help the dead' is kept for the very bad | PASS |
| the-paper-itself | pass / pass / tight | handwriting, content and 'from the clergy' follow the Latin; longest 23 | PASS |
| the-people-kept-watch-at-the-door | pass / pass / tight | all clauses; no prison cell implied | PASS |
| the-psalms-hung-upon-the-wall | pass / pass / tight | 'very few' follows the Latin per the divergence note; longest 25 | PASS |
| the-trees-and-the-trembling-executioner | pass / pass / tight | all clauses; the strengthening stays inside Pontius's telling | PASS |
| the-whole-people-of-the-brethren-came | pass / pass / tight | faithful to the Latin; no danger supplied | PASS |
| all-the-merit-or-demerit-is-acquired-in-this-life | pass / pass / tight | keeps 'their living friends' / 'Those friends' for suorum; makes the friends offer the sacrifice where the Latin is passive | **FAIL P1** |
| not-to-be-refused-to-any-one-born-of-man | pass / pass / tight | all clauses; 'any human being who is born' follows nulli hominum nato | PASS |
| remember-me-at-the-lords-altar | pass / pass / tight | all clauses; stays inside quotation marks as Monica's reported words | PASS |
| the-life-and-the-death-shall-both-be-without-end | pass / pass / tight | all clauses; 'without end' kept; no group named | PASS |
| the-mildest-punishment-of-all | pass / pass / tight | 'sin of their own' fixes the misleading 'actual'; no infants or baptism named | PASS |
| they-first-dwelt-together-in-unity | pass / pass / tight | 'he says' kept; 'there' left unnamed per claim_guards; longest 25 | PASS |
| thirteen-letters-sent-to-rome (current, after round-2 fix) | pass / pass / tight | 'Nothing was missing from them' widens the Latin 'none of these was lacking' to everything; that sentence runs 26 words | **FAIL P2** |
| no-repentance-is-too-late (current, after 'provided for') | pass / pass / tight | 'provided for' is right for prouidetur; warning and offer both kept | PASS |

## Details of each FAIL

### lpc.quote.a-standard-bearer-of-the-sect: FAIL P1 (hedge dropped)

The text keeps all four charges inside the proconsul's sentence: 'wherein he was called a standard-bearer of the sect, and an enemy of the gods, and one who was to be an example to his people; and that with his blood discipline would begin to be established'. The Latin is the same: in qua dictus est … et qui suis futurus esset ipse documento et quod sanguine eius inciperet disciplina sanciri.

The rendering keeps the frame only for the first two: 'In it Cyprian was called…'. It then states the other two as Pontius's own assertion: 'He was to be an example to his own people, and with his blood discipline would begin to be made firm.' That is reported speech losing its hedge. It also puts two thoughts in one sentence.

Proposed rendering:

> And so the judge read the sentence from his tablet, the one he had not read in the vision a little before. It was a spiritual sentence, not to be spoken lightly. It was a sentence worthy of such a bishop and such a witness. It was a glorious sentence. In it Cyprian was called a standard-bearer of the sect and an enemy of the gods. It also called him one who was to be an example to his own people. And it said that with his blood, discipline would begin to be made firm.

### lpc.quote.good-done-to-all-not-only-the-household: FAIL P2 (misleading modern sense)

The Latin is ignoscat ille et ignoscat iterum et frequenter ignoscat aut … merito concedat. Both verbs are jussive subjunctives: 'let him forgive', 'let him rightly grant'. Pontius is asking Tobias's pardon for the comparison.

In modern English, 'Tobias must forgive' and 'he must rightly grant' read as obligations laid on Tobias. Changing 'must' to 'let' fixes this without adding anything.

Proposed rendering:

> So good was done, in a flood of generous works, to all people, not only to those of the household of faith. More was done than is recorded of the matchless kindness of Tobias. Let Tobias forgive, and forgive again, and often forgive. Or, to speak more truly, let him rightly grant this. Much could be done before Christ, but something more could be done after Christ, since all fullness belongs to His times. Tobias gathered those whom the king had killed and thrown out, but only those of his own race.

### lpc.quote.o-blessed-people-of-the-church: FAIL P2 (generalization made factual; unclear referent)

- **'some' for 'whoever'.** The text says 'whoever … eagerly desired to suffer' (Latin quicumque … uoluit), a general statement. The rendering says 'Yet some … truly longed to suffer', which turns it into a report that some people did. That is a claim the sentence does not make.
- **'as his envoy'.** Hartel has legationis … litteras, an envoy's letter. 'Each of them sent a kind of letter to God, as his envoy' leaves unclear who the envoy is.

Proposed rendering:

> O blessed people of the Church! In sight and in feeling, and what is more in words spoken aloud, they suffered with such a bishop as theirs. As they had always heard him say in his own sermons, they were crowned by God the Judge. The common wish was that the whole congregation should suffer at once, sharing a like glory. That could not happen. Yet whoever truly longed to suffer, under the watching eyes of Christ and in the hearing of the bishop, sent God a kind of envoy's letter. That longing was witness enough.

(The second-to-last sentence is 25 words. 'That longing was witness enough' renders 'by the sufficient testimony of that desire', Latin per idoneum uoti sui testem.)

### lpc.quote.shut-up-in-two-cells: FAIL P2 (added structure)

The text reads 'in part of what Paulus bade me, as what we in all cases decreed'. The Latin is partim quod mihi Paulus praecepit quam uniuersis quod censuimus, and is broken.

The rendering, 'partly what Paulus told me, and partly what we all decided for everyone', makes two changes:

- It splits the act into two shares ('partly … partly'), which neither the English nor the Latin does.
- It moves 'all' onto the subject ('we all').

The result is a clear claim built on a sentence the record's own not_for says is not clear. The fix keeps the text's 'in part … as [also]' and 'in all cases'.

Proposed rendering:

> So you see, brother, how I have done this. It is in part what Paulus told me, and also what we decided in every case while we were in this trouble. In it, by the emperor's command, we were ordered to be put to death by hunger and thirst. We were shut up in two cells, so that they might weaken us by hunger and thirst. Besides, the fire that came with our torture was so unbearable that no one could endure it. But now we have reached the brightness itself.

### lpc.quote.all-the-merit-or-demerit-is-acquired-in-this-life: FAIL P1 (misleading modern sense)

- **'friends' for suorum.** The Latin is pietate suorum viventium, 'by the devotion of their own living people', meaning family and household. The rendering keeps the ANF's 'their living friends' and repeats it as 'Those friends'. This is the same 'friends' for suos fault that `a-dreadful-plague-broke-out` corrects in its divergence note.
- **Who offers the sacrifice.** The Latin is passive: quum pro illis sacrificium mediatoris offertur, vel eleemosynae in ecclesia fiunt, 'when the sacrifice of the Mediator is offered for them, or alms are given in the church'. The rendering's 'Those friends offer the sacrifice of the Mediator' names the relatives as the ones who offer it. That goes past the claim_guard that the passage says nothing of the sacrifice beyond those words.

Proposed rendering:

> Nor can it be denied that the souls of the dead are helped by the devotion of their own living people. This is when the sacrifice of the Mediator is offered for them, or alms are given in the church on their behalf. But these services help only those who earned, during their lives, the kind of merit that lets such services help them. For there is a way of life that is not so good that it needs no such help after death. Nor is it so bad that such help is of no use after death. There is also a kind of life so good that it does not need them. And there is one so bad that, when life is over, they give no help. So all merit or blame is gained in this life. It can either ease or worsen a person's sufferings after this life. No one, then, should hope to gain after death the merit with God that he neglected to secure here.

The record's divergence_note is currently null. It should then record that the rendering follows Hartel/Bruder's Latin over the ANF English for suorum and for the passive offertur.

### lpc.quote.thirteen-letters-sent-to-rome: FAIL P2 (widened claim; length), current rendering after round-2 fix

The Latin is nec clero consilium nec … adlocutio et persuasio nostra defuit: none of these four things was lacking. The rendering opens with 'Nothing was missing from them'. That widens the claim to everything, and only then lists the four.

The same sentence runs 26 words and stacks three qualifiers ('as far as…', 'with the Lord's help', 'under the law of faith…'). Moving the 'nothing missing' sentence after the list, and limiting it to 'these', fixes both problems.

Proposed rendering:

> These thirteen letters show you what I did. I sent them out at different times, and I have passed them on to you. In them there was advice to the clergy and encouragement to the confessors. When it was needed, there was rebuke to the exiles. And there were my appeals to the whole brotherhood, urging them to beg for God's mercy. None of these was missing. I gave as much as my poor abilities could, with the Lord's help, by the law of faith and the fear of God.

## Notes on borderline items passed

- **no-repentance-is-too-late.** 'Provided for' is correct for prouidetur ('is provided for', not 'is secured'). The re-read found nothing else.
- **thank-offerings-for-the-very-good.** 'So sacrifices … are offered' turns the text's 'When, then, …' into a statement. The Latin cum ergo … offeruntur is a general 'whenever'. The statement is true of the practice the passage assumes and adds no claim.
- **penitents-in-peril-of-sickness-should-be-assisted.** 'Peace' is kept as the world's own term for readmission. Sibling renderings use it the same way (for example `before-even-a-deacon`, 'letters of peace').
- **a-standard-bearer-of-the-sect.** 'Witness' (teste) is kept. Its martyr sense is explained in the modern_lens_note.

## Round 2 recheck

Targeted recheck of the six records whose modern_rendering was replaced after round 1. Each new rendering was read against the record's `text` and the cited Latin (Hartel for Pontius and the Cyprian letters, Bruder for the Enchiridion). Sentence lengths were counted by hand.

| Record | Verdict |
|---|---|
| a-standard-bearer-of-the-sect | PASS |
| all-the-merit-or-demerit-is-acquired-in-this-life | PASS |
| good-done-to-all-not-only-the-household | PASS |
| o-blessed-people-of-the-church | FAIL (length) |
| shut-up-in-two-cells | PASS |
| thirteen-letters-sent-to-rome | PASS |

- **a-standard-bearer-of-the-sect.** All four charges now sit inside the sentence's frame ('It also called him…', 'And it said that…'), as in dictus est … et qui … et quod. The round 1 finding is fixed. Longest sentence: 20 words.
- **all-the-merit-or-demerit-is-acquired-in-this-life.** 'Their own living people' renders suorum viventium. The passive 'is offered … are given' matches offertur … fiunt and names no offerer. The divergence_note records both choices. Longest sentence: 22 words.
- **good-done-to-all-not-only-the-household.** 'Let Tobias forgive … let him rightly grant this' renders the jussives ignoscat … concedat. Nothing else changed.
- **o-blessed-people-of-the-church.** 'Whoever' (quicumque) and 'a kind of envoy's letter' (legationis quodammodo litteras) fix both round 1 points. But the round 1 count of 25 words was wrong. 'Yet whoever truly longed to suffer, under the watching eyes of Christ and in the hearing of the bishop, sent God a kind of envoy's letter.' is 26 words and stacks two qualifiers between subject and verb. That is the same fault failed in thirteen-letters in round 1. Corrected rendering (that sentence becomes 22 words; nothing else changes):

> O blessed people of the Church! In sight and in feeling, and what is more in words spoken aloud, they suffered with such a bishop as theirs. As they had always heard him say in his own sermons, they were crowned by God the Judge. The common wish was that the whole congregation should suffer at once, sharing a like glory. That could not happen. Yet whoever truly longed to suffer, under Christ's watching eyes and in the bishop's hearing, sent God a kind of envoy's letter. That longing was witness enough.

- **shut-up-in-two-cells.** 'In part … and also' and 'in every case' keep the text's 'in part … as' and 'in all cases' (partim … quam uniuersis). The split shares and the moved 'all' are gone. Longest sentence: 22 words.
- **thirteen-letters-sent-to-rome.** 'None of these was missing' now limits the claim to the four items (nec … nec … defuit). The modesty hedge (quantum … nostra mediocritas potuit eniti) is kept in the next sentence. Longest sentence: 22 words.
