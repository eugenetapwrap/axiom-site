function initScheme(root, data, startId) {
  var scheme = root.querySelector('.scheme');
  var blocksEl = root.querySelector('.blocks');
  var whoEl = root.querySelector('.who');
  var svg = root.querySelector('svg.links');
  var panel = root.querySelector('.panel');
  var panelHome = root.querySelector('.panel-home');
  var mq = window.matchMedia('(max-width: 900px)');
  var byId = {};
  data.who.forEach(function (w) { byId[w.id] = w; });

  data.blocks.forEach(function (b, i) {
    var li = document.createElement('li');
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'block';
    btn.dataset.id = b.id;
    btn.setAttribute('aria-pressed', 'false');
    btn.innerHTML = '<span class="n">' + (i + 1) + '</span><span><b>' + b.title + '</b><span class="s">' + b.short + '</span></span>';
    li.appendChild(btn);
    blocksEl.appendChild(li);
    btn.addEventListener('mouseenter', function () { if (!mq.matches) activate(b.id); });
    btn.addEventListener('focus', function () { activate(b.id); });
    btn.addEventListener('click', function () { activate(b.id); });
  });
  data.who.forEach(function (w) {
    var li = document.createElement('li');
    li.dataset.id = w.id;
    li.textContent = w.title;
    whoEl.appendChild(li);
  });

  var current = null;
  function activate(id) {
    current = id;
    var b = data.blocks.filter(function (x) { return x.id === id; })[0];
    var targets = Object.keys(b.why);
    blocksEl.querySelectorAll('.block').forEach(function (el) { el.setAttribute('aria-pressed', el.dataset.id === id ? 'true' : 'false'); });
    whoEl.querySelectorAll('li').forEach(function (el) {
      var on = targets.indexOf(el.dataset.id) !== -1;
      el.classList.toggle('on', on);
      el.classList.toggle('off', !on);
    });
    panel.innerHTML = '<h3>' + b.title + '</h3>' +
      '<div><h4>Что входит</h4><ul class="inside">' + b.inside.map(function (t) { return '<li><span>' + t + '</span></li>'; }).join('') + '</ul></div>' +
      '<div><h4>Кому и зачем</h4><ul class="for">' + targets.map(function (k) { return '<li><b>' + byId[k].title + '</b><span>' + b.why[k] + '</span></li>'; }).join('') + '</ul></div>';
    place();
    draw();
  }

  function place() {
    if (mq.matches) {
      var btn = blocksEl.querySelector('.block[data-id="' + current + '"]');
      if (btn && panel.parentNode !== btn.parentNode) btn.parentNode.appendChild(panel);
    } else if (panel.parentNode !== panelHome) {
      panelHome.appendChild(panel);
    }
  }

  function draw() {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    if (mq.matches || !current) return;
    var c = scheme.getBoundingClientRect();
    var btn = blocksEl.querySelector('.block[data-id="' + current + '"]');
    var a = btn.getBoundingClientRect();
    var sx = a.right - c.left, sy = a.top + a.height / 2 - c.top;
    var b = data.blocks.filter(function (x) { return x.id === current; })[0];
    Object.keys(b.why).forEach(function (k) {
      var t = whoEl.querySelector('li[data-id="' + k + '"]').getBoundingClientRect();
      var ex = t.left - c.left, ey = t.top + t.height / 2 - c.top;
      var dx = (ex - sx) / 2;
      var p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      p.setAttribute('d', 'M' + sx + ' ' + sy + ' C' + (sx + dx) + ' ' + sy + ', ' + (ex - dx) + ' ' + ey + ', ' + ex + ' ' + ey);
      svg.appendChild(p);
      var dot = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      dot.setAttribute('cx', ex); dot.setAttribute('cy', ey); dot.setAttribute('r', 3.5);
      svg.appendChild(dot);
    });
    var s0 = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    s0.setAttribute('cx', sx); s0.setAttribute('cy', sy); s0.setAttribute('r', 3.5);
    svg.appendChild(s0);
  }

  window.addEventListener('resize', function () { place(); draw(); });
  if (mq.addEventListener) mq.addEventListener('change', function () { place(); draw(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
  activate(startId || data.blocks[0].id);
}
