(function () {
  const S = window.CFTSearch;
  const CSS = `
#searchPanel{position:fixed;z-index:24;left:.6rem;top:calc(var(--map-top,8rem) + .4rem);width:min(28rem,calc(100vw - 1.2rem));max-height:calc(100vh - var(--map-top,8rem) - var(--bar-h,56px) - 1.4rem);overflow:auto;box-sizing:border-box;background:var(--vellum);border:1px solid var(--gold-leaf);border-radius:10px;box-shadow:var(--shadow);padding:.7rem .8rem .8rem;color:var(--iron-gall);font:1.05rem/1.4 "Alegreya Sans",sans-serif}
#searchPanel[hidden]{display:none}
#searchPanel .sp-head{display:flex;gap:.5rem;align-items:center;margin:0 0 .4rem}
#searchPanel label{font-weight:700;flex:1}
#searchPanel .sp-close{min-height:44px;min-width:44px;background:none;border:0;font-size:1.5rem;color:var(--iron-gall);cursor:pointer}
#searchPanel input{display:block;width:100%;box-sizing:border-box;min-height:44px;padding:0 .7rem;font:inherit;color:var(--iron-gall);background:var(--parchment);border:1px solid var(--graphite);border-radius:8px}
#searchPanel input:focus-visible,#searchPanel button:focus-visible,#searchPanel [role=option].active{outline:2px solid var(--madder);outline-offset:2px}
#searchPanel [role=listbox]{margin:.5rem 0 0;padding:0}
#searchPanel [role=option]{display:block;padding:.45rem .6rem;border-radius:8px;cursor:pointer;min-height:44px;box-sizing:border-box}
#searchPanel [role=option]:hover,#searchPanel [role=option].active{background:var(--parchment)}
#searchPanel .sp-t{display:block;font-weight:700}
#searchPanel .sp-d{display:block;font-size:.95rem;color:var(--ink-faded)}
#searchPanel .sp-note{margin:.5rem .3rem 0}
#searchPanel .sp-act{min-height:44px;padding:0 .8rem;font:700 1rem "Alegreya Sans",sans-serif;color:var(--iron-gall);background:var(--parchment);border:1px solid var(--graphite);border-radius:8px;cursor:pointer}
`;
  const LIMIT = 6;
  const el = (tag, attrs, text) => {
    const n = document.createElement(tag);
    for (const k in attrs || {}) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    return n;
  };
  const plural = (n, one, many) => `${n} ${n === 1 ? one : many}`;
  const SMALL = new Set(['of', 'the', 'and', 'in', 'on', 'for', 'de', 'von', 'van', 'to']);
  const titleCase = (s) => s.split(' ').map((w, i) => (i && SMALL.has(w) ? w : w.charAt(0).toUpperCase() + w.slice(1))).join(' ');
  const ordinal = (n) => n + (n % 100 > 10 && n % 100 < 14 ? 'th' : ['th', 'st', 'nd', 'rd'][n % 10 < 4 ? n % 10 : 0]);
  const plainDates = (e) => (e.dates || '').replace(/-/g, '–');

  function open(hooks) {
    if (!open.ui) open.ui = create(hooks);
    open.ui.show();
  }

  function create(hooks) {
    document.head.appendChild(el('style')).textContent = CSS;
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
    const list = el('div', { id: 'searchList', role: 'listbox', 'aria-label': 'Results' });
    list.hidden = true;
    const note = el('div', { class: 'sp-note' });
    const status = el('div', { class: 'sr-only', role: 'status', 'aria-live': 'polite' });
    panel.append(head, input, list, note, status);
    document.body.appendChild(panel);

    let searcher = null, loading = null, last = '', options = [], active = -1, timer = 0, announceTimer = 0, opener = null;
    const load = () => loading || (loading = fetch('data/search/names.json').then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }).then((index) => {
      const living = new Set(index.living);
      const rows = index.entries.map((id, i) => { const e = infoById.get(id); if (e) e.living = living.has(i); return e || null; });
      searcher = S.createSearcher(index, rows, null);
      searcher.rows = rows;
    }, (err) => { loading = null; throw err; }));

    function say(text) { clearTimeout(announceTimer); announceTimer = setTimeout(() => { status.textContent = ''; setTimeout(() => { status.textContent = text; }, 40); }, 700); }
    function setActive(n) {
      options.forEach((o, i) => o.node.classList.toggle('active', i === n));
      active = n;
      if (n >= 0) { input.setAttribute('aria-activedescendant', options[n].node.id); options[n].node.scrollIntoView({ block: 'nearest' }); }
      else input.removeAttribute('aria-activedescendant');
    }
    function clear() {
      input.removeAttribute('aria-activedescendant');
      list.textContent = ''; list.hidden = true; note.textContent = ''; options = []; active = -1;
      input.setAttribute('aria-expanded', 'false');
    }
    function close() {
      panel.hidden = true;
      if (hooks.button) hooks.button.setAttribute('aria-expanded', 'false');
    }
    function choose(run) { close(); run(); }

    const litIds = (ids) => ids.filter((i) => searcher.rows[i] && searcher.rows[i].kind === 't').map((i) => searcher.rows[i].id);

    // One flat list: a year or a country first, then names. Exact names come first, then (for a broad word)
    // the traditions that are alive today, then the rest by date.
    function choices(r) {
      const out = [];
      if (r.date) {
        const d = r.date, ids = litIds(d.ids), n = ids.length;
        const span = d.type === 'year' ? `${d.a}` : d.type === 'century' ? `the ${ordinal(d.n)} century` : `${d.a} to ${d.b}`;
        if (n) out.push({ title: d.type === 'year' ? `The year ${span}` : span.charAt(0).toUpperCase() + span.slice(1), desc: `Lights ${plural(n, 'tradition', 'traditions')} on the map`, run: () => hooks.lightSet(ids, `${plural(n, 'tradition', 'traditions')} in ${span}`) });
        return out;
      }
      for (const p of r.places.filter((x) => x.rank <= 2)) {
        const ids = litIds(p.ids), n = ids.length;
        if (!n) continue;
        const title = p.alias ? titleCase(p.alias) : p.label;
        out.push({ title, desc: `${p.note && p.alias ? `${p.note} for ${p.label}. ` : ''}Lights ${plural(n, 'tradition', 'traditions')} on the map`, run: () => hooks.lightSet(ids, `${plural(n, 'tradition', 'traditions')} in ${p.label}`) });
      }
      const rank0 = r.entries.filter((h) => h.rank === 0), rest = r.entries.filter((h) => h.rank > 0);
      const isT = (h) => searcher.rows[h.i].kind === 't' || searcher.rows[h.i].kind === 'm';
      const broad = r.query.trim().split(/\s+/).length === 1 && rest.filter(isT).length >= 6;
      const ordered = broad
        ? [...rank0, ...rest.filter((h) => isT(h) && searcher.rows[h.i].living), ...rest.filter((h) => isT(h) && !searcher.rows[h.i].living), ...rest.filter((h) => !isT(h))]
        : [...rank0, ...rest];
      for (const hit of ordered) {
        const e = searcher.rows[hit.i];
        let said = '';
        if (hit.via !== 'n' && hit.via !== 's' && hit.via !== 'e' && hit.rank <= 3 && S.NAME_NOTE[hit.via] && hit.matched !== S.normalize(e.short || e.name)) said = `“${titleCase(hit.matched)}”, ${S.NAME_NOTE[hit.via]}`;
        out.push({ title: e.short || e.name, desc: [said, plainDates(e)].filter(Boolean).join(' · '), run: () => hooks.openEntry(moveById.get(e.id)) });
      }
      return out;
    }

    function render(r, all) {
      clear();
      const shown = all.slice(0, LIMIT);
      shown.forEach((o, n) => {
        const node = el('div', { role: 'option', id: `so-${n}`, 'aria-selected': 'false' });
        node.append(el('span', { class: 'sp-t' }, o.title), el('span', { class: 'sp-d' }, o.desc));
        node.addEventListener('mousedown', (ev) => ev.preventDefault());
        node.addEventListener('click', () => choose(o.run));
        list.appendChild(node);
        options.push({ node, o });
      });
      list.hidden = !shown.length;
      input.setAttribute('aria-expanded', shown.length ? 'true' : 'false');
      if (shown.length) {
        if (all.length > shown.length) note.textContent = `Showing the first ${LIMIT}. Type more to narrow them.`;
        say(`${plural(all.length, 'result', 'results')}.`);
        return;
      }
      note.appendChild(document.createTextNode(`Nothing matches “${r.query.trim()}”. `));
      if (r.nearest) {
        note.appendChild(document.createTextNode('Did you mean '));
        const b = el('button', { type: 'button', class: 'sp-act' }, r.nearest);
        b.addEventListener('click', () => { input.value = r.nearest; run(r.nearest); input.focus(); });
        note.append(b, '?');
      }
      say(`No results for ${r.query.trim()}.`);
    }

    async function run(query) {
      const q = query.trim();
      last = q;
      if (!q) { clear(); return; }
      try { await load(); } catch (e) { clear(); note.textContent = 'Search did not load. Check your connection, then try again.'; return; }
      if (q !== last) return;
      const r = searcher.search(q);
      render(r, choices(r));
    }

    input.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(() => run(input.value), 140); });
    input.addEventListener('keydown', (ev) => {
      if (ev.key === 'ArrowDown') { ev.preventDefault(); if (options.length) setActive((active + 1) % options.length); }
      else if (ev.key === 'ArrowUp') { ev.preventDefault(); if (options.length) setActive(active <= 0 ? options.length - 1 : active - 1); }
      else if (ev.key === 'Enter') {
        ev.preventDefault();
        const o = options[active >= 0 ? active : 0];
        if (o) choose(o.o.run); else { clearTimeout(timer); run(input.value); }
      }
    });
    panel.addEventListener('keydown', (ev) => { if (ev.key === 'Escape') { ev.preventDefault(); ev.stopPropagation(); close(); (opener || hooks.button).focus(); } });
    head.querySelector('.sp-close').addEventListener('click', () => { close(); (opener || hooks.button).focus(); });

    return {
      show() {
        opener = document.activeElement && document.activeElement !== document.body ? document.activeElement : hooks.button;
        panel.hidden = false;
        if (hooks.button) hooks.button.setAttribute('aria-expanded', 'true');
        input.focus(); input.select();
        load().catch(() => { note.textContent = 'Search did not load. Check your connection, then try again.'; });
      },
    };
  }

  window.CFTSearchUI = { open };
})();
