# Census lineage rigor pass — drafting brief

You are drafting re-graded lineage links for the Church in Conversation world census
(`/home/user/CIC-Project/cic-website/data/world-census.json`, field `edges`). Repo root:
`/home/user/CIC-Project`. Read `CLAUDE.md` there first; its "Trust and source fidelity"
and "Accessible and rigorous" sections bind every word you write. Do NOT edit any file in
the repo. Write only your one output file.

## The six link types (decided; use exactly these strings)

Every link reads as a sentence: *from* [type] *to*.

| type | claim | to be Documented, a source must show |
|---|---|---|
| `gave rise to` | *to* emerged out of *from*'s people, communities or institutions | named people/communities passing from one to the other, in a dated text |
| `continued as` | the same community, carried into a later census entry (period split or rename) | continuity of the same community or see |
| `influenced` | ideas, texts or practices passed on, with or without contact or institutional ties | the later side using or naming the earlier one's work |
| `argued against` | *from* wrote or acted against *to*. The arrow runs FROM the critic. If both wrote against each other, that is two links | a text or act directed at the other by name |
| `broke with` | a rupture both sides recorded. Symmetric | dated rupture documents, ideally from both sides |
| `in contact with` | documented meeting or exchange, no influence claimed. Symmetric. Overlapping dates alone do NOT qualify | a named meeting, letter or shared event |

For the two symmetric types, put the two movement ids in alphabetical order (`from` < `to`).
Two links on one pair are allowed where both are true (e.g. Origen influenced Jerome's
circle AND Jerome argued against Origenism) — but only if each is separately evidenced.

## The five confidence grades (the project's vocabulary; exactly these strings)

`Documented`, `Widely Accepted`, `Dominant Modern Reconstruction`, `Contested`, `Inferential-Thin`.

**Grade the relationship the link claims, not the events the note mentions.** A canon that
names a party documents "argued against". "Direct continuation", "the same community",
"grew in its shadow" are interpretations even when every event behind them is attested.

What each grade must carry:
- **Documented** — at least one `primary` source with a locus in a vendored file under
  `cic/texts/`, with a verbatim quote from that file that shows the relationship itself.
  If the documenting text is not vendored, the link CANNOT be Documented: grade it at the
  highest level the vendored evidence supports and list the missing text in `wants`.
- **Widely Accepted** — a primary source for the underlying facts, plus at least one
  `secondary` work for the consensus reading.
- **Dominant Modern Reconstruction** — the secondary work(s) whose reconstruction it is. A
  single 19th- or early-20th-century account alone is Inferential-Thin; it is Dominant Modern
  Reconstruction only where a modern study already cited in the repo supports the same reading
  (2026-11-08, Decision-Log "Whole-set rulings").
- **Contested** — sources for each side; name in the note what the disagreement is.
- **Inferential-Thin** — the evidence it rests on, said plainly to be thin.

## Sources — the shape

```json
{"kind": "primary", "source_id": null, "work": "Gregory of Nazianzus, Letter 101 (To Cledonius)",
 "file": "cic/texts/<exact filename>", "lines": "1234-1236",
 "locus": "Ep. 101", "quote": "<verbatim from those lines>", "license": "public-domain"}
```

- `file` must be an existing file under `cic/texts/`. `lines` are 1-based line numbers in
  that file (a single number or `a-b`). Use `grep -n` to find them.
- `quote`: copied **character for character** from those lines (you may join a quote that
  wraps across lines with single spaces; do not change spelling, punctuation or archaic
  forms). Under ~40 words. Start and end at sentence or clause boundaries. No internal
  ellipses. A script will check every quote against the file; a quote that fails is a
  failed link.
- `source_id`: only if a world record already exists for that source — find it with
  `grep -rn "<work title words>" records/*/source/` — else `null`.
- `license`: read it from the file's header or `cic/texts/README.md`/`INTAKE.md`
  conventions; vendored texts are almost all `public-domain`. If you can't tell, write
  `"unknown"` and flag it.
- **Secondary sources** (`"kind": "secondary"`): `work` = author, title, year. When the work
  itself is vendored under `cic/texts/`, give `file`, `lines` and a verbatim `quote` too, all
  three together, checked like a primary's; otherwise `file`, `lines`, `quote` = null
  (amended 2026-11-08, Decision-Log "Whole-set rulings"). **Anti-fabrication rule: cite only a secondary work that is
  already cited somewhere in this repo** (`grep -rn` across `records/`, `Build/`,
  `cic/`). Never add a page number you have not seen in the repo. If no repo-cited
  secondary work supports a Widely Accepted / DMR grade, say so in `drafter_flags`; do not
  invent one.

## Per-link fields

- `citation_specificity`: `A` exact passage with line locus; `B` chapter/section; `C` work
  only; `D` author only; `E` none. (Same scale as the world records.)
- `verification_state`: `verified-direct` if you yourself read the quoted lines in the
  vendored file and they match; whether they show the relationship is what the grade says
  (amended 2026-11-08, Decision-Log "Whole-set rulings"). `named-not-rechecked` for support
  with no quote; `unverified` otherwise.

## The note (public text — this is participant-facing)

- One to three sentences, roughly 12–20 words each, nothing past ~25 words. Plain,
  serious, BBC/National Geographic register. Active voice, concrete verbs.
- Say what the evidence shows: who did what, when, in which text.
- Self-standing: it must make sense read alone (no "…and of", no "its sibling").
- **No internal language**: no census/atlas IDs (I.9, IX.34), no "edge", "grade",
  "record", "census", "entry", "shelving", "continuesAs", "process honesty", no build or
  cataloguing commentary. No double full stops.
- State uncertainty plainly ("Scholars disagree about…", "This rests on one source…").
- No invented detail. Every fact in the note must be supported by a listed source or be
  the kind of fact the existing note already asserted and you checked.
- No AI tells, no hedging filler.

## Known candidate problems (verify against texts; do not assume)

- old #39: "restoring the lapsed, argued under Callistus" — Hippolytus's charge against
  Callistus concerned penance for other sins; the lapsed crisis follows Decius (250).
- old #62: Sabellius (Rome, c. 215–220) and Paul of Samosata (deposed 268) are not "the
  same decades".
- old #6: School of Nisibis is c. 489 (after Edessa's school closed); 410 is the Synod of
  Seleucia-Ctesiphon.
- old #20: "total depravity, unconditional election, irresistible grace" are Dort-era /
  later labels, not Calvin's; "primary authority next to Scripture" is stronger than the
  evidence cited.
- old #59: who formally presided at Aquileia 381 (Valerian of Aquileia vs. Ambrose).
- old #49: authorship and setting of the Address to Origen are disputed.
- old #44: "read by its churches" — reception evidence is thin.
- old #10/#11, #7, #16, #38, #42, #13, #61, #5, #50: see the audit — likely over-grade or
  wrong type. #13's arrow may be backwards. #8/#25 and #9/#26 duplicate the same Cassian
  evidence: keep both only if each is separately true and separately evidenced, else keep
  the better-evidenced one and mark the other `"action": "remove"`.

## Output — write ONE JSON file to the path you are given

```json
{"group": "<group name>",
 "links": [
  {"old_index": 39,               // null for a new link
   "action": "keep" | "retype" | "regrade" | "rewrite" | "remove" | "split" | "new",
   "from": "...", "to": "...", "type": "...", "confidence": "...",
   "note": "...",
   "sources": [ ... ],
   "citation_specificity": "A", "verification_state": "verified-direct",
   "wants": ["text that would document this, if not vendored"],
   "drafter_flags": ["anything the reviewer must look at; your doubts; what you could not verify"],
   "change_reason": "one line: what changed from the old link and why"}
 ]}
```

`action` may combine (e.g. "retype+regrade" is fine as "retype"; explain in change_reason).
A `remove` still needs `change_reason`. A `split` means the old link becomes two entries,
both carrying the same `old_index`.

Every old link in your input must appear at least once in your output. Be honest in
`drafter_flags` — an honest "could not find this in the vendored texts" is worth far more
than a confident guess. Fabrication is the single most serious failure this project
recognises.

## Amendment, 2026-11-10: a seventh type, "member of"

Atlas World Map Decision-Log, "Change order: a seventh link type". `member of`: a church that
joined a council or fellowship of churches, on that body's own record (for example its member
list, or the minutes that admitted it). The direction runs from the member to the council.
Membership claims no descent and no influence. It is never major, and never carries `outcome`.
Do not use "in contact with" or "gave rise to" for membership.

