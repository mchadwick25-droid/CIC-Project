# P2-G3b build: revision brief (round 1 findings)

Read `Person_Drafting_Brief.md` (this folder) again. Your drafts and the Opus review of them are
named in your task. Write a revised draft for each, `Draft_r1.json`, in the same folder as the
draft, same format, and a `Revision_Round1.json` beside it: one entry per finding,
`{"id", "action": "fixed|no change", "what"}`.

- Apply every blocking, substantial and minor finding. Where a finding gives replacement text or a
  corrected English rendering, use it exactly as given (renderings are Opus-authored; do not
  reword them).
- **Pamphilus is held (decided after the review).** Remove `pamphilus-of-caesarea` entirely: its
  entry, its fact-table rows, its `rows` item and any `concerns` naming it. Ignore findings on him.
- Paula stays: her Letter XLVI, issued in her name, counts as her own words (ruling B).
- floorNote follows release 29's use (the doctrinal-floor note, as in `origen`); caveats about
  dates or sources go in `sourcing`.
- Every new or changed sentence keeps a fact-table row with a verbatim quote. Never invent.
- Run the helper and fix every line it prints:
  `cd /home/user/CIC-Project && python3 Build/Ministry/Operations/Audits/2026-11-10_agreed-entries/check_draft.py <Draft_r1.json>`
- Do not edit the repository; no model calls, no network. Finish with a short summary.
