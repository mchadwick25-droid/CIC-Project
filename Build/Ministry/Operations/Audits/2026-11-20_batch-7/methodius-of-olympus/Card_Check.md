# Card check: Methodius of Olympus

Batch 7, 2026-11-20. Independent checker; I wrote neither the brief nor the card. This card was approved before the kit. Its research is `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/drafts/methodius-of-olympus.refs.md`, and the brief changed only at B1, B2 (and the content-neutral M1) in `Revision.md`. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (3 changes, below).

## 1. Each edit justified

- **Edit 1, uncertain[0], Tyre or Patara: justified.**
  - Jerome has "bishop of Olympus in Lycia and afterwards of Tyre" (npnf203 41095-41097).
  - Note 1126 has "Bishop first of Olympus and then of Patara" (20518-20519).
  - It adds a held source that differs, as the review's M2 asked.
- **Edit 2, uncertain[1], "Only Socrates": justified, but the insertion breaks a reference (FIX 1).**
  - "Only" contradicted the brief, which also tells Eusebius's question.
  - Jerome's Apology I.11 (51484-51490) holds: "makes the same complaint", and "How could Methodius dare to write now against Origen, after having said this thing and that of his doctrines?"
  - But the new sentences sit between Socrates and "He names the dialogue ...: Xenon". "He" now reads as Eusebius or Jerome. It is Socrates who names Xenon (npnf202 18154).
  - Moving the insertion after the Xenon sentence keeps every old word in its old order.
- **Edit 3, briefReferences[2], the Banquet: justified.** Brief paragraph 3; Jerome names it at 41098; the ten guests are at anf06 29930-29933.
- **Edit 4, briefReferences[10], the Patara note: not justified (FIX 3).** The brief does not tell Patara. It says only "Jerome says he was bishop of Olympus and later of Tyre." The Patara note belongs in `uncertain`, where Edit 1 has already put it.

## 2. Nothing else moved

I diffed the card against `Card.existing.json`. Apart from the four listed edits, every field is word for word and in order. The two inserted references push the later entries down.

## 3. References

Two entries name what the brief does not tell:

- [3], "at sixty-nine" (FIX 2). The brief tells only "some fifty years". "Under Gallus" stays as the basis for that reckoning.
- [10], Patara (FIX 3).

[4]'s "sixth book" is a locator, not a claim, and stays.

After the fixes, these 11 entries remain:

- Socrates VI.13
- Jerome, Lives 83
- the Banquet
- Jerome, Lives 54
- Jerome's Apology I.11
- Photius 234
- On the Resurrection (its quotation is verbatim in the brief)
- Epiphanius, Panarion 64
- Jerome's Letter 70
- Theodoret's Eranistes
- the census tradition

## 4. Census rules

- Keys are allowed, and there is no `briefLength`.
- There is one entry for the brief's one quoted span, and no extra. Its `printed` wording stands at anf06 35400-35402, across "same / parts".
- anf06 is in `sources`.
- `secondReading` ("minor") and `uncertain` are copied from `quotation-originals.json`.
- No audit is named, and the spelling is American ("honored").

## 5. Originals, and the ruling on the printed form

The card gives no `original`, and none is needed. There is no outline, and the refs file says that the span is Clark's English verbatim. So check 5 does not apply.

For the coordinator, I checked the held Greek by hand. Epiphanius keeps the passage in Panarion 64.33 (Holl, `epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` 35490-35495). It reads "ἀπὸ τῶν αὐτῶν ἣ σὰρξ μερῶν ... ἀϑάνατος χαὶ ἀπήμων ἐγερϑῇ, τελέως ἐκ βάϑρων ἀποΙ-λομένης τῆς ἁμαρτίας".

If it were added, the ruling would **LEAVE IT OUT**:

- χ for κ ("χαὶ").
- "ἣ" for ἡ.
- "ἀποΙ-λομένης".

No other held print of this Greek has been found. The Oehler Panarion covers haer. 48-69, and its Greek was not checked here. The Greek's τελέως ἐκ βάϑρων ("completely, from its foundations") matches the existing `uncertain` note on the doubled emphasis. Nothing more is needed.

## 6. "Not found" and anything left wrong

- **"Epiphanius of Cyprus" (legacy.traces[0]): stands.** He was bishop of Salamis, on Cyprus. The brief's "of Salamis" names the same man, so nothing is wrong.
- The card claims nothing else not found, and I found nothing else wrong.

## Fixes

**FIX 1.** `uncertain[1]`
- Old: `Socrates of Constantinople tells of his change of heart, and Socrates admired Origen. Eusebius of Caesarea, as Jerome quotes him, asks how Methodius dared to write against Origen now. Jerome reads this as the same charge, but Eusebius's words do not themselves say that Methodius praised Origen. He names the dialogue in which Methodius of Olympus praised him: Xenon.`
- New: `Socrates of Constantinople tells of his change of heart, and Socrates admired Origen. He names the dialogue in which Methodius of Olympus praised him: Xenon. Eusebius of Caesarea, as Jerome quotes him, asks how Methodius dared to write against Origen now. Jerome reads this as the same charge, but Eusebius's words do not themselves say that Methodius praised Origen.`

**FIX 2.** `briefReferences[3]`
- Old: `Jerome, Lives of Illustrious Men 54, tr. Richardson: Origen's death under Gallus at sixty-nine, some fifty years before.`
- New: `Jerome, Lives of Illustrious Men 54, tr. Richardson: Origen's death under Gallus, some fifty years before.`

**FIX 3.** `briefReferences[10]`
- Old: `Theodoret, Eranistes, editor's note: bishop first of Olympus and then of Patara at the beginning of the fourth century.`
- New: (remove the entry)
