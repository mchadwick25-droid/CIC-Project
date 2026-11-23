# Frumentius: card check, third pass (what it was about), 2026-11-23

**PASS.**

Checked `frumentius.card.json` against `Card.pass2.json`, the edit list in `Card_Edits.md` ("Third pass: what it was about (2026-11-23)") and `frumentius.brief.txt` as it now stands.

1. **Nothing else moved.** A key-by-key diff of the two cards shows exactly the five listed edits: two new `uncertain` items, the shortened Socrates/Sozomen/Theodoret `briefReferences` entry, the new Arius/Athanasius `briefReferences` entry, and the Ludolf `briefReferences` entry removed. Every other field is word for word.
2. **Each edit justified; every cited line opened.**
   - N204 35938-35940: "their Churches were given up to the professors of Arianism". Holds.
   - N203 6043-6047: "the Son has a beginning, but that God is without beginning"; "subsisted before time" supports "before all time". Holds.
   - N204 19675-19680: "from the essence of the Father ... One in essence with the Father". Holds.
   - N204 34917-34924: the first charge, setting Constans against Constantius, called slander. N204 35099-35104: the second charge, letters to "the tyrant" Magnentius, called calumny. Holds.
   - N204 5741-5744: the Nicene formula rejected "in the East generally, except where the bishops were positively Arian". Supports the new `uncertain` item. N204 5748-5752: Constans murdered in 350, Magnentius's bid for Egypt. Holds.
   - N204 36151-36153: "he has not been able fairly to clear himself of any of the charges". Supports the third `uncertain` item.
   - All three files are already in `sources.about` (N203 and N204 by file).
3. **briefReferences.** The Ludolf count and Valesius's "almost word for word" are gone from the brief; the edits remove them from `briefReferences`, and both stay held in `legacy.traces` and `uncertain[0]`. Every remaining entry names something the brief still tells.
4. **Census rules.** The keys are unchanged. The brief has four quoted spans, matching the four `quotationOriginals` entries word for word, none dropped or added. No audit, review or ruling is named. Spelling is American.
5. **"checked at card".** No quotation under six words; none to check.
6. **Not found / clearly wrong.** None found.
