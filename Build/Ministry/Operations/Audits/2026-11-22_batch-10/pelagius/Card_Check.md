# Pelagius: card check

**Verdict: FIX** (two changes to `quotationOriginals`, three scan readings to add). Everything else passes.

## What was checked

1. **Edits against evidence.** Each new `legacy.traces` and `uncertain` entry was re-read at its cited lines and holds: NPNF105 10285-10286 (name with praise at Rome; glimpsed once or twice), 10294-10299 (Timasius and Jacobus; name left out to keep a friendly relation; "former disciples"), 4627 (brief notes on Paul), 10276 (private letters read at the trial), 9524 ("God is its helper whenever it chooses good"), 942 (eighteen Italian bishops, Julian), AVELL 11233 and 11277-11278 (Herote; "laicum uirum ad bonam frugem longa erga deum seruitute nitentem"), PL30 66-81 and 157-160, MERC 6998-7005, Jerome 47933, Bede 5432 and 5437. Two citations in `Card_Edits.md` are loose, not wrong in the card: Heros and Lazarus as the Gaulish bishops stand at NPNF105 9487 (and 905), not 9491; Bede's two quoted phrases stand at 5432 and 5437, inside the Source Sheet's 5428-5440, not 5395-5426. No card change needed.
2. **Nothing else moved.** A JSON diff of `Card.existing.json` and `pelagius.card.json` shows only appended items (two `legacy.traces`, seven `uncertain`, nine `sources.about`) and the two new keys. The census card equals `Card.existing.json`.
3. **`briefReferences`.** All 17 name what the brief tells. The "World census, The Pelagians" form is the census's own pattern (61 such entries).
4. **Census rules.** The card, set into a one-entry copy of the census with the brief as `longDescription`, gives no key, file, lines or `printed` error from `tools/validate-census.mjs`. The only `pelagius` errors are those release clears: `secondReading` absent (as the role requires) and the brief's modern quotes awaiting `tools/quote_renderings.json`. `tools/check_spelling.py`: 0 British spellings. No audit, review or ruling is named. Every cited file is in `sources`. **Fails on one point**: the outline renders quotation 1 from a held original (Outline.md line 52: PL30 814-817, "confirmed by two more held prints"), and the card does not carry it (FIX 1).
5. **"checked at card".** None; all three quotations are six words or more.
6. **Not found / clearly wrong.** None listed; none found left in.
7. **Census entry.** None (the entry exists).

## The eight scan readings (Goldbacher, CSEL 57, lines 4513-4515)

Checked against the file and against Migne PL 33 lines 62421-62424, the other held print of Letter 188 ("Non possunt / esse ista bona nisi in te, optime et verissime dictum / est; iste plane cibus est : quod vero ait, nonnisi ex u\ / hoc omnino virus est").

| Line | Scan | Reads | Verdict |
|---|---|---|---|
| 4513 | possnnt | possunt | Right (PL33 "possunt") |
| 4513 | boua | bona | Right (PL33 "bona") |
| 4514 | ni.i in te | nisi in te | Right (PL33 "nisi in te") |
| 4514 | optinie | optime | Right (PL33 "optime") |
| 4514 | uerissiine | uerissime | Right (PL33 "verissime"; "u" is Goldbacher's spelling, as in "uero" on 4515) |
| 4514 | piane | plane | Right (PL33 "plane") |
| 4515 | oinniuo | omnino | Right (PL33 "omnino") |
| 4515 | uirns | uirus | Right (PL33 "virus"; Goldbacher's "u") |

Each scan string stands once on its declared line, and the validator applies all eight without complaint. All eight are right, and none needs correcting.

## FIX

**FIX 1. `quotationOriginals[0]` (the riches passage): carry the Latin the outline renders from.** The role's rule ("prints its English alone unless another held print confirms the reading") does not apply: PL33 62416-62419 and Goldbacher 4493-4496 confirm every damaged word of PL30 814-817 (poterii: Goldbacher "poterit"; bis: both "his"; caeleris: PL33 "exteris", Goldbacher "eeteris", both pointing to "caeteris"). The card already accepts the same kind of confirmation for quotation 2. Replace the entry with:

```json
{
  "modern": "But spiritual riches no one can give you except yourself. In these, then, you are rightly praised. In these you are rightly set above others. They cannot exist except from you and in you.",
  "printed": "Spirituales vero divitias nullus tibi, praeter te, conferre poterit. In his ergo jure laudanda es : in his merito caeteris praeferenda es : quae nisi ex te, et in te esse non possunt.",
  "work": "Pelagius, Letter to Demetrias, ch. 11, ed. Migne (PL 30)",
  "file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt",
  "lines": "814-817",
  "englishPrinted": "your spiritual riches no one can have conferred on you but yourself; for these, then, you are justly praised, for these you are deservedly to be preferred to others,—for they can exist only from yourself and in yourself",
  "englishFile": "cic/texts/npnf105_augustine-anti-pelagian-writings.xml",
  "englishLines": "1281-1282",
  "uncertain": "The print is damaged; the wording given here is the reading it shares with Migne PL 33 lines 62416-62419 and Goldbacher lines 4493-4496, both also damaged, which quote the passage inside Augustine's Letter 188 without \"es\" after \"laudanda\". The English is B. B. Warfield's."
}
```

and append to `tools/quote_scan_readings.json`:

```json
{"file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt", "lines": "815", "scan": "poterii", "reads": "poterit", "kind": "OCR misread"},
{"file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt", "lines": "815", "scan": "in bis", "reads": "in his", "kind": "OCR misread"},
{"file": "cic/texts/pelagius_epistula-ad-demetriadem-lat_migne.txt", "lines": "816", "scan": "caeleris", "reads": "caeteris", "kind": "OCR misread"}
```

Tested in a scratch copy of the validator and readings: this entry and the three readings give no new error. Record the change in `Card_Edits.md` (item 1, riches passage).

**FIX 2. `quotationOriginals[1].printed`: restore the opening quotation mark.** The print reads `'Non possnnt` at line 4513; the card drops the `'`, which leaves the closing `'` after "in te" unpaired. The validator does not catch this, because it ignores punctuation, but the field is meant to be verbatim.
- Old: `Non possunt esse ista bona nisi in te', optime ...`
- New: `'Non possunt esse ista bona nisi in te', optime ...` (the rest unchanged)
