# Card check, "what it was about" pass: John Chrysostom

Card `john-chrysostom.card.json` against starting card `Card.pass2.json`, the edit list in `Card_Edits.md` (Third pass, 2026-11-23) and `john-chrysostom.brief.txt` as it now stands. Every cited line opened.

**Verdict: FIX** (three changes).

## What holds

- Nothing moved outside the edit list. A field-by-field diff of the two cards shows only `legacy.traces` (+1), `uncertain` (+6), `sources.about` (+1) and `briefReferences` (edits 1-9). Every other field is word for word, in the same order.
- References no longer told were trimmed as listed (edits 5-9). Each trim matches the brief: "from Antioch", "In 398 Eutropius made Theophilus of Alexandria ordain him", the hospital only, no Eutropius-sermon clause, "toward Pityus". Every other reference is still told in the brief.
- The new references hold at their lines. Gainas and "It is said" are at npnf202 17368-17372. The Son's beginning is at 2094-2095, inside Book I, Chapter V (it begins at 2064). The monks and the false report are at 17578-17592, 17640-17693 and 17826-17843. The Oak charges are in Photius at 3875, 3877, 3931 and 3933. The statue, the games, the second council's sole ground and the decree are at 18427-18444, 18468-18472 and 18486-18496.
- Uncertain items 10, 12, 14 and 15 and the fire trace (16) hold at 17097-17108, 3843 and 3939 with 18271-18274, 18239-18249, 18474-18480 and 18496-18500.
- `quotationOriginals` is unchanged and still right. There is one quoted span ("Glory to God for all things."). Its printed form "Glory to God for all things;" stands at Palladius 6498-6499. Nothing is marked "checked at card".
- The census rules hold. With this card in a scratch census copy, `node tools/validate-census.mjs --skip-quotes` gives 0 errors, and the 4 warnings are none of this entry's. No audit file is named. The spelling is American ("defense" and "authorized" are unquoted).
- Not-found item: the "thirty-fifth year after his deposition" (VII.45, 21465 against 21478) is still listed and left in place. That is correct.

## FIX

1. **`uncertain`, the Oak minutes item (edit 13): clearly wrong against Photius.** The minutes do not go from the first and second counts straight to the vote. After the first and second counts (3946) they investigate the ninth and twenty-seventh (3956), then Isaac's charges and the deacon John's third (4011-4013), and then the fourth (4022-4024). Only then comes the vote (4025-4031). The outline itself says "examined some of the counts".
   - Old: "The minutes, as Photius gives them, say the first and second counts were examined and then the forty-five members present voted unanimously to deprive him."
   - New: "The minutes, as Photius gives them, say several of the counts were examined, beginning with the first and second, and then the forty-five members present voted unanimously to deprive him."

2. **`uncertain`, Theophilus's motive item (edit 11): clearly wrong against Socrates VI.9.** At 17838-17843 the real motive the letters hid was revenge on Isidore and Dioscorus, and the casting of John out of his see. "Revenge on the monks" leaves out John, who is the point of the brief's sentence. It also folds in Isidore, who was not one of the monks (17793-17797).
   - Old: "and that his letters condemning the books of Origen hid his real motive, which was revenge on the monks."
   - New: "and that his letters condemning the books of Origen hid his real motive, which was revenge on Isidore and Dioscorus and the removal of John."

3. **`sources.about`: the I.5 reference (edit 1) has no source entry.** It is the same file as Book 6. But the card lists Socrates by book (Book 6, and Book 7 chapter 45), and edit 3 set the precedent: Sozomen VIII.2 got its own entry for a file already listed. Insert after the "Church History, Book 7, chapter 45" entry:
   - Old: (none)
   - New: `{"title": "Church History, Book 1, chapter 5", "author": "Socrates", "date": null, "language": "English translation", "file": "cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml"}`

Minor, no change required: "Gothic" in the Gainas reference comes from the VI.6 chapter title (17388-17390). It does not come from VI.5 at 17368-17373. Socrates does say it, so it is not wrong.

## The skipped "Socrates is no friend of Theophilus"

The skip is right in outcome, but the writer's reason is only half right.

- The writer is right that 18122-18125 do not say it. Those lines are the end of VI.12 (Theotimus's reply to Epiphanius) and the heading of VI.13, "The Author's Defence of Origen". Neither is about Theophilus.
- The held text does support the point elsewhere. In VI.7 Socrates calls Theophilus "evidently of a hasty and malignant temperament" (17648-17649). He says Theophilus acted "to gratify his vindictive feelings" (17662-17663). In VI.9 he says Theophilus concealed "his real motive" (17841). So the claim is not unsupported. It is mis-cited.
- It was never a card item. In outline item 9, "Credit Socrates, who is no friend of Theophilus" tells the brief how to credit, and the brief does credit Socrates ("Socrates says that when Theophilus heard..."). The item's "Card." follows the Origen sentences, and the card carries those in edit 11. The card already credits Theophilus's motive to Socrates as contested. A separate line on Socrates's bias would go past what the outline sends.
- Outside this card: the outline's citation for the phrase should read VI.7, 17648-17649 and 17662-17663, not VI.13, 18122-18125. That is the outline owner's fix, not the card's.
