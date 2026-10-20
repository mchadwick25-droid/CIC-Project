(function () {
"use strict";

var MAX_SEATS = 3;
var FAN = 2;
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
function joinNames(list) {
  if (list.length < 2) return list.join("");
  return list.slice(0, -1).join(", ") + " and " + list[list.length - 1];
}
function shuffleIndex(len) { return Math.floor(Math.random() * len); }

function init(mount, census) {
  var mode = mount.getAttribute("data-mode") === "table" ? "table" : "landing";
  var fromPage = mount.getAttribute("data-from") || "index.html#who";

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
        shapedList: Array.isArray(en.shaped) ? en.shaped : [],
        summary: en.summary || en.tile || "",
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
    el("p", { class: "chooser-help", id: helpId, text: "Try a tradition, a topic or a person: Lutheran, baptism, Augustine." })
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
  var prevBtn = el("button", { type: "button", class: "chooser-arrow prev", "aria-label": "Previous card" });
  var nextBtn = el("button", { type: "button", class: "chooser-arrow next", "aria-label": "Next card" });
  var stage = el("div", { class: "chooser-stage" }, [hand, prevBtn, nextBtn]);
  var allBtn = el("button", { type: "button", class: "cbtn quiet", "aria-expanded": "false" });
  var nav = el("div", { class: "chooser-nav" }, [posEl, allBtn]);
  var tableLine = el("p", { class: "chooser-tableline", text: "Choose Table on two or three cards to build a table, then put one question to all of them." });
  var hint = el("details", { class: "chooser-how" }, [
    el("summary", { text: "How this works" }),
    el("ul", null, [
      el("li", { text: "Click a card to bring it forward. Click it again to turn it over." }),
      el("li", { text: "Talk starts a conversation with that one representative." }),
      el("li", { text: "Table adds the representative to a table of two or three. When you have two or three, choose Go to the table." }),
      el("li", { text: "Swipe or use the arrows to see more cards. Search or pick an era to narrow them." })
    ])
  ]);
  var deckRow = el("div", { class: "chooser-deckrow", hidden: true });

  // ---------- tray ----------
  var seatsEl = el("ul", { class: "seats", "aria-label": "On your table" });
  var statusEl = el("span", { class: "status", "aria-live": "polite" });
  var goBtn = el("button", { type: "button", class: "cbtn primary go", text: "Go to the table" });
  var facilitator = el("a", { class: "cbtn quiet facilitator", text: "Have the Facilitator set the table →" });
  var tray = el("div", { class: "chooser-tray", role: "region", "aria-label": "Your table" }, [
    el("div", { class: "in" }, [el("strong", { text: "Your table" }), seatsEl, statusEl, facilitator, goBtn])
  ]);

  if (slot) { slot.textContent = ""; slot.appendChild(searchBox); }
  else mount.appendChild(el("div", { class: "chooser-top" }, [searchBox]));
  mount.appendChild(stage);
  mount.appendChild(deckBox);
  mount.appendChild(nav);
  if (mode !== "table") mount.appendChild(tableLine);
  mount.appendChild(deckRow);
  mount.appendChild(hint);
  mount.appendChild(tray);

  // ---------- links ----------
  function talkHref(ids, m, source) {
    return "talk.html?worlds=" + ids.join(",") + "&mode=" + m +
      "&from=" + encodeURIComponent(fromPage) + "&via=" + source;
  }

  // ---------- cards ----------
  var ICON_TALK = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 5h16v11H10l-5 4v-4H4z"/></svg>';
  var ICON_SEAT = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v8M8 9h8M6 21v-5h12v5"/></svg>';
  function icon(svg) { var s = el("span", { class: "ico" }); s.innerHTML = svg; return s; }

  function cardEl(w) {
    var e = eras[w.era] || { no: "", name: "", dates: "", tint: FALLBACK_TINT };
    var card = el("article", { class: "card", "data-id": w.id });
    card.style.setProperty("--era", e.tint);
    var bandText = (e.no ? e.no + ". " : "") + e.name;
    var front = el("button", { type: "button", class: "cfront", "data-act": "front",
      "aria-label": w.rep + ", " + w.world + ", " + e.name + ". " + w.dates + ". Press to bring the card forward, then again to turn it over." });
    var img = el("img", { src: w.img, alt: "", loading: "lazy", decoding: "async" });
    var talk = el("a", { class: "sidebtn left", "data-act": "talk", "aria-label": "Talk with " + w.rep }, [icon(ICON_TALK), el("span", { class: "lbl", text: "Talk" })]);
    var seat = el("button", { type: "button", class: "sidebtn right", "data-act": "seat", "aria-pressed": "false", "aria-label": "Add " + w.rep + " to the table" }, [icon(ICON_SEAT), el("span", { class: "lbl", text: "Table" })]);
    (mode === "table" ? seat : talk).classList.add("primary");
    var frontFace = el("div", { class: "face front" }, [
      el("div", { class: "band" }, [el("span", { text: bandText }), el("span", { text: e.dates })]),
      el("div", { class: "head" }, [el("p", { class: "tname", text: w.world }), el("p", { class: "tdates", text: w.dates + " · " + w.place })]),
      el("div", { class: "pic" }, [img, talk, seat]),
      el("div", { class: "plate" }, [el("p", { class: "rep", text: w.rep }), w.tag ? el("p", { class: "tag", text: w.tag }) : null, w.shapedList.length ? el("p", { class: "shapedby", text: "Shaped by " + joinNames(w.shapedList) + " among others." }) : null]),
      front
    ]);

    var about = el("a", { class: "cbtn quiet", href: "traditions/" + w.id + ".html", text: "Get more information" });

    var body = el("div", { class: "bbody", tabindex: "0", role: "group", "aria-label": "About " + w.world + ". Press Enter to turn the card back." },
      [w.summary ? el("p", { text: w.summary }) : null]);
    var backFace = el("div", { class: "face back", inert: true }, [
      el("div", { class: "band" }, [el("span", { text: bandText }), el("span", { text: e.dates })]),
      el("p", { class: "btitle", text: w.subtitle || w.name }),
      body,
      el("div", { class: "acts" }, [about])
    ]);

    card.appendChild(el("span", { class: "seatmark", "aria-hidden": "true", text: "On table" }));
    card.appendChild(el("div", { class: "inner" }, [frontFace, backFace]));

    front.addEventListener("click", function () {
      if (!listMode() && !card.classList.contains("active")) { setActive(handIds.indexOf(w.id), true); return; }
      turn(card, true);
    });
    card.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && card.classList.contains("turned")) { turn(card, false); ev.stopPropagation(); }
    });
    seat.addEventListener("click", function () { toggleSeat(w.id); });
    backFace.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) return;
      turn(card, false);
    });
    body.addEventListener("keydown", function (ev) {
      if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); turn(card, false); }
    });
    return card;
  }

  function turn(card, on, quiet) {
    var frontFace = card.querySelector(".face.front"), backFace = card.querySelector(".face.back");
    card.classList.toggle("turned", on);
    if (on) {
      frontFace.setAttribute("inert", ""); backFace.removeAttribute("inert");
      backFace.querySelector(".bbody").focus();
    } else {
      backFace.setAttribute("inert", ""); frontFace.removeAttribute("inert");
      if (!quiet) card.querySelector(".cfront").focus();
    }
  }

  function listMode() { return mount.classList.contains("is-list"); }

  function decorateCards() {
    [].forEach.call(hand.children, function (card) {
      var id = card.getAttribute("data-id"), w = byId[id], on = seated.indexOf(id) >= 0;
      card.classList.toggle("seated", on);
      var seat = card.querySelector('[data-act="seat"]');
      seat.setAttribute("aria-pressed", on ? "true" : "false");
      seat.querySelector(".lbl").textContent = on ? "On table" : "Table";
      seat.setAttribute("aria-label", on ? "Remove " + w.rep + " from the table" : "Add " + w.rep + " to the table");
      card.querySelector('[data-act="talk"]').setAttribute("href", talkHref([id], "interview", via[id] || "hand"));
    });
  }

  function layout() {
    var cards = [].slice.call(hand.children);
    cards.forEach(function (card, i) {
      var d = i - active;
      card.style.setProperty("--d", String(d));
      card.style.setProperty("--ad", String(Math.abs(d)));
      card.classList.toggle("active", d === 0);
      card.classList.toggle("peek", Math.abs(d) === FAN + 1);
      card.classList.toggle("off", Math.abs(d) > FAN + 1);
      card.setAttribute("aria-current", d === 0 ? "true" : "false");
      [].forEach.call(card.querySelectorAll(".cfront, .sidebtn"), function (c) { c.setAttribute("tabindex", (d === 0 || listMode()) ? "0" : "-1"); });
    });
    posEl.textContent = cards.length ? (active + 1) + " of " + cards.length : "";
    prevBtn.setAttribute("aria-disabled", active <= 0 ? "true" : "false");
    nextBtn.setAttribute("aria-disabled", active >= cards.length - 1 ? "true" : "false");
    hand.setAttribute("aria-label", handIds.length + " representatives in order of time. Use the arrow buttons, the arrow keys or swipe to roll the hand.");
    var minis = deckRow.querySelectorAll(".mini");
    [].forEach.call(minis, function (m) { m.classList.toggle("inhand", m.getAttribute("data-id") === handIds[active]); });
  }

  function setActive(i, focus) {
    if (!handIds.length) return;
    var next = Math.max(0, Math.min(handIds.length - 1, i));
    if (next !== active) [].forEach.call(hand.querySelectorAll(".card.turned"), function (c) { turn(c, false, true); });
    active = next;
    layout();
    if (focus) { var c = hand.children[active]; if (c) c.querySelector(".cfront").focus(); }
  }

  function renderHand(activeId) {
    hand.textContent = "";
    handIds.forEach(function (id) { hand.appendChild(cardEl(byId[id])); });
    active = activeId && handIds.indexOf(activeId) >= 0 ? handIds.indexOf(activeId) : Math.min(FAN, Math.max(0, handIds.length - 1));
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
    var parts = [w.rep, w.world, w.name, w.informal, w.subtitle, w.place, w.tag, w.shaped, w.dates, eraName(w)]
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
    var names = [["its name", w.world + " " + w.name + " " + w.informal + " " + w.subtitle], ["its place", w.place], ["its Representative", w.rep], ["its era", eraName(w)]];
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

  function deal(reason) {
    var deck = deckIds(), term = deckState.q.trim();
    whyEl.textContent = "";
    var activeId = null;
    if (!deck.length) {
      countEl.textContent = "Nothing matches that yet. Try an era, a place, or another name.";
      hand.textContent = ""; posEl.textContent = ""; handIds = [];
      renderDeckRow(deck);
      return;
    }
    handIds = deck.slice();
    handIds.forEach(function (id) { via[id] = reason === "search" ? "search" : "hand"; });
    if (reason === "search" && term) {
      activeId = deck[0];
      countEl.textContent = deck.length + (deck.length === 1 ? " match." : " matches, in order of time.");
      deck.forEach(function (id) {
        var w = byId[id];
        whyEl.appendChild(el("li", null, [el("b", { text: w.rep + ", " + w.world + ". " }), document.createTextNode(whyMatched(w, term))]));
      });
    } else if (deckState.era) {
      activeId = deck.length > 2 ? deck[Math.floor((deck.length - 1) / 2)] : deck[0];
      countEl.textContent = "Showing " + deck.length + " of " + allIds.length + ", in order of time.";
    } else {
      countEl.textContent = "";
    }
    renderHand(activeId);
    renderDeckRow(deck);
  }

  var qTimer = null;
  q.addEventListener("input", function () {
    clearTimeout(qTimer);
    qTimer = setTimeout(function () { deckState.q = q.value; deal(q.value.trim() ? "search" : "reset"); }, 250);
  });
  allBtn.addEventListener("click", function () { deckOpen = !deckOpen; renderDeckRow(deckIds()); if (deckOpen) { var r = deckRow.querySelector(".chooser-row"); if (r) r.focus(); } });

  function renderDeckRow(deck) {
    allBtn.textContent = deckOpen ? "Hide the deck" : "See all " + deck.length;
    allBtn.setAttribute("aria-expanded", deckOpen ? "true" : "false");
    allBtn.hidden = !deck.length;
    deckRow.hidden = !deckOpen;
    deckRow.textContent = "";
    if (!deckOpen) return;
    var row = el("div", { class: "chooser-row", tabindex: "0", role: "group", "aria-roledescription": "row of cards",
      "aria-label": deck.length + " cards in order of time. Activate a card to take it into your hand." });
    deck.forEach(function (id) {
      var w = byId[id], e = eras[w.era] || { no: "", name: "", tint: FALLBACK_TINT };
      var showing = id === handIds[active];
      var b = el("button", { type: "button", class: "mini" + (showing ? " inhand" : "") + (seated.indexOf(id) >= 0 ? " seated" : ""), "data-id": id,
        "aria-label": w.rep + ", " + w.world + ", " + e.name + ". " + (showing ? "Showing now." : "Bring this card to the front.") }, [
        el("img", { src: w.thumb || w.img, alt: "", loading: "lazy", decoding: "async" }),
        el("span", { class: "mname" }, [document.createTextNode(w.rep), el("small", { text: w.world }), w.shapedList.length ? el("small", { class: "mshaped", text: "Shaped by " + joinNames(w.shapedList) }) : null])
      ]);
      b.style.setProperty("--era", e.tint);
      b.addEventListener("click", function () { pickFromDeck(id); });
      row.appendChild(b);
    });
    deckRow.appendChild(el("div", { class: "head2" }, [el("p", { text: "The whole deck, in order of time. Tap a card to bring it to the front." })]));
    deckRow.appendChild(row);
  }

  function pickFromDeck(id) {
    if (handIds.indexOf(id) < 0) {
      deckState.era = 0; deckState.q = ""; q.value = "";
      [].forEach.call(erasBox.children, function (x) { x.setAttribute("aria-pressed", x.getAttribute("data-era") === "0" ? "true" : "false"); });
      deal("reset");
    }
    via[id] = "scroll";
    setActive(handIds.indexOf(id), false);
    hand.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "center" });
    var c = hand.children[active]; if (c) c.querySelector(".cfront").focus({ preventScroll: true });
  }

  // ---------- seats and tray ----------
  function toggleSeat(id) {
    var i = seated.indexOf(id);
    if (i >= 0) seated.splice(i, 1);
    else if (seated.length >= MAX_SEATS) { statusEl.textContent = "A table holds three at most. Remove one to add another."; return; }
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
    statusEl.textContent = n === 0 ? "No one is on the table yet. Add two or three representatives, then go."
      : n === 1 ? "1 of " + MAX_SEATS + " on the table. Add one more to open the table."
      : n + " of " + MAX_SEATS + " on the table. Ready when you are.";
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
    q.setAttribute("placeholder", narrowMq.matches ? "Search traditions or topics" : "Search traditions, topics, people");
    mount.classList.toggle("is-list", narrowMq.matches || rmMq.matches);
    layout();
  }
  [narrowMq, rmMq].forEach(function (mq) { (mq.addEventListener ? mq.addEventListener("change", applyMode) : mq.addListener(applyMode)); });

  allBtn.textContent = "See all " + allIds.length;
  applyMode();
  deal("reset");
  if (seated.length) setActive(handIds.indexOf(seated[0]), false);
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
