# R4 cap check: era 4 batch 5

## Scope

One targeted check, under Mark's standing ruling of 2026-11-14 (Decision-Log, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"). It does not count toward the three-round cap. It covers only the string changed in commit a7394764 under `Who-Profiles/era4/batch5/`:

1. Sophronius of Jerusalem, card `uncertain` item 1 (index 0): the second sentence, "His Greek" changed to "Theophanes's Greek" (R3-M1).

Reviewer: independent Opus, first sight of these files and of the drafting. I edited no profile file, made no git writes and made no web, paid or model calls. I used local reads, read-only git and a JSON load only.

## Method

- I read R3-M1 in `R3_recheck.md` and its fix text, then `git diff HEAD~1 HEAD -- Build/Ministry/Features` and `git diff HEAD~1 HEAD --stat`.
- I opened the vendored file myself and read the passage around the cited lines: THEOPH (`theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt`) l.61780-61830, Greek and Latin. OCR noise was read through.
- I read the brief's Theophanes sentences (`sophronius-of-jerusalem.brief.txt` l.9) and the `records.json` Theophanes claim and the contested claim "Sophronius's words to Umar".
- For the item I checked what the source says, the witness, pronoun reference, sentence length, AI tells and spelling.
- By script: `json.load` on the card and on `records.json`; word counts per sentence.

## 1. Sophronius, card `uncertain` 1: PASS

String: "Theophanes's account of Umar at Jerusalem, with Sophronius's words on the abomination of desolation, was written in the early ninth century. Theophanes's Greek can be read as saying it of the temple or of Umar; the Latin printed with it takes Umar. No text of Sophronius's own time gives those words." (21, 21 and 9 words.)

- The Greek: l.61787, "Toy vady iFhrnaev" (τὸν ναὸν ἐζήτησε, Umar asks for the temple), then l.61789, "Toiroy d wy Lwpdvs" (Τοῦτον δὲ ἰδὼν Σωφρόνιος). Τοῦτον is masculine accusative; ναός is masculine, and so is Umar. The object can be either. "Can be read as saying it of the temple or of Umar" holds.
- The Latin: l.61822, "lemplum a Salomene constructum" (templum, neuter), then l.61824, "Hune cum Sophronius vidisset" (Hunc, masculine). Hunc cannot take the neuter templum, so it takes Umar. "The Latin printed with it takes Umar" holds.
- Reference: "Theophanes's Greek" now names the author, so it can no longer be heard as Sophronius's own Greek. This is the R3-M1 fix, word for word. The later "with it" points to the Greek just named, and "those words" in the third sentence points back to "Sophronius's words". Holds.
- The whole item reads in order: who tells it and when, how the two texts differ, and that no source of his own time has the words.
- Brief: l.9 says "Sophronius wept. This is truly the abomination of desolation, he said, standing in the holy place." It leaves open what he saw, as the card does. Agrees.
- Records: the Theophanes claim reads "the Greek \"Τοῦτον\" (l.61789, OCR \"Toiroy\") can take the temple, \"ναόν\" (l.61787), or Umar; the Latin \"Hunc\" (l.61824) takes Umar", rated Contested, witness THEOPH l.61787-61792, 61809-61828. The contested claim gives "No held text of the seventh century gives the words". The card agrees with both.
- Writing: American spelling; no AI tell, hedge filler, contrast frame or beat line. The repeated "Theophanes's" at the head of two sentences is the price of a clear referent and reads as plain, not mechanical.

Considered, and not a finding:
- "saying it of the temple" and "printed with it" use "it" for two things in one sentence. The first is the idiom "say [the words] of" something, and the second follows straight after "Theophanes's Greek"; neither can be heard wrongly. Unchanged by this fix.
- The third sentence says "No text" where the records say "No held text". It is unchanged since R1 and passed rounds 1 to 3, and it is outside this check's changed string.

## Commit scope and JSON

- `git diff HEAD~1 HEAD --stat`: the Sophronius card (one line) and `R3_recheck.md`. Under `Build/Ministry/Features` the only change is this one string. `R3_recheck.md` is the round 3 review itself, the permanent audit trail, not participant text. Nothing else changed.
- The card and `records.json` load with `json.load`. PASS.

## Findings

None. No BLOCKING or MINOR finding.

## Verdict

CLEAR.

- "Theophanes's Greek" removes the pronoun capture R3-M1 found. The claim holds against THEOPH l.61787 and 61789 (masculine Τοῦτον after masculine ναόν, so open) and l.61822-61824 (masculine Hunc after neuter templum, so Umar).
- The item agrees with the brief and with `records.json`. The card parses, and nothing else in participant text changed.
