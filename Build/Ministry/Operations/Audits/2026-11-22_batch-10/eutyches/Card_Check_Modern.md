# Eutyches: card check, fourth pass (no modern opinion), 2026-11-23

Checked `eutyches.card.json` against `Card.pass3.json`, the edit list under "Fourth pass: no modern opinion (2026-11-23)" in `Card_Edits.md`, and `eutyches.brief.txt` as it now stands (compared with `eutyches.brief.v4.txt`).

**Verdict: FIX** (two changes, below).

## What holds

- **Nothing else moved.** A JSON diff of the starting card and the card shows only the five listed edits: three `uncertain` entries appended, `briefReferences[1]` and `[8]` changed.
- **Evagrius's date** (uncertain, new). Evag-E 12203-12204: "Here let me close my history, in the twelfth year / of the reign of Maurice Tiberius". Line 214: "FROM 431 TO 594 A.D."; line 12173: "DEATH OF GREGORY.—A.D. 594." Holds, and is marked as Walford's.
- **Timothy's return** (uncertain, new). Evag-E 5367: "REVOLT OF BASILISCUS.—a.D. 475." Zach 5248-5249: "So Basiliscus issued an order that Timothy should return / from banishment." No year there. Holds.
- **The churches not his followers** (uncertain, new). Payne Smith, `john-ephesus_ecclesiastical-history-part3_paynesmith1860.txt` 225-228: "though his party are not to be confounded with the fol / lowers of Eutyches, whom they anathematized by name". Douglas, `christian-east_v3-no1-march-1922.txt` 3909-3913: "have never been so to the core. They / -anathematized Eutyches, and their rejection of Chalcedon cannot be / taken as proof of their heresy." The article is J. A. Douglas's, "Relations with Mar Ignatios" (heading at 3658, byline 3673). Both are named and marked as modern.
- **briefReferences[1].** The brief no longer has the "later writer" sentence; the clause on the followers of Dioscorus and Eutyches is rightly removed. Evag-E 6795-6797 holds only "the genuine followers / of Dioscorus and Eutyches were reduced to a very / small number".
- **briefReferences[8].** Zach 4093-4097 (Timothy wrote "against / those who hold the opinions of Eutyches") supports the brief's "did not count themselves his followers"; Zach 5638-5643 holds the curse and the cleared suspicion. No quotation marks; no wording the brief has lost.
- **Every other briefReferences entry** names only what the brief still tells.
- **quotationOriginals.** Four entries for the brief's four quoted spans, unchanged. Re-opened: Perry 23843-23845 and 23494-23495, 23504; Bidez-Parmentier 2285-2286; Leo 5028 ("this he certainly never did") and 4560 ("two natures,"). The two "checked at card" renderings match their print.
- No audit named; American spelling.

## FIX

**1. `sources.about`: two cited files are missing.** The new `uncertain` entry cites Payne Smith and Douglas by line, but neither file is in `sources`. `Card_Edits.md` says "every file already listed"; that is wrong for these two. Append to `sources.about`, after the Michael the Syrian entry:

Old text: (none)

New text:
```json
{
  "title": "The Third Part of the Ecclesiastical History of John, Bishop of Ephesus, translator's preface",
  "author": "R. Payne Smith",
  "date": "1860",
  "language": "English",
  "file": "cic/texts/john-ephesus_ecclesiastical-history-part3_paynesmith1860.txt"
},
{
  "title": "Relations with Mar Ignatios, The Christian East, volume 3, number 1",
  "author": "J. A. Douglas",
  "date": "1922",
  "language": "English",
  "file": "cic/texts/christian-east_v3-no1-march-1922.txt"
}
```

**2. `legacy.traces[2]`: a modern date is given as the chronicle's.** The chronicle gives no year for the Henotikon (no year near Zach 5170-5194 or 5900-6200). "482" is Walford's running head, Evag-E 5875: "HENOTICON OF ZENO.—A.D. 482." This is the same defect the pass fixed for Timothy's 475.

Field `legacy.traces[2]`.
Old text: `The Syriac chronicle says Peter Mongus of Alexandria, about 482, accepted the emperor Zeno's Henotikon, a letter of union that anathematized Nestorius and Eutyches.`
New text: `The Syriac chronicle says Peter Mongus of Alexandria accepted the emperor Zeno's Henotikon, a letter of union that anathematized Nestorius and Eutyches.`

Field `uncertain`, appended after the Payne Smith and Douglas entry.
Old text: (none)
New text: `The year of Zeno's Henotikon, 482, is a modern date, Walford's, from his running head (Evagrius, line 5875). The Syriac chronicle gives no year for it.`

Run `tools/validate-census.mjs` again after both changes.
