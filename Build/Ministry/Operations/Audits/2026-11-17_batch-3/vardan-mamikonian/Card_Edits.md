# Card edits: Vardan Mamikonian

Every field of `vardan-mamikonian.original.card.json` is kept word for word, in its order. Nothing was corrected.

L12 = `cic/texts/langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`; N = `cic/texts/eghishe_history-of-vartan-and-the-armenian-war_neumann1830.txt`; O = `cic/texts/ormanian_church-of-armenia_gregory1912.txt`.

## New

1. `briefLength`. Old: none. New: "about 3 minutes 15 seconds". Evidence: the brief is 492 words by the profiler (Review.md), 495 by `wc`, at about 150 words a minute (`roles/writer.md`).
2. `sources.about`, a fourth entry. Old: none. New: Langlois, Collection, tome II, Elishe in French and Lazar of Pharp, file L12. Evidence: all three quotes are cited from this file's lines. The card's existing Lazar entry points to the other scan of the same printing (`langlois_collection-historiens-armenie-tome2-fra_1869.txt`) and stays as it was.
3. `quotationOriginals`. Old: none. New: three entries, each `modern` matching the brief word for word:
   - Lazar on his name: L12 91072-91076, re-read. OCR fault kept: "parini".
   - Vardan before the king (Lazar): L12 90623-90626, re-read.
   - Vardan to his army before Avarayr (Elishe, French): L12 82667-82673, re-read. OCR faults kept: "ua", "nous.le", "ordresiniques", "estle". Neumann's differing English noted from N 3930-3933, re-read.
4. `briefReferences`. Old: none. New: seventeen entries for what the brief draws on. Lines re-read: L12 91056-91076, 87726-87729, 87776-87779, 90889-90891, 90618-90626, 90690-90698, 90795-90799, 90958-90966, 91122-91126, 80463-80471, 91615-91625, 95201-95205, 95332-95334, 95976-95983, 99484-99498, 100500-100512, 100549-100552, 99215, 87287-87289, 92126-92128, 82667-82673, 92384-92387; N 1116-1118, 1470-1473, 2204-2209, 2372-2383, 2402-2421, 2444-2446, 2647-2659, 2890-2893, 2957-2961, 4162-4166, 4175, 4227; O 2254-2262, 2287-2294.

## Left alone (checked, not wrong)

- `datesNote`, `uncertain[1]`: 26 May 451 (O 2256), 2 June in Neumann's margin (N 4147) and in a note to Lazar (L12 92368-92370). Hold.
- `otherNames[1]`: "Vartan le Grand" in a note in Lazar's introduction (L12 89063-89064). Holds.
- `legacy.traces[0]`: the title (N 1-2) and the dedication to David, "which thou hast requested" (N 1033-1035; L12 78263-78266). Holds.
- `legacy.traces[1]`: 1,036 (N 4227; L12 92386-92387). Holds.
- `legacy.remembered[1]`: O 2263-2265, 8564-8565. Holds.
- `uncertain[2]`: the brief also gives Elishe's Vardan saying "we deceived that unjust prince". That is the princes' "we", not his personal yielding, which the outline keeps as Lazar's alone. Not contradicted.
- `uncertain[3]`: Lazar (L12 90889-90891) and Neumann's preface (N 572-574). Holds.

## Not found

None.
