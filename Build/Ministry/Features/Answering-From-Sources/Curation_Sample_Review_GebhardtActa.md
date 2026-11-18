# Curation sample review: Gebhardt, Acta martyrum selecta (redo of PR #1337)

Reviewer: Opus 5.5, 2026-10-30. Reviewed fresh against the vendored file `cic/texts/acta-martyrum-selecta_gebhardt1902.txt` (12,350 lines), with the sister scan `cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` used for second printed instances. `check` and `sample` were run with the `answering_library` code exported from origin/main.

## Verdict

| stem | verdict | what was checked (line numbers) | defects / notes |
|---|---|---|---|
| acta-martyrum-selecta_gebhardt1902 | needs-redo | `check`: RESULT PASS, class curated, 88 divisions (86 body, 2 apparatus), coverage 100%, 0 oversize, 217 of 217 byte ranges exact; perpetua-latin 1-21 no defects, pionius 1-23 no defects, perpetua-greek 1-21 with one gap (6 to 8 at 3821) excused by `expected_gaps`. All 24 evidence quotes found. The 7 fixes, the widened pionius pattern, line 4356, the 4 hand-listed Greek lines and the warns judged below. Divisions checked against the printed head: all 22 piece heads (548, 1080, 1290, 1447, 1698, 2394, 3203, 4786, 5672, 5907, 6002, 6172, 6374, 6931, 7590, 7748, 7954, 8451, 8530, 8679, 9442, 9890) with running heads at 1735, 2490, 5708, 5940, 6078, 6210, 6412, 7631, 7781, 7994, 8716, 9476, 9935; all 41 Perpetua chapter heads (Latin 3208-4627, Greek 3228-4645); all 23 Pionius heads (4793-5655). The 3 largest (piece20 8679, piece6 2394, piece5 1698) and 3 smallest (piece7 3203, piece8 4786, lat-ch3 3349) seen. Apparatus 11-547 (front matter, ending in the abbreviation list) and 10569-12350 (Verzeichniss der Bibelstellen and the name index) confirmed. | One defect: the Greek Perpetua chapter VII head is printed at line 3729 and was missed; the `expected_gaps` entry hides it. |

## The defect

**Greek Perpetua VII, line 3729, printed `25 VIL Καὶ μετ’ ὀλίγας ἡμέρας προσευχομένων ἡμῶν`.** The edition prints the numeral. The OCR reads the final I as L, so the pattern `[IVX]+[.,]? ` does not match, and the line is not hand-listed. Three printed instances back the reading VII, none of them sequence:

- the Latin counterpart VII at 3709, `VII. Post dies paucos, dum uniuersi oramus` (the same words as μετ’ ὀλίγας ἡμέρας προσευχομένων ἡμῶν ἁπάντων);
- the running heads `79 VII. Passio S. Perpetuae VII.` at 3698 and `VII. Passio S. Perpetuae VII. - 13` at 3746;
- the sister scan, line 4048, `25 VII. Kai usr” ökiyas nueoas 1r0008vXouEvav Numv`, a clean VII.

The redo report says the Greek VII text "begins at line 3765" and that the sister scan shows no numeral "from line 4054 onward". Both are wrong: 3765 (`αὐτῇ τῇ νυκτὶ ἐδηλώθη μοι τοῦτο`) is the middle of the chapter, after a page turn, and the sister head sits at 4048, just before 4054. The `expected_gaps` entry for perpetua-greek at 3821 therefore records a scan limit that does not exist. It is not an honest explanation of the gap, and it must go. As it stands, Greek VII (3729-3737 and 3765-3779) sits inside `piece7/lat-ch7`; it stays addressable, but the edition's own Greek chapter VII is not a division.

**Correct reading for the redo drafter:** hand-list line 3729 in `perpetua-greek`, add a fix `{line: 3729, set: {c: 'VII'}, quote: '25 VIL Καὶ'}` with an evidence entry, and remove the `expected_gaps` entry. The series then reads 1-21 with no gap. Nothing else needs to change.

## The judgment calls that hold

- **Greek VIII, 3821, printed `25 VII Kai`, set to VIII.** Latin VIII at 3800 `VIII. Die quo in neruo mansimus` (= ἐν τῇ ἑσπέρᾳ ἐν ᾗ ἐν νέρβῳ ἐμείναμεν), running head 3789 `VII. Passio S. Perpetuae VIII.`; the sister scan 4143 also reads `VII Kai`, so the damage is in the print source, but the counterpart and running head carry it. Accepted.
- **Greek XI, 4043, printed in Greek letters `ΧΙ. ᾿“λλὰ`.** Latin XI at 4025 `XI. Sed et Saturus benedictus` (= Ἀλλὰ καὶ ὁ μακάριος Σάτυρος), running heads 4019 `Perpetuae ΧΙ.` and 4062 `Perpetuae ΧΙ,`; sister 4398 `XI Ha xoi 0 paxagıos`. Accepted.
- **Greek XII, 4128, printed `XI. Ko`, set to XII.** Latin XII at 4112 `XII. Et uenimus prope locum` (= ἤλθομεν πλησίον τοῦ τόπου), running head 4109 `Perpetuae XII. 81`. The sister 4493 also reads `XI.`, so again the counterpart and running head carry it. Accepted.
- **Greek XIII, 4191, printed `20 XII.`, set to XIII.** Latin XIII at 4173 `XIII. Et exiuimus` (= Ἐξήλθομεν δὲ καὶ εἴδομεν πρὸ τῶν θυρῶν), running head 4161 `Perpetuae XIII.`; sister 4551 `20 XIII E&nAdouev`. Accepted.
- **Greek XVIII, 4416, printed `XVII.` a second time, set to XVIII.** Latin XVIII at 4397 `XVIII. Inluxit dies uictoriae` (= Ἐπέλαμψεν δὲ ἡ ἡμέρα τῆς νίκης), running heads 4384 and 4428 `XVIII.`. The real Greek XVII is 4374 `XVII. Ale καὶ πρὸ μιᾶς` (= Latin XVII 4356 `Pridie quoque`), so 4416 is not a true repeat. Accepted.
- **Pionius IX, 5132, printed `ΙΧ. Εἶτα`.** Running head 5125 `Martyrium S. Pionü IX. 103` on the page where the head stands; the sister scan has the running head at 5529 and, more strongly, the head itself at 5536 `IX. Era enngornoev`. Accepted.
- **Pionius XX, 5558, printed `AX. Σιωπῶντε`.** Running head 5533 `112 VIII. Martyrium 8. Pionii XX.`; sister running head 5991 and the head itself at 6017 `XX. Nıoravr de`. Accepted.
- **Pionius XVII, 5465, printed `15 XVII. Kai`.** A margin line number before a plain XVII; the widened pattern `^(?:\d{1,2} )?` admits it. Running head 5445 `110 VIII. Martyrium S. Pionii XVII. XVIII.`; XVIII follows at 5476. No other line in 4787-5672 newly matches through the widening (the 23 hits were listed by hand). Accepted.
- **Line 4356, `piece7/lat-ch17`.** The line is `XVII. Pridie quoque cum illam caenam ulti-`, a true Latin head; running head 4343 `Perpetuae XVII.`. Accepted.
- **The 4 hand-listed Greek lines 3821, 4043, 4191, 4416** are true Greek chapter heads (each judged above). 4043 still appears in a warn because its Greek-letter numeral does not match the pattern; the fix sets it, so the warn is noise.
- **Running-head hazard (Pionius).** Every Pionius division starts at its chapter head, not a running head. The running heads 4819, 4874, 4919, 4981, 5021, 5082, 5125, 5166, 5209, 5249, 5290, 5346, 5445, 5492, 5533, 5573, 5632 all begin `VIII. Martyrium` or a page number plus `VIII. Martyrium`, and none matches the pattern (the lookahead and the required `. ` after the numeral both stop it). Heads: I 4793, II 4804, III 4829, IV 4851, V 5007, VI 5036, VII 5072, VIII 5106, IX 5132, X 5174, XI 5194, XII 5222, XIII 5274, XIV 5314, XV 5396, XVI 5435, XVII 5465, XVIII 5476, XIX 5524, XX 5558, XXI 5584, XXII 5638, XXIII 5655. Each chapter starts on or after the page whose running head names it.
- **Piece heads read through OCR.** `Υ.` at 1698 (backed by running head 1735 `V. Epist. eccl.`), `ΙΧ.` at 5672 (5708), `ΧΙ.` at 6002 (6078), `X VII.` at 7954 (7994), `ΧΙΧ.` at 8530, `ΧΧ,` at 8679 (8716), `ΧΧΙ.` at 9442 (9476). Each is the printed numeral in Greek-letter or spaced OCR form, not set from sequence.

## The look-alike warns

All 61 pionius warn lines were read. They are verse numbers inside the Greek text (for example 4833 `2 καί`, 5134 `2 Πολέμων`, 5160 `8 Πολέμων`), apparatus lines of Bible references (4816, 4865, 4909-4911, 5119-5122, 5245-5246, 5282-5287, 5381-5382, 5665), and plain text lines. Two (5132, 5558) are the fixed heads. None is a missed roman chapter head; the head list above is complete I-XXIII.

## Recurring pattern

The drafter's report states as fact a reading of the file that the file does not bear out ("Greek text begins at line 3765", "no numeral ... line 4054 onward"), and an `expected_gaps` entry was used to excuse a gap instead of looking a page back for the head. The gap needed one more search of the Latin counterpart's page, where the Greek head stands.

## Tooling observations

- `check` passed while the file carried the missed head, because `expected_gaps` silenced the one signal that pointed at it. An `expected_gaps` entry should perhaps require a stated reason the reviewer can check (for example "the counterpart page prints no Greek numeral"), not only a quote of the next head.
- The warn for perpetua-greek still lists 4043 although a fix on that line sets the number; warns could skip lines a fix covers.
