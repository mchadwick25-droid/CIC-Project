# Era 4 Who batch 11: round 3 review (targeted recheck, the last round allowed)

Three parts, each by a fresh Opus agent at full effort that had seen neither the drafting nor rounds 1-2, against R2_review.md and R2_changes.md and the round 2 diff (git diff a9674142 b5929511). Totals: 1 blocking, 11 minor (Part A 0 and 1, Part B 1 and 4, Part C 0 and 6). Every round 2 blocking fix (R2-AB1, R2-BB1, R2-BB2, R2-CB1) was independently re-confirmed; R3-BB1 is new, from round 2's own fix wording. It is open at the cap and goes to the coordinator for Mark's cap ruling.

## Era 4 Who batch 11, round 3 review: PART A

**Scope.** A targeted recheck of the round 2 changes to `stepanos-of-taron`, `eulogius-of-cordoba` and `paulus-alvarus`: brief, card, `records.json` entries and audio, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch11/`, plus the README lines changed for them in round 2 (the length line; "Other profiles", Paulus Alvarus; "Corrections to the re-score", Alvarus (l.134); "Names and ids", Eulogius of Cordoba and Paulus Alvarus). Untouched text was not re-reviewed. I tripped over nothing plainly wrong in it.

**Method.** I read CLAUDE.md, `Who_Profile_Pattern.md` with its checklist, `lessons.md`, R2_review.md Part A with its README section, and R2_changes.md Part A with the README log. I worked from `git diff a9674142 HEAD` over the batch folder. I reopened each source line behind a changed string with `sed -n`:
- CHAB (michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt) l.1-12, l.45-55, l.38262-38330;
- MAC (stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt) l.736-802, l.973-978, l.4340-4350, l.15208-15215;
- ZAK (zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt) l.26012-26022;
- CONY (rituale-armenorum-lectionary_conybeare1905.txt) l.1-15, l.2578-2581;
- EUL (eulogius-cordoba_opera-with-alvarus-vita-eulogii-pl115-lat_migne1852.txt) l.56812-56824, l.68012-68022;
- ALV (paulus-alvarus_confessio-epistolae-indiculus-luminosus-pl121-lat_migne1852.txt) l.31012-31076, l.31680-31720.

I ran score.py, which rebuilt the audio; `git status` showed no file changed, so the audio already matched. I compared each audio file with its brief by script, and loaded both cards and `records.json` as JSON. No README census bullet of my part changed in round 2, so census.json was not needed.

**Quotations.** No changed brief or card string of the three uses quotation marks. The changed quotes in `records.json`:
- "Sur ce concile, cf. le récit d'Etienne Asolik, trad. Dulaurier, p. 131" (CHAB l.38282-38283, inside l.38282-38284): verified. The signature "(J. M,)" (scan for "(J. M.)") is at l.38284, inside the new range.
- "régnèrent à Ani" (scan "régnérent", MAC l.976, inside the new range l.975-976): verified.
- "Matriti, dum ... legatus" (ALV l.31036 and l.31059, inside l.31019-31036 and l.31058-31075): verified.

**Audio.** All three audio files equal their brief, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. Final newlines are present.

**Scores.** (score.py, 162.5 wpm)

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| stepanos-of-taron | 336 | 2:04 | 6.7 | 69.1 |
| eulogius-of-cordoba | 336 | 2:04 | 6.9 | 69.5 |
| paulus-alvarus | 336 | 2:04 | 7.9 | 63.3 |

All three are under about 2:05 (338 words), so no README exception is needed. All pass FK ≤ 10 and Flesch ≥ 60. The README's "336 to 338 words, about 2:04" matches all eight scores.

**Round 2 findings.**
- R2-AB1 (blocking; independently re-confirmed, holds): confirmed, applied with change. The note cited is note 6 of a block on Book XI, ch. xx, and it ends "... trad. Brosset, p. 252. La note de Brosset, p. 75, est inexacte. (J. M,)" (CHAB l.38282-38284). Chabot signs the volume as "J.-B. CHABOT" (l.50) and says in the next note block that "M. J. Marquart ... a bien voulu me communiquer les notes qui accompagnent cette liste" (l.38314-38315). So the note is in Chabot's edition, and it is not Chabot speaking. The new card text, "A note in Jean-Baptiste Chabot's French edition of Michael the Syrian's Chronicle points to Stepanos's account of the synod of Manazkert.", claims only that. "Sur ce concile" refers to the council at Manazkert of notes 5-6 (l.38279-38282), so "the synod of Manazkert" holds. The fixer's "Stepanos's" for "his" is right: aloud, "his" would go to Michael. Not naming J. M. as Marquart is right too, since the note does not spell out the initials. The records claim and the range l.38282-38284 match the card. The `sources.about` entry ("Michael the Syrian; Jean-Baptiste Chabot (tr.)", "notes") still describes the file correctly.
- R2-AM1: confirmed, applied. "In his youth, Stepanos writes, he saw some great teachers in their old age." The source line is MAC l.4346-4348 ("Dans notre jeunesse, nous avons vu nous-même quelques-uns de ces [Pères], qui étaient déjà avancés en âge"), as the fixer says, not l.4302-4304. Records claims[7] already cites l.4346-4348.
- R2-AM2: confirmed, applied. "no one knows when Stepanos died" holds against "Du reste on ne sait pas qüand mourut l'auteur" (ZAK l.26019-26020).
- R2-AM3: confirmed, applied. Emin's "Asolik aurait encore été en vie entre 1041 et 1045" and "il mourut âgé d'environ 117 où 129 ans" (MAC l.740-743), Malkhasiants's "tout à fait invraisemblable" (l.762-764), and Macler's "le même Grégoire a écrit jusqu'en 1097 [scan], et l'on [pourrait] aussi bien dire qu'Étienne de Tarôn était encore vivant à cette date" (l.754-756) all hold. Each sentence is under 25 words. The closing "Brosset ... when he died" now follows a sentence whose subject is Stepanos.
- R2-AM4: confirmed, applied with change. The fixer's order follows the source: "on croit [qu']il était chantre et marie [garbled] du Tarôn. Mais, écrit Alichan, une liste des historiens distingue deux Étienne" (MAC l.788-793). Alishan is introduced earlier in the card (`uncertain[3]`, "Ghevond Alishan, an Armenian scholar"). "Stepanos" in place of "he" removes the ambiguity the reviewer's wording would have left.
- R2-AM5: confirmed, applied. MAC l.975-976 reads "Asolik est lhistoriographe des rois arméniens de la [dynastie] Bagratouni (Bagratide) qui régnérent à Ani".
- R2-AM6: confirmed, applied. "Rituale Armenorum" and "Clarendon Press, 1905" are at CONY l.1 and l.6. Macler's "M. Conybeare (Rituale Armenorum, p.xxxm) estime qu'Étienne Asolik dut écrire son histoire entre 991 et 1019" (MAC l.799-801) supports "as Macler reports". The scan "19190" is at CONY l.2580.
- R2-AM7: confirmed, applied. "when Muslim emirs ruled Cordoba". "Cordube civitatis" is at EUL l.56819 ("genius (1), Cordube civitatis patriciz (2) senato-"), as the fixer says. Para 6's "The city's Christians" now has Cordoba as its referent.
- R2-AM8: confirmed, applied with change. "Nos inde ... habemus exemplum, transcriptum ex altero nobis communicato ex amplissima ... cardinalis Barberini Romana bibliotheca, in qua asservatur: olim eidem, ... Matriti, dum ... a latere venisset legatus, ab eodem Thoma Tamaio de Vargas ... scriptum et oblatum" (ALV l.31029-31036, l.31058-31061). Both new sentences hold: the copy is kept in the cardinal's library at Rome, and it was given to the cardinal himself at Madrid. "it" resolves to the copy in the library. The records claim adds "Matriti, dum ... legatus", inside the range.
- R2-AM-R1: confirmed, applied as worded on all three lines. Both sides hold against ALV l.31683-31708. Tamayo "hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre" (l.31685-31689), and his note reads "non carnis nexu, sed contubernii vinculo" (l.31703-31705). Antonio holds "fratrem vere germanum Eulogii alterum Alvarum" (l.31710-31711). EUL l.68018 has "fratres meos Alvarum et Isidorum". A small namesake point on the new wording is R3-AM1.

## stepanos-of-taron

**Verdict:** pass (0 blocking, 0 minor). R2-AB1 holds on independent re-confirmation. I reread the brief in full for flow: the two pronoun fixes resolve aloud, and nothing else in it changed.

## eulogius-of-cordoba

**Verdict:** pass (0 blocking, 0 minor). I reread the brief in full: "Cordoba" in para 2 gives para 6's "The city's Christians" its place.

## paulus-alvarus

**Verdict:** pass (0 blocking, 0 minor). The card's brief did not change in round 2.

## README

**R3-AM1 (README "Other profiles", Paulus Alvarus; "Corrections to the re-score", Alvarus (l.134); "Names and ids", Eulogius of Cordoba and Paulus Alvarus): a bare "Tamayo" has a namesake on the same card.** The view belongs to Juan Tamayo: "Oscitantiam Joannem Tamaii nunquam satis demirari possum, qui ... hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre" (scan "Ozxcitantiam Joannem Tamaii"; ALV l.31685-31689). The Alvarus card also names Thomas Tamayo de Vargas, the royal chronicler (`legacy/traces[0]`). The README's Eulogius bullet says "Juan Tamayo's view", but the "Corrections" and "Names and ids" lines stand in other sections with a bare "Tamayo".
Fix:
- "Other profiles": "give both Tamayo's view that he was Paulus Alvarus" → "give both Juan Tamayo's view that he was Paulus Alvarus".
- "Corrections": "and Tamayo took for Paulus Alvarus (ALV l.31683-31716)." → "and Juan Tamayo took for Paulus Alvarus (ALV l.31683-31716)."
- "Names and ids": "Tamayo took the two for one (ALV l.31683-31716)." → "Juan Tamayo took the two for one (ALV l.31683-31716)."
No card or records change is needed. Both cards already name Juan Tamayo.

The length line ("After round 2 the eight run 336 to 338 words, about 2:04, so none claims an exception.") matches score.py.

**Verdict.** Blocking 0. Minor 1 (README 1). All three people pass. R2-AB1 holds on independent re-confirmation.

## Era 4 Who batch 11, round 3 review: PART B

**Scope.** `theodore-abu-qurrah`, `stephen-of-mar-saba`, `ishoyahb-iii`. I checked every round 2 change to their briefs, audio, cards and `batch11/records.json` entries (`git diff a9674142 HEAD`), plus the README lines changed for them in round 2: the length line l.11, the Stephen census bullet l.27 and the Stephen re-score correction l.60. I re-confirmed R2-BB1 and R2-BB2 independently. I checked R2-BM2 against all of cic/texts. I edited no repo file.

**Method.** I read CLAUDE.md, the Pattern and its checklist, lessons.md, R2_review Part B, R2_changes Part B and the worker's README log, the diff, and the README. I reopened each changed string's source in context with `sed -n`:
- AASS (acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt): l.665-669, l.1110-1120, l.2720-2760, l.9255-9262, l.9486-9496, l.50365-50392, l.50428-50492, l.50550-50560, l.50598-50625, l.53300-53345, l.53410-53484, l.224005-224022. I also grepped every Sabait/Sabae hit in the volume and checked the index entries at l.7626-7633 and l.8846-8853 for further placings. There are none.
- NIK1 l.23268-23322. GRAF l.638-650. TOM l.5684-5691, l.5748-5752. Papadopoulos-Kerameus t.4 l.12935-12965.
- For R2-BM2, I ran my own all-texts rg for "Stephen the Sabaite", Stephan… Sabait…, Stephanus Sabaita, Στεφάνου τοῦ Σαββαΐτου, "Stephani Sabaitae/Thaumaturgi", Stephen/Étienne the Wonderworker/Thaumaturge, and twenty/vingt/zwanzig monks or martyrs. Every hit is the AASS volume, a namesake (the Wonderworker: PG94 l.5332, l.35211; PG99 l.72016, l.72454; AB7 l.7994; AASS l.53095, l.169862, l.223683, l.224017), or unrelated (Augustine's Twenty Martyrs of Hippo, Curzon, Pascal).
- For Easter, I computed the Julian dates: 789 is 19 April, which matches note e and confirms the 789 reading of scan "189". 796 is 3 April and 797 is 23 April.

**Quotations.** No brief or card quotation changed in Part B. These are the records strings that were changed or added, verified whitespace- and hyphen-tolerantly inside their ranges:
- "Hoc (juxta ea qua ad. Theophanis | Chronologiam notavimus) annum. nobis pccxcvi signant" (AASS l.50454-50455): verified.
- "nam. Alecandrinz Fre annis octo ram communem subsequenti, adjiciendus est annus unus, Phocz, ob caussam ibi explicatam. detractus, itaque ad. Indictionem indicatam. pervenitur" (l.50455-50459): verified.
- "OBSERVATIONES PERQUAM UTILES AD 5. THEOPHANIS CHRONOGRAPHIAM" (l.667): verified.
- "Magni-agri in Sigriana Hegumeni Confessorisque" (l.1116-1118): verified.
- "vide xx Martii probatum in Martyribus Sabaitis" (l.2739): verified.
- "et annum unum ex more omisisset computare" (l.2741): verified.
- "cum quinta Indictio annum nostrum pccxcvir signet" (l.2749-2750): verified.
- "INDEX CHRONOLOGICUS TOMI III MARTII" (l.9259): verified.
- ". 797 Martyres xx mon: chi Laurg S. Sabze" (l.9493): verified.
- NIK1 "ΣΤΕΦΑΝΟΥ τοϋ Σαΰΰαίτου, τοΰ χαϊ 'Κταοχύιχου γενομέγον" (l.23273-23274), "ήκμαζεν έν ετει ψ/ (790)" (l.23278), "εΐσελθών δηλαδή εις τήν Λαύραν τοϋ μεγάλου πατρός Σάββα" (l.23278-23280) and "ήξιώθη καί τοϋ χαρίσματος της άρχιερωσύνης" (l.23290-23291): verified.

**Audio.** All three audio files equal their briefs, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. I checked this by script, and score.py's rebuild left `git status` clean. All cards and records.json parse and end with a newline.

**Scores.** (score.py)

| id | words | minutes | FK | Flesch |
|---|---|---|---|---|
| theodore-abu-qurrah | 338 | 2:04 | 8.2 | 61.7 |
| stephen-of-mar-saba | 337 | 2:04 | 6.2 | 75.5 |
| ishoyahb-iii | 338 | 2:04 | 7.2 | 65.5 |

All three are inside about 2:05, so no README reason is needed. README l.11, "336 to 338 words, about 2:04", holds for all eight.

**Round 2 findings.**
- R2-BB1 (Stephen's raid year): applied with change. It holds except for one added sentence, R3-BB1. These placings each hold, told with their owner:
  - The Acts give AM 6288, AD 788, fifth indiction, under Elias and Basil (l.50556-50557, l.50619-50623).
  - The essay gives 797 (l.2736-2750).
  - The index gives 797 (l.9493).
  - The margin gives Easter of 797 (l.50373-50387).
  - The commentary's scan figure is 796, with its own reasoning (l.50454-50460).
  - Christopher died in 789, seven years before (l.53478-53480).
  - Graf gives 796 or 797 (GRAF l.645-646).

  The card's "They say Stephen counted by the Alexandrian era, which runs eight years behind theirs, and left out one year" is the Bollandists' own: "octennio dempto" (l.2732), "annum unum ex more omisisset" (l.2741) and "annis octo … communem subsequenti" (l.50456). "That passage goes on to add the missing year, to reach the fifth indiction" follows the Latin's order and words, "adjiciendus est annus unus … itaque ad Indictionem indicatam pervenitur", and draws no year from them. One sentence does not hold. "The note names no year for the twenty, and seven years after 789 is 796" is the profile's own arithmetic, not the note's (R3-BB1).
- R2-BB2 (README Stephen lines): applied with change. It holds, with one small citation fix (R3-BM4).
- R2-BM1 (Theodore, "Graf gives Michael's account in German"): confirmed applied.
- R2-BM2 ("No source" in place of "used here"): applied with change, and confirmed.
  - "No source gives his birth or death", "No source gives his birthplace" and "No source makes the writer a relative of John of Damascus" are true of all of cic/texts, by my own search (Method). The only Mar Saba Stephens with a kinship or a death are the Wonderworker and Nikodemos's 28 October bishop, and no source makes either of them the writer. AASS l.224017 ("credimus Sabaitam esse S. Joannis Damasceni nepotem") concerns the Wonderworker.
  - "A Life of Stephen the Wonderworker that the Library does not hold" is true. The Life is only cited, at PG94 l.5332, AASS l.53095 and AB7 l.7994 ("tom. III Julii 581").
  - The fixer's "For the writer's own life" in place of "For his own life" is right.
  - The new "It ends with him singing hymns to the martyrs" misplaces the line (R3-BM1).
- R2-BM3 (Ishoyahb, "Parts of the history, Thomas says, came down by the monastery's tradition"): confirmed applied (TOM l.5687-5690, l.5750-5751). The compensating "Its 1903 editor, Ignazio Guidi," keeps its meaning and its referent.
- R2-BM4 (Nikodemos's 28 October Stephen): applied with change, and confirmed. Leaving out "wonderworker" is right. "Flourished in 790", "a monk of the laura" and "later became a bishop" (τότε … ἀρχιερωσύνης) hold at NIK1 l.23277-23291. One new pronoun is unclear (R3-BM2).

## theodore-abu-qurrah

**Verdict:** pass. The round 2 change is right ("der folgendes zu erzählen weiß" is Michael's; R2 cited GRAF l.906). There are no new findings.

## stephen-of-mar-saba

**Verdict:** one blocking, three minor. The standing rulings are kept:
- He is a Who under the recorders rule, with his thin life flagged in `uncertain` "His name".
- The card name is "Stephen of Mar Saba".
- "Mansur" appears nowhere on the card or in the brief.
- The Wonderworker is named apart, in brief para 3 and in "Which Stephen".
- "Stephen the Poet" is only an other form, as the Typikon's title.

**R3-BB1 (card `uncertain` "The year" and records `contested_claims` "The year of the raid", Bollandists' side: the profile's own arithmetic on the Christopher note).** Note e reads, at AASS l.53478-53480: "Adeo- que anno Christi 189, quando Pascha incidit in 19 Aprilis sep- tennio ante horum Patrum passionem." It gives Christopher's year and "seven years before these Fathers' passion", and nothing more. "Seven years after 789 is 796" is not in the source. It is the profile's own sum, and it does more than count. Round 2 removed "which also points to 796" from this same sentence, and the new wording puts that inference back. It sets the note up as a further witness for 796, inside the Bollandists' own side. Their essay, index and margin give 797, and "septennio ante" need not be exact or exclusive. The fixer's note says the card "draws no inference from it". But "and seven years after 789 is 796" exists only to make the listener draw one. This is something added that a source does not say.
- Card `uncertain` "The year": "seven years before the twenty. The note names no year for the twenty, and seven years after 789 is 796. Georg Graf, in his 1910" → "seven years before the twenty. Georg Graf, in his 1910". This keeps the note's own placing as held. Round 2's reviewer worded it the same way.
- Records `contested_claims` "The year of the raid", side 2: "seven years before, and names no year for the twenty; seven years after 789 is 796 (l.53478-53480)" → "seven years before the twenty's passion, and names no year for the twenty (l.53478-53480)".

**R3-BM1 (card `uncertain` "His name", new in round 2: "It ends with him singing hymns to the martyrs").** The hymns line is para 80: "Quin et indigni famuli vestri reminiscimini, despicabiles vobis sermonis sui primitias offerentis, atque accinentis hymnos" (AASS l.53325-53328). The account does not end there. Paras 81-83 turn to Saint Sabas ("Tu vero … beatissime Saba", l.53341-53344), name Christopher (l.53420) and close with a doxology, "Amen" (l.53464).
- Card: "It ends with him singing hymns to the martyrs." → "Near its end, he speaks of singing hymns to the martyrs."
- Brief and audio, last paragraph, untouched but with the same slip: "He ends by asking the martyrs to remember their unworthy servant" → "Near the end, he asks the martyrs to remember their unworthy servant". That is 338 words, still inside 2:05. The audio keeps "[warmly] " before "Near".
- Card `keyWorks[1]`: "at the end of his account" → "near the end of his account", so the card uses one term throughout.
- Records: the existing claim at l.53326-53328 covers it, so no change.

**R3-BM2 (card `uncertain` "Which Stephen", new in round 2: an unclear pronoun).** "Nikodemos the Hagiorite keeps a Stephen the Sabaite on 28 October, the day after the Poet's feast in the Typikon. He was a monk of the laura who flourished in 790 and later became a bishop." Read aloud, "He" can attach to "the Poet", which would make the writer the bishop. That is exactly the blur this item exists to prevent.
- Card: "He was a monk of the laura who flourished in 790" → "This Stephen was a monk of the laura who flourished in 790" (NIK1 l.23277-23291).
- Records: no change.

**R3-BM3 (records `contested_claims` "The year of the raid", Acts side, untouched: the range misses the year).** "AASS l.50556-50557, l.50600-50607" does not reach "septingentesimo octogesimo octavo, Indietione quinta", which is at l.50619-50620. Lines 50600-50607 hold only "a nato vero" and margin text. The matching `claims` entry already cites l.50600-50624.
- Records: "(AASS l.50556-50557, l.50600-50607; Greek l.229190-229198)" → "(AASS l.50556-50557, l.50600-50624; Greek l.229190-229198)".

Checked and sound:
- Brief para 4: "He gives the year as 788. The Bollandists, by their own count of the years, make it 797." Both sides are told, and the card carries the rest.
- Card `dates`.
- "the year the fifth indiction marks" (l.2749-2750).
- "Theophanes the Confessor" (l.1118).
- "Elias … Basil" (l.50621-50623).
- The new `sources.about` entry for NIK1, which records cite.
- The `absent_details` note.

## ishoyahb-iii

**Verdict:** pass. Both round 2 edits in para 2 and para 3 hold. There are no new findings.

## README

**R2-BB2 re-confirmed.** l.27 ("March 797" agrees with the Bollandists…) and l.60 (the re-score's "Bollandists reckon 796", Rescore l.160) match what I verified:
- the essay, l.2736-2750;
- the index, l.9259 and l.9493;
- the margin, l.50373-50387;
- the commentary's scan figure and its reasoning, l.50454-50460;
- Graf, l.645.

Neither line repeats the Christopher arithmetic. "The profile gives each placing" will hold once R3-BB1 is applied. It holds already as to held placings, since R3-BB1 removes an addition, not a placing.

**R3-BM4 (README l.27, Stephen census bullet, rewritten in round 2: the range misses the year).** "The Acts give AM 6288, 788 (l.50556-50557)": l.50556-50557 carry AM 6288, but 788 is at l.50619.
- README: "The Acts give AM 6288, 788 (l.50556-50557)" → "The Acts give AM 6288, 788 (l.50556-50557, l.50619)".

**Verdict.** Part B: 1 blocking (R3-BB1: Stephen, the profile's own "seven years after 789 is 796" arithmetic on the Christopher note, in the card and records) and 4 minor (R3-BM1: "It ends with" / "He ends by" misplaces the hymns line; R3-BM2: "He" after "the Poet's feast"; R3-BM3: records Acts-side range; R3-BM4: README Acts range). R2-BB1 holds apart from R3-BB1. R2-BB2 holds. R2-BM2's "No source" claims are true of all of cic/texts. Theodore and Ishoyahb pass. Stephen passes once R3-BB1 is applied.

## Era 4 Who batch 11, round 3 review: PART C

**Scope.** A targeted recheck of round 2's changes to `al-tabari` and `ibn-ishaq` (brief, card, `records.json` entry, audio), and of the README as changed in round 2: every item in the worker's README log at the end of R2_changes.md, and the restated word range. This includes an independent re-confirmation of the round 2 blocking fix R2-CB1 (Ibn Ishaq card `uncertain[6]`, the Negus's hidden paper, WEIL l.9573-9595). I did not re-review untouched text from scratch.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md with its checklist, lessons.md, R2_review.md Part C, and R2_changes.md Part C plus the README sections of Parts A and B and the worker's README log. I read `git diff a9674142 HEAD` for both people's briefs, cards, records entries and audio, and for the README. I reopened every changed string in context with sed: WEIL l.993-1001, 1066-1067, 1092-1093, 9560-9600; T4 l.1490-1496; T5 l.40-96 (title page, "RECENSUIT E. PRYM", 1893); EVETTS l.15210-15215; QUATREMERE l.14044-14054; ELIAS l.124-129; MOBERG l.2628-2640, 2688-2712; HITTI l.734-742. I grepped cic/texts for other placings of al-Maqrizi's death (only EVETTS l.15213 gives one). For the README log I reopened ALV l.31683-31716, both Alvarus cards, AASS (martii-tomus-3) l.2736-2750, 9257-9260, 9491-9494, 50373-50388, 50448-50461, 50555-50640, and GRAF l.644-647. I walked census.json (release 44) `movements[53]` for `sources`, `relationsSummary`, `voices` and `documentedStories[1]/sources`. A script counted sentence lengths in every changed card field. I ran score.py and quotes.py, and compared the audio files with the briefs before score.py rebuilt them. The rebuild left git status clean.

**Quotations.**
- Ibn Ishaq records, revolt claim (claims[21]): "ich bekenne, dass es keinen Gott gibt ausser Gott, dass Mohammed sein Diener ist und sein Gesandter, dass Jesus sein Diener ist und sein Gesandter und sein Geist und sein Wort" (WEIL l.9574-9576), "die rechte Seite seines Oberkleids" (l.9577-9578), "Du hast unsern Glauben verlassen und Jesus einen Diener genannt" (scan "onsem", marked; l.9588-9589), "Wir sagen, er ist Gottes Sohn" (l.9590-9591), "seine Hand auf die Brust" (l.9591), "ich bekenne, dass Isa, der Sohn Mariams nichts Anderes als diess war, er meinte damit, als in der Schrift, auf welche er seine Hand gelegt, ausgesprochen war" (l.9592-9594), "Die Abissynier gaben sich aber zufrieden, und giengen auseinander" (l.9594-9595). All verified. One inline range starts a line late (Ibn Ishaq R3-CM2).
- Ibn Ishaq records, Moberg claim: the new "(l.2708-2710)" holds ("One single point suggests the narrative of the Book of the Himyarites, viz. the death of the Jewish King in the sea", MOBERG l.2708-2710). Verified.
- Ibn Ishaq records, new claim: "The year 279/892 saw his death" (HITTI l.742; l.736 names Ahmad ibn-Yahya ibn-Jabir al-Baladhuri as the subject). Verified.
- Ibn Ishaq records, Faymiyun claim (range changed only): "ein frommer, eifriger Christ" (l.996), "ein Zimmermann und Maurer" (l.999-1001), "in Nadjran verkauft" (l.1067) are inside the new ranges. "Diess ist die Tradition des Wahb Ibn Munabbah, nach dem Berichte der Bewohner von Nadjran" (l.1092-1093): the scan reads "Wahb Ihn Munabbah" and the claim does not mark it (Ibn Ishaq R3-CM3).
- Ibn Ishaq brief para 5: "anything that suggests an independent Muhammadan tradition of historical value." (MOBERG l.2694-2695). Unchanged, verified.
- al-Tabari records, Quatremère claim (claims[24]): the added "AL-MAKRIZi (died A. H. 845 = A. D. 1441)" (EVETTS l.15213, scan "AL-MAKRIZi" marked). Verified.
- al-Tabari brief and card: no new quotation marks in round 2. quotes.py: bad 2, the two known hits named in the worker's log (the Evetts quote with a folio mark, and a regex artifact on the Ishoyahb card).

**Audio.** Both audio files equaled their briefs before the rebuild, with "[calmly] " at the start and "[warmly] " at the start of the last paragraph. score.py rebuilt them with no change in git. Both cards and records.json parse and end in a newline.

**Scores.** (words; minutes at 162.5 wpm; FK; Flesch)
- al-tabari: 336; 2:04; 6.7; 68.4
- ibn-ishaq: 338; 2:04; 6.8; 68.8
- eulogius-of-cordoba: 336; 2:04; 6.9; 69.5
- ishoyahb-iii: 338; 2:04; 7.2; 65.5
- paulus-alvarus: 336; 2:04; 7.9; 63.3
- stepanos-of-taron: 336; 2:04; 6.7; 69.1
- stephen-of-mar-saba: 337; 2:04; 6.2; 75.5
- theodore-abu-qurrah: 338; 2:04; 8.2; 61.7

All pass FK ≤ 10 and Flesch ≥ 60. None is past about 338 words, so none needs a README length reason. The README's restated range, "336 to 338 words, about 2:04", matches.

**Round 2 findings.**
- R2-CB1 (Negus's answer to the revolt): applied with change. **The fix holds.** I re-confirmed it independently against WEIL l.9565-9597. The new text keeps the concealed paper, the Abyssinians' charge as theirs ("saying he had left their faith"), their creed, the double-edged oath and how the revolt ended. Each of the fixer's five departures from the reviewer's wording is correct. (1) "his spirit and his word" is l.9576. (2) The charge and creed are l.9588-9591, and without them "this" in the oath has nothing to play against. (3) "The report explains" is right: the gloss "er meinte damit ..." sits inside Djafar's report after his father (l.9567), so its voice cannot be pinned on Ibn Ishaq. (4) "The Negus hid it" keeps the pronoun off Jesus. (5) "dispersed" is "giengen auseinander" (l.9595). "Hid" for "steckte ... in die rechte Seite seines Oberkleids" is a fair reading: the paper goes inside his robe and the oath turns on it being unseen. All sentences are 6 to 20 words, and every pronoun resolves aloud. One paraphrase word shifts the oath (Ibn Ishaq R3-CM1), and one inline range is a line short (R3-CM2). Neither is blocking.
- R2-CM1 (al-Tabari, "the killing"): applied. "and killed many" holds ("واكثروا القاتل", scan, T4 l.1494), and "the killing" now has its antecedent. Confirmed.
- R2-CM2 (al-Tabari `traces[2]`): applied. EVETTS l.15213 and QUATREMERE l.14048-14051 ("l'histoire de Tabary ... cette chronique") verified. Records claim and witness updated. No other placing of al-Maqrizi's death is in cic/texts. Confirmed, with one wording point (al-Tabari R3-CM1).
- R2-CM3 (al-Tabari, Prym twice): applied. The T5 title page (l.88-95, "RECENSUIT / E. PRYM", "1893") and the conspectus (l.47) verified. "Prym" in `uncertain[4]` and "He" after it resolve. Confirmed.
- R2-CM4 (al-Tabari `traces[0]`): applied. The sentences are 15 and 13 words. ELIAS l.128 "arabici Annales Al Tabari". Confirmed.
- R2-CM1 (Ibn Ishaq, Moberg's scope): applied, word-neutral. MOBERG l.2637-2638 and l.2692-2710 support "the Arabic stories of the persecution" and "older Christian accounts" (the Acta, and the Book of the Himyarites for the sea death). Records updated. Confirmed.
- R2-CM2 (Ibn Ishaq, Faymiyun ranges): applied. l.993-1001, 1066-1067, 1092-1093 verified. Confirmed. I tripped over an unmarked scan form in the same claim (R3-CM3).
- R2-CM3 (Ibn Ishaq, al-Baladhuri's death year): applied. HITTI l.742 verified, tag Documented. Confirmed.
- R2-CM4 (Ibn Ishaq `knownFor`): applied with change. "The book" for "It" is right, since "It" would land on "reworking". The colon introduces a list. The second sentence is 26 words, a list of three named parties. That is within "about 25" and is not a finding. Confirmed.
- R2-CM-R1 (README, Ibn Ishaq census sentence): applied as worded. It is true for `relationsSummary` and `voices`, which cite nothing. It leaves out the story's fourth source (README R3-CM-R1).
- R2-CM-R2 (README, "used here" on the Stephen card): applied by Part B. A grep of every batch 11 JSON file finds no "used here". Confirmed.

## al-tabari

**Verdict:** pass (0 blocking, 1 minor).

**R3-CM1 (card `legacy.traces[2]`: "(died 1441, by Evetts)" reads as if Evetts were the agent).** Source: "AL-MAKRIZi (died A. H. 845 = A. D. 1441)" (EVETTS l.15213). The fact and the attribution are right, but "died 1441, by Evetts" can be misread. Fix, `traces[2]`: "The historian al-Maqrizi (died 1441, by Evetts) is quoted in Étienne Quatremère's French of 1811 on the caliph Aziz's library." → "The historian al-Maqrizi died in 1441, Evetts says. Étienne Quatremère's French of 1811 quotes al-Maqrizi on the caliph Aziz's library." (Sentences of 8 and 14 words. Evetts is introduced in `traces[1]`. The next sentence, "Aziz had more than twenty copies of al-Tabari's history ...", is unchanged.) Records: none, because claims[24] already carries EVETTS l.15213.

Checked and sound in the round 2 text: brief para 3, read in full for flow, with the Hira sentence at 17 words and "the killing" resolved; `traces[0]`; `uncertain[3]` and `[4]`, where Prym is introduced once with role and date and "this volume of the Annals" has its referent. There is no "X, not Y", colon reveal, tail or unintroduced name in the changed text.

## ibn-ishaq

**Verdict:** pass (0 blocking, 3 minor). R2-CB1 holds.

**R3-CM1 (card `uncertain[6]`: "nothing more than this" narrows the oath).** Source: "ich bekenne, dass Isa, der Sohn Mariams nichts Anderes als diess war" (WEIL l.9592-9593), which reads "nothing other than this". The oath works because "this" can point both to the Abyssinians' "God's son" and to the paper. "Nothing more than" tilts it toward a lowering of Jesus that the Abyssinians would not have accepted. Fix: "the Negus said that Jesus, son of Mary, was nothing more than this." → "the Negus said that Jesus, son of Mary, was nothing other than this." (Word-neutral, 19 words.) Records: none, because the claim quotes the German.

**R3-CM2 (records, revolt claim (claims[21]): the inline range for the Abyssinians' words starts a line late).** "Du hast" begins at l.9588 ("antworteten : „so gut als möglich.“ — „Was wollt ihr denn?“ „Du"), and l.9589 has "hast onsem Glauben verlassen ...". Fix: "\"Wir sagen, er ist Gottes Sohn\" (l.9589-9591)" → "\"Wir sagen, er ist Gottes Sohn\" (l.9588-9591)". The witness, l.9565-9597, already covers the line. Card: none.

**R3-CM3 (records, Faymiyun claim (claims[10]): an unmarked scan form inside a quotation).** Source: "Diess ist die Tradition des Wahb Ihn / Munabbah, nach dem Berichte der Bewohner von Nadjran." (WEIL l.1092-1093). The claim quotes "Wahb Ibn Munabbah" with no scan mark, although the entry marks other scan forms. Fix, claim: "\"Diess ist die Tradition des Wahb Ibn Munabbah, nach dem Berichte der Bewohner von Nadjran\"" → "\"Diess ist die Tradition des Wahb Ibn Munabbah, nach dem Berichte der Bewohner von Nadjran\" (scan \"Ihn\")". Card: none.

Checked and sound in the round 2 text: brief para 5, read in full for flow. The Moberg sentence is 23 words, and "In those stories" resolves to "the Arabic stories of the persecution". `knownFor`, with "The book" resolving to "life of Muhammad". `uncertain[6]`, read in full: the charge is the Abyssinians' own, "The report explains" owns the gloss, "They" lands on the Abyssinians, and each "he" lands on the Negus. There is no "X, not Y", colon reveal, tail, aphorism or unintroduced name. Records claims[14], [21] and [22] support the card text. Tags are right: what the text reports is Documented, and Moberg's judgment is Dominant Modern Reconstruction.

## README

Each item in the worker's README log was checked against README.md as it now stands:
- Length line: applied as logged, and true (all eight briefs 336 to 338 words, 2:04, by score.py).
- R2-AM-R1, three lines: applied as Part A worded them. True. ALV l.31683-31708 has Antonio's charge that Tamayo "hunc nostrum confundere non dubitavit cum Alvaro, Eulogii fratre", Tamayo's "non carnis nexu, sed contubernii vinculo", and Antonio's "fratrem vere germanum Eulogii alterum Alvarum". Both batch 11 cards (eulogius-of-cordoba and paulus-alvarus) give Tamayo's view and Antonio's, as the "Other profiles" line says.
- R2-BB2, Stephen, two lines: applied as Part B worded them. True on the 797 placings: the essay at l.2736-2750 ("Indictione v: cum quinta Indictio annum nostrum DCCXCVII signet", scan), the index at l.9259 (heading) and l.9493 ("797 Martyres xx"), the margin at l.50373-50387 ("post Pascha anni 797"), the commentary's scan "pccxcvi" and its "adjiciendus est annus unus ... ad Indictionem indicatam pervenitur" at l.50454-50458, and GRAF l.645-646 ("im März 796 oder 797"). One range in the Live census line is short (README R3-CM-R2).
- R2-CM-R1: applied as worded. See README R3-CM-R1.
- R1-CM8: true. No "used here" is in any batch 11 card or records entry.
- quotes.py: true, bad 2, the two known hits.

**R3-CM-R1 (Live census mentions, Ibn Ishaq: the story's source list leaves one out, and "The story's" has a distant referent).** Census `movements[53]/documentedStories[1]/sources` holds four works: Simeon of Beth Arsham (primary), the Book of the Himyarites (primary), Procopius, Wars I.20 (primary), and "Glen Bowersock, The Throne of Adulis (Oxford, 2013)" (reference). "The story's sources are Simeon, the Book of the Himyarites and Procopius" reads as the full list. "The story" also sits three sentences after "Kaleb Crosses the Sea" is named. Fix: "The story's sources are Simeon, the Book of the Himyarites and Procopius, not him; `relationsSummary` and `voices` cite none." → "\"Kaleb Crosses the Sea\" cites Simeon, the Book of the Himyarites and Procopius as primary sources and Bowersock as reference, and none of them is him; `relationsSummary` and `voices` cite none."

**R3-CM-R2 (Live census mentions, Stephen, a line Part B owns: the Acts' 788 is outside its range).** "The Acts give AM 6288, 788 (l.50556-50557)". l.50556-50557 carries only the AM year ("sexies millesimo ducente- / simo octogesimo octavo"). The Acts' Incarnation year is at l.50619 ("tro Christo Jesu, septingentesimo octogesimo octavo,"), after the margin notes that interrupt the column. The R2 rewrite carried this range over from round 1. Fix: "The Acts give AM 6288, 788 (l.50556-50557)" → "The Acts give AM 6288, 788 (l.50556-50557, l.50619)". This is for Part B or the coordinator to apply. If the Stephen card or records cite l.50556-50557 for the 788, they need the same fix.

**Verdict.** al-tabari passes after one minor fix. ibn-ishaq passes after minor fixes, and the round 2 blocking fix R2-CB1 holds on independent re-confirmation. The README passes after minor fixes, and its restated word range matches the briefs. Blocking: 0. Minor: 6 (al-tabari 1, ibn-ishaq 3, README 2).

