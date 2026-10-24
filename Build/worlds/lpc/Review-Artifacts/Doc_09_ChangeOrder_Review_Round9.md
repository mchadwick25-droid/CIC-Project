Simulated review — informational only, not an Article 31 substitute.

# Doc_09 full review after change order CO-LPC-1

- **Document:** `Build/worlds/lpc/Doc_09_Story_Inventory.md`, with `Build/worlds/lpc/Story-Chunks/` (seven chunks), `records/lpc/story/` (seven records) and the generated `Build/worlds/lpc/lpc_Story_Index.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `4e7a4bd9`; Doc_09 is unchanged since commit `949edbcf`, "lpc change order, part 2", and is the same blob at `a0209b8d`)
- **Round:** 9
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent adversarial review subagent, fresh context (drafted none of the text under review)
- **Drafter:** Sonnet 5.5 drafters for CO-LPC-1 (Doc_09 line 11, §6 item 5 line 110, §7 item 5 line 128, §8 item 4 line 137), checked by the `lpc` build thread; earlier text by the `lpc` build thread (draft 2026-09-15, Round 1 to Round 8 fix passes 2026-09-15; drafting model not recorded in the log)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** CO-LPC-1 drafters and the `lpc` build thread
- **Date:** 2026-10-23
- **Scope:** full review of Doc_09, its chunks and its story records in their current state: every substantive claim; quotations re-verified word for word against `cic/texts/` at their structural markers and against CF V7.4 Part II; consistency with the 2026-10-23 rulings (D1 to D5, Doc_02 §7, Doc_05 crosswalk, Article 20, lexicon discovery method, liturgical candidates, the `lpcstory006` rulings) and with OG-28 to OG-51; the CO-LPC-1 edits (diff `949edbcf^..949edbcf`); and what the `lpcstory006` story text gets wrong against `Review-Artifacts/Doc09_Acta_Proconsularia_Read_lpcstory006_2026-10-23.md`. No tier is recommended for `lpcstory006`. The Forces Framework integration requirement does not apply to Doc_09. Prior review files read: `Doc09_Round1_Review.md` to `Doc09_Round8_Review.md` (Round 8 in full; earlier rounds for their findings ledgers).
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md:6875`), which names this file. `roundcount lpc 9 --check-new` reports 8 files on record and routes to the project lead, which that ruling covers.
- **Truncation check, method 1:** line and byte count with an end-of-file read: `wc` gives 182 lines and 40,741 bytes; the file was read in full through line 182, which ends "…and it has now had seven review rounds.**", and all eleven `## ` headings are present in order (§1 to §8, Document Log, Disposition, plus the subtitle).
- **Truncation check, method 2:** hash comparison against the committed blobs: `git hash-object` of the working file, `git rev-parse HEAD:<path>` and `git rev-parse a0209b8d:<path>` all give `395b229e4cbbe1df1887b0b415f888e8e54030f3`.
- **Method limits:** no web search and no model call. Nothing edited except this file. CF V7.4 was read from `word/document.xml` with tags stripped. Chunk and record quotations were checked by script against `anf05` and the Possidius file with XML tags and endnotes stripped; every miss was then read by hand at its line.

---

## What was checked and found sound

- **Every Story Text quotation in the seven chunks holds at source**, apart from the `lpcstory006` issues below and the disclosed capitalisation convention (Doc_09 line 31). Hand-checked misses were all endnote markup inside the ANF sentence: *Ep.* LIX §1 and §3 (`anf05` lines 36000–36090, "With excessive grief of mind, and not without tears"; "sharers in your anxiety"; "one hundred thousand sesterces" at 36082); *Ep.* XXI (`anf05` 30706–30722, "so intolerable that nobody could bear it", the martyr list); *Ep.* XXXIV (`anf05` 32110, "remained unwillingly"); Pontius §§9–10 (`anf05` 27956, 27992); Possidius XXXI (`possidius_vita-augustini_weiskotten1919.txt` 4924–4934 and 4979–4980). No invented participant, event or outcome was found.
- **CF V7.4 quotations in §2 and §3.1** are verbatim (extracted text, Part II tier definitions and the Tier 4 "How to use" paragraph). One sentence start is lower-cased ("the construction notes must…"); trivial.
- **Prosper's entry** in `lpcstory007` matches the OCR exactly (`prosper_chronica-minora-1-lat_mommsen1892.txt` 54206–54209).
- **Doc_08 §2B-5's "thirteen letters" quotation** (Doc_09 line 66) holds at `anf05` 30188–30190.
- **The Possidius headings** at §7 item 5 hold (`possidius…` 3137–3613); Possidius's quotation of *De Mortalitate* (§7 item 1) holds at 3877–3878.
- **CO-LPC-1's Gesta edits** (lines 110 and 137) are correct: they match Doc_08 lines 358 and 438 and Doc_04's closure of item 6 (OG-38, OG-40).
- **The Acta reading note's key Latin was spot-checked** at `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` 41344–41357, 41510–41520 and 41576–41600, and Harnack at 5232–5239. The note's readings hold.
- **Doc_02 §7 quotation** at line 23 still holds after the restatement (Doc_02 line 122), and Doc_02 §1's "native to one, etic evidence for the other" holds (Doc_02 line 25).

---

## P0 — blocking

None.

## P1 — substantial

**P1-1. §6 item 1 and §8 item 5 say the sermons on Perpetua and the Scillitan martyrs are not available to this build at all. They are vendored, and Doc_02 says so.**
- *Where:* `Build/worlds/lpc/Doc_09_Story_Inventory.md:106` ("the sermon texts are not available to this build at all. Unavailable is a different problem from unread … the only story-candidate in this document blocked that way"); `:138` ("unavailable, not unread … An acquisition question for the project lead").
- *Evidence:* `cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt:89935` (SERMO CCLXXX, "In Natali martyrum Perpetuae et Felicitatis, i", line 89937), `:90170` (CCLXXXI), `:90261` (CCLXXXII); `cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt:1361` and `:8466` ("De natale sanctorum Scillitanorum"). Doc_02 after CO-LPC-1 says the same: `Build/worlds/lpc/Doc_02_Source_Ecology.md:137` ("Sermons 280–281 on Perpetua and Felicitas … in the Latin of PL 38, row 216, and has not been read"), and `:31` and `:49` make these files the quote base for the sermon scope. Doc_01 line 26 puts all Augustine's sermons inside the world (D1).
- *Why substantial:* this is the defect pattern this document's own Disposition names: a silence claimed about a source that the corpus refutes. CO-LPC-1 brought the sermons into scope and edited Doc_09, but left both sentences standing. They now contradict Doc_01 and Doc_02. They also send a reading task to the project lead as an acquisition task.
- *Fix:* restate both items. The sermons are vendored in Latin (PL 38, row 216; Morin 1917, row 267) and unread for this document. Building the story is a reading task under the sermon scope, subject to the OCR limits Doc_02 line 49 states. Drop "the only story-candidate … blocked that way". At §6 item 4, note that the sermon scope also bears on the healing-miracle candidate.

**P1-2. The *Acta Proconsularia* is described as unread, as vendored only inside Hartel's volume, and as "the court's own record". All three are now wrong, in Doc_09 and in the fields that instruct the Representative.**
- *Where:* Doc_09 `:107` ("vendored in Latin only, inside row 194's Hartel volume"; "the one strictly documentary … record"; "licensable and simply not yet done") and `:134` ("The *Acta Proconsularia* is unread"). In the chunk: `Story-Chunks/lpcstory006_the-death-of-cyprian.md:6` (Source: "has not been read in this build"), `:8` (Do-Not-Retrieve), `:47` ("the *Acta* is unread"), `:55` (Usage Guidance part three: "this build has not read it"), and `:63` ("the court's own record of the proceedings … this build has not opened it"). In the record: `records/lpc/story/lpc.story.the-death-of-cyprian.md:25`, `:36`, `:83` and `:86–87`.
- *Evidence:* `Review-Artifacts/Doc09_Acta_Proconsularia_Read_lpcstory006_2026-10-23.md` §§2–4. Three printings of Hartel's text are vendored: H `cyprian_opera-spuria…:41413–41626`, `gebhardt_acta-martyrum-selecta…1902.txt` no. XI, and `knopf_ausgewaehlte-maertyrerakten…1929.txt` no. 13 (OG-49, correction 1). The text carries Christian framing, such as "beatum Cyprianum" (H 41463) and the closing doxology (H 41625–41626). So "the court's own record" and "strictly documentary" are not supported (OG-49, correction 2). The provenance column of Registry row 41 marks that phrase as builder prior knowledge.
- *Fix:* do this within the `lpcstory006` change order already ordered (Decision Log, 2026-10-23, "`lpcstory006` re-tiered…"; OG-49). Remove every "unread / not opened / not read in this build" statement. Describe the *Acta* as an early, unnamed Christian compilation built around the hearing records, in one edition (Hartel's) and three printings. Update §6 item 2 and §8 item 1 to say it has been read, and what it confirms and does not confirm.

**P1-3. What the `lpcstory006` story text gets wrong (reported as ordered; no tier is recommended).**
- *Where:* `Story-Chunks/lpcstory006_the-death-of-cyprian.md:17`, `:21`, `:61`; `records/lpc/story/lpc.story.the-death-of-cyprian.md:71–74`, `:81–83`.
- *Errors, each checked at source:*
  1. **"Then the bishop bound his own eyes"** (chunk `:21`, record `:71`). This repeats Pontius's *"per manus suas"* (H 41353; `anf05` 28260) as narration. The independent witness differs. In it he covers his eyes with his own hand, cannot tie the cloths, and *"Iulianus presbyter et Iulianus subdiaconus ei ligauerunt"* (H 41592–41594). The sentence states as fact a detail the second witness contradicts.
  2. **"The executioner could not do it"** (chunk `:21`). This overstates even the translation it relies on. ANF says the man "with difficulty clasped the blade" (`anf05` 28262–28263): he did it with difficulty. The Latin *"labente dextera gladium vix trementibus digitis circuibat"* (H 41354–41355) has a disputed subject. Harnack makes Cyprian the one whose fingers barely tremble as he guides the sword (`harnack_vita-cypriani-commentary-lat-deu_1913.txt` 5232–5239). The record's "could not do it easily" (`:72`) is closer to ANF but does not disclose the dispute either.
  3. **"The ground beyond was open"** (chunk `:17`). ANF says the place "is level, so that it affords a noble spectacle, with its trees thickly planted on all sides" (`anf05` 28254–28256), and Hartel's text prints the conjecture *"conuallis"* (H 41344). "Open" is not in any witness.
  4. **"What cannot be told is what the crowd made of it"** (chunk `:61`; record `:81`). The *Acta* records the crowd speaking as a body: *"turba fratrum dicebat: et nos cum ipso decollemur"* (H 41581–41582). It also records the overnight vigil of *"universus populus fratrum"* (H 41513–41516). The absence must be narrowed to "no individual account".
  5. **"the hand of the centurion"** is quoted correctly from Pontius. The *Acta* calls the executioner *spiculator* throughout (H 41588–41589), and Harnack queries "centurion" (reading note row 8). The text should not let the rank stand as fact outside the quotation.
  6. The Formation Ecology centre ("They came. They climbed trees to see", chunk Formation Ecology Connection) mixes an attested fact (the crowd came, H 41583) with a detail only Pontius gives (the trees). The attested and Pontius-only details should be told apart.
- *Fix:* correct these sites in the retelling already ordered, with the independent check against the Latin that the ruling requires.

**P1-4. Process narration and review history remain inside canonical files that CO-LPC-1 edited.**
- *Where:* Doc_09 Disposition `:174–182`. It is a round-by-round account of review history: counts of HIGH findings, `notice_strip.py`, "the reviewer read…", and "three rounds of this document's own escalations were artefacts". Also Doc_09 `:33`, which narrates where correction history went and why. In the chunk, `lpcstory006:63` ("and this note previously denied") is change history inside a field that instructs the Representative. In the records, the body of all seven files has "independently re-located this session…" (for example `records/lpc/story/lpc.story.the-plague-and-the-enemies.md:85` and `lpc.story.the-death-of-cyprian.md:89`).
- *Evidence:* CLAUDE.md, "Keep the live/canonical surfaces clean". `Build/worlds/` and `records/` contain "no notes, commentary, change history, review discussion, or process narration", and "any PR that edits a live or canonical file also removes the commentary already in that file". CO-LPC-1 removed the equivalent lines from Doc_05 and Doc_06 ("Doc_06's Round 2 verdicts and 'nine rounds' line; Doc_05's Round 1 count line", Decision Log, CO-LPC-1 entry). It edited Doc_09 and left Doc_09's equivalent lines standing. `tools/check_live_commentary.py` does not flag these lines, so the gate does not catch this.
- *Fix:* move the review-history narrative of the Disposition into `Review-Artifacts/Doc09_Correction_History.md` or the Decision Log. Keep in the Disposition only the disposition itself, its date and authority, and the escalation-category assessment. Delete "and this note previously denied" from `lpcstory006:63`. Remove the "this session" narration from the record bodies, or reduce it to a provenance line with no session language, in the change that touches the records.

## P2 — minor

**P2-1. The closing line contradicts the document.** `Doc_09_Story_Inventory.md:182` says Doc_09 "has now had seven review rounds", but the Document Log (`:166`) and Disposition (`:174`) record eight. The same line says "Five documents in this world are … awaiting a disposition only the project lead can give", which line 11 contradicts: Docs 04 to 08 were approved on 2026-09-15. *Fix:* correct the count and delete the stale sentence.

**P2-2. §7 item 1 says two things about the gap that pull against each other.** `:120` opens "there cannot be" a story from inside the silence, then says "The silence is a subject-matter gap and a build choice". After the restatement, Doc_02 §7 (`Doc_02:122`) calls it "a genuine silence in the surviving record for this world specifically" on Doc_01's narrower test, and lists gap-era rows (councils, the *Codex Theodosianus*, Optatus) that are not that voice. *Fix:* restate item 1 to Doc_01's test in the words Doc_02 §7 now uses, and drop "a build choice". Also, Registry row 27's "not drawn on for a specific claim in this world's own Doc_01 or Doc_02", which `:120` quotes, is now stale, because Doc_02 §7 cites rows 27, 64 and 300. That row is Doc_02's to fix; Doc_09 should not quote it as current.

**P2-3. §2 says `lpcstory002` carries none of CF's markers, but its own chunk says one is present.** `:43` rejects the Tier 3 reading "for the two stories Pontius reports without CF's markers". `Story-Chunks/lpcstory002_the-plague-and-the-enemies.md:53` says "**Marker one is present.**" Line 45 states the route `lpcstory002` actually takes. *Fix:* reword `:43` to match: one story corroborated outside Pontius's frame, and one whose idealising portrait attaches to the man and not to the events.

**P2-4. A factual slip in `lpcstory002`.** It says the preacher "would himself be executed eight years later" (`Story-Chunks/lpcstory002…:37`; `records/lpc/story/lpc.story.the-plague-and-the-enemies.md:83`). The only date the vendored corpus gives for the plague treatise is ANF's "a.d. 252" (`anf05` 46663), six years before 258, and Doc_08 2A-2 dates the plague only as "c. 249–262". *Fix:* say "a few years later", or "six years later" citing the ANF note as editorial.

**P2-5. A stale ranking.** `:134` ranks the *Acta* "second … behind item 9", but item 9 is CLOSED (`:142`). *Fix:* delete the ranking, or rank only the open items.

**P2-6. A missing full stop.** `:128` reads "the list is a sample, not the full range It is **row 192…**". *Fix:* add the full stop.

**P2-7. The generated index is out of step with its source.** Regenerating `lpc_Story_Index.md` from the current files on a scratch copy (`scripts/gen_story_index.py <copy>`) changes line 89 from "1124 words" to "1125 words". CO-LPC-1's edit of §7 item 5 was not followed by a regeneration. The generator also counts review files named `Doc09_Round*`, so it will not count this file. *Fix:* regenerate after the `lpcstory006` change order, and make the generator count the change-order review file.

---

## Is Doc_09 doing its stage's job?

On the stories themselves, yes. Six of the seven chunks hold at source, sentence by sentence, and §4's No-Tier-5 audit is borne out. §7 answers the required Absent Stories question with real, sourced absences. The tier discipline is disclosed rather than assumed.

The summary layer around the stories has not kept up with the 2026-10-23 rulings. Two source-status claims are now false: the sermons are "unavailable", and the *Acta* is "unread" and a "court record". `lpcstory006` tells a detail the independent witness contradicts. CO-LPC-1 also edited this file without removing the review history it holds. Each fix lies within rulings already made (D1, the `lpcstory006` retelling, CLAUDE.md). This is Doc_09's review under the CO-LPC-1 Cap ruling, so the substantial findings go to the project lead.

VERDICT: Substantial revision required
