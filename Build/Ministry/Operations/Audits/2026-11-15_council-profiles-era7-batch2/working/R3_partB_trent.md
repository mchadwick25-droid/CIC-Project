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
