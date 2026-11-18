# Card edits: Pachomius

Every field of `pachomius.original.card.json` is kept word for word and in its order, except the one correction below. `secondReading` is left out of every quotation entry: a blind second reading fills it later.

## New

1. **`briefLength`** (added after `role`). Old: none. New: "about 3 minutes 10 seconds". Evidence: `pachomius.brief.txt` is 479 words (`wc -w`). That is about 3:10 at the pace the finished cards use (470 words is "about 3 minutes 10 seconds" for Justin Martyr in this batch).
2. **`sources.about`, seven new items** (after the four already there). Each is a file the brief draws on, vendored for this batch or already held:
   - The Bohairic Life, tr. Émile Amélineau, 1889 (`amelineau_histoire-de-saint-pakhome-annales-guimet-17_leroux1889.txt`): the prison, the vow, Palamon, Tabennisi, the first brothers, the clergy, Athanasius, Mary.
   - The Greek Life in Daniel Cardon's Latin, Acta Sanctorum, May, vol. 3, 1866 (`acta-sanctorum_maii-tomus-3-lat-grc_palme1866.txt`): Esneh, the plague, the blanket, Petronius and Horsiesius.
   - Jerome's preface to the Rule, PL 23, 1883 (`jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt`): the Latin version.
   - Cassian, Institutes 4.1 (`npnf211_...cassian.xml`): "the monks of Tabenna".
   - Gennadius, On Illustrious Men 8 (`npnf203_...rufinus.xml`): Theodore's letters and the split. The card's existing Gennadius entry is chapter 7 only, so chapter 8 gets its own entry.
   - Archibald Robertson, Prolegomena, NPNF 2nd series vol. 4 (`npnf204_athanasius-select-works-letters.xml`): the year 346.
   - Ardo's Life of Benedict of Aniane and the Concordia regularum, PL 103, 1851 (`benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt`): the brief's last paragraph.
3. **`briefReferences`** (new list, sixteen items). Each was re-read at its lines:
   - Bohairic 4954-4957, 5093-5101, 5139-5148, 5182-5183 (the prison, "par amour pour le Dieu du ciel", the vow).
   - Greek 80977-80992, 81009-81013, 86417.
   - Bohairic 5240-5241, 5283-5291, 5424-5434 (baptism, epidemic, Palamon's rule "telle que nous l'ont apprise ceux qui nous ont précédés").
   - Bohairic 6013-6021, 6246-6248, note e at 6260; Greek 81345-81349, 81972-81974.
   - Palladius 399 (brass tablet); Clarke 657 ("I.e. 419-420"); Greek 82214-82217 (the bracketed tablet passages).
   - Bohairic 6252-6300, 6333-6336, 6436-6442.
   - Bohairic 6385-6391, 6670-6674; Greek 82514-82520.
   - Bohairic 6523-6528, 6570-6581; Palladius 409.
   - Greek 86393-86400, 86463-86466.
   - Greek 86508-86512, 86572-86574, 86619-86633, 86655-86672; Bollandist notes 86728, 86730; Robertson npnf204 5643-5644 ("died on May 9, 346").
   - Gennadius npnf203 42276-42286.
   - Palladius 405 ("amounting to 7000 men").
   - Cassian npnf211 18521-18531.
   - Jerome PL 23 4335-4354, 4384-4388 ("Alexandria missos", Metanoia, "nostro sermone dictavi", Eustochium).
   - Ardo PL 103 30903-30911; Concordia 66976.
   - The census, desert monasticism: `Outline.md` Setting, *Tradition*.
4. **`quotationOriginals`** (new list, three items). The modern wording is the brief's, checked by script to stand in the brief. The printed wording is the file's, OCR and all, with spaces closed and line breaks joined, checked by script to stand in the cited lines. All three were re-read in the file.
   - "They are Christian people. They treat us this way out of love for the God of heaven." Printed: "Ce sont des gens chrétiens : ils agissent ainsi avec nous, par amour pour le Dieu du ciel." Amélineau 5145-5146.
   - "Pachomius, Pachomius, the will of God is that you serve the human race and unite them to Him." Printed: "Pakliôme, Pakhôme, Pakhôme, la volonté de Dieu est que lu serves la race humaine et que Iules unisses àLui." Amélineau 6247-6248. `uncertain` gives the true readings (Pakhôme, tu, tu les, à Lui) and Amélineau's added third name (note e, 6260).
   - "Take this blanket away from here at once. It is not right that I should be better off in anything than the other brothers." Printed: "Istud, inquit, straguli absque mora hine aufer; non enim iequum est ut in re quapiam melius mihi sit quam Fratribus ceteris." Acta 86630-86633. `uncertain` gives hinc and aequum, and marks "inquit" as the narrator's.

## Clearly wrong

1. **`uncertain`, first item.** Old: "His life and rule otherwise reach us through Palladius of Helenopolis, who tells them as a holy man's story, and through Sozomen, who follows Palladius." New: "His life and rule otherwise reach us through his Coptic and Greek Lives, through Palladius of Helenopolis, who tells them as a holy man's story, and through Sozomen, who follows Palladius." Evidence: the held Lives (Amélineau's Bohairic Life, 4889-14805; Cardon's Greek Life, 80934 to about 88520) contradict "otherwise ... through Palladius ... and through Sozomen", and the brief rests on them: "His own communities' Coptic Life gives the answer", "both his oldest Lives say".

## Checked, left alone

- `datesNote`: "died 348 (George Schodde; Ernest Cushing Richardson's note to Gennadius)". The brief says "346 or 348". The card gives 348 as those two editors' date, and both say it (Schodde 136; npnf203 42254). Attributed, so not contradicted; the 346 is in `briefReferences`. A checker may judge otherwise.
- `legacy.traces`: the women's house "across the river", which "Palladius and the Ethiopic version both record". Both do (Palladius 409; Schodde 206). The brief adds that the Coptic Life puts it in the village; the card's sentence is attributed and stands.
- `uncertain`: Clarke on Ladeuze ("inferior in authority to the Lives", the angel "legendary", 1033; the lettered groups, 1047) and Butler's "probably the most authentic epitome" (1049). Verbatim.
- `uncertain`: Schodde, "if not verbatim from his pen" and "almost to the days of Pachomius himself" (39-40); "the father of monastic institutions" (136). Verbatim.
- `knownFor` and `legacy.remembered`: Gennadius, "founder of the Egyptian monasteries" and "apostolic grace" (npnf203 42256-42257); "angelic dictation" (42259). Verbatim.
- `legacy.traces`: seven thousand monks (Palladius 405). Verbatim in substance.
- `uncertain`: the head house Pabau, not Tabennisi. Supported by Clarke's notes and Bohairic 9597-9599.

## Not found

None.
