# Priscillian — Fresh read

Read of the final `priscillian.brief.txt` (674 words), against the kit, the batch header, `Outline.md` and `Source_Sheet.md`. Not opened: `Review.md`, `Revision.md`, `Outline_Check.md`, `Recheck.md`, `Writer_Reply.md`, any `.v1`/`.v2`.

## The three lines, from one hearing

1. **Who:** Priscillian, a rich, learned layman of Spain who called men and women to give up family, wealth and rank for a strict life given to God, and became bishop of Abila.
2. **What happened:** Spanish bishops fought him. Damasus and Ambrose turned him away, and he was tried at the usurper Maximus's court at Trier. Martin pleaded for him, but a prefect found him guilty of sorcery, and he was put to death by the sword in about 385.
3. **Why it matters:** his death split the church. His followers kept him as a martyr, his chief accuser lost his bishopric, and a bishop of Rome later praised the sword. His own writings were found again in 1885.

All three lines come through clearly.

## Essence and what is also told

- **Essence** (census and outline): a rich, learned layman of Spain who drew men and women into a strict ascetic life and was made bishop of Abila. Accused by bishops, he was tried at Maximus's court at Trier and put to death in about 385, and his followers honoured him as a martyr. The hook (his book carried to Damasus, quote 1) leads straight into it, and it is fully told by about word 105. Pass.
- **Also told** (the approved heart, Hearts.md ruling 1):
  - What his book to Damasus taught. Only the ascetic call is told. **His creed and his curse on every heresy, the Manichaeans above all, are absent** (see finding 1).
  - How the bishops fought him: Saragossa, with the two accounts side by side; Gratian's order; Damasus and Ambrose. Present.
  - The trial: his appeal, Ithacius's suspicion of readers and fasters, Martin's plea, the prefect's two hearings, sorcery, the deaths. Present, with its weight.
  - What came of it: the martyr's cult, the bishops' fifteen-year quarrel, Ithacius deposed, Leo, Braga 561, the 1885 find. Present.
- **Order:** after the essence the life is told once, in order. The hook reaches ahead to Rome, which the kit allows. No event is told twice and nothing jumps back.
- **Ending:** it ends on the person, his own call found again in his own book. Pass.
- **Names heard once that neither act nor link:** Gratian is named once. He acts (his order), so this is not a finding, though the outline gave him by role.
- **Where I got lost:** nowhere badly. Two small snags are below (findings 3 and 4). Nothing reads as a children's book or talks down.

## Source check

Every sentence traced to the outline and source sheet, and the key lines were re-read in `cic/texts/`:
- **Quote 1** matches Pr 4415-4417 ("nec prohibere si quis contemptis parentibus liberis facultatibus dignitate et adhuc et anima sua deum malluerit amare quam saeculum"). The OCR has the letter misreadings the outline notes. The rendering is faithful.
- **Quote 2** matches SulpL 5890-5891 ("mihi tam reos quam accusatores displicere", OCR "dispUcere"). This is the slate's lifted line, rendered from the Latin, and it does the lifted job.
- **Quote 3** matches Leo 3276-3278 (Feltoe). The rendering keeps every clause.
- **Other lines checked:** Saragossa from both sides (SulpE 11502-11510; Pr 4394-4396, the "nemo ... damnatus est" passage and "ne quid in absentes et inauditos decerneretur"). The beating at Emerita (Pr, "adflicti uerberibus sumus"). "In a cause of faith" (Pr, "in causa fidei sanctorum iudicium malle quam saeculi"). Martin "while he was in Trier" (SulpL "quoad usque Martinus Treueris fuit"; the brief rightly avoids Roberts's "as long as Martin survived"). Sorcery (SulpL "conuictumque maleficii"). The cult (SulpE 11722-11729). The quarrel "inter nostros", the bishops above all (SulpL 6003-6006). Toledo (Mansi3, "Priscillianum catholicum, sanctumque martyrem clamassent"). Braga (Bruns 2513-2515). The 1885 find (Pr 80-93).
- **Do not say list:** honoured throughout. The story never says "the first put to death". The verdict is the court's, for sorcery (batch ruling item 5). The magic rumour stays as "was believed". The charges are framed as "the court's findings". The date is "in about 385", and he dies "with several companions".
- No fact is wrong. One understatement is noted below (finding 2).

## Score

`python -m engine.m1.profile_readability`: 674 words, grade 8.2 (names out 7.0), reading ease 72.0, 15.3 words a sentence, longest sentence 29 words. **Pass.** The batch ceiling of 675 is met.

| | Score | Reason |
|---|---|---|
| Voice | 4 | An adult narrator's voice, and the three quotes do work the narrator could not. The witness is credited openly and Sulpicius's dislike of both sides lands. A few "he says / he adds" tags run close together in the Saragossa and Trier paragraphs. |
| Craft | 4 | A strong hook that comes back in the ending, the essence early, and a clean time order. The connection (one death, two memories) is carried through what people did. "The deaths split the other side too" is a slightly blurred hinge. |
| Rigor | 3 | Faithful sourcing, careful witness credit, and the batch ruling kept. But the heart's teaching item is cut to the ascetic call alone. That leaves Sulpicius's "heresy of the Gnostics" standing with no word of Priscillian's own creed and his curse on the heresies. One edict is also understated. |
| Accessibility | 5 | Grade 8.2 and reading ease 72. Plain words, with Gnostics, usurper and sorcery worked into the sentences. Easy to follow by ear. |

## Verdict: REVISE

## Findings

1. **BLOCKING — missing essential material (an approved heart item).** The heart's first "also told" item is "what he taught, in his own book to Damasus: the ascetic call open to all, his creed, his curse on every heresy, the Manichaeans above all" (Pr 4483-4485, 4565-4567, checked). The brief tells only the call. This also leaves the hostile label ("the heresy of the Gnostics") without the book's own answer, the answer the outline's Do not say line points to ("he himself cursed the Manichaeans").
   *Change:* after "...cannot be his disciple." add: "The same book gives his creed and curses every heresy, the followers of the Persian teacher Mani above all." (18 words.)
   *To stay at 675:*
   - In "His enemies won an order from the emperor Gratian that drove all heretics from the cities," change "the emperor Gratian" to "the emperor" (−1, and it keeps Gratian by role, as the outline asks).
   - Change "a German scholar" to "a scholar" (−1).
   - Cut "At Emerita, he says, his group came in peace and was beaten in the church." (−15). This is one side's account, beyond the heart's list. The harassment by the bishop of Emerita stays.
   - Net 674 + 18 − 17 = 675. Confirm with the scorer.
   *Do not say line for the outline:* "Leaving out what the book to Damasus teaches beyond the ascetic call. Say also: the book gives his creed and curses every heresy, the followers of the Persian teacher Mani above all (Pr 4483-4485, 4565-4567)." Add a matching clause to Story beat 1, which does not carry this item now.
2. **MINOR — an edict's force understated.** Gratian's rescript ordered heretics "not only to leave churches or cities, but to be driven forth beyond all the territory" (SulpE 11526-11541). "Drove all heretics from the cities" narrows it.
   *Change:* "...that drove all heretics from the cities" → "...that drove all heretics out of the cities and beyond all its lands." (+5 words. If the length forces a choice, make finding 1's change first and keep this one only if the count holds.)
3. **MINOR — the hook and the refusal at Rome.** The listener hears that he "carried a book to Damasus", and later that "Damasus would not even see him". They may wonder how the book reached him.
   *Change:* "Priscillian went to Rome:" → "Priscillian went to Rome with his book:" (+2; use only if the count allows). Leaving it as it stands is acceptable.
4. **MINOR — an ambiguous "he" in the last line.** "Among them was the book he had carried to Damasus" follows a sentence whose subject is the scholar.
   *Change:* "the book he had carried to Damasus" → "the book Priscillian had carried to Damasus" (a one-word swap, no change to the count).
