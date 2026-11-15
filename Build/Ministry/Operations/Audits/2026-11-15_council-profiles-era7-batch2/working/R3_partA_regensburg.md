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
