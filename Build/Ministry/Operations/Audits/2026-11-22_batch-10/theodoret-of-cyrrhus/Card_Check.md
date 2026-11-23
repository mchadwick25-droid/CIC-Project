# Card check: Theodoret of Cyrrhus (`theodoret-of-cyrrhus`)

Read: `CLAUDE.md` (Trust and source fidelity), the card role, `theodoret-of-cyrrhus.brief.txt`, `theodoret-of-cyrrhus.card.json`, `Card_Edits.md`, `Card.existing.json`, `Outline.md`, `Source_Sheet.md`, `Review.md`, `Fresh_Read.md`, and the cited lines in `cic/texts/`. No census entry is written (the person has one), so check 7 does not apply.

## Verdict: FIX (three changes)

## What holds

1. **Edits justified.** The one correction (`uncertain[1]`, "which the Library holds in Greek") holds: the Religious History is held at `cic/texts/theodoret_opera-omnia-t3-historia-religiosa-pg82-grc-lat_migne1864.txt`, and the outline names this correction. The seven new `uncertain` entries hold at their lines: NP3 37972-37986 (Greek copies perished, three Latin versions, "not long after" the Chapters) and 37999-38000 (the Egyptian writings accepted); NP3 31455-31457 (Letter to Nomus, "No indictment was published; no prosecutor appeared"); P449 13316-13323 (Pelagius's libel); NP3 2913-2916 (the edict a year after Irenaeus, 17 Feb. 448); P449 header (22 August 449), NP3 2956-2957 (8 August), NP3 33035 (11 August); NP3 3303 (eighth session), EVW 5242 (ninth meeting); NP3 3350-3353 (Cyrus or Nicerte); ZACH 2219-2221 (the gift which blinds the eyes of the soul); NP3 17855-17864 (438-439, somewhat later). New `sources` rows are in the right groups and cover every cited file.
2. **Nothing else moved.** A JSON comparison with `Card.existing.json` shows only `uncertain[1]` changed, seven `uncertain` entries appended, three `sources` rows appended, and the new `briefReferences` and `quotationOriginals`. Every other field is word for word.
3. **briefReferences.** No quotation marks. Every entry but two parts (FIX 2, FIX 3) names something the brief tells.
4. **Census rules.** Only allowed keys; no `briefLength`; no connections. Seven quoted spans in the brief (`tools/list_second_readings.py`: 3 READ BLIND, 4 CARRIED), seven entries, each `modern` identical to the brief, none dropped. Each `printed` stands verbatim at its lines, re-read: NP3 38007-38010, NP3 4724-4726, NP3 31499, RH 113735-113738 (Greek, checked by hand, character for character with the scan), NP3 3335, EVW 1110, NP3 33203. No `secondReading` on the three long spans. Each file is in `sources`. No audit, review or ruling named. American spelling. Quote 1 renders from the held Latin (Mansi V 88759-88763: "injuste & inique", "anime imbecillitatem robo-rante", "cooperante gratia"), a damaged scan, so its English print stands alone and the `uncertain` says why. Quote 3's original is carried; no English or second print is held, so the damaged Greek is the only printed wording, and its faults are named.
5. **"checked at card" quotations.** "unwillingly" (NP3 31499, "was unwillingly consecrated bishop"), "Anathema to Nestorius" (NP3 3335), "a most excellent record" (EVW 1110), "not a tomb" (NP3 33203): each rendering is the print's own words, used in the print's sense. All hold.
6. **Not found.** `keyWorks[0].about`, "to the death of Theodore of Mopsuestia", rightly left and listed: NP3 18272-18274 has "the death of the admirable Theodorus and Theodotus", and Jackson's note dates Theodotus to 429. Not contradicted. Nothing else clearly wrong is left in the existing card.

## Changes

### FIX 1. `quotationOriginals[3].uncertain`: the scan faults are misdescribed

RH 113735 prints the first numeral correctly, "ἕξ" (six, rough breathing). The fault is at 113736, "νῦν δὲ ἐξ χαὶ τριάκοντα", where the six of thirty-six is printed "ἐξ", the preposition. And "καὶ" is printed correctly at 113737; the stray mark "«ἧς" (113738) stands where "τῆς" alone should stand.

- Old: `a stray mark where kai tes should stand; the first numeral is printed with a breathing mark that reads as the preposition ex.`
- New: `a stray mark where tes should stand; the six of thirty-six is printed with a breathing mark that reads as the preposition ex.`

### FIX 2. `briefReferences[1]`: the porticoes are not in the brief

The brief tells "he built bridges and a water channel for the town" and nothing of porticoes (Review B1 cut the list down).

- Old: `the monastery and being made bishop unwillingly; the porticoes, two bridges and the conduit;`
- New: `the monastery and being made bishop unwillingly; two bridges and the conduit;`

### FIX 3. `briefReferences[3]`: the birth at Antioch is not in the brief

The brief never says where he was born.

- Old: `Jackson's Prolegomena: his birth at Antioch from the Religious History; Ephesus in 431 on John's side;`
- New: `Jackson's Prolegomena: Ephesus in 431 on John's side;`

## Open item, not a change here

The role says that what the outline sends to the card goes under `uncertain` or its field. `Outline.md` sends many items "to the card" (lines 157-187: Juvenal's "salt", the first session's cries, the Eranistes and side works, Dioscorus on the pavement, Theodosius's death and the summons, the withdrawal to his monastery, Jackson's verdict on 553, Cassiodorus, the envoys of 431, the Apollinarius point, the parents' promise, the History's purpose, Simeon's leather clothes, the Arabs baptized, Eutyches restored, the second request to Leo, the officials' word on Leo restoring the see; Review cuts 12-13). Of these only the ten books, the 553 verdict and the officials' word were already on the card. `Card_Edits.md` does not list the rest as carried or set aside. The other batch-10 card checks did not apply this rule either, so it is raised for the batch to rule on, not given as a fix.
