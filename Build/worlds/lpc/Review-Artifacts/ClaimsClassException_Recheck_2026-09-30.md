Simulated review — informational only, not an Article 31 substitute.

# The class-level exception in the lpc silence claims: independent targeted recheck

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-verifier subagent, fresh context, launched from session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** the lpc build-thread worker, commit b340a2d3d "lpc: state the row 6 and 194 pseudo-Cyprianic exception as a class, date Pontius's Life as disputed ... log OG-51"
- **Round:** 3 (targeted recheck of F1 and F2 in ClaimsException194_Verification_2026-09-30.md, carried out as OG-51's change order; not a document revision round)
- **Truncation check, method 1:** hash and tail comparison. The working tree was clean at the start. For the thirteen build files read (Doc_01, Doc_02, Doc_05, Doc_08, Doc_09, Source_Registry.md, Open_Gaps_Tracking.md, lpc_World_Profile.md, both claims registers before editing, and the force, limit and core records), `git hash-object` equals `git rev-parse HEAD:<path>` (13 of 13), and each file's last 40 bytes end on a complete sentence, table cell or record note. The ten vendored files opened (Hartel Pars III, Monceaux tomes 2 and 3, Koch 1926, Harnack, Morin, Gebhardt, Knopf-Krueger, Petschenig's anti-Donatist volume, NPNF108) also equal HEAD (10 of 10).
- **Truncation check, method 2:** structural parse. Source_Registry.md parses to 326 numbered rows, 1 to 326, with no gap or duplicate. Doc_02 has its ten `## ` headings, from `1. Primary Sources` to `10. Disposition`. The force, limit and core records parse as YAML front matter (15, 13 and 16 keys), each with a body after the closing `---`. The lpc claims register has 105 rows, all of 7 cells, before and after this pass's edits. The Doc_09 register has 142 rows before and after.
- **Date:** 2026-09-30
- **Scope:** the nine UNVERIFIED rows of lpc_Claims_Register.md (e92358e4, 72c692a3, f2712e45, b1c7f1d5, fea87e6e, dc7b8b34, 5992ae73, fb07c9ad, 02f75b9a); the three re-registered rows of Doc09_Claims_Register.md (2572f600, a3aeea2f, 1d7336df); four questions put by the build thread: (a) whether the class covers every Native-row work that could be a bishop's or congregation's voice in 259-391; (b) every line and quotation cited in Doc_02 §7's explanatory paragraph; (c) the Pontius dating wording across Docs 02, 05, 08 and 09, the records and the generators; (d) the new plain-voice record sentences and their readability.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but does not disqualify, P2 polish or disclosure.

## (a) Does the class cover every candidate?

**Inside rows 6 and 194 the class is closed.** Hartel's Pars III holds, by its headings: De spectaculis (line 155), De bono pudicitiae (702), De laude martyrii (1461), Ad Novatianum (3022), De rebaptismate (3893), De aleatoribus (4979), De montibus Sina et Sion (5666), Ad Vigilium (6522), Orationes I and II (7934, 8039), De duodecim abusivis (8395), De singularitate clericorum (9559), De duplici martyrio (11963), De Pascha Computus (13237), four letters (15465 to 15580) and the Carmina (16106 to 17527). Row 6 adds the English Exhortation to Repentance. Each work is either placed outside 258-391 by a vendored file or falls in the class:

- Outside: De Pascha Computus, 243 (Hartel, line 39131); Ad Novatianum, autumn 253 (Monceaux, lines 5111-5112); De rebaptismate, 256 (lines 13951-13952); Ad Vigilium, the Vandal period (lines 13882-13883).
- In the class, date and place not fixed: De aleatoribus; De singularitate; De spectaculis; De bono pudicitiae; the letter to the plebs of Carthage; De laude martyrii; De montibus and Adversus Iudaeos (Monceaux, lines 13875-13882: "probablement des traductions du grec", fixing neither date nor place); the Orationes; the Carmina; the Exhortatio (Monceaux, lines 13948-13949: clerics of Cyprian's circle or school).

A work cannot fall between the two, so the class wording cannot be undercounted again.

**Outside rows 6 and 194, no Native-row work was found that supplies such a voice in the interval.** Checked:

- Row 8 (the English Ad Novatianum and De rebaptismate) is pseudo-Cyprianic but dated 253 and 256.
- Rows 39, 205 and 207 are the standing Hartel reference and two studies; they add no text of their own beyond rows 191 and 194.
- Koch (row 233) treats Quod idola as Cyprian's own (chapter title, line 326: `Quod idola dii non sint: ein Werk Cyprians`). His other chapters are on works already in row 194.
- Monceaux tome 3 (row 208, Native, secondary) describes the fourth-century African material. Its primary texts are in other files, dealt with below.
- Knopf nos. 19-22 and 29 and Morin's nine further tractatus lie in Native-row files but have no row. Doc_02 discloses both.
- **Gebhardt (row 232) also prints no. XX, the Gesta apud Zenophilum, and no. XXI, the Acta purgationis Felicis** (contents, lines 464-466; the Cirta cries at lines 9856 and 9863). Row 232 is scoped to the three Cyprianic acts, so these have no row. Doc_02 §7 speaks of the Gesta only as row 265, and row 232's cell does not mention them, unlike row 231's cell. See P2-1.
- Augustine's Native anti-Donatist works report or quote interval documents. The Breviculus (row 268) reports the letter of Mensurius, bishop of Carthage, to Secundus (Petschenig, lines 64671-64737). Contra Cresconium (row 216) quotes the Cirta protocol, `Secundus dixit` (line 47550). Both fall under Doc_02's sentence on "the documents of the Donatist dispute". Mensurius comes to us in Augustine's indirect speech and writes to a bishop, not to his flock. See P2-2.
- Rows 227 (Migne's dubii) and 230 (Caillau) hold sermons whose authorship is not settled. A search of both files found no ascription to Optatus or to any other African bishop before 391.

The claims hold on the reading "a bishop's ordinary pastoral voice to his own flock" and on the Registry's scoping of rows.

## (b) Doc_02 §7 explanatory paragraph: cited lines and quotations

All checked at source. Each quotation is verbatim, allowing for the OCR forms that Doc_02 discloses:

- Hartel III: line 158 `CYPKIANVS PLEBI IN EVANGELIO STANTI S.`; line 4982 `magna nobis ob uniuersam fraternitatem cura est, fideles`; line 9562 `filii carissimi`; line 15508 `CYPEIANVS PLEBI CAETAGINI`; line 15517 `traditoribus`; lines 39121-39125, with `nescio annon iure Grauius et alii ipsum libelli subiectorem esse sint suspicati`; line 39131 (243); lines 39159-39170, where the praefatio treats the third letter by manuscript only and gives no date.
- Monceaux tome 2: lines 6168-6169 `une lettre adressée par un évêque absent aux fidèles de sa communauté`; lines 6399-6404, "de peu postérieure à la mort de l'évêque de Carthage" and `écrits probablement par un clerc de l'école de Cyprien`; line 6655 `un évêque africain de l'école de Cyprien`; line 6671 `une véritable homélie`; lines 6493 and 6652-6653, third-century Africa.
- Koch: lines 22901-22903 (`novatianischen`, `res iudicata`); lines 22876-22878 and 22907-22909; lines 20766-20790 (Morin, Achelis, Harnack); lines 4405-4414 and 15497-15499, with the Pontius quotation verbatim across the line breaks.
- Harnack: lines 376-381 and 4361.
- Morin: lines 281-282 `forsitan iure`; lines 1701-1702, where the file reads `baud`; lines 10848-10850, the Orléans (Aurelianensis 154) heading. "A different manuscript ... and Morin judges" is now correct.

Three small citation points:

1. `officiis episcopi` runs over lines 711-713 of Hartel III. The citation gives "lines 702–712". Proposed: "lines 702–713".
2. Monceaux's "de 253" for Ad Novatianum is on line 5112. The citation gives "5105–5111". Proposed: "5105–5112".
3. Koch writes `‚novatianischen‘` in quotation marks, signalling "so-called". "Koch calls ... the `novatianischen` writings" is a shade strong. Proposed: "Koch refers to ... as the 'Novatianic' writings, in his own quotation marks, and warns ...".

None of these changes a claim.

## (c) Pontius dating wording

The wording is consistent across Doc_02 §7 and §8 (Contested), Doc_05 §0.3, Doc_08 (the structural-fact paragraph and Layer 1), Doc_09 (line 23 and §7 item 1), the three records, and the generators `wb_lpc_s21.py` (lines 4395 and 4519), `wb_lpc_s25.py` (lines 1554, 1601 and 1619) and `wb_lpc_s28.py` (line 889). "Dated to 259 or much later" is a fair plain gloss of Harnack's 259 against Koch's "frühestens am Ende des 3. Jahrhunderts".

**F1 (P1): the ascription to the deacon is stated as settled beside the date that denies it.** The force description reads: "The life written by his deacon Pontius stands beside them. Scholars date it to 259, or to the end of the third century at the earliest." The core record's cautions item 2 reads: "The life written by his deacon Pontius is dated to 259 or much later." Koch's later date is an authorship claim. His author is "kein Zeit- und Lebensgenosse" of Cyprian but a writer "der den Augen- und Ohrenzeugen spielt" (lines 4410-4414). Hartel heads the work `Pontio diacono uulgo adscripta` (row 194, line 40260; the file's OCR reads `iiiilgo`). Putting both sentences side by side presents a disputed ascription as settled. The records must not be edited in this pass, so the wording is proposed here:

- Force description: "The life of him that bears the name of his deacon Pontius stands beside them. Scholars date it to 259, or to the end of the third century at the earliest."
- Core cautions item 2: "The life that bears the name of his deacon Pontius is dated to 259 or much later."
- The same change in the generators that emit these fields (`wb_lpc_s25.py` line 1554 and `wb_lpc_s21.py` line 4395), then a package rebuild.

Other places attribute the Life to "our own deacon Pontius" without giving its date: `lpc.story.election-of-cyprian` (text), `lpcstory006` line 15, and the `wb_lpc_s24.py` generator. In an emic voice this can stand as the tradition's own memory, as Jerome's notice does. The build thread should decide whether those places also take "that bears his name". This is not decided here.

**Residual (P2-3).** `lpc_Gapped_Formation_Precedent.md` line 21 still reads "between the texts written at and just after his martyrdom (the *Acta Cypriani*, Pontius's *Life* and two martyr acts ...)". OG-51 routes this line to the project lead for its silence sentence only. The dating copy should be named in the same routing.

## (d) The new plain-voice sentences

"Some short works handed down under Cyprian's name may come from those years" (core cautions), and "apart from some short works handed down under his name that may come from those years. We have not weighed them" (force description, claim 5992ae73). These are true, and they invent nothing: the works are in the Native rows, transmitted under Cyprian's name, short, not dated by the vendored files, and not assessed. "Our own texts" correctly renders the Native rows.

Readability, using the record gate's own scorer (`engine.m1.gates.grade_text`, called by `engine/m7/turn_readability.py`): the whole force description scores FK 7.5 and FRE 66.9. At HEAD~1 it scored FK 7.6 and FRE 65.9. The sentence alone scores FK 6.7. That is below the floor of 8, which is report-only and never fails. The pass lowered the grade by 0.14. The floor guards against flattening the world's voice, and these sentences are plain but not flattened. **No fix is clearly needed.** If F1 is applied, "that bears the name of" adds a little length. No further change is recommended.

## The three Doc_09 claims

- **2572f600 and a3aeea2f.** The changed clause holds: the Acta and martyr acts belong to Cyprian's phase, and Pontius is dated to 259 or much later. The main clauses rest on a reading. "This world tells itself no stories at all" between 258 and 391, and "none comes from the silence ... and none can", both hold if "story" means storytelling that begins inside the interval. §6 item 1 uses that reading when it says that Augustine's use of Perpetua would be a Phase Two story.
- **P2-4.** Augustine narrates a martyr from inside the interval: Crispina of Theveste, 304 (Knopf no. 29, `Diocletiano nouies et Maximiano <octies> consulibus`, line 7930). He does so in two feast-day sermons in the Native row 20: NPNF108 Psalm CXXI, headed "A sermon to the people on the day of St. Crispina" (endnote ii.CXXI-p2), and Psalm CXXXVIII (ii.CXXXVIII-p8: "She rejoiced when she was being seized ..."). The Latin is in row 201's file (line 114389, `in natali S. Crispinx martyris`, the OCR for `Crispinae`). No lpc file mentions Crispina. A reader who takes "tells itself no stories at all" to mean no story set in those years would find it refuted. Proposed disclosure after the §7 item 1 sentence: "Augustine does preach one martyr of those years, Crispina of Theveste (304), on her feast (row 20, the Expositions on Psalms 121 and 138); like his sermons on Perpetua (§6 item 1), that is a Phase Two telling, and it is not built here."
- **1d7336df.** The unchanged text is as verified on 2026-09-16. The new pointer is accurate, and it is needed, since De aleatoribus and De bono pudicitiae carry congregational subject matter.

## Disclosure points (P2, no claim is false)

- **P2-1.** Doc_02 §7, after the Knopf sentence: "Gebhardt's volume (the row 232 file) also prints the *Gesta apud Zenophilum* and the *Acta purgationis Felicis* (nos. XX and XXI), which have no row; the *Gesta* is the text row 265 holds as Excluded." Row 232's cell should say the same, as row 231's does.
- **P2-2.** Doc_02 §7 could name the nearest case under "documents of the Donatist dispute": Mensurius's letter to Secundus, known only through Augustine's report of its reading in 411 (row 268, Breviculus III 13, 25). It is a bishop's letter to a bishop, reported in Augustine's words, so it does not fill the silence.
- **P2-3** and **P2-4** as above.

## Per-claim verdicts

| id | verdict | status set |
|---|---|---|
| e92358e4 | Class closed over rows 6 and 194; no other Native-row candidate found; holds on the stated reading | JUDGEMENT, Widely Accepted |
| 72c692a3 | None assessed or drawn on (grep); OG-51 records the boundary decision | VERIFIED, Documented |
| f2712e45 | As e92358e4 | JUDGEMENT, Widely Accepted |
| b1c7f1d5 | Short form matches the class | JUDGEMENT, Widely Accepted |
| fea87e6e | Pontius dating and sequence clauses at source; class as e92358e4 | JUDGEMENT, Widely Accepted |
| dc7b8b34 | "With open exceptions", completed by the next sentences, matches the class; neighbouring F1 | JUDGEMENT, Widely Accepted |
| 5992ae73 | True plain-voice form; FK 7.5, report-only; neighbouring F1 | JUDGEMENT, Widely Accepted |
| fb07c9ad | Row statuses, Gesta, Morin and Pontius at source; class as e92358e4 | JUDGEMENT, Widely Accepted |
| 02f75b9a | As e92358e4 | JUDGEMENT, Widely Accepted |
| 2572f600 | Changed clause holds; main clause on the origin reading; P2-4 | JUDGEMENT |
| a3aeea2f | As 2572f600 | JUDGEMENT |
| 1d7336df | Unchanged text verified 2026-09-16; pointer accurate | VERIFIED |

F1 is a P1 defect in record sentences next to two claims, not in a claim. It needs the build thread's fix and an independent re-confirmation. It is not self-certifiable.

## Gates

- `python -m engine.m10.cli claims lpc`, after this pass's register edits: PASS (105 derived, 105 registered, 0 UNVERIFIED). A first run failed on five `evidence-unresolved` findings, because the source cells named records by file path. They now name records by id, as the other rows do, and the gate passes.
- `python Build/worlds/lpc/scripts/check_claims.py` (the Doc_09 register's own checker): exit 1 before and after this pass, on the same 19 unregistered Doc_09 and story-chunk claims that OG-51 already records. This pass registers nothing and removes nothing.
- `python -m engine.m10.cli reviewfile` on this file: PASS.
- Only `lpc_Claims_Register.md` and `Doc09_Claims_Register.md` (status, confidence, source and check cells of the twelve rows) and this file were written. Nothing was committed.
