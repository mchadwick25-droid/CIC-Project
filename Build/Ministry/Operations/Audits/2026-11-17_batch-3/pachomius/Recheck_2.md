# Pachomius: recheck 2

Targeted recheck of the revised `pachomius.brief.txt` (463 words) against `Review_2.md`, the amended `Outline.md`, `Source_Sheet.md` and the Brief-Kit `Standard.md`. Heard in Neo's voice, about 150 words a minute.

## Verdict: FAIL

One new factual claim (the birth date) entered in the revision. Everything Review_2 asked for is otherwise done. The fix is one clause.

## 1. The heart, and the first minute

**Heart:** Before him, Egypt's monks each lived the monk's life their own way. Pachomius drew them into one shared life under one written rule: houses inside a walled monastery, the same clothes, one table, shared work, nine monasteries in one fellowship. Through Jerome's Latin, that rule later reached the monks of the West.

**First minute:** Yes. Words 1 to about 150 run from Antony's witness ("no community anywhere ... your father did this great good") to "Nine monasteries along the Nile came to form one fellowship." The heart is stated and shown before the life story begins. The connection lands at the end, told through acts.

## 2. Review_2 findings

- **BLOCKING 1 (Palladius misdated): RESOLVED.** Now "Palladius, writing about seventy years later, counted some seven thousand monks under the rule." It still comes before Jerome, as Outline line 89 requires. Outline line 94 adds the Do not say line.
- **BLOCKING 2 (Esneh left unfinished): RESOLVED.** Now two sentences: the questioning "over claims that he read hidden thoughts", then "a man driven by an evil spirit burst in with a sword to kill him, but the Life says the Lord saved him with the help of those present." The questioning, the intent and the rescue are all there. Bishops and sword are in separate sentences with no causal link. This matches Outline beat 6 and the Do not say on the bishops (line 96).
- **MINOR 3 (long sentences): PARTLY.** The closing is split as asked, which eases the two Benedicts. But trimming the opening made it the tool's longest sentence, at 50 words (see MINOR 2 below).
- **MINOR 4 (length): PARTLY.** 472 down to 463 words, about 3.1 minutes. The outline's range is 380 to 450.
- **MINOR 5 ("in the early fourth century, each monk..."): RESOLVED.** Now "Before him, in Upper Egypt, each monk lived by his own way", as in Outline line 95.

## 3. Source check of new and changed sentences

- Opening, "In the Greek Life of Pachomius, by a monk of the next generation, the great hermit Antony speaks to the monks after their father's death". Supported by Source_Sheet row Greek Life ("suppar"; Robertson: "by a person who had known Pachomius") and Acta 86884-86893 ("Pater vester"). The quote matches Outline quote 1 word for word, and the rendering is faithful to 86887-86893.
- "Pachomius drew such monks into one shared life under one written rule." Outline heart, beat 1. Dropping the rank clause is a trim, not an error.
- **"Born to pagan parents early in the fourth century"**: not supported (BLOCKING 1 below).
- "Locked up with other recruits, he asked who the strangers feeding them were." Amélineau 5139-5146 ("apportèrent des pains et des mets ... ils forcèrent ... à les manger"). Faithful.
- "The Coptic Life, from his own communities, gives the answer": Source_Sheet row Bohairic Life. Quote 2 is verbatim to the outline, and the rendering is faithful to Amélineau 5145-5146.
- "Once free and baptized, he became a hermit's pupil, until at a deserted village called Tabennisi he began to build." This rests on E3 (5240-5241), E4/H1 (Palamon; Greek 81103-81107) and E5 (Amélineau 6014-6021: "un village désert, (situé) sur les bords du fleuve (et) nommé Tabennisi ... bâtis pour toi une cellule"). Acceptable. Dropping the voice removes a wonder rather than misstating one.
- Esneh: checked against Acta 86393-86400 ("eo quod diceretur dignoscere occulta ... Monachi et Episcopi") and 86463-86466 ("Vix autem sermonem finierat, cum a malo genio actus quispiam et machera armatus, virum santum interfecturus irrumpit : sed auxilio presentium salvavit eum Dominus"). Faithful.
- "In 346 or 348, as a plague swept the monasteries, he fell ill and asked for a lighter blanket." This rests on S4, E13 and Acta 86618-86629. Quote 3 is verbatim to the outline, and the rendering is faithful to 86630-86633.
- Palladius and the closing sentences: as above. "About 404 he dictated a Latin version for them, and for his own brothers and Eustochium's nuns" is unchanged in substance and matches the outline's connection and line 91.

All three quotes were re-checked verbatim against Outline.md and their source lines.

## 4. Score

`python -m engine.m1.profile_readability`: 461 words, grade 8.2 (names out 7.6), reading ease 72.2, 17.7 words a sentence, longest sentence 50 words. Pass.

## Findings

**BLOCKING 1. "Born to pagan parents early in the fourth century, he was taken at about twenty for Constantine's war."** No held witness dates his birth. The only held estimate is the editors' "about 292" (S4: Richardson, Schodde), which is in the late third century and is Inferential-Thin. The sentence states a contested date as settled, and it runs against the only figure held. The previous draft did not make this claim. Change to: "Born to pagan parents, he was taken at about twenty for Constantine's war, early in the fourth century." That puts the period on the conscription, where the Lives put it (Constantine, after the persecution: Bohairic 5093-5096, Greek 80977-80980).
- **Amend the outline.** Setting (line 11) and the Do not say "Born in 292" (line 78) should both say that "in the early fourth century" describes his life and the conscription, not his birth. Add: "Born early in the fourth century" → "taken at about twenty for Constantine's war, early in the fourth century"; no held source dates his birth.

**MINOR 2. Opening sentence, 50 words by the tool.** The trim joined a 28-word lead-in to the 25-word first quoted sentence. It also loses the "Pachomius's monks" that made "your father" plain, which the outline asks for. Change to: "In the Greek Life of Pachomius, by a monk of the next generation, the great hermit Antony speaks to Pachomius's monks after his death." Then start the quote as its own sentence: "He says: "When I first began ..."". If the extra words matter, use "He tells them:".

**MINOR 3. Length, 463 words against 380 to 450.** Cut the doubled attribution at Esneh: "At Esneh, monks and bishops questioned him over claims that he read hidden thoughts. As he finished, a man driven by an evil spirit burst in with a sword to kill him, but the Greek Life says the Lord saved him with the help of those present." That saves four words. For the rest, cut "along the Nile" from "Nine monasteries along the Nile", since Upper Egypt is already given. Leave the quotes untouched. Do not cut the heart, the split, Theodore's letters, or Eustochium's nuns (Do not say lines 90 and 91).
