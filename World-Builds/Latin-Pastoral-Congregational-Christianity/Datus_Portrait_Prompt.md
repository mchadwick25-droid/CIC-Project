# Datus Portrait — Research Brief and Generation Prompt
## Latin Pastoral-Congregational Christianity (`lpc`) — Bishop of the Kept Flock

**Status:** APPROVED (2026-09-15) by the project lead, as part of the single packaged M1 identity-and-image decision recorded in `lpc_Decision_Log.md`. Built the same way the seven already-approved portraits were (`Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`, 2026-07-24 entries; `donatism/Fidelis_Portrait_Prompt.md`, 2026-09-10): historical grounding first, prompt built from that grounding second.

**FILE LOCATION — UNRESOLVED, and deliberately not guessed.** `Representative-Portraits/README.md` requires one subfolder per world *"named by the same `world_id` the flat icons in `../World-Icons/` already use."* **`lpc` has no `world_id`**: it is absent from `records/worlds.yaml` (nine worlds registered, this is not one) and has no icon in `World-Icons/`. Inventing a slug here would be a portfolio-level decision this build cannot make, and would create churn if registration later chose differently. **This document therefore sits in the world-build folder and should be relocated to `Ministry/Communication/Brand-Assets/Representative-Portraits/<world_id>/Datus_Portrait_Prompt.md` once `lpc` is registered.**

**The image asset itself is likewise not in place.** It was uploaded to `origin/mchadwick25-droid-patch-1` (commit `286f722d`, "Add files via upload") as `Ministry/Communication/Brand-Assets/Representative-Portraits/Latin Pastoral Image.jpg` — root of the folder, not in a per-world subfolder, and not following the `Name_Portrait.png` convention. **It is not on `main`.** It needs renaming to `<world_id>/Datus_Portrait.png` and merging.

**Governing style lock (2026-07-24, "Style locked"):** painterly/fine-art oil portrait — visible canvas texture and cracquelure, not photorealistic; warm, in-dialogue expression, not stern and not mid-speech; no jewelry; a historically-grounded held object; isolated-portrait chest-hold pose. **§0 anti-ghost (binding):** solid and fully opaque, no glow/halo/aura/bloom.

---

## Part One — Research Brief

### Who is being pictured

A bishop of an urban African congregation, across this world's full span (258–430) rather than at one moment in it. **Not Cyprian and not Augustine**, and not drawn to evoke either: this world's two documented bishops carry almost its whole record, and the Representative exists to speak for the congregations rather than to impersonate the two men who wrote about them.

### Step 1 — What this world's own record establishes

**ROLE (DOCUMENTED).** Doc_04 makes **G1 — Pastoral Office as Territorial Flock-Keeping** the Primary gravity. Doc_05 §4: authority here is *"pastoral in mode and territorial in scope … a bounded local community he is personally answerable for and to — not as jurisdiction over other sees."* Doc_03 counts **113 combined occurrences of flock / shepherd / pastor in Cyprian's corpus alone** (57 *flock*, 39 *shepherd*, 17 *pastor*).

**URBAN, NOT RURAL (DOCUMENTED BOUND).** Doc_05 §6.9: this world's surviving evidence is predominantly urban (Carthage, Hippo), and *"any claim this world's Representative makes about rural or Punic-speaking congregational life would rest on nothing this build has verified."*

**AGE (DOCUMENTED-ADJACENT INFERENCE).** Mid-to-late forties. Doc_05 §1 describes this world's first bishop as *"a rhetorician converted in middle life and made bishop of Carthage within two or three years"*; Augustine likewise took office in mid-life. **Both of this world's documented bishops were middle-aged when their crises hit.** **A man of sixty would be both worse-grounded and redundant in a portfolio where five of eight existing Representatives already read grey or elderly.**

**DRESS (SILENT — INFERENCE flagged).** This world's sources do not itemise clothing and Doc_05 does not reconstruct it. Per the standing three-step process (2026-07-24), the internal record was exhausted first and is silent; the *birrus* — a hooded African travelling cloak — comes from step two, geography-bound external evidence, and is the one element marking him as African rather than generically late-Roman. **Deliberately NOT the renunciant-plainness register** used for Albina and Chilo: an urban bishop is not a renunciant, and the 2026-07-24 standing caution warns specifically against inheriting one world's dress theme onto another. **No insignia:** mitre, crozier, pectoral cross, ring, stole and pallium are all centuries later.

### Step 2 — Defensible diversity, not a default

**APPEARANCE (SILENT — INFERENCE flagged).** Complexion is absent from the record, the same class of silence as Yausep's and Chilo's. **The value was deliberately NOT differentiated from Fidelis.** Datus and Fidelis are the same region, the same population and overlapping centuries; separating them on skin tone would have invented an ethnic distinction for a compositional reason, which is exactly what the standing three-step process exists to prevent. Age, dress, palette and object carry the whole separation instead.

---

## Part Two — The Held Object

**Disposition: a *libellus pacis* — a certificate of peace, with names written on it.**

**DOCUMENTED.** *Ep.* XV, Cyprian to the martyrs and confessors, verified note-stripped in body text: *"I beg you that you will **designate by name in the certificate** those whom you yourselves see, whom you have known, whose penitence you see to be very near to full satisfaction"* — written against certificates reading *"Let such a one be received to communion along with his friends,"* which, he says, *"opens a wide door"* to *"twenty or thirty or more"* unnamed people.

**Why this object.** It carries **three gravities at once**: G1 (a flock is kept *by name*), G2 (penitential discipline), and **G8, the Tensional gravity this world leaves unresolved** — the certificate is not the bishop's; a confessor wrote it, and he must decide what it is worth. It is also the material of `lpcstory005`. Doc_05 §1.1 gives the world's own voice on it: *"We were not decimated by an enemy at the gate; we were emptied at a table, one certificate at a time."*

**Rejected as weaker:** a purse (the hundred thousand sesterces of `lpcstory004` — reads as generic almsgiving); the commemoration record of death-dates (*Ep.* XXXVI, *"take note of their days on which they depart"* — attested, but it is Tertullus's object, not the bishop's).

### OPEN — the silhouette constraint, routed to the project lead

`donatism/Fidelis_Portrait_Prompt.md` records a codex **superseded and rejected** as Fidelis's object on the project lead's own critique: *"Silhouette recognition at icon/table-scene scale does not survive that distinction; two of seven Representatives reading as 'a bishop holding a book' defeats the object system's own purpose."* That constraint bars *"no book, codex, scroll, tablet, or any bound/rolled/flat written-text object of any kind"* and explicitly extends to collisions with **Theon (an opened scroll)** and **Albina (a wax tablet + stylus)**.

**Datus's certificate is a flat written-text object.** At icon scale it reads as a pale rectangle held in two hands. If the constraint governs the portfolio and not only Fidelis's document, four of nine Representatives would hold flat written things. **This was not visible when the object was chosen** — it lives on `main`, which this build's branch predates. The project lead elected to **proceed with the certificate and record the collision** rather than substitute. Alternatives remain live and reversible: the ransom purse (non-textual, no other Representative holds money), or no object, as Fidelis resolved.

---

## Part Three — Differentiation against the existing family

- **Fidelis (Donatism) — the sharpest adjacency, and the collision was real.** Same region, overlapping period, both bishops. The first draft was, point for point, the same man. Separated on four levers: **age** (mid-forties, dark-haired, against Fidelis's greying fifty), **the hood** (a bulky hooded silhouette against his bare-headed smooth drape), **palette** (dark tunic under a pale cloak, inverting his light-under-dark), and **the object** (a held document against his open empty hands). **Fidelis's empty open hands are the Donatist emblem** — that world turns on the purity of *the giver's hand* — which makes the certificate an apt contrast but places both images' focus in the same spot.
- **Chilo (Cappadocian).** Shares a hooded coarse-wool silhouette. Separated by beard (Datus short and dark; Chilo long, pointed and white), garment colour (grey-taupe against cream), belt (Chilo has one, Datus none) and object. **Judged "different enough" by the project lead, 2026-09-15.** Recorded as a known overlap, not as closed.
- **Theon (Alexandria).** The other document-holder. Theon points at a papyrus scroll; Datus holds a flat slip open in both hands. See the open constraint above.

---

## Part Four — The Gemini Generation Prompt

> A painterly fine-art oil portrait in the manner of an aged canvas — visible canvas weave and fine craquelure.
>
> Bust portrait: head and chest only, cropped at mid-chest, against a plain warm cream ground.
>
> A Roman North African man in his mid-forties — a man at the height of his working life, not an elder. Thick dark hair, short and slightly wavy, with the first grey at the temples. A full, neatly trimmed dark beard, lightly touched with grey. A strong, composed face. Level brows, warm direct gaze to the viewer as if mid-conversation.
>
> He wears a hooded African travelling cloak (*birrus*) of coarse woven oatmeal-grey wool — flat, tightly woven cloth with a visible weave. The hood is pushed back onto his shoulders, visible as a folded mass of the same flat woven cloth. Under it, a dull ochre-brown tunic. No ornament, no jewellery, no insignia.
>
> In both hands at chest height, turned toward the viewer, a single small flat slip of papyrus held open — one loose sheet, bearing only faint indistinct marks suggesting handwriting.
>
> Solid and fully opaque. No glow, halo or backlight. Wide landscape aspect ratio.

**Exclude:** fleece, shearling, sheepskin, fur, quilted or napped fabric, any modern-looking coat; old, elderly, frail or gaunt appearance; white hair; grey beard; **legible or pseudo-legible writing of any kind**; grey or cool background; full-length figure; codex, bound book, rolled scroll, document case, wax tablet; halo, nimbus, glow, backlight; mitre, crozier, cross, ring, stole, pallium, any vestment; jewellery.

**Avoided, and why:** any likeness of Cyprian or Augustine, or attributes evoking them (the Representative speaks for the congregations, not for the two men who wrote about them); a rural or desert setting (Doc_05 §6.9); renunciant/monastic dress register (Albina's and Chilo's, per the 2026-07-24 cross-contamination caution); legible Latin on the certificate (**invented names on a document would be a fabrication in a build whose first rule is never to invent**, so readable pseudo-Latin is out).

---

## Participant-facing text

**Alt text** (house template, written from the actual image):

> Datus: a bearded man in his forties with dark greying hair, in a hooded coarse wool cloak over an ochre tunic, holding a small papyrus sheet open in both hands, painted against a warm neutral ground.

**Caption** (names the tradition, never describes the image — the binding rule from the 2026-09-03 change order):

> **Datus, Bishop of the Kept Flock.** A representative voice for the town churches of Roman Africa — who learned, under persecution and plague, that a church which takes everyone back the same afternoon has no door, and one that takes no one back has no Master.

---

## Cross-reference

- Full M1 decision and its grounding: `lpc_Decision_Log.md`, 2026-09-15 entry.
- Governing style lock and the standing three-step appearance process: `Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`, 2026-07-24.
- Object-system silhouette constraint: `Ministry/Communication/Brand-Assets/Representative-Portraits/donatism/Fidelis_Portrait_Prompt.md`, 2026-09-10.
- Icon/table spec, §0 anti-ghost and §2 evidence-gating: `Ministry/Communication/Brand-Assets/CiC_World_Icon_and_Table_Template_Spec_V0_1.md`.
- Folder and filename convention: `Ministry/Communication/Brand-Assets/Representative-Portraits/README.md`.
