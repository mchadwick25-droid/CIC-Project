# Recheck of the review fixes: Manichaeism

A targeted recheck of what `Fixes_Review.md` changed in `Outline.md` and `Source_Sheet.md` (diff from the commit that added `Review.md` to HEAD), against `Review.md` and the vendored sources.

## Verdict: FIX

Two MINOR fixes, both in working lines, not in story wording. Every story-facing line holds. The heart is whole, the beats run once and in order, and the plan lands at the ruled length. No reread of the story is needed after these two replacements.

## Each change, against its source

| Change | Source re-read | Holds? |
|---|---|---|
| Essence: "a few" / "the many" struck. Glosses: "the few who" / "the many who" struck. D Hearers row: "Those who lived" | BIR 29072-29085 (Siddiks; laymen); FIH 4878-4898 | Yes. Neither source gives numbers. No "few" or "many" is left for the ranks (line 72's "many in China" is B29). |
| Setting, Century: Adharban, Ardawan the last, Ardashir by the 13th year; no ruler named for 216; "Parthian" out. Place: "then ruled by Persia" struck. Cut first 25: "Keep Babylonia, in Mesopotamia." A1 extended | BIR 29094-29100; 12375-12376 ("whom I believe to be Ardawan the Last"); 11939, 12068; 12293-12295; 11735-11736 ("from the royal Persian house") | Yes. All cites land. Biruni's "I believe" is marked as his own. The outline names no house or empire for 216. |
| Beat 6: the 732 exemption restored ("though the foreigners from the West, whose own religion it was, might still keep it themselves"); Cut first 20 struck; "the Hu" out | CHI 6877-6886: "puisque c'est la religion indigène des Hou occidentaux et autres, s'ils la pratiquent personnellement, il ne faut pas leur en faire crime"; *Tong tien* 766-801, 6877 | Yes. It says no more than the order. Dropping "et autres" narrows the exemption but does not mislead. |
| Beat 2 / B6: "and he wrote his own scriptures, among them his gospel" | BIR 29061-29062 ("In his gospel ..."); 29112-29115 ("He composed many books, his gospel, the Shaburkan ...") | Yes. Cite right. The working note on 29090 says a little too much: see MINOR 2. |
| Beat 5: "a book answering their opponents' questions on the gospel and the Old Testament"; D row "Faustus's book" | NPNF 4314 (I.2, "brief and pointed replies to the captious objections of our adversaries"); 4338 and 4512 ("Do I believe the gospel?"); 4471 ("Do I believe the Old Testament?"); 4312 | Yes. Told in the narrator's words. The questions are the opponents', as Faustus sets them. |
| Beat 4: the Egypt writer struck to Cut first 29 (card, with its dispute); "Bahram had him killed"; Who tells it: ALX card only; Do not say row on Bahram | BIR 29119-29127 ("He gave orders to search for Mani ... It is well known that he killed Mani"); 29132-29138; ALX 24496-24498 | Yes. "Bahram had him killed" follows Biruni's sentence and stays inside his credit. The death "at the hands of the Persian king" (heart, What they faced) is kept. |
| Cut first 30, "Far to the east" (Leave out); Cut first 31 (three "says that" to "says"; "once he was found" to "found") | — | Yes. "A Chinese emperor's order" places it. No cut touches the heart, a witness, a reason or a quote. The record keeps its force: the exemption, the gospel, Faustus's book and the exile's cause all stay. |
| Four Do not say rows added | as cited | Three hold. The "a few" / "the many" row quotes words its source does not use: see MINOR 1. |
| Governing length: about 830 (Decision-Log item 2); the 725 ruling is marked superseded | `Review.md` header | Yes. |

## Heart and beats

The heart's only change is the essence's ranks sentence. Its substance is unchanged, and it is still told in the second paragraph, inside the first minute. The beats still run Babylonia, then the king and the books, Elect and Hearers, the death and the hunt, the West, and the East, in that order. No event falls in two beats. The exemption sits only in beat 6, and the Egypt writer is only in Cut first 29.

## Count

I applied every review change to a copy of the live `manichaeism.brief.txt` (838 by `wc -w`): the six BLOCKING fixes in this outline's wording, the MINOR changes word for word, and Cut first 29, 30 and 31. The copy also counts **838 by `wc -w`**. The profiler gives the brief 830, so the plan is about 830, as ruled.

## MINOR

1. **Do not say row, line 172.** It puts "the Elect ... the Hearers" in quotation marks and credits them to BIR 29072-29085. Biruni's words there are "the Siddiks" and "the Sam^na' (laymen)". Replace:
   `| "a few" / "the many" for the Elect and Hearers | no held source gives their numbers: "the Elect ... the Hearers" (BIR 29072-29085; FIH 4881-4898) |`
   with:
   `| "a few" / "the many" for the Elect and Hearers | no held source gives their numbers: Biruni names the two ranks, "the Siddiks" and the laymen, with no count (BIR 29072-29085), and so does the Fihrist (FIH 4881-4898) |`

2. **Beat 2 (Outline line 68) and B6 (Source_Sheet line 44).** At 29090 Biruni says he has read some of Mani's books ("what I have read of his books"). He does not say he read the books he names at 29112-29115.
   - In `Outline.md`, replace `a later witness, about 700 years on, naming books he says he had read, BIR 29090; Documented` with `a later witness, about 700 years on, who says he had read some of Mani's books, BIR 29090; Documented`.
   - In `Source_Sheet.md`, replace `Biruni names books he says he had read ("what I have read of his books", 29090).` with `Biruni says he had read some of Mani's books ("what I have read of his books", 29090).`

Neither change touches the brief's wording or its count.
