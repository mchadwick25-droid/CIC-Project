# Handoff — small projects thread — 2026-10-24

From session: https://claude.ai/code/session_01LXQVhoN4b7gUG2KwMhR8CK · World or workstream: Go Deeper page, landing page, conversation chooser · Branch / PR: https://github.com/mchadwick25-droid/CIC-Project/pull/1120 (merged), https://github.com/mchadwick25-droid/CIC-Project/pull/1122 (merged), card voice on claude/card-back-narration

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Gift links ("Keep the door open for others") on `go-deeper.html`, Option A words approved by Mark; ruling 91 | `test_go_deeper_pages.py` passes; page rendered and compared with its neighbours; PR 1120 CI green, merged |
| "Get more conversations" link on the landing page's free line; ruling 92 | Same test file passes (37); PR 1122 CI green, merged |
| Voice on the card backs: tool, 11 clips, player on the back face, freshness test, log entries | Printed paid settings match the manifest; each hash matches its summary; clips 31 to 48 seconds; 39 page and audio tests pass; headless render shows the player on a turned card and a click on it does not turn the card back |

## 2. Not done

- Per-world voices for the card backs (Later_List.md, Conversation-Chooser, item 1).
- The sentence in "Already have a code?" is not a link into the room; Mark said the landing link is enough.

## 3. Re-check before you trust it

- Wittenberg's back summary differs between the site census (531 characters) and `Approved-Card-Words.yaml` (517); the audio reads the census.
- The Go Deeper page still reads "Codes are not on sale yet", which a visitor now reaches from the landing page.
- Playback was not heard in a real browser by this thread; only the markup and the click behaviour were checked.

## 4. Waiting on Mark

- Which Wittenberg text is approved.
- Whether the gift fine print should carry the Faithways Studio line.

## 5. Next step

Open the card-back narration pull request, then merge when its CI is green.

## 6. Spend

Allowance share used: not measured. Metered: ElevenLabs, "card-back-sample-theon" (430 characters, cap 430) and "card-back-run-10" (4,969 characters, cap 5,000), both approved by Mark by name.
