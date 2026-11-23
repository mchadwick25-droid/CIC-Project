# mesrop-mashtots: Writer, "what it was about" pass

`About_Check.md` verdict FIX. Its five exact replacements went into `Outline.md` first, word for word (logged in `Outline_Synced.md`). The brief before this pass is kept as `mesrop-mashtots.brief.v3.txt`. Every change below traces to the outline as synced; every other sentence is unchanged.

## Explanations (What it was about, items 6, 8, 9)

1. Item 8, the Borborites (BLOCKING finding). Before: "He fought the Borborites, a sect Koriun calls rash and insolent. Those who would not yield ..." After: "He fought the Borborites, a sect Koriun calls rash and insolent. Koriun never says what they taught. Those who would not yield ..." Augustine's and Marutha's charges are not used. The force stays in full.
2. Item 6, Moses's letter. Before: "... Moses of Khoren, says the letters were first refused." After: "... Moses of Khoren, says the letters were first refused. In the emperor's letter Moses gives, Sahak is blamed for serving a pagan king and for turning to Syrians, not to Constantinople's scholars."
3. Item 9, the man shut out from Ephesus. Before: "When the council of Ephesus warned of a man it had shut out, who came with heretical books, Sahak and Mesrop drove him out." After: "When the council of Ephesus warned of a man it had shut out, whose books, Koriun says, followed Nestorius, Sahak and Mesrop drove him out. That council's quarrel turned on whether Mary could be called Mother of God; Nestorius urged Mother of Christ instead."

## Leave out (items 7, 10, 12, 13) and the other Room for it cuts

1. Cut 1. Before: "He learned Greek as a boy and kept the king's decrees. Then he became a monk, ..." After: "He became a monk, ..."
2. Cut 2 (item 13). Before: "... only Syriac learning was allowed. Mesrop went to Sahak about letters, and found him even more eager." After: "... only Syriac learning was allowed."
3. Cuts 3 and 4. Before: "... the Syriac lands to the south, where the bishop's letters failed. Rising from prayer, Mesrop made new letters ..." After: "... the Syriac lands to the south. Mesrop made new letters ..."
4. Cut 5 (item 7). Before: "... sent Mesrop to them, and the bishop named him a preacher." After: "... sent Mesrop to them."
5. Cut 6. Before: "Back in Armenia, with Greek learning barred on the Persian side, Sahak and Mesrop went west ..." After: "Back in Armenia, Sahak and Mesrop went west ..." (The check's optional restore was not taken: the ban is told in the Koghten paragraph, and the outline makes this cut.)
6. Cut 7 (item 10). Before: "... true copies of the Scriptures and the canons of Nicaea and Ephesus, and the first hasty translations were corrected." After: "... true copies of the Scriptures, and the first hasty translations were corrected."
7. Cut 8 (item 12). Before: "... drove him out. Koriun calls them defenders of the true faith." After: the sentence removed (item 9's added sentence now follows "drove him out.").
8. Cut 9. Before: "After a short illness in the New City, he sat up ..." After: "After a short illness, he sat up ..."

## First-time listener read

Each thing named is now said plainly: the letters and why (preaching in Armenian), the Syrian letters (could not carry the sounds), Proverbs and the Tablets, the Persian ban, the Georgian rival claim, the refusal and its reason in Moses's account, the Borborites (with the honest limit that their teaching is unknown), and the Ephesus man (books following Nestorius, and the Mother of God quarrel). Nothing is left named but unexplained.

## Count

`python -m engine.m1.profile_readability --report`: 657 words (cap 675), grade 8.5, reading ease (names out) 76.3, 16.8 words a sentence, longest sentence 28 words. Pass. `wc -w` also 657.

## Noted, not changed

`Outline.md`, Room for it, still reads "**Words the explanations add:** 65." `About_Check.md` gave no replacement for that line, so it was left as is; the synced count line now gives the true sum (6 + 23 + 20 = 49).
