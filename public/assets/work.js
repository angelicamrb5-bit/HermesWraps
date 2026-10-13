/* Work page: filters + native <dialog> image zoom */
(function () {
  'use strict';
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var cards = $$('#workGrid .project-card'), filters = $$('.filter');
  var types = document.getElementById('types'), catalog = document.getElementById('catalog');
  var title = document.getElementById('catalogTitle'), status = document.getElementById('filterStatus');
  var LABELS = { commercial: 'Commercial & work vehicles', signs: 'Signs & storefronts', vinyl: 'Other vinyl', vehicle: 'Personal vehicles' };

  /* No type chosen: show one sample per type. A type chosen: show only its catalog. */
  function apply(cat, focus) {
    if (!LABELS[cat]) {
      filters.forEach(function (f) { f.setAttribute('aria-pressed', 'false'); });
      types.hidden = false; catalog.hidden = true;
      return;
    }
    var n = 0;
    cards.forEach(function (c) { var on = c.getAttribute('data-cat') === cat; c.hidden = !on; if (on) n++; });
    filters.forEach(function (f) { f.setAttribute('aria-pressed', String(f.getAttribute('data-filter') === cat)); });
    types.hidden = true; catalog.hidden = false;
    title.textContent = LABELS[cat] + ' · ' + n + (n === 1 ? ' project' : ' projects');
    status.textContent = title.textContent;
    if (focus) { title.focus({ preventScroll: true }); catalog.scrollIntoView(); }
  }
  filters.forEach(function (f) {
    f.addEventListener('click', function () {
      var cat = f.getAttribute('data-filter');
      history.replaceState(null, '', '#' + cat);
      apply(cat, false);
    });
  });
  window.addEventListener('hashchange', function () { apply(location.hash.slice(1), true); });
  /* A link to the catalog that is already open doesn't change the hash, so handle it here */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="/work#"]');
    if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
    var cat = a.getAttribute('href').split('#')[1];
    if (!LABELS[cat] || location.hash.slice(1) !== cat) return;
    e.preventDefault();
    apply(cat, true);
  });
  document.querySelector('[data-type-reset]').addEventListener('click', function (e) {
    e.preventDefault();
    history.pushState(null, '', location.pathname);
    apply('', false);
    window.scrollTo(0, 0);
  });
  window.addEventListener('popstate', function () { apply(location.hash.slice(1), false); });
  apply(location.hash.slice(1), false);

  var dlg = document.getElementById('zoom');
  if (!dlg || typeof dlg.showModal !== 'function') {
    $$('[data-zoom]').forEach(function (b) { b.addEventListener('click', function () { window.open(b.getAttribute('data-zoom').split(',')[0], '_blank'); }); });
    return;
  }
  var img = dlg.querySelector('img'), cap = document.getElementById('zoomCap'), cnt = document.getElementById('zoomCount');
  var prev = dlg.querySelector('[data-zoom-prev]'), next = dlg.querySelector('[data-zoom-next]');
  var list = [], at = 0, alt = '';
  function show(n) {
    at = (n + list.length) % list.length;
    img.src = list[at];
    img.alt = alt + (list.length > 1 ? ' (photo ' + (at + 1) + ' of ' + list.length + ')' : '');
    cnt.textContent = list.length > 1 ? (at + 1) + ' / ' + list.length : '';
    prev.hidden = next.hidden = list.length < 2;
  }
  $$('[data-zoom]').forEach(function (b) {
    b.addEventListener('click', function () {
      var card = b.closest('.project-card');
      list = b.getAttribute('data-zoom').split(',');
      alt = card.querySelector('.media img').alt;
      cap.textContent = b.textContent + ' — ' + card.querySelector('p:last-of-type').textContent;
      show(0);
      dlg.showModal();
    });
  });
  prev.addEventListener('click', function () { show(at - 1); });
  next.addEventListener('click', function () { show(at + 1); });
  dlg.addEventListener('keydown', function (e) {
    if (list.length < 2) return;
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(at - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); show(at + 1); }
  });
  /* Swipe left/right on touch screens */
  var x0 = null;
  img.addEventListener('touchstart', function (e) { x0 = e.touches.length === 1 ? e.touches[0].clientX : null; }, { passive: true });
  img.addEventListener('touchend', function (e) {
    if (x0 === null || list.length < 2) return;
    var dx = e.changedTouches[0].clientX - x0; x0 = null;
    if (Math.abs(dx) > 40) show(dx < 0 ? at + 1 : at - 1);
  });
  dlg.querySelector('[data-close-zoom]').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();
