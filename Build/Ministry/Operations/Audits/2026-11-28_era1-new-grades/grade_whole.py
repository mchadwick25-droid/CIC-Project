"""Grade on the whole text: every held finding weighed by its size (Mark, 2026-11-28, option "a").

Uses only findings already held: this folder's scans, listener read and hedged dates, through
grade.py's own readers, and the same for ../2026-11-25_person-council-grades/ as calibration.
grade.py is left unchanged. Run from the repository root:
python Build/Ministry/Operations/Audits/2026-11-28_era1-new-grades/grade_whole.py
Writes Grades_Whole.csv, Grades_Whole.json and Calibration_Whole.json in this folder.
"""
import csv
import importlib.util
import json
import os
import re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
NOV25 = os.path.join(HERE, '..', '2026-11-25_person-council-grades')

# ---- Weights by size, committed before any brief was scored. ----
SIZE = {
    'note': 0,    # Below the kit's bar (Part 3): exactness that neither misleads nor touches the heart.
    'small': 1,   # One clause fixes it, and the listener is not misled meanwhile.
    'medium': 3,  # A claim the listener takes as the record that the record does not hold, or a lost thread.
    'large': 6,   # A misread source, a missing heart, a softened record, or a story the listener leaves.
}

# Each finding kind the method already has, and its size.
KIND = {
    ('rigor', 'bare', 'Passing'): ('small', 'a thing or act left unexplained on the way; one clause supplies it'),
    ('rigor', 'bare', 'Supporting'): ('small', 'unexplained where the story leans on it, still one clause to supply'),
    ('rigor', 'bare', 'Central'): ('large', 'the heart itself left unexplained: missing essential material'),
    ('rigor', 'bare', 'below the bar'): ('note', 'an ordinary act or detail, which Part 1 says needs no gloss'),
    ('rigor', 'hedged date', 'any'): ('small', 'a date hedged but resting on modern reckoning; Mark ruled it one modern finding, and Moses the Black B'),
    ('rigor', 'modern', 'Passing'): ('small', 'an unnamed modern view in a side clause; cut or attribute it'),
    ('rigor', 'modern', 'Supporting'): ('small', 'an unnamed modern view where the story leans on it, still a clause to cut'),
    ('rigor', 'modern', 'Central'): ('large', 'the heart told through a modern view'),
    ('rigor', 'guess', 'Passing'): ('medium', 'a modern guess told as the record: the listener is misled, though one clause cuts it'),
    ('rigor', 'guess', 'Supporting'): ('medium', 'a modern guess told as the record where the story leans on it'),
    ('rigor', 'guess', 'Central'): ('large', 'the heart rests on a modern guess told as the record'),
    ('rigor', 'trust', 'sentence'): ('medium', 'a sentence the trust read found the sources do not hold'),
    ('rigor', 'trust', 'heart'): ('large', 'a sentence on the heart that the sources do not hold'),
    ('craft', 'test line', 'any'): ('large', 'after one hearing the listener cannot say who, what, or why: the heart is missing'),
    ('craft', 'opening', 'any'): ('small', 'the opening lacks a when or where; a clause fixes it'),
    ('craft', 'bare', 'any'): ('small', 'the listener lost a thing named without its explanation; one clause'),
    ('craft', 'bare', 'below the bar'): ('note', 'an ordinary act or detail, which Part 1 says needs no gloss'),
    ('craft', 'tell', 'any'): ('small', 'a tell Part 1 names, in one sentence; cut or retell it'),
    ('craft', 'thread', 'any'): ('medium', 'a sentence where the listener lost the thread: a failure to understand on one hearing'),
    ('craft', 'pull', 'no'): ('medium', 'the opening does not pull an adult listener in'),
    ('craft', 'leave', 'no'): ('large', 'the listener would not stay to the end'),
    ('craft', 'summary', 'any'): ('large', 'a summary, not a story: the form Part 1 requires is missing'),
    ('craft', 'short', 'any'): ('large', 'under the kind\'s length floor'),
}

# A bare statement meets the kit's bar when it names a thing (a book, teaching, charge, quarrel,
# ruling or label) or an act of conflict or punishment without its what or why (Part 1, "Explain
# it or leave it out"; Part 3: "missing essential material"). Otherwise it is a note. Read on the
# quoted words and the reader's question together; the same rule is applied to every set.
BAR_WORDS = re.compile(
    r'persecut|prison|arrest|exil|banish|deport|sent to |condemn|depos|excommun|put out|cast out|expel|'
    r'heretic|heres|charg|accus|trial|tried|judg|execut|kill|martyr|burn|behead|sentenc|punish|'
    r'dissolv|suppress|forbid|ban(ned)? |quarrel|disput|split|schism|broke|break|reject|refus|'
    r'would not accept|enrag|oppos|attack|against|fight|war\b|siege|besieg|army|protest|court|'
    r'teaching|taught|doctrine|book|letter|writ|ruling|decree|canon|council|sermon|creed|reform|'
    r'ideas|confess|seiz|shameful|law\b|crime|guilt|wrong|offen',
    re.I)

# Grade from the summed weight, per 700 words of brief (the middle of this set's length).
PER = 700
# Upper bound of load for each letter; above D's bound is F.
THRESHOLDS = [
    ('A', 0),    # Nothing counted: only notes below the bar.
    ('B', 3),    # Up to about three one-clause fixes, or one misleading clause: OK to keep.
    ('C', 6),    # Several small fixes, or two misleading clauses: would benefit.
    ('D', 10),   # A large fault, or many mediums: should be redone.
]
# A large fault holds the dimension, and the overall, at D or below (the truth guard).
LARGE_CAP = 'D'
# Overall: the mean of rigor and craft (A=4 ... F=0); a half point goes to rigor's side.
POINTS = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
LETTER = {v: k for k, v in POINTS.items()}
ACTION = {'F': 'must be redone', 'D': 'should be redone', 'C': 'would benefit',
          'B': 'OK to keep', 'A': 'great as is'}
WEIGHT_NAME = {1: 'Passing', 2: 'Supporting', 3: 'Central'}
# ---- End of committed weights. ----


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def letter(points_sum, words, has_large):
    ld = points_sum * PER / max(words, 1)
    g = 'F'
    for lt, bound in THRESHOLDS:
        if ld <= bound:
            g = lt
            break
    if has_large and POINTS[g] > POINTS[LARGE_CAP]:
        g = LARGE_CAP
    return g, round(ld, 1)


def finding(dim, kind, band, quote, fix, why=''):
    size, reason = KIND[(dim, kind, band)]
    return {'dim': dim, 'kind': kind, 'band': band, 'size': size, 'weight': SIZE[size],
            'quote': quote, 'fix': fix, 'reason': reason, 'why': why}


def meets_bar(quote, asks):
    return bool(BAR_WORDS.search(quote + ' ' + (asks or '')))


def rigor_findings(items, trust):
    out = []
    for i in items:
        band = WEIGHT_NAME.get(i.get('weight'), 'Passing')
        if i['test'] == 'bare statement':
            asks = i.get('asks', '')
            kind_band = band if (band == 'Central' or meets_bar(i['quote'], asks)) else 'below the bar'
            out.append(finding('rigor', 'bare', kind_band, i['quote'],
                               f"Answer in a clause, from the source: {asks} If the old source gives only the act, leave it as told and the finding falls.",
                               i.get('decided_by', '')))
        elif i.get('kind') == 'hedged date':
            out.append(finding('rigor', 'hedged date', 'any', i['quote'],
                               'Give the date only as roughly as the old sources allow, or cut it.', i.get('decided_by', '')))
        elif i.get('kind') == 'guess':
            out.append(finding('rigor', 'guess', band, i['quote'],
                               'Cut the clause, or give it in the voice of an old witness who says it.', i.get('decided_by', '')))
        else:
            out.append(finding('rigor', 'modern', band, i['quote'],
                               'Cut the clause, or say what the old sources themselves say.', i.get('decided_by', '')))
    if trust and not trust.get('all_hold'):
        n = trust.get('not_holding', 0)
        heart = trust.get('heart_blocking', False)
        for k in range(n):
            band = 'heart' if (heart and k == 0) else 'sentence'
            out.append(finding('rigor', 'trust', band, f"trust read, sentence {k + 1} of {n} not holding ({trust.get('file', '')})",
                               trust.get('ruling', 'Retell the sentence from what the source holds, or cut it.')))
    return out


def listener_items(path):
    """The quoted lines of each listener block, by section label."""
    out = {}
    for block in re.split(r'^## ', open(path, encoding='utf-8').read(), flags=re.M)[1:]:
        pid = block.split('\n', 1)[0].strip()
        sec, cur = {}, None
        for line in block.split('\n')[1:]:
            m = re.match(r'^([A-Z][A-Za-z -]+):', line)
            if m:
                cur = m.group(1)
                sec.setdefault(cur, [])
            elif line.startswith('- ') and cur:
                q = re.match(r'- "(.*)"\s*\|\s*(.*)$', line)
                sec[cur].append((q.group(1), q.group(2)) if q else (line[2:], ''))
        out[pid] = sec
    return out


def craft_findings(r, li, words, floor):
    out = []
    lines = li or {}
    tl = lines.get('Unfilled test lines', [])
    for k in range(r['unfilled'] or 0):
        q = tl[k] if k < len(tl) else ('test line', '')
        out.append(finding('craft', 'test line', 'any', q[0], f"Give the listener this in the story: {q[1] or q[0]}"))
    if r['opening']:
        out.append(finding('craft', 'opening', 'any', r['opening_note'], 'Bring the ' + r['opening_note'].replace('missing ', '') + ' into the opening, in a clause.'))
    bl = lines.get('Bare statements', [])
    for k in range(r['bare'] or 0):
        q = bl[k] if k < len(bl) else ('bare statement', '')
        band = 'any' if meets_bar(q[0], q[1]) else 'below the bar'
        out.append(finding('craft', 'bare', band, q[0], f"Answer in a clause, from the source: {q[1].replace('asks: ', '')}"))
    tells = lines.get('AI tells', [])
    for k in range(r['tells'] or 0):
        q = tells[k] if k < len(tells) else ('tell', '')
        out.append(finding('craft', 'tell', 'any', q[0], f"Cut the sentence, or tell what happened instead ({q[1]})."))
    th = lines.get('Thread-losing sentences', [])
    for k in range(r['thread'] or 0):
        q = th[k] if k < len(th) else ('thread', '')
        out.append(finding('craft', 'thread', 'any', q[0], f"Retell the sentence so the listener keeps hold of it: {q[1]}"))
    if r.get('pull') is False:
        out.append(finding('craft', 'pull', 'no', r.get('pull_note', ''), 'Open on one moment from the record with someone acting.'))
    if r['listen'] is False:
        out.append(finding('craft', 'leave', 'no', r['drift'], 'Tell it as a story in order, so the listener stays.'))
    if r['form'] == 'summary':
        out.append(finding('craft', 'summary', 'any', r['form_note'], 'Retell it as a story: one opening moment, then events in order with people acting.'))
        if words < floor:
            out.append(finding('craft', 'short', 'any', f"{words} words", f"Bring it to the kind's floor of about {floor} words, or say why the record is thin."))
    return out


def pulls(path):
    out = {}
    for block in re.split(r'^## ', open(path, encoding='utf-8').read(), flags=re.M)[1:]:
        pid = block.split('\n', 1)[0].strip()
        m = re.search(r'^Pulls in:\s*(\w+)\s*\|?\s*(.*)$', block, re.M)
        out[pid] = (m.group(1).lower() == 'yes', m.group(2).strip()) if m else (None, '')
    return out


def score(mod, here, set_path, trust_path):
    tset = json.load(open(set_path, encoding='utf-8'))
    items = mod.scan_items()
    listen = mod.parse_listener()
    li, pl = {}, {}
    import glob
    for f in sorted(glob.glob(os.path.join(here, 'listener', 'L*.md'))):
        li.update(listener_items(f))
        pl.update(pulls(f))
    trust = json.load(open(trust_path, encoding='utf-8')) if os.path.exists(trust_path) else {}
    rows = []
    for e in tset:
        key = 'tree/' + e['id']
        r = dict(listen[e['id']])
        r['pull'], r['pull_note'] = pl.get(e['id'], (None, ''))
        rf = rigor_findings(items.get(key, []), trust.get(e['id']))
        cf = craft_findings(r, li.get(e['id']), e['words'], e['floor'])
        rl = any(f['size'] == 'large' for f in rf)
        cl = any(f['size'] == 'large' for f in cf)
        rg, rload = letter(sum(f['weight'] for f in rf), e['words'], rl)
        cg, cload = letter(sum(f['weight'] for f in cf), e['words'], cl)
        mean = (POINTS[rg] + POINTS[cg]) / 2
        if mean == int(mean):
            ov = LETTER[int(mean)]
        else:
            ov = LETTER[int(mean)] if POINTS[rg] < POINTS[cg] else LETTER[int(mean) + 1]
        if (rl or cl) and POINTS[ov] > POINTS[LARGE_CAP]:
            ov = LARGE_CAP
        rows.append({'id': e['id'], 'name': e['name'], 'kind': e['kind'], 'era': e['era'], 'batch': e['batch'],
                     'reference': bool(e['reference']), 'words': e['words'],
                     'rigor': rg, 'rigor_load': rload, 'craft': cg, 'craft_load': cload,
                     'overall': ov, 'action': ACTION[ov], 'findings': rf + cf})
    return rows


def strict(row):
    """The stricter reading of the truth guard: every modern guess is large. Shown, not used."""
    rf = [dict(f) for f in row['findings'] if f['dim'] == 'rigor']
    hit = False
    for f in rf:
        if f['kind'] == 'guess':
            f['weight'], hit = SIZE['large'], True
    if not hit:
        return None
    rg, _ = letter(sum(f['weight'] for f in rf), row['words'], True)
    return rg


def main():
    today = load('grade28', os.path.join(HERE, 'grade.py'))
    nov25 = load('grade25', os.path.join(NOV25, 'grade.py'))
    rows = score(today, HERE, os.path.join(HERE, 'Set.json'), os.path.join(HERE, 'trust', 'Trust_Results.json'))
    old = {r['id']: r for r in json.load(open(os.path.join(HERE, 'Grades.json'), encoding='utf-8'))}
    for x in rows:
        o = old[x['id']]
        x.update({'old_conversion': o['overall'], 'old_conversion_rigor': o['rigor'], 'old_conversion_craft': o['craft'],
                  'old_live': o['old_overall'], 'strict_rigor': strict(x)})
    rows.sort(key=lambda x: (POINTS[x['overall']], x['id']))
    json.dump(rows, open(os.path.join(HERE, 'Grades_Whole.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    cols = ['id', 'name', 'words', 'rigor', 'rigor_load', 'craft', 'craft_load', 'overall', 'action',
            'old_conversion', 'old_conversion_rigor', 'old_conversion_craft', 'old_live', 'strict_rigor']
    with open(os.path.join(HERE, 'Grades_Whole.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    cal = score(nov25, NOV25, os.path.join(NOV25, 'Set.json'), os.path.join(NOV25, 'trust', 'Trust_Results.json'))
    old25 = {r['id']: r for r in csv.DictReader(open(os.path.join(NOV25, 'Grades.csv'), encoding='utf-8'))}
    for x in cal:
        x['old_conversion'] = old25[x['id']]['overall']
    weak = [x for x in cal if x['old_conversion'] in 'DF']
    summary = {
        'today_new': dict(Counter(x['overall'] for x in rows)), 'today_old': dict(Counter(x['old_conversion'] for x in rows)),
        'nov25_new': dict(Counter(x['overall'] for x in cal)), 'nov25_old': dict(Counter(x['old_conversion'] for x in cal)),
        'nov25_old_D_or_F_now': dict(Counter(x['overall'] for x in weak)),
        'nov25_kit_new': dict(Counter(x['overall'] for x in cal if x['batch'] != 'before the kit')),
        'nov25_kit_old': dict(Counter(x['old_conversion'] for x in cal if x['batch'] != 'before the kit')),
        'nov25_before_kit_new': dict(Counter(x['overall'] for x in cal if x['batch'] == 'before the kit')),
        'nov25_before_kit_old': dict(Counter(x['old_conversion'] for x in cal if x['batch'] == 'before the kit')),
        'references': [{k: x[k] for k in ('name', 'rigor', 'craft', 'overall', 'old_conversion')} for x in cal if x['reference']],
        'moses_the_black': [{k: x[k] for k in ('rigor', 'craft', 'overall', 'old_conversion')} for x in cal if x['id'] == 'moses-the-black'],
        'bare_set_aside': {'today': sum(1 for x in rows for f in x['findings'] if f['size'] == 'note'),
                           'nov25': sum(1 for x in cal for f in x['findings'] if f['size'] == 'note'),
                           'nov25_bare_all': sum(1 for x in cal for f in x['findings'] if f['kind'] == 'bare')},
    }
    json.dump({'summary': summary, 'rows': [{k: x[k] for k in ('id', 'name', 'batch', 'reference', 'words', 'rigor', 'craft', 'overall', 'old_conversion')} for x in cal]},
              open(os.path.join(HERE, 'Calibration_Whole.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(json.dumps(summary, indent=0))


if __name__ == '__main__':
    main()
