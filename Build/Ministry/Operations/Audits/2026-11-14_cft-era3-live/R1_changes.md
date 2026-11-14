# Era 3 on the live tree (release 42): changes after review round 1

Each finding of `R1_review.md` and what was done. The old and new census text is in `Census_Text_Changes.md`.

## Blocking

- **B1. Fulgentius and Victor of Vita in the Non-Nicene river.** Both are now told within no tradition, in the Africa river, as Boethius is in Latin West. The Homoian voice row for Victor of Vita stays a named row. The choice is put to Mark in the preview's question 2, with the Homoian placing as the alternative.
- **B2. The Nisibis story.** Rewritten so each witness carries only what it holds. Barhadbshabba praises Henana. The synods of 585 and 596 condemned teaching Labourt takes as aimed at Henana, and the acts never name him (Braun). The Chronicle of Seert tells of Gregory's condemnation, the king's physicians, Sabrisho taking Henana's side (with Labourt's contrary reading of Sabrisho's synod) and the walk-out of about three hundred, leaving twenty and scarcely as many boys. The governor's protection, which no held line gives, is gone. With M9, Henana's death is told as Scher's notes give it. The Chronicle of Seert source note names what it holds.

## Substantial

- **S1. Liberatus.** The caveat now says he mentions bishops rewarded, deposed, exiled or in hiding but passes over the details, and that Jean Garnier takes him to mean the Africans, Reparatus among them.
- **S2. Philoxenus.** Dates line now "bishop 485 to 518 or 519" (Budge's 485 and his reading of the year 830).
- **S3. Julian and Longinus.** Places now "Constantinople · the land of the Nobadae", with no id.
- **S4. Voices.** The Julian line (no 543, no "Nobadia") and the Benedict line (543, by his order's tradition) now agree with their cards. The other 247 items: Theodosius's "patriarch from 535" rests on Evetts's heading and Brooks's notes, which are held; Longinus's "around 580" is R. Payne Smith's held reckoning. Both stand and are named in the Decision-Log.
- **S5. Isidore.** Story: "In 633 the bishops of Spain met at Toledo ... to legislate for church and kingdom together. Isidore of Seville's name stands first among their signatures." Teaser: "The bishops of Spain, with Isidore of Seville's name first on their acts, declare forced baptism wrong".
- **S6. The Ladder.** "John Climacus wrote the Ladder of Divine Ascent at Sinai, in the later 500s or about 600. The Greeks held it in great value, Philippe Labbe says, and Elias of Crete wrote explanations of it."
- **S7. The rendering rule.** Replaced by `tools/quote_renderings.json`, which lists the 14 renderings by entry, span and original (file and lines). The check skips exactly those spans and fails when a listed span no longer stands in its entry; a tamper test confirmed both errors. The old comment is updated.
- **S8. Release records.** `Census_Text_Changes.md` is written; the Decision-Log entry and the Open-Gaps closures and carry are added.

## Minor

- **M1.** The Maccurritae lines now say "not settled" and "thought them a people of Mauretania"; source notes point to the caveat; "John of Biclaro" throughout the entry and its link.
- **M2.** Caesaria: "The second greets her as a holy sister".
- **M3.** Victor of Tunnuna: "Note to section 91 of the Life of Antony"; the ANF item is "Introductory Note to Part I".
- **M4.** Dates lines: Cassiodorus "c. 480-c. 575", Columbanus "c. 543-c. 615", John of Ephesus "c. 507-c. 586", Marius "bishop c. 574-594", Theodosius "patriarch 535-566 or 567", Ferrandus "6th c.; esteemed in 546", John of Biclaro "home c. 576; a John of Gerona signs in 610", Dionysius "at work c. 500-525; dead by 556". Benedict's "c. 480-543" stands: both held writers give 543.
- **M5.** Severinus at Noricum only; John Rufus at Antioch and Maiuma. `regions` stays the home tradition's, as in release 41 (no page reads it); carried in Open-Gaps.
- **M6.** Constantius of Lyon and Gennadius are named in the Decision-Log as the worker's calls.
- **M7.** Victor of Vita: "nostrae civitatis" (of our city). Moses of Khoren: The "nouveau Platon", new Plato.
- **M8.** A dropped range must now hold exactly its declared lines (`lines_held`) and blank lines.
- **M9.** Henana's death fixed with B2. The statutes' year (602) is carried in Open-Gaps.
- **M10.** Constantius: "And yet I call God". Faustus: "We walk the middle way, then". The Moschus "he said" stands.
