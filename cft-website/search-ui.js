(function () {
  const S = window.CFTSearch;
  const CSS = `
#searchPanel{position:fixed;z-index:24;left:.6rem;top:calc(var(--map-top,8rem) + .4rem);width:min(32rem,calc(100vw - 1.2rem));max-height:calc(100vh - var(--map-top,8rem) - var(--bar-h,56px) - 1.4rem);overflow:auto;box-sizing:border-box;background:var(--vellum);border:1px solid var(--gold-leaf);border-radius:10px;box-shadow:var(--shadow);padding:.7rem .8rem .8rem;color:var(--iron-gall);font:1.05rem/1.4 "Alegreya Sans",sans-serif}
#searchPanel[hidden]{display:none}
#searchPanel .sp-head{display:flex;gap:.5rem;align-items:center;margin:0 0 .4rem}
#searchPanel label{font-weight:700;flex:1}
#searchPanel .sp-close{min-height:44px;min-width:44px;background:none;border:0;font-size:1.5rem;color:var(--iron-gall);cursor:pointer}
#searchPanel input{display:block;width:100%;box-sizing:border-box;min-height:44px;padding:0 .7rem;font:inherit;color:var(--iron-gall);background:var(--parchment);border:1px solid var(--graphite);border-radius:8px}
#searchPanel input:focus-visible,#searchPanel button:focus-visible,#searchPanel a:focus-visible,#searchPanel [role=option].active{outline:2px solid var(--madder);outline-offset:2px}
#searchPanel [role=listbox],#searchPanel ul{list-style:none;margin:.5rem 0 0;padding:0}
#searchPanel [role=group]{list-style:none;margin:.5rem 0 0;padding:0}
#searchPanel .sp-h{font:700 .85rem "Alegreya Sans",sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faded);padding:.2rem .3rem}
#searchPanel .sp-line{font-size:.95rem;color:var(--ink-faded);padding:0 .3rem .2rem}
#searchPanel [role=option]{display:block;padding:.45rem .6rem;border-radius:8px;cursor:pointer;min-height:44px;box-sizing:border-box}
#searchPanel [role=option]:hover,#searchPanel [role=option].active{background:var(--parchment)}
#searchPanel .sp-t{display:block;font-weight:700}
#searchPanel .sp-d{display:block;font-size:.95rem;color:var(--ink-faded)}
#searchPanel .sp-act,#searchPanel .sp-all{min-height:44px;padding:0 .8rem;font:700 1rem "Alegreya Sans",sans-serif;color:var(--iron-gall);background:var(--parchment);border:1px solid var(--graphite);border-radius:8px;cursor:pointer}
#searchPanel .sp-full h2{font:700 1rem "Alegreya Sans",sans-serif;margin:.8rem 0 .2rem}
#searchPanel .sp-full li{display:flex;gap:.5rem;align-items:center;justify-content:space-between;padding:.2rem 0;border-bottom:1px solid var(--rule)}
#searchPanel .sp-none p{margin:.4rem 0}
#searchPanel .sp-row{display:flex;flex-wrap:wrap;gap:.4rem;margin:.3rem 0}
`;
  const GROUPS = [
    ['t', 'Traditions'], ['p', 'People'], ['c', 'Councils'], ['places', 'Places'], ['parts', 'Parts of the map'], ['text', 'Found in the text'],
  ];
  const LIMIT = 4;
  const el = (tag, attrs, text) => {
    const n = document.createElement(tag);
    for (const k in attrs || {}) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    return n;
  };
  const plural = (n, one, many) => `${n} ${n === 1 ? one : many}`;
  const joinWords = (list) => (list.length < 2 ? list[0] || '' : list.slice(0, -1).join(', ') + ' and ' + list[list.length - 1]);
  const SMALL = new Set(['of', 'the', 'and', 'in', 'on', 'for', 'de', 'von', 'van', 'to']);
  const titleCase = (s) => s.split(' ').map((w, i) => (i && SMALL.has(w) ? w : w.charAt(0).toUpperCase() + w.slice(1))).join(' ');
  const ordinal = (n) => n + (n % 100 > 10 && n % 100 < 14 ? 'th' : ['th', 'st', 'nd', 'rd'][n % 10 < 4 ? n % 10 : 0]);
  const plainDates = (e) => (e.dates || '').replace(/-/g, '–');

  function open(hooks) {
    if (open.ui) return open.ui.show();
    const ui = open.ui = create(hooks);
    ui.show();
  }

  function create(hooks) {
    const style = document.head.appendChild(el('style'));
    style.textContent = CSS;
    const movements = hooks.movements;
    const info = movements.map((m) => ({
      id: m.id, name: m.name, short: m.shortName && m.shortName !== m.name ? m.shortName : '',
      kind: m.kind === 'person' ? 'p' : m.kind === 'major-council' ? 'c' : m.kind ? 'm' : 't',
      start: m.start, end: m.end, living: false, dates: m.dates,
      countries: [...new Set((m.modernCountries || []).map((c) => c.country))], place: m.placeLabel || '',
    }));
    const infoById = new Map(info.map((e) => [e.id, e])), moveById = new Map(movements.map((m) => [m.id, m]));
    const panel = el('div', { id: 'searchPanel', role: 'dialog', 'aria-label': 'Search the tree' });
    panel.hidden = true;
    const head = el('div', { class: 'sp-head' });
    head.append(el('label', { for: 'searchInput' }, 'Search the tree'), el('button', { type: 'button', class: 'sp-close', 'aria-label': 'Close search' }, '×'));
    const input = el('input', { id: 'searchInput', type: 'search', role: 'combobox', 'aria-expanded': 'false', 'aria-controls': 'searchList', 'aria-autocomplete': 'list', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', placeholder: 'A name, a country or a year' });
    const hint = el('p', { class: 'sp-line', id: 'searchHint' }, 'Try a church, a person, a country, a year or a word.');
    input.setAttribute('aria-describedby', 'searchHint');
    const list = el('div', { id: 'searchList', role: 'listbox', 'aria-label': 'Results' });
    const body = el('div', { class: 'sp-body' });
    const status = el('div', { class: 'sr-only', role: 'status', 'aria-live': 'polite' });
    panel.append(head, input, hint, list, body, status);
    document.body.appendChild(panel);

    let textTokens = [], searcher = null, loading = null, wordMap = null, wordsLoading = null, last = null, options = [], active = -1, timer = 0, announceTimer = 0, opener = null;
    const load = () => loading || (loading = fetch('data/search/names.json').then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }).then((index) => {
      const living = new Set(index.living);
      const rows = index.entries.map((id, i) => { const e = infoById.get(id); if (e) e.living = living.has(i); return e || null; });
      searcher = S.createSearcher(index, rows, null);
      searcher.rows = rows;
    }));
    const loadWords = () => wordsLoading || (wordsLoading = fetch('data/search/words.json').then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }).then((w) => { wordMap = S.decodeWordList(w); }));

    function say(text) { clearTimeout(announceTimer); announceTimer = setTimeout(() => { status.textContent = ''; setTimeout(() => { status.textContent = text; }, 40); }, 700); }

    function setActive(n) {
      options.forEach((o, i) => o.node.classList.toggle('active', i === n));
      active = n;
      if (n >= 0) { input.setAttribute('aria-activedescendant', options[n].node.id); options[n].node.scrollIntoView({ block: 'nearest' }); }
      else input.removeAttribute('aria-activedescendant');
    }

    function close() {
      panel.hidden = true; input.setAttribute('aria-expanded', 'false');
      if (hooks.button) hooks.button.setAttribute('aria-expanded', 'false');
    }
    function done(fn) { close(); fn(); }

    function entryOption(hit) {
      const e = searcher.rows[hit.i], m = moveById.get(e.id);
      let note = '';
      if (hit.via !== 'n' && hit.via !== 's' && hit.via !== 'e' && hit.rank <= 3) {
        const asked = hit.matched, shown = S.normalize(e.short || e.name);
        if (asked !== shown && S.NAME_NOTE[hit.via]) note = `“${titleCase(asked)}”, ${S.NAME_NOTE[hit.via]}`;
      }
      const dates = plainDates(e);
      return { title: e.short || e.name, desc: [note, dates].filter(Boolean).join(' · '), entryId: e.id, run: () => hooks.openEntry(m) };
    }

    function litIds(ids) { return ids.filter((i) => searcher.rows[i] && searcher.rows[i].kind === 't').map((i) => searcher.rows[i].id); }

    function compute(r, text) {
      const g = { t: [], p: [], c: [], places: [], parts: [], text: [] };
      const exact = r.entries.filter((h) => h.rank === 0), rest = r.entries.filter((h) => h.rank > 0);
      const trad = r.entries.filter((h) => searcher.rows[h.i].kind === 't' || searcher.rows[h.i].kind === 'm');
      const broad = r.query.trim().split(/\s+/).length === 1 && trad.filter((h) => h.rank > 0).length >= 6;
      let ordered = [...exact, ...rest];
      if (broad) {
        const isT = (h) => searcher.rows[h.i].kind === 't' || searcher.rows[h.i].kind === 'm';
        const liv = rest.filter((h) => isT(h) && searcher.rows[h.i].living);
        const ear = rest.filter((h) => isT(h) && !searcher.rows[h.i].living);
        ordered = [...exact, ...liv, ...ear, ...rest.filter((h) => !isT(h))];
      }
      for (const h of ordered) {
        const kind = searcher.rows[h.i].kind;
        const opt = entryOption(h);
        opt.live = broad && kind !== 'p' && kind !== 'c' ? (exact.includes(h) ? 'exact' : searcher.rows[h.i].living ? 'living' : 'earlier') : '';
        g[kind === 'm' ? 't' : kind].push(opt);
      }
      for (const p of r.places) {
        const ids = litIds(p.ids), n = ids.length;
        const label = n === 0 ? `No traditions list ${p.label} yet` : `${plural(n, 'tradition', 'traditions')} in ${p.label}`;
        const title = p.alias ? p.alias.replace(/\b\w/g, (c) => c.toUpperCase()) : p.label;
        const lead = p.note && p.alias ? `${p.note} (${p.label}). ` : '';
        g.places.push({ title, desc: `${lead}${n ? `Lights ${plural(n, 'tradition', 'traditions')} that name ${p.label} as a modern country or place.` : 'No tradition lists this place yet.'} Entries without a place recorded are not found.`, run: n ? () => hooks.lightSet(ids, label) : null });
      }
      if (r.date) {
        const d = r.date, ids = litIds(d.ids), n = ids.length;
        const span = d.type === 'year' ? `${d.a}` : d.type === 'century' ? `the ${ordinal(d.n)} century` : `${d.a} to ${d.b}`;
        g.parts.unshift({ title: d.type === 'year' ? `The year ${span}` : span.charAt(0).toUpperCase() + span.slice(1), desc: n ? `Lights ${plural(n, 'tradition', 'traditions')} whose dates include ${d.type === 'year' ? 'this year' : 'these years'}. Dates are the span each tradition covers.` : 'No tradition has dates that cover this.', run: n ? () => hooks.lightSet(ids, `${plural(n, 'tradition', 'traditions')} in ${span}`) : null });
      }
      for (const p of r.parts) {
        if (p.type === 'era') { const row = searcher.eraRows[p.at]; g.parts.push({ title: row.label, desc: `${row.dates} · Moves the map to this era`, run: () => hooks.goEra(row.num) }); }
        else g.parts.push({ title: p.label, desc: `${p.common ? p.common + ' · ' : ''}Moves the map to this river`, run: () => hooks.goRiver(p.k) });
      }
      if (text && text.ids.length) {
        const quoted = joinWords(text.shown.map((t) => `“${t}”`));
        g.textLine = `${plural(text.ids.length, 'entry uses', 'entries use')} ${quoted}. Other entries may cover the subject in other words.`;
        for (const i of text.ids.slice(0, 60)) {
          if (!searcher.rows[i]) continue;
          const e = searcher.rows[i];
          g.text.push({ title: e.short || e.name, desc: '', index: i, entryId: e.id, run: () => hooks.openEntry(moveById.get(e.id)) });
        }
      } else if (text) g.textLine = text.shown.length ? `No entry uses ${joinWords(text.shown.map((t) => `“${t}”`))}${text.shown.length > 1 ? ' together' : ''}. Other entries may cover the subject in other words.` : '';
      return g;
    }

    function render(r, g) {
      list.textContent = ''; body.textContent = ''; options = []; active = -1;
      input.removeAttribute('aria-activedescendant');
      const total = GROUPS.reduce((n, [k]) => n + g[k].length, 0);
      const shownCap = (k) => g[k].slice(0, LIMIT);
      let n = 0;
      for (const [k, title] of GROUPS) {
        const items = shownCap(k);
        if (!items.length && !(k === 'text' && g.textLine && total)) continue;
        const ul = el('div', { role: 'group', 'aria-labelledby': `sg-${k}` });
        ul.append(el('div', { role: 'presentation', class: 'sp-h', id: `sg-${k}` }, title));
        if (k === 'text' && g.textLine) ul.append(el('div', { role: 'presentation', class: 'sp-line' }, g.textLine));
        let lastLive = '';
        for (const o of items) {
          if (o.live && o.live !== lastLive && k === 't') { lastLive = o.live; if (o.live === 'living') ul.append(el('div', { role: 'presentation', class: 'sp-line' }, 'Living today')); else if (o.live === 'earlier') ul.append(el('div', { role: 'presentation', class: 'sp-line' }, 'Earlier, by date')); }
          const node = el('div', { role: 'option', id: `so-${n}`, 'aria-selected': 'false' });
          node.append(el('span', { class: 'sp-t' }, o.title), el('span', { class: 'sp-d' }, o.desc));
          if (!o.run) node.setAttribute('aria-disabled', 'true');
          node.addEventListener('mousedown', (ev) => ev.preventDefault());
          node.addEventListener('click', () => { if (o.run) done(o.run); });
          ul.appendChild(node);
          options.push({ node, o });
          n++;
        }
        list.appendChild(ul);
      }
      if (total > GROUPS.reduce((c, [k]) => c + shownCap(k).length, 0)) {
        const node = el('div', { role: 'option', id: `so-${n}`, 'aria-selected': 'false' });
        node.append(el('span', { class: 'sp-t' }, `See all ${total} results`), el('span', { class: 'sp-d' }, 'Opens the whole list here, with links to each page.'));
        node.addEventListener('mousedown', (ev) => ev.preventDefault());
        node.addEventListener('click', () => showFull(r, g));
        const o = { run: () => showFull(r, g), keep: true };
        list.appendChild(node);
        options.push({ node, o });
      }
      input.setAttribute('aria-expanded', options.length ? 'true' : 'false');
      list.hidden = !options.length;
      if (!total) renderNone(r, g);
      if (g.textLine == null && r.query.trim().length > 2 && total) {
        const row = el('div', { class: 'sp-row' });
        const b = el('button', { type: 'button', class: 'sp-act' }, 'Also look in the text');
        b.addEventListener('click', () => run(r.query, true));
        row.appendChild(b); body.appendChild(row);
      }
      return total;
    }

    function renderNone(r, g) {
      const box = el('div', { class: 'sp-none' });
      const where = g.textLine != null ? ', in a name or in the text' : '';
      box.appendChild(el('p', {}, `Nothing in the tree matches “${r.query.trim()}”${where}.${g.textLine != null ? ' Other entries may cover the subject in other words.' : ''}`));
      if (r.nearest) {
        const p = el('p', {}, 'The nearest name is ');
        const b = el('button', { type: 'button', class: 'sp-act' }, r.nearest);
        b.addEventListener('click', () => { input.value = r.nearest; run(r.nearest); input.focus(); });
        p.append(b, '.');
        box.appendChild(p);
      }
      box.appendChild(el('p', {}, 'Or go to a part of the map:'));
      const eras = el('div', { class: 'sp-row', role: 'group', 'aria-label': 'Eras' });
      searcher.eraRows.forEach((e) => { const b = el('button', { type: 'button', class: 'sp-act' }, e.label); b.addEventListener('click', () => done(() => hooks.goEra(e.num))); eras.appendChild(b); });
      const rivers = el('div', { class: 'sp-row', role: 'group', 'aria-label': 'Rivers' });
      searcher.riverRows.forEach((rv) => { const b = el('button', { type: 'button', class: 'sp-act' }, rv.label); b.addEventListener('click', () => done(() => hooks.goRiver(rv.k))); rivers.appendChild(b); });
      box.append(eras, rivers);
      body.appendChild(box);
    }

    function showFull(r, g) {
      list.hidden = true; list.textContent = ''; body.textContent = ''; options = []; input.setAttribute('aria-expanded', 'false'); input.removeAttribute('aria-activedescendant');
      const wrap = el('div', { class: 'sp-full' });
      const back = el('button', { type: 'button', class: 'sp-act' }, 'Back to the short list');
      back.addEventListener('click', () => { render(r, g); input.focus(); });
      wrap.appendChild(back);
      for (const [k, title] of GROUPS) {
        if (!g[k].length) continue;
        wrap.appendChild(el('h2', {}, `${title} (${g[k].length})`));
        if (k === 'text' && g.textLine) wrap.appendChild(el('p', { class: 'sp-line' }, g.textLine));
        const ul = el('ul');
        for (const o of g[k]) {
          const li = el('li');
          const left = el('span');
          if (o.entryId) left.appendChild(el('a', { href: hooks.href(o.entryId) }, o.title));
          else left.appendChild(document.createTextNode(o.title));
          if (o.desc) left.appendChild(el('span', { class: 'sp-d' }, o.desc));
          li.appendChild(left);
          if (o.run) { const b = el('button', { type: 'button', class: 'sp-act' }, k === 'places' || k === 'parts' ? 'Show' : 'Show on the map'); b.addEventListener('click', () => done(o.run)); li.appendChild(b); }
          ul.appendChild(li);
        }
        wrap.appendChild(ul);
      }
      body.appendChild(wrap);
      wrap.querySelector('a, button').focus();
    }

    async function fillSentences(g, token) {
      const shown = g.text.slice(0, LIMIT);
      for (const o of shown) {
        const m = moveById.get(o.entryId);
        try {
          const wait = hooks.ensureEntry(m); if (wait) await wait;
        } catch (e) { continue; }
        if (token !== last) return;
        const s = S.bestSentence(S.visibleText(m), textTokens);
        if (s) { o.desc = s; const opt = options.find((x) => x.o === o); if (opt) opt.node.querySelector('.sp-d').textContent = s; }
      }
    }

    async function run(query, forceText) {
      const q = query.trim();
      if (!q) { input.removeAttribute('aria-activedescendant'); list.hidden = true; list.textContent = ''; body.textContent = ''; options = []; input.setAttribute('aria-expanded', 'false'); return; }
      const token = last = q + (forceText ? '*' : '');
      try { await load(); } catch (e) { body.textContent = 'Search did not load. Check your connection, then try again.'; return; }
      if (token !== last) return;
      const r = searcher.search(q);
      let text = null;
      if (forceText || r.question || (!r.strong && !r.date)) {
        try { await loadWords(); } catch (e) { body.textContent = 'The text search did not load. Check your connection, then try again.'; return; }
        if (token !== last) return;
        text = S.searchWords(wordMap, q);
        textTokens = text.tokens;
      }
      const g = compute(r, text);
      const total = render(r, g);
      say(total ? `${plural(total, 'result', 'results')}.` : `No results for ${q}.`);
      if (text && g.text.length) fillSentences(g, token);
    }

    input.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => run(input.value), 140); });
    input.addEventListener('keydown', (ev) => {
      if (ev.key === 'ArrowDown') { ev.preventDefault(); if (options.length) setActive((active + 1) % options.length); }
      else if (ev.key === 'ArrowUp') { ev.preventDefault(); if (options.length) setActive(active <= 0 ? options.length - 1 : active - 1); }
      else if (ev.key === 'Home' && active >= 0) { ev.preventDefault(); setActive(0); }
      else if (ev.key === 'End' && active >= 0) { ev.preventDefault(); setActive(options.length - 1); }
      else if (ev.key === 'Enter') {
        ev.preventDefault();
        const o = options[active >= 0 ? active : 0];
        if (!o) { clearTimeout(timer); run(input.value); return; }
        if (o.o.keep) o.o.run(); else if (o.o.run) done(o.o.run);
      }
    });
    panel.addEventListener('keydown', (ev) => { if (ev.key === 'Escape') { ev.preventDefault(); ev.stopPropagation(); close(); (opener || input).focus(); } });
    head.querySelector('.sp-close').addEventListener('click', () => { close(); (opener || input).focus(); });

    return {
      show() {
        opener = document.activeElement && document.activeElement !== document.body ? document.activeElement : hooks.button;
        panel.hidden = false;
        if (hooks.button) hooks.button.setAttribute('aria-expanded', 'true');
        input.focus(); input.select();
        load().catch(() => { body.textContent = 'Search did not load. Check your connection, then try again.'; });
      },
    };
  }

  window.CFTSearchUI = { open };
})();
