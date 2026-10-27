# Opus review of the honest-limit batch — 2026-10-27

Independent review of the nine records on `claude/honest-limits-batch` (PR 1178), run by an Opus reviewer from the files, read-only. Findings F1 to F14 are applied or answered in the commits that follow it on that branch; see the Decision-Log entry of the same date.

I reviewed the nine records on branch claude/honest-limits-batch against the vendored files in cic/texts/ and edited nothing. Two of the nine are not fit as written. For every quote and line number I don't flag below, I found the cited words in the vendored file and they match the line numbers given.

## 1. Verdicts

| Record | Verdict |
|---|---|
| don.limit.fate-of-those-who-end-their-own-lives | Fit with named changes (F1) |
| alx.limit.faith-alone-later-frame | **Not fit** (F2, F3) |
| alx.source.origen-comm-romans | Fit |
| pahc.limit.faith-alone-later-frame | Fit with named changes (F6, F7) |
| pahc.limit.assurance-and-the-dead | **Not fit** (F4) |
| pahc.quote.appointed-to-be-read use_note | Fit only if the record becomes `voice: analytic` (F8) |
| pahc.term.eucharistia sentence removal | Fit (F9) |
| syr.limit.what-must-one-do | Fit with named changes (F10) |
| desert.limit.origins-no-single-founder | Fit with named changes (F5, F11) |
| desert.source.jerome-life-of-paulus | Fit |

## 2. Findings

**F1. Blocking: don's absence claim is false.** `don.limit...:24-26` says "No Donatist text we have speaks to it", and `:38-39` says "Petilian II.17 is the only Donatist-voiced line close by".
- Augustine's *Contra Gaudentium* (c. 420, inside the window) quotes Gaudentius, the Donatist bishop of Thamugadi, at length. It is vendored in `augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt`.
- It opens with Gaudentius threatening "se ipsum in ecclesia... incendere" (to burn himself in his church), at line 73276.
- Augustine answers the Donatists' appeal to Razias (2 Maccabees 14) at I.31.36, line 75702.
- The world's own source record `don.source.augustine-contra-gaudentium` marks the work as unread.
- So a Donatist-voiced text on chosen death does exist. Finding 11 of the precedent review ("only Donatist-voiced line") missed it too.
- The fix must not voice Gaudentius's defence in a record that fires on suicide questions. Narrow the claim, and name the unread work in `why_sources`.
- Otherwise the record meets finding 11: no verdict, no condition, no crisis wording, and it does not quote Augustine's Judas-and-the-devil verdict.
- Petilian (npnf104:15887) and Optatus III.4 (optatus:2014, "cast themselves down headlong") check out.

**F2. Blocking: alx misreads Clement, Stromateis I.9.** At anf02:28313-28320 the people who "demand bare faith alone" refuse "philosophy or logic... natural science". The vine needing pruning is about learning, not good works. `alx...:28-30` turns this into a faith-against-works answer.

**F3. Blocking: alx leaves out Clement's strongest text on the question.** Paedagogus I.6 (anf02:19356-19368) says "those who have believed have life, what remains beyond the possession of eternal life? Nothing is wanting to faith, as it is perfect and complete in itself."
- Without it, the record reads Clement as one-sided against faith.
- It also contradicts the spoken "We have no word on how sure a person may feel" (`:33`) and the `why_sources` claim that "none addresses felt assurance" (`:35`). No search for assurance was done.

**F4. Blocking (safety-adjacent): pahc assurance slants against the faithful dead being with the Lord.** The world's own vendored texts say:
- 1 Clement 50 (anf01:2124-2127): "those who... have been made perfect in love, now possess a place among the godly, and shall be made manifest at the revelation of the kingdom of Christ".
- Polycarp, Philippians 9 (anf01:3489-3492): Ignatius, Paul and the apostles "are [now] in their due place in the presence of the Lord".
- 1 Clement 5 (anf01:687, 704): Peter "departed to the place of glory", Paul "went into the holy place".

The record leaves all of these out. It then gives Justin's rejection of "souls... taken to heaven" without Justin's main charge: those people denied the resurrection and "blaspheme the God of Abraham" (anf01:22127-22130). A grieving visitor would hear "our church rejected heaven at death". The first not_for line, "a claim that believers were taught their souls go to heaven at the moment of death", is contradicted by these same texts. Justin also says "some who are called Christians", not "teachers" (`:30`).

**F5. Blocking: desert misstates Jerome.** `why_sources` (`:32`) says Jerome "does not settle" the dispute. Jerome, citing Amathas and Macarius on Paul, writes: "this opinion has my approval also" (npnf206, within 29742-29757). The statement also leaves out that Jerome says the Elijah-and-John view goes "back too far", and that "partly true" means Antony gave the others "the necessary stimulus".

**F6. Should fix: pahc faith alone.**
- 1 Clement 32 says God "has justified all men" (anf01:1532). The record drops "all".
- Polycarp is quoting Ephesians 2:8-9; the record should say so.
- "We have no list of what a person must do" overclaims: the Didache's two ways is such a body of precepts.
- `why_sources` lists Irenaeus as both searched (ANF 1) and "not searched". I confirmed ANF 1, 7 and 8 have no "faith alone/only" across line breaks, so the Irenaeus half was covered.

**F7. Should fix: the four statements share one voice.**
- alx, pahc, syr and don open on near-identical frames ("We cannot answer in those words, because the argument that uses them came after us" against "We did not use those words, and the argument that uses them came after us").
- Three of them close on the same unprompted tail ("We have no word on how sure a person may feel/be"), added where the visitor didn't ask about assurance.
- CLAUDE.md treats a uniform generic voice as a fabrication risk.

**F8. Should fix: the 367 quote's guard.** See section 3.

**F9. Nit: eucharistia sentence removal is fine.** `pahc.contested.table-diversity` does not exist, so the removed sentence pointed nowhere. No meaning is lost: `divergence_note` and the `evidential` sense still carry the Justin-representativeness contest. But OG-42 says the contested record has "no verifiable text". The Didache, Ignatius and Justin do support it. Record it as an unbuilt contested_claim, not as unsupported.

**F10. Should fix: syr years.** The sources are Aphrahat only: Demonstration I (337) and XXII (345). `years: 337-373` has no source for 373; sibling `syr.quote.aphrahat-stone-foundation` uses 337. Use `{from: 337, to: 345}`.
- Demonstration I.3 order (npnf213:24618-24624), I.4 (24650-24660) and XXII.18 (28368-28380) all verified.
- "Then he is made perfect" leaves out "consummated". That is acceptable.
- Same assurance tail as F7.

**F11. Should fix: desert contradicts a sibling, and one not_for line forbids what the source says.** Piamun in Cassian XVIII.5 (npnf211:~42538) says the coenobite life "continued unbroken for a very long period up to the time of Abbot Paul and Antony". So not_for line 4 bars a claim the cited source makes. Sibling `desert.dw.apostolic` ("We did not claim an unbroken line back to the apostles for our way of life") is contradicted by that same passage. The sibling isn't this batch's content, so flag it to desert's thread rather than editing it.
- Verified: Piamun is the speaker of Conference XVIII (npnf211:~42384, "Abbot Piamun had received us").
- Verified: Jerome wrote in the Syrian desert in 374 or 375 (npnf206:29736).
- Verified: "Amathas and Macarius", exact.

**F12. Should fix: alx must say Origen comes to us through Rufinus.** The corpus map (`alexandria-catechetical.yaml:715-719`) says any record citing this text "must say so". The spoken "Origen said" doesn't, though not_for does.
- The Latin itself is verified: "sine operibus sola fide justificatus" and "pro hac sola fide" (origen...:13331-13337), and "indulgentia... non futurorum, sed praeteritorum criminum datur" (13414-13415).
- Rufinus's translation (c. 406-410) falls after the 400 window end. Origen's authorship (d. 254) falls inside it.

**F13. Should fix: Clement's Quis Dives Salvetur 27 is about the rich.** "Nor is by any means saved by trusting and believing that he shall be saved" (anf02:56877-56880) is about the prosperous, not "no one". "To know God" is not in 27-29.

**F14. Nits.**
- The alx and desert waiver bumps (`enforce.py` shelf-row +1 each) give "no row_id exists" as the reason, but the corpus-map rows do exist for both new source records. They follow the fleet convention, so this is not blocking.
- don `why_sources` is in first person with file paths. It is stripped from the package (`builders.py:719`), so it is harmless.
- The two lines in don's statement that open "I will not..." read as a rule spoken aloud.
- The body of `pahc.quote.appointed-to-be-read` still has process narration ("THIS QUOTE CORRECTED A CLAIM...") and says "line 68714" where the locus is 68817 (68817 is right). `check_live_commentary` reports 0 hits.
- Canon cells are all correct: F6-T for don and the pahc assurance record, F1-T for alx, pahc and syr faith/what-must-I-do, F3-I for desert (I checked these against `engine/canon/records/canon_question/`).
- Every source and nearest_material id exists.
- Every means line is one sentence, has at most 4 not_for lines, and doesn't open with an imperative.

## 3. Corrected text

**F1, don.** Statement:
> What do we teach about a person who ends their own life? I cannot give you an answer of ours. What survives in our own words holds no teaching on it, as far as I know. The nearest line of ours I know is Petilian's. He says that the traitor Judas perished by the rope. That is a charge made in a quarrel about traitors. It is not a teaching about the dead. Our enemies did write of men who threw themselves from cliffs. They wrote it to argue over who may be called a martyr. They were not speaking of anyone alive today. I will not pass a verdict on any person's death, and I will not set a condition on one.

In `why_sources`, replace the last two sentences with:
> Petilian II.17 is the nearest Donatist-voiced line found in what was read, and it speaks of a traitor. Not read for this record: Augustine's Contra Gaudentium (c. 420; Petschenig file from line 73262), which quotes the letters of Gaudentius, Donatist bishop of Thamugadi, written when he threatened to burn himself in his church rather than submit (I.1, line 73276); Augustine answers his appeal to Razias at I.31.36 (line 75702). Those letters are Donatist-voiced and concern chosen death under coercion, a martyr question; whether they say anything on the fate of the dead is unchecked. Also not read: the Monumenta 303-340 file. I did not search every volume.

Add an OG entry for reading Contra Gaudentium on this point.

**F2, F3, F12, F13, alx.** Statement:
> Were you taught that a person is saved by faith alone? Those are not our words; that argument came later. Clement taught that those who have believed already have life, and that nothing is lacking to faith. Yet he also told the rich that none of them is saved just by trusting that he will be saved. He told them to love God and their neighbour, and to do the Father's will. Origen, in his commentary on Romans, said the thief on the cross was justified by faith alone, without works. He added at once that forgiveness covers past wrongs, not new ones. We hold these together. We cannot say whether we would have taken up the later phrase.

- Replace the Stromateis source with `alx.source.clement-paidagogos`, locus "I.6 (anf02 lines 19356-19368): those who have believed have life; nothing is wanting to faith".
- In `why_sources`, describe Stromateis I.9 as "bare faith alone without learning (philosophy, logic), not faith without works". Replace "none addresses felt assurance" with "assurance was not searched".
- means: "The Alexandrian teachers said faith already holds life and lacks nothing, and also that love of God and neighbour and doing God's will are needed, and none of the texts read sets faith against works as a contest."

**F4, pahc assurance.** Statement:
> If you ask whether a believer who died today would go to heaven, we did not put it in those words. Our writers speak of the dead in two ways. Clement of Rome wrote that those made perfect in love now have a place among the godly. They will be shown when Christ's kingdom comes. Polycarp wrote that Ignatius, Paul and the apostles are now in their place with the Lord. And our writers hope for a rising. Ignatius wrote that the Father will raise up those who believe in Christ. Polycrates wrote that the great ones of Asia had gone to their rest and would rise when the Lord comes. Justin met some, called Christians, who denied the rising and spoke against the God of Abraham. They said souls are taken to heaven at death. He would not count them Christians, and his quarrel was over the rising. We will not name anyone's end for you.

- Add `pahc.source.first-clement` (50; anf01:2124-2127) and `pahc.source.polycarp-philippians` (9; anf01:3489-3492).
- means: "The record's writers say that those made perfect in love, and the martyrs, now have their place with the Lord, and they hope for a rising on the Lord's day, with no full account of the time between."
- not_for line 1: "a claim that these writers set a present place with the Lord against the rising, or the rising against it". Line 3: "a claim about where any person went after death, including anyone the visitor names".
- years: `{from: 80, to: 200}`.

**F6, F7, pahc faith alone.** Statement:
> Were you taught that a person is saved by faith alone? We did not use those words. First Clement says we are not justified by our own wisdom or works, but by the faith through which God has justified all people from the beginning. Its next chapter asks whether we should then grow lazy in doing good. It answers, God forbid. Polycarp, taking Paul's words, wrote that you are saved by grace, not by works, but by the will of God through Jesus Christ. The Teaching of the Twelve opens with two ways, one of life and one of death. The way of life begins with love of God and of neighbour. Our writers hold these side by side.

In `why_sources`, change "Not searched" to: "Tertullian (ANF 3-4), past the window's edge; Irenaeus sits in ANF 1 and was covered by the phrase search."

**F10, syr.** Set years to `{from: 337, to: 345}`. Delete the last sentence of the statement, or reword it in the world's own idiom of judgment: "Aphrahat leaves the reckoning to the judge."

**F5, F11, desert.** Statement:
> You ask who started us. No single man did, and the tellings we have do not agree. Antony is the one we remember best, and many call him the first. Jerome wrote of this from the desert of Syria. He says some reach back too far, to Elijah and John. He says the view that Antony was first is only partly true. Antony did not so much come first as stir the rest to follow. Two of Antony's disciples, Amathas and Macarius, said Paul of Thebes led the way, and Jerome agreed with them. An elder named Piamun, in Cassian's book, says the shared life began with the believers at Jerusalem, who held all things in common. He says it ran on unbroken to the time of Paul and Antony, and he traces the solitaries to those two. For life together under a written rule, we tell of Pachomius and the angel with the tablet. We cannot say which telling is right. None was written by someone who was there at the start.

- In `why_sources`, replace "does not settle it" with "sides with Amathas and Macarius for Paul ('this opinion has my approval also')".
- not_for line 3: "a claim that Paul of Thebes came first as historical fact, since it rests on what two disciples asserted and Jerome accepted".
- not_for line 4: "a claim that the unbroken line from Jerusalem that Piamun describes is historically established".
- Flag `desert.dw.apostolic` to desert's thread.

**F8, the 367 quote.** `use_note.years` means "the years it speaks from" (`schemas.py:360-362`). Setting 70-200 on a text of 367 states a false date to satisfy the gate. The means line also hands a 70-200 voice a post-window person, which the horizon gate misses only because it checks years and terms, not names. `schemas.py:355-358` says a post-window mention belongs only on an analytic record. The options, least bad first:
1. **Mark the record `voice: analytic` and drop the use_note** (recommended). The use-note-present gate covers voiced records only, so no waiver comes back. `pahc.force.selective-canonization` already carries the transmission fact for the voice. Run the reciprocity gate afterwards: `pahc.term.two-ways` and the force record both point to this quote.
2. Keep the quote voiced and change the years gate for etic transmission quotes. That is an engine and governance change, so it is Mark's call.
3. Keep it as written. Not acceptable: the field is false.
4. Remove the quote. That loses the correction it gives the force record.

## 4. Not verified
- The Greek behind Origen on Romans III (the Tura papyrus covers parts of it) is not vendored, so I can't say whether "sola fide" is Origen's own or Rufinus's.
- Gaudentius's own quoted words on Razias. I found Augustine's answers to them, not the quotations themselves.
- Ephrem's prose refutations and the Odes of Solomon, for syr.
- Readability scores (I did not run m7) and the m1/m9 gates.
- Letter 185 wording.
- `pahc.contested.ignatius-dating` contents.

## 5. Moving use_note.status to reviewed

Each of these is possible only after the named corrections are made and someone other than the author rechecks them.

| Record | Can move to reviewed? |
|---|---|
| don | Yes, after F1 (and only after the precipice-charge record is also rechecked, per OG-51) |
| alx limit | Yes, after F2, F3, F12, F13 |
| pahc faith alone | Yes, after F6 and F7 |
| pahc assurance | Yes, after F4. Given the safety exposure, the recheck should be a full one. |
| 367 quote | No. Make it analytic instead. |
| syr | Yes, after F10 |
| desert | Yes, after F5 and F11 |

The source records carry no use_note.
