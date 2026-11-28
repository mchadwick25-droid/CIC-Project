# Church Family Tree coordinator — handover, 2026-11-28

You are the new Church Family Tree coordinator. Every earlier CFT thread, the old coordinator included, is retired (Mark, 2026-11-28: "we do one at a time and start all new threads, dont loos anything, but you are all going away for good"). Nothing is lost: every thread's work is pushed, and each has a resume file named below. Your first job: archive the two idle threads still open, batch 12 continued (`session_01JMNsSBNPfSCovXv4tQJF1X`) and era 1 cards (`session_01JMNsS9jvf8MiuJ4c5BaFtq`), then tell Mark you are ready and ask the open decision below. The old coordinator (`session_01JMNsSDxiDjhkPh1K48BmfL`) is Mark's to archive.

Read CLAUDE.md first. Then this file. Do not read old transcripts.

## Why the old threads were retired

On 2026-11-27/28 batch 12 used about a quarter of Mark's weekly allowance in a couple of hours. The causes, found in the session logs:

1. **The coordinating session did small jobs at full size.** It grew to about 405,000 tokens, and every edit, command or reply it handled re-read all of it. In a four-minute sample that was about 70% of all tokens used; the helper agents doing the writing and checking were about 30%. It never handed over, because the Kit's "near its context limit" never came with a million-token window.
2. **Each story ran about 9 review passes** (outline check and recheck, two trust reads, two listener reads, fresh read, craft check, card check, blind second readings and comparer), each a fresh Opus hand reloading the sources. Mark: "i have a 3 review limit".
3. **The batch was 20 people in one session.** The Kit says two halves of about six, each in a fresh session. The old coordinator set it up wrong.

## Standing rules for every thread from now on

- **One thread at a time.** Never two working threads at once, the coordinator aside.
- **Hand over at about 150,000 tokens.** Any thread that nears it writes its resume file, pushes, and stops; a fresh thread continues from the file.
- **A coordinating thread does no small jobs itself.** Edits, applies and commands go to helper agents; the coordinating thread reads their short reports.
- **Check usage after each thread finishes**, and stop to tell Mark before a thread goes past about 5% of the week.
- **You stay small too.** Short replies to Mark; no polling; read other sessions only when something needs checking.

## The open decision (Mark has not answered)

How a story's checking fits Mark's 3-review limit. This changes the Brief Kit, which only Mark's words change. Options shown to him:

- **A (recommended).** Three reviews: (1) the outline against the sources; (2) one review of the draft carrying a trust read and a listener read, revised once; (3) one fresh final read that also checks the card and re-verifies every quote verbatim against the vendored source. Blind second readings and the separate craft check go.
- **B.** As A, but blind second readings stay inside review 3 for quotes of six words or more.
- **C.** Keep the Kit's checks, run them in small fresh sessions only.

Nothing restarts until Mark decides. Ask him this one question when he is ready; do not stack others on it.

## Work, in order

1. **Batch 12: era 1 people and the era 1 brief.** Branch `claude/batch12-era1-persons` (head 3b1287508). Resume file: `Build/Ministry/Operations/Audits/2026-11-26_batch-12/Continue_Prompt.md`, with the batch README beside it. State: 9 people done to release; 4 with cards done and second readings in progress; Josephus, Peter, Cyprian and Eusebius held for length, now ruled by Mark's "follow recommendations on all" (Decision-Log, 2026-11-28); the rest per the resume file. No recording in this batch. Restart in small fresh threads of 3–4 people each, under the decision above.
2. **Era 1 cards (all kinds).** Branch `claude/built-world-short-descriptions-v2` (head 2f33c9d9a). Resume file: `Build/Ministry/Operations/Audits/2026-11-26_era1-cards/README.md` and `Header.md` beside it. State: all 20 traditions done (14 live via #1829, 6 checked, waiting for the next release); next are 7 people (Irenaeus, Dionysius of Alexandria, Novatian, Polycrates, Pliny the Younger, Marcion of Pontus, Hermas), then stories, connections, rivers, and the site code for those card kinds. Starts only after batch 12 is released, in small threads.
3. **After the era 1 cards release:** a capped recording run (Daniel) of the four Church in Conversation Tradition briefs: House Church, Alexandria, Syriac, Latin pastoral. Sample first, Mark's approval and cap.
4. **Later:** Sally Ford recordings for new people and stories (PR #1840; sample and cap first); feedback email options A/B/C (parked); about 270 old artifacts to clean up (Mark: "we will get back to clean up later"); Stripe page wording (Mark's dashboard).

## Fixed points

- CFT site `cft-website/` deploys from `main`. `live` is Church in Conversation production: never promote it or open a PR into it.
- Only Mark's words change a kit; rulings go in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, gaps in `Open-Gaps.md`.
- Mark answers threads in the thread itself; do not relay questions he has already answered there.
- Public wording: "Christian Tradition", and "Church in Conversation Tradition" for the built ones; never "world".
