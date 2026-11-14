# R4 cap check: era 4 batch 3

## Scope

One targeted check, under Mark's standing ruling of 2026-11-14 (Decision-Log, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"). It does not count toward the three-round cap. It covers only the strings changed in commit 91ac7e3a under `Who-Profiles/era4/batch3/`:

1. Cuthbert of Lindisfarne, card `uncertain` item 7: the Ripon item (R3-M1).
2. Cogitosus, brief P1 and `audio/cogitosus.audio.txt`: "Painted boards adorned the church, and one wall bore pictures." (R3-M3).
3. Cuthbert, `records.json`: the Ripon claim and the new Raine claim (R3-M2).
4. `README.md`: the length line (R3-M4).

Reviewer: independent Opus, first sight of these files and of the drafting. I edited no profile file, made no git writes and made no web, paid or model calls. I used local reads, read-only git, a JSON load and `grade_text` only.

## Method

- I read `R3_recheck.md` (R3-M1 to R3-M4) and `R3_changes.md`, then `git show 91ac7e3a` over the batch folder.
- I opened every cited line in the vendored file myself and read the passage around it: AASS3 l.33596-33603, 34603-34614 and 34676-34686; GILES l.13994-14002; PL72 l.59425-59434; RAINE l.4930-4997, from the heading of Stephen's chapter VIII through note 4. OCR noise and hyphen breaks were read through.
- For each string I checked what the source says, the witness, any quotation word for word, pronoun reference, sentence length and AI tells, contrast frames and beat lines.
- By script: `json.load` on every card and on `records.json`; audio against brief plus tags; word counts and times at 162 words a minute; `grade_text` on the Cogitosus brief.
- Commit scope: `git show --stat 91ac7e3a`, and `git status` / `git diff 91ac7e3a` on the folder to see that the working tree matches the commit.

## 1. Cuthbert, card `uncertain` 7: PASS

String: "Ripon. Bede's prose Life says Eata took Cuthbert to found a monastery at Ripon, and that both were later driven home. Bede's History says the founders left rather than take the Roman Easter. The Bollandists join the two accounts." (1, 20, 12 and 6 words.)

- The founding: AASS3 l.34606-34612, "locum quemdam regni sui, qui vocatur Inrhipum, ad construendum ibidem monasterium Eatae Abbati donare, tollens idem Abbas quosdam e Fratibus secum, in quibus et Cuthbertum, condidit ibi quod petebatur monasterium". Holds. This is Bede's prose Life, chapters 7-8 ("Interea quia fragilis est et more freti volubilis omnis seculi status" opens chapter 8).
- "Driven home": l.34680-34682, "Abbas Eata cum Cuthberto et ceteris, quos secum adduxerat, Fratribus domum repulsus est". "Repulsus" is driven back, so the verb now keeps its force, as R3-M1 asked. "Both" points to Eata and Cuthbert, the two men just named, and the Life puts both under "repulsus". Holds.
- The History: GILES l.13997-14001, "they afterwards, being left to their choice, would rather quit the place than adopt the catholic Easter, and other canonical rites, according to the custom of the Roman" church. "The founders" are "those that followed the doctrine of the Scots, to build a monastery upon" (l.13997-13998). "Left rather than take the Roman Easter" says what Bede says. Holds.
- "Bede's History" now names its author, so the "His" that could be heard as Cuthbert's is gone (R3-M1). Holds.
- The Bollandists: AASS3 l.33599-33601, "Cum ergo SS. Eata, Cuthbertus aliique propter Pascha Catholicum ceterosque ritus reliquerunt Riponense monasterium". They join the leaving to the Easter reason. "Join" carries no "only", so it stays true beside Raine (item 3). Holds.
- Witness: each sentence names its witness (prose Life, History, Bollandists).
- Writing: short sentences, no AI tell, no contrast frame. The closing "The Bollandists join the two accounts." carries a fact and is not a beat line, as R3 also found.

## 2. Cogitosus, brief P1 and audio: PASS

String: "Painted boards adorned the church, and one wall bore pictures." (10 words.)

- Source: PL72 l.59427-59432, "Ecclesia namque ... decorata pictis tabulatis, ... in quo unus paries decoratus, et imaginibus depictus". The painted boards are on the church itself, and one wall is painted with images. Holds.
- Reference: "the church" replaces the "it" that could be heard as the altar or the tomb (R3-M3). The paragraph's first sentence, "the great church of Kildare", is its antecedent. Holds.
- Witness: the paragraph ends "So, the writer says", and paragraph 2 names the writer as Cogitosus. Unchanged, and enough for a scene drawn from his text.
- The rest of P1 reads in order around it (17, 19, 10, 20 and 16 words).
- Audio: `audio/cogitosus.audio.txt` equals the brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, one of each.
- `grade_text` on the brief: FK 7.85, Flesch 64.90. Passes (FK 10 or below, Flesch 60 or above). 327 words, about 2:01.

## 3. Cuthbert, `records.json`: PASS

Ripon claim, changed tail: "the Bollandists join this to the History's Easter reason; so does James Raine's note to Stephen's chapter 8, citing Bede's Life of Cuthbert (RAINE l.4986-4995, in the claim below)".

- "Alone" is gone, so the false absence R3-M2 found is gone.
- Raine's note: RAINE l.4986-4995 is note 4, on "Hrypis", in Stephen's "[CAPITULUM VIII.] De eo quod dedit ei Alhfrithus coenobium in Hrypis" (l.4936-4938). It reads: "Ripon, where Alchfrid had founded a monastery, which he had given in the first instance to Eata, abbot of Melrose. When the Scottish party refused to give up their anti-catholic views, Alchfrid removed them, and gave Ripon to Wilfrid. See Beda's Life of Cuthbert, capp. vii." "Note to Stephen's chapter 8, citing Bede's Life of Cuthbert" holds. Raine sets the Easter reason ("anti-catholic views") beside the removal and cites the Life for it, so "so does" holds.
- The witness stays AASS3, and the claim points to the Raine claim by its lines. R3_changes.md gives the reason: each claim cites one file. That differs from R3-M2's wording but meets its aim. "Below" is true; the Raine claim is the second after it.
- The other quotations in this claim did not change. I checked them anyway against AASS3 l.33599-33601, 34610-34611 and 34680-34682. They are verbatim, with the file's "ceteros-" / "que" line break kept, as elsewhere in the records.
- `formation_confidence` stays Inferential-Thin, as R3-M2 asked.

New Raine claim: "Raine's note: \"When the Scottish party refused to give up their anti-catho- lic views, Alchfrid removed them\"; \"See Beda's Life of Cuthbert\"", witness RAINE l.4986-4995.

- Both quotations are verbatim against l.4990-4993 and l.4994-4995. "anti-catho- lic" keeps the file's line break, the records' habit. "Beda’s" in the file has a curly apostrophe, folded.
- The witness file and lines are right.
- `formation_confidence` "Dominant Modern Reconstruction" is one of the five levels. It is a fair rating for an editor's 1879 reconstruction that agrees with the Bollandists. Jane's note on Wiltenburg (records l.272) is rated Contested, but that note disputes an identification, and this one does not. Not a finding.

## 4. README length line: PASS

String: "All eight run 327 to 346 words, about 2:01 to 2:08."

- By script, at 162 words a minute: Cogitosus 327 (2:01), Theodore 329 (2:02), Willibrord 332 (2:03), Cuthbert 335 (2:04), Tirechan 336 (2:04), Leoba 337 (2:05), Muirchu 338 (2:05), Wilfrid 346 (2:08). The range and times match. Holds.

## Commit scope and JSON

- `git show --stat 91ac7e3a`: the five profile files above, each changed only in the listed strings (README one line, Cogitosus brief and audio one line each, Cuthbert card one line, `records.json` the Ripon claim and the added Raine claim), plus `R3_changes.md` and `R3_recheck.md`. `R3_recheck.md` is the round 3 review itself, the permanent audit trail, not a profile change. Nothing else changed.
- The working tree matches 91ac7e3a for the batch folder.
- All eight cards and `records.json` load with `json.load`. PASS.

## Findings

None. No BLOCKING or MINOR finding.

## Verdict

CLEAR.

- The Cuthbert Ripon item keeps the Life's "repulsus" as "driven home", names Bede for the History, and says no more than AASS3 l.33599-33601, 34606-34612, 34679-34684 and GILES l.13996-14001 carry.
- The Cogitosus sentence puts the painted boards on the church, as PL72 l.59427-59432 does. Audio matches, and the brief scores FK 7.85, Flesch 64.90.
- The records drop the false "alone" and hold Raine's note verbatim, with its witness (RAINE l.4986-4995).
- The README range is true. Every file parses, and nothing outside the listed strings changed.
