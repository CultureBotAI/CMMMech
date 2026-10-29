/* CMMMech client-side record filtering */
(function () {
  'use strict';
  var form = document.getElementById('record-filters');
  if (!form) return;
  var query = document.getElementById('record-query');
  var kind = document.getElementById('record-kind');
  var mechanism = document.getElementById('record-mechanism');
  var criticality = document.getElementById('record-criticality');
  var sortSelect = document.getElementById('record-sort');
  var count = document.getElementById('record-count');
  var empty = document.getElementById('record-empty');
  var tbody = document.querySelector('#record-table tbody');
  var rows = Array.from(document.querySelectorAll('#record-table tbody tr')).map(function (row, idx) {
    return {
      row: row,
      idx: idx,
      name: row.dataset.name || (row.textContent || '').trim().toLowerCase(),
      id: (row.dataset.id || '').toLowerCase(),
      text: (row.textContent + ' ' + (row.dataset.search || '')).toLowerCase(),
      kind: row.dataset.kind || '',
      mechanism: (row.dataset.mechanisms || '').split(' '),
      mechCount: parseInt(row.dataset.mechCount || '0', 10) || 0,
      orgCount: parseInt(row.dataset.orgCount || '0', 10) || 0,
      critical: row.dataset.critical || ''
    };
  });

  function readUrlParams() {
    var params = new URLSearchParams(window.location.search);
    if (query && params.has('q')) query.value = params.get('q') || '';
    if (kind && params.has('kind')) kind.value = params.get('kind') || '';
    if (mechanism && params.has('process')) mechanism.value = params.get('process') || '';
    if (criticality && params.has('criticality')) criticality.value = params.get('criticality') || '';
    if (sortSelect && params.has('sort')) sortSelect.value = params.get('sort') || 'name-asc';
  }

  function syncUrlParams() {
    if (!window.history || !window.history.replaceState) return;
    var params = new URLSearchParams(window.location.search);
    var qVal = query ? query.value.trim() : '';
    var kVal = kind ? kind.value : '';
    var mVal = mechanism ? mechanism.value : '';
    var cVal = criticality ? criticality.value : '';
    var sVal = sortSelect ? sortSelect.value : 'name-asc';

    if (qVal) params.set('q', qVal); else params.delete('q');
    if (kVal) params.set('kind', kVal); else params.delete('kind');
    if (mVal) params.set('process', mVal); else params.delete('process');
    if (cVal) params.set('criticality', cVal); else params.delete('criticality');
    if (sVal && sVal !== 'name-asc') params.set('sort', sVal); else params.delete('sort');

    var qs = params.toString();
    var newUrl = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
    window.history.replaceState(null, '', newUrl);
  }

  function sortRows(mode) {
    if (!tbody) return;
    var sorted = rows.slice().sort(function (a, b) {
      if (mode === 'name-desc') return b.name.localeCompare(a.name);
      if (mode === 'mechs-desc') return (b.mechCount - a.mechCount) || a.name.localeCompare(b.name);
      if (mode === 'orgs-desc') return (b.orgCount - a.orgCount) || a.name.localeCompare(b.name);
      if (mode === 'kind-asc') return a.kind.localeCompare(b.kind) || a.name.localeCompare(b.name);
      if (mode === 'crit-desc') {
        var ac = a.critical === 'true' ? 0 : 1;
        var bc = b.critical === 'true' ? 0 : 1;
        return (ac - bc) || a.name.localeCompare(b.name);
      }
      return a.name.localeCompare(b.name) || (a.idx - b.idx);
    });
    sorted.forEach(function (item) {
      tbody.appendChild(item.row);
    });
  }

  function apply() {
    var term = query ? query.value.trim().toLowerCase() : '';
    var selectedKind = kind ? kind.value : '';
    var selectedMech = mechanism ? mechanism.value : '';
    var selectedCrit = criticality ? criticality.value : '';
    var selectedSort = sortSelect ? sortSelect.value : 'name-asc';
    var visible = 0;
    // A query that is exactly a record's own id finds that record alone: a slug
    // can begin another slug (cmmmech:cobalt, cmmmech:cobaltite), so a substring
    // match would answer one identifier with several records.
    var exactId = term && rows.some(function (r) { return r.id === term; }) ? term : '';

    sortRows(selectedSort);

    rows.forEach(function (r) {
      var matchText = exactId ? r.id === exactId : (!term || r.text.indexOf(term) !== -1);
      var matchKind = !selectedKind || r.kind === selectedKind;
      var matchMech = !selectedMech || r.mechanism.indexOf(selectedMech) !== -1;
      var matchCrit = !selectedCrit || (selectedCrit === 'critical' ? r.critical === 'true' : r.critical !== 'true');

      var match = matchText && matchKind && matchMech && matchCrit;
      r.row.hidden = !match;
      if (match) visible += 1;
    });

    if (count) {
      count.textContent = visible + ' of ' + rows.length + ' materials shown';
    }
    if (empty) {
      empty.hidden = visible !== 0;
    }
    syncUrlParams();
  }

  form.addEventListener('submit', function (e) { e.preventDefault(); });
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  form.addEventListener('reset', function () { setTimeout(apply, 0); });
  form.hidden = false;
  readUrlParams();
  window.addEventListener('pageshow', function () {
    readUrlParams();
    apply();
  });
  apply();
})();
