# Round 3 recheck: era 7 council profiles, batch 2 (2026-11-15)

The last round. Four fresh Opus reviewers, one per council, none of whom had seen the drafting or any fixing: a targeted recheck of the round 2 changes only, at full effort. Part A Regensburg (0 blocking, 1 substantial, 0 minor; A3-S1, an entry string, applied as worded), Part B Trent (1 blocking: B3-B1, a round 2 length cut that moves Sarpi's "first"), Part C Augsburg 1555 (0, 0, 0; pass), Part D Poissy (1 blocking: D3-B1, Sarpi still counted on the Catholic side). Both blocking points come from round 2 fix wording and go to Mark for a cap ruling; neither is applied.

---

## Council profiles, era 7 batch 2, round 3: Part A (Colloquy of Regensburg 1541)

**Council.** `colloquy-of-regensburg-1541`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/colloquy-of-regensburg-1541.brief.txt`, `audio/colloquy-of-regensburg-1541.audio.txt`, `colloquy-of-regensburg-1541.entry.json`, `records.json` key `colloquy-of-regensburg-1541`, and the README line "Colloquy of Regensburg (about 2:30)" under "Batch 2". Scope: `git diff 7ad6d2a2 HEAD` on these files (branch `claude/cft-councils-era7-batch2`), against `R2_recheck.md` Part A and `R2_changes.md` Part A.
**Brief.** 396 words by `wc -w` (2.48 min, 2:29 at 160 wpm). `grade_text`: FK 8.00, Flesch 60.19. Longest sentence 25 words (the unchanged close, "In his bull he recalled proposing a council ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag (`diff` after stripping the two tags: identical).
**Records.** No change to the Regensburg key in this round (the `records.json` diff touches only Trent, Augsburg 1555 and Poissy). `working/records_colloquy-of-regensburg-1541.json` equals the key (python compare). Both JSON files and the entry parse.
**Entry.** One string changed: `uncertain[7]`, last sentence.
**README.** The Regensburg line is unchanged and still true (2:29 is "about 2:30"; every stage it names keeps its witness).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or any fixing. Read and grep only; no repo file edited; no model, network or paid calls.

Abbreviations: CLET1 = `calvin_letters-vol1_bonnet1858.txt`; PALL = `pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt`; FAB = `faber_memoriale-lat_1873.txt`.

## Verdict: REVISE (0 blocking, 1 substantial, 0 minor)

The two brief changes are right. The cut leaves "wanted peace" with Calvin's tag, and the Turks and France stay in the entry. "Not clear" renders "dubbietà" as faithfully as "unclear" did. "Without naming the talks" is a true absence, and it stops Faber's sentence being heard as a verdict on the formula.

The one point is the round 2 fix to the entry (A2-M2). It turned Faber's "we" into "he and his readers". The letter does not support that. Throughout it, Faber's "nos" is himself and those like him, set against "vos", the Paris scholastics. He says so in so many words: "longe nobis antecellitis, mihi, inquam, et similibus mei" (FAB l.13376-13378). "The means we use" (l.13477-13481) are the means used at Regensburg, not by students in Paris. So the fix names a subject its witness does not name. This is the batch 1 pattern: a round 2 fix that overstates its witness. Because it is wrong in the entry, it is Substantial (A3-S1).

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| A2-S1 | CLOSED, fix right | Brief l.3 now "The emperor Charles V, Calvin thought, wanted peace." Calvin's tag kept; CLET1 l.11030-11032 ("The Emperor ... is not at all inclined to heap up new troubles for himself"). Turks and France kept in entry `issue[1]` ("He feared the Turk, and an uncertain peace or open war with the king of France"; CLET1 l.11032-11034, "he fears an attack on the side of Turkey ; on the part of the King of France"). Brief l.11 "because their meaning was not clear": PALL l.27652-27653 ("le concordate parole nell'articolo della Giustificazione per la dubbietà loro non contentarono", OCR "Me concordate parole nell' articolo del* UGiidlificazione perla dubbietàloro"). The tag "Pallavicino says" still governs the sentence. No witness tag orphaned. Brief 396 words, Flesch 60.19, as R2_changes reports. |
| A2-M1 | CLOSED, fix right | Brief l.11 "On 12 May, without naming the talks, he wrote that the faith's business went on in great doubt." (18 words.) The date: FAB l.13514 ("Ratisbonæ, 12 Maii t541"). The words: FAB l.13476 ("Negotium fidei valde ambigue procedit"). The absence holds (searches below). "Went on" for the present "procedit" in reported speech is fair. Placed between Calvin's joy and Rome's doubt, the sentence now says plainly that Faber names neither. |
| A2-M2 | CLOSED as worded, but the fix is wrong (A3-S1) | Entry `uncertain[7]` "so that he and his readers trust in God alone." "Leaving them" is gone, but the new subject is not Faber's. See A3-S1. |

## New findings

### Blocking

None.

### Substantial

**A3-S1. Substantial (a translation that names a subject its witness does not name; a round 2 fix overstating its witness).**

- Entry `uncertain[7]`, last sentence: "He says the business of the faith went forward 'valde ambigue', very doubtfully, so that he and his readers trust in God alone."
- Faber: "Negotium fidei valde ambigue procedit, et eo modo ut in Deo solum immediate confidamus, cum media quibus utimur nihil sint in homi- / -num judicio" (FAB l.13476-13481). "Confidamus" is first person plural; the Latin does not say who "we" are.
- The letter keeps its "nos" apart from its "vos" (the scholastics at Paris, l.13292-13293). "Sane vobis in Domino gratulor, quod hac in re longe nobis antecellitis, mihi, inquam, et similibus mei" (l.13376-13378): "us" is "me, I say, and those like me". Also "nec minores debentur a nobis ... defuit nobis talis ac tanta componendi ordinandique studii nostri facultas" (l.13417-13420), and "quem prædicamus, quemque vobis proponimus" (l.13454-13455). And "media quibus utimur", "the means we use", are the means of the faith's business at Regensburg, which his Paris readers did not use.
- Round 2's support for "his readers" was "omnes fratres nostri" (l.13307). That phrase calls the Paris brothers "ours"; it does not put them inside the "we" who trust. So "he and his readers" is unsupported.
- "So that" also reads as purpose; "eo modo ut" is "in such a way that".
- Fix, entry `uncertain[7]` last sentence (24 words): `He says the business of the faith went forward 'valde ambigue', very doubtfully, so that he and his readers trust in God alone.` → `He says the business of the faith went forward 'valde ambigue', very doubtfully, in such a way that trust rests directly on God alone.`
- This keeps "immediate" ("directly"), which records claim 88's translation also keeps, and gives "we" no subject the Latin does not give. Records claim 88 ("in such a way that we trust directly in God alone") is right as it stands, quoting Faber's own person; no records change. The brief does not carry this clause; no brief or audio change.

### Minor

None.

## Verified

- **Changed brief strings, against source in context.** "wanted peace" (Calvin, CLET1 l.11030-11032, the emperor's own inclination, 1541). "On 12 May ... went on in great doubt" (Faber, a Jesuit at Ratisbon, Catholic side, 12 May 1541; FAB l.13476, l.13514). "Their meaning was not clear" (Pallavicino, of Rome's reaction; PALL l.27652-27653). Each sits with its own witness; no tag orphaned by the cut.
- **Changed and added quotes.** No new quoted words in the brief. Entry `uncertain[7]` quotes "valde ambigue": verbatim, FAB l.13476. The rest of `uncertain[7]` is unchanged.
- **Translations.** "In great doubt" and "very doubtfully" for "valde ambigue": faithful. "Not clear" for "dubbietà": faithful. "He and his readers" for the subject of "confidamus": not faithful (A3-S1).
- **Brief figures.** 396 words, FK 8.00, Flesch 60.19, longest 25. The A3-S1 fix is entry-only and does not move them.
- **Audio** equals the brief bar the two tags. **Records** key equals the working file; unchanged this round. **README** line unchanged and true.
- **Unchanged text.** Not re-reviewed. Nothing blocking seen in passing.

## Searches run

- **"Without naming the talks" (brief) and "does not name the talks" (entry).** Faber's letter, FAB l.13290-13520, case-insensitive: `collo|di(æ|ae)?et|conven|imperat|ca?(e|æ)sar|legat|contar|granv|protest|luther|h(æ|ae)retic|[ji]ustif|concord|ratisb` gave only "contra hæreticos" (l.13495, on letters' weakness against heretics) and the date line "Ratisbonæ" (l.13514). A second pass, `confer|disput|negot|tract|articul|libr|concil|pontif|papa|princip`, gave "Negotium fidei" (l.13476) and two uses of "principium" (l.13381, l.13422) on the order of study. No name of the colloquy, the Diet's talks, the Book, the formula or justification. The absence holds.
- **Who "we" are in the letter.** `\b(nos|nobis|nostr|vos|vobis|vestr)` over FAB l.13300-13512: "nos/nobis" is Faber and those like him, set against "vos/vobis" the Paris scholastics (l.13376-13378, l.13417-13420, l.13454-13455). No line puts the readers inside "we".

## Counts

Blocking 0, Substantial 1, Minor 0.

---

## Council profiles, era 7 batch 2, round 3: Part B (Council of Trent 1545-1563)

**Council.** `council-of-trent`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/council-of-trent.brief.txt`, `audio/council-of-trent.audio.txt`, `council-of-trent.entry.json`, `records.json` key `council-of-trent` (equal to `working/records_council-of-trent.json`, checked by script), and the README line "Council of Trent (about 2:30)" (l.22). Scope: `git diff 7ad6d2a2 HEAD` for these files, against `R2_recheck.md` Part B (l.131-277) and `R2_changes.md` Part B (l.54-106).
**Brief.** 398 words by `wc -w` (2:29 at 160 wpm). `grade_text`: FK 7.74, Flesch 61.63. Longest sentence 22 words. No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` and `[warmly] ` only (checked by `diff` after stripping the two tags).
**Entry.** Parses (`python3 -m json.tool`). Every changed entry sentence is 25 words or fewer.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or fixing. No repo file edited; no model, network or paid calls.

Abbreviations as in round 2: W (Waterworth), S (Sarpi, Brent 1676), P2 (Pallavicino parte 2, 1664), P3 (Pallavicino tomo 3, 1846), BOC (Jacobs's Book of Concord), BENSOW.

## Verdict: REVISE (1 blocking, 0 substantial, 0 minor)

The Formula of Concord sentence (B2-S1) is now right. It quotes the Formula verbatim, names no decree the acts lack, and "the decree" reads back to the condemnation of faith alone, which sits in the same Decree on Justification as canon XXIV, the Formula's target. The four other changed entry and records strings are faithful.

The one blocking point is a round 2 length cut (B2-M5). It moved Sarpi's word "first" from the council's act to the envoys' asking. In Sarpi the Saxons' first requests were a safe-conduct and delay; the supremacy request comes late in the speech, asking the council to act on it first. One word moves back; the count is unchanged.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| B2-S1 | CLOSED, fix right | Brief: `In 1577 the Lutheran Formula of Concord rejected the decree "that our good works support salvation."` BOC l.30993-30999: "the de- cree of the Council of Trent, and whatever elsewhere is set forth in the same sense, should by right be rejected, viz. that our good works support salvation". The Formula names Trent in its own text; Jacobs's footnote gives "Sess. vi., Can. xxiv." (BOC l.31038). Canon XXIV is in the Decree on Justification (W l.12960, 13781-13785), the same decree as canon IX on faith alone, so "the decree" after "It condemned the teaching that faith alone justifies" points to the right decree. Swedish text independently: "förkasta Tridentinska mötets beslut ... nämligen att våra goda gärningar bevara saligheten" (BENSOW l.26803-26806). The passage is in the Solid Declaration (BOC p.588); BENSOW l.31612-31617 has the epitome and solida declaratio finished together as the Bergen book and signed, and BOC l.27925 dates the Epitome "Bergen May 29th, 1577", so "In 1577" holds. Entry `traditions` Lutheran note now quotes the same clause verbatim. |
| B2-M1 | CLOSED, fix right | `uncertain[7]`: "argued against confirming outright" matches P3 l.57848-57850 ("disconsigliarono il papa dell'assoluta confermazione") and S l.70324-70326 (eight cardinals "almost all of opinions that it was fit they should be moderated before the Confirmation"). "In the consistory, he says, the pope asked the cardinals' votes and confirmed by common consent" matches P3 l.58030-58040 ("Nel concistoro ... addomandate secondo il rito le sentenze de' cardinali, di comune consentimento l'approvò e 'l confermò per Bolla"); "he" follows Pallavicino's sentence, so the claim keeps its witness. The fixer's matching records claim (records.json l.3476) says the same and is right. |
| B2-M2 | CLOSED, fix right | `absent_details[1]` detail: "The Württemberg Confession handed in at Trent in 1552, and any Saxon confession". P2 l.22388-22390 ("i Vvirtembergesi ... presentata la lor Confessione in mano del Segretario"); the Saxons heard "Lo stesso giorno verso la sera" (P2 l.22414); S l.36636 margin "1552"; the Wittenberg envoys "were to tender the Confession" (S l.36658-36660), future. |
| B2-M3 | CLOSED, fix right | `record` witness: "Martin Luther's Smalcald Articles (1537), and the Lutherans' Formula of Concord (1577), in Jacobs's English Book of Concord". Luther is given only the Smalcald Articles. |
| B2-M4 | CLOSED | README l.22 now reads as proposed; the Formula sits with "four decrees", not the refusal list. "About 2:30" holds at 398 words. |
| B2-M5 | NOT CLOSED: the cut overstates its witness | See B3-B1. |
| B2-M6 | CLOSED, fix right | `Pope Paul III's bull of 1542 called the council to Trent, because the Germans "wished for the city of Trent."` W l.11982-11987 ("that they (the Germans) wished for the city of Trent ... we have chosen the city of Trent"); W l.12141 "Given at Rome, at St. Peter's, in the year MDXLII." Quote verbatim; the bull stays the witness. |

## New findings

### Blocking

**B3-B1. Blocking (a round 2 length cut gives the Saxon envoys' asking a "first" that Sarpi gives to the council's act).**

Location: brief, paragraph 4 (and audio): "Sarpi says they first asked the council to affirm it stood above the pope."

- Sarpi's speech, for Maurice by Badehorn, opens with a safe-conduct "in the form of that of Basil" and a delay "until his Divines be heard" (S l.36586-36612), then re-examination of the decrees (l.36613-36621). Only then come Constance and Basel, and the request: "Therefore prayeth the Assembly, That they would first repeat, approve, and ratifie the Article of the Superiority of the Council above the Pope" (S l.36622-36638). "First" governs the council's act ("That they would first ... ratifie"), not the order of the envoys' asks.
- Pallavicino agrees: the petitions were "à cinque capi" (P2 l.22420); the first was the safe-conduct (l.22422); the supremacy request is "In quarto luogo" (l.22531), that "innanzi à tutto si dichiarasse quello ponto da' Padri Tridentini" (l.22536-22537).
- As cut, the sentence tells the reader this was the envoys' opening demand. Neither historian says so. The old wording ("Before anything else, Sarpi says, they asked ...") was ambiguous; the cut made the wrong reading the plain one.
- Fix, brief paragraph 4: `Sarpi says they first asked the council to affirm it stood above the pope.` becomes `Sarpi says they asked the council to first affirm it stood above the pope.` (14 words, unchanged). Regenerate the audio from the fixed brief.
- After the fix: 398 words, 2:29 at 160 wpm, FK 7.74, Flesch 61.63, longest sentence 22 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/trent_r3_fix.txt`). The entry has no matching sentence (grep "above the pope|superiority|first asked" over the entry: none).

### Substantial

None.

### Minor

None.

## Verified

- **Every changed or added quote, verbatim.** "that our good works support salvation" (BOC l.30998-30999); "the decree of the Council of Trent" (BOC l.30994-30995, with hyphen break "de- cree"); "wished for the city of Trent" (W l.11983). Unchanged quotes in changed sentences: "will never permit him to be the judge", "a conspiracy and not a council" are outside the changed words and were not re-reviewed.
- **Translations in changed strings.** "argued against" for "disconsigliarono", "asked the cardinals' votes" for "addomandate ... le sentenze de' cardinali", "confirmed by common consent" for "di comune consentimento l'approvò e 'l confermò". Faithful; nothing added. (The pope also "approved"; "confirmed" alone omits nothing a reader needs.)
- **The Formula sentence in the audio.** The spoken "rejected the decree that our good works support salvation" has the Formula as its subject, so the "our" is the Lutherans'. "Support" renders the Formula's own verb (BENSOW "bevara", preserve), close to canon XXIV's "preserved ... through good works" (W l.13781-13785). Not a Lutheran gloss told as Trent's text in a way that misleads.
- **Sarpi and Pallavicino.** Every changed string keeps each historian as his own: "Sarpi says" (brief), "Pallavicino says ... he says" and "Sarpi says" (`uncertain[7]`), "by Sarpi's and Pallavicino's accounts" (`traditions`).
- **No orphaned witness tag.** B2-M5 keeps "Sarpi says"; B2-M6 keeps the bull as the witness to the reason.
- **Records.** Trent key equal to the working file. The added "exorbitant power" claim at records.json l.5235 is in the Poissy key, not Trent's; Trent's own (l.2947) is unchanged.

## Searches run

- No new absence was introduced in round 2. The narrowed `absent_details[1]` detail rests on round 2's search (`R2_recheck.md` Part B, "Searches run"), which I did not repeat beyond re-reading P2 l.22380-22420 and S l.36570-36662.
- `Trent|Tridentin` in BOC: the Formula's own mention at l.30995; the rest are Jacobs's footnotes (l.8975, 25662, 26145, 26934, 26937, 27469, 32861).
- `1542|MDXLII` in W: the bull's date at l.12141.
- `above the pope|superiority|first asked` in the entry: none.

## Counts

Blocking 1, Substantial 0, Minor 0.

---

## Council profiles, era 7 batch 2, round 3: Part C (Diet of Augsburg and the Religious Peace 1555)

**Council.** `diet-of-augsburg-1555` (distinct from `diet-of-augsburg-1530`).
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1555.brief.txt`, `audio/diet-of-augsburg-1555.audio.txt`, `diet-of-augsburg-1555.entry.json` (`uncertain[9]`, the only changed string), `records.json` key `diet-of-augsburg-1555` (`contested_claims[4]`, the only changed string; the key equals `working/records_diet-of-augsburg-1555.json`, checked by script: 105 claims, 8 contested claims, 12 absent details), and the README "Batch 2" line "Diet of Augsburg 1555 (about 2:30)" (unchanged). Scope: `git diff 7ad6d2a2 HEAD` restricted to this council, checked against `R2_recheck.md` Part C and `R2_changes.md` Part C.
**Brief.** 399 words (2.49 min at 160 wpm). `grade_text` via the batch's `grade.py`: FK 7.87, Flesch 62.60. Longest sentence 25 words ("Religion was to be handled in an assembly of Catholics and heretics, and he thought a legate no fit witness to such a monstrous thing."; unchanged). None over 25. The changed sentence is 10 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Entry.** JSON parses. Changed `uncertain[9]`: four sentences of 4, 13, 12 and 11 words.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or fixing. Read and grep only. No repo file edited. No model, network or paid calls.

Abbreviations: PALL2 = `cic/texts/pallavicino_istoria-del-concilio-di-trento-parte2-ita_1664.txt`; POL5 = `cic/texts/polanco_chronicon-v5-lat_1897.txt`.

## Verdict: PASS (no blocking, no substantial, no minor)

Both round 2 findings are closed, and the fixes say only what their witnesses say.

**The key sentence.** Brief p.13: "Ferdinand answered sharply, Pallavicino says, feeling the concessions plainly necessary." Pallavicino's sentence in context, PALL2 l.27564-27576 (book 13, chapter 14):

> "ERA vscito il Recesso in sù lo spirar di Settembre: e'l Papa informatone fé perciò asprissime querele col Rè Ferdinando espostegli dal Nunzio Delfino che di Roma sul principio dell'anno seguente 1556. ritornò ad esercitare il carico antico. Mà il Rè, parendogli e che nelle concezioni [concessioni] dannose a cattolici la manifesta necessità l'havesse tenuto lungi da-* e che nelle cose arbitrarie à sé, si fosse per lui dimostrato ogni maggior zelo, rispose con maniere più risentite di quel che portava l'uso della sua temperata natura."

- Who speaks: Pallavicino, telling Ferdinand's view ("parendogli", it seemed to him). The brief keeps it inside "Pallavicino says" and gives it as Ferdinand's feeling, not his words. The round 2 error (necessity put into the answer by "pleading") is gone.
- Which side and what: the concessions are the ones harmful to Catholics, made in the recess; necessity is "manifesta" (plainly). "Feeling the concessions plainly necessary" uses only legible words. Whatever the lost word after "lungi da" is, the legible clause has plain necessity governing the concessions in Ferdinand's view; the brief claims no more.
- Cause: Pallavicino gives this view as why he answered sharply ("parendogli ... rispose con maniere più risentite"). The participle "feeling" carries that link without stating what the answer said.
- Omitted, not misstated: the second half of Ferdinand's view (greatest zeal where the choice was his) and Pallavicino's further "fors'anche" cause (Paul's ill will toward the House of Austria, l.27576-27579; the latter is in entry `uncertain[11]`). Leaving them to the entry is fair at this length.
- Antecedent: "the concessions" follows "called the recess ruinous" in the same paragraph, so it reads as the recess's terms, which is Pallavicino's referent.

**The matching entry and records strings.**
- Entry `uncertain[9]`: "Pallavicino says he 'consented to very grave losses for the Catholic religion'. Pallavicino adds that Ferdinand felt the harmful concessions were plainly necessary." The first sentence is PALL2 l.27413-27414 ("consentì à grauissimi detrimenti della Religion Cattolica"), book 13 chapter 13; the second is l.27569-27572, chapter 14. "Adds" is right: two passages by the same author. "Harmful" renders "dannose". "Felt" renders "parendogli". The fixer was right to change these too, not leave them: chapter 13's excuse (l.27415-27434, "Scusavasi egli di ciò con addurre") names Charles's curt reply, the feuds and Naumburg, and has no "necessità" in it; "pleaded necessity" had no ground in either passage.
- Records `contested_claims[4]` `sides`: "He 'consentì à grauissimi detrimenti della Religion Cattolica', and Ferdinand felt ('parendogli') the harmful concessions plainly necessary: Pallavicino (... l.27413, 27568-27574)". Quote verbatim (PALL2 l.27413-27414, long s read as s). "Parendogli" is verbatim at l.27569. The cited range covers the "parendogli" clause (l.27569-27572). Agrees with the brief and with `claims[73]` and entry `outcome[2]`, which already say "it seemed to Ferdinand" / "felt".
- No "plead" or "pleaded" remains anywhere in the brief, entry or this records key (grep).

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| C2-M1 | CLOSED; fix right, and the optional entry/records part rightly applied | Brief p.13, entry `uncertain[9]`, records `contested_claims[4]` as above. PALL2 l.27564-27576 ("parendogli ... la manifesta necessità ... rispose con maniere più risentite"); l.27413-27434 (chapter 13 excuse, no "necessità"). |
| C2-M2 | CLOSED | Brief p.1: "Ferdinand, King of the Romans, came out with bishops and princes to meet him, writes the Jesuit Juan Alfonso de Polanco." POL5 l.15370-15372 "magnifice a Rege Romanorum, Cardinali augustano et aliis Episcopis et Principibus excepti fuerunt; qui fere leucam unam obviam Legato processerunt". The cut removes only "almost a league"; the scene and its witness tag stay. Entry `issue` and records keep the distance, so nothing disagrees. "Five days later" still holds (vigil of the Annunciation, 24 March; death news "29.*", l.15373-15374). |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

None.

## Verified

- **Changed brief strings**, against their source lines in context: p.1 (POL5 l.15369-15376); p.13 (PALL2 l.27564-27579, and l.27405-27440 for the chapter 13 excuse).
- **Quotes re-verified verbatim** (OCR and long s allowed for): 'consentì à grauissimi detrimenti della Religion Cattolica' (PALL2 l.27413-27414, "grauifsimi"); 'parendogli' (l.27569). Translation "consented to very grave losses for the Catholic religion" is faithful and adds nothing.
- **No new quote** in the brief. No new absence claim (`absent_details[11]` is unchanged from round 2).
- **Witness tags.** "Pallavicino says" still sits with the changed sentence; "writes the Jesuit Juan Alfonso de Polanco" still sits with the cut sentence. None orphaned.
- **Pallavicino given as his.** Every changed string attributes the view to Pallavicino; none gives it as settled fact.
- **Writing.** The changed sentence has no empty contrast, no summing-up line, no filler; 10 words. Brief 399 words, under the ceiling, Flesch 62.60 (at least 60).
- **Audio** matches the brief with the two tags (diff). **Entry JSON** parses. **records.json key** equals the working records file.
- **README line** "Diet of Augsburg 1555 (about 2:30)" still true at 399 words (2:29). Unchanged and needs no change.

## Searches run

1. `grep -n "parendogli\|temperata  natura\|grauifsimi  detrimenti\|Delfino  che"` in PALL2: confirms line numbers l.27413, l.27567, l.27569, l.27576.
2. `grep -n -i "plead\|necess\|18 December\|ruinous\|concession"` in the brief and entry: no "plead" left; `outcome[2]`, `uncertain[9]` and brief p.13 agree.
3. Script over records key `diet-of-augsburg-1555` for `necess|plead|parendo|lungi|ruin|December`: `claims[49]`, `claims[73]`, `claims[85]`, `contested_claims[4]`, `absent_details[11]`; all agree with the brief; no "plead" left.
4. `grep -rl "leucam"` over Polanco files, then POL5 l.15366-15382: confirms the scene for C2-M2.

## Counts

Blocking 0, Substantial 0, Minor 0. Brief: 399 words, 2.49 min, FK 7.87, Flesch 62.60, longest sentence 25.

---

## Council profiles, era 7 batch 2, round 3: Part D (Colloquy of Poissy 1561)

**Council.** `colloquy-of-poissy-1561`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/colloquy-of-poissy-1561.brief.txt`, `audio/colloquy-of-poissy-1561.audio.txt`, `colloquy-of-poissy-1561.entry.json`, `records.json` key `colloquy-of-poissy-1561` (113 claims, 12 contested claims, 7 absent details; equal to `working/records_colloquy-of-poissy-1561.json`, checked by script), and the README "Colloquy of Poissy (about 2:30)" line. Scope: `git diff 7ad6d2a2 HEAD` for this council only, against `R2_recheck.md` Part D and `R2_changes.md` Part D.
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm). `grade_text`: FK 7.50, Flesch 65.65. Longest sentence 25 words ("In January 1562 a royal edict ...", unchanged). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag (checked by stripping the two tags and diffing: identical).
**Reviewer.** Fresh Opus, full effort. Read and grep only; no repo file edited; no model, network or paid calls. Scratch copies at `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/poissy_r3/`.

Abbreviations as in rounds 1 and 2 (HE1, AYM, LAI6, LAI8, PAL1, SARPI, WAT).

## Verdict: REVISE (1 blocking, 0 substantial, 0 minor)

Round 2 fixed Sarpi's label. He is now "the Venetian friar Paolo Sarpi, hostile to the papal court", which matches the batch. But the fix kept the frame "The Catholic side speaks through Jesuits ... So do two historians of Trent". That frame now says outright that a witness hostile to the papal court speaks for the Catholic side. At Poissy that side was the prelates and the pope's legate. Sarpi's own Poissy chapter does not speak for them (D3-B1). The fix is word-neutral and keeps the brief at 400 words.

The "two meetings" change holds, in both the brief and the entry. Every other round 2 fix is closed and right, and every changed quote is verbatim.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| D2-S1 | PARTLY CLOSED; see D3-B1 | The label is closed. Brief p.2: "the Jesuit Sforza Pallavicino and the Venetian friar Paolo Sarpi, hostile to the papal court." It matches Regensburg and Trent ("The Venetian friar Paolo Sarpi was hostile to the papal court"). The appositive sits right after Sarpi's name, so it attaches to him alone. New `claims[112]` holds "hostile": SARPI l.8828-8830, "the See of Rome ... exorbitant power, mounted from ſmall beginnings by divers degrees unto an unlimited exceſs, it hath ſo eſtabliſhed and confirmed the fame". That is Sarpi's own opening judgment, and the claim renders it faithfully. Not closed: the side. "So do" still puts him in "the Catholic side speaks through". The finding's own heading was "a side that is not quite his". |
| D2-M1 | CLOSED | Entry `calledBy`: "Her two meetings 'à deux divers jours' fit the sessions Polanco dates to 24 and 26 September." (17 words). The quote is verbatim: AYM l.25545-25546, "de deux Communications qu'ils a voient faites à deux divers jours". "Her" is fair, because the letter says she thought it good that the prelates meet the ministers (l.25539-25543), and `calledBy` is about who called them. "Fit" keeps the identification as the profile's own. The dates check out. Polanco's letter of 27 September gives "El miércoles passado" (LAI6 l.3606-3607; the editors' note 4 reads "Id est 24 Septembris 1561", l.3634), and "El viernes siguiente, que fué ayer 26 de Setiembre" (l.3653). Records `claims[67]` agrees. |
| D2-M2 | CLOSED | `claims[81]` witness is now "l.9099-9102; for "canonists", l.7353-7358, 9761-9762, 10501-10502". The corrected range is right. l.9761 ends "the" and l.9762 begins ")nists, Boncompagno, Fachenetti, Paleotto, Lancellotto". l.7353-7358 gives Simonetta "his intimate acquaintance with canon law", with the four assistants. l.10501-10502 gives "Castagna ... one of the most able canonists of his day". The entry is unchanged. |
| D2-M3 | CLOSED | Entry `traditions` (the-society-of-jesus): "It came in as a college, not a new order, on condition it take another name." Source: LAI8 l.39603-39605, "par forme de collége et non de religión nouuellement institutée, á la charge qu'ilz seroient tenuz prandre aultre tiltre que de société de Jésus ou de Jésuites". The condition is now told as a condition. |
| D2-M4 | CLOSED | All four cuts are in place: "refectory", "directed it", "to give the ministers a safe-conduct and a hearing" and "spoke to the queen". The rendering in P3 is faithful to HE1 l.25997-25998, "auroient faufconduict pour l'y trouver, & y eftre ouis". "The History says" still sits on the aim in the next sentence. No witness tag was orphaned. "Italian" stays in the entry's `record`. |
| P7 observation | CLOSED | Brief p.7: "Catherine wrote that two meetings bred disputes upon disputes, far more than union." Source: AYM l.25545-25548, "de deux Communications ... Confufion de Difputes fur Difputes nourries de Diffencions & Difcordes beaucoup plus que d'Union". This is now limited to the two meetings, which come before the five-and-five in her letter ("je m'advifé de faire effiier fi par cinq ou fix", l.25550-25551). The sentence is faithful and adds nothing. It agrees with `calledBy` and with `outcome`. |

## New findings

### Blocking

**D3-B1. Blocking (a witness given a side that is not his, in the brief; from the D2-S1 fix).** Brief p.2: `The Catholic side speaks through Jesuits who came with the pope's legate. So do two historians of Trent, the Jesuit Sforza Pallavicino and the Venetian friar Paolo Sarpi, hostile to the papal court.`
- "So do" makes both historians voices of "the Catholic side". In this brief that side is the prelates who stood with the pope's legate against the Reformed, the counterpart of "It tells the Reformed side". The new appositive now tells the listener that the same man was hostile to that side's head. As written, the sentence puts an anti-curial writer in the papal party's mouth. Pallavicino's whole book was written to refute him as "un'istoria falsa" (PAL1 l.1).
- Sarpi's own Poissy chapter does not carry the prelates' case. He gives the Chancellor urging the bishops "not to be averſe from the Proteſtants, who were their Brethren" (SARPI l.42805). He has Tournon rise "full of -difdain" (l.42840). On the one point the brief takes from him, he says Beza spoke "with ſuch heat, that bogeve [OCR for "it gave"] ill fatisfaction to thoſe'of his vwis [own] party ; ſothat he was command.ed to conclude" (l.42836-42838). That detail runs against the History, but Sarpi gives it as Beza's own party's displeasure, not as a Catholic charge.
- He is a Catholic witness, and his side is "Catholic but hostile to the papal court" (entry `record`, D-S5). The pattern asks that a partisan witness carry his own side (Pattern C1; review_brief_r1 Severity: "a claim given to the wrong witness ... or anything else wrong or misleading in the brief"). The README's new reason, "each Catholic witness with his own side", promises the same thing. In batch 1, the blocking point after round 3 was a round 2 fix that overstated its witness. This fix is the same kind.
- Fix, brief p.2 (replace these two sentences; they are 12 + 21 = 33 words now, and become 18 + 15 = 33): `The Catholic side speaks through Jesuits: those with the pope's legate, and Sforza Pallavicino, a historian of Trent. Another historian of Trent, the Venetian friar Paolo Sarpi, was hostile to the papal court.`
  - The second sentence matches the batch label word for word ("The Venetian friar Paolo Sarpi was hostile to the papal court"). "Another" claims no count of Trent's historians.
  - Pallavicino keeps "Jesuit" through the colon. "Those with the pope's legate" are the same Jesuits as before.
  - Apply the same change to `audio/colloquy-of-poissy-1561.audio.txt` (regenerate with `mkaudio.py`).
  - No entry or records change is needed. `record` already places both men, and `claims[110]` and `[112]` hold Sarpi's order and stance.
  - The README line stays true and needs no change.
- Checked on a scratch copy: 400 words (2:30), FK 7.58, Flesch 65.01, longest sentence 25 words (unchanged). The new sentences are 18 and 15 words.

### Substantial

None.

### Minor

None.

## Verified

- Every changed brief string, read against its source in context: p.1 "refectory" (HE1 l.27648); p.2 "directed it" (Reuss's view unchanged); p.2 the Sarpi sentence (see D3-B1); p.3 safe-conduct (HE1 l.25997-25999); p.5 Laínez on 26 September (LAI6 l.3653); p.7 "two meetings" (AYM l.25545-25548).
- Changed or added quotes, verbatim: "à deux divers jours" (AYM l.25546); "exorbitant power" (SARPI l.8829, in `claims[112]`); "canonists" (WAT l.10502). The French in D2-M3 is unchanged and matches LAI8 l.39603-39605.
- Translations and renderings: `claims[112]`, "the council confirmed the 'exorbitant power' of the See of Rome", is faithful to SARPI l.8826-8830. In that passage Rome feared the council as a means to moderate its power, and the council "eſtabliſhed and confirmed the fame". `claims[67]` adds nothing to the letter: the identification is marked as fitting Polanco's dates.
- Records: the working file equals `records.json`. `claims[112]` was appended, so no index moved. The shared fields (`claim`, `witness`, `witness_kind`, `formation_confidence`) are present.
- Entry sentence lengths in the changed strings: `calledBy`'s new sentence is 17 words; the Jesuit note's new sentence is 15. None is over 25.
- Audio equals the brief apart from the two tags.
- README line: "so its standing must be placed, and each Catholic witness with his own side". It is true of the brief once D3-B1 is applied. The time "about 2:30" is true at 400 words.

## Searches run

No new absence is asserted in the changed text. Reads and greps for the points above:
- SARPI l.42760-42900 (the whole first-session passage); `grep -n` for "Brethren, repe|fatisfaction to thoſe|full of -difdain|ed to conclude" (hits l.42805, 42837, 42838, 42840); l.8818-8838.
- AYM l.25530-25560 (the body of Catherine's letter).
- LAI6 l.3595-3656 (Polanco's postscript, the editors' notes on the days); `grep -n -i "miércoles|viernes"`.
- LAI8 l.39598-39606.
- WAT l.7352-7359, 9097-9103, 9759-9763, 10500-10503.
- PAL1 l.1 (title).
- The era 7 briefs: `grep -o` for Sarpi sentences and `grep -n` for "speaks through|Catholic side" (label and framing comparison).

## Counts

Round 2 findings: 5 (D2-S1, D2-M1 to D2-M4), plus the P7 observation. 4 are closed (D2-M1 to D2-M4), and the observation is closed. 1 is partly closed (D2-S1): the label is fixed, the side is not, and this carries into D3-B1.
New: Blocking 1 (D3-B1). Substantial 0. Minor 0.
Brief: 400 words (2:30) now; 400 words (2:30) with D3-B1, FK 7.58, Flesch 65.01, longest sentence 25 words.
