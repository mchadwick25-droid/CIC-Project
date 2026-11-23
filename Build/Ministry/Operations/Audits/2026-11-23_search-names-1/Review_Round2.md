# Search names batch 1: review, round 2 (Opus, 2026-11-23)

Targeted recheck. Only what changed since round 1 was checked, against round 1's three findings. Each new basis was re-read by script against `cic-website/data/world-census.json` → `movements[id = entry]` → dotted field.

## Row count

`cic-website/data/search-names.json` now has 27 rows. No row names "Greek Orthodox Patriarchate of Antioch" or "Asia Minor", and neither string appears anywhere in the file. Both are held in `Wanted.md` with the reason from round 1.

## Findings from round 1

**A. Greek Orthodox Patriarchate of Antioch: resolved.** The row is out of the file. `Wanted.md` holds it for Mark's ruling on a contested heir, citing the entry's own "so the line is disputed" and its Contested descent confidence. No Melkite row was added.

**B. Asia Minor → Turkey: resolved.** The row is out of the file. `Wanted.md` holds it, saying the basis places a region inside a country and does not make Asia Minor an older name for Turkey.

**C. Rows for Jerusalem and the Latter-day Saints: resolved.**
- Greek Orthodox Patriarchate of Jerusalem: the basis is now `livingEvidence.basis`, "The church of Jerusalem is alive today as the Greek Orthodox Patriarchate". It appears word for word. The sentence says this entry's church lives on as that patriarchate, and "of Jerusalem" comes from the same sentence. The entry's descent confidence is Widely Accepted, so the row does not hide a dispute.
- Church of Jesus Christ of Latter-day Saints: the basis is now the full citation in `livingEvidence.evidence`, through ": own-voice; verified." It appears word for word. It shows the name is the church's own, used by its own newsroom. Round 1 also suggested pairing it with the basis sentence. A row holds one basis, and the citation supports the row by itself, so leaving the pairing out is not wrong.

No findings.
