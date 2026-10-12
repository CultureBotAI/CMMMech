/* CMMMech client-side record filtering */
(function () {
  'use strict';
  var form = document.getElementById('record-filters');
  if (!form) return;
  var query = document.getElementById('record-query');
  var kind = document.getElementById('record-kind');
  var mechanism = document.getElementById('record-mechanism');
  var criticality = document.getElementById('record-criticality');
  var count = document.getElementById('record-count');
  var empty = document.getElementById('record-empty');
  var rows = Array.from(document.querySelectorAll('#record-table tbody tr')).map(function (row) {
    return {
      row: row,
      text: (row.textContent + ' ' + (row.dataset.search || '')).toLowerCase(),
      kind: row.dataset.kind || '',
      mechanism: (row.dataset.mechanisms || '').split(' '),
      critical: row.dataset.critical || ''
    };
  });

  function apply() {
    var term = query.value.trim().toLowerCase();
    var selectedKind = kind ? kind.value : '';
    var selectedMech = mechanism ? mechanism.value : '';
    var selectedCrit = criticality ? criticality.value : '';
    var visible = 0;

    rows.forEach(function (r) {
      var matchText = !term || r.text.indexOf(term) !== -1;
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
  }

  form.addEventListener('submit', function (e) { e.preventDefault(); });
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  form.addEventListener('reset', function () { setTimeout(apply, 0); });
  form.hidden = false;
  window.addEventListener('pageshow', apply);
  apply();
})();
