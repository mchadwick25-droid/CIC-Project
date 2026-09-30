Simulated review — informational only, not an Article 31 substitute.

# The row-194 exception in the lpc silence claims: independent targeted verification

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-verifier subagent, fresh context, launched from session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** the lpc build-thread worker, commit 81f1eab4d "lpc: add the open row-194 exception ... re-register claims; log OG-50"
- **Round:** 2 (targeted recheck of the F1 fix recorded in ClaimsScopeRecheck_2026-09-30.md; not a document revision round)
- **Truncation check, method 1:** hash and tail comparison. The working tree was clean at the start. For the ten files checked (Doc_01, Doc_02, Doc_05, Doc_08, Source_Registry.md, Open_Gaps_Tracking.md, the core, force and limit records, and the claims register before editing), `git hash-object` equals `git rev-parse HEAD:<path>` (10 of 10), and each file's last 40 bytes end on a complete sentence or table cell. The six vendored files opened (Koch, Monceaux tome 2, Hartel Pars III, Morin, Knopf-Krueger, Harnack) also equal HEAD (6 of 6).
- **Truncation check, method 2:** structural parse. Source_Registry.md parses to 326 numbered rows, 1 to 326, no gap or duplicate, 263 Native. Doc_02 has its ten `## ` headings, from `1. Primary Sources` to `10. Disposition`. The three records parse as YAML front matter (16, 15 and 13 keys), each with a body after the closing `---`. The claims register has 104 rows of 7 columns, before and after this pass's edits.
- **Date:** 2026-09-30
- **Scope:** the eight UNVERIFIED claims (1d15999b, bd7a1c2b, 5ff28070, f9e63052, 0612cfe1, 8960fb57, edcc7675, 12eee5b2); the three re-registered claims (c9013983, 93802ce0, 9fa60830); the new Doc_02 §7 paragraph read whole; a sweep for copies of the silence claim in Build/worlds/lpc and records/lpc. No `packages/lpc` or `cic-poc/frontend` copy exists (grep: none).
- **Severity vocabulary:** P0 blocks, P1 must be fixed but does not disqualify, P2 polish.

## What holds

- **De aleatoribus (row 194).** Hartel III line 4982: `magna nobis ob uniuersam fraternitatem cura est, fideles`. Monceaux (row 207) concludes the author is `un évêque africain de l'école de Cyprien` (line 6655) and calls the piece `une véritable homélie` (line 6671). He fixes no year. He sets it in `l'Afrique du iue siècle` (lines 6493, 6652-6653). The rival hypotheses he reports run to 350 (line 6474). Date and place are not fixed, as the claims say.
- **De singularitate clericorum (row 194).** Hartel III lines 9562-9570: `filii carissimi` ... `ne clerici cum feminis commorentur`. Koch (row 233) writes `Verfaßt ist sie wahrscheinlich gegen Ende des 3. Jahrhunderts` (lines 22909-22910). Koch also reports Blacha's case for Novatian in the 250s (lines 20799-20800) and Harnack's later retreat to `ins 4. Jahrhundert oder noch etwas später` (lines 20842-20844). Monceaux counts it among works `de provenance tout à fait inconnue, mais certainement bien postérieurs au temps de Cyprien` (lines 13883, 13937). The dating range runs from the 250s to after 391, so "date and place not fixed" holds. The earlier finding's statement that every dating falls inside the interval was too strong. The claims do not rely on that statement.
- **Neither work is drawn on.** A grep of Build/worlds/lpc and records/lpc for `aleator` and `singularitate` finds them only in the exception passages, their generators, the gaps log and this register.
- **De duplici martyrio and De Pascha Computus.** Hartel's praefatio: `persecutionum Diocletiani et Maximini (231,26), Caesaris Turcarumque (238,29)` (line 39122) and `nescio annon iure Grauius et alii ipsum libelli subiectorem esse sint suspicati` (lines 39124-39125); `a. a Christo n. 243 editus` (line 39131). Neither is placed in the interval.
- **Row 229.** Morin: `unus (6) Optato Mileuitano episcopo ... baud sine aliqua ueri similitudine alibi adscribitur` (lines 1700-1702); the Orléans codex heads it as a sermon for the Holy Innocents by Optatus (line 10850); Morin adds `forsitan iure` (lines 281-282).
- **Knopf acts 19-22 and 29 (row 231 file, no row of their own).** Maximilianus at Theveste, `Tusco et Anulino consulibus` (line 6456); Marcellus and Cassianus at Tingi under Agricolanus (lines 6556-6565, 6704-6707); Felix, `Diocletiano VIII et Maximiano VII consulibus`, `Felix episcopus`, who answers the curator in his own words (lines 6753-6760 and following); Crispina at Theveste, `Diocletiano nouies et Maximiano <octies> consulibus` (line 7930). All fall inside the interval. Tingi is in Mauretania Tingitana, so "African" is used in the broad sense.
- **Sequence clauses (f9e63052, edcc7675).** Harnack lines 376-381 and 4361, and the Acta consular dates at Knopf lines 4823 and 4857, read as stated. F2 below qualifies what they establish.
- **Rows 202, 264 and 265** were verified in the previous round and are unchanged at HEAD.
- **c9013983, 93802ce0 and 9fa60830** hold (verdicts below).

## Finding F1 (P1): the exception undercounts the row-194 works

**Defect.** Every bishop-voice claim now reads "with one open exception: two short pseudo-Cyprianic works in row 194". Row 194 (and row 6, in English) also holds two more works written as a bishop's own pastoral letters to his people. The vendored scholarship leaves their date and place just as open, and one Native source places them inside the interval:

- *De bono pudicitiae* (Hartel III lines 702-712): the author speaks of his `cotidianis euangeliorum tractatibus` and asks what better befits `officiis episcopi` than teaching the faithful. That is a bishop's ordinary preaching voice.
- *De spectaculis* (Hartel III lines 155-160): headed `CYPRIANVS PLEBI IN EVANGELIO STANTI S.`, an absent bishop writing to his flock.
- Monceaux (row 207) reads both as one frame, `une lettre adressée par un évêque absent aux fidèles de sa communauté` (lines 6166-6170). He calls them a forgery `de peu postérieure à la mort de l'évêque de Carthage`, from third-century Africa, `écrits probablement par un clerc de l'école de Cyprien` (lines 6399-6405). The Registry's row 6 note says two of these pieces are "widely attributed to Novatian", which would make them Roman and earlier than 258. Koch warns against treating the Novatian ascription as `res iudicata` (lines 22901-22904).

On Monceaux's reading, *De bono pudicitiae* is closer to "a bishop's ordinary pastoral voice that continues Cyprian's" than either named work. On the Novatian reading, it falls outside the interval. So its status is exactly as open as *De aleatoribus*'s. Doc_02 §7 now says "the pseudo-Cyprianic works are not set aside on a ground of date, because the vendored files do not settle their dates". It then disposes only of *De Pascha*, *De duplici martyrio* and the two named works. The others in rows 6 and 194 are left with no stated ground.

The same holds, more weakly, for the short spurious letter `CYPRIANVS PLEBI CARTAGINI CONSISTENTI` (Hartel III lines 15508-15520). It speaks of `traditoribus`, which points after 303, and Hartel's praefatio gives it no date (lines 39159-39170). The other works set out in Monceaux's list are placed outside the interval by the vendored files: *Ad Novatianum* in 253 and *De rebaptismate* in 256 (Monceaux lines 13950-13952, 5105-5111), and *Ad Vigilium* in the Vandal period (lines 13875-13882). They need no exception, but Doc_02 should say so rather than leave them unaddressed.

**Affected:** 1d15999b, bd7a1c2b, 5ff28070, f9e63052, 0612cfe1, 8960fb57, edcc7675, 12eee5b2. All stay UNVERIFIED and Contested.

**Proposed wording** (not applied; a reworded claim takes a new id and must be re-registered). Replace the count with the works and their grounds:

- Claim form (Doc_02 §7, Doc_05 §0.3, Doc_08 lines 23 and 264, limit, core and force records): "... that continues Cyprian's, with open exceptions among the pseudo-Cyprianic works of rows 6 and 194, whose date and place the vendored files do not fix: *De aleatoribus*, a bishop's homily, which Monceaux (row 207) gives to an African bishop of Cyprian's school; *De singularitate clericorum*, a bishop's letter to his clergy, which Koch (row 233) dates probably toward the end of the third century; and *De spectaculis* and *De bono pudicitiae*, written as an absent bishop's letters to his people, which the Registry's row 6 note gives to Novatian and Monceaux gives to a cleric of Cyprian's school writing shortly after his death. None is assessed, and none is drawn on for a claim."
- Doc_05 line 293 and table line 299: "... apart from four unassessed pseudo-Cyprianic works of unfixed date (rows 6 and 194) ...".
- Force description (8960fb57), plain register: "... Four short works handed down under Cyprian's name may come from those years: a bishop's sermon against gambling, a bishop's letter to his clergy, and two letters written as from an absent bishop to his people, on the public shows and on chastity. We have not weighed them."
- Doc_02 §7, after the *De duplici martyrio* sentence, one sentence on the rest: "The vendored scholarship places *Ad Novatianum* (253) and *De rebaptismate* (256) before the interval and *Ad Vigilium* after it (Monceaux, lines 13875-13882, 13950-13952); the short letter to the people of Carthage on traditors (Hartel III, line 15508) is undated."

Whether to count *De spectaculis* and *De bono pudicitiae* at all, given the Novatian ascription, is a reading. It belongs with the boundary decision OG-50 already routes to the build thread and the project lead. Until that decision, the claims cannot state that exactly two works are open.

## Finding F2 (P1): the date of Pontius's Life is stated as settled

**Defect.** Doc_02 §7, Doc_05 §0.3, Doc_08 lines 23 and 264, Doc_09 lines 23 and 120, the Precedent (line 21) and the three records say the interval begins with "the texts written at and just after Cyprian's martyrdom", and Pontius's *Life* is one of them. Claims f9e63052 and edcc7675 carry this in their own sentences. Doc_02 §7 reports Harnack correctly: `das Jahr 259 als Jahr der Abfassung` and `(dies ist auch die herrschende Ansicht)` (Harnack lines 380-381). But Koch (row 233, Native, vendored) holds the opposite. He writes that Reitzenstein and Martin have `aufs schwerste erschüttert, m. E. sogar ... tödlich getroffen` the view that the author was Cyprian's contemporary. His author is `ein frühestens am Ende des 3. Jahrhunderts lebender Schriftsteller, der den Augen- und Ohrenzeugen spielt` (lines 4405-4412), and he repeats the view at lines 15497-15499. No lpc file discloses this. The dating is Contested inside the corpus, and the claims present it as settled.

On either date, the *Life* is a biography of Cyprian, not a bishop's pastoral voice to his flock. So F2 does not reopen the silence itself. It changes the start-point clause.

**Proposed wording** (Doc_02 §7, item (2)): "(2) Pontius's *Life* (rows 7, 40, 194 and 205). Harnack (row 205, lines 380–381) dates it to 259 as the prevailing view in 1913. Koch (row 233, lines 4405–4412) follows Reitzenstein and Martin in placing its author at the end of the third century at the earliest, writing as if an eyewitness. On either date it is a life of Cyprian, not a bishop's voice to his own flock, and it does not fill the silence." Then change "texts written at and just after his martyrdom" to "texts written at or after his martyrdom and about it", or name the dispute where the phrase recurs. Record the dating as Contested in Doc_02 §8.

## The new Doc_02 §7 paragraph read whole: smaller points (P2)

1. **Koch's own view is left out.** The sentence on *De singularitate* reports that Morin and Harnack ascribe it to Macrobius. It does not say that Koch rejects the ascription. He endorses Schanz's verdict that it fails on `unüberwindlichen Hindernissen` (lines 22876-22878), and he judges that the author was not a schismatic bishop (lines 22907-22908). "He also reports that Achelis ... and leaves open a Donatist origin" also has an unclear subject: the words are Achelis's, not Koch's. Proposed: "Koch reports that Achelis placed it before Nicaea while leaving a Donatist origin open, and that Morin and Harnack ascribed it to Macrobius, a priest and later Donatist bishop at Rome; Koch himself rejects the Macrobius ascription and thinks the author was not a schismatic bishop (lines 20766–20790, 22876–22910)."
2. **"Names no date" is too strong for Monceaux on *De aleatoribus*.** He sets it in third-century Africa (lines 6493, 6652-6653). Proposed: "places it in third-century Africa and names no year".
3. **The Latin idiom in the Hartel sentence.** Hartel's `nescio annon iure ... sint suspicati` (line 39124) follows his remark that the signs of forgery are too plain for Erasmus to have missed. It leans toward the suspicion that Erasmus produced the text. It is not a plain statement that he does not know. Proposed: "and inclines to the suspicion of Gravius and others that Erasmus himself produced it".
4. **Row 229.** "Morin gives one of them ... to Optatus" makes Morin the one who assigns the sermon. In fact the manuscript does (`alibi adscribitur`; the Orléans codex, line 10850), and Morin judges the ascription not unlikely. The records already say this correctly. Proposed: "a manuscript gives one of them, a sermon on the Holy Innocents, to Optatus, and Morin judges this `haud sine aliqua ueri similitudine`".
5. **Registry cells are out of step with use.** The paragraph now rests statements on rows 207 and 233 (both "Not currently licensed for any specific claim", Confidence C) and on the spuria in row 194, whose Licensed-For cell covers only the Vita and the Acta. These are disclosures, not positive claims. The Registry should still say that the rows are cited for the row-194 exception, and apply its own priority-review rule to them.

## Sweep: copies of the silence claim not qualified by the exception

Checked by grep for `silen`, `133`, `century gap`, `continues Cyprian`, `carries on Cyprian`, `just after` and `one open exception` across Build/worlds/lpc (Doc_01 to Doc_09, World Profile, Capsule Core, Step 0, Precedent, Registry, indexes, Representative phases and prompt, chunks, context files) and records/lpc. No copy exists in `packages/` or `cic-poc/frontend/`.

**Qualified (carry the exception):** Doc_02 §7; Doc_05 §0.3, line 293, table line 299; Doc_08 lines 23 and 264; the limit record's why_sources_cannot_answer; the core record's cautions item 2; the force record's description and manifestations. The core record's keyword note (lines 414-419) says "none of the assessed ones continues Cyprian's voice". That is consistent, because the row-194 works are unassessed.

**Contradicted by the exception (a bishop's pastoral voice, or congregational subject matter, stated as wholly absent):**

- `lpc_Gapped_Formation_Precedent.md` line 21: "no surviving voice in the Registry, native to this world's own boundary, that continues Cyprian's". This is unqualified. OG-50 says the Precedent was "received from the project lead" and left as it stands. It is still the plainest unqualified copy, and the project lead should decide.
- `Doc_01` line 110: "What is genuinely missing is a surviving voice, continuous with Cyprian's own ordinary-pastoral mode, from within this world's own boundary, for roughly 133 years." Doc_01 is the binding that Doc_02 §7 discharges. A pointer would do: "(Doc_02 §7 records open exceptions among the pseudo-Cyprianic works of rows 6 and 194)".
- `Doc_09` line 120: "What the gap lacks is not documents but this world's own congregational subject-matter". `lpc_World_Profile.md` line 26 has the same point: "what the gap lacks is this world's own congregational subject matter, not documents". *De aleatoribus* (gambling among the faithful) and *De bono pudicitiae* (chastity, preached to the flock) are congregational subject matter, and they may fall inside the gap. Proposed for both: "... what the gap lacks, apart from a few unassessed pseudo-Cyprianic works of unfixed date (Doc_02 §7), is this world's own congregational subject matter ...".

**General silence statements left unqualified (P2; they hold on the congregation's-own-voice reading, and should be revisited when OG-50 is decided):** Doc_05 line 305; Doc_07 lines 176 and 232; Doc_08 line 359; Doc_09 line 23 and its Story Index line 93 (stories, and neither work narrates); World Profile lines 428 and 650-654; Capsule Core line 79; Permanent Prompt line 21; Rep Phase 1 line 82; Phase 2 line 31; Phase 3 line 55; Phase 4 line 28; Phase 6 line 39; Phase 7 lines 52 and 68; core record horizon (lines 90-92) and thinness (lines 240-243); the limit record's statement. The spoken copies (Permanent Prompt line 21, Capsule Core line 79, the limit record's statement) speak of "our own congregational voice". They should not take on scholarly exception language, which would be meta-commentary. But if OG-50 places any of these works inside the interval, those spoken lines must change.

**F2 copies (the "at and just after" dating):** Doc_02 §7; Doc_05 §0.3; Doc_08 lines 23 and 264; Doc_09 lines 23 and 120; Precedent line 21; limit, core and force records; generators `scripts/wb_lpc_s21.py`, `wb_lpc_s25.py`, `wb_lpc_s28.py`.

## Per-claim verdicts

| id | verdict | status set |
|---|---|---|
| 1d15999b | Named works described correctly; exception undercounts (F1) | UNVERIFIED, Contested |
| bd7a1c2b | Same as 1d15999b (F1) | UNVERIFIED, Contested |
| 5ff28070 | "two unassessed works" undercounts (F1) | UNVERIFIED, Contested |
| f9e63052 | Sequence clauses hold as reported; F1; Pontius dating contested (F2) | UNVERIFIED, Contested |
| 0612cfe1 | The count sits in the next sentences, which name two works (F1) | UNVERIFIED, Contested |
| 8960fb57 | The "can date" hedge does not cure F1: Monceaux dates two more works just after 258 | UNVERIFIED, Contested |
| edcc7675 | Named items all check; F1; F2 | UNVERIFIED, Contested |
| 12eee5b2 | Same as 1d15999b (F1) | UNVERIFIED, Contested |
| c9013983 | Holds: row 37 names no inscription and was not re-checked | VERIFIED, Documented |
| 93802ce0 | Holds: both quotations verbatim in the Selection method paragraph; no "orthogonality" there | VERIFIED, Documented |
| 9fa60830 | Holds: §6's named sources are at source; the reception clause is a reading | JUDGEMENT, Widely Accepted |

## Gates

- `python -m engine.m10.cli claims lpc`, after this pass's register edits: PASS (104 derived, 104 registered, 8 UNVERIFIED).
- `python -m engine.m10.cli reviewfile` on this file: PASS.
- Only `lpc_Claims_Register.md` (source, check, status and confidence cells of the eleven rows) and this file were written. Nothing was committed.
