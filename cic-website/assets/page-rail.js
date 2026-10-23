(function () {
  var doc = document.documentElement;
  var rail = document.createElement("div");
  rail.className = "page-rail";
  rail.setAttribute("role", "scrollbar");
  rail.setAttribute("aria-orientation", "vertical");
  rail.setAttribute("aria-label", "Page position");
  rail.setAttribute("aria-valuemin", "0");
  rail.setAttribute("aria-valuemax", "100");
  rail.setAttribute("tabindex", "0");
  var thumb = document.createElement("div");
  thumb.className = "page-rail-thumb";
  rail.appendChild(thumb);
  document.body.appendChild(rail);

  var thumbH = 0, drag = null;

  function metrics() {
    var view = window.innerHeight, total = doc.scrollHeight, track = rail.clientHeight;
    return { view: view, total: total, track: track, max: Math.max(0, total - view) };
  }

  function update() {
    var m = metrics();
    rail.hidden = m.max <= 0;
    if (rail.hidden) return;
    thumbH = Math.max(56, Math.round(m.track * m.view / m.total));
    var top = (m.track - thumbH) * (window.pageYOffset / m.max);
    thumb.style.height = thumbH + "px";
    thumb.style.transform = "translateY(" + Math.round(top) + "px)";
    rail.setAttribute("aria-valuenow", String(Math.round(100 * window.pageYOffset / m.max)));
  }

  function scrollToThumbTop(y) {
    var m = metrics(), room = m.track - thumbH;
    var ratio = room > 0 ? Math.min(1, Math.max(0, y / room)) : 0;
    window.scrollTo(0, ratio * m.max);
  }

  thumb.addEventListener("pointerdown", function (ev) {
    drag = { startY: ev.clientY, startTop: thumb.getBoundingClientRect().top - rail.getBoundingClientRect().top };
    thumb.setPointerCapture(ev.pointerId);
    rail.classList.add("dragging");
    ev.preventDefault();
    ev.stopPropagation();
  });
  thumb.addEventListener("pointermove", function (ev) {
    if (!drag) return;
    scrollToThumbTop(drag.startTop + ev.clientY - drag.startY);
  });
  function endDrag() { drag = null; rail.classList.remove("dragging"); }
  thumb.addEventListener("pointerup", endDrag);
  thumb.addEventListener("pointercancel", endDrag);

  rail.addEventListener("pointerdown", function (ev) {
    if (ev.target !== rail) return;
    var t = thumb.getBoundingClientRect();
    var m = metrics();
    window.scrollBy(0, (ev.clientY < t.top ? -1 : 1) * m.view * 0.9);
    ev.preventDefault();
  });

  rail.addEventListener("keydown", function (ev) {
    var m = metrics(), by = 0;
    if (ev.key === "ArrowDown") by = 48;
    else if (ev.key === "ArrowUp") by = -48;
    else if (ev.key === "PageDown") by = m.view * 0.9;
    else if (ev.key === "PageUp") by = -m.view * 0.9;
    else if (ev.key === "Home") { window.scrollTo(0, 0); ev.preventDefault(); return; }
    else if (ev.key === "End") { window.scrollTo(0, m.max); ev.preventDefault(); return; }
    else return;
    window.scrollBy(0, by);
    ev.preventDefault();
  });

  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  if (window.ResizeObserver) new ResizeObserver(update).observe(document.body);
  update();
})();
