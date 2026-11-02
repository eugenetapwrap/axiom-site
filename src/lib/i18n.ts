// Язык страницы (ветка intl): русская главная на «/», английская на «/en/».
// Язык ставит страница до отрисовки (setLang), сборка идёт по одной странице за раз.
// В браузере язык берётся из <html lang>. Русский текст служит ключом: tr('Кейсы') → 'Cases'.
export type Lang = 'ru' | 'en';

let cur: Lang = typeof document !== 'undefined' && document.documentElement.lang === 'en' ? 'en' : 'ru';
export const setLang = (l: Lang) => { cur = l; };
export const lang = (): Lang => cur;
export const isEn = () => cur === 'en';
// Корень текущей версии сайта: якоря в меню и подвале ведут на свою языковую версию
export const root = () => (cur === 'en' ? '/en/' : '/');

// Разделители чисел: 25 000 и 16,3 по-русски, 25,000 и 16.3 по-английски
export const DEC = () => (cur === 'en' ? '.' : ',');
export const THOU = () => (cur === 'en' ? ',' : ' ');
// Число с d знаками после запятой и знаком минус «−»
export const dec = (v: number, d: number) => v.toFixed(d).replace('.', DEC()).replace('-', '−');

const EN: Record<string, string> = {
  // Шапка, подвал, общие подписи
  'Услуги': 'Services',
  'Методика': 'Methodology',
  'Калькуляторы': 'Calculators',
  'Кейсы': 'Cases',
  'Команда': 'Team',
  'Вопросы': 'FAQ',
  'Контакты': 'Contacts',
  'Направления': 'Services',
  'Компания': 'Company',
  'Axiom, на главную': 'Axiom, home page',
  'Основное меню': 'Main menu',
  'Личный кабинет клиента': 'Client portal',
  'Обсудить проект': 'Discuss your project',
  'Проверить модель': 'Review a model',
  'Перейти к содержанию': 'Skip to content',
  'Финансовый консалтинг для девелопмента и строительства. Юго-Восточная Азия и СНГ.': 'Financial consulting for real estate development and construction. Southeast Asia and the CIS.',
  'Кетут': 'Ketut',
  'Язык сайта': 'Site language',
  // Плавающая кнопка
  'Финмодель': 'Financial model',
  'Аудит модели': 'Model audit',
  'Учёт': 'Accounting',
  'Инвестанализ': 'Investment analysis',
  'Закрыть': 'Close',
  'Какая у вас задача?': 'What is your task?',
  'Написать без темы': 'Write without a topic',
  'Написать в Telegram': 'Message on Telegram',
  // Главная
  'Что входит': 'What is included',
  'Результат': 'Result',
  'Решение': 'Solution',
  'Посчитайте сами на сайте': 'Calculate it yourself on the site',
  'Вводите': 'You enter',
  'Получаете': 'You get',
  'Пример': 'Example',
  'Цифры в примерах — демо-данные.': 'Figures in the examples are demo data.',
  'Задачи, которые мы решали': 'Problems we have solved',
  'Клиентов и проекты не называем': 'We do not name clients or projects',
  'Частые вопросы': 'Frequently asked questions',
  'Не нашли ответ?': 'Did not find an answer?',
  'Напишите в Telegram': 'Message us on Telegram',
  'лимит': 'limit',
  'после': 'after',
  'запас': 'headroom',
  'до: разрыв': 'before: gap',
  'Заявка №': 'Request no.',
  'дубль': 'duplicate',
  'Норма': 'Norm',
  'Факт': 'Actual',
  // Демо-проекты и статьи (src/lib/sankey.ts, MiniJCurve)
  'Прочие проекты': 'Other projects',
  'Прочие': 'Other',
  'Поступления': 'Receipts',
  'Строительство': 'Construction',
  'Операционные': 'Operating',
  'Инвестиции': 'Investments',
  'Прирост остатка': 'Cash build-up',
  'Материалы': 'Materials',
  'Работы подрядчиков': 'Contractor works',
  'Инжиниринг': 'Engineering',
  'ФОТ и консалтинг': 'Payroll and consulting',
  'Налоги': 'Taxes',
  'Общие расходы': 'Overheads',
  'Основные средства': 'Fixed assets',
  'Осталось на счетах': 'Left on accounts',
  'Земля': 'Land',
  'Проектирование и инжиниринг': 'Design and engineering',
  'Мебель и оснащение': 'Furniture and equipment',
  'Налоги и сборы': 'Taxes and fees',
  'Резерв': 'Contingency',
  'Маркетинг и запуск': 'Marketing and launch',
  'Капитальные расходы': 'Capital expenditure',
  'Операционные расходы': 'Operating expenses',
  'Чистый поток': 'Net cash flow',
  'Основная': 'Basic',
  'Расширенная': 'Extended',
  'Вид схемы': 'Chart view',
  // Реестр замечаний (MiniRegister)
  'Критичное': 'Critical',
  'Существенное': 'Significant',
  'Незначительное': 'Minor',
  'График': 'Schedule',
  'Продажи': 'Sales',
  'Затраты': 'Costs',
  'Финансирование': 'Financing',
  'Ввод': 'Inputs',
  'Стройка 18 месяцев, а по договору генподряда 24': 'Construction takes 18 months, the general contract says 24',
  'Темп продаж выше, чем у соседних проектов': 'Sales pace is faster than at neighbouring projects',
  'Нет резерва на непредвиденные расходы': 'No contingency for unforeseen costs',
  'Проценты по кредиту начинаются с ввода, а не с первой выдачи': 'Loan interest starts at completion, not at first drawdown',
  'Курс валюты введён числом, а не ссылкой': 'Exchange rate typed in as a number, not linked to inputs',
  'Реестр замечаний, фрагмент': 'Issues Log, extract',
  'IRR в модели': 'IRR in the model',
  'После пересчёта': 'After recalculation',
  'Замечаний': 'Issues',
};

export function tr(s: string): string {
  if (cur !== 'en') return s;
  const v = EN[s];
  // Предупреждаем только о русском тексте без перевода: Arvo Residence и другие имена остаются как есть
  if (v === undefined && /[А-Яа-яЁё]/.test(s) && typeof console !== 'undefined') console.warn(`[i18n] нет перевода: ${s}`);
  return v ?? s;
}
