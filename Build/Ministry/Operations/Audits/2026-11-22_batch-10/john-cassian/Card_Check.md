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
