# Frumentius: card check, the modern pass (2026-11-23)

Checked `frumentius.card.json` against `Card.pass3.json`, the **Fourth pass: no modern opinion (2026-11-23)** edit list in `Card_Edits.md`, and `frumentius.brief.txt` as it now stands. Every cited line was opened.

**Verdict: FIX** (one change).

## The change

1. **`legacy.remembered[2]`.** The fifteenth-century date is Enno Littmann's (Geschichte der äthiopischen Litteratur, 1907), as Budge reports it (SYN1 1087-1094). "Its editors' dating" credits no one by name and does not mark the date as modern.
   - Old: "The Ethiopian book of saints, put into Ge'ez in the fifteenth century by its editors' dating, keeps his day on 26 Hamle"
   - New: "The Ethiopian book of saints, put into Ge'ez in the fifteenth century by the modern dating of Enno Littmann, which Budge reports, keeps his day on 26 Hamle"

## Checked and sound

- **Edit 1** (`uncertain[1]`, "These are modern editors' judgments..."): Robertson following Gwatkin, N204 5674-5684; the earliest date at the end of 346, N204 10381, 10405-10408; Valesius, N202 4294-4296; Rufinus's "nuper", RUF 27374. No old source gives another date. Sound.
- **Edit 2** (Fremantle, "probably 401"): N203 44550-44552. Credited by name and marked modern. Sound.
- **Edit 3** (Ethiopia and Eritrea): the census region and description (world-census.json 36261, 36302). The brief now says only "in what is now Ethiopia". Sound.
- **Edits 4 and 5** (Rufinus's preface and Prosper): RUF 26045-26047 ("diruptis Italiae claustris Alarico duce Gothorum"); Prosper 53486-53488 (a. 400, "Gothi Italiam Alarico et Radagaiso ducibus ingressi"). Prosper's file is now in `sources.about`. Sound.
- **Edit 6** (Robertson's prolegomena removed from `briefReferences[3]`): the Arians and the charges rest on Athanasius. Sound.
- **Edit 7** (`briefReferences[4]`, the Alexandrian index): N204 64079-64081 (Januarius and Justus); N204 64351-64362 (13 to 14 Mechir, 356). Sound.
- **Edits 8 and 9** (`briefReferences[5]`, and the census reference removed): SYN 18812-18830 (Cosmas consecrates Peter for Ethiopia); SYN 25056-25069 (Michael "cannot appoint another bishop without the command of the archbishop"). The brief no longer says the church of Aksum kept taking its bishops from Alexandria. Sound.
- **Nothing else moved.** Outside the nine listed edits, the card is word for word `Card.pass3.json`.
- **`briefReferences`.** Every entry names something the brief still tells. "The bishop George" in `briefReferences[2]` names the source's bishop, who is the brief's "emperor's bishop in Athanasius's place" (N204 36145-36146). It is not quoted wording, so it stands.
- **Quotations.** There are four quoted spans and four `quotationOriginals`, each unchanged. Each `printed` is verbatim: RUF 27376-27377 and 27383-27385; N204 36144-36145 and 36150-36151. Migne's Greek is at 92806-92807 and 92812-92814.
- **Other modern views.** Each is credited by name to its modern source, and each source is identified as a modern editor, translator or reconstruction: Hartranft and the Dictionary of Christian Biography (N202 29919; N203 7768); Ludolf, 1681; Jackson; Mingana; Valesius and Zenos; Robertson's 356 to 357 (N204 7299) and 346; Littmann's stone match ("a modern reconstruction"); Robertson on the Arians.
- **Rules.** No audit is named, the spelling is American, and the keys are the census keys.
