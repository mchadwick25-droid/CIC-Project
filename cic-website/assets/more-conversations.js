(function () {
  "use strict";
  var cfg = window.GoDeeperConfig;
  var toggle = document.getElementById("more-toggle");
  var drawer = document.getElementById("more-drawer");
  var scrim = document.getElementById("more-scrim");
  var frame = document.getElementById("more-frame");
  if (!cfg || !cfg.enabled || !cfg.drawer || !toggle || !drawer || !scrim || !frame) return;
  toggle.hidden = false;

  var appOrigin = cfg.app;
  var loaded = false;
  var isOpen = false;

  function open() {
    if (isOpen) return;
    isOpen = true;
    drawer.hidden = false;
    scrim.hidden = false;
    toggle.setAttribute("aria-expanded", "true");
    if (!loaded) {
      loaded = true;
      frame.src = appOrigin + "/#get-more";
    } else if (frame.contentWindow) {
      frame.contentWindow.postMessage({ type: "cic:panel-open" }, appOrigin);
    }
    window.requestAnimationFrame(function () {
      drawer.classList.add("open");
      scrim.classList.add("open");
    });
    frame.focus();
  }

  function close() {
    if (!isOpen) return;
    isOpen = false;
    drawer.classList.remove("open");
    scrim.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
    var done = function () { if (!isOpen) { drawer.hidden = true; scrim.hidden = true; } };
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) done();
    else window.setTimeout(done, 260);
    toggle.focus();
  }

  toggle.addEventListener("click", function () { if (isOpen) close(); else open(); });
  [].forEach.call(document.querySelectorAll("[data-more-open]"), function (link) {
    link.addEventListener("click", function (ev) { ev.preventDefault(); open(); });
  });
  scrim.addEventListener("click", close);
  document.addEventListener("keydown", function (ev) { if (ev.key === "Escape") close(); });
  window.addEventListener("message", function (ev) {
    if (ev.origin !== appOrigin || ev.source !== frame.contentWindow) return;
    if (ev.data && ev.data.type === "cic:panel-close") close();
  });
})();
