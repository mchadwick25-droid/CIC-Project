# Fixes: Latin Pastoral Christianity in Africa

The fix pass applies `Outline_Check.md` to `Outline.md` (and to `Source_Sheet.md` where a finding names the sheet). Every BLOCKING and MINOR finding is applied. Library lines are `cic/texts/` files.

## Applied verbatim

- **B2** (Connection, sentences 2 and 3): the check's two sentences replace them in Outline "Connection to carry into the story". The last sentence is unchanged.
- **B3** (beat 1): "In 250 the emperor Decius began a persecution of the churches, and his edict called for sacrifice to the gods (S4; CyLap 1051, 'obtemperauit eius edicto')." replaces "An emperor ordered everyone to sacrifice to the gods (S4)." The Do not say row was added as given. Checked: Eus 37413-37414 has "commenced a persecution of the churches". The universal order is only in the editor's note at 37405-37412. In `cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt`, "obtemperauit" ends line 1050 and "eius edicto" begins line 1051.
- **B4** (beat 2): the check's two sentences replace "His envoys came ... refused them communion". The Do not say row was added as given. Checked: CyL 6189-6191 ("a communicatione eos nostra statim cohibendos esse censuimus") and CyL 6228-6233 ("collegae nostri iam delecti et ordinati et laudabili multorum sententia conprobati uentilari ... pateremur").
- **B5** (Do not say): the check's row replaces the row "'Augustine hated judging' | ... forced labor (B3, B4)".
- **M2** (Length and Cut first): "**650 words** (approved). All eleven Cut first items are out of the story (Mark, 2026-11-25)" replaces the Length section's first line. "All eleven go, as marked (Mark, 2026-11-25)." replaces the Cut first preamble.
- **M3** (Sibling): "Stephen to the card (cut 8)" replaces "Stephen in one clause (beat 4)". "none here (cut 1); Manichaeism tells it" replaces "one clause, his nine years among them and what they taught (beat 5)".
- **M3** (Links): Donatism "argued against (H5)" now reads "(B9)".
- **M4** (What came of it, item 1): "Not told in the story (no beat carries it after the cuts); card, with B6." replaces "here carried by beat 5 and, if room, ... Card if cut."
- **M5**: "one who was himself stained could not wash away sins" replaces "a stained hand could not wash away sins" in beat 5 and in Words to explain. Checked: Ziwsa 590 "inquinatus".
- **M11**: "; that card text is this story's to replace" is deleted from the Q2 note. `python tools/check_tree_overlap.py` was run on a scratch brief holding the three quotes, named `latin-pastoral-congregational-christianity.brief.txt`. It printed "latin-pastoral-congregational-christianity: clear" (exit 0), so Q2 is not flagged.
- **M13**: three Do not say rows were added as given: "in Numidia"; "a stained hand"; "killed only for being a Christian" (checked at PonL 41566-41575: "inimicum te diis Romanis et religionibus sacris constituisti", "nequissimorum criminum auctor et signifer").

## Worded by me

- **B1** (length). Each of the check's seven items is struck through in place and marked "[cut: card]":
  - Ending: "At such times ... (V4)" and the Possidius sentence (V6-V8).
  - Beat 1: the money sentence (K3), with "confessor" in Explain it.
  - Beat 2: the long penance (L3).
  - Beat 4: "sent into exile and then" and the girls guarded. The people in the street are kept.
  - Beat 5: "by Possidius's account ... the larger church in Africa, and". "They lived in Hippo and the towns around it" is kept.
  - Beat 6: "; he heard them until mealtime ... forced labor (B3, B4)". The sentence now ends "(B3)".

  A line under the Cut first list records them: "Also to the card (outline check, B1), each marked "[cut: card]" where it stood: ...".

  The recount was done the check's way, on narration only: Opening 1, the essence, beats 1-6 and Ending 1, without source codes, Explain it notes or struck text. It gives 681 words. The quotes add 129 and the glosses about 40, which makes about 850, still over 650. So the check's next item went too: the Opening now reads "Their priest Augustine~~, serving under the aged bishop,~~ [cut: card] read them". The Do not say row "Their priest Augustine" is kept.

  The Length section's second paragraph now records this: "Recount, after the eleven Cut first items and the outline check's B1 items ... comes to 681 words. The three quotes add 129, and the remaining glosses ... about 40: about 850 in all. That is still over 650, so the Gladness opening's "serving under the aged bishop" goes to the card too (5 words), leaving about 845 in the outline's wording, about 195 over the approved 650."
- **B4, the beat's remaining clause**: the old ", and they went from house to house (L4-L6)" followed the replaced span and is cut 4, so it now stands as "~~They went from house to house (L6).~~ [cut: card]".
- **M1**: the essence's source list now reads "(K1, K3-K6, ...)". A new row was added to Source_Sheet.md: "| K6 | Until the church's peace returns, the bishops, meeting with the clergy and with the people who stood firm also present, are to settle everything by common counsel (on the fallen who press to be taken back) | CyL 2920-2927 (Hartel Ep. 19.2) | own words | Documented | "ut praepositi cum clero conuenientes praesente etiam stantium plebe, quibus et ipsis pro fide et timore suo honor habendus est, disponere omnia consilii communis religione possimus" |". The quoted Latin is at CyL 2924-2927, not the check's 2923-2926. "Expectent ... publicam pacem" is at 2922-2923, and "quidam de lapsis" is at 2929.
- **M2** (marks): every Cut first item in beats 1-6, the Opening and the Ending is struck through and marked "[cut: card]". The Manichaean clause is marked "[cut: Leave out]". The cut Explain it notes (confessor, the ransom's reason, the psalm's purpose) and the beat 6 note "Keep the deacon to one sentence to make room." are struck the same way. In the Ending, "that" stays outside the struck span: "Augustine answered that ~~one man ... but~~ [cut: card] when the danger ...".
- **M3** (Names, Words to explain, Links, Sibling note):
  - The Stephen and Manichaeans rows were removed from Names.
  - The rows "Stephen's rule / Cyprian's", "Manichaeans", "first teaching (catechumens)" and "sesterces" were removed from Words to explain.
  - The Roman Church link now ends "(D1); card." and the Manichaeism link ends "(H3); card."
  - Added to the Sibling field: "The slate gave Stephen "told here"; the hearts and lengths ruling sent him to the card with cut 8." and "The slate gave the Manichaean "a clause here"; the hearts and lengths ruling left it out with cut 1."
- **M6**: "; Numidia, inland, where the captives were taken (P4)" was deleted from Setting, Place. The line now ends "today's Algeria (S1)."
- **M7**: Who tells it, Pontius row, now adds: "Jerome, On Illustrious Men 68: "Pontius, diaconus Cypriani, usque ad diem passionis ejus cum ipso exsilium sustinens, egregium volumen vite et passionis Cypriani reliquit" (`jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt` 57618-57622; sheet P6)". A matching sheet row P6 was added: "Pontius was Cyprian's deacon, shared his exile up to the day of his passion, and left a fine book on his life and passion | ... | later (Jerome, more than a century after) | Documented". Checked at 57618-57622: the file breaks "egre- / gium".
- **M8**: sheet line 21 now reads "His Latin is held: **Ziwsa** = `optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt`, with `optatus_libri-vii-critical_ziwsa1893.txt` (Ziwsa, CSEL 26, 1893)." R3 adds "Ziwsa 989: "exitum est foras et altare contra altare erectum est"". R4 adds "Ziwsa 589-590: "dixisti enim fieri non posse, ut [in] falso baptismate inquinatus abluat, inmundus emundet"". "fieri non posse, ut [in]" is on 589.
- **M9**: Words to explain, the rival church's charge, now reads "had handed over the Scriptures in the persecution" in place of "to be burned".
- **M10**: What came of it, item 3, now ends "Told in the Ending. Defended." Beat 2 now ends "Defended: the refusal of a second bishop."
- **M12**: beat 2's Explain it now reads "an unlawful ordination against the bishop already chosen (L4; narrate only, no quotation marks)".
- **M14**: Openings 1 adds, after "(E1-E3, E6.)": "Keep the opening to these three sentences and Q1, with nothing added before the essence."

## Not applied

None.
