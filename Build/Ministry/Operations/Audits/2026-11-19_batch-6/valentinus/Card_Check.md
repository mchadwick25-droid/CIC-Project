# Card check: Valentinus

Checker, batch 6, 2026-11-19, per `Card_Check_Prompt.md`. Card: `valentinus.card.json`, against `Card.existing.json` (identical to the census `card`), `valentinus.brief.txt` and `Card_Edits.md`.

## Verdict: FIX (two changes)

## 1. Each edit is justified

- keyWorks, "A sermon": CL 39090-39096 ("Valentinian, in a homily, writes in these words"). Justified.
- sources.ownWords[0].title, "and a sermon ... Books 2 and 4": as above. Justified.
- sources.about, Clement, "Books 2, 4, 5 and 7": CL 39096-39098 (IV.13, "supposes a class saved by nature"), CL 40954-40960 (V.1, "apart from the Saviour's appearance"). Justified.
- sources.about, Kroymann's Latin added: the outline renders Quote 2 from KR 9633-9634, 9652-9653, and the ending's "now nowhere" from KR 9663 ("nusquam iam Valentinus"). Justified.
- uncertain[4], "No early source": HOLL 28941-28948 (*Panarion* 31.2) reports that some said he was born a Phrebonite on the Egyptian coast, and that most do not know. A held source contradicts the old line, and the outline's own wording is "no early source says where he was born". Justified, fewest words.
- briefReferences and quotationOriginals: new, checked below.

## 2. Nothing else moved

A field-by-field diff against the starting card shows only the edits listed: keyWorks[1] added; sources.ownWords[0].title; sources.about[3] (Kroymann) inserted before Clement, whose title alone changed; uncertain[4]; briefReferences and quotationOriginals added. Every other field is word for word.

## 3. References

One part names something the brief does not tell. VI.29's "and the first pair": the brief gives Hippolytus's account only as "the Father was alone, and he was all love", with the quotation. It does not tell Hippolytus's pair (Nous and Aletheia, HIP 9172-9173); the brief's pairs are Irenaeus's. FIX 1.

The rest remain, each told by the brief: Clement II.20 (the inn); IV.13 and V.1 (the sermon; saved by nature, apart from the Savior's appearance); Irenaeus III.4.3 (Hyginus to Anicetus, the brief's "from the time of one bishop there to another") and I.11.1 (the pairs and the fall); Tertullian, *Against the Valentinians* 4 (bishopric, martyr's claim, the true rule, ambition and revenge, Ptolemy, now nowhere, Axionicus; the editor's date, behind "about fifty years later", TE 42916); *Prescription* 30 (expelled more than once, TE 21336-21338); Hippolytus VI.35 (the two branches, HIP 9643-9661); the census tradition entry (eighteen centuries, 1945). No quotation marks.

## 4. Census rules

Allowed keys only; no `briefLength`. Four quoted spans in the brief, four entries, each `modern` the brief's span. Each `printed` stands at its file and lines (re-read: CL 34300-34302, TE 43109-43114, HIP 9171-9172, CL 39093), and every cited file is in `sources`. The one quotation mark in another field ("the disciple of Platonism.") stands at TE 21333. No audit, review or ruling named. American spelling outside printed wording ("Savior's").

The ANF index files CL 39090 under Valentinus (page 425, index line 58852), as entry 4's `uncertain` says. The `uncertain` note on quotationOriginals[2] ("the 'he' who says it is not named") agrees with HIP 9170-9171.

`secondReading` is absent on all four, as the step order has it (step 7). The validator fails until then.

## 5. Originals

Quote 2 is rendered from Kroymann's Latin, and the outline cites it (Outline, Quotes, 2: KR 9633-9634, 9652-9653). The card leaves it out of `original`, saying the page break and apparatus mean it "cannot stand as one `original` span". It can: `tools/quote_scan_readings.json` drops footnote, apparatus and running-head lines inside a span (as at Augustine, Confessions, Knoll 13474-13500). FIX 2.

The Latin fails at four places, each only a scan fault, all in `cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt`:

- line 9633: scan `episco-  25`, reads `episco-` (Kroymann's margin line number 25 sits between the line-end hyphen and the break, so the hyphen join cannot make episcopatum).
- line 9634: scan `Yalentinus`, reads `Valentinus`.
- lines 9635-9651: Kroymann's notes and apparatus, the running head and the page number 181, dropped. Held lines, exactly as the file has them (trimmed), are in the JSON below.
- line 9652: scan `aliura`, reads `alium`.

With these four readings the `original` below stands in lines 9633-9653 (checked with the validator's own fold and hyphen rules). Entries for `tools/quote_scan_readings.json`:

```json
[
 {
  "file": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt",
  "lines": "9633",
  "scan": "episco-  25",
  "reads": "episco-",
  "kind": "line number run into the line"
 },
 {
  "file": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt",
  "lines": "9634",
  "scan": "Yalentinus",
  "reads": "Valentinus",
  "kind": "OCR misread"
 },
 {
  "file": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt",
  "lines": "9635-9651",
  "scan": "11]  cf.  I  Tini.  1,  4.",
  "drop": true,
  "kind": "footnotes, apparatus, running head and page number",
  "lines_held": [
   "11]  cf.  I  Tini.  1,  4.",
   "1  putant  F  2  ad  aliam  fort.  4  fidem  om.  P  (add.  E  in  mg.  ex",
   "Hirsaugiensi)  ostendere  F  6  <(recor)>dabitur  se  Eng:  dabitur  te",
   "FMF  7  aliqua  scripsi:  alia  PMF  8  fidei  PM,  filii  F  9  genimina",
   "M  {syll.  ni  s.  u.  a  m.  ])  NGR^,  gemina  PFB^       14  neque  PM,  nec  F",
   "16  utique   astute  scil.  non   omnes  perdocent  (-=  sie  lehren  vollstdndig)",
   "17  omnia  (ia  ex  es  M)  scimus  MFGR^,  ornnes  sumus  PB^  18  armabimus",
   "f.cripsi:  armauimus  PMF  20  auspicamus  (s  in  r)  M  22  nouissimus",
   "F      originem  optime  M      25  sperauerat  R,  separauerat  P  (corr.  R)  MF",
   "IIII.  Aduersus  Valentinianos  3—4.  •     181"
  ]
 },
 {
  "file": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt",
  "lines": "9652",
  "scan": "aliura",
  "reads": "alium",
  "kind": "OCR misread"
 }
]
```

## 6. Not-found claims, and anything clearly wrong left in

The card lists none not found. I confirmed the ones it names: IR 31519-31521, 39968-39970; TE 21332-21338, 43117-43128; HIP 10054-10065; CL 52962-52963. Nothing else clearly wrong.

## The fixes, as exact JSON changes

**FIX 1.** `briefReferences[5]`
- Old: "Hippolytus, Refutation of All Heresies VI.29: the Father alone and all love, and the first pair. VI.35: the Italian and Eastern branches of the school."
- New: "Hippolytus, Refutation of All Heresies VI.29: the Father alone and all love. VI.35: the Italian and Eastern branches of the school."

**FIX 2.** `quotationOriginals[1]`: `uncertain` replaced, and `original`, `originalFile`, `originalLines` added (after `uncertain`), once the four readings above are in `tools/quote_scan_readings.json`.
- Old `uncertain`: "The modern English is rendered from the Latin, which Kroymann prints across a page break, at lines 9633-9634 and 9652-9653: sperauerat episcopatum Valentinus, quia et ingenio poterat et eloquio, sed alium ex martyrii praerogatiua loci potitum indignatus de ecclesia authenticae regulae abrupit (the scan reads Yalentinus and aliura). \"Suffering for the faith\" renders martyrii, where the ANF has \"confessorship\"; \"the true rule\" renders authenticae regulae, where the ANF has \"the true faith\"."
- New `uncertain`: "The modern English is rendered from Kroymann's Latin. \"Suffering for the faith\" renders martyrii, where the ANF has \"confessorship\"; \"the true rule\" renders authenticae regulae, where the ANF has \"the true faith\"."
- Added: `"original": "sperauerat episcopatum Valentinus, quia et ingenio poterat et eloquio, sed alium ex martyrii praerogatiua loci potitum indignatus de ecclesia authenticae regulae abrupit"`, `"originalFile": "cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt"`, `"originalLines": "9633-9653"`
