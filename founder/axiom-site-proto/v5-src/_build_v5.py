#!/usr/bin/env python3
# Сборка страниц услуг варианта 5: общий стиль главной + схема + тело страницы
import json, pathlib
D = pathlib.Path(__file__).parent
base = (D / '_v5-base.css').read_text()
scheme_css = (D / '_scheme.css').read_text()
svc_css = (D / '_svc.css').read_text()
scheme_js = (D / '_scheme.js').read_text()

MODEL = {
  "who": [
    {"id": "owner", "title": "Собственник и инвестор"},
    {"id": "bank", "title": "Банк"},
    {"id": "cfo", "title": "Финансовый директор и бухгалтерия"},
    {"id": "pmo", "title": "Проектный офис"},
    {"id": "sales", "title": "Отдел продаж"}
  ],
  "blocks": [
    {"id": "inputs", "title": "Исходные данные", "short": "Параметры проекта и допущения",
     "inside": ["Типы и площади юнитов", "Затраты по статьям: земля, проектирование, разрешения, строительство", "Операционные расходы", "Цены продаж и условия рассрочек", "Налоговые ставки и условия финансирования"],
     "why": {"pmo": "Даёт и утверждает параметры проекта и сметы.", "cfo": "Сверяет условия финансирования и налоги.", "owner": "Видит, на каких допущениях построен расчёт."}},
    {"id": "tep", "title": "ТЭП", "short": "Технико-экономические показатели",
     "inside": ["Площади GFA и NSA, количество юнитов", "Стоимость строительства на 1 м²", "Целевая цена продажи на 1 м²", "Сводка параметров для утверждения"],
     "why": {"owner": "Утверждает концепцию и параметры проекта.", "pmo": "Сверяет проектные решения с утверждёнными параметрами.", "bank": "Оценивает параметры объекта при рассмотрении финансирования."}},
    {"id": "budget", "title": "Бюджет", "short": "Затраты по статьям и стадиям",
     "inside": ["CAPEX и OPEX по статьям", "Бюджет итого и на 1 м²", "Затраты по стадиям проекта", "Резервы"],
     "why": {"cfo": "Получает лимиты по статьям для контроля платежей.", "pmo": "Контролирует себестоимость и выбирает подрядчиков в рамках бюджета.", "owner": "Видит полную стоимость проекта."}},
    {"id": "schedule", "title": "График реализации", "short": "Сроки и последовательность работ",
     "inside": ["Сроки по стадиям проекта", "Помесячный график работ и платежей", "Авансы и длительность по статьям затрат", "График налоговых платежей"],
     "why": {"pmo": "Планирует работы и закупки.", "cfo": "Строит платёжный календарь.", "bank": "Видит, когда проекту потребуются средства."}},
    {"id": "cashflow", "title": "Cash Flow", "short": "Движение денег по месяцам",
     "inside": ["Помесячные поступления и платежи", "Укрупнённый бюджет с привязкой к графику", "Потребность в финансировании и её пик", "График финансирования", "Налоги"],
     "why": {"cfo": "Управляет ликвидностью и предотвращает кассовые разрывы.", "bank": "Оценивает потребность в финансировании и возможность возврата.", "owner": "Видит, сколько собственных средств потребуется и когда."}},
    {"id": "kpi", "title": "Инвестиционные показатели", "short": "Доходность проекта и инвестора",
     "inside": ["Прибыль, NPV, IRR, ROI, PI", "Срок окупаемости", "Показатели проекта и инвестора", "Сравнение вариантов концепции"],
     "why": {"owner": "Принимает решение о запуске и выбирает вариант концепции.", "bank": "Оценивает устойчивость проекта."}},
    {"id": "offers", "title": "Варианты для инвестора", "short": "Стратегии, сценарии, условия продаж",
     "inside": ["Продажа после строительства или сдача в аренду", "Сценарии цены выхода", "План продаж под требуемую доходность", "Условия для покупателей: цена, рассрочка, доходность аренды"],
     "why": {"owner": "Выбирает стратегию и условия выхода из проекта.", "sales": "Получает цены, рассрочки и расчёт доходности для покупателей."}}
  ]
}

CONTROL = {
  "who": [
    {"id": "exec", "title": "Исполнитель и прораб"},
    {"id": "pmo", "title": "Проектный офис и закупки"},
    {"id": "acc", "title": "Бухгалтерия"},
    {"id": "cfo", "title": "Финансовый директор"},
    {"id": "owner", "title": "Собственник и инвестор"}
  ],
  "blocks": [
    {"id": "request", "title": "Заявка", "short": "Подача заявки на оплату",
     "inside": ["Простая форма, доступная с телефона", "Фото или файл документа", "Распознавание суммы, контрагента и категории, включая рукописные чеки", "Около 30 секунд на одну заявку"],
     "why": {"exec": "Подаёт заявку без звонков и переписки и видит её статус.", "pmo": "Получает заявку сразу с документами."}},
    {"id": "approval", "title": "Согласование", "short": "Маршрут по регламенту",
     "inside": ["Заранее настроенный маршрут согласования", "Проверка цены и объёмов отделом закупок или ПТО", "Комментарии и документы в одном месте, без мессенджеров", "Статус каждой заявки виден участникам"],
     "why": {"pmo": "Проверяет цены, объёмы и себестоимость.", "cfo": "Видит очередь платежей и узкие места.", "exec": "Понимает, на каком этапе его заявка."}},
    {"id": "check", "title": "Контроль", "short": "Дубликаты и нарушения",
     "inside": ["Проверка документа на дубликат при загрузке", "Уведомления о нарушениях регламента", "Фиксация изменений в оплаченных заявках", "Журнал всех действий с платежами"],
     "why": {"owner": "Защищён от двойных оплат и злоупотреблений.", "cfo": "Получает уведомления о подозрительных действиях."}},
    {"id": "payment", "title": "Оплата", "short": "Оплата и документы",
     "inside": ["Бухгалтер фиксирует факт оплаты", "Документы архивируются автоматически", "Банковская книга обновляется сразу"],
     "why": {"acc": "Работает с полным комплектом документов по каждому платежу.", "cfo": "Видит фактические оплаты без ручного сведения."}},
    {"id": "ledger", "title": "Управленческий учёт", "short": "Классификация каждого платежа",
     "inside": ["План счетов под девелопмент и генподряд", "Привязка к проекту, статье, юниту и контрагенту", "Учёт поступлений: договор → счёт → оплата", "Для генподряда: смета (BOQ) → счёт → оплата"],
     "why": {"acc": "Ведёт учёт по единому плану счетов.", "cfo": "Получает данные, готовые для отчётности.", "pmo": "Видит затраты по проекту и статьям."}},
    {"id": "reports", "title": "Отчётность", "short": "Аналитика в реальном времени",
     "inside": ["ДДС и Cash Flow", "План-факт по проектам и статьям", "Дебиторская и кредиторская задолженность", "Производственный P&L по проектам"],
     "why": {"owner": "Видит финансы всех проектов без ручных отчётов.", "cfo": "Готовит отчётность для инвесторов и банков без ручного сведения.", "pmo": "Контролирует бюджет проекта онлайн."}}
  ]
}

def header():
    return '''<header class="top">
  <div class="wrap">
    <a class="logo" href="v5.html" aria-label="Axiom Consulting, на главную"><b>Axiom</b><small>consulting</small></a>
    <button class="burger" id="burger" aria-expanded="false" aria-controls="nav">Меню</button>
    <nav class="nav" id="nav" aria-label="Разделы">
      <a href="v5.html#cycle">Подход</a>
      <a href="v5.html#services">Услуги</a>
      <a href="v5.html#cases">Кейсы</a>
      <a href="v5.html#team">Команда</a>
      <span class="lang">RU · EN</span>
      <a class="btn primary" href="#request">Связаться</a>
    </nav>
  </div>
</header>'''

def form(service, others):
    opts = ["Финансовая модель проекта", "Аудит финансовой модели", "Контроль платежей и управленческий учёт", "Инвестиционный анализ", "Финансовый директор на аутсорсе", "Nota", "Другое"]
    options = ''.join('<option%s>%s</option>' % (' selected' if o == service else '', o) for o in opts)
    links = ''.join('<a href="%s"><span>%s</span><span aria-hidden="true">→</span></a>' % (h, t) for t, h in others)
    return '''  <section class="band soft" aria-labelledby="oth-h">
    <div class="wrap">
      <div class="head"><p class="kicker">Другие услуги</p><h2 class="h2" id="oth-h">Финансы проекта полного цикла</h2></div>
      <nav class="others" aria-label="Другие услуги">%s</nav>
    </div>
  </section>

  <section class="band" id="request" aria-labelledby="req-h">
    <div class="wrap req">
      <div>
        <p class="kicker">Контакты</p>
        <h2 class="h2" id="req-h" style="margin-top:16px">Обсудить проект</h2>
        <p class="lead" style="margin-top:18px">Оставьте контакт и выберите услугу. Мы свяжемся, чтобы уточнить задачу.</p>
        <div class="contacts">
          <div><span>E-mail</span><span class="ph">⟦e-mail⟧</span></div>
          <div><span>Telegram</span><span class="ph">⟦Telegram⟧</span></div>
          <div><span>WhatsApp</span><span class="ph">⟦WhatsApp⟧</span></div>
        </div>
      </div>
      <form id="req-form" novalidate>
        <div class="row2">
          <div class="field"><label for="f-name">Имя</label><input id="f-name" name="name" autocomplete="name"></div>
          <div class="field"><label for="f-contact">Контакт <small>Telegram, WhatsApp или e-mail</small></label><input id="f-contact" name="contact"></div>
        </div>
        <div class="field"><label for="f-service">Услуга</label><select id="f-service" name="service">%s</select></div>
        <div class="field"><label for="f-msg">Комментарий <small>необязательно</small></label><textarea id="f-msg" name="message"></textarea></div>
        <div><button class="btn primary" type="submit">Отправить</button></div>
        <p class="form-note">Нажимая кнопку, вы соглашаетесь с <a href="#request">политикой конфиденциальности</a>.</p>
        <p class="form-done" id="f-done" hidden>Это прототип: заявка никуда не отправляется.</p>
      </form>
    </div>
  </section>''' % (links, options)

FOOTER = '''<footer>
  <div class="wrap">
    <a class="logo" href="v5.html"><b>Axiom</b><small>consulting</small></a>
    <nav aria-label="Подвал"><a href="v5.html#cycle">Подход</a><a href="v5.html#services">Услуги</a><a href="v5.html#cases">Кейсы</a><a href="v5.html#team">Команда</a><a href="#request">Контакты</a></nav>
    <span class="ph">⟦юрлицо⟧</span>
  </div>
</footer>
<a class="back" href="index.html">← Все варианты</a>'''

COMMON_JS = '''(function () {
  var b = document.getElementById('burger'), n = document.getElementById('nav');
  b.addEventListener('click', function () { var o = n.classList.toggle('open'); b.setAttribute('aria-expanded', o ? 'true' : 'false'); });
  n.addEventListener('click', function (e) { if (e.target.tagName === 'A') { n.classList.remove('open'); b.setAttribute('aria-expanded', 'false'); } });
  document.getElementById('req-form').addEventListener('submit', function (e) { e.preventDefault(); document.getElementById('f-done').hidden = false; });
})();'''

def page(fname, title, body_file, root_id, data, start, service, others):
    body = (D / body_file).read_text()
    html = '''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Inter:wght@400;500;600&display=swap&subset=cyrillic,cyrillic-ext">
<style>
%s
%s
%s
</style>
</head>
<body>
%s
<main>
%s
%s
</main>
%s
<script>
%s
initScheme(document.getElementById('%s'), %s, '%s');
%s
</script>
</body>
</html>
''' % (title, base, scheme_css, svc_css, header(), body, form(service, others), FOOTER, scheme_js, root_id, json.dumps(data, ensure_ascii=False), start, COMMON_JS)
    (D / fname).write_text(html)
    print(fname, len(html))

page('v5-model.html', 'Axiom — финансовая модель', '_model.body.html', 'model-scheme', MODEL, 'cashflow',
     'Финансовая модель проекта',
     [("Аудит финансовой модели", "v5.html#svc-audit"), ("Контроль платежей и управленческий учёт", "v5-control.html"), ("Инвестиционный анализ", "v5.html#svc-invest"), ("Финансовый директор на аутсорсе", "v5.html#svc-cfo")])
page('v5-control.html', 'Axiom — контроль платежей', '_control.body.html', 'control-scheme', CONTROL, 'check',
     'Контроль платежей и управленческий учёт',
     [("Финансовая модель проекта", "v5-model.html"), ("Аудит финансовой модели", "v5.html#svc-audit"), ("Инвестиционный анализ", "v5.html#svc-invest"), ("Финансовый директор на аутсорсе", "v5.html#svc-cfo")])
