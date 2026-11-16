# Standard v1 test: Gregory of Tours and Benedict of Nursia

The record of the test that became Standard v1 (Mark, 2026-11-16: "yes this is a much better revision, i approve to move forward"). The rulings are in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, "The Who brief: what Mark has ruled so far, from the Gregory of Tours and Benedict test" (2026-11-15) and "Standard v1 approved to proceed" (2026-11-16).

The approved briefs are `Who-Profiles/bar/gregory-of-tours.brief.txt` and `benedict-of-nursia.brief.txt`, the same texts as in `Who-Profiles/era3/batch5/` and `era3/batch2/`. Nothing here is live. The census and the live audio are unchanged until era 3 is released.

| Path | Holds |
|---|---|
| `recording/gregory-of-tours.mp3`, `recording/benedict-of-nursia.mp3` | The second recording, of the approved texts. Each `text_sha256` in `manifest-entries.json` matches the committed brief. |
| `recording/manifest-entries.json` | The manifest lines the recording script wrote, for use at release. |
| `recording/run1.log`, `recording/run2.log` | The printed settings and costs of both paid runs. |
| `reviews/` | The independent reviews: three rounds on the first version (the cap), then the targeted rechecks of the revision that Mark ordered. |
| `references.md` | The references for each brief, as the test page showed them. |

## The two paid runs

Both runs used the same printed settings: voice `MFZUKuGQUsGJPQjTS4wC` (Jon v4), model `eleven_v4`, format `mp3_44100_128`, settings `{"stability":0.85,"similarity_boost":0.88,"style":0.05,"use_speaker_boost":true,"speed":0.95}`, tags `[calmly]` and `[warmly]`.

| Run | Approved by | Characters sent | Credits charged | Balance |
|---|---|---|---|---|
| First version | Mark: "yes i want to hear audio" | 4,630 | 2,245 | 240,897 to 243,142 |
| Revision | Mark approved re-recording both | 4,693 | 2,275 | 243,142 to 245,417 |

After the first run, the balance at first moved only 1,141. The run was stopped and reported. A later read showed the full 2,245, so the second charge had settled late.
