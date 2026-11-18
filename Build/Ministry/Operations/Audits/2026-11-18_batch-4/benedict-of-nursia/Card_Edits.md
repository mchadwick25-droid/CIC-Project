# Card edits: Benedict of Nursia

Base: the census card for `benedict-of-nursia` in `cic-website/data/world-census.json`, not the copy that was in this folder. Every field is kept word for word and in its order except `briefReferences` and `quotationOriginals`, as listed below. No `briefLength` (the census does not allow it).

Ardo's Life of Benedict of Aniane is not added to `sources`: the brief does not draw on it (it names neither Benedict of Aniane nor anything from Ardo).

## New

1. **`quotationOriginals`, new first entry (Q3), awaiting second reading.** Old: none. New: modern "For the holy man could in no way teach otherwise than he lived." (the brief's first paragraph, exact); printed "for the holy man could not otherwise teach, than himself lived." (GRG `gregory-great_dialogues_gardner1911.txt` 5571-5572, re-read); original "quia sanctus vir nullo modo potuit aliter docere quam vixit." (AS `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` 80438-80440, re-read); work Dialogues II.36 (the 1608 heading of chapter thirty-six, on the rule he wrote for his monks, GRG 5558-5560; OCR garbled). `uncertain` notes "nullo modo" read as "in no way". No `secondReading`: the span is new. Both files are already card sources.
2. **`briefReferences`, four new entries** (inserted beside the related entries; no existing entry moved):
   - Dialogues II.36, the pointer to the Rule. GRG 5563-5572; AS 80434-80440. Brief: "and then pointed his readers somewhere else, to the rule Benedict wrote for monks."
   - Dialogues II.15, Totila. GRG 4460-4487 (the chapter fifteen heading at 4460); AS 79150-79164 ("sese in terram dedit", "prostratumque de terra levavit", "minus crudelis fuit"). Brief: "Totila, king of the Goths, threw himself to the ground before Benedict ... the king was less cruel." This takes the place of the removed II.14 entry (below).
   - Dialogues II.37, his death. GRG 5582-5591; AS 80448-80457 ("inter discipulorum manus", "erectis in coelum manibus stetit"). Brief's last sentence.
   - Rule, ch. 53, 58, 73. Ch. 53: RBL 7799-7800 ("tamquam Christus suscipiantur"). Ch. 58: RBL 8568-8569 ("de stabilitate sua, et CONVERSIONE MORUM SUORUM, et OBEDIBNTIA"), RBL 8556-8560 (no leaving, the yoke of the Rule). Ch. 73: RBE 4297-4300 ("this little Rule written for beginners"). Brief: "Every guest is received as Christ"; "the promise binds for life ..."; "Benedict called it a little rule for beginners."

## Clearly wrong

Each item is a `briefReferences` entry that names something the finished brief no longer draws on, or breaks the quotation-mark rule.

1. Prologue entry. Old: "born in the province of Nursia, sent to Rome to study". New: "sent to Rome to study". Evidence: the brief never names Nursia.
2. II.1 entry. Old: "Subiaco, almost forty miles from Rome; Romanus, the cave for three years, the bread on a rope with a little bell; others coming to him for teaching." New: "Subiaco; the cave for three years." Evidence: the brief has only "spent three years in a cave near Subiaco"; no distance, Romanus, bread or disciples.
3. II.8 entry. Old: "the move to Cassino. Gardner: about 528 or 529." New: "the move to Cassino; the idol of Apollo smashed, the altar overturned, the sacred woods burned, and chapels built." Evidence: the brief gives no year; it tells the Apollo passage (AS 78762-78767; GRG 4167-4184).
4. II.14 entry removed. Old: "Dialogues II.14: \"in the time of the Goths\"." Evidence: the brief does not use the words, and they are quoted without standing in the brief.
5. Rule ch. 48 entry. Old: "\"Idleness is an enemy of the soul\";" New: "Idleness is an enemy of the soul;" Evidence: the brief has "the Rule calls idleness an enemy of the soul", so the quoted words are not verbatim in it. Quotation marks only removed.
6. II.17 entry. Old: "the Lombards plunder Monte Cassino by night, and no monk is taken." New: "the Lombards plunder Monte Cassino." Evidence: the brief has "the Lombards sacked Monte Cassino", with no night and no word on the monks.
7. **`quotationOriginals`, Paul the Deacon entry removed** ("carrying with them the manuscript of the Holy Rule"). Evidence: the brief no longer quotes it ("Paul the Deacon later wrote that the monks fled to Rome with the manuscript of the Rule"). The Paul source stays, since the brief still draws on it.

## Kept, with second readings copied

- Q1 ("So we must found a school for the Lord's service ...") and Q2 ("Let him so temper everything ..."): modern wording and source unchanged from the census card, so each keeps its census `secondReading` ("same"). Re-read: RBE 768-770, RBL 1240-1245; RBE 3960-3961, RBL 9527-9528.

## Left alone

- `uncertain`, last item, on the modern English of Benedict's words to Totila and of Gregory's praise of the Rule. The brief now paraphrases Totila and quotes only Gregory's last sentence, so the note speaks of renderings it no longer gives. Not contradicted by a source, so left under the card rule, as at release 50 (Open-Gaps, "What release 50 leaves", 2026-11-17).
- `legacy.traces`, "twelve monasteries near Subiaco, with twelve monks in each". Supported (GRG 3845-3850); the brief's "twelve at Subiaco" agrees.
- `legacy.remembered`, Simplicius "the third head of his order". The 1608 has "third General of his order" (GRG 3439); attributed to Gregory and not contradicted by the brief.

## Not found

None.


## Card check fixes applied verbatim, 2026-11-18

- `briefReferences[1]`: "Book II is the only early Life of Benedict, and Gregory tells it" became "Gregory tells Book II".
- NOT applied, held for Mark: the fix removing `uncertain[5]` (the Totila rendering note).
