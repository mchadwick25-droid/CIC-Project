Simulated review — informational only, not an Article 31 substitute.

# Doc_06 full review after change order CO-LPC-1

- **Document:** `Build/worlds/lpc/Doc_06_Full_Lexicon_Development.md` (branch `claude/lpc-augustine-sermons-2026-10-23`; the file is identical at `a0209b8d` and at `HEAD` `4e7a4bd9`, last changed by commit `949edbcf`, "lpc change order, part 2"), with the deliverables it governs: `Lexicon-Chunks/lpclex001`–`lpclex019`, `Lexicon_Deployment_Index.md`, and the nineteen `records/lpc/term/` records
- **Round:** 4
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent adversarial review subagent, fresh context (drafted none of the text under review)
- **Drafter:** Sonnet 5.5 drafters for CO-LPC-1, checked by the `lpc` build thread; earlier text by the `lpc` build thread (draft 2026-09-14, fix passes 2026-09-15; drafting model not recorded in the Decision Log)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** CO-LPC-1 drafters and the `lpc` build thread
- **Date:** 2026-10-23
- **Scope:** full review of Doc_06 in its current state: every substantive claim; quotations re-verified against `cic/texts` by structural marker; consistency with the 2026-10-23 rulings (D1 to D5, Doc_02 §7, Doc_05 crosswalk, Article 20, lexicon discovery method, liturgical candidates), with OG-28 to OG-51, and with Docs 01 to 05; the three prior files `Doc06_Round1_Review.md` to `Doc06_Round3_Review.md`; the CO-LPC-1 diff (`949edbcf^..949edbcf`, three hunks at lines 18, 95 and 122); every chunk and term record OG-32 and OG-33 name. Doc_06 (Step 6) is not one of the six Forces Framework integration points, so that requirement does not apply.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md:6875`)
- **Truncation check, method 1:** line and byte count with an end-of-file read: `wc` gives 172 lines and 32,358 bytes; the file was read in full through line 172, which ends on the Disposition's closing sentence ("...neither bears on anything this lexicon asserts."), with §1 to §6, the Document Log and the Disposition present in order (lines 26, 36, 89, 105, 118, 135, 146, 160).
- **Truncation check, method 2:** hash comparison against the committed blob: `git hash-object` of the working file equals `git rev-parse HEAD:<path>` and `git rev-parse a0209b8d:<path>` (`afed9568`); `sha256sum` `95cdfde9…2c61`.
- **Method limits:** no web search and no model call. Nothing edited except this file. `regate lpc` was run read-only.

---

## What was verified and holds

- **CO-LPC-1's three edits.** Line 18 drops the Doc_04 round numbers and Doc_05's Round 2 verdict; line 95 drops "Round 1 verified"; line 122 (§5 item 3) now says the liturgical reads exist and cites the 2026-10-23 ruling, which exists under that title (`lpc_Decision_Log.md:2413`). Both reads exist (`Review-Artifacts/Liturgical_Evidence_Read_Cyprian_2026-09-19.md`, `…_Augustine_2026-09-19.md`). The edits change no tier, tag or count.
- **§2.4 quotations and count.** Each was confirmed inside `div1 id="iv" title="Cyprian."` of `anf05_hippolytus-cyprian-caius-novatian.xml`. The three are "designate by name in the certificate those whom you yourselves see…" and "Let such a one be received to communion along with his friends" (Epistle X, `iv.iv.x`), and "thousands of certificates". The shorter quotation fits both Cyprian's "were daily given" (line 30204) and the endnote's variant (line 29851, inside `<note>`), so it is safe. *Certificate(s)*: 42 in the div1, 38 once `<note>` spans are removed, under both substring and whole-word matching. This matches §2.4.
- **LDF V2.1 quotations** (§2, §2.3): all five were found verbatim in `CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx`.
- **Tier grounds against Doc_04.** G1, G2, G3 and G6 are Primary; G4, G5 and G7 are Supporting; G8 is Tensional (`Doc_04_Gravity_Discovery.md:158-165`; the gravity records agree). Doc_05 §5.2, §5.3, §6.5, §6.7, §9.1 and §9.2 say what Doc_06 cites them for (`Doc_05_Ecological_Reconstruction.md:207, 209, 251-255, 271, 325, 327`). Doc_04 §2 declines the illegal-to-established shift (`Doc_04:18`).
- **§4 shape 3, plenary Council.** The sentence in `npnf104` (On Baptism II.3) carries both moves as `lpclex013` quotes them.
- **[CT] Contest Types** (§3) are present in all three chunks, which agrees with the OG-29 ruling (`lpc_Decision_Log.md:2406`).

---

## Findings

### P1-1. The *libelli* and *libellatici / sacrificati* entries deny a classification that Cyprian's own text carries (M-N3, carried and wider than OG-32 records)

- **Sites.** `Doc_06_Full_Lexicon_Development.md:65` ("the two-way classification reaches this record as the vendored edition's own 19th-century editorial endnote on a different, Confidence-C text"). `:125-127` counts *libellatici* and *the lapsed* among the seven editorial instances and calls the second a "regression". `Lexicon-Chunks/lpclex017_libelli.md:55-57` ("on Doc_01's gloss rather than on attestation in this world's own primary text"). `lpclex018_libellatici-sacrificati.md:120-122` ("not as a claim about Cyprian's own terminology"). `lpclex002_the-lapsed.md:61` (Tier 1). `Lexicon_Deployment_Index.md:143-144`. `records/lpc/term/lpc.term.libelli.md:23-30, 61-65` and `lpc.term.libellatici-sacrificati.md:93-98, 128-133` (`formation_confidence: Inferential-Thin`, with build vocabulary in `senses.evidential`).
- **Evidence.** In English: `anf05_hippolytus-cyprian-caius-novatian.xml:33676-33678`, inside `div3 n="LI"` ("To Antonianus About Cornelius and Novatian"), Cyprian's own text reads *"those who receive certificates are to be put on a par with those who have sacrificed"*. Lines 33694-33696 add *"to associate those who have received certificates, with those who have sacrificed"*. In Latin, vendored since 2026-10-17: `cyprian_epistulae-lat_hartel1871-csel3-tei.txt:7838` (letter `n="55"`, section `n="13"`) reads *"libellaticos cum sacrificatis aequari"*, and line 7979 reads *"libellaticos interim admitti, sacrificatis in exitu subueniri"*. *De Lapsis* uses the word itself: `cyprian_de-lapsis-lat_hartel1868-csel3-tei.txt:1029` (§27, *"libellis tamen conscientiam miscuerunt"*) and `:1071` (§28, *"nullo sacrificii aut libelli facinore"*). Hartel's letters carry 44 *libell-* forms. The claim that the word is absent from the English holds (`anf05:64312`, the American editor's Note, is the only *libell-* hit). The conclusion drawn from that absence does not hold.
- **Why P1.** A confidence rating and a sourcing conclusion are wrong. The register's sixth "regression" was in fact a correct sentence. This is the same defect class as the editorial-apparatus problem the document guards against: the claim rests on the editor while the primary text says the same thing. Ep. LI and *De Lapsis* §27-28 also show that Cyprian graded the two acts, so a Contested or Inferential-Thin hedge is not warranted on the substance.
- **Fix.** Re-source both entries to Registry rows 1 and 39 (Ep. LI / Hartel 55 §13, §17; *De Lapsis* §27-28). Re-set `formation_confidence` on both records. Strip build vocabulary from `senses.evidential`. Rewrite §2.3's ground, then remove *libellatici* and *the lapsed* from the §5 item 6 register and index §7, and recount the instances wherever the count appears (Doc_06:125, :168, :170; index §7). Separately, record that Latin *libellus* in Cyprian also names the martyrs' petitions (`epistulae-lat:2467, 3629`), so that the *libelli* / *certificates* split in `lpclex017` / `lpclex019` is not presented as the Latin's own distinction. Register the corrected absence claims in `lpc_Claims_Register.md`.

### P1-2. The *plebs* absence claim and §5 item 7's "English throughout" premise are false against the vendored corpus

- **Sites.** `Doc_06_Full_Lexicon_Development.md:129` ("This world's corpus is a 19th-century English translation throughout"). The chain from §5 item 6 (`:125`) to `Lexicon_Deployment_Index.md:141` ("the only three occurrences of *plebs* in the vendored Cyprian corpus are in the editor's prose … the term is therefore **not** a headword"). `lpclex010_the-people.md:57`. `records/lpc/term/lpc.term.the-people.md:26-30, 64-66`.
- **Evidence.** `cyprian_epistulae-lat_hartel1871-csel3-tei.txt` carries 128 lower- and upper-case *pleb-* forms (plebs 10, plebem 40, plebis 32, plebi 29, plebe 17). They appear in running text: letter `n="4"` §2, line 498, *"et praepositis et plebi"*; letter `n="5"`, line 769, *"plebi prouidere debemus"*. Letter `n="43"`, the letter the chunk itself cites as ANF Ep. XXXIX "to the people", is headed *"CYPRIANVS PLEBI VNIVERSAE S."*. Doc_02 itself says *"Original-language witnesses are now vendored for nearly the whole corpus"* (`Doc_02_Source_Ecology.md:31`). The sermon scope (D1, D4) rests on the Latin of PL 38 (OG-28).
- **Why P1.** This is an unregistered absence claim, now false, in a record that feeds the room. It also disqualifies a term from headword status on that ground.
- **Fix.** Restate the *plebs* finding as scoped to the English volume. Add the Latin attestation, and decide by change order whether *plebs* becomes the world word. Correct §5 item 7's corpus premise to match Doc_02:31. Register the claim. Re-run the §5 item 6 register count after P1-1.

### P1-3. Doc_06's escalation assessment still treats Doc_04 Open Item 6 as an open tension (an OG-38 site CO-LPC-1 missed)

- **Site.** `Doc_06_Full_Lexicon_Development.md:170`: *"Unresolved tensions: **one open** — the evidentiary question at Doc_04 §7 Open Item 6"*.
- **Evidence.** `Doc_04_Gravity_Discovery.md:266`: *"Unresolved tensions: none open. §7 Open Items 6 and 8 are closed."* `Doc_05_Ecological_Reconstruction.md:368, 425` and `Doc_07:250` agree. The CO-LPC-1 entry says Open Items 6 and 8 are now "shown closed everywhere" (`lpc_Decision_Log.md:2495`). OG-38's site list omitted Doc_06, and the sweep did not go outward to it.
- **Why P1.** It is a stale status claim in the disposition's own escalation control. It says an escalation category is open against this document when the governing document says none is. The CO record claims a completeness that does not hold.
- **Fix.** Restate line 170 to match Doc_04:266. Then sweep every remaining approved file for "Open Item 6" again.

### P2-1. Status and history lines contradict each other, and the CO record overstates what was removed

`Doc_06:20` says five Round 2 findings are "listed at §5". `:22`, an orphaned paragraph that begins "…then returned", says "the remaining six are carried at §5". `:168` says five. §5 lists none of them. `:164` points to §5 for L-N1, and §5 does not mention it. `:156` says the Round 3 fix pass was "All applied", while OG-32 carries the Round 3 M-R2 residue at `:129`. `:120` keeps the round narration ("since Doc_04's Round 2 … survived two rounds") that CO-LPC-1 removed from `:18`. The Decision Log says CO-LPC-1 removed "Doc_06's Round 2 verdicts and 'nine rounds' line" (`lpc_Decision_Log.md:2497`). The Round 2 verdict remains at `:22`. No "nine rounds" line was ever in Doc_06 (`git show 949edbcf^`); the phrase survives at `lpclex012:55`. *Fix:* delete `:22`; make the carried-findings pointer name the Disposition, or make §5 list them; correct `:156`; align `:120` with `:18`; correct the Decision Log line by a logged note.

### P2-2. The new §5 item 3 cites a Doc_02 site that still says the reading was not done

`Doc_06:122` cites "Doc_02 §9 item 9" for the reading. `Doc_02_Source_Ecology.md:141` still says the liturgical category "has not been read as liturgical evidence specifically". The ruling named three stale sentences (`lpc_Decision_Log.md:2416`); this is a fourth copy. *Fix:* propagate the correction to Doc_02:141, or cite the reads directly instead of Doc_02.

### P2-3. The OG-36 ruling is not reflected, and the count and rule statements drift

§5 item 7 (`:129`) and the Disposition (`:170`) still say the discovery-method question is "flagged for the project lead" and "filed here". It was ruled for `lpc` on 2026-10-23 (`lpc_Decision_Log.md:2398-2402`). `:129` still gives a bare "42" without the 38 (M-R2 residue, OG-32). §5 item 5 (`:124`) says 113 reproduces under "markup-stripped substring matching". Doc_05 §11 item 14 says "raw substring" (`Doc_05:387`). Neither gives the note-free 106 that OG-36 records. *Fix:* cite the ruling, give 42/38, and state the rule and the note-free figure.

### P2-4. The Source Registry status is stale

`Doc_06:16` and §5 item 4 (`:123`) say `Source_Registry.md` is "returned to independent review 2026-09-13". The Registry's own status is Approved to proceed, with later rechecks (`Source_Registry.md:3`). *Fix:* restate it.

### P2-5. *Suffrage* has no [DR] tag (OG-33, open)

Doc_06 §4 shape 2 (`:110`) names *suffrage* as a captured-sense word. `lpclex011:10` and index row 11 (`Lexicon_Deployment_Index.md:25`) carry [AS] only, the record has `distortion_risk: medium` (`lpc.term.suffrage.md:56`), and index `:92` calls it "unresolved". The chunk carries the full Modern/World Hearing pair, so the harm is limited to retrieval priority. *Fix:* as OG-33 states.

### P2-6. Carried hygiene findings, all still present (OG-32)

L-N2: review-round narration at `lpclex012:55`, `lpclex016:59` and `lpclex019:63`. `lpclex019:73` calls a paragraph with no brackets a "bracketed block". Index `:5`, `:72`, `:92`, `:104`, `:110`, `:129`, `:159`. L-N3: `Doc_06:67` and index `:72` rest the zero-Tier-3 result on a premise Doc_03 does not state. C-N1: `lpclex019:33, 35` print "*Designate…*" and "*Certificates…*" with capitals the source does not have (`anf05`, Epistle X, lower-case, mid-sentence). *Fix:* as OG-32 states.

### P2-7. A quotation is attributed to the wrong framework

`Doc_06:32` attributes *"the ecology informs the depth of lexicon entries — a term's true ecological weight becomes clearest after the formation ecology is established"* to CF V7.4. CF V7.4 has only the first clause. The full sentence is LDF V2.1's Doc_06 paragraph. *Fix:* attribute it to LDF V2.1, or quote only CF's clause.

### P2-8. A preface phrase is attached to the wrong referent

`Doc_06:125` says the `npnf101` preface calls Augustine's coercion doctrine *"least satisfactory to Protestant readers"*. In the source, that phrase describes the anti-Donatist works as a body ("These works are the chief patristic authority of the Roman Catholic doctrine of the church… They are thoroughly Romanizing in spirit and aim, and least satisfactory to Protestant readers"). The coercion sentence, with *"a false exegesis"*, follows it. The same framing appears at `lpclex016:63`, index `:142` and `lpc.term.compel-them-to-come-in.md:33, 88`. *Fix:* attach each phrase to its own referent.

### P2-9. Term records carry build vocabulary and later reception in world-voice fields

The first-person `senses.informational` fields say "Doc_06 names it…" (`lpc.term.grace.md:74`, `compel-them-to-come-in.md:75`, `schism.md:62`). Grace and compel also narrate "Reformation-era … appropriations" in the world's own "we". D3 places Reformation questions outside the room, with a pointer to `rzg`. These fields are not in the spoken-field registry (`engine/m1/spoken_fields.py:224`), so the voice does not say them today. *Fix:* move contest wording to `divergence_note` in third person, and drop document names.

### P2-10. Two spoken term fields fall below the readability floor

`regate lpc` reports `lpc.term.grace` `plain_meaning` at FRE 59.1 and `lpc.term.preaching` `quick_meaning` at FRE 51.7. Both failures predate this change and are unchanged, and both fields are participant-facing. *Fix:* re-draft both to FRE 60 or higher without losing the world's wording.

---

## Summary

Counts: 0 P0, 3 P1, 10 P2. The tiering argument, the gravity grounds, the [CT] contest types, §2.4's quotations and count, and CO-LPC-1's own three edits hold. The three P1s share one root. The lexicon's sourcing claims were made against an English-only corpus and against one document's list of stale sites. Neither premise holds now. The Latin vendored on 2026-10-17 overturns two absence or editorial findings, and the OG-38 sweep did not reach Doc_06. Under the Cap ruling, these findings go to the project lead; no further review file follows without a new ruling.

## VERDICT: Substantial revision required

VERDICT: Substantial revision required
