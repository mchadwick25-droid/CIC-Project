# Card check: Hild of Whitby (batch 4)

**Verdict: FIX** (three changes below).

## 1. Edits justified

All eight listed edits hold against the brief and the files.

- Kept quote: Plummer 24946-24948 and Giles 10973-10975 stand verbatim as printed.
- Removing the "Mother" quote is right. The brief now says it without quotation marks.
- Edits 3-8 match the brief's sentences. The steward, Gaul, "built or set in order", Oftfor, III.24 and the Humber are all gone from the brief, so they were rightly dropped.

## 2. Nothing else moved

I diffed the card against the census `card` for `hild-of-whitby`. Only `briefReferences` and `quotationOriginals` differ, exactly as `Card_Edits.md` lists. Every other field is word for word.

## 3. References that remain

1. IV.23: birth, Edwin, Paulinus, thirty-three years, Aidan and the East Angles, Hartlepool, Whitby, peace and charity, goods shared, no one rich or poor, Scripture, advice-seekers, five bishops, Mother, fever, cockcrow. All of it is in the brief.
2. III.25: the synod paragraph. All of it is in the brief.
3. IV.24: Caedmon. All of it is in the brief.
4. V.24: about fifty years. This is in the brief.
5. "Bede on the Scots from Ireland and Aidan from Iona (Hii)." **The Aidan part fails.** The brief names Aidan only as the one who called her home from the East Angles. It never says he came from Iona. It does tell the Irish monks of Iona, "whom Bede calls the Scots". See FIX A.
6. World census: two missions, converted within living memory. This matches "faith from Rome and from the Irish monks of Iona" and "the English church was still young".

## 4. Census rules

- Keys are allowed and there is no `briefLength`.
- The brief has one quoted span and the card has one entry for it.
- Both cited files are in `sources`.
- There are no quotation marks in `briefReferences`.
- No audit is named, and the spelling is American.

## 5. The "not found" claim: "In those days a bishop led the church of a whole region"

**Ruling: it is held. The Source Sheet does not carry it, but the vendored Bede does.**

- **III.21.** Giles 7426-7431: Diuma "was made bishop of the Midland Angles, as also of the Mercians ... for the scarcity of priests was the occasion that one prelate was set over two nations." Plummer 20711-20714: "Paucitas enim sacerdotum cogebat unum antistitem duobus populis praefici" (OCR "eiiim", "i^raelici").
- **IV.12.** Giles 9874-9880 tells that after Wilfrid was driven out, two bishops were set "to preside over the nation of the Northumbrians, namely, Bosa, to preside over the nation of the Deiri; and Eata over that of the Bernicians". Plummer 23690-23696 has the same. Bosa is the first of Hild's five bishops (Giles 10975).
- **IV.5, the synod of Hertford, canon IX.** This supports "the English church was still young". Giles 9358-9360: "more bishops should be made, as the number of believers increased; but this matter for the present was passed over." Plummer 23031-23033: "Ut plures episcopi crescente numero fidelium augerentur".

Bede never states the rule in general terms. Still, these lines show a bishop set over a whole people or province, and a young church with too few bishops. The brief's sentence fairly sums up what they show. It needs no replacement and should not be cut. The card should carry the reference (FIX B) and cite the chapters in `sources` (FIX C). The Source Sheet should also gain these lines. That is noted here for the sheet's owner; this check does not make that edit.

## FIXes

**A. `briefReferences[4]`**
- Old: `Bede on the Scots from Ireland and Aidan from Iona (Hii).`
- New: `Bede on the Scots from Ireland and Iona (Hii).`

**B. `briefReferences`: insert a new entry after index 4, before the World census entry**
- Old: (none)
- New: `Ecclesiastical History III.21, IV.5 and IV.12 (Giles 7426-7431, 9358-9360, 9874-9880; Plummer's Latin 20711-20714, 23031-23033, 23690-23696): one bishop set over the Midland Angles and the Mercians for want of priests; the synod of Hertford putting off the making of more bishops as believers increased; Bosa, one of her five, set over the nation of the Deiri.`

**C. `sources.about`**
- `[0].title`
  - Old: `Ecclesiastical History III.24-25, IV.23-24 and 26, and V.24 (tr. J. A. Giles, ed. L. Cecil Jane, with his notes)`
  - New: `Ecclesiastical History III.21, III.24-25, IV.5, IV.12, IV.23-24 and 26, and V.24 (tr. J. A. Giles, ed. L. Cecil Jane, with his notes)`
- `[1].title`
  - Old: `Historia ecclesiastica gentis Anglorum III.24-25 and IV.23, in Venerabilis Baedae Opera historica, volume 1, with Plummer's Introduction`
  - New: `Historia ecclesiastica gentis Anglorum III.21, III.24-25, IV.5, IV.12 and IV.23, in Venerabilis Baedae Opera historica, volume 1, with Plummer's Introduction`

The brief is unchanged.
