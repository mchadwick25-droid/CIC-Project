# Era 4 Who batch 11: cap check of the round 3 fixes (Mark's cap ruling, 2026-11-15)

**Scope.** The one check Mark ordered in his cap ruling ("Fix + one check", 2026-11-15). Only the strings changed in round 3 were checked (`git diff 8caf6392 c9c4ced2`), against R3_review.md and R3_changes.md. Untouched text was not reviewed, except one clause in the sentence on the Christopher note, which the ordered confirmation covers (R4-M1). One fresh Opus checker, full effort, read and grep only.

**Method.** I read CLAUDE.md, lessons.md, R3_review.md, R3_changes.md and the diff. I reopened each source line with `sed -n` and `grep -n`:
- AASS (acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt) l.50552-50560, l.50598-50626, l.53318-53345, l.53410-53440, l.53455-53490.
- NIK1 (nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt) l.23270-23293.
- ALV l.31683-31692. EVETTS (abu-salih_churches-and-monasteries-of-egypt_evetts1895.txt) l.15205-15216. QUATREMERE l.14025, l.14030-14054.
- WEIL (ibn-ishaq_leben-mohammeds-nach-ibn-hischam-deu_weil1864.txt) l.9574-9595 and l.1090-1094.
- cic-website/data/world-census.json, release 44, `movements[53]/documentedStories[1]/sources`.

I loaded the three changed cards and `records.json` as JSON, compared Stephen's audio with his brief by script, and scored his brief with `engine.m1.gates.grade_text`.

## Round 3 findings

- **R3-AM1** (README, bare "Tamayo", three lines): applied as worded. "Oscitantiam Joannem Tamaii ... hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre" (scan "Ozxcitantiam"; ALV l.31684-31689, inside l.31683-31716). All three lines now read "Juan Tamayo". Holds.
- **R3-BB1** (Stephen card `uncertain` "The year", records `contested_claims` side 2, the 789 + 7 arithmetic): applied as worded. Holds; see "The Christopher note" below.
- **R3-BM1** (Stephen, "It ends with" / "He ends by"): applied as worded in the card's "His name", the brief, the audio and `keyWorks[1]`. "Quin et indigni famuli vestri reminiscimini, despicabiles vobis sermonis sui primitias offerentis, atque accinentis hymnos" (AASS l.53325-53328) is para 80. Paras 81-83 follow, and "Amen" closes the account (l.53464). "Near its end" and "near the end" hold. In "His name", "its" goes to the account and "he" to the writer. In the brief, "he" follows "Stephen argues that they were martyrs all the same." It resolves to Stephen.
- **R3-BM2** (Stephen card "Which Stephen", "He"): applied as worded. "This Stephen was a monk of the laura who flourished in 790 and later became a bishop." holds against NIK1 l.23272-23291: "ΣΤΕΦΑΝΟΥ τοϋ Σαΰΰαίτου" (l.23273), "ήκμαζεν έν ετει ψ/ (790)" (l.23278), "τήν Λαύραν τοϋ μεγάλου πατρός Σάββα" (l.23279-23280), "ήξιώθη καί τοϋ χαρίσματος της άρχιερωσύνης" (l.23290-23291). The bishop can no longer attach to the Poet. 17 words.
- **R3-BM3** (records, Acts-side range): applied as worded. "septingentesimo octogesimo octavo" is at l.50619, "Indietione quinta" at l.50620, and Elias and Basil at l.50621-50623, all inside the new l.50600-50624. AM 6288 is at l.50556-50557.
- **R3-BM4 / R3-CM-R2** (README Stephen census bullet, Acts range): applied once, as worded. "(l.50556-50557, l.50619)" covers both AM 6288 (l.50556-50557) and 788 (l.50619).
- **R3-CM1** (al-Tabari `legacy.traces[2]`): applied as worded. "AL-MAKRIZi (died A. H. 845 = A. D. 1441)" is a heading in Evetts's book (EVETTS l.15213), so "Evetts says" holds. Quatremère quotes al-Maqrizi: "La bibliothèque des khalifes, dit Macrizy" (QUATREMERE l.14025), with Aziz's twenty copies of Tabary at l.14048-14051. Evetts is introduced in `traces[1]`. The sentences are 8 and 13 words.
- **R3-CM1** (Ibn Ishaq `uncertain[6]`, "nothing other than this"): applied as worded. The source is "nichts Anderes als diess war" (WEIL l.9592-9593). Holds.
- **R3-CM2** (Ibn Ishaq records, revolt claim range): applied as worded. "„Du" ends l.9588, "hast onsem Glauben" is l.9589, and "Wir sagen, er ist Gottes / Sohn" is l.9590-9591. Both quotes are inside l.9588-9591. Verbatim, with "onsem" marked.
- **R3-CM3** (Ibn Ishaq records, Faymiyun claim scan mark): applied as worded. The scan reads "Wahb Ihn / Munabbah" (WEIL l.1092-1093). The quote with (scan "Ihn") verifies.
- **R3-CM-R1** (README, Ibn Ishaq census sentence): applied as worded. The census lists four sources: Simeon of Beth Arsham, the Book of the Himyarites and Procopius, Wars I.20 (all "primary"), and Bowersock, The Throne of Adulis ("reference"). The new sentence is true and complete.

## The Christopher note (R3-BB1)

Note e reads: "— e Adeo- / que anno Christi 189, quando Pascha incidit in 19 Aprilis sep- / tennio ante horum Patrum passionem." (AASS l.53478-53480). It annotates "feria tertia e" (l.53435), the Tuesday of Holy Week, 14 April, on which Christopher was beheaded (l.53420-53436).

- Card: "Their note on the martyr Christopher, a convert from Persia whom Stephen names, puts his death in 789 (the scan reads 189), seven years before the twenty." The sentence "The note names no year for the twenty, and seven years after 789 is 796." is gone. The sum is gone, and nothing points the note at 796. What remains is the note's year and its "septennio ante". One unchanged pronoun in this sentence can make it say more than the note (R4-M1).
- Records side 2: "their note e puts Christopher's death in 789 (scan 189), seven years before the twenty's passion, and names no year for the twenty (l.53478-53480)". "the twenty's passion" renders "horum Patrum passionem". "names no year for the twenty" states only what the note lacks, and draws nothing from it. The range includes all three lines.
- A grep of the batch for "seven years", "789" and "796" finds no other arithmetic on the note, in the card, records, brief or README.

**Held placings of the raid year, all still on the card (`uncertain` "The year"), each with its owner:**
- The Acts: "the year of the world 6288, AD 788, in the fifth indiction" (l.50556-50557, l.50619-50620).
- The Bollandists' essay on the chronicle of Theophanes the Confessor, and the volume's index of dates: 797.
- Their margin: "just after Easter of 797".
- Their commentary: "One figure in the scan of their commentary reads 796. That passage goes on to add the missing year, to reach the fifth indiction." The reasoning is kept just before it ("counted by the Alexandrian era, which runs eight years behind theirs, and left out one year").
- Graf: "puts the massacre in March 796 or 797".

## Audio and score

Stephen's audio equals his brief, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph ("[warmly] Near the end, he asks ..."). Both end in a newline. The three changed cards and `records.json` parse and end in a newline.

`grade_text` on stephen-of-mar-saba.brief.txt: 338 words, FK 6.17, Flesch 75.80. That passes FK ≤ 10 and Flesch ≥ 60. 338 words is within about 2:05, and the README's "336 to 338 words, about 2:04" still holds.

## Writing check on the new strings

No new string has "X, not Y", "not X but Y", a colon reveal, a tail or drafting-process language. No sentence in participant text passes about 25 words. The longest is the README census sentence (33 words), which is not participant text. The new names all have an identifier: Juan Tamayo, al-Maqrizi ("The historian"), Evetts (introduced in `traces[1]`), and "This Stephen".

## New findings

**R4-M1 (Stephen card `uncertain` "The year", the Christopher sentence: "his death" reads aloud as Stephen's).** This clause was not changed in round 3. I checked it because Mark's check asks whether this sentence says only what note e says. Note e (AASS l.53478-53480) dates the death of Christopher, which the account gives at l.53420-53436. In "Their note on the martyr Christopher, a convert from Persia whom Stephen names, puts his death in 789", the nearest noun before "his" is Stephen. Heard aloud, the card can say the writer died in 789, eight years before the raid he saw. Note e does not say that. Records side 2 already says "Christopher's death". The fix is word-neutral, and the brief does not mention Christopher.
- Card: "whom Stephen names, puts his death in 789 (the scan reads 189)" → "whom Stephen names, puts Christopher's death in 789 (the scan reads 189)".
- Records: no change.

**Verdict: CLEAR.** All 12 round 3 findings (R3-BB1 and 11 minor) were applied as worded and hold against their sources. Every cited range includes its line. The Christopher note now gives only note e's own year and "seven years before", and every held placing of the raid year stays on the card with its owner. Blocking: 0. Minor: 1 (R4-M1, a word-neutral pronoun fix to apply without a further round).
