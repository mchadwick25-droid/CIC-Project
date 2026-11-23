# frumentius: "what it was about" check

**FIX** (three MINOR findings, no BLOCKING). Checked 2026-11-23 against `Outline.md` sections What it was about and Room for it, `Gaps.md`, `frumentius.brief.txt`, Kit Parts 1 and 3.

## What holds

- **The Arian teaching is told fairly.** Arius's view is given in his own sentence from his letter to Eusebius of Nicomedia, as Theodoret keeps it: "we say that the Son has a beginning, but that God is without beginning" (N203 6045-6046). His side would recognize it. Athanasius's view is the Nicene creed's own words as he gives them, "from the essence of the Father ... One in essence with the Father" (N204 19676-19679). The label is credited: "Athanasius called the emperor's bishops Arians", which matches his "the professors of Arianism" (N204 35938-35939). His own editor's caution that the East mostly rejected the Nicene wording without being Arian (N204 5741-5744) is why it must stay credited. It does. The letter itself names no teaching, only "the same doctrine" (N204 36143-36144), as the outline says.
- **The charges are the enemy's, told in their own content.** "The emperor's side had charged" credits them. Constans against Constantius (N204 34917-34924) and the letters to "the tyrant" Magnentius (N204 35101-35104) are both there. "He denied it all" holds: the Apology answers all four charges (N204 34917, 35101, 35398, 35620). The letter's "has not been able fairly to clear himself of any of the charges" is at N204 36151-36153. Confidence is right: Documented that they were charged, Contested whether they were true.
- **Items 3 to 8 hold.** Rufinus gives nothing more on the treaty than the custom (RUF 27311-27314; spot-checked). Philostorgius (item 8) is held and rightly left out.
- **Length.** By `python -m engine.m1.profile_readability`, the brief now counts 675. With the Room for it list applied as written it counts 671. With the fixes below it counts **675**, at the approved length, grade 7.9, longest sentence 30 words, pass. No heart, force, conflict, needed credit or carrying scene is cut.

## Findings

1. **MINOR. Item 1 and Room for it, item 1 wording: Arius's "beginning" without his "before all time".** Arius's letter says in the same passage that the Son "has subsisted before time, and before ages, as perfect God" (N203 6038-6040). Heard alone, "the Son had a beginning" can sound as if Arius made him a later creature. His side would add the "before time". There is room for three words. Replace the Room for it line for item 1 with:
   > item 1, **33** ("Athanasius called the emperor's bishops Arians, after Arius, who taught that the Son had a beginning, before all time, and God had none. Athanasius held that the Son shares the Father's own being."), after "as in the empire's.";

   and in What it was about item 1, change "who taught that the Son had a beginning and God had none" to "who taught that the Son had a beginning, before all time, and God had none", adding the witness "(N203 6038-6040, 6045-6046)".

2. **MINOR. Room for it, cut 2: "in the next century" would mislead.** Rufinus wrote around 400. Heard after a line about Aksum, "the next century" points nowhere clear, or to the 500s. Keep the anchor. Replace cut 2 with:
   > 2. What came 2: "in the century after Rufinus, Socrates almost word for word, one editor says" becomes "in the century after Rufinus" (8). The three historians' retelling stays; the editor's dependence goes to the card.

3. **MINOR. Room for it, cut 4: the cut text leaves "pray in so that" without its comma.** Replace cut 4 with:
   > 4. Beat 4: " and gave them sites for buildings," (6), leaving "meeting places to pray in, so that". The meeting places to pray in stay.

   Then replace the After line with:
   > - After: by `python -m engine.m1.profile_readability`, the brief now counts 675; the additions (61) and cuts (61) bring it to **675**, at the approved 675 (checked on a scratch copy). Not cut: the heart, the emperor's letter and its two quotes, Rufinus's and Edesius's credits, the date dispute, the tree scene.

   and the "Total **58**" to "Total **61**", the "Cuts ... **62** words" to "**61** words", and "Brief now (`wc -w ...`): **678** words, already 3 over" to "Brief now (`python -m engine.m1.profile_readability`): **675** words, at the approved 675".
