# R4 cap check: era 7 batch 1, Chanforan and Worms fix strings

- Ordered by: Mark's cap ruling, 2026-11-15, answer "A". One targeted check of the strings changed by the fixes for C3-B1, C3-M1, C3-M2 (Part C) and A3-M1, A3-M2 (Part A) of `R3_recheck.md`. Unchanged text not reviewed.
- Scope: `git diff de2cd251b 34e53ac17 -- Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/`
  - `synod-of-chanforan-1532.brief.txt`
  - `audio/synod-of-chanforan-1532.audio.txt`
  - `synod-of-chanforan-1532.entry.json` (`uncertain[12]`)
  - `records.json` (Worms `claims[60]` witness, `contested_claims[2]` sides, `absent_details[3]` note; Chanforan contested claim "That the Waldensians joined the Reformation in 1532, and what the meeting changed")
- Brief figures (`working/grade.py`): 400 words, 2.50 min, FK 6.99, Flesch 66.50, longest sentence 25 words.
- Reviewer: Opus, fresh, full effort. No paid calls, no network.

Abbreviations: LEG = `cic/texts/leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt`; GIL81 = `cic/texts/gilles_histoire-ecclesiastique-eglises-vaudoises-v1-fra_1881.txt`; PALL1 = `cic/texts/pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt`; WAT = `cic/texts/council-of-trent_canons-and-decrees_waterworth1848.txt`; THEI = `cic/texts/theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt`; ZKG14 = `cic/texts/jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt`. OCR quoted with long s normalised.

## Verdict: CLEAR

C3-B1, C3-M1, C3-M2, A3-M1 closed. A3-M2 closed, with one new Minor in its added wording (A4-M1). It is in a records note and does not touch the brief or the entry.

## Checks

### 1. The brief's Léger sentence (C3-B1)

Brief p.8, s.1: "Léger wrote in 1669 that the valleys changed nothing at the Reformation, but later went beyond self-defense." (17 words.)

- LEG l.23072-23076: "Bien qu'au tems de la Reformation, les Vaudois ou habitans des Vallées, eussent envoyé des Députés pour conférer avec Bucer, Melanchton, Oecolampade, Zwingle, Luther, Calvin, & autres, touchant les points de Doctrine, & de Discipline. Je ne trouve point qu'ils y ayent changé la moindre chose, si ce n'est qu'ils étoient presque Anabatistes en ce qui regarde le maniement des armes seulement".
- LEG l.23078-23082: "il n'appartenoit qu'aus Magistrats de manier l'épée ... ou, en toute extrémité, d'être seulement sur la defensive, sans seulement faire un pas pour poursuivre leurs ennemis quand ils prenoient la fuite. Ils en étoient même encore là logés l'an 1560 [OCR "l ait 1 fSo. 8c <f I ."] pendant la cruelle guerre que leur fit Emanuel Philibert".
- LEG l.23085-23086: "comme le remarque Pierre Gilles ... bien qu'enfin à l'exemple des anciens Machabées, ils en ayent uzé autrement du depuis."
- GIL81 l.8775-8789: the ministers refused the pursuit, "car ils avoyent conclu dès le commencement de la guerre au mois d'octobre précédent, et puis confirmé au commencement de février dernier, que si l'extrême nécessité les contraignait de se défendre par armes ... on se contiendroit en la seule défense". GIL81 l.8275-8278: "grande quantité d'armes de toutes sortes, harquebuses, morions, tambours, picques, halebardes, espées".

Findings on the sentence:
- Nothing reversed. The old rule allowed defense in extremity and held through 1560-61 (LEG l.23081-23082; GIL81 l.8776-8789). "Later went beyond self-defense" places the change after that war, which is Léger's "du depuis". It no longer says the valleys first took up arms later.
- Nothing added. "Went beyond self-defense" is the only reading "en ayent uzé autrement" allows here. What they "acted otherwise" against is the rule just stated, and in 1560 they already bore arms in defense. So the change can only be going past defense. "Self-defense" renders "seulement sur la defensive". "Later" renders "du depuis".
- Witness. The sentence opens "Léger wrote in 1669", so both clauses sit with him. The next sentence names Montet, so Montet's view stays separate.
- "At the Reformation." The time phrase is faithful to "au tems de la Reformation". The sentence leaves out Léger's scope, "touchant les points de Doctrine, & de Discipline". Nothing it says goes against that scope, and "pas la moindre chose" is his own sweeping claim. The narrower scope is carried in the entry and records (check 3). Not a finding.

C3-B1: CLOSED.

### 2. "the historians Alexis Muston and Édouard Montet" (C3-M2)

Brief p.2, s.1: "That manuscript reaches us only in quotations by the historians Alexis Muston and Édouard Montet."
- Entry `sources`: "Alexis Muston, The Israel of the Alps (1850; English 1866)" and "Édouard Montet, Histoire littéraire des Vaudois du Piémont (1885)". Both are histories. The entry's manuscript source note says "It is not held; we have only their quotations." The entry `datesNote` already calls them "the modern historians Muston, Montet and Zezschwitz". The kind is right, and it matches the README's "a manuscript quoted by two historians".
- The word count is back at 400, the cap (grade.py output above).

C3-M2: CLOSED.

### 3. Entry `uncertain[12]` and the records contested claim (C3-M1)

- Entry: "Léger says nothing changed in doctrine or discipline through their talks with the reformers."
- Records, Léger's side: "Nothing changed in doctrine or discipline through their talks with the reformers; their near-Anabaptist view that only magistrates bear the sword held until at least 1560 ... and only later, after the Maccabees' example, did they act otherwise: Léger (... l.23072-23086)."
- Against LEG l.23072-23076: "y" points back to the deputies' talks "touchant les points de Doctrine, & de Discipline". "In doctrine or discipline through their talks" matches that. The relationship reading that C3-M1 flagged is gone. "Says" for "Je ne trouve point" is fair, since the sentence names him as the one judging.
- Fit with the brief. The brief has the broader time phrase and the entry and records have the exact scope. They do not conflict. Both put the arms change after 1560.
- The applied entry wording differs from R3's proposal ("Léger finds they changed nothing ..."). It is equally faithful.

C3-M1: CLOSED.

### 4. Worms records strings (A3-M1, A3-M2)

- `claims[60]` witness `PALL1 l.10137-10178`: l.10137 "La mattina proſſima Ceſare fè chiamar gli Elettori,"; l.10178 "coRui come notorio eretico^". The range now carries "come notorio eretico".
- `contested_claims[2]` Waterworth `l.1720-1729`: l.1720 "On alighting at Worms,"; l.1726 "on the sixteenth of April"; l.1728 "on the follow"; l.1729 "ing clay, the seventeenth of April, 1521". The range now carries both dates.
- A3-M1: CLOSED.
- `absent_details[3]`, first added item: THEI l.48761 "Hieronymum Aleandrum tit. Sancti Grisogni presbiterum Cardinalem, Sanctitatis Vestrae Legatum". The year is in the running head at l.48715, "PAULI PP. III. ANNO IV. CHRISTI 1538", and in the letter's own date at l.48768-48769, "Datis in oppido nostro Thorda vigesima nona Octobris Anno Domini mdxxxviii" (John, King of Hungary, l.48773). The line, the year and "legate" are all right.
- Second added item: ZKG14 l.24355-24362. It describes Capasso's work on "die für dieses Konzil bestellten päpstlichen Legaten (I legati al concilio di Vicenza del 1538 ...)", then "Beigegeben sind sechs Briefe in der Mehrzahl von Aleander". The line, the year, "six letters, mostly his" and "printed by Capasso" are right. But the notice never calls Aleander a legate. It names him only as the writer of most of the letters. "Two 1538 items name him as legate" therefore says more than this line does (A4-M1).
- Neither item comes from Worms, so the absence still stands.
- A3-M2: CLOSED, with A4-M1.

### 5. Limits, audio, JSON, tells

- Brief: 400 words (cap 400). Longest sentence 25 words (cap 25). FK 6.99, Flesch 66.50.
- Audio: I rebuilt it from the brief, with "[calmly] " at the start and "[warmly] " before the 9th and last paragraph. It is identical to `audio/synod-of-chanforan-1532.audio.txt`.
- JSON: `records.json` and `synod-of-chanforan-1532.entry.json` both parse.
- AI tells: none in the changed strings. No filler, no hedging and no assistant cadence.

## Findings

### Blocking
None.

### Minor

**A4-M1. Minor (the added ZKG 14 item is said to name Aleander as legate; the line names him only as a letter writer).** Records `absent_details[3]` note: "Two 1538 items name him as legate: a letter in Theiner (... l.48761), and ZKG 14's notice of six letters, mostly his, printed by Capasso (... l.24362)." THEI l.48761 does call him "Legatum". ZKG14 l.24355-24362 names the Vicenza legates as Capasso's subject but names Aleander only as the author of most of the six letters. This is not reader-facing and does not change the absence.

Fix, replace that sentence with: "Two 1538 items name him: a letter in Theiner that calls him legate (theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt l.48761), and ZKG 14's notice of Capasso's work on the legates to Vicenza, with six letters, mostly his, printed by Capasso (jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt l.24355-24362)."

## Counts

Fixes checked: 5. Closed: 5 (C3-B1, C3-M1, C3-M2, A3-M1, A3-M2).
New: Blocking 0. Substantial 0. Minor 1 (A4-M1). Total 1.
