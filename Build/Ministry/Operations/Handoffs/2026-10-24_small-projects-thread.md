# Handoff — small projects thread — 2026-10-26

From session: https://claude.ai/code/session_01LXQVhoN4b7gUG2KwMhR8CK · World or workstream: Go Deeper page, landing page, conversation chooser · Branch / PR: see the table

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Gift links "Keep the door open for others" on `go-deeper.html`, with the Faithways fine print (rulings 91, 94). PRs 1120, 1126 | Page tests pass; CI green; merged |
| "Get more conversations" on the landing page (ruling 92, now superseded by 106). PR 1122 | Merged |
| Voice on the card backs: tool, 11 clips, player, freshness test. PRs 1123, 1125 (Wittenberg text) | Paid settings printed and matched the manifest; each hash matches its summary; sample and 10 clips approved by name with caps (430 and 5,000 characters) |
| The app's panel carries the gift section; the app draws its panel alone at `#get-more` (rulings 98 and 99; the ruling 97 in the log is the accounts thread's). PR 1129, promoted by PR 1142 | 350 app tests, `tsc`, `vite build`; Mark checked a new conversation and the panel on the live app after deploying `29052b8` by hand |
| The landing page's top-row "Get more conversations" button and the free-line link open the app's panel in a slide-out over the cards (rulings 105, 106). PR 1146 | Headless browser against the live domains: opens, closes from inside, reopens, no errors; Mark confirmed it works like the conversation page |

## 2. Not done

- Keyboard focus is not trapped inside the slide-out (Go-Deeper Later_List item 3).
- The accounts fixes (PRs 1124, 1130), the LPC records (PRs 1128, 1136) and later `main` work are not on `live`. Promotion 1131 carried them with this thread's panel, and new conversations showed a 404 on that build; it was rolled back (PR 1137). The cause is not found.
- (Resolved 2026-10-27) Render's auto-deploy for cic-engine was left off by the manual rollback; Mark set it to "After CI checks pass".

- Card-back audio on flip: draft PR https://github.com/mchadwick25-droid/CIC-Project/pull/1150 starts the clip from the tap that turns the card (Mark confirmed it directly). No audio, word or voice changed, nothing generated. The clips match the card text as of 2026-10-24; they are redone after Mark's text edits, with a new named run, cap and sample approved by ear (Conversation-Chooser Later_List items 5 and 6; iOS Safari and screen readers untested).

## 2b. Seen on Mark's live screenshot, 2026-10-26 (not looked at, not fixed)

- The top-bar "Get more conversations" button in the conversation shows a tight yellow box with the text touching its edges. It may be the keyboard focus outline.
- The panel's text runs close to the right edge.
- The message box shows a scrollbar with almost no text in it.
- The panel's "Get more conversations" link opens a popup of `go-deeper.html` (`getCodeUrl()` in `cic-poc/frontend/src/lib/deeper.ts`). While buying is suspended (ruling 80) that page reads "Codes are not on sale yet".

## 2c. The promotion after the 1131 rollback (2026-10-26), done

`live` was rebuilt in pieces taken from `main`, each merged and deployed by Mark by hand and checked with a new conversation: piece 1 (docs, library, LPC records; PR 1155), 2a (accounts, ledger, backup, refill days, accounts off; PR 1156), 2c (tester codes without a daily limit, dashboard list; PR 1157), 2b (question text deleted at 90 days with the privacy page, and the site files; PR 1163). Render reports `053f20d`. The 404 on promotion 1131 was never explained; Mark said to let it go. `live` does not equal `main`: the LPC thread's newer work (PRs 1158 to 1161, one commit marked "held") stays on `main`. The first daily retention run after the 2b deploy clears question text older than 90 days. Render's auto-deploy for cic-engine is set to "After CI checks pass" (Mark, 2026-10-27), so a merge into `live` deploys by itself once CI passes on the push to `live`.

## 3. Re-check before you trust it

- The 404 on the 1131 build: the Render log line for it would name the path. Not read by this thread.
- The slide-out was tried on a computer in a headless browser only, not on a phone, with accounts on, or with a screen reader.
- Wittenberg's back summary now reads the site text in `Approved-Card-Words.yaml` (Conversation-Chooser Later_List item 4).

## 4. Waiting on Mark

- Per-world voices for the card backs (Conversation-Chooser Later_List item 1).

## 5. Next step

Nothing open from this thread. If more of `main` is promoted later, build it as explicit pieces on `live` (a merge would not carry the reverted 1131 content), and wait for the LPC thread's word on its held work.

## 6. Spend

Allowance share used: not measured. Metered: ElevenLabs, "card-back-sample-theon" (430 characters, cap 430) and "card-back-run-10" (4,969 characters, cap 5,000), both approved by Mark by name.
