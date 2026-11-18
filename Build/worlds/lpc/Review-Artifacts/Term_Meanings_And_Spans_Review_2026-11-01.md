# LPC term meanings and spans, and the election-of-Cyprian loci: independent review

Date: 2026-11-01. Reviewer: independent (Opus 5.5). I did not draft these records, and I made no edits to them.
Branch: `claude/lpc-term-spans`, uncommitted working tree (`git diff -- records/lpc/term records/lpc/story`).
Method: I opened every cited line range with three to ten lines of context on each side. I checked the English and the Latin separately. I also searched the vendored corpus for any passage that a locus quotes but its span leaves out.

## Severity rule used

- **P1**: part of `means`, `plain_meaning` or `quick_meaning` rests on no cited, line-verified passage, and no locus in the record names a specific place that carries it. A P1 can also be a locus that attributes a quotation to the wrong work.
- **P2**: the claim is carried by the vendored text next to the span, or in a section the locus already names, but the span does not hold it. P2 also covers a span that starts or ends mid-sentence, a locus with the wrong section number, and meaning wording that breaks the rendering rules (sentence length, misleading word, weakened claim).
- File names are relative to `cic/texts/`. `anf05` means `anf05_hippolytus-cyprian-caius-novatian.xml`. `Hartel-Ep` means `cyprian_epistulae-lat_hartel1871-csel3-tei.txt`. Every line number below was checked against the file.

## Summary

| # | Term | Verdict | Sev. |
|---|---|---|---|
| 1 | bishop-of-bishops | FAIL | P2 |
| 2 | catechesis | FAIL | P2 |
| 3 | certificates-letters-of-peace | FAIL | P2 |
| 4 | communion | FAIL | P2 |
| 5 | compel-them-to-come-in | FAIL | P2 |
| 6 | confessor | FAIL | P1 |
| 7 | grace | PASS | — |
| 8 | heresy | FAIL | P2 |
| 9 | libellatici-sacrificati | FAIL | P2 |
| 10 | libelli | FAIL | P2 |
| 11 | plenary-council | FAIL | P2 |
| 12 | preaching | FAIL | P1 |
| 13 | reconciliation-penitential-discipline | FAIL | P2 |
| 14 | schism | FAIL | P1 |
| 15 | suffrage | FAIL | P2 |
| 16 | the-flock | FAIL | P2 |
| 17 | the-lapsed | FAIL | P2 |
| 18 | the-one-episcopate | PASS | — |
| 19 | the-people | FAIL | P1 |

**Part A: 2 PASS, 17 FAIL (4 at P1, 13 at P2).** Most P2s are mechanical span corrections, and each one comes with verified line numbers. Only four terms need a change to their meaning text: confessor, preaching, schism and the-people.

**Part B (election-of-Cyprian): FAIL, P2.** Two of the three spans end or start mid-sentence. Five sentence-level claims in `text` and `telling` rest on none of the cited lines. Details are in Part B below.

---

## Part A: term by term

### 1. lpc.term.bishop-of-bishops: FAIL (P2)
**Span.** English anf05 56875-56879 opens on the tail of the editor's endnote ("Cyprian with that of his intolerant compeer].") and then runs "nor by tyrannical terror … can judge another." It leaves out the headword clause the locus quotes: "For neither does any of us set himself up as a bishop of bishops" (56871-56872). It also leaves out the clause that `means` needs for "each answers to Christ": "But let us all wait for the judgment of our Lord Jesus Christ … judging us in our conduct there" (56881-56884). The Latin, cyprian_sententiae-episcoporum 140-144, does hold "episcopum se episcoporum" through "alterum iudicare. sed expectemus". But "iudicium Domini nostri Iesu Christi … de actu nostro iudicandi" runs on to 147.
- Supported: no bishop stands over another; each has his own judgment.
- Not supported by the span: "each answers to Christ".

**Meaning.** PASS. "Only Christ judges him" is a fair reading of "the only one that has the power … of judging us".
**Fix.** English: anf05 lines 56871-56884. Latin: lines 140-147. No change to the meaning text.

### 2. lpc.term.catechesis: FAIL (P2)
**Span.** The only line span is Enchiridion 52 (npnf103 line 21773, "not adults only, but infants as well"). The span is accurate, but it supports neither part of `means`: not "teaching of the creed before baptism", and not "Augustine wrote a guide to it". The other loci name works but give no lines.
**Meaning.** "Catechesis was the teaching of the creed" is narrower than *On the Catechising of the Uninstructed*. That work treats first instruction of inquirers, "taught the Christian faith from its very rudiments". The creed was handed over in a separate sermon. `quick_meaning` already says "the creed, and the basics of belief", which is the better scope.
**Fix.**
- Add verified spans:
  - On the Creed, a sermon to the catechumens: npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml, lines 30467-30478, from "Receive, my children, the Rule of Faith" to "to rehearse and to repeat in answer". This passage carries the creed received and given back.
  - On the Catechising of the Uninstructed 1: same file, lines 24020-24028, from "You have requested me, brother Deogratias" to "an attractive method of discourse". This passage carries the guide.
- `means`: "Catechesis was the teaching given before baptism, including the creed, and Augustine wrote a guide to it."

### 3. lpc.term.certificates-letters-of-peace: FAIL (P2)
**Span.** anf05 29945-29948 holds only Epistle X 4's "designate by name in the certificate …". It ends one line early: the sentence closes "faith and discipline." on 29949. The Latin, Hartel-Ep 2473-2475, likewise stops at "libello et", and the sentence ends "litteras dirigatis" on 2476.
- Supported: "Cyprian wanted a name on it".
- Not supported by the span: "a confessor's letter of peace for the lapsed". That claim sits in the same paragraph, anf05 29935-29944: "designate those by name to whom you desire that peace should be granted … certificates are so given … 'Let such a one be received to communion along with his friends'".
- The Epistle XIV and XVI quotations in the locus have no span. I verified both:
  - Ep. XIV: anf05 30198-30207, "thousands of certificates were daily given"; Latin Hartel-Ep 3010.
  - Ep. XVI: anf05 30387-30391, "we have granted peace"; Latin Hartel-Ep 3389-3391.

**Meaning.** `plain_meaning` says "Some named one person and then let in his own people too". The confessors did not let anyone in. The certificate *asked* that the man's friends be received, and the bishop did the admitting.
**Fix.**
- Spans: English anf05 29935-29949, Latin Hartel-Ep 2473-2476 (from "et ideo peto"). Add the Ep. XIV and Ep. XVI lines above.
- `plain_meaning`, last sentence: "Some named one person, and then asked peace for his friends too, without naming them."

### 4. lpc.term.communion: FAIL (P2)
**Span.** The English, anf05 56868-56871, holds "It remains … if he should think differently from us." Good. The Latin, 138-139, starts after the page break and leaves out "superest ut de hac ipsa" on line 121.
- Supported: communion can be taken away ("rejecting any one from the right of communion"), and it should be kept through disagreement.
- Not supported by any span: "given back". The Augustine and Letter 185 loci carry no lines.

**Meaning.** PASS on wording.
**Fix.**
- Latin: lines 121 and 138-139.
- For "given back", add Epistle IX 2 as a cyprian-epistles source. Read it from "For although in smaller sins" through "receive the right of communion": anf05 29767-29773, Latin Hartel-Ep 2566-2569 (the same passage as term 13). Alternatively, drop "given back" from `means`.

### 5. lpc.term.compel-them-to-come-in: FAIL (P2)
**Span.** npnf104 19616-19617 holds the right passage: "if the power which the Church has received … through the religious character and the faith of kings, be the instrument by which those … in heresies and schisms … are compelled to come in". But that passage is **§24** (paragraph id v.vi.viii-p22, Chapter 6), not §§25-26 as the locus says. §26 starts at 19634 and is about the envoys and the laws. The Latin, Goldbacher 913-914, cuts the sentence on both sides. It leaves out "quapropter si potestate[m] quam per religionem ac [fidem] regum tempore, quo" (911-912). It also leaves out the main verb "coguntur intrare, non quia coguntur reprehendant, sed quo cogantur adtendant" (915-916).
- Supported: a Christian ruler's power used to compel separated groups back.
- Not supported by the span: "late" and "against his own earlier view". I verified this part elsewhere: Letter XCIII §17, npnf101_augustine-confessions-letters.xml lines 38245-38251, "originally my opinion was, that no one should be coerced into the unity of Christ". That locus has no lines.

**Meaning.** PASS.
**Fix.**
- Locus: "Letter 185, §24 (Chapter 6)".
- Latin span: 911-916.
- Add lines 38245-38251 to the Letter XCIII locus.

### 6. lpc.term.confessor: FAIL (P1)
**Span.** De Lapsis 2, anf05 43651-43656 and Latin 124-128, ends mid-sentence. "armed for the endurance of death" is on 43657, and "armati ad tolerantiam mortis" is on 129. The passage shows confessors held in honour, who resisted persecution and survived. The phrase "That religious voice has named the name of Christ" (43660) carries "kept faith when questioned".
- Supported: who a confessor is.
- **Not supported: "could rival a bishop."** This is the defining claim of `means` and appears in both meaning fields. The finder flagged it correctly, and nothing line-verified in the record carries it.

**Fix.** Add a passage that does carry it. I verified Epistle XVI, "The Confessors to Cyprian": anf05 30387-30391, from "Know that, to all" to "made known by you to the other bishops also"; Latin Hartel-Ep 3389-3391, "Scias nos uniuersos … aliis episcopis innotescere uolumus". In it the confessors announce that they *have granted peace* and instruct the bishop to publish this to his colleagues. That is the rivalry, in their own words. Ep. XIV, anf05 30198-30207, adds Cyprian's side ("thousands of certificates were daily given").
- Extend the De Lapsis span to 43651-43660 and Latin 124-131.
- If no passage is added, narrow the meaning text:
  - `means`: "In Cyprian's time a confessor was one who kept faith when questioned, lived, and was held in honour."
  - `plain_meaning`, second sentence: "In Cyprian's time, the church held that standing in high honour."
  - `quick_meaning`, second sentence: "In Cyprian's time, the church held them in high honour."

### 7. lpc.term.grace: PASS
**Span.** npnf105 10082 is Proceedings of Pelagius ch. 34 (confirmed). It holds "we certainly do not deserve by any faith that we should have faith itself; but, in its bestowal upon us … 'His mercy has prevented us.'" This supports both halves of `means`: our own effort is not enough, and the good was given first. Optional: extend to 10085 ("Did we ourselves make ourselves faithful? … It is He that hath made us"). The one-voice hedge is kept in the confidence block.
**Meaning.** PASS. All sentences are 23 words or fewer.

### 8. lpc.term.heresy: FAIL (P2)
**Span.** npnf104 10829-10830 holds "as the baptized person, if he depart … does not lose … For neither sacrament may be wronged." This supports only that baptism is not lost through separation.
- Not supported by the span: "truly given but did no good there". That is the sentence just before it, 10827-10828: "it is not indeed rightly given, but yet it is given … that which without it was given to no profit".
- Not supported by the span: "Cyprian's council said no". The 256-council locus has no lines. I verified the passage: anf05 56858-56864, "Cyprian said: You have heard … heretics who come to the Church must be baptized and sanctified by the baptism of the Church"; Latin sententiae episcoporum 112-117.

On the finder's note: they are right that the council ruling is not in the cited passage. It is in the same council preface the record already cites, so this is P2, not P1.
**Meaning.** "truly given" can be heard as "rightly or properly given", which is the very word Augustine denies ("not indeed rightly given"). The `means` sentence is also at the 25-word ceiling and holds three thoughts.
**Fix.**
- Augustine span: 10827-10830. Add the council span above.
- `means`: "The word asks if baptism outside the church counts. Cyprian's council said no; Augustine said it was given, though it did no good there."

### 9. lpc.term.libellatici-sacrificati: FAIL (P2)
**Span.** Ep. LI 13, anf05 33676-33679 and Hartel-Ep 7837-7840, holds "those who receive certificates are [not] to be put on a par with those who have sacrificed". It supports the split and "not alike". The locus also quotes §17 ("libellaticos interim admitti, sacrificatis in exitu subueniri"), but no span covers it. §17 is what carries "both fallen", because both groups need the church's peace.
**Meaning.** PASS.
**Fix.** Add §17: anf05 33780-33784, from "And therefore it was decided" to "in the place of the departed"; Latin Hartel-Ep 7978-7981.

### 10. lpc.term.libelli: FAIL (P2)
**Span.** De Lapsis 27, anf05 44357-44360 and Latin 1028-1030, holds only the first sentence: they "have defiled their conscience with certificates" and must still repent. That supports "Cyprian still held them fallen". Three claims sit just outside the span:
- "said you had made the pagan offering" and the plain "called that paper a denial". Lines 44362-44365 hold "That profession of one who denies … He says that he has done what another has actually committed". The Latin continues across a page break at 1048-1049, "est christiani quod fuerat abnuentis. fecisse se dixit …".
- "bought". This is in Ep. LI 14, anf05 33696-33716 ("I pay a price for this purpose … although his hand is pure … yet his conscience is nevertheless polluted"). The Latin ends at Hartel-Ep 7880-7887 ("dare me ob hoc praemium").
- The De Lapsis 28 quotation in the locus is at Latin 1071, but no span covers it.

**Meaning.** PASS. "Holding that paper" in `quick_meaning` is acceptable.
**Fix.** English 44357-44365; Latin 1028-1030 and 1048-1049. Add the Ep. LI 14 lines above to the Ep. LI locus.

### 11. lpc.term.plenary-council: FAIL (P2)
**Span.** The English, npnf104 11302-11303, is good. The Latin, Migne PL43 7942-7945, starts on "giones ve[l] provincias", the second half of a word split across a page. The clause begins "et ipsa concilia quae per singulas re-" on line 7926.
**Meaning.** PASS. `means` and `quick_meaning` say no more than the passage, and "when experience brings to light what was hidden" keeps Augustine's condition.
**Fix.** Latin: 7926-7945.

### 12. lpc.term.preaching: FAIL (P1)
**Span.** Sermon I.1, npnf106 9398, holds a regular address to an assembled, willing congregation. That supports "the regular talk to the … church".
- Not supported: "to the whole church, baptized or still learning".
- **Not supported anywhere: "the main way its teaching reached plain believers".** The finder flagged this correctly. "Main way" comes from the build's own Doc_05 finding, which is analytic reasoning and not a source. No cited source says it.

**Fix.**
- Add the verified passage Sermon LXXXII (Ben. 132) §1: npnf106 lines 20038-20039, from "For those of you who have been baptized and the faithful" to "Accordingly our discourse is directed to both." This carries "baptized or still learning".
- `means`: "Preaching was the bishop's regular talk to the whole gathered church, the baptized and those still learning."
- `quick_meaning`: "For us, preaching is the regular talk to the whole church, baptized or still learning. It is how our bishop speaks to all of us at once."
- `plain_meaning` can stand.

### 13. lpc.term.reconciliation-penitential-discipline: FAIL (P2)
**Span.** Epistle IX 2, anf05 29771-29775, opens on the endnote ("'Exomologesis.'"). It leaves out the first half of the very words the locus quotes, "do penance for a set time, and according to the rules of discipline come to public confession" (29768-29770). It also ends mid-sentence. The Latin, Hartel-Ep 2568-2569, likewise leaves out "nam cum in minoribus peccatis agant peccatores paenitentiam iusto tempore, et secundum disciplinae ordinem ad" (2566-2567).
- Supported once the span is corrected: all of `means` (public, in stages, bishop and clergy, return to communion).
- Note: Cyprian is stating the rule "in smaller sins". `means` does not misstate this.

**Meaning.** PASS.
**Fix.** English 29767-29778, from "For although in smaller sins" to "the eucharist is given to them". Latin 2566-2569.

### 14. lpc.term.schism: FAIL (P1)
**Span.** De Unitate 17, anf05 42698-42701 and Latin 901-903, starts mid-sentence. It leaves out the clause the locus quotes, "who separates himself from the company of His clergy and people" (42694-42695; Latin 898). It ends before the sentence closes at 42706 (Latin 906).
- Supported: leaving clergy and people, and setting up another altar. This is all of `quick_meaning`.
- Not supported by any cited passage:
  - "when arguing stops", in `means` and `plain_meaning`. This is the build's contrast with the 256 preface, which is not a source of this record.
  - "a separate … bishop".
  - "in the same town", in `means` and `plain_meaning`.
- The contested-claim note says the entry must not present the distinction as settled. "When arguing stops" builds a particular account of the distinction into the definition.

**Fix.**
- Spans: English 42693-42706, Latin 897-906.
- Add De Unitate 10, verified: anf05 42458-42462, "who appoint themselves prelates without any law of ordination, who assume to themselves the name of bishop, although no one gives them the episcopate"; Latin 547-550. This carries the rival bishop.
- `means`: "Schism is the tear made when someone leaves the church's bishop, clergy and people, and sets up another altar and another bishop."
- `plain_meaning`: "We argue hard, and we stay. Schism is the other thing: someone walks out, and sets up a new altar and a new bishop."
- If "in the same town" is wanted, add Ep. LI 8 as a cyprian-epistles source, verified: anf05 33584-33592, "as after the first there cannot be a second, whosoever is made after one who ought to be alone, is not second to him, but is in fact none at all"; Latin Hartel-Ep 7699-7706.
- If "We argue hard, and we stay" is kept, add the 256 preface as a source (anf05 56868-56871).

### 15. lpc.term.suffrage: FAIL (P2)
**Span.** Ep. XXXIX, anf05 32372-32373 and Latin Hartel-Ep 5904-5906, holds "against my episcopate, that is, against your suffrage and God's judgment". That supports the people's voice joined with God's judgment as what made him bishop.
- Not supported by the span: "even against his wishes". The finder is right. The cited Pontius locus does carry it, but has no lines. I verified Pontius §5, anf05 27826-27840: "he humbly withdrew, giving place to men of older standing … A crowd of the brothers was besieging the doors of the house … he desired [to be] let down through a window".
- The phrase-level English span is acceptable for a quoted phrase. Note, though, that the full sentence runs 32369-32375.

**Meaning.** PASS. "voice of the people" avoids the modern franchise sense that the record flags.
**Fix.** Add "anf05 lines 27817-27840" to the Pontius locus. No change to the meaning text.

### 16. lpc.term.the-flock: FAIL (P2)
**Span.** Ep. LIV 14, anf05 35009-35011 and Hartel-Ep 10115-10117, holds "a portion of the flock has been assigned to each individual pastor, which he is to rule and govern, having to give account of his doing to the Lord".
- Supported: "the particular people given to one bishop in one place, for whom he answers".
- Not supported by the span: "who can hold him to it". The Letter CXXVI locus carries this, but has no lines. I verified npnf101 44486-44507: the Hippo crowd "in front of the steps, … persisting … with terrible and incessant clamour". That crowd was pressing Augustine to ordain Pinianus, so "hold him to it" reads more into it than the letter says.
- The Epistle V quotation in the locus has no span.

**Meaning.** `plain_meaning` has a 28-word sentence: "The charge runs both ways: he answers for his flock, and his flock can stand in front of his seat and refuse to leave until he hears them."
**Fix.**
- Add npnf101 lines 44486-44507 to the Letter CXXVI locus.
- `means`: "The flock is the particular people given to one bishop in one place, for whom he answers and who can press him face to face."
- `plain_meaning`, last sentence: "The charge runs both ways. He answers for his flock. And his flock can stand before his seat and refuse to leave until he hears them."

### 17. lpc.term.the-lapsed: FAIL (P2)
**Span.** anf05 33453-33455 and Hartel-Ep 7487-7488 hold the right content: "those who have stained their conscience with certificates, or have offered abominable sacrifices, are to have peace made easy to them". But this is **Epistle LI 3** (to Antonianus). The locus text names "Epistles XX-XXI, two lay confessors' own first-person voices", so the locus describes a different passage from the one its lines point to.
- Supported: gave way by sacrifice or by certificate, and the question of their peace.
- Not supported by the span: "bought" (see Ep. LI 14 in term 10).

**Meaning.** `plain_meaning` opens with a 31-word sentence.
**Fix.**
- Rewrite the locus as "Epistle LI 3 (to Antonianus) … anf05 lines 33453-33455; Latin Hartel-Ep 7487-7488". Keep the Epistles XX-XXI description separate and without lines.
- `plain_meaning`, first sentence: "The lapsed are our own people who obeyed the order to sacrifice during the persecution. Some sacrificed. Others only paid for a certificate that said they had."

### 18. lpc.term.the-one-episcopate: PASS
**Span.** English anf05 42290-42291 and Latin 339-340 begin and end exactly on "The episcopate is one … for the whole" and "episcopatus unus est … pars tenetur." The recension caution is kept.
**Meaning.** PASS. "On behalf of the whole" in `quick_meaning` is a fair plain rendering of *in solidum*, given the ANF's "for the whole".

### 19. lpc.term.the-people: FAIL (P1)
**Span.** The locus says "Letter CXXVI … cites 'the love of Valerius and the importunity of the people'", with the span npnf101 44502-44507.
- **That quotation is not in Letter CXXVI.** It is Letter XXXI §4 (to Paulinus and Therasia), npnf101 lines 25850-25858: "persuaded, through the love of Valerius and the importunity of the people, that it was the Lord's will". The span 44502-44507 holds the Hippo crowd episode instead.
- The span also starts mid-sentence. "I said, moreover" is on 44501, and the episode itself begins at 44486.

**Meaning.** "We put men into office" and "they elect" rest on Letter XXXI and Ep. XXXIX. Neither has a span in this record. Once the loci are corrected, the meaning text stands.
**Fix.** Split the Augustine locus into two:
- "Letter CXXVI 1, the Hippo crowd: npnf101 lines 44486-44507"
- "Letter XXXI 4, 'the love of Valerius and the importunity of the people': npnf101 lines 25850-25858"

Optionally add Ep. XXXIX: anf05 32369-32375, Latin Hartel-Ep 5902-5908.

---

## Part B: lpc.story.election-of-cyprian

### Spans
- **Pontius §5, anf05 27815-27849:** correct. It begins on "It would be tedious" and ends on "a mind so retentive?". It holds the judgment-of-God-and-favour sentence (27817-27821), "untaught season" (27821-27825), the withdrawal and the crowd at the doors (27826-27840), and "Some resisted him" (27844).
- **Ep. XXXIX, anf05 32370-32374:** FAIL (P2). It starts mid-sentence: the subject, "the malignity and treachery of certain of the presbyters", is on 32369. It ends mid-sentence: "with their / accustomed craft." runs to 32375. Correct to **32369-32375**. The letter's heading, "To the People, Concerning Five Schismatic Presbyters", with the editor's date "A.D. 251", is at 32346-32350.
- **Ep. LXVII, anf05 37563-37568:** FAIL (P2). It ends mid-sentence on "by the sentence of the bishops who". The sentence closes "in the place of Basilides." on 37571. Correct to **37563-37571**. The passage does support the cross-check: choice "in the presence of the people" and "by the suffrage of the whole brotherhood".

### Sentences in `text` / `telling` that rest on none of the cited lines
1. `text`, sentence 1, and `telling`, sentence 1: "Our [own] deacon Pontius". Pontius is not named a deacon in §5. The name appears only in the work's title line, anf05 27661, "By Pontius the Deacon".
2. Same sentences: "after Cyprian had been executed" / "after Cyprian had been put to death". Nothing in §5 says this. Pontius's execution narrative is §18, anf05 28260-28267.
3. `text`, last paragraph, "years afterward", and `telling`, "Years later". No cited line dates Ep. XXXIX or the election. The editor's date for Ep. XXXIX is at 32349-32350 (A.D. 251), which is about two to three years after 248/249.
4. `telling`: "Cyprian answered them in a letter to us." The addressee, the people, is in the heading at 32346. That line is outside the cited span. "your suffrage" only implies it.
5. Interpretive sentences that rest on the build's reading rather than a line. They are acceptable as voice, but no cited line states them: "The second is how the first became visible to us" (`text`), "The people's favour was how God's judgment became visible to us" (`telling`), and "What we saw in him was not training. It was something we thought we could already see." (`text`). The nearest support is 27821-27827 ("untaught … a generous disposition so shone forth"; "the entire people by God's inspiration leapt forward").

**Fix.** Add a Pontius locus for the title line and §18: anf05 27661 and 28260-28267. Optionally add §1, 27664-27677. Extend Ep. XXXIX to 32346-32350 plus 32369-32375. Extend Ep. LXVII to 37563-37571.

### Other defects found in the story record
These are outside the strict brief, but they are relevant to "no commentary in live files".
- The `events` entry "Cyprian stepped back from the office; the people pressed him" still says `rests_on: 'the reviewed telling only …'`. That is now stale, because Pontius §5, lines 27826-27840, carries it directly.
- The prose under the front-matter ("Derived from Story-Chunks/… line 27820 … through 27823 … is this record's own addition, … not in the chunk") is process narration inside a canonical `records/` file. It also contradicts the new locus (27815-27849). It should be removed per the CLAUDE.md live/canonical rule. I have flagged it only and did not touch it.

---

## Failed term ids
P1: lpc.term.confessor, lpc.term.preaching, lpc.term.schism, lpc.term.the-people.
P2: lpc.term.bishop-of-bishops, lpc.term.catechesis, lpc.term.certificates-letters-of-peace, lpc.term.communion, lpc.term.compel-them-to-come-in, lpc.term.heresy, lpc.term.libellatici-sacrificati, lpc.term.libelli, lpc.term.plenary-council, lpc.term.reconciliation-penitential-discipline, lpc.term.suffrage, lpc.term.the-flock, lpc.term.the-lapsed.
Story: lpc.story.election-of-cyprian, FAIL (P2).

---

## Round 2 recheck

Date: 2026-11-01. Reviewer: independent (Opus 5.5), not the worker who applied the fixes. Targeted recheck of `git diff -- records/lpc/term records/lpc/story` against the round 1 findings above. Every changed or added span was opened in `cic/texts/` with its ThML tags and endnotes folded. All 19 changed files parse as YAML.

Span standard used: the first line of a span holds the first word of the passage the locus quotes or relies on, and the last line holds its last word. A span that holds the whole relied-on passage but cuts a longer sentence is noted as advisory, not failed.

### Result
**Terms: 12 PASS, 5 FAIL. Story: FAIL.**

| Term | R2 | Note |
|---|---|---|
| bishop-of-bishops | PASS | 56871-56884 and Latin 140-147 hold the headword clause through "judging us in our conduct there" / "iudicandi". |
| catechesis | PASS | 24020-24028 and 30467-30478 start and end on the passage. New `means` is 19 words and stays inside the On the Creed sermon to catechumens. |
| certificates-letters-of-peace | **FAIL** | See below. |
| communion | PASS | Latin 121 + 138-139 correct. Ep. IX 2 (29767-29773; Latin 2566-2569) carries "given back". |
| compel-them-to-come-in | PASS | See worker's extra changes. |
| confessor | **FAIL** | See below. |
| heresy | PASS | 10827-10830 holds "not indeed rightly given, but yet it is given … given to no profit". Council 56858-56864 / Latin 112-117 exact. New `means` fixes "truly given". Open finding outside round 1 scope: see below. |
| libellatici-sacrificati | PASS | §17 at 33780-33784 / Latin 7978-7981 holds "libellaticos interim admitti, sacrificatis in exitu subueniri". |
| libelli | **FAIL** | See below. |
| plenary-council | PASS | Latin 7926-7945 holds the quote. Advisory: the Latin sentence, with the "experience" condition that `plain_meaning` uses, closes at 7951. |
| preaching | PASS | 20038-20039 is exact. New `means` (17 words) and `quick_meaning` drop "main way" and add nothing the two sermons do not carry. |
| reconciliation-penitential-discipline | PASS | 29767-29778 / Latin 2566-2569 exact. |
| schism | PASS | 42693-42706 / Latin 897-906, and De Unitate 10 at 42458-42462 / Latin 547-550, exact. New `means` (23 words) and `plain_meaning` drop "same town" and "when arguing stops". Open finding outside round 1 scope: see below. |
| suffrage | PASS | Pontius 27817-27840 carries "even against his wishes". Advisory: 27840 ends inside the window sentence ("had he also been equal"), which closes on 27841. |
| the-flock | **FAIL** | See below. |
| the-lapsed | **FAIL** | See below. |
| the-people | PASS | Locus split is correct. Letter XXXI quote is inside 25850-25858. Advisory: the sentence opens on 25849 ("But I beg to") and closes on 25859 ("appointments."). |

### The worker's three changes beyond the review
1. **compel-them-to-come-in, `senses.evidential` "SS25-26" changed to "SS24": correct.** §24 is paragraph v.vi.viii-p22 (npnf104 line 19606). §25 opens Chapter 7 at 19624. This keeps the sense consistent with the corrected locus. No other "SS25-26" remains in the record.
2. **libelli, Ep. LI 14 Latin given as 7855-7887 instead of round 1's 7880-7887: correct, and better than round 1.** Round 1's 7880 starts mid-plea ("uenire non posse"), and that cut leaves out "ad aras diaboli me" (7861). Line 7855 ("qui sacrificauerint iungere, quando is cui libellus acceptus est") matches the English start at 33696. Line 7887 closes the section ("paratus sit contestatur").
3. **schism, 256 preface Latin borrowed as 121 and 138-139: correct.** Line 121 ends "superest ut de hac ipsa" and 138-139 run "re singuli … si diuersum senserit amouentes." That is the Latin of English 56868-56871. Round 1 offered this source for "We argue hard, and we stay", and the Latin is the right pair for it.

### Failed records: exact corrections

**certificates-letters-of-peace (P2).** Two of the added spans leave quoted words outside.
- Ep. XVI: the locus quotes "to all, concerning whom". "Know that, to" is on 30386, so the span starts one word into the quote.
- Ep. XIV Latin: line 3010 ends "contra euangelii", and "legem" is on 3011.

In the locus, replace `30387-30391 (Epistle XVI)` with `30386-30391 (Epistle XVI)`. Replace `3010 (Epistle XIV)` with `3010-3011 (Epistle XIV)`. The meaning text is unchanged and passes. The new `plain_meaning` sentence is 15 words and is supported by 29937-29939.

**confessor (P1 closed, P2 open).** Ep. XVI (30387-30391 / Latin 3389-3391) does carry "could rival a bishop": the confessors grant peace and direct the bishop to make it known. So the P1 is closed. The De Lapsis span still starts after the quote begins. The locus quotes "We look with glad countenances upon confessors", and those words open on line 43650. Line 43660 also stops at "in whom". The "kept faith" clause closes on 43661 ("it has once confessed that it believed"), and its Latin "est, in quem se semel credidisse confessa est" is on 142.

In the De Lapsis locus, replace `lines 43651-43660; Latin at cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt, lines 124-131` with `lines 43650-43661; Latin at cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt, lines 124-131 and 142`. For consistency, also replace the Ep. XVI `lines 30387-30391` with `lines 30386-30391`.

**libelli (P2).** The De Lapsis locus quotes De Lapsis 28 ("nullo sacrificii aut libelli facinore constricti") and then says "verified directly against" lines that hold only §27. The §28 words are at English 44392-44394 and Latin 1070-1071, which no span covers. Round 1 flagged this, and it is not fixed.

In the De Lapsis locus, replace `lines 44357-44365; Latin at cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt, lines 1028-1030 and 1048-1049` with `lines 44357-44365 (section 27) and 44392-44394 (section 28); Latin at cic/texts/cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt, lines 1028-1030 and 1048-1049 (section 27) and 1070-1071 (section 28)`. The Ep. LI 14 span and the meaning text pass.

**the-lapsed (P2).** Round 1 found "bought" unsupported. It is still in `means` ("by a bought certificate") and in the new `plain_meaning` ("Others only paid for a certificate"). No locus in this record carries it. The Ep. LI 3 locus fix is correct (33453-33455 / 7487-7488), and the new `plain_meaning` sentences are 15, 2 and 9 words.

In the lpc.source.cyprian-epistles locus, before `. The same correspondence includes Epistles XX-XXI`, insert: `; Epistle LI 14 -- the plea of one who obtained a certificate, 'I pay a price for this purpose'; verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 33696-33716; Latin at cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt, lines 7855-7887`.

**the-flock (P2).** Round 1 found "who can hold him to it" reads more into Letter CXXVI than it says. `means` was fixed, but the same phrase is still in `quick_meaning` (line 122). The new `means` (25 words) and the new `plain_meaning` sentences pass, and 44486-44507 is exact.

Replace `quick_meaning` with: `For us, the flock is not the church in general. It is the particular people one bishop is given, in one place. He answers for them, and they can press him face to face.`

### Story: lpc.story.election-of-cyprian: FAIL (P2)
**Spans.** All pass.
- 27815-27849 is all of §5.
- 27661 is "By Pontius the Deacon."
- 28260-28267 is the execution: "accomplish the death of the excellent man".
- 32346-32350 holds the title "To the People, Concerning Five Schismatic Presbyters" (in the div3 heading) and the editor's "a.d. 251".
- 32369-32375 opens on "malignity and treachery of certain of the presbyters" and closes on "accustomed craft."
- 37563-37571 closes on "in the place of Basilides."

**Round 1's five unsupported items.**
1. "deacon": now cited, line 27661.
2. "after Cyprian had been executed / put to death": now cited, §18.
3. "years afterward" / "Years later": **not fully fixed.** The span now dates Ep. XXXIX to 251, but no cited line dates the election. Pontius §5 gives no year. The 248 date is only in the ANF editor's introductory notice (27520-27526, "(a.d. 248)"), which is not cited. The phrase also appears in `events` and `telling_short`.
4. "a letter to us": now cited, heading at 32346.
5. The interpretive sentences: see the last paragraph of this section.

**Fix for item 3.** Pick one option.
- (a) Cite the editor's notice. Use a source record that covers the ANF editorial matter if one exists; none is in `records/lpc/source/`. Add the locus `the editor's introductory notice to Cyprian, 'the popular urgency constrained him to accept the office of Bishop of Carthage (a.d. 248)'; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 27520-27526`.
- (b) Narrow the wording to what the cited lines carry: Ep. XXXIX's "ancient venom" and "renew their old attack", written while he was already bishop. Make these replacements:
  - `text`: `and years afterward, writing` becomes `and later, writing`.
  - `telling` and `telling_medium`: `Years later, rivals` becomes `Later, rivals`.
  - `telling_short`: `Years later, answering rivals` becomes `Later, answering rivals`.
  - `events` line: `Years later, against rivals` becomes `Later, against rivals`.

**The three interpretive sentences are not marked or tagged anywhere as the build's own reading.**
- `claim_guards` is `[]`.
- `absent_detail` covers only the neophyte claim and Pontius's praise.
- `formation_confidence` is Documented for the whole record.
- The `events` entry "For Pontius, the people's favour was how God's judgment became visible" is marked `essential: true`. Its `rests_on` cites the record's own `text` ("The second is how the first became visible to us"), not a source line.
- `heart` repeats the reading as the reason the story is kept.
- `telling` and `telling_medium` frame it as Pontius's view ("For Pontius, …"). Pontius §5 states the pairing ("by the judgment of God and the favour of the people") but not this relation between its two parts.

This is outside what was edited and is reported for decision, not as part of this verdict.

**Other defects (flagged, not part of the verdict).**
- The round 1 note on the stale `events` `rests_on: 'the reviewed telling only …'` for "Cyprian stepped back" is unaddressed. It can now cite 27826-27840.
- The process-narration paragraph under the story front matter was edited (its line numbers were updated) instead of removed. That runs against the CLAUDE.md live/canonical rule. The same rule applies to the "Re-derived from …" / "Derived from …" paragraphs in every edited term record, since a PR that edits these files must remove their commentary.

### New findings outside round 1 scope (open; log them, do not let them go quiet)
Round 1 reviewed `means`, `plain_meaning` and `quick_meaning`. The same defects it fixed there are still in unedited `senses` fields:
- **schism `senses.informational`:** "when the arguing stops being argument and becomes a separate altar, a separate bishop, a separate people in the same town." This is the claim removed from `means` as unsupported, and it builds one account of the contested distinction into the definition. Suggested: `Schism is the other thing: someone walks out, and sets up another altar and another bishop.` `senses.translational` "in a town where both parties are present" rests on the same uncited premise.
- **heresy `senses.informational`:** "what was given outside was truly given". This is the wording round 1 found misleading against "not indeed rightly given". Suggested: `what was given outside was given, though not rightly, and does no good where the person stands`.

### Failed ids
lpc.term.certificates-letters-of-peace, lpc.term.confessor, lpc.term.libelli, lpc.term.the-lapsed, lpc.term.the-flock; lpc.story.election-of-cyprian.

## Cap-exception read

Date: 2026-11-01. Reviewer: independent (Opus 5.5). This is Mark's one-time cap exception, not a new round. It is a targeted read of the round 2 corrections, which were applied unread. Records read at HEAD of `claude/lpc-term-spans`; the story read from the working tree. Every cited span was opened in `cic/texts/` with tags and notes folded.

### Result
**12 items: 9 PASS, 3 FAIL.**

| Item | Verdict | Note |
|---|---|---|
| certificates-letters-of-peace | PASS | 30386 holds "Know that, to"; 30389 closes "we have granted peace". Latin 3010 "contra euangelii" / 3011 "legem". |
| confessor | PASS | 43650 opens "We look with glad countenances upon"; 43661 closes "it has once confessed that it believed". Latin 124 opens "Confessores"; 131 "religiosa uox Christum locuta", 142 "est, in quem se semel credidisse confessa est". Ep. XVI 30386-30391 as above. |
| libelli | PASS | §28: English 44392-44394 ("28. Moreover ... bound by no crime of / sacrifice to idols or of certificate"); Latin 1070-1071 ("Denique ... nullo sacrificii aut libelli facinore constricti"). |
| the-lapsed | PASS | Ep. LI 14 clause inserted as specified. 33696-33716 holds the libellaticus's plea from "when he by whom the certificate has been received" to "prepared."; "I pay a price for this purpose" is on 33709. Latin 7855 "quando is cui libellus acceptus est" to 7887 "paratus sit contestatur"; "dare me ob hoc praemium" on 7880. The plea joins the received certificate to the price paid, so "bought" (`means`) and "paid for" (`plain_meaning`) now rest on a cited line. Advisory: "a certificate that said they had" rests on De Lapsis 27 ("He says that he has done what another has actually committed", 44363-44364), which this record's De Lapsis locus cites without lines. |
| the-flock | PASS | `quick_meaning` matches the prescribed text exactly. Sentences 10, 12, 12 words. |
| schism `senses.informational` | PASS | "someone walks out, and sets up another altar and another bishop" rests on De Unitate 17 (42693-42706) and 10 (42458-42462). "same town" is gone. 15 words. |
| schism `senses.translational` | PASS | The uncited "a town where both parties are present" is removed; nothing added. Advisory: the sentence is 29 words. |
| heresy `senses.informational` | **FAIL** | Wording is right against 10827-10830 ("not indeed rightly given, but yet it is given"; "given to no profit"). But the edited sentence is now 46 words. |
| story: "Later" | PASS | `text`, `telling`, `telling_medium`, `telling_short` and the `events` line all read "Later"/"later"; no "Years later" remains. Advisory: `years: {from: 248, to: 251}` still carries the uncited 248. |
| story: "For us" | **FAIL** | Applied only to `telling_short`, `telling_medium` and the `events` line. It doubles "us" there. `telling` and `text` still give the relation and the non-tension as Pontius's view, which the new claim guard forbids. |
| story: new `claim_guards` entry | **FAIL** | Content is right and the tag is right. Its second sentence is 52 words. The record's own `telling` and `text` break it (see the row above). |
| story: `events` rests_on | PASS | "our own reading (Inferential-Thin); Pontius section 5 gives the pairing ... not this relation between them" is accurate against 27817-27821. |

### Exact corrections for the three FAILs

**heresy `senses.informational`.** Replace `The other answer, a century and a half later, from a man arguing against that very ruling: what was given outside was given, though not rightly, and does no good where the person stands; bring them in, and what they already carry will begin to work.` with `The other answer came a century and a half later, from a man arguing against that very ruling. What was given outside was given, though not rightly, and does no good where the person stands. Bring them in, and what they already carry will begin to work.`

**story "For us".**
- `telling_short` and `telling_medium`: `For us, the people's favour was how God's judgment became visible to us.` becomes `For us, the people's favour was how God's judgment became visible.`
- `telling`: `For Pontius, God's judgment and the people's favour were not two claims pulling against each other. The people's favour was how God's judgment became visible to us.` becomes `Pontius names God's judgment and the people's favour together. For us, the people's favour was how God's judgment became visible.`
- `text`: `Two things are claimed at once in that sentence, and for Pontius they are not in tension: the judgment of God, and the favour of the people. The second is how the first became visible to us -- and later,` becomes `Two things are named at once in that sentence: the judgment of God, and the favour of the people. For us, the second is how the first became visible. Later,` The rest of that sentence is unchanged. The `text` line "It was something we thought we could already see." stays, since the guard now marks it as our reading.

**story `claim_guards`.** Replace the entry with: `That the people's favour was how God's judgment became visible to us is our own reading (Inferential-Thin). Pontius section 5 pairs the two but does not state how they relate. Do not present that relation as Pontius's own statement. The same holds for any claim that for Pontius the two were not in tension. It also holds for the line about what we thought we could already see in Cyprian.`

### Still open, outside this read
- The `events` entry "Cyprian stepped back from the office; the people pressed him" still rests on "the reviewed telling only". It can cite Pontius §5, 27826-27840.
- The process-narration paragraphs under the front matter of the story and the edited term records remain (CLAUDE.md live/canonical rule).
