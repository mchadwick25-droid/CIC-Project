import json, sys
sys.path.insert(0, 'Build/Ministry/Operations/Audits/2026-11-26_batch-12/_gen')
from people import P
B = 'Build/Ministry/Operations/Audits/2026-11-26_batch-12'
role = open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/researcher.md').read()
c = json.load(open('cic-website/data/world-census.json'))
m = {x['id']: x for x in c['movements']}
RUL = 'Mark, 2026-11-27, "Batch 12: the slate approved": "approve the slate as recommended". This batch only.'
only = sys.argv[1:]
for slug, d in P.items():
    if only and slug not in only: continue
    e = m[slug]; folder = f'{B}/{slug}'
    card = f'{folder}/Card.existing.json'
    json.dump(e.get('card') or {}, open(card, 'w'), ensure_ascii=False, indent=2)
    old = d['old']
    if 'refs.md' in old:
        oldp = f"`Build/Ministry/Operations/Audits/{old.replace('SLUG', slug)}` (a reference list only; never open a brief)"
    else:
        oldp = f"`Build/Ministry/Operations/Audits/{old}/` (its `Source_Sheet.md` and `Outline.md` only, never a brief)"
    h = f"""# Batch header

- **Story:** {e['name']} (census id `{slug}`). **Kind:** person (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/person.md`). **Folder:** `{folder}/`. **Card file:** `{card}` (the census `card` field as it stood when this prompt was made; the era 1 card thread may be rewriting it in the census).
- **Job on the slate ({RUL}):** {d['job']} Part {d['part']}. Shape proposed on the slate: {d['shape']}; the record decides the order.
- **Census home and direct line:** {d['home']}
- **Descent or break:** {d['brk']}
- **Siblings:** {d['sib']}
- **Live beside it:** {d['beside']}
- **Heart and length:** not yet set; your outline proposes the heart and length, and they go to Mark on the hearts page.
- **This batch's rulings ({RUL}):**
  - A new source sheet and outline from the Library. The earlier research for this person, {oldp} is a pointer only: use it to find passages, then read every passage in its file yourself. Its wording and its judgments are not carried over. Do not open `{slug}.brief.live.txt` in your folder or any other version of the live story. The census entry's `longDescription` in `cic-website/data/world-census.json` is the live story: take any census field you need with a command that leaves `longDescription` out.
  - Quotes: no reuse in this batch. Every quote in the live stories named under Live beside stays barred, and no quote is shared inside the batch. A researcher who wants a barred quote asks. Barred: {d['bars']}
  - No census change. A descent or break named above is told as the old sources give it, crediting each witness.

---

"""
    body = role.replace('{NAME}', e['name']).replace('{FOLDER}', folder).replace('{CARD}', card)
    open(f'{folder}/Researcher_Prompt.filled.md', 'w').write(h + body)
print('ok', len(P))
