# Opus final read of the three corrected limits — 2026-10-27

Third review round on the don, alx and pahc assurance limits, by a fresh Opus reader. Two blocking safety findings (D1, P1) were found; under the three-round cap they went to Mark, who ruled to apply the reader's exact corrections and order one more read by a fresh reader (`opus-honest-limits-read-4.md`).

Independent read of the three records. I edited nothing, made no model or network calls, and did not open canon/sealed_probes. I checked every locus against the vendored files in cic/texts/.

## 1. Verdicts

- **don.limit.fate-of-those-who-end-their-own-lives: NEEDS CHANGES (one blocking finding).** It should not move to reviewed.
- **alx.limit.faith-alone-later-frame: READY to mark reviewed.** Two optional fixes below.
- **pahc.limit.assurance-and-the-dead: NEEDS CHANGES (one blocking finding).** It should not move to reviewed.

This is the third review round. Under CLAUDE.md's three-round cap, the don and pahc changes should go to Mark as a cap ruling, not into a fourth self-run round.

## 2. Findings

**DON: records/don/honest_limit/don.limit.fate-of-those-who-end-their-own-lives.md**

**D1. Blocking (safety): the spoken text names a method and ties suicide to "the traitor" (lines 26-28).**
- The text says: "The nearest line is Petilian's. He says that the traitor Judas perished by the rope. That is a charge made in a quarrel about traitors."
- This record fires on suicide questions. "Perished by the rope" names hanging, which breaks the no-method rule.
- It also puts the visitor's question next to the figure of "the traitor." In the same work, Augustine uses exactly that link against the Donatists (npnf104 lines 16889-16891): "two especially vile and customary deaths… hanging and the precipice… the fellow-disciples of the traitor… Judas by hanging himself."
- A visitor who has lost someone this way can hear that link, even though the next sentence tries to separate it.
- The quote itself is accurate: line 15887, with "went and hanged himself" at line 15884. The problem is safety, not accuracy.

Exact corrected statement:
> What do we teach about a person who ends their own life? I cannot give you an answer of ours. In the words of ours that I know, there is no teaching on it. Our enemies charged some of us with seeking death to be counted as martyrs. That was a quarrel over who may be called a martyr. It was not a teaching about the dead. No verdict on any person's death is mine to give. No condition on one is mine to set.

Changes that follow from this:
- Add don.source.optatus-against-the-donatists (III.4, optatus_against-the-donatists.txt line 2014, which I verified) as the spoken source.
- Petilian can stay in `why_sources_cannot_answer`, as material that was read and not used.
- not_for line 46 can stay as it is.

**D2. Should fix: the account of what was searched misdescribes the Monumenta file (line 31-33), and a sibling record contradicts it.**
- The record says the Monumenta file's "only passages near the subject are an editor's note on Marculus and a quotation of Augustine, both written from outside."
- That file also holds the Passio Marculi itself, a Donatist text (Passio starts at line 874). At lines 1232-1276 it says the executioner pushed Marculus over the cliff, and that angels set his spirit "ad aeternas sedes" (in the eternal seats).
- It also holds the Passio Isaac et Maximiani. Both are cited in don.dw.not-a-death-wish, which is already marked reviewed.
- So the file does contain Donatist-voiced teaching on the fate of a martyr whose death opponents called self-inflicted.
- The spoken claim, "no teaching on it" (on suicide), still holds, because in their telling Marculus was pushed. The search account does not.

Replace the second and third sentences of `why_sources_cannot_answer` with:
> I read the Monumenta Vetera Donatistarum in cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt for any Donatist text on this question and found none. It holds Donatist martyr texts, the Passio Marculi and the Passio of Isaac and Maximian, which place their martyrs in heaven; the Passio Marculi says he was thrown from the cliff by his executioner, so it answers the charge of self-destruction rather than teaching on it. Its other passages near the subject, an editor's note and a quotation of Augustine, are written from outside.

**D3. Nit: the Petilian locus is wrong (line 18).** It says "Book II, chapter 17." In NPNF it is chapter 8, section 17, so it should read II.8.17.

**D4. Nit: two lines sound like rules read aloud (lines 28-29).** "No verdict on any person's death is mine to give. No condition on one is mine to set." This is acceptable, but it reads like a rule recited to the visitor. If you rework the statement anyway, consider a warmer phrasing in the world's own voice. It does not block.

**ALX: records/alx/honest_limit/alx.limit.faith-alone-later-frame.md**

Every locus checks out:
- **Paedagogus I.6:** anf02 lines 19366-19367.
- **Quis Dives 27:** lines 56877-56880, verbatim "nor is by any means saved by trusting and believing that he shall be saved". The love-of-neighbour and "will of My Father" passages fall in 28-29, inside 56873-56945.
- **Origen on Romans III (Rufinus's Latin):** "quis sine operibus sola fide justificatus sit" at line 13333, the thief at lines 13334-13339. "indulgentia namque non futurorum, sed praeteritorum criminum datur" is around line 13412.
- **Stromateis I.9 "bare faith alone":** line 28315.

The years (180-254) are honest and fall inside the window. The Rufinus caveat is handled correctly. The voice is distinct from pahc.limit.faith-alone-later-frame.

**A1. Should fix: one sentence slightly overstates (line 31-32).** "The phrase 'saved by faith alone' belongs to a later quarrel" comes right after Origen's own "sola fide." The Rufinus text also has "pro sola fide… fides tua te salvam fecit" (lines 13403-13405), which is close to the phrase. The quarrel is later; the words are not. Replace with:
> The quarrel over "saved by faith alone" came later. We cannot say whether we would have taken a side in it.

**A2. Nit: the list of what was found leaves out two Clement hits (line 33).**
- Stromateis V.6 has "clothed in faith alone" (anf02 line 41905). There, simple believers get a lesser abode than the gnostic.
- Another Stromateis passage has "apprehended by faith alone" (line 32187).
- Neither sets faith against works, so the conclusion stands. The list of what was found should still be complete.
- Separately, "merely" in "not saved merely by trusting" is not in the source.

**PAHC: records/pahc/honest_limit/pahc.limit.assurance-and-the-dead.md**

Every locus checks out:
- **1 Clement 50:** lines 2124-2127.
- **1 Clement 5:** lines 687 and 704.
- **Polycarp 9:** lines 3490-3491. Note that "[now]" is a word the translator supplied.
- **Trallians 9:** lines 6621-6623.
- **Justin, Dialogue 80:** lines 22127-22131.
- **Polycrates:** anf08 lines 72583-72585.

The years (80-200) match the Welborn range given in the source record.

**P1. Blocking (safety): the Justin passage reads as a verdict on a grieving visitor's belief (lines 38-40).**
- The text says: "they said souls are taken to heaven at death. He would not count them Christians."
- The visitor's question, as the record itself restates it, is "whether a believer who dies goes at once to heaven."
- A bereaved listener hears: the belief that my mother is in heaven now is not Christian.
- The patch "His quarrel was over the rising" is too abstract to undo that. It is also narrower than the source, since Justin also charges them with blasphemy against the God of Abraham.
- The passage pushes the answer away from "the faithful dead are with the Lord," which the brief forbids for this record.
- Justin's view already sits in not_for and the divergence note, so the spoken text does not need it.

Exact corrected statement:
> You ask whether a believer who dies goes at once to heaven. Our writers spoke of the faithful dead in two ways. Clement of Rome wrote that those made perfect in love, by God's grace, now have a place among the godly. They will be shown when Christ's kingdom comes. Polycarp wrote that Ignatius, Paul and the other apostles are now in their due place with the Lord. Our writers also hope for a rising. Ignatius wrote that the Father will raise up those who believe in Christ. Polycrates wrote that the great ones of Asia had gone to their rest and would rise when the Lord comes. How the time between death and that day is spent, we cannot lay out. We will not name anyone's end for you.

This also restores "by God's grace" from the source (line 2125). Without it, a grieving visitor can hear "made perfect in love" as a test their loved one had to pass.

**P2. Should fix: a format fault puts a line break inside the spoken text (line 41).** " We will not name" is indented one space more than the block. YAML keeps the extra indent, so the parsed statement ends `"...lay out.\n We will not name\nanyone's end for you.\n"`. I confirmed this with yaml.safe_load. The corrected text in P1 fixes it if written as normally wrapped lines.

**P3. Should fix: the last sentence of `why_sources_cannot_answer` is broken (line 43).** It reads "…before the rising in full, Assurance for a living person was not searched." Replace with:
> It cannot give their full teaching on the state of the dead before the rising. Assurance for a living person was not searched.

**P4. Nit: a not_for line has nothing to refer back to (line 54).** "Justin's rejection of that view": no earlier line in use_note says what "that view" is. Suggest:
> a claim that Justin's view in Dialogue 80 was the view of the whole network

## 3. What I could not verify

- **Augustine, Letter 185:** I confirmed it is in npnf104 (around line 19454 onward), but the record gives no line for it, so I could not tie the record's claim to a specific passage.
- **Hermas:** the claim that pahc.story.hermas-visions "carries no merit, penance-scale or afterlife geography" I did not check against the Hermas text.
- **Contra Gaudentium and the Monumenta 303-340 file:** I did not read for content. Both are honestly declared as unread. I confirmed the Contra Gaudentium line references (73262, 73276-73278 for the threat to burn, 75702 for Razias).
- **Greek:** no Greek of Clement or of Trallians is vendored. I accepted "believe in Christ" for "believe in Him" from the English, where "His Father" makes Christ the referent.
- **Readability:** I made no numeric readability scores. Every sentence in the corrected texts is under 25 words.
