# P2-G3b: adversarial review brief (Opus)

You review a draft list of people for the Church Family Tree. Work from the census, the Library
and the texts, not from the drafters' or checkers' conclusions. Your job is to find what is wrong.

Repository (read only): `/home/user/CIC-Project`. Census `cic-website/data/world-census.json`;
shelves `cic/corpus-map/<movement id>.yaml`; texts `cic/texts/`; world builds `Build/worlds/`.

## The rule being applied

A person qualifies by this route when they are named in at least 5 distinct passages in each of
at least 2 later traditions' own-voice texts (Decision-Log 2026-11-09, "People on the map"; Mark's
answer D a, 2026-11-10: namesakes checked, editors' notes left out). Strict rules used:

- A counted passage must lie in a work that tradition's shelf (`cic/corpus-map/<tradition>.yaml`,
  role `tradition`) holds, inside the locus the row gives; "whole file" means the file's own text.
  Another work in the same file does not count.
- Editorial matter does not count: editors', translators' or modern scholars' notes, prefaces,
  introductions, headings an editor added, apparatus, indexes, contents, running heads.
- Namesakes do not count. One person under two spellings is one person.
- Distinct passages: mentions in the same paragraph count once; the same passage in two
  languages or two editions counts once.
- Later: the tradition starts after the person's last year, and is not the person's own home.

And the qualifying test (ruling 14): a party in their own right, with writing of their own or a
recorded position (own words = own writing, a document issued or signed in their name, verbatim
minutes; not speech others report, not works of disputed authorship), who founded no lasting
movement. Founders go to Mark as a question; they are recommended "hold".

## What you check, for every candidate in your file

1. **Every counted ref** (`refs` under each tradition in `consolidated`): open the file at the
   line (`sed -n 'L-8,L+8p'`), and confirm in-shelf, same person, not editorial, distinct.
   Recount. If a tradition falls below 5 after your recount, that is BLOCKING for the candidate
   (it no longer passes) unless you find, yourself, other valid passages in the same shelved
   works to make it up; then list them as file:line.
2. **Later and not home**: compare the tradition's census start with the person's last year;
   check the counted tradition is not the person's real home.
3. **The draft row** (`draft`): home, dates, own words, founder, why, recommendation. Each quote
   must be verbatim in the file (grep it). Any invented fact or misquote is BLOCKING.
4. **Recommendation**: would you stand behind it? If not, say what it should be and why.

Severity: BLOCKING (wrong or unsupported: fails the count, invented, misquoted, misidentified),
SUBSTANTIAL (the recommendation or a stated fact should change), MINOR (wording, a weak ref that
does not change the count). Do not raise "could be stronger" findings; the bar is sound, not perfect.

## Output

`review.json` in your own folder: a list, one object per candidate, in input order:
```json
{"cid": "...", "name": "...", "verdict": "approve" | "revise",
 "recount": {"<tradition id>": {"valid": 6, "rejected": {"file:line": "reason"}, "added": ["file:line"]}},
 "passes_after_review": true,
 "findings": [{"severity": "BLOCKING|SUBSTANTIAL|MINOR", "what": "...", "evidence": "file:line or census id", "fix": "..."}],
 "recommendation_should_be": "include|hold", "why": "one sentence"}
```
End with a short summary: how many candidates pass after review, how many findings by severity.
Do not edit the repository; write only in your own folder; no model or network calls.

## A note on the inputs

The drafters were given `refs` from a first build with a bug (context ids repeated across
candidates, so some refs pointed at other people's lines). Several drafts say the refs were
"stale" and recount from their own searches. The `consolidated.refs` in your file are rebuilt and
correct as labelled; check them, and where a draft's own count differs, settle it from the text.
Where a round-1 tradition was never strictly rechecked (`strict_rechecked: false`), apply the
strict rule to every ref yourself.
