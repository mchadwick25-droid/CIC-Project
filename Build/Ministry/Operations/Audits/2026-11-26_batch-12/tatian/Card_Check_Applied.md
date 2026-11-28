# Card check applied: Tatian

| Change | Where it went | Result |
|---|---|---|
| FIX 1 | `tatian.card.json`, `quotationOriginals[0].uncertain` | applied |
| FIX 2 | `tatian.card.json`, `quotationOriginals[1].uncertain` | applied |
| FIX 3(a) | `tatian.card.json`, `timeline` line "Later writers of the Church of the East say Ephrem, a deacon of Nisibis, commented on it.", `reference` extended with the Chronicle of Edessa part | applied |
| FIX 3(b) | `tatian.card.json`, `sources.about`, new entry "Chronicle of Edessa, section 30" right after "The Doctrine of Addai" | applied |
| FIX 4 | `Card_Edits.md`, new heading "Entry fields (card check)", `modernWorks` note for `Corpus Apologetarum Christianorum saeculi secundi 9` | applied (entry field, written for release) |

Every old text was found once, as quoted.

JSON check: `python -m json.tool tatian.card.json > /dev/null` passed.

Readability score: not run. `Card_Edits.md` names `python -m engine.m1.profile_readability`, but that tool scores profile briefs, not card running text, and no card-scoring command is given.
