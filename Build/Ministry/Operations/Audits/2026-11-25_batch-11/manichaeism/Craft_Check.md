# Craft check: Manichaeism

Kit Part 3, step 5. This checks the six changes `Fresh_Read.md` applied to `manichaeism.brief.txt`, each against its source, the fault it was meant to fix and the sentences around it. No `.v*` file was opened.

## Verdict: FIX

Two of the changes add something their source does not hold: "their daily prayer" (S16) and "a royal city" (S20). Each has an exact change below. The other four hold. The gospel cut stands, under ruling (a).

## Each change

1. **S32, "some seventy of their women religious at the capital all died." HOLDS.** CHI 14093-14095: "A la capitale, soixante-dix religieuses manichéennes périrent toutes." "Some" fits, because another chapter gives 72 (CHI 14114). The change fixes what both trust reads blocked: the widened "women of their faith" and the doubled "their". The chronicle is still credited. It reads on one hearing.

2. **S12, the cut "among them his gospel". HOLDS: ruling (a), the cut stands.** BIR 29061-29062 says only that Mani "arranged" his gospel "according to the twenty-two letters of the alphabet". That is the gospel's form, not a plain account of what it was. So the outline has no cited plain sense to give, and option (b) has nothing to stand on. The scriptures are not left bare: the sentences just before describe one of them, the book for Shapur, which Biruni names among Mani's books (BIR 29112-29113: "his gospel, the Shaburkan, ..."). The scorer's "possible bare statement" flag on s13 passes for that reason. The brief needs no change. The outline changes:
   - Beat 2. Old: "and he wrote his own scriptures, among them his gospel (B6; BIR 29061-29062, 29112-29115: "his gospel, the Shaburkan, ... the Book of the Giants"; a later witness, about 700 years on, who says he had read some of Mani's books, BIR 29090; Documented). The Shaburkan is already the book for Shapur, so the clause names only the gospel." New: "and he wrote his own scriptures (B6; BIR 29112-29115: "his gospel, the Shaburkan, ... the Book of the Giants"; a later witness, about 700 years on, who says he had read some of Mani's books, BIR 29090; Documented). The book for Shapur, the Shaburkan, is the one the story describes; it names no other."
   - The Do not say row. Old: `| "he wrote his own scriptures" with nothing said of them | what they were, from B6, in a clause: "among them his gospel" (BIR 29061-29062, 29112-29115) |`. New: `| "he wrote his own scriptures" with nothing said of them | keep the book for Shapur, its opening told just before, as the one described (BIR 29054-29061, 29112-29113); name no other book |`. Keep the row below it ("Do not name Mani's gospel unless the story says what it was.").

3. **S3, the split Hippo answer. HOLDS.** CFo Latin 7683-7692: "sed solum contra fidem animadverti, quam postea didici et probavi, quod contra solem facitis orationem." "Only that they prayed facing the sun, which went against the faith he later learned" keeps the Latin's sense and adds nothing. "Against what" is now clear, and the lines read on one hearing.

4. **S16, "confession" glossed as "their daily prayer". ADDS: FIX.** KHU calls it "a confession-prayer of the Manichaean auditores" (KHU 15390, title). The text says the sins are committed "every day" (17347, 17370) and "every month and every day" (17598). It never says the prayer was said every day. So "daily" adds a claim. The outline's "daily confession (C9)" has the same fault, from C9's quote. "Prayer" also does not say what a confession is. The refrain does: "forgive my sin" (KHU 17443-17449).
   - Brief. Old: "The Hearers' own confession, their daily prayer, says the Light was in the food they ate, and that their sins sent it "to the Bad Place."" New: "The Hearers' own confession, a prayer for forgiveness, says the Light was in the food they ate, and that their sins sent it "to the Bad Place.""
   - Outline, How they practiced. Old: "daily confession (C9)". New: "the Hearers' confession, a prayer for forgiveness (C9; KHU 15390, 17443-17449)".

5. **S20, "at the gate of Gundeshapur, a royal city". ADDS: FIX.** BIR 29125-29127: "hung it up at the gate of Gundisapur". FIH 5115 has only "der Stadt Dschundisäbür" (the city of Gundeshapur). Nothing in B10's cited lines makes it a royal city. That rests only on Flügel's modern note on its founding by Shapur I (FIH 16794-16804). The outline's Place line has the same fault. The city's name fixes the second trust read's point.
   - Brief. Old: "Some say he was flayed and his skin hung at the gate of Gundeshapur, a royal city." New: "Some say he was flayed and his skin hung at the gate of the city of Gundeshapur."
   - Outline, Place. Old: "Gundeshapur, a Persian royal city (B10)". New: "Gundeshapur, a city (B10; BIR 29126 "the gate of Gundisapur"; FIH 5115 "der Stadt Dschundisäbür")".

6. **S24, the split Bema sentence. HOLDS.** It has the same content as before, cut into two sentences that read on one hearing.

## Counts

- `wc -w`: 839 now; 840 after the two fixes (+1, then 0). The target is about 830.
- `engine.m1.profile_readability`: 832 words, grade 9.0 (7.7 with names out), reading ease 74.8 with names out, 19.8 words a sentence, longest sentence 41 words. Pass.
- `tools/check_brief_craft.py`: 12 flags. Only s13 (the cut) touches a change, and it passes, as item 2 sets out. The rest are on unchanged sentences.
