# Council profiles, era 3: review round 3, targeted recheck (2026-11-14)

**Scope.** Only what changed in the last commit (`HEAD~1..HEAD`, `44cda4a3`) under `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era3/`, set against `R2_recheck.md` and the author's answer `R2_changes.md`. Changed files: the Constantinople 553 brief, audio script and entry; the Dvin entry; `records.json`. The Toledo profile did not change. Text that did not change was not reviewed again. This is the third and last review file on each of these documents.

**Method.**
- Read the word diff of every changed file against `HEAD~1`, then read each changed sentence in its paragraph or record row.
- Checked every new quotation and line citation in its vendored file: Ormanian on Mekhitar (`ormanian_church-of-armenia_gregory1912.txt` l.4483-4495); Barmby on Gregory and Istria (`npnf212_leo-great-gregory-great.xml` l.22455-22462, with l.23069-23071); Gregory's "The fifth council also I equally venerate" (`npnf212` l.31921-31922); Brosset's note citing Kirakos and Ukhtanes (`zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt` l.22668-22672); the address of Register XI.52 (`gregory-great_registrum-epistolarum-t2-pars2-libri-10-14-lat_ewald-hartmann1895.txt` l.12138, 12179). Looked for any held file of Kirakos or Ukhtanes in `cic/texts/` (none).
- Checked Gregory the Great's new people row against the Who scans (`2026-11-11_who-scan-era3/Who_Scan_Era3.md` l.5, 77) and the id `gregory-the-great` against `cic-website/data/world-census.json`.
- Counted words, ran `engine.m1.gates.grade_text` on the Constantinople brief from the repo root, split sentences and counted the longest, and compared the audio script with the brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph. Validated all four JSON files.
- No model calls, no network calls, no paid calls. No draft was edited.

## Gates (changed brief)

| Council | Words | FK | FRE | Audio = brief | Sentences over 25 words |
|---|---|---|---|---|---|
| second-council-of-constantinople-553 | 400 | 8.15 | 60.22 | yes | none (longest 24) |

It passes: 400 words, FK 10 or under, FRE 60 or over. The scores match `R2_changes.md`. The audio script equals the brief with the two tags, and carries no other tag. The Toledo and Dvin briefs did not change, so their round 2 scores stand. All four JSON files parse.

## Round 2 findings

| Finding | Severity (R2) | Status | Evidence |
|---|---|---|---|
| R2-1 | substantial | RESOLVED (records citation left out; see R3-1) | Dvin `uncertain[0]`: "Among the writers held, the synod at Dvin is told only by modern ones: Issaverdens in 1875, Brosset in 1876 and Ormanian in 1912. Brosset cites the medieval Armenian historians Kirakos and Ukhtanes for it; neither is held." Brosset: "Cette indication chronologique est entièrement fausse; v. Kiracos tr. fr. p. 24, Oukhtanès, tr. fr. p.284 sqq. La sécession eut lieu lors du concile de Dovin, tenu en 596" (l.22669-22671). The claim is now scoped and names the older witnesses, so the false absence is gone. Neither writer has a file in `cic/texts/`, so "neither is held" is true. "Medieval" is not in a held line, but it is true of both and not misleading. |
| R2-2 | minor | PARTLY | The letter to Quiricus is now `"kind": "participant"`, with the note "A letter of the time, not an account of the council; the nearest of the four kinds." "In Kyrion's time" is dropped, and "the Catholic bishops of Iberia" matches the address, "Quiricum episcopum et ceteros in Hiberia episcopos catholicos" (l.12138). The inference that overreached is gone. The new kind raises its own small point (R3-2). |
| R2-3 | minor | RESOLVED | `record` note: "whose founder, Ormanian says, had to yield to the demands of the Roman Curia." Ormanian: "Then he decided to settle in the small island of San-Lazaro at Venice (1717). Mekhitar had to yield to the demands of the Roman Curia" (l.4491-4493). The phrase now belongs to San Lazzaro, not the Morea house of 1712 (l.4486-4490). "For visitors" and the file-header witness are gone from the entry and `records.json`. The claim's "founded by Mekhitar" is a fair gloss of "decided to settle"; its citation l.4491-4495 is right. |
| R2-4 | minor | RESOLVED | New people row: Gregory the Great, `gregory-the-great`, WHO, "Not present; as bishop of Rome tried to bring the Istrian bishops back to communion, by James Barmby's account, and venerated the council". The era 3 scan scores him WHO (l.77), and the census has `gregory-the-great` as an era 3 person entry. Barmby: "He in vain endeavoured, either by remonstrance or by trying to enlist the emperor's aid, to bring back the Istrian bishops to conformity" (l.22460-22462). "Back to communion" rests on the same passage, where the churches "had renounced communion with Rome" (l.22456-22457). "Venerated the council" rests on l.31921-31922. The new `records.json` claim quotes Barmby verbatim and cites l.22455-22462 correctly. The row is applied under the profile's own rule, and Pelagius II stays. |
| R2-5 | minor | RESOLVED | Brief and audio: "Gregory the Great of Rome said he honoured the fifth council." Word count unchanged; rescored above. Side note R3-3. |

The one substantial finding of round 2 is resolved.

## New findings

All are minor. None makes a claim unsupported or a quotation inexact, and none blocks.

**R3-1. Minor (Dvin `records.json`; citation not carried).** R2-1's fix also asked for the Kirakos and Ukhtanes citation in the date's contested claim. `R2_changes.md` does not mention it, and the claim still gives "Brosset 1876: 596 (l.22671)" alone. The entry now carries the fact, so nothing is false or hidden. Optional fix: "Brosset 1876: 596, citing Kirakos and Ukhtanes, neither held (l.22670-22671)."

**R3-2. Minor (Dvin `record`; witness kind).** "Participant" puts Gregory among those who took part. The note says plainly that the letter is not an account of the council, and Facundus in the Constantinople profile sets a loose precedent for the kind. But Facundus was a party to that dispute, and Gregory had no part in the Armenian-Georgian break. The letter bears on Dvin only through the census's identification of Quiricus with Kyrion, which is tagged Inferential-Thin. "The nearest of the four kinds" is also process wording in a record row. Optional fix: take the letter out of `record`, as R2-2 first proposed; it stays in `uncertain[4]`, the contested claim and `sources`. Or say in the note: "It bears on the council only if Quiricus is Kyrion."

**R3-3. Minor (Constantinople entry; consistency left by R2-5).** The brief now says "the fifth council", but the unchanged note on the Roman church in `affected` (entry l.81) still says "Gregory the Great venerated a fifth council". It is the same wording R2-5 fixed in the brief. Optional fix: "the fifth council".

No new quotation was found outside its file. The changed text has no false absence, no witness swap, no translation or paraphrase in quotation marks, no first mention without a role, no sentence over 25 words, no AI tells and no "not X but Y" contrast.

## Counts (new findings)

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| second-council-of-constantinople-553 | 0 | 0 | 1 (R3-3) |
| third-council-of-toledo-589 | 0 | 0 | 0 |
| council-of-dvin-609 | 0 | 0 | 2 (R3-1, R3-2) |

## Final verdict

| Council | Verdict |
|---|---|
| second-council-of-constantinople-553 | CLEARS (R3-3 optional) |
| third-council-of-toledo-589 | CLEARS (unchanged since R2) |
| council-of-dvin-609 | CLEARS (R3-1, R3-2 optional) |

No blocking or substantial point remains open on any of the three councils. This is the third review file on each document, so the cap is reached. The minor items above do not justify another round and may be taken up or left at the author's discretion. None of them touches a brief, so taking them needs no rescore and no new audio.
