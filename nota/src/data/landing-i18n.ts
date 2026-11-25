// Языки главной (25.11): русский — исходные тексты (content-v12.ts), английский и индонезийский — собранные бандлы
// src/data/i18n/en.json и id.json (скрипт scripts/i18n-build.mjs из ru.json и переводов *-strings.json).
// UI — надписи, которые раньше были зашиты в разметке Landing.astro и ScreenSlot.astro.
import en from './i18n/en.json';
import id from './i18n/id.json';

export type Lang = 'ru' | 'en' | 'id';
export const bundles = { en, id } as const;
// 25.11, основатель: «основная версия на англ» — английская на /, русская на /ru/, индонезийская на /id/ (старый /en/ → / в public/_redirects)
export const homePath: Record<Lang, string> = { en: '/', ru: '/ru/', id: '/id/' };

export const UI = {
  ru: {
    skip: 'К содержанию', home: 'Nota — на главную', navLabel: 'Разделы', langLabel: 'Язык сайта', langName: 'русский',
    open: 'Открыть в Telegram', openSm: 'В Telegram', qrAlt: 'QR-код: открыть @NotaGetBot в Telegram',
    sheetTabs: 'Листы таблицы', shotFallback: (tab: string) => `Лист ${tab} на тестовых данных`,
    allPlans: 'Во всех тарифах:', plansAria: 'Тарифы', thPlan: 'Тариф', thDocs: 'Документов в месяц', thGroups: 'Группы', thPrice: 'Цена', thAction: 'Действие',
    docsWord: 'документов', perMonthTail: ' в месяц', groupsPrefix: 'Группы: ', perMo: ' / мес', planSr: ' — тариф ', over500: 'Более 500', docsPerMonth: 'документов в месяц',
    cmpAria: 'Сравнение: Nota, админ с Excel, приложение для расходов', question: 'Вопрос', yes: 'Плюс.', no: 'Минус.', mid: 'Отчасти.',
    who: 'Кто делает', faqTitle: 'Вопросы', finalQr: 'Или наведите камеру телефона', quick: 'Быстрый старт', docsNav: 'Документы',
    terms: 'Пользовательское соглашение', privacy: 'Политика конфиденциальности', refund: 'Правила возврата', support: 'Поддержка в боте',
    shotOpen: 'Открыть в полном размере', shotOpenNew: 'открыть в полном размере, в новой вкладке',
  },
  en: {
    skip: 'Skip to content', home: 'Nota — home', navLabel: 'Sections', langLabel: 'Site language', langName: 'English',
    open: 'Open in Telegram', openSm: 'Telegram', qrAlt: 'QR code: open @NotaGetBot in Telegram',
    sheetTabs: 'Sheet tabs', shotFallback: (tab: string) => `${tab} tab, test data`,
    allPlans: 'All plans include:', plansAria: 'Plans', thPlan: 'Plan', thDocs: 'Documents per month', thGroups: 'Groups', thPrice: 'Price', thAction: 'Action',
    docsWord: 'documents', perMonthTail: ' per month', groupsPrefix: 'Groups: ', perMo: ' / mo', planSr: ' — plan ', over500: 'Over 500', docsPerMonth: 'documents per month',
    cmpAria: 'Comparison: Nota, an admin with Excel, an expense app', question: 'Question', yes: 'Yes.', no: 'No.', mid: 'Partly.',
    who: 'Who is behind it', faqTitle: 'Questions', finalQr: 'Or point your phone camera here', quick: 'Quick start', docsNav: 'Documents',
    terms: 'Terms of Service', privacy: 'Privacy Policy', refund: 'Refund Policy', support: 'Support bot',
    shotOpen: 'Open full size', shotOpenNew: 'open full size in a new tab',
  },
  id: {
    skip: 'Langsung ke konten', home: 'Nota — beranda', navLabel: 'Bagian', langLabel: 'Bahasa situs', langName: 'Bahasa Indonesia',
    open: 'Buka di Telegram', openSm: 'Telegram', qrAlt: 'Kode QR: buka @NotaGetBot di Telegram',
    sheetTabs: 'Tab spreadsheet', shotFallback: (tab: string) => `Tab ${tab}, data contoh`,
    allPlans: 'Semua paket termasuk:', plansAria: 'Paket', thPlan: 'Paket', thDocs: 'Dokumen per bulan', thGroups: 'Grup', thPrice: 'Harga', thAction: 'Aksi',
    docsWord: 'dokumen', perMonthTail: ' per bulan', groupsPrefix: 'Grup: ', perMo: ' / bln', planSr: ' — paket ', over500: 'Lebih dari 500', docsPerMonth: 'dokumen per bulan',
    cmpAria: 'Perbandingan: Nota, admin dengan Excel, aplikasi pengeluaran', question: 'Pertanyaan', yes: 'Ya.', no: 'Tidak.', mid: 'Sebagian.',
    who: 'Siapa di baliknya', faqTitle: 'Pertanyaan', finalQr: 'Atau arahkan kamera ponsel ke sini', quick: 'Mulai cepat', docsNav: 'Dokumen',
    terms: 'Ketentuan Layanan', privacy: 'Kebijakan Privasi', refund: 'Kebijakan Pengembalian Dana', support: 'Bot dukungan',
    shotOpen: 'Buka ukuran penuh', shotOpenNew: 'buka ukuran penuh di tab baru',
  },
};
