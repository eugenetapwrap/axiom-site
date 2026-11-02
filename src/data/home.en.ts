// Тексты английской главной (ветка intl, 02.11.2026). Та же структура и те же цифры, что в home.ts:
// по исследованию рынка крупные клиенты в Индонезии читают сайты консультантов на английском.
// Перевод мой, Евгений его ещё не видел. Цифры не меняем, только формат: 25,000+ и 16.3%.
import type { Practice } from './home';

export const hero = {
  title: 'Financial planning and management accounting',
  audience: 'for developers and contractors',
  lines: ['Financial planning', 'and management accounting'],
  audLines: ['for developers', 'and contractors'],
  lead: '15 years in real estate development and construction. Southeast Asia and the CIS.',
  note: 'Southeast Asia and the CIS. We reply within a day',
  // Те же цифры, что в русской версии: 25 000+ платежей, $35 млн+
  stats: [
    { value: '15 years', text: 'in development and construction' },
    { value: '25,000+', text: 'payments processed through our control system' },
    { value: '$35M+', text: 'total value of these payments' },
  ],
};

export const practices: Practice[] = [
  {
    id: 'models',
    num: '01',
    title: 'Financial planning',
    card: 'A financial model at any project stage: for forecasting and control',
    lead: 'Cash flow and investor metrics: a project model from land purchase to sale or operation',
    items: [
      'Monthly project cash flow',
      'Investor metrics: NPV, IRR, MOIC, break-even',
      'Concept and scenario comparison',
      'Construction budget and schedule',
      'Sales plan, instalments, rentals',
      'Taxes and financing schedule',
      'Model updates on actuals',
      'In project currency and USD, with local taxes',
    ],
    result: 'A project model with monthly cash flow and an investor summary',
    cta: 'Discuss a model',
    topic: 'Hello! We need a financial model for a project.',
  },
  {
    id: 'accounting',
    num: '02',
    // Исследование: в Индонезии это описываем как внедрение системы, а не как бухгалтерские услуги
    title: 'Management accounting',
    card: 'Full financial control: from payment request to owner dashboard',
    lead: 'System implementation in 30 days, or accounting run by our team',
    items: [
      'Payment request and approval workflow',
      'Anti-fraud check for duplicates before payment',
      'Cash flow and plan vs actual by project',
      'BOQ, receivables and payables',
      'Dashboards for owners and investors',
      'ClickUp, Metabase, Google Sheets, Telegram bots',
    ],
    result: 'Accounts and plan vs actual for every project, an owner dashboard',
    cta: 'Discuss implementation',
    topic: 'Hello! We are interested in management accounting and payment control.',
  },
  {
    id: 'audit',
    num: '03',
    title: 'Financial model audit',
    card: 'Independent review of a model before a key decision',
    lead: 'We review models by third-party consultants and in-house teams before decisions are made on them',
    items: [
      'Express audit and full audit',
      'Formulas and links between sheets',
      'Validity of assumptions',
      'Impact of errors on profit, IRR and funding need',
      'Issues Log with three severity levels',
      'Recommended fixes',
    ],
    result: 'An Issues Log and profit and IRR recalculated for the errors found',
    cta: 'Send a model for review',
    topic: 'Hello! I would like to send a financial model for review.',
  },
  {
    id: 'advisory',
    num: '04',
    title: 'Investment analysis',
    card: 'Calculations and analysis for owner and investor decisions',
    lead: 'We answer one question with numbers: buy the property or not, what discount to give for full payment, which contractor to choose',
    items: [
      'Yield and value of a property',
      'Instalment plan vs upfront discount',
      'Bank statement analysis',
      'Tax burden calculation',
      'Selecting and vetting a general contractor',
    ],
    result: 'A calculation with a conclusion and a recommendation',
    cta: 'Discuss a task',
    topic: 'Hello! I have an investment analysis task.',
  },
];

export const results = {
  title: 'Results over 2 years',
  items: [
    { value: '$215k', text: 'of duplicates and errors stopped before payment, about 0.9% of costs' },
    { value: '4.7%', text: 'of transactions in the first weeks of accounting: duplicates, double payments, inflated prices' },
    { value: '3–5 days', text: 'it took to prepare an investor report. Now it builds automatically' },
  ],
};

export const cases = [
  {
    tag: 'Financial planning',
    problem: 'The model showed a cash gap',
    action: 'Fixed the model errors and tuned 12 project parameters',
    result: 'Peak funding within the set limits, with headroom',
  },
  {
    tag: 'Management accounting',
    problem: 'Invoices paid twice',
    action: 'Anti-fraud bot that checks the contents of documents',
    result: 'Duplicates are blocked before payment',
  },
  {
    tag: 'Management accounting',
    problem: 'Overpaying for materials',
    action: 'Plan vs actual on quantities and consumption rates',
    result: 'Discrepancy found in the first week',
  },
  {
    tag: 'Model audit',
    problem: 'Wrong assumption on the construction schedule',
    action: 'Audit of a third-party consultant’s model',
    result: 'IRR 9.0% → 8.2%, NPV 3.6 times lower',
  },
];

export const team = {
  title: 'Team',
  people: [
    { name: 'Evgenii Popov', role: 'Founder, 15 years in development', photo: '' },
    { name: 'Olga Petrova', role: 'Investment analyst', photo: '' },
    { name: 'Sergei Semenov', role: 'Software engineer', photo: '' },
  ],
};

export const method = {
  eyebrow: 'Methodology',
  title: 'How we build and review models',
  rules: {
    title: 'Modelling rules',
    items: [
      'Inputs, calculations and outputs on separate sheets',
      'One timeline: months from land purchase to exit',
      'No hard-coded numbers in formulas',
      'Units and currency on every row',
      'Checks sheet: cash balance, totals, signs',
      'Version and change log',
    ],
    note: 'Aligned with the principles of the FAST Standard and the ICAEW Financial Modelling Code',
  },
  audit: {
    title: 'Two-stage audit',
    steps: [
      { name: 'Express audit', text: 'Key assumptions, cash flow and investor metrics. The main risks of the model' },
      { name: 'Full audit', text: 'Every formula and link between sheets, validity of assumptions, independent recalculation of results, re-check after fixes' },
    ],
    deliverables: 'You receive a Review Report and an Issues Log',
    stat: {
      value: '63',
      text: 'issues found in one of our audits',
      parts: [
        { n: 7, label: 'critical', cls: 'hi' },
        { n: 38, label: 'significant', cls: 'mid' },
        { n: 18, label: 'minor', cls: 'lo' },
      ],
    },
  },
  limits: {
    title: 'What we do not do',
    items: [
      'We do not issue an opinion on the accuracy of forecasts',
      'We do not give legal or tax advice: we check how law and taxes are reflected in the model',
      'We do not replace a valuer: we check where market assumptions come from',
      'We do not do bookkeeping or statutory tax reporting',
    ],
  },
};

export const faq = [
  {
    q: 'How is Axiom different from an accounting firm?',
    a: 'Accountants handle source documents, taxes and statutory reporting. We work for the owner: cash flow forecasts, plan vs actual by project, payment control before payment, contractor and buyer balances. We do not replace your accountants: we take their data and bank statements and build a management view from them.',
  },
  {
    q: 'At what stage do you need a financial model?',
    a: 'Ideally before buying the land: the model helps decide whether to take the plot and on what terms. Then it is used to raise investor or bank funding. If construction is under way, we update the model on actuals: compare plan with actual and recalculate the project metrics.',
  },
  {
    q: 'Can you review a model built by another firm?',
    a: 'Yes. Send the model and a short project description. An express audit shows the main risks; a full audit checks formulas, links between sheets and the validity of assumptions. You receive an Issues Log with three severity levels and profit and IRR recalculated for the errors found.',
  },
  {
    q: 'How long does implementation take?',
    a: '30 days. First a diagnostic: which accounts, documents and spreadsheets exist. Then the chart of accounts, the payment route from request to payment, plan vs actual by project and an owner dashboard. After that your team can run the system, or you can hand it over to us.',
  },
  {
    q: 'Why a BOQ if you have a price per m²?',
    a: 'A price per m² is fine for a first estimate. A BOQ breaks it down into quantities and rates by work and material. It shows what the price includes and lets you check actuals against plan line by line.',
  },
  {
    q: 'Do you sign an NDA?',
    a: 'Yes, before you send a model, budget or bank statements. We do not name clients or projects, on the website or in conversations with other clients. The examples on this site are built on fictional projects.',
  },
  {
    q: 'Where do you work?',
    a: 'Southeast Asia and the CIS. Models and reports are kept in the project currency and in USD, with local taxes.',
  },
  {
    q: 'What languages do you work in?',
    a: 'English and Russian. The model and the report are prepared in the language your bank or investor needs.',
  },
  {
    q: 'How much does it cost?',
    a: 'It depends on scope: how many projects, how many scenarios in the model, whether you need accounting after implementation. We quote the exact fee and timeline in a proposal 2 days after the call.',
  },
  {
    q: 'What should I send to start?',
    a: 'A description of the task in your own words is enough. If you have a financial model, budget or BOQ, send them right away. Bank statements and system access we discuss on the call.',
  },
];

export const requestForm = {
  open: 'Request a proposal',
  title: 'Request for proposal',
  choose: 'Not selected',
  name: 'Name',
  company: 'Company',
  service: 'Service',
  services: ['Financial planning', 'Management accounting', 'Financial model audit', 'Investment analysis', 'Other'],
  country: 'Project country',
  countries: ['Indonesia', 'Thailand', 'UAE', 'Uzbekistan', 'Other'],
  stage: 'Project stage',
  stages: ['Land and concept', 'Design', 'Construction', 'Sales', 'Operation'],
  task: 'Task',
  taskHint: 'What you need and by when',
  channel: 'Reply via',
  submit: 'Send request',
  note: 'The form opens Telegram or your email with a ready message. Your data goes nowhere else.',
  greet: 'Hello! A request from the Axiom website.',
  subject: 'Request from the Axiom website',
};

export const finalCta = {
  title: 'Discuss your project',
  items: ['Financial model for review', 'Budget or BOQ', 'Short project description'],
  text: 'Describe the task in your own words. We reply within a day and send a proposal with fee and timeline 2 days after the call. We sign an NDA before you share any data.',
  itemsTitle: 'If you have them at hand, send right away:',
};

export const ketut = {
  q: 'Where’s the money, Ketut?',
  a: 'When you can see the road, you can walk faster, boss.',
};
