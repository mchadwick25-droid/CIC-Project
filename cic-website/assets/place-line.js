(function (root) {
  function joinNames(list) {
    return list.length < 2 ? (list[0] || '') : list.slice(0, -1).join(', ') + ' and ' + list[list.length - 1];
  }
  function formatPlace(entry, opts) {
    const today = !!(opts && opts.today);
    const label = (entry && entry.placeLabel) || '';
    if (!label) return '';
    const beyond = / and beyond$/.test(label);
    const places = label.replace(/ and beyond$/, '').split(' · ');
    const named = new Set(places);
    const qualifiers = entry.placeQualifiers || {};
    const byPlace = {};
    const isCountry = {};
    (entry.modernCountries || []).forEach(c => {
      const list = byPlace[c.place] || (byPlace[c.place] = []);
      if (!list.includes(c.country)) list.push(c.country);
    });
    (entry.modernCountries || []).forEach(c => {
      if (c.placeId && c.placeId === c.countryId && byPlace[c.place].length === 1) isCountry[c.country] = c.place;
    });
    const omit = ((opts && opts.omitIn) || '').toLowerCase();
    const shown = p => !omit || !omit.includes(p.toLowerCase());
    const said = c => (named.has(c) && shown(c)) || (named.has(isCountry[c]) && shown(isCountry[c]));
    const groups = [];
    places.forEach(p => {
      const countries = (byPlace[p] || []).filter(c => !said(c));
      const key = countries.join('|');
      const last = groups[groups.length - 1];
      if (last && key && last.key === key) last.places.push(p);
      else groups.push({ places: [p], countries, key });
    });
    const parts = groups.map(g => {
      const visible = g.places.filter(shown).map(p => p + (qualifiers[p] || ''));
      const hiddenQualifiers = g.places.filter(p => !shown(p) && qualifiers[p]).map(p => qualifiers[p].replace(/^[\s,(]+|\)$/g, ''));
      const where = visible.concat(hiddenQualifiers).join(' · ');
      const countries = g.countries.length ? joinNames(g.countries) : '';
      if (!where) return countries ? (today ? 'today in ' : '') + countries : '';
      return where + (countries ? (today ? ', today in ' : ', ') + countries : '');
    }).filter(Boolean);
    if (!parts.length) return '';
    return parts.join(' · ') + (beyond ? ' and beyond' : '');
  }
  root.CFTPlace = { formatPlace };
})(typeof globalThis !== 'undefined' ? globalThis : this);
