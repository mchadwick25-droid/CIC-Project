# Card edits: Thomas à Kempis

Card written to `thomas-a-kempis.card.json`, from `thomas-a-kempis.original.card.json`. Every other field is word for word. Files are in `cic/texts/`.

## Clearly wrong

1. **`briefLength`.**
   - Old: "about 2 minutes 30 seconds"
   - New: "about 2 minutes 40 seconds"
   - Evidence: the finished brief is 400 words (`wc -w`; 398 by the profiler, Recheck.md). The writer's rate is about 150 words a minute (`Brief-Kit/roles/writer.md` line 8), which gives 2 minutes 40 seconds.

2. **`legacy.traces`, the Ignatius entry.**
   - Old: "Ignatius of Loyola told the story of his life to Consalvius de Cámara. In Spanish he said that at Manresa"
   - New: "Ignatius of Loyola told Consalvius de Cámara, who wrote it down in Spanish in 1555, that at Manresa"
   - Evidence: the Gerçonzito passage is not in the story of his life (the Acta). It is no. 97 of Câmara's Memoriale (`ignatius-loyola_scripta-de-sancto-ignatio-tomus01-lat-spa-ita_1904.txt` 9403–9406, under the running head "MEMORIALE P. CONSALVII DE S. IGNATIO", 9255). The Memoriale was begun on 26 January 1555 and covers ten months of that year (765–766, 775–776). Brief: "A fellow Jesuit, Luis Gonçalves da Câmara, wrote down in 1555 what Ignatius told him".

## New

3. **`sources.ownWords`: two entries added** after the Pohl treatises volume.
   - Pohl, *Opera omnia* II, 1902: `kempis_opera-omnia-sermones-de-compunctione-lat_pohl1902.txt`. It opens with the Latin Imitation, Book I (595–605: "Thomae a K. Opera. II." and "[DE IMITATIONE CHRISTI ... LIBER PRIMVS]"). The brief's first quotation comes from it.
   - Pohl, Sermons to the Novices, 1905: `kempis_opera-omnia-sermones-ad-novicios-lat_pohl1905.txt` 254–261 ("pro noviciis nostris ... in unum collegi ... simplicibus placere cupiens"). Brief: "Thomas gathered into one book the talks made for the novices ... in plain speech for simple minds."

4. **`sources.about`: two entries added** at the end.
   - Methodist Conference Minutes I, 1862: `methodist-conference_minutes-v1-1744-1798_1862.txt` 2648–2653, the 1746 conference ("From four to five in the morning ... Kempis"). Brief: "His Methodists set it for their preachers' early mornings."
   - Woolman, Journal and Essays, ed. Gummere 1922: `woolman_journal-and-essays_gummere1922.txt` 12189–12192 ("lived & died in the profession of the Roman Catholick Religion ... a man of a true Christian spirit"). Brief: "The Quaker John Woolman, told Thomas was a Roman Catholic, judged him a man of a true Christian spirit."

5. **`briefReferences`: added**, seventeen entries, one for each source the brief draws on. Lines re-read: Chronicle (arthur1906) 1052–1055, 1068–1077, 1100–1106, 1189–1195, 1816–1829, 1883–1915, 292–300, 3413–3417, 3421–3424; Benham 490–491; Founders 8990–9033; Pohl VI 254–261 and Scully 1010–1020; Pohl II 704–706; Busch 5410–5415; Ingram 1176–1186; Exercises 3101–3105, 24995–25000; Neale 4716–4722; Scripta 9403–9406, 9431; Wesley 960–963; Methodist minutes 2648–2653; Woolman 12189–12192.

6. **`quotationOriginals`: added**, the brief's two quotations.
   - "I would rather feel sorrow for sin than know how to define it." Printed: "Opto magis sentire compunctionem : quam scire eius definitionem." Pohl II 704–706, Imitation I.1.
   - "At Manresa he had first seen the little Gerson. ... He read one chapter a day, in order." Printed, OCR as the file has it: "que en Manrresa auia visto primero el Ger^onzito, y nunca m^ auia querido leer otro libro de deuoci6n; y este encomendaua A todos los que trataua, y leya cada dia vn capitulo por orden;" Scripta 9403–9406, Câmara's Memoriale no. 97. The line-break hyphen in "deuo-ci6n" is joined, and the footnote mark after "Ger^onzito" is left out.
   - Both modern renderings match the brief word for word.

## Not found

None of the card's claims went unsupported in the lines opened.

## For the brief, not changed here

- The brief says: "In 1429 a disputed election for bishop of Utrecht brought a papal ban on church services. The canons kept it and stopped singing". The Chronicle puts Sueder's confirmation, the interdict and the end of the singing under 1425 ("In the same year Sueder of Culenborgh was confirmed", 1816, within the 1425 entry from 1777; "we ceased from our singing", 1823–1824). It dates only the exile to 1429 (1883–1904). The card's "in exile from 1429" is right. Raised for the reviewer; the brief is not mine to edit.
