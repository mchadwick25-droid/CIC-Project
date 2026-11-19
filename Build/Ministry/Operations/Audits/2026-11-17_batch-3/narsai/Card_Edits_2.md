# Card edits 2: Narsai of Nisibis

Starting card: the census's current `card` object for `narsai` (`cic-website/data/world-census.json`). Written to `narsai.card.json`, overwriting the old batch card.

## Edits

- **`briefLength` left out.** The old batch card carried `"briefLength": "about 2 minutes 45 seconds"`; the census check does not accept the key.
- **`briefReferences` replaced.** The thirteen old lines (for the previous brief) are replaced by sixteen plain-text lines for what the new brief draws on, each with file and lines re-read: History 36830-36839, 31574-31577, 36179-36180, 36684-36698, 36700-36705, 37307-37335, 37409-37412, 37453-37462; Cause 17457-17460, 20482-20491, 20547-20560, 20611-20617, 20690-20693, 20739-20747, 20813-20815, 20827; Connolly 253-260, 6857-6858; Guidi 9884-9888, 9948-9952, 9982-9995; Bar Hebraeus 4554-4557; Junillus 22735-22738; the census. No quotation marks inside them. Dropped from the old list because the new brief no longer uses them, or because the outline now holds them otherwise: the succession "after him Elisha, then Abraham" (order Contested, Source_Sheet D7; the brief says only that Abraham later led the school); Simeon's "Leper" letter and the Chronicle of Edessa's 489 closure (not in the new brief); Connolly's note that his friends called him "The Harp of the Holy Spirit" (Outline_Check_2 M4: an editors' name, not his friends' in his lifetime; not in the new brief).

## Quotations

- `quotationOriginals`: both entries kept unchanged. The new brief quotes exactly these two spans and no others (script check: no quoted span missing, no entry unquoted). `printed` re-checked against Cause 20743-20746 and Connolly 6857-6858: both found verbatim. `secondReading` kept as the existing values ("same").

## Checked against the outline's new findings, no change needed

- Forty-seven printed, not surviving: the card says only that Ebedjesu credits him with 360, as Connolly reports, and that the Library holds four in English (`keyWorks[0]`). It never says forty-seven survive. Holds.
- Abraham as the only kinsman: the card names no kinsman outside the old `briefReferences`, now replaced. Holds.
- "Harp of the Holy Spirit": not on the card outside the old `briefReferences`. Holds.
- "Trained the Church of the East's teachers": the card does not say it. `knownFor` says he founded with Barsauma "the school of the Church of the East", which Outline.md's census check marks held (E3, E4, E6-E8, I1). `legacy.traces[1]` is Connolly's own words, credited (Connolly 4486). Holds.
- `datesNote` and `uncertain[1]-[2]` agree with the brief (457 or after 471; early 500s) and with D1-D2.

## Claims not found

None new. The earlier note stands: `legacy.remembered[1]`, "a long fight against Satan", is supported only loosely (History 36639-36643, 36427).

## Other fields

All other fields word for word as the census card.
