# R3 recheck: nine Who profiles, era 2 batch 4

Scope: round 3, the last allowed. A targeted recheck of the round 2 changes only (`git diff 98e841eb e971c997` on `era2/batch4/`), against `R2_recheck.md` and `R2_changes.md`. Seven files changed: two briefs, their two audio scripts, two cards and the batch README. No records.json file changed. Unchanged text was not re-reviewed. Each changed line was read as a word diff, and each changed sentence and quotation was opened at its line in the vendored file to confirm who is speaking. No drafts were edited and no paid, model or web calls were made.

## 1. The R2 blocking findings

None were raised in R2.

## 2. The R2 minor findings

| Finding | Status | Check against source |
|---|---|---|
| N1 Palladius, brief l.5: "takes him for John Chrysostom" | RESOLVED | "W. K. Lowther Clarke, its translator, takes this John for John Chrysostom, bishop of Constantinople." The words "having become embroiled in the disturbance connected with the blessed John" are Palladius's own, in the first person of the Lausiac History (`palladius_lausiac-history_clarke1918.txt` l.427), and Clarke's note 238 on them reads "Chrysostom" (l.1113). The referent is now the John of the quotation, not Palladius. |
| N2 Palladius, brief l.9: the frame sentence settled the identification | RESOLVED | "Foes in the quarrel over Origen attacked a Palladius." The frame no longer prejudges the dispute. The sentences after it are unchanged and still give the identification to the notes to Fremantle's edition and Tillemont's doubt (npnf206 l.42611–42618). "Of Alexandria" was dropped after Origen (see §3). |
| N3 Honoratus, brief l.9: "Arles called him", with Hilary nearest | RESOLVED | "Later, Arles called Honoratus to be its bishop." Same word count, 325. |
| N4 Pelagius, card uncertain #1: 43-word sentence | RESOLVED | Now three sentences: "…his story comes through Augustine of Hippo and Jerome of Strido. Augustine appealed to Jerome, who wrote against him too. It also comes through modern editors who take Augustine's side, such as B. B. Warfield." Fremantle's Prolegomena, in his own voice: "Augustin from Africa and Ctesiphon from Rome appealed to him (272, 280) … and at length Jerome himself felt compelled to take the pen" against the Pelagians (npnf206 l.1712–1715). The claims are those R2 checked; only the sentence breaks are new. "Him" in "wrote against him too" falls on Pelagius, the card's subject, with "too" pointing back to Augustine. |
| N5 Cassian, card uncertain #1: Gibson's gloss on Photius dropped | RESOLVED | "Gibson adds that Photius of Constantinople calls him a Roman, which \"need mean no more than born within the Roman Empire\"." Gibson: Photius "calls him ῾Ρωμαῖος, which need mean no more than born within the Roman Empire" (npnf211 l.14992–14995). The quotation is exact and is Gibson's voice, not Photius's. The card parses as JSON. |
| N6 README: "by Fremantle's and Richardson's notes" | RESOLVED | "Rufinus died in 410 by the notes to Fremantle's edition of Jerome and by Richardson's note." This follows the batch's rule for the npnf206 endnotes (Fremantle's preface, l.492–494). |

## 3. The one drafter's choice beyond the fixes

- **"Origen of Alexandria" cut to "Origen" (Palladius brief).** Accepted. The drafter's stated reason, that no one else in the brief shares the name, is not the pattern's test; the test is whether the name could mean more than one person, and whether a general listener has context. Origen is not a shared name in the sources, the brief gives context in the same paragraph ("the quarrel over Origen", "the heresy of Origen"), and era 2 batch 3 cleared the same bare first mention in the Epiphanius of Salamis brief. Nothing is wrong or misleading. The Palladius card is unchanged.

## 4. Gates on the changed briefs

| Brief | Words | Cap | FK | Flesch | Audio = brief less `[calmly] ` and one `[warmly] ` |
|---|---|---|---|---|---|
| Palladius of Helenopolis | 327 | ~325 | 7.4 | 60.6 | Yes |
| Honoratus of Arles | 325 | 325 | 6.7 | 69.2 | Yes |

Both pass (FK at most 10, Flesch at least 60). Each script carries one `[calmly]` and one `[warmly]`, the latter before the closing sentence. Palladius sits near the Flesch floor and within "about 325", as R2 accepted. Both changed cards parse as JSON.

## 5. New findings

None. The changed text adds nothing wrong, unsupported, misleading or not verbatim, and no witness swap or new wrong attribution was found.

## Verdict

N1 to N6 are all resolved and hold against the sources. The one further trim is accepted. No new finding. The batch clears review at round 3.
