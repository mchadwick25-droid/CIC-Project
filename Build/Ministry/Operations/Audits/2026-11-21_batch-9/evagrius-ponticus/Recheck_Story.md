# Recheck: Evagrius Ponticus (`evagrius-ponticus`)

## Verdict: FIX

One fix, same word count. Every factual finding is fixed. The only miss is a word left without its plain sense the first time it is heard.

## 1. Findings in Review.md

- **B1 (second book; Gennadius's translation).** Fixed. "A second book set verses of Scripture against each of the eight, as Christ answered his tempter." Outline line 14 and Beat 5 (line 59). Gennadius, npnf203 : 42330-42335, has "setting against them eight books taken from the testimony of the Holy Scriptures only, after the example of our Lord, who always met his tempter with quotations from Scripture". "He put that second book into Latin himself" matches 42335-42336 ("This work I have, under instructions, translated into Latin"). The Do not say line is at Outline 146.
- **B2 (bread and oil).** Fixed. "he ate a pound of bread, and a pint of oil lasted him three months" matches clarke1918 : 459 §10 ("he used to eat a pound of bread, and in three months a pint of oil"). No period is added to the bread. Do not say at Outline 147.
- **B3 (oath made him a monk).** Fixed. The oath now "set Evagrius Ponticus on the road to the Egyptian desert", and the Melania paragraph keeps the promise "to live as a monk" (457 §9). "There he became a monk" means the desert life Palladius begins at Nitria (457 §9, "exiled himself in the mount of Nitria"). It does not give the oath Melania's part, and it agrees with the Do not say at Outline 148. Accepted.
- **M1, M2.** Fixed as the review set them. "Palladius, his disciple and our main witness" is held by Outline line 110. "fleshly desire" is Palladius's own phrase (459 §13).
- **M3.** Only half fixed. See the FIX below.
- **Payers.** Each cut removes only words. "Cassian never names Evagrius" still holds the outline's line 87 duty, since the match of lists is heard in the sentence before it. Dropping "the son of a bishop for the countryside" leaves country-bishop unheard, so it no longer needs explaining. Dropping "writing against Pelagius" costs no credit: the Do not say at Outline 140 forbids "Jerome's council", and the story says neither.
- **Not restored:** the well, fifty hours, the hundred prayers and the other MINOR details. These were MINOR and no words remain to restore them. Accepted.

## 2. Changed sentences against their sources

All are held at the lines above. Each says no more than its source and credits the right witness (Palladius, Gennadius, the councils). The quotes are unchanged from the old draft, and I re-checked each one verbatim:
- Q1 against clarke1918 §7 ("Even if the oath was in a trance, nevertheless I did take it").
- Q2 against dysinger : 197.
- Q3 against npnf206 : 27825-27826.
- Gennadius's "or among the first at least" against npnf203 : 42330-42331, where it runs across a line break.
- Thomas of Marga's "the holy Evagrius" against budge1893 : 22401.
- The council list against npnf214 : 26636-26638.

## 3. Shape

- **Hook:** the vision and the oath.
- **Essence:** complete at word 106 ("the mind's own work"). The reach ahead, to the condemnation and the later use, ends at word 134.
- **Also told:** all present. That covers the eight, Q2, acedia, prayer, the second book, the desert regime, the philosophy of deeds and Jerome.
- **Ending:** on the person.
- **Length:** 673 words against the 675 cap.
- **Longest sentence:** 32 words, the prayer sentence, unchanged from the old draft. It is about 30, so it is accepted.
- **Words to explain:** these fail on one word. Origen is first heard at word 120, in the essence ("councils named him with Origen among the condemned"). His plain sense comes only in paragraph 9. The original review named this as where the listener got lost. Placing the gloss after "and" also lets the listener hear "a third-century teacher of Alexandria" as Didymus.

### FIX (moves the gloss to where Origen is first heard; same 673 words)

Replace:
> Long after his death, councils named him with Origen among the condemned.

with:
> Long after his death, councils named him with Origen, a third-century teacher of Alexandria, among the condemned.

And replace:
> listed Evagrius with Origen, a third-century teacher of Alexandria, and Didymus as condemned at Constantinople in 553.

with:
> listed Evagrius with Origen and Didymus as condemned at Constantinople in 553.

The gloss comes from Outline line 42 (Words to explain). With the fix, the reach ahead ends at word 140, still inside the first minute.

## 4. Score

`python -m engine.m1.profile_readability …/evagrius-ponticus.brief.txt`:
- 673 words.
- Grade 7.2 (6.0 with names left out).
- Reading ease 79.2.
- 15.3 words a sentence.
- Longest sentence 32 words.
- Result: pass.

The grade is under 8. On the listener read it is not flat. The fix moves words without adding any, so the score should not change.

## Applied (coordinator, 2026-11-22)
The replacements above applied word for word to the brief.
