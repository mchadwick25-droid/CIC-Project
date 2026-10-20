(function () {
"use strict";

var MAX_SEATS = 3;
var HAND_SIZE = 5;
var HAND_CAP = 8;
var FALLBACK_TINT = "#D9B35C";

function el(tag, attrs, kids) {
  var n = document.createElement(tag);
  if (attrs) Object.keys(attrs).forEach(function (k) {
    if (k === "text") n.textContent = attrs[k];
    else if (k === "class") n.className = attrs[k];
    else if (attrs[k] === true) n.setAttribute(k, "");
    else if (attrs[k] !== false && attrs[k] != null) n.setAttribute(k, attrs[k]);
  });
  (kids || []).forEach(function (c) { if (c) n.appendChild(c); });
  return n;
}
function pad2(n) { return (n < 10 ? "0" : "") + n; }
function shuffleIndex(len) { return Math.floor(Math.random() * len); }

function init(mount, census) {
  var mode = mount.getAttribute("data-mode") === "table" ? "table" : "landing";
  var fromPage = mount.getAttribute("data-from") || "index.html#who";
  var treeHref = mount.getAttribute("data-tree") || "atlas-v3.html";

  var eras = {};
  census.eras.forEach(function (e) {
    eras[e.num] = {
      no: e.no,
      name: String(e.title || "").replace(/\s+Era$/, ""),
      dates: e.dates,
      tint: e.chooserTint || FALLBACK_TINT
    };
  });

  var worlds = census.movements
    .filter(function (m) { return m.status === "Built & Live" && m.entry && m.entry.representativeName; })
    .sort(function (a, b) { return (a.start - b.start) || (a.id < b.id ? -1 : 1); })
    .map(function (m) {
      var en = m.entry;
      return {
        id: m.id,
        era: m.era,
        rep: en.representativeName,
        role: en.representativeTitle || "",
        world: en.worldName || m.informalName || m.name,
        subtitle: en.subtitle || "",
        name: m.name,
        informal: m.informalName || "",
        dates: m.dates || "",
        place: m.region || "",
        img: en.portrait || en.icon || "",
        thumb: (en.portrait || en.icon || "").replace(/portraits\/([^/]+)\.[a-z]+$/, "portraits/thumb/$1.webp"),
        tag: en.intro || en.subtitle || "",
        shaped: Array.isArray(en.shaped) ? en.shaped.join(", ") : (en.shaped || ""),
        summary: en.tile || "",
        record: en.recordHolds || "",
        matches: Array.isArray(en.matches) ? en.matches : [],
        voices: (m.voices || []).filter(function (v) { return typeof v === "string"; }),
        start: m.start,
        end: m.end,
        topics: Array.isArray(en.topics) ? en.topics : [],
        aliases: Array.isArray(en.aliases) ? en.aliases : [],
        keywords: Array.isArray(en.keywords) ? en.keywords : []
      };
    });
  if (!worlds.length) return;
  var byId = {};
  worlds.forEach(function (w) { byId[w.id] = w; });
  var allIds = worlds.map(function (w) { return w.id; });
  var order = function (a, b) { return allIds.indexOf(a) - allIds.indexOf(b); };

  var seated = [];
  var handIds = [];
  var via = {};
  var active = 0;
  var deckOpen = false;
  var deckState = { era: 0, q: "" };
  var seen = [];
  try { seen = JSON.parse(localStorage.getItem("cic-dealt") || "[]"); } catch (e) { seen = []; }
  if (!Array.isArray(seen)) seen = [];

  if (mode === "table") {
    var pre = new URLSearchParams(window.location.search).get("worlds");
    if (pre) pre.split(",").forEach(function (s) {
      s = s.trim();
      if (byId[s] && seated.indexOf(s) < 0 && seated.length < MAX_SEATS) seated.push(s);
    });
  }

  mount.classList.add("chooser");
  mount.textContent = "";

  // ---------- deck controls ----------
  var helpId = "chooser-help-" + mode;
  var q = el("input", { type: "search", id: "chooser-q-" + mode, placeholder: "Search traditions, topics, people", autocomplete: "off", "aria-describedby": helpId });
  var erasBox = el("div", { class: "chooser-eras", role: "group", "aria-label": "Narrow by era" });
  var countEl = el("p", { class: "chooser-count", "aria-live": "polite" });
  var whyEl = el("ul", { class: "chooser-why" });
  var deckBox = el("div", { class: "chooser-deck" }, [erasBox, countEl, whyEl]);
  var searchBox = el("div", { class: "chooser-search" }, [
    el("label", { class: "vh", for: q.id, text: "Search for a tradition, a topic or a person" }),
    q,
    el("p", { class: "chooser-help", id: helpId, text: "Look for a tradition, a topic or a person. Try Lutheran, baptism or Augustine." })
  ]);
  var slotSel = mount.getAttribute("data-search-slot");
  var slot = slotSel ? document.querySelector(slotSel) : null;

  function eraChip(num, label, tint) {
    var b = el("button", { type: "button", class: "chooser-erachip", "aria-pressed": num === 0 ? "true" : "false", "data-era": String(num) });
    if (tint) { var i = el("i", { "aria-hidden": "true" }); i.style.background = tint; b.appendChild(i); }
    b.appendChild(document.createTextNode(label));
    b.addEventListener("click", function () {
      deckState.era = num;
      [].forEach.call(erasBox.children, function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      deal("era");
    });
    return b;
  }
  erasBox.appendChild(eraChip(0, "All eras"));
  var present = {};
  worlds.forEach(function (w) { present[w.era] = true; });
  Object.keys(present).map(Number).sort(function (a, b) { return a - b; }).forEach(function (n) {
    var e = eras[n];
    if (e) erasBox.appendChild(eraChip(n, e.no + ". " + e.name + ", " + e.dates, e.tint));
  });

  // ---------- hand ----------
  var hand = el("div", { class: "chooser-hand", role: "group", "aria-roledescription": "hand of cards" });
  var posEl = el("span", { class: "pos", "aria-hidden": "true" });
  var prevBtn = el("button", { type: "button", class: "cbtn roll", "aria-label": "Previous card", text: "‹ Previous" });
  var nextBtn = el("button", { type: "button", class: "cbtn roll", "aria-label": "Next card", text: "Next ›" });
  var shuffleBtn = el("button", { type: "button", class: "cbtn quiet", text: "Shuffle" });
  var allBtn = el("button", { type: "button", class: "cbtn quiet", "aria-expanded": "false" });
  var nav = el("div", { class: "chooser-nav" }, [prevBtn, posEl, nextBtn, shuffleBtn, allBtn]);
  var hint = el("p", { class: "chooser-hint", text: "Hover or tab to raise a card. Press Enter on a raised card to turn it over. The arrow keys roll the hand." });
  var deckRow = el("div", { class: "chooser-deckrow", hidden: true });
  var tree = el("p", { class: "chooser-tree" }, [
    document.createTextNode("The whole map is one step away: "),
    el("a", { href: treeHref, text: "browse every tradition on the Church Family Tree" }),
    document.createTextNode(".")
  ]);

  // ---------- tray ----------
  var seatsEl = el("ul", { class: "seats", "aria-label": "Seated at your table" });
  var statusEl = el("span", { class: "status", "aria-live": "polite" });
  var goBtn = el("button", { type: "button", class: "cbtn primary go", text: "Go to the table" });
  var facilitator = el("a", { class: "cbtn quiet facilitator", text: "Have the Facilitator set the table →" });
  var tray = el("div", { class: "chooser-tray", role: "region", "aria-label": "Your table" }, [
    el("div", { class: "in" }, [el("strong", { text: "Your table" }), seatsEl, statusEl, facilitator, goBtn])
  ]);

  if (slot) { slot.textContent = ""; slot.appendChild(searchBox); }
  else mount.appendChild(el("div", { class: "chooser-top" }, [searchBox]));
  mount.appendChild(hand);
  mount.appendChild(nav);
  mount.appendChild(hint);
  mount.appendChild(deckRow);
  mount.appendChild(deckBox);
  mount.appendChild(tree);
  mount.appendChild(tray);

  // ---------- links ----------
  function talkHref(ids, m, source) {
    return "talk.html?worlds=" + ids.join(",") + "&mode=" + m +
      "&from=" + encodeURIComponent(fromPage) + "&via=" + source;
  }

  // ---------- cards ----------
  function cardEl(w) {
    var e = eras[w.era] || { no: "", name: "", dates: "", tint: FALLBACK_TINT };
    var card = el("article", { class: "card", "data-id": w.id });
    card.style.setProperty("--era", e.tint);
    var bandText = (e.no ? e.no + ". " : "") + e.name;
    var statRows = [["Years", w.dates], ["Place", w.place]];
    if (w.shaped) statRows.push(["Shaped by", w.shaped]);

    var front = el("button", { type: "button", class: "cfront", "data-act": "front",
      "aria-label": w.rep + ", " + w.role + ", " + w.world + ", " + e.name + ". " + w.dates + ". Press to bring the card forward, then again to turn it over." });
    var img = el("img", { src: w.img, alt: "", loading: "lazy", decoding: "async" });
    var frontFace = el("div", { class: "face front" }, [
      el("div", { class: "band" }, [el("span", { text: bandText }), el("span", { text: e.dates })]),
      el("div", { class: "head" }, [el("p", { class: "tname", text: w.world }), el("p", { class: "tdates", text: w.dates + " · " + w.place })]),
      el("div", { class: "pic" }, [img]),
      el("div", { class: "plate" }, [el("p", { class: "rep", text: w.rep }), el("p", { class: "role", text: w.role }), w.tag ? el("p", { class: "tag", text: w.tag }) : null]),
      el("span", { class: "num", "aria-hidden": "true", text: pad2(allIds.indexOf(w.id) + 1) + " / " + pad2(allIds.length) }),
      front
    ]);

    var talk = el("a", { class: "cbtn", "data-act": "talk", text: "Talk with " + w.rep });
    var seat = el("button", { type: "button", class: "cbtn", "data-act": "seat", "aria-pressed": "false", text: "Seat at the table" });
    var about = el("a", { class: "cbtn quiet", href: "traditions/" + w.id + ".html", text: "About this tradition" });
    var back = el("button", { type: "button", class: "cbtn quiet", "data-act": "back", text: "Turn the card back" });
    if (mode === "table") { seat.classList.add("primary"); } else { talk.classList.add("primary"); }
    var acts = mode === "table" ? [seat, talk, about, back] : [talk, seat, about, back];

    var body = el("div", { class: "bbody", tabindex: "0", role: "group", "aria-label": "About " + w.world },
      [w.summary ? el("p", { text: w.summary }) : null, w.record ? el("p", { class: "rec", text: "What the record holds: " + w.record }) : null]);
    var backFace = el("div", { class: "face back", inert: true }, [
      el("div", { class: "band" }, [el("span", { text: bandText }), el("span", { text: e.dates })]),
      el("p", { class: "btitle", text: w.rep + " · " + w.world }),
      el("div", { class: "stats" }, statRows.map(function (r) { return el("div", null, [el("b", { text: r[0] }), el("span", { text: r[1] })]); })),
      body,
      el("div", { class: "acts" }, acts)
    ]);

    card.appendChild(el("span", { class: "seatmark", "aria-hidden": "true", text: "Seated" }));
    card.appendChild(el("div", { class: "inner" }, [frontFace, backFace]));

    front.addEventListener("click", function () {
      if (!listMode() && !card.classList.contains("active")) { setActive(handIds.indexOf(w.id), true); return; }
      turn(card, true);
    });
    card.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && card.classList.contains("turned")) { turn(card, false); ev.stopPropagation(); }
    });
    acts.forEach(function (a) {
      var act = a.getAttribute("data-act");
      if (act === "back") a.addEventListener("click", function () { turn(card, false); });
      if (act === "seat") a.addEventListener("click", function () { toggleSeat(w.id); });
    });
    return card;
  }

  function turn(card, on) {
    var frontFace = card.querySelector(".face.front"), backFace = card.querySelector(".face.back");
    card.classList.toggle("turned", on);
    if (on) {
      frontFace.setAttribute("inert", ""); backFace.removeAttribute("inert");
      var first = backFace.querySelector(".acts .cbtn"); if (first) first.focus();
    } else {
      backFace.setAttribute("inert", ""); frontFace.removeAttribute("inert");
      card.querySelector(".cfront").focus();
    }
  }

  function listMode() { return mount.classList.contains("is-list"); }

  function decorateCards() {
    [].forEach.call(hand.children, function (card) {
      var id = card.getAttribute("data-id"), w = byId[id], on = seated.indexOf(id) >= 0;
      card.classList.toggle("seated", on);
      var seat = card.querySelector('[data-act="seat"]');
      seat.setAttribute("aria-pressed", on ? "true" : "false");
      seat.textContent = on ? "Leave the table" : "Seat at the table";
      card.querySelector('[data-act="talk"]').setAttribute("href", talkHref([id], "interview", via[id] || "hand"));
      void w;
    });
  }

  function layout() {
    var cards = [].slice.call(hand.children);
    cards.forEach(function (card, i) {
      var d = i - active;
      card.style.setProperty("--d", String(d));
      card.style.setProperty("--ad", String(Math.abs(d)));
      card.classList.toggle("active", d === 0);
      card.setAttribute("aria-current", d === 0 ? "true" : "false");
      card.querySelector(".cfront").setAttribute("tabindex", (d === 0 || listMode()) ? "0" : "-1");
    });
    posEl.textContent = cards.length ? (active + 1) + " of " + cards.length : "";
    hand.setAttribute("aria-label", handIds.length + " voices in your hand. Use the arrow keys to roll the hand.");
  }

  function setActive(i, focus) {
    if (!handIds.length) return;
    active = Math.max(0, Math.min(handIds.length - 1, i));
    layout();
    if (focus) { var c = hand.children[active]; if (c) c.querySelector(".cfront").focus(); }
  }

  function renderHand(activeId) {
    hand.textContent = "";
    handIds.forEach(function (id) { hand.appendChild(cardEl(byId[id])); });
    active = activeId && handIds.indexOf(activeId) >= 0 ? handIds.indexOf(activeId) : Math.floor(handIds.length / 2);
    layout();
    decorateCards();
  }

  prevBtn.addEventListener("click", function () { setActive(active - 1, false); });
  nextBtn.addEventListener("click", function () { setActive(active + 1, false); });
  hand.addEventListener("keydown", function (ev) {
    if (listMode()) return;
    if (ev.key === "ArrowRight") { setActive(active + 1, true); ev.preventDefault(); }
    if (ev.key === "ArrowLeft") { setActive(active - 1, true); ev.preventDefault(); }
  });
  var px = null;
  hand.addEventListener("pointerdown", function (ev) { px = ev.clientX; });
  hand.addEventListener("pointerup", function (ev) {
    if (px === null || listMode()) { px = null; return; }
    var dx = ev.clientX - px; px = null;
    if (Math.abs(dx) > 40) setActive(active + (dx < 0 ? 1 : -1), false);
  });

  // ---------- deck: filtering, dealing, search ----------
  function eraName(w) { var e = eras[w.era]; return e ? e.name : ""; }
  function haystack(w, withVoices) {
    var parts = [w.rep, w.role, w.world, w.name, w.informal, w.subtitle, w.place, w.tag, w.shaped, w.dates, eraName(w)]
      .concat(w.matches.map(function (m) { return m && m.term; }))
      .concat(w.topics.map(function (t) { return t.word + " " + t.note; }))
      .concat(w.aliases.map(function (a) { return a.name; }))
      .concat(w.keywords);
    if (withVoices) parts = parts.concat(w.voices);
    return parts.join(" ").toLowerCase();
  }
  var topicWords = [];
  worlds.forEach(function (w) { w.topics.forEach(function (t) { var k = t.word.toLowerCase(); if (topicWords.indexOf(k) < 0) topicWords.push(k); }); });
  function isTopicTerm(term) { return topicWords.some(function (k) { return k.indexOf(term) >= 0; }); }
  var CENTURY_WORDS = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth"];
  function yearRange(term) {
    var m = /^(\d{2,4})$/.exec(term);
    if (m) return [+m[1], +m[1]];
    m = /^(\d{1,2})(?:st|nd|rd|th)?\s+century(?:\s+(?:ce|ad))?$/.exec(term);
    var c = m ? +m[1] : 0;
    if (!c) {
      m = /^([a-z]+)\s+century(?:\s+(?:ce|ad))?$/.exec(term);
      if (m) c = CENTURY_WORDS.indexOf(m[1]) + 1;
    }
    return c > 0 ? [(c - 1) * 100 + 1, c * 100] : null;
  }
  function inYears(w, term) {
    var r = yearRange(term);
    return !!r && typeof w.start === "number" && typeof w.end === "number" && w.start <= r[1] && w.end >= r[0];
  }
  function deckIds() {
    var term = deckState.q.trim().toLowerCase();
    return allIds.filter(function (id) {
      var w = byId[id];
      if (deckState.era && w.era !== deckState.era) return false;
      return !term || haystack(w, !isTopicTerm(term)).indexOf(term) >= 0 || inYears(w, term);
    });
  }

  function whyMatched(w, term) {
    var t = term.toLowerCase();
    for (var i = 0; i < w.matches.length; i++) {
      var m = w.matches[i];
      if (m && m.term && m.term.toLowerCase().indexOf(t) >= 0) return m.term + ": " + (m.why || "");
    }
    var tw = w.topics.filter(function (x) { return x.word.toLowerCase().indexOf(t) >= 0; });
    if (tw.length) return tw.slice(0, 2).map(function (x) { return x.word + ": " + x.note; }).join(" ");
    for (var a = 0; a < w.aliases.length; a++) {
      if (w.aliases[a].name.toLowerCase().indexOf(t) >= 0) return "Also known as " + w.aliases[a].name + ". " + w.aliases[a].note;
    }
    var names = [["its name", w.world + " " + w.name + " " + w.informal + " " + w.subtitle], ["its place", w.place], ["its Representative", w.rep + " " + w.role], ["its era", eraName(w)]];
    for (var n = 0; n < names.length; n++) if (names[n][1].toLowerCase().indexOf(t) >= 0) return "Matches " + names[n][0] + ".";
    if (inYears(w, t) || (w.dates || "").toLowerCase().indexOf(t) >= 0) return "Active " + w.dates + ".";
    var tn = w.topics.filter(function (x) { return x.note.toLowerCase().indexOf(t) >= 0; });
    if (tn.length) return tn[0].word + ": " + tn[0].note;
    for (var v = 0; v < w.voices.length; v++) {
      var voice = w.voices[v], at = voice.toLowerCase().indexOf(t);
      if (at < 0) continue;
      var prior = voice.lastIndexOf(". ", at), start = prior < 0 ? 0 : prior + 2;
      var end = voice.indexOf(". ", at); end = end < 0 ? voice.length : end + 1;
      var s = voice.slice(start, end);
      if (s.length > 170) s = s.slice(0, 167).replace(/\s+\S*$/, "") + "…";
      return "In its record: “" + s + "”";
    }
    for (var k = 0; k < w.keywords.length; k++) {
      if (w.keywords[k].toLowerCase().indexOf(t) >= 0) return "Matches this tradition.";
    }
    return "Mentioned in its record.";
  }

  function dealFive(deck) {
    if (deck.length <= HAND_SIZE) return deck.slice();
    var pool = deck.filter(function (id) { return seated.indexOf(id) < 0; });
    var unseen = pool.filter(function (id) { return seen.indexOf(id) < 0; });
    if (!unseen.length) { seen = seen.filter(function (id) { return deck.indexOf(id) < 0; }); unseen = pool; }
    var pick = seated.filter(function (id) { return deck.indexOf(id) >= 0; });
    var keep = function (id) { return pick.indexOf(id) < 0; };
    var eraList = []; deck.forEach(function (id) { if (eraList.indexOf(byId[id].era) < 0) eraList.push(byId[id].era); });
    eraList.forEach(function (era) {
      if (pick.length >= HAND_SIZE) return;
      var c = unseen.filter(function (id) { return byId[id].era === era && keep(id); });
      if (c.length) pick.push(c[shuffleIndex(c.length)]);
    });
    while (pick.length < HAND_SIZE) {
      var c2 = unseen.filter(keep);
      if (!c2.length) c2 = pool.filter(keep);
      if (!c2.length) break;
      pick.push(c2[shuffleIndex(c2.length)]);
    }
    pick.forEach(function (id) { if (seen.indexOf(id) < 0) seen.push(id); });
    try { localStorage.setItem("cic-dealt", JSON.stringify(seen)); } catch (e) {}
    return pick.sort(order);
  }

  function deal(reason) {
    var deck = deckIds(), term = deckState.q.trim();
    whyEl.textContent = "";
    var activeId = null;
    if (!deck.length) {
      countEl.textContent = "Nothing matches that yet. Try an era, a place, or another name.";
      hand.textContent = ""; posEl.textContent = ""; handIds = [];
      shuffleBtn.hidden = true;
      renderDeckRow(deck);
      return;
    }
    if (reason === "search" && term) {
      var next = [];
      handIds.concat(deck).forEach(function (id) { if (next.indexOf(id) < 0) next.push(id); });
      while (next.length > HAND_CAP) {
        var drop = -1;
        for (var i = 0; i < next.length; i++) if (seated.indexOf(next[i]) < 0 && deck.indexOf(next[i]) < 0) { drop = i; break; }
        if (drop < 0) break;
        next.splice(drop, 1);
      }
      next.sort(order);
      deck.forEach(function (id) { if (handIds.indexOf(id) < 0) via[id] = "search"; });
      handIds = next; activeId = deck[0];
      countEl.textContent = deck.length + (deck.length === 1 ? " match" : " matches") + ", brought into your hand of " + handIds.length + ".";
      deck.forEach(function (id) {
        var w = byId[id];
        whyEl.appendChild(el("li", null, [el("b", { text: w.rep + ", " + w.world + ". " }), document.createTextNode(whyMatched(w, term))]));
      });
    } else {
      handIds = dealFive(deck);
      handIds.forEach(function (id) { via[id] = "hand"; });
      countEl.textContent = deck.length <= HAND_SIZE
        ? "Showing all " + deck.length + (deck.length === 1 ? " that matches." : " that match.")
        : "Showing " + handIds.length + " of " + deck.length + ". Shuffle for " + Math.min(HAND_SIZE, deck.length - handIds.length) + " more.";
    }
    shuffleBtn.hidden = deck.length <= HAND_SIZE;
    renderHand(activeId);
    renderDeckRow(deck);
  }

  var qTimer;
  q.addEventListener("input", function () {
    clearTimeout(qTimer);
    qTimer = setTimeout(function () { deckState.q = q.value; deal(q.value.trim() ? "search" : "shuffle"); }, 250);
  });
  shuffleBtn.addEventListener("click", function () { deal("shuffle"); });
  allBtn.addEventListener("click", function () { deckOpen = !deckOpen; renderDeckRow(deckIds()); if (deckOpen) { var r = deckRow.querySelector(".chooser-row"); if (r) r.focus(); } });

  function renderDeckRow(deck) {
    allBtn.textContent = deckOpen ? "Hide the deck" : "See all " + deck.length;
    allBtn.setAttribute("aria-expanded", deckOpen ? "true" : "false");
    allBtn.hidden = !deck.length;
    deckRow.hidden = !deckOpen;
    deckRow.textContent = "";
    if (!deckOpen) return;
    var row = el("div", { class: "chooser-row", tabindex: "0", role: "group", "aria-roledescription": "row of cards",
      "aria-label": deck.length + " cards in order of time. Scroll sideways, or use the buttons. Activate a card to take it into your hand." });
    deck.forEach(function (id) {
      var w = byId[id], e = eras[w.era] || { no: "", name: "", tint: FALLBACK_TINT };
      var inHand = handIds.indexOf(id) >= 0;
      var b = el("button", { type: "button", class: "mini" + (inHand ? " inhand" : "") + (seated.indexOf(id) >= 0 ? " seated" : ""), "data-id": id,
        "aria-label": w.rep + ", " + w.world + ", " + e.name + ". " + (inHand ? "Already in your hand. Activate to bring it to the front." : "Take this card into your hand.") }, [
        el("span", { class: "mband", text: (e.no ? e.no + ". " : "") + e.name }),
        el("img", { src: w.thumb || w.img, alt: "", loading: "lazy", decoding: "async" }),
        el("span", { class: "mname" }, [document.createTextNode(w.rep), el("small", { text: w.world })])
      ]);
      b.style.setProperty("--era", e.tint);
      b.addEventListener("click", function () { pickFromDeck(id); });
      row.appendChild(b);
    });
    var scrollBy = function (dir) { row.scrollBy({ left: dir * 340, behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }); };
    var back = el("button", { type: "button", class: "cbtn", "aria-label": "Scroll the deck back", text: "‹" });
    var fwd = el("button", { type: "button", class: "cbtn", "aria-label": "Scroll the deck forward", text: "›" });
    back.addEventListener("click", function () { scrollBy(-1); });
    fwd.addEventListener("click", function () { scrollBy(1); });
    deckRow.appendChild(el("div", { class: "head2" }, [el("p", { text: "The whole deck, in order of time. Tap a card to take it into your hand." }), el("div", null, [back, document.createTextNode(" "), fwd])]));
    deckRow.appendChild(row);
  }

  function pickFromDeck(id) {
    if (handIds.indexOf(id) < 0) { handIds.push(id); handIds.sort(order); via[id] = "scroll"; }
    renderHand(id);
    renderDeckRow(deckIds());
    hand.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "center" });
    var c = hand.children[active]; if (c) c.querySelector(".cfront").focus({ preventScroll: true });
  }

  // ---------- seats and tray ----------
  function toggleSeat(id) {
    var i = seated.indexOf(id);
    if (i >= 0) seated.splice(i, 1);
    else if (seated.length >= MAX_SEATS) { statusEl.textContent = "Three is the most a table can seat. Leave a seat to take another."; return; }
    else seated.push(id);
    decorateCards();
    renderTray();
    var minis = deckRow.querySelectorAll(".mini");
    [].forEach.call(minis, function (m) { m.classList.toggle("seated", seated.indexOf(m.getAttribute("data-id")) >= 0); });
  }

  function randomTrio() {
    var pool = allIds.slice(), picks = [];
    while (picks.length < MAX_SEATS && pool.length) picks.push(pool.splice(shuffleIndex(pool.length), 1)[0]);
    return picks;
  }

  function renderTray() {
    var n = seated.length;
    seatsEl.textContent = "";
    seated.forEach(function (id) {
      var w = byId[id];
      var rm = el("button", { type: "button", "aria-label": "Remove " + w.rep + " from the table", text: "×" });
      rm.addEventListener("click", function () { toggleSeat(id); });
      seatsEl.appendChild(el("li", { class: "chip" }, [document.createTextNode(w.rep), rm]));
    });
    statusEl.textContent = n === 0 ? "No one seated yet. Seat two or three voices, then go."
      : n === 1 ? "1 of " + MAX_SEATS + " seated. Seat one more to open the table."
      : n + " of " + MAX_SEATS + " seated. Ready when you are.";
    goBtn.disabled = n < 2;
    goBtn.setAttribute("aria-disabled", n < 2 ? "true" : "false");
    facilitator.hidden = !(mode === "table" && n === 0);
    facilitator.setAttribute("href", talkHref(randomTrio(), "table", "table-tray"));
    var show = mode === "table" || n > 0;
    tray.hidden = !show;
    document.body.style.paddingBottom = show ? "5.5rem" : "";
  }
  goBtn.addEventListener("click", function () {
    if (seated.length < 2) return;
    window.location.href = talkHref(seated, "table", "table-tray");
  });

  // ---------- list fallback ----------
  var narrowMq = matchMedia("(max-width: 699px)"), rmMq = matchMedia("(prefers-reduced-motion: reduce)");
  function applyMode() {
    mount.classList.toggle("is-list", narrowMq.matches || rmMq.matches);
    layout();
  }
  [narrowMq, rmMq].forEach(function (mq) { (mq.addEventListener ? mq.addEventListener("change", applyMode) : mq.addListener(applyMode)); });

  // seated cards from a pre-seated table link join the first hand
  handIds = seated.slice();
  allBtn.textContent = "See all " + allIds.length;
  applyMode();
  deal("shuffle");
  renderTray();
}

function boot() {
  var mounts = document.querySelectorAll("[data-chooser]");
  if (!mounts.length) return;
  var src = mounts[0].getAttribute("data-census") || "data/world-census.json";
  fetch(src).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (census) { [].forEach.call(mounts, function (m) { init(m, census); }); })
    .catch(function () {
      [].forEach.call(mounts, function (m) {
        var fb = m.querySelector("[data-chooser-fallback]");
        if (fb) fb.hidden = false;
      });
    });
}
if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
