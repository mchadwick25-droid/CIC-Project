Simulated review — informational only, not an Article 31 substitute.

# The ten Native-row silence claims: independent targeted recheck (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-verifier subagent, fresh context, launched from session_01EgyL7xtErqj72CaFiEUx4q (wrote none of the text under review)
- **Drafter agent:** the lpc build-thread worker, commit 262773c06 "lpc: scope the silence claims to the Registry's Native rows"
- **Round:** 1 (targeted recheck of ten re-registered claims; not a document revision round)
- **Truncation check, method 1:** hash and tail comparison. For the seven claim-bearing files not edited since HEAD (Doc_05, Doc_08, lpc_World_Profile.md, lpc_Rep_Phase1_Ecology_Assessment.md, and the limit, force and world core records), `git hash-object` equals `git rev-parse HEAD:<path>` (7 of 7). Doc_02 and Source_Registry.md differ from HEAD by another thread's uncommitted quotation-mark edits; the word diff touches no Boundary Status cell and no claim sentence. Every file's last 40 bytes end on a complete sentence.
- **Truncation check, method 2:** structural parse. Source_Registry.md parses to 326 numbered rows, 1 to 326, no gap or duplicate (263 Native, 63 Excluded). Doc_02 has its ten `## ` headings, ending at `## 10. Disposition`. The three records parse as YAML front matter (13, 15 and 16 keys), each with a body after the closing `---`. The claims register has 104 rows, every one of 7 columns.
- **Date:** 2026-09-30
- **Scope:** the ten claims whose check cell read "re-verification pending after the Native-row scope change" (9fc4235e, c7e95bf2, 568ce991, 31c29bec, bc8f815c, 47d348b0, ab5908db, 7bf15a21, caf67658, 004afcf9); every Registry row; the vendored files by structure marker.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but does not disqualify, P2 polish.

## Method

1. Parsed all 326 Registry rows and listed every Native row that is not secondary scholarship. Checked each against the interval 259 to 391.
2. Opened the vendored files for the rows in doubt, by structure marker: Optatus (rows 27, 64, 264), the appendix (row 265), Bruns (row 202), Morin (row 229), Knopf and Gebhardt (rows 231, 232), Confessions (row 9), the Theodosian Code (rows 44, 88), Hartel's Opera Spuria (row 194), and the scholarship on the pseudo-Cyprianic works that the Registry vendors (rows 207, 233).
3. Read each claim in its own file and context.

## What holds

- **Optatus (rows 27, 64, 264, Native).** The only Cyprian mentions are the chair, `cathedra Petri uel Cypriani` (row 264 file, line 561), and the list of earlier bishops at the Carthage altar (line 988). A search for `clamau-`, `acclam-` and `populus` finds no quoted congregational speech. Dates in the file headers: `fl. 366-385` (row 264) and `c. 366-393` (row 27).
- **Row 265 (Excluded, Named Comparandum).** The Cirta cries are there: `respondit populus: alius fiat` (appendix lines 484-485), `ciuem nostrum uolumus, ille traditor est` (line 490), `non illi communicauimus` (line 573). The consular formula names Constantine (line 129). The claims describe it correctly as outside the Native rows.
- **Row 202 (Bruns).** The Gratus minutes are spoken by bishops: `Absit, absit` (lines 7927-7928), `tamen et ego unus ex vobis` (line 7942), `tractatu assiduo et commonitione frequenti` (line 8008). The Genethlius council heading and variants sit at lines 8267-8273 and 8316-8317. An act of assembled bishops, as the claims say.
- **Row 229 (Morin).** The nine tractatus have no row and no Boundary Status. Morin gives one of them, a sermon on the Holy Innocents, to Optatus `haud sine aliqua ueri similitudine` (line 1701; `forsitan iure`, line 281; heading, line 10850). ab5908db and the records report this correctly.
- **Rows 231 and 232.** The three Cyprianic acts are Native. The row-231 file also holds African acts dated inside the interval, nos. 19-22 and 29 (Maximilianus, Marcellus, Cassianus, Felix, Crispina; lines 6454, 6556, 6704, 6753, 7928). These have no row, so they sit outside the Native-row scope.
- **Confessions III.12 (row 9).** A bishop answers Monica in direct speech: "it is not possible that the son of these tears should perish" (npnf101, `vi.III.XII-p2`). The text is written after 391 and reports the words through Monica and Augustine. The limit record's sentences after caf67658 name it as seen through Augustine's eyes. The text names no see for the bishop.
- **Theodosian Code.** `XVI,  2,  4  (321  lul.  3).` at line 83906 of the Mommsen-Meyer file. It is imperial law, not a church voice.

## Finding F1 (P1): the bishop-voice claims overreach on row 194

**Defect.** Row 194 (Hartel, CSEL 3 Pars III, Opera Spuria) is Native. It holds two pseudo-Cyprianic works that speak in a bishop's own pastoral voice:

- *De singularitate clericorum*. A bishop writes to his clergy (`filii carissimi`) and orders `ne clerici cum feminis commorentur` (Hartel III, lines 9562-9570). Cyprian dealt with the same problem. Koch (row 233, Native, vendored) dates it: `Verfaßt ist sie wahrscheinlich gegen Ende des 3. Jahrhunderts` (koch_cyprianische-untersuchungen-deu_1926.txt, line 22909). Koch also reports Achelis's pre-Nicene date and the Morin-Harnack ascription to Macrobius (lines 20766-20790). Every dating in the file falls inside the interval. Its place of origin is not settled.
- *De aleatoribus*. A bishop's homily to the faithful: `magna nobis ob uniuersam fraternitatem cura est, fideles` (Hartel III, line 4982). Monceaux (row 207, Native, vendored) calls it `une véritable homélie` (tome 2, line 6671). He gives it to `un évêque africain de l'école de Cyprien` (line 6655), in the third century, with no fixed date. The hypotheses he reports run to 350 (line 6474). Koch finds it full of Cyprian's phrasing (line 3119).

Doc_02 §7 sets rows 6 and 194 aside "because no vendored file places them inside the interval". That ground is false for *De singularitate clericorum*. It is open for *De aleatoribus*. The earlier SilenceClaim_Ruling_Verification_2026-09-30.md searched only Hartel's praefatio. It did not open the vendored scholarship.

The eight claims that deny a bishop's voice say, without qualification, that no source in the Native rows supplies one. That states as settled an absence which turns on two unassessed Native texts of disputed date. Whether either text "continues Cyprian's" voice is a reading, and it may go either way. *De singularitate* may be Roman or Donatist; *De aleatoribus* may date from before 258. But the claims cannot rest on a dating ground that the vendored files contradict.

**Affected:** 9fc4235e, c7e95bf2, 568ce991, 31c29bec, bc8f815c, 47d348b0, ab5908db, 7bf15a21.
**Not affected:** caf67658 and 004afcf9. They concern a congregation's own voice, and both works speak as bishops.

**Proposed wording** (not applied; a reworded claim takes a new id and must be re-registered):

- Doc_02 §7 (9fc4235e), and the same qualifier at Doc_05 §0.3 (c7e95bf2), Doc_08 line 264 (31c29bec), the limit record (7bf15a21), the core record (bc8f815c) and the force manifestations (ab5908db): "... no source in the Registry's Native rows supplies a bishop's ordinary pastoral or congregational voice, or a congregation's voice, that continues Cyprian's, with one open exception: two pseudo-Cyprianic works in row 194 whose date and place are not fixed. *De aleatoribus* is a bishop's homily to his people, which Monceaux (row 207) gives to an African bishop of Cyprian's school. *De singularitate clericorum* is a bishop's letter to his clergy, which Koch (row 233) dates probably to the late third century. Neither is assessed, and neither is drawn on for a claim."
- Doc_02 §7's set-aside sentence should be replaced. It should say what Koch and Monceaux report, not that no vendored file places these works in the interval.
- Doc_05 line 293 (568ce991): "... an interval in which no source in the Registry's Native rows continues Cyprian's pastoral or congregational voice, apart from two unassessed pseudo-Cyprianic works of unfixed date (row 194), and the construction says so at every level."
- Force description (47d348b0), in its own plain register: "After them, until Augustine, none of the texts we hold as our own and can date to those years carries on Cyprian's voice. Two short works handed down under Cyprian's name may come from those years: a bishop's sermon against gambling and a bishop's letter to his clergy. We have not weighed them." This also gives the sentence its missing end point. On its own, "After them, none ..." has none; the context supplies it.

One decision belongs to the build thread or the project lead: whether to assess these two works and settle their Boundary Status. Placing a text of unsettled provenance inside or outside a world is a boundary question.

## Per-claim verdicts

| id | verdict | status set |
|---|---|---|
| 9fc4235e | Overreaches (F1); the rest holds | UNVERIFIED, Contested |
| c7e95bf2 | Overreaches (F1); the rest holds | UNVERIFIED, Contested |
| 568ce991 | Overreaches (F1); the rest holds | UNVERIFIED, Contested |
| 31c29bec | Sequence clauses hold; silence clause overreaches (F1) | UNVERIFIED, Contested |
| bc8f815c | Overreaches (F1); context bounds it to 258-391 | UNVERIFIED, Contested |
| 47d348b0 | Overreaches (F1); no end point of its own | UNVERIFIED, Contested |
| ab5908db | Named items all check; silence clause overreaches (F1) | UNVERIFIED, Contested |
| 7bf15a21 | Overreaches (F1); the rest holds | UNVERIFIED, Contested |
| caf67658 | Holds; consistent with Confessions III.12 as the next sentences read it, and with Rep Phase 1 line 82 (quoted verbatim) | JUDGEMENT, Widely Accepted |
| 004afcf9 | Holds; a congregation's own voice only | JUDGEMENT, Widely Accepted |

The two JUDGEMENT rows rest on one reading: a voice reported inside a later author's text (Confessions III.12, V.8, VI.2) is not the congregation's own.

## Observations (outside the ten claims; not fixed here)

- **O1 (P2).** Doc_02 §7 does not mention the nine row-229 tractatus. One of them is the Holy Innocents sermon that Morin thinks may be Optatus's: a bishop preaching to a congregation inside the interval. It stays outside the Native rows only because row 229 declines to give the nine a row. The downstream records disclose it; Doc_02 does not.
- **O2 (P2).** Doc_02 §7 does not name the rowless Knopf acts nos. 19-22 and 29, which are dated inside the interval. Felix of no. 22 is a bishop, heard at his trial.
- **O3 (P2).** The force record's description calls the Confessions V.8 oratory "not yet assessed". Doc_02 §7 treats III.12, V.8 and VI.2 as seen through Augustine's eyes and not filling the silence. The two statements disagree about whether it has been assessed.
- **O4 (P2).** Doc_02 §7 says Hartel argues that *De duplici martyrio* is "later than Cyprian". Hartel goes further: he suspects Erasmus wrote it, citing its mention of Diocletian and Maximin and of the Turks (Hartel III praefatio, `Diocletiani et Maximini (231,26), Caesaris Turcarumque (238,29)`).
- **O5 (P2).** Row 39 (Hartel CSEL 3.1-3.3, Native) also covers the spuria. Doc_02 §7 names rows 6 and 194 only.

## Gates

- `python -m engine.m10.cli claims lpc` in the live tree: FAIL, 4 findings. All four come from another thread's uncommitted edits to Doc_01 and Doc_02: two unregistered claims (93802ce0, 9fa60830) and two stale ids (1370a5c0, 345168d2). None comes from this pass. With HEAD's Doc_01 and Doc_02 and this register, in a clean worktree: PASS (104 derived, 104 registered, 8 UNVERIFIED).
- `python -m engine.m10.cli reviewfile` on this file: PASS.
