# Card check: John Cassian (`john-cassian`)

**Verdict: FIX** (one finding, two edits)

## What holds

1. Edits justified. All four `quotationOriginals` match their files and lines word for word: N211 38028-38030, N211 15774-15775, N203 43669-43671, N211 25949-25952. The new legacy traces hold at their lines: Gregory of Tours (GT-E 22152-22155), Victor of Martyrites (N211 16004-16007), the Gallic Chronicle at 429 (MOM 71060-71062, damaged print, and the card says so), and the Philokalia heading ΚΑΣΣΙΑΝΟΥ͂ ΤΟΥ͂ ΡΩΜΑΙΟΥ͂ … ΠΡῸΣ ΚΑΣΤΌΡΑ (philokalia v1 6184-6190, read by hand). The new uncertain entry on the Cursus tract holds too (BANG 1581, 1610-1623; "beatum Honorium", "corrupt text", "eighth century continental Scotic monk").
2. Nothing else moved. A JSON diff against `Card.existing.json` shows only the additions listed in `Card_Edits.md`.
3. Each `briefReferences` entry matches something the brief tells. No entry is stale, and no quotation marks are used.
4. Census rules: only allowed keys, one `quotationOriginals` entry per quoted span (four spans, four entries), each file listed in `sources`, no audit file named, American spelling. The under-six-word span carries "checked at card".
5. "the Conferencer" / "Contra Collatorem": Gibson glosses it "against the author of the Conferences" (N211 15775). The rendering holds, and the card says "the Conferencer" is our English for it.

## Finding: `uncertain` entry 5 misleads

The card says Gibson notes "that Prosper joins the two names". The words are Gibson's (N211 15040-15042, citing "Chronicle"). But Mommsen prints the line, "Iohannes monachus cognomento Cassianus Massiliae insignis et facundus scriptor habetur", under "VI. Interpolationes Prosperi chronicis insertae saec. XV" (MOM 56178-56179, 56423-56425). He says he sets these additions out "ne fallerent deinceps, ut adhuc saepe fefellerunt" (so that they no longer mislead, as they have often misled) (MOM 56194-56197). Prosper's genuine Chronicle in the same edition never names Cassian. A reader would take Prosper, his contemporary, as an early witness to the name John Cassian. A held source says he is not. Crediting the claim to Gibson does not stop it misleading, because the card states the claim without its contradiction. That is a disputed claim presented as settled, so it is clearly wrong under the card rules. The fix keeps Gibson's words and adds the held correction. The Latin is not quoted because the scan is damaged ("lohannes nionachus").

**Edit 1.** Field `uncertain`, entry 5.
- Old: `Gibson notes that the monks of Egypt called him John in his own writings, and that Prosper joins the two names. Gennadius calls him only Cassianus.`
- New: `Gibson notes that the monks of Egypt called him John in his own writings, and that Prosper joins the two names. But Theodor Mommsen prints the line Gibson means, which calls him John surnamed Cassian, among fifteenth-century additions to Prosper's Chronicle, not Prosper's own words. Gennadius calls him only Cassianus.`

**Edit 2.** Field `sources.about`, the Mommsen entry `title`, so the source list names what the card now draws from this file.
- Old: `Gallic Chronicle of 452, in Chronica Minora I, edited by Theodor Mommsen`
- New: `Gallic Chronicle of 452 and the fifteenth-century additions to Prosper's Chronicle, in Chronica Minora I, edited by Theodor Mommsen`

Log both in `Card_Edits.md` under "Clearly wrong", with the evidence MOM 56178-56179, 56194-56197, 56423-56425, and remove the "needs a ruling" note.

## Not found

The writer listed no claim as not found. The Palladius note (PAL 2641, 2661-2669) is correctly given as the editor's. No other clearly wrong statement is left in.

## Second pass check (2026-11-23)

**Verdict: FIX** (one edit)

1. Checker changes. Both went in word for word (`uncertain` entry 5; Mommsen `title` in `sources.about`). A diff of the card at commit ac5e90be (the checked card) against now shows nothing else moved in those fields. The "needs a ruling" note is gone from `Card_Edits.md`.
2. Additions.
   - `keyWorks`, Conferences `about`: holds. Gibson gives Conferences I-X to "Leontius, Bishop (probably) of Fréjus, and Helladius, who is termed 'frater'" (N211 15535-15538), Part II to Honoratus and Eucherius, Part III to Jovinian, Minervius, Leontius and Theodore (N211 15546-15558). The preface itself has "blessed Pope Leontius, and holy brother Helladius" (N211 25897-25902). Gibson is credited. "Provence" rightly left out.
   - `legacy.traces`, Philokalia preface: the preface is credited and the rest holds against philokalia v1 6136-6175, read by hand ("ὁ περὶ τῶν ὀκτὼ λογισμῶν, καὶ ὁ περὶ διακρίσεως ὧδε ἐτέθησαν"; the scan's "χθ΄" is its usual χ-for-κ error, as in "χαὶ", so κθ΄, the twenty-ninth). But the preface says only "ὁ σοφώτατος Φώτιος" (6148-6149). "of Constantinople" is not at the lines.
3. Outline "card" items: the Cursus tract, the Gallic Chronicle, "the blessed Cassian" (N211 15944-15948), Gregory of Tours, Victor's recension, the Philokalia and the dedications are all on the card. The skips hold: the Benedict of Aniane hits are Migne's notes in a damaged scan (e.g. 58855-58909), with no line of Benedict's own cited; Isidore's hits are Arevalo's notes; Photius's codex is not held. Cut first 3 and 4 are Leave out.
4. Scan readings: none listed, and the first check gave none.
5. No new keys, American spelling ("honors"), no audit named.

**Edit 1.** Field `legacy.traces`, last entry.
- Old: `and says Photius of Constantinople mentions them.`
- New: `and says the most learned Photius mentions them.`


Coordinator (2026-11-23): the second pass check's edit applied word for word (`legacy.traces`, last entry: "Photius of Constantinople" → "the most learned Photius").
