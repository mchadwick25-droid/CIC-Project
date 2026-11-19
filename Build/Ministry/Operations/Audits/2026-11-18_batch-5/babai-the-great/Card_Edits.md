# Card edits: Babai the Great

Card writer, batch 5, 2026-11-18. Base: the census card for `babai-the-great` (identical to `Card.existing.json`, checked by object comparison). Every existing key and value is kept word for word and in order. Result: `babai-the-great.card.json`.

## New

1. **`quotationOriginals`** (old: none). Two entries, one for each quoted span in the brief. Both spans are new, so neither has a `secondReading`. Both are **awaiting second reading**.
   - Q1. Modern: "Here too, in the same way, we say that Christ was crucified, that Christ died and rose again. But we do not say that God was crucified and died." Printed: "Ici aussi, de même, nous disons que le Christ a été crucifié, que le Christ est mort et est ressuscité, mais nous ne disons pas que Dieu a été crucifié et est mort." Work: Babai, *Book of the Union*, f. 122 B, in Labourt's French. Evidence: `cic/texts/labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` lines 15887–15890, re-read ("res- / suscité" split over a line end; the footnote "De Unione, f. 122 B" is at line 15880). The file is already in `sources.ownWords`.
   - Q2. Modern: "If I had known you were with me, I would have taken on this great work with all care. But now go in peace, and pray for me." Printed: "If I had known that thou wast with me, I would, with all care, have accepted this great work; but now depart in peace, and pray for me;" Work: Thomas of Marga, *Book of Governors* I.35, tr. Budge. Evidence: `cic/texts/thomas-of-marga_book-of-governors-v2-english_budge1893.txt` lines 5185–5188, re-read (chapter XXXV begins at 4992). The file is already in `sources.about`.
   - Both printed wordings checked by the census fold (case, accents and punctuation folded; line-end hyphen joined) against their cited lines: both stand.
2. **`briefReferences`** (old: none). Eleven entries, for what the brief draws on, re-read at:
   - TM I.26 (oath, 3996–4008; Budge's note, 4012–4013); I.6 (head of the monastery, 2015–2017); I.11–14 (expulsions 2594–2599, Jacob driven out 2681–2683, the ban 2723–2726, "without fault been driven forth unjustly" 2766–2768, the scattering 3016–3023); I.21 (Jacob to Beth Abe, 3428–3432; "this monastery of Beth 'Abhe", 609); I.27 (three metropolitans, "a solitary and not a bishop", 4085–4141); I.28 (eighty-four works, 4186–4190); I.35 (refusal and angel, 5160–5188). Chapter numbers from the file's own headings.
   - Synodicon orientale, Chabot's French of the *Life of George*: communion refused to Henana's followers (42215–42219); the king's demand, the profession, and his answer on Nestorius (42365–42368, 42403–42417).
   - Labourt: Q1 (15887–15890); his judgment on the wide spread of Babai's writings (13096–13099).
   - Guidi's Latin, Chronica minora: George accused, a year in prison, crucified at Seleucia (2013–2019).
   - Braun's German *Life of George*: † 14 January 615 (852); written at the request of the faithful gathered for the feast (12426–12437).
   - World census: tradition `the-church-of-the-east-under-persia` (a Zoroastrian shah; an answer on Christ "not Chalcedon's, nor the Miaphysites'"); entry `nestorius` (bishop of Constantinople from 428; the council of Ephesus in 431). No quotation marks in `briefReferences`.
3. **`briefLength`**: not added. `card.md` asks for the brief's real length in one sentence and for no `briefLength` in another; `tools/validate-census.mjs` (`CARD_KEYS`, line 205) does not allow the key, so it is left out. (The brief is 568 words, about 3¾ minutes, per `Revision.md`.)

## Clearly wrong

None. No statement on the card is contradicted by a held source or by the finished brief.

## Not found

None. One claim was checked because `Source_Sheet.md` (Library sweep, "Set aside") says the held Latin of Mari does not name Babai: the card's `uncertain` entry "The Arabic histories of Mari and 'Amr ... say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head. Mari counts seventeen years." It stands. `cic/texts/mari-ibn-sulayman_de-patriarchis-nestorianorum-commentaria-pars-prior-ara-lat_gismondi1899.txt` lines 13517–13520, in poor OCR: "patriarcha occlosia oaruit ad annos docem ot septom, oius intoroa guberna- / tionom gorontibus Mar Aba arcliidiacono alquo Mar Babaoo Magno e coe- / nobio Mar Abraliam" (the church had no patriarch for seventeen years, Mar Aba the archdeacon and Mar Babai the Great of the monastery of Mar Abraham governing it). The source sheet's note missed this passage, probably because of the OCR.
