# Card check: Cyril and Methodius

I compared the new card `cyril-and-methodius.card.json` with `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch9/cyril-and-methodius.card.json`. I checked every changed, added or removed claim against `Source_Sheet.md` and the cited lines, and re-read all seven quotations in their files.

**Verdict: FIX** (one blocking finding)

## Quotations

| # | Modern (matches brief) | Printed wording re-read | Result |
|---|---|---|---|
| 1 | "if they have letters for their language." | VC 20224–20225, "si litteras habent linguae suae accomodatas" | Verbatim |
| 2 | "who can write words on water, and who wants to be called a heretic?" | VC 20227–20228, "quis potest in aqua orationem scri-/bere, et quis vult haeretici sibi nomen comparare?" | Verbatim, with the line-break hyphen joined |
| 3 | "Does God's rain not fall on all alike? ... blind and deaf." | VC 20307–20310, "nonne pluvia a deo aequa-/liter ... caecos et surdos esse iubentes ?" | Verbatim. Every clause is rendered |
| 4 | "Look, brother, we were partners ploughing a single furrow. ..." | GZ 12251–12253, "Ecce frater nos consortes eramus, ... diem / meum terminavi," | Verbatim |
| 5 | "Greek", with his "newly invented Slavic letters", had partly cheapened ... | GZ 13641–13643, 13662–13663 | Verbatim, OCR kept, footnote marker left out. "partly" (ex parte) is kept, as Do not say requires |
| 6 | "he who made the three chief languages ... for his praise and glory." | GZ 13974–13976, "qüoniam qui fecit tres linguas principales, bebream ..." | Verbatim |
| 7 | "the first bishop of the Bulgarian tongue" | PG 99371–99372, "Bulgariez lingue Clemens / primus constituitur episcopus" | Verbatim |

Each modern wording matches the brief exactly.

## Changed claims

The following are supported:
- role: Methodius governing a Slavic district (VM 12150–12151); Constantine teaching philosophy, a monk only at the end (M1, M11).
- place: Thessalonica (S2), Constantinople, Venice (VC 20292), and Rome with the church of St Clement (VC 20441–20445).
- dates: Lützow's 862 (LUT 1297), the census's 863, death aged 42 in 6377 (VC 20429–20431), the garbled VM year, and 885 (LUT 1479; GZ 6245).
- knownFor, keyWorks[0], and traces 0–3 (I1, I3; LCl 12972–12974; PG 98734–99594; RPC 7870–7873).
- remembered 1–3 (VC 20447; GZ 1532–1538; TH).
- uncertain 0–12 (D1–D11, M14, M16, I2, N3).
- The source list. All seven files exist.
- The brief references and their line ranges.

The brief has 450 words, so "about 3 minutes" is right. The hostile Salzburg complaint stays the Salzburg writer's, marked hostile. Ginzel's anti-schism stance stays attributed to him.

## The removals you asked about

The writer's reason, "not found in the files", is **not confirmed**. All three removed judgements are in the held files:

- **"Ginzel follows the Legend and calls the Life wrong."** Ginzel gives four and a half years in Moravia (GZ 3202–3203). His note 15 cites the Translatio "per annos quatuor et dimidium" and goes on: "Unrichtig ist die Angabe der pannonischen L. c. 5. Ac tribus annis elapsis ..." (GZ 3245–3249, Fraktur OCR "Unrid^tig ifl bie Eingabe ber ^ a n n n i f d^ e n ß.").
- **Wattenbach's doubt about the death date.** Ginzel's note 5 quotes Wattenbach (Beiträge S. 34) against the death day: "Es ist immer bedenklich, wenn der Todestag heiliger Männer mit einem hohen Feste zusammenfällt, wie hier in der Osterwoche". Ginzel then defends the date (GZ 6170–6180, Fraktur). He confirms the year 885 from Easter tables (GZ 6180–6190, 6245).
- **Wattenbach's "highly rated" judgement.** Dümmler's introduction says Wattenbach "glaubte ihren historischen Werth sehr hoch anschlagen zu müssen" (VC file 18108–18109). Ginzel quotes the same words from Dümmler (GZ 1817–1820).

These removals are not blocking. The new card says nothing these lines contradict. The new uncertain[0] gives the balance as "judged by their editors to be close to the events", against Ginzel's dismissal. The duration and death-date entries still state their facts plainly. The finding that led to the removals was wrong, though, and it should be corrected wherever it was recorded. A writer may restore the three judgements at these lines if wanted.

## BLOCKING

1. **keyWorks[1].about: "which Cross calls generally regarded as apocryphal" is misleading and ungrammatical.** "Which" follows "except Maccabees", so a hearer can take Maccabees to be the thing Cross calls apocryphal. Cross means the tradition of the six-month translation (RPC 5662–5666; sheet D5). Exact correction:
   - Replace: `it adds that Methodius later put the rest of the Scriptures, except Maccabees, into Slavonic in six months, which Cross calls generally regarded as apocryphal.`
   - With: `it adds that Methodius later put the rest of the Scriptures, except Maccabees, into Slavonic in six months. Cross says this six-month tradition is generally regarded as apocryphal.`

## Non-blocking

- uncertain[10] has Miklosich place the author "in the early tenth century". The Monitum says the author lived with Clement, who died in 916, and wrote while Hungarians raided Bulgaria in the 930s–960s (PG 96738–96746). "In the tenth century" would be safer.
- quotationOriginals[4].uncertain lists three OCR faults but not "aique", "liieras" or "lalinas". The printed text is right as it stands.
