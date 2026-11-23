# Outline check: John Cassian (`john-cassian`)

## My own account, written before reading Outline.md

**Essence.** A monk who spent years among the elders of Egypt and then, settled at Marseilles, wrote down what he had learned there in Latin, in the Institutes (the monks' customs and the eight principal faults with their remedies) and the Conferences (the elders' talks as he told them). Those books carried the desert's teaching into the Latin West, where the Rule of Benedict had them read aloud to monks. That is why he is on the tree.

**Also told.** His start at Bethlehem with Germanus and the seven years in Egypt, against a promise to return; ordination as deacon by John Chrysostom at Constantinople, and the clergy's letters he and Germanus carried to Rome after John's exile; the two houses at Marseilles, one for men and one for women (Gennadius); the books written for Castor, Leontius and Helladius, Honoratus and Eucherius, with his choice to leave out wonders and to soften Egyptian rigor for Gaul; On the Incarnation against Nestorius in 430, at Leo's request; Conference XIII on grace and free will, the Marseilles doubts reported to Augustine, Prosper's attack and no known reply; and his later reading: Benedict's Rule, Cassiodorus ("read with care", "with caution" on free will), Gennadius taking his side, Gregory of Tours's house that kept his rule. The later label "semi-Pelagian" is not his and is not told as his. Death at Marseilles, year unknown.

Sources hold all of this at the sheet's lines (own words for Egypt, the books and Conference XIII; Palladius and Innocent for the mission; Gennadius for the deacon, the houses and Leo; the Rule, Cassiodorus and Gregory for the later reading).

## Verdict: FIX

The heart matches my account in substance: Egypt, the Latin books for Gaul, their reading under Benedict's Rule, and Conference XIII drawing Prosper's attack, with "semi-Pelagian" kept off him. No major contribution is missing from the heart. The beats tell the essence in the first minute and then follow the life in order. Every quote checks verbatim against its source. Three findings block: one overstatement in the essence, one event told twice, and one major held witness the sweep missed.

## My renderings, made before comparing

- Q2 (N211 38028-38030): "These two, God's grace and free will, seem to be against each other. In truth they agree." The outline's rendering keeps every clause and adds nothing. It holds.
- Q3 (N203 43669-43671): "The church of God finds them healthy; he brands them as harmful." The outline's rendering holds. It is lifted on the slate for this job, and `Allowed_Reuse.txt` lists both spans.
- Q1 (N211 25945-25952): "May we set before you the men themselves, living, as it were, in their own rules. And, more to the point, may they speak in Latin." The outline's rendering holds, and so does its note on "Institutes".
- I ran `tools/check_tree_overlap.py` over these spans and the outline's other quoted phrases, and the census search found none of them elsewhere on the tree. The only hits were Cassian's own entry and a Zwingli "Latin tongue" that is a different text.

## Findings

**B1. BLOCKING: the essence, What came 1 and the Connection overstate Benedict's Rule.** RB 6830-6850 and 6876-6893 set the after-supper reading as "the Conferences, or the lives of the Fathers, or something else which may edify". The Conferences are named outright only for fast days, after Vespers. The "four or five pages" also belongs to the fast-day reading. "Had the Conferences read aloud to monks every evening" and "fixed them as nightly reading" say more than the Rule does.
- In the essence, replace "A century later, Benedict's Rule had the Conferences read aloud to monks every evening." with "A century later, Benedict's Rule named the Conferences first among the books read aloud to monks in the evening, before night prayer."
- In What came 1, replace "After supper, the Rule says, the monks sit together and one reads the Conferences aloud, four or five pages, or as much as time allows." with "After supper, the Rule says, the monks sit together and one reads aloud: the Conferences, or the Lives of the Fathers, or something else that builds up the hearers. On fast days it is the Conferences, four or five pages, or as much as time allows."
- In the Connection, replace "Benedict's Rule fixed them as nightly reading (RB 6838-6846)" with "Benedict's Rule named the Conferences for the monks' evening reading (RB 6838-6846)".
- Add to Do not say: "'read every night' or 'Benedict's monks read the Conferences every evening'. Say: the Rule names them first for the evening reading, and orders them on fast days."
- For "A century later", add the cite RB 150 (Hunter Blair: "About 535 a. d.").

**B2. BLOCKING: the ordination is told twice.** Beat 2 tells how John admitted him to the ministry, sourced to N211 55142-55145. Beat 6 then tells it again: "He wrote that Bishop John had admitted him to the ministry, and that though absent in body he was still there in heart." That puts one event in two beats and sends the listener back after the essence.
- Delete that sentence from beat 6, and drop "55139-55147" from beat 6's Source.
- The writer may keep the image in beat 2, as his own later words. After "admitted him to the ministry", add "(years later he wrote that, though absent in body, he was still there in heart; N211 55142-55145)".
- This saves about 25 words.

**B3. BLOCKING: the Library sweep missed a major held later witness.** `cic/texts/philokalia_ton-ieron-neptikon-v1-grc_tzelatis1893.txt` holds Cassian's works in Greek, as "ΚΑΣΣΙΑΝΟΥ͂ ΤΟΥ͂ ΡΩΜΑΙΟΥ͂" (Cassian the Roman), at 6133-6183 and the headings at 6567, 7239, 7629, 7902, 8197, 8485 and 8768. The pieces include his works to Castor on the eight thoughts and on discernment. The editor's preface (6136-6183) dates him under Theodosius the Younger, about 431. It quotes Photius on these works, and it says the Church keeps his memory on 29 February ("κατὰ τὴν κθ΄ τοῦ Φεβρουαρίου"). `nikodemos-hagiorite_synaxaristes-vol2-mar-aug-grc_1900.txt` 53996 indexes "Κασσιανὸς ὁ Ῥωμαῖος, Φεβρουαρ." This is the Greek East reading his books, and the sheet's search for "Κασ(σ)ιαν" should have found it. It also falsifies the outline's Leave out reason for Eastern veneration ("an 1894 report, not a held statement").
- Add to the sheet's impact section: "I9. Read in Greek in the East: the Philokalia (1782; held print 1893) prints his pieces on the eight thoughts and on discernment as Cassian the Roman's, and its preface says the Church keeps his feast on 29 February (philokalia v1 6133-6183). Later (about 1,350 years). Documented that the Philokalia prints and commemorates him."
- Add the file to the sweep's Used list, and the Synaxaristes line to the Set aside list (index only).
- In the outline, replace the Leave out line "His title 'the blessed Cassian' and Eastern veneration (N211 15944-15956): an 1894 report, not a held statement of today. Card." with "Read in Greek in the East: the Philokalia prints his pieces on the eight thoughts and on discernment as Cassian the Roman's, and its preface gives his feast as 29 February (philokalia v1 6133-6183). Card; the story has no room for a Greek strand. 'The blessed Cassian' (N211 15944-15948): card."
- The "Who keeps him today" line may stay out: the source is of 1782/1893, not of today.

**M1. MINOR: the Length line disagrees with the count.** It says "4 minutes, about 600 words", but its own count (and `Length_Count.md`) is 724 before the cut list and 663 after it. Replace it with "Length: about 4:25, 663 words after the Cut first list (cap 675); 724 before it." After B2's cut it falls to about 638; say so if the fix pass recounts. I recounted the carry: three quotes of about 55 words, eight glosses of about 45, and ten credits of about 70. That agrees with the outline. With B1's longer wording added (about +20), the outline still fits under 675 once the list is cut.

**M2. MINOR: beat 2's receipt adds to Palladius.** PAL 2646-2654 has "valuables in gold, silver, and clothing" deposited "with the magistrates". He does not say they were the church's. Replace "the church's gold, silver and robes had been handed to the city's officials" with "valuables in gold, silver and clothing had been left with the city's magistrates".

**M3. MINOR: beat 3 drops half of Cassian's reason for tempering.** PET 7996-8003 and N211 16526-16534 give the harshness of the climate "or the difficulty and difference of customs". In beat 3 and Also told, replace "too hard for Gaul's harsh climate" with "too hard for Gaul, for its harsher climate or its different ways".

**M4. MINOR: beat 5's dates lack their lines.** Cite "429" to N211 15724-15726 (editor: "This fixes the date of the correspondence as 429"), marked Dominant Modern Reconstruction. Cite "Conference about 426" to N211 15546-15552 (Part II, "not later than that year"), also Dominant Modern Reconstruction.

**M5. MINOR: "His friend Eucherius" (What came 4) and "a priest of Marseilles" (What came 2).** Gennadius does not call Eucherius a friend. Replace it with "Eucherius, one of the two he wrote seven Conferences for, later bishop of Lyons" (N211 36721; N203 43288-43297). Cite Gennadius's priesthood to N203 43968-43969 ("I Gennadius, a presbyter of Marseilles").

**M6. MINOR: "the Rule of Cassian" in What came 4 is quoted.** It would count as a fourth quoted span in the brief. Tell it in the narrator's words: "kept Cassian's rule beside Basil's".

**M7. MINOR: the Connection asserts an absence.** "Later monks did not come from his houses" is not in any source. Replace it with "the record shows later monks reading his books, not coming from his houses".

**M8. MINOR: Names and beat 2 disagree on Innocent.** Beat 2 names "Innocent, bishop of Rome", while Names gives him by role. Either add "Innocent I, link (received the letters)" to Names, or say "the bishop of Rome" in beat 2.

**M9. MINOR: Do not say gaps.** Add these:
- "he spent seven years in Egypt" (as the whole stay). Say: after seven years they went back to keep their promise, then returned to the desert (N211 42239-42249).
- "the Abbey of Saint-Victor" or a named house. Gennadius names neither house.
- "Augustine wrote against Cassian" or "Augustine answered him". The held letter does not name him (N211 15721-15724).
- "Chrysostom ordained him priest". Say: deacon, in Gennadius's word.

## Checked and holding

- Beats 1, 2 (apart from M2), 3, 4, 6 and 7 hold at their cited lines, with the right witness kinds and confidence levels. That includes the seven years, Palladius and Innocent, Gennadius on the deacon and the two houses, the books for Castor and the soft-pedalled wonders, Part II for Honoratus and Eucherius, Leo the archdeacon, the tie of Nestorius to the Pelagians, Prosper's title and Gibson's twelve propositions, and the death in the reign of Theodosius and Valentinian.
- Opening 1 holds at N211 36717-36737.
- The glosses hold: the eight faults at N211 15347-15350, and Nestorius at 48516-48519.
- The Do not say items on Martin (N211 15443-15447) and "papa" (16417-16419) hold.
- Cassiodorus holds at CAS 83928-83951: "sedulo legite, et libenter audite".
- Gregory holds at GT-E 22152-22155.
- The shape (Monk or ascetic) fits. The ranking (the Rule, then Gennadius, Cassiodorus, and Gaul) is right. The thing he defended is marked.
- The tradition's spoken name, "the monks of Gaul", does not mislead.
- Sibling: none, as the slate set it. Each link keeps its job.
