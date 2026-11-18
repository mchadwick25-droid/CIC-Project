# Church Family Tree, batch 5: launch

Paste this as the first message of a new session.

---

Run Church Family Tree batch 5 end to end on the brief kit, `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, with its role prompts in `Brief-Kit/roles/`. Read `CLAUDE.md` first, then the kit, then the Decision-Log entries "The brief kit for batch 5, as one document" and "Batch 5: the slate and each story's job" (both 2026-11-18), and Open-Gaps 329 and 330.

**The twelve.** Each is a person already on the tree whose story was written before the new kit. Rewrite each on the kit, as batch 4 did (`Build/Ministry/Operations/Audits/2026-11-18_batch-4/`: its README and prompts are the working model). The census id is given; the job is Mark's, and sets each story's focus. A sibling's live story is read before research, and its quotes are not reused.

| Census id | Job | Siblings and links |
|---|---|---|
| `nestorius` | What he taught about Christ and Mary, why it cost him his see, and how his name and his late defense of himself were carried east. | `council-of-ephesus-431` tells the council; here it is a sentence. `cyril-of-alexandria`. |
| `cyril-of-alexandria` | The bishop of Alexandria, his teaching of the one Christ, and how his words became the measure for the Coptic and other Oriental Orthodox churches. | `nestorius` (the same quarrel, from Cyril's side and what it made), `council-of-ephesus-431`, `council-of-chalcedon-451`. |
| `barsauma-of-nisibis` | The frontier bishop and the synods that set the Church of the East on its own path in Persia. | `narsai` has the school; here it is a clause. |
| `babai-the-great` | The abbot of Izla who, while the church had no head, wrote the teaching on Christ that became its own and reformed its monks. | `barsauma-of-nisibis`. |
| `timothy-i-of-baghdad` | The church at its widest: a patriarch under the caliphs, his debate before the caliph, and the bishops he sent toward Central Asia and China. | Link: `alopen`. |
| `martin-luther` | The protest over indulgences, his stand at Worms, and the German Bible and hymns his churches kept. | `william-tyndale`. |
| `william-tyndale` | The English New Testament from the Greek, printed in exile, and his death for it. | `martin-luther` (Worms: Luther's stand, Tyndale's printing); `john-wyclif` already quotes Tyndale ("no one's English to follow"), so use other words. |
| `john-calvin` | The exile held in Geneva, the Institutes, and the Reformed churches that took their order from it. | None. |
| `john-wesley` | The warmed heart, preaching in the open air, and the societies and classes that became Methodism. | `thomas-a-kempis` already quotes Wesley ("true religion was seated in the heart"), so use other words. |
| `augustine-of-hippo` | The teacher of rhetoric turned bishop, the Confessions and the City of God, and his teaching on grace that the West carried on. | `antony-the-great` and `conference-of-carthage-411`: each at most a sentence. |
| `patrick-of-ireland` | The captive who came back as a bishop, told in his own two short writings. | None. |
| `athanasius-of-alexandria` | The long defense of Nicaea's creed after the council: five exiles, the Life of Antony, and his list of the books of Scripture. | `council-of-nicaea-325` and `arius` tell the council and the teaching; here Nicaea is a sentence. His old recording is replaced. |

**How.** Follow the kit's Part 4, step by step, with a fresh hand for each role. Opus drafts and checks the stories and outlines; Sonnet or Haiku do mechanical census and page work. Write prompts and records to `Build/Ministry/Operations/Audits/<date>_batch-5/`; no shared scratch file between agents. The hearts come to Mark on one page before the outline checks. Run `python tools/check_tree_overlap.py` over the batch's briefs before review. Stop for Mark only at the kit's own stops (the hearts, a brief that fails after one revision, a sibling question) or a missing input.

**Recording** is a paid run: it waits for Mark's approval and a credit cap, records one item first, prints its settings, and checks the balance after. Use the voice and settings of batch 4 (its `recording/` logs).

**Release.** One pull request for the batch: open it as a draft, push once after the local checks pass (census validator, atlas-check, live commentary, American spelling, readability, tool tests), then mark it ready. Merge it when CI is green. Promotion to live is Mark's call.
