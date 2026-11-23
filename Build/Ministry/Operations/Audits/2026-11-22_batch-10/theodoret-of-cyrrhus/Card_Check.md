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

## Second pass check (2026-11-23)

Compared with the card before the second pass (`git show 265332d5:<folder>/theodoret-of-cyrrhus.card.json`) by a JSON walk. Changed: `briefReferences[1]`, `briefReferences[3]`, `quotationOriginals[3].uncertain`; added: `legacy.traces[3-6]`, `legacy.remembered[3-4]`, `uncertain[14-24]`, `sources.about[8-9]`. Nothing else moved.

1. **Checker changes.** FIX 1, 2 and 3 went in word for word, and nothing else in those fields moved.
2. **Additions.** Each is in its field and re-read at its lines: NP3 3205-3291 (the first assembling; the cries; "The vulgar cries are not worthy of bishops"), 3186-3205 (note 79), 31496-31498, 33171-33172, 33189-33193, 33476-33485 (Letter 119, note "i.e. Nicerte"), 3064-3069 ("The latter alternative was conceded"), 5208-5213, 36078-36109 (Letter 150, prefixed to the remarks on the anathemas), 2826-2838, 20518-20520 (Dialogue I), 3628-3634, 3666-3667; EVW 1773-1787; NP2 1695-1699; P449 15695-15709; ZACH 2429-2436; ANF9 1788-1794, 1922-1923; RH 113729-113734 and 113926-113940. Witnesses are credited where the outline credits them (Jackson, the chronicle, Hogg, Zenos, Evagrius). Two faults, below.
3. **Outline items.** Every "to the card" item (Outline 157, 163, 164, 166, 167, 169; Cut 2-9, 11-14, 16; Review 1, 12, 13) is now on the card or rightly skipped as already held (`datesNote`, `uncertain[1]`, `[4]`, `[5]`, `[7]`, `legacy.traces[0-2]`, `keyWorks[2]`). Fresh_Read sends nothing to the card.
4. **Scan readings.** None given, none listed.
5. **Rules.** Keys unchanged and allowed; American spelling; no audit, review or ruling named.

### Verdict: FIX (two changes)

**FIX A. `uncertain[24]`: "heard of them" turns his claim to have heard them into hearsay.** RH 113938-113941, "Καὶ τούτων αὐτόπτης ἐγενόμην ἐγὼ, καὶ ἀκήκοα", runs on (113952-113953) "τὴν πατρῴαν ἀσέβειαν ἀρνουμένων": he heard them themselves, renouncing.

- Old: `and that he was an eyewitness of these things and heard of them.`
- New: `and that he was an eyewitness of these things and heard them.`

**FIX B. `legacy.traces[4]`: the rescinded decree is given to the note.** It is in Jackson's text (NP3 3202-3205), not note 79, and the clause does not parse after "his note names".

- Old: `his note names Marcian as the emperor who summoned the bishops to Chalcedon, and that the decree keeping Theodoret in Cyrrhus appears to have been rescinded, so that he was free to present himself.`
- New: `his note names Marcian as the emperor who summoned the bishops to Chalcedon. He adds that the decree keeping Theodoret in Cyrrhus appears to have been rescinded, so that he was free to present himself.`


Coordinator (2026-11-23): FIX A and FIX B applied word for word.
