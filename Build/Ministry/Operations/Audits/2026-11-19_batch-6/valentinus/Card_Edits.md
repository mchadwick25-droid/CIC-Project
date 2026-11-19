# Card edits: Valentinus

Card: `valentinus.card.json`. Base: the census card for `valentinus` (same as `Card.existing.json`). Every other field is kept word for word.

## New

1. **keyWorks**, added entry. Old: (none). New: `{"title": "A sermon", "about": "known only from a passage Clement of Alexandria quotes in his Stromata, Book 4"}`. Evidence: brief, "In a sermon, Valentinus told his hearers they were immortal from the beginning"; CL (`anf02_...clement-alexandria.xml`) 39090–39096, *Stromata* IV.13, "Valentinian, in a homily, writes in these words".
2. **sources.ownWords[0].title**. Old: "Fragments of his letters, in Clement of Alexandria, Stromata, Book 2". New: "Fragments of his letters and a sermon, in Clement of Alexandria, Stromata, Books 2 and 4". Evidence: as edit 1; the brief quotes the sermon.
3. **sources.about, Clement title**. Old: "Stromata, Books 2 and 7". New: "Stromata, Books 2, 4, 5 and 7". Evidence: brief, "Clement answered that this made some people saved by their nature, not by Christ's coming"; CL 39096–39098 (IV.13, "supposes a class saved by nature") and CL 40954–40960 (V.1, "saved by nature ... apart from the Saviour's appearance").
4. **sources.about**, added entry: Tertullian, "Against the Valentinians 4, Latin, ed. Emil Kroymann, CSEL 47", Latin, `cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt`. Evidence: the brief's Tertullian quotation is rendered from this Latin (KR 9633–9634, 9652–9653), and "now nowhere" follows KR 9663 ("nusquam iam Valentinus").
5. **briefReferences**, added (7 entries): Clement II.20, IV.13 and V.1; Irenaeus III.4.3 and I.11.1; Tertullian *Against the Valentinians* 4 (Latin and ANF, with the editor's date, TE 42916); *Prescription* 30 (TE 21336–21338); Hippolytus VI.29 (HIP 9166–9173) and VI.35 (HIP 9643–9661); and the census tradition entry `valentinian-and-other-gnostic-christianities` ("known almost entirely through such opponents", and the 1945 find). No quotation marks used.
6. **quotationOriginals**, added (4 entries, one per quoted span in the brief), each line re-read in its file:
   - "It is unclean, the home of many demons. But when the Father, who alone is good, visits it, it is made holy and shines with light." Printed: CL 34300–34302, "being unclean, and the abode of many demons. But when the only good Father visits it, it is sanctified, and gleams with light."
   - "Valentinus had hoped to become a bishop ... the church of the true rule." Printed: TE (`anf03_tertullian.xml`) 43109–43114, ANF English. The rendering is from the Latin, KR 9633–9634 and 9652–9653, given in the entry's `uncertain` note, since the file divides it with a page break and the editor's apparatus (lines 9635–9651), so it cannot stand as one `original` span.
   - "love is not love unless there is something to love." Printed: HIP (`anf05_...novatian.xml`) 9171–9172, "love is not love except there may be some object of affection."
   - "death may die in you." Printed: CL 39093, "death may die in you and by you".

## Awaiting second reading

All four quoted spans are new (the census card had no `quotationOriginals`), so none has a `secondReading`:

- "It is unclean, the home of many demons. ..." (CL 34300–34302)
- "Valentinus had hoped to become a bishop, ..." (TE 43109–43114; Latin KR 9633–9634, 9652–9653)
- "love is not love unless there is something to love." (HIP 9171–9172)
- "death may die in you." (CL 39093)

## Clearly wrong

7. **uncertain[4]**. Old: "No source we hold says where he was born." New: "No early source we hold says where he was born." Evidence: HOLL (`epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt`) 28941–28948, *Panarion* 31.2: Epiphanius, about 375, reports that some said he was born a Phrebonite on the Egyptian coast, while noting that most do not know. A held source does name a birthplace, as hearsay; no early one does.

## Not found

None. Every other card statement was found: Irenaeus I.11.1 (IR 31519–31521), III.4.3 (IR 39968–39970); Tertullian *Prescription* 30 (TE 21332–21338) and *Against the Valentinians* 4 (TE 43117–43128); Hippolytus VI.42 (HIP 10054–10059) and note 736 (HIP 10059–10065); Clement VII.17 (Theudas, CL 52962–52963).

## Note for the census step

The validator requires `secondReading` on every `quotationOriginals` entry, so the card passes only once the second-reading step fills the four above.
