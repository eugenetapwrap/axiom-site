// Контакты и ссылки. Всё, что помечено TBD, нужно подтвердить у Евгения.

// Ссылка в Telegram с готовой первой строкой сообщения
export const tgLink = (text?: string) =>
  text ? `https://t.me/ask_ketut?text=${encodeURIComponent(text)}` : 'https://t.me/ask_ketut';
export const site = {
  name: 'Axiom',
  legalName: 'PT Axiom Development Asia',
  telegram: 'ask_ketut',
  telegramUrl: 'https://t.me/ask_ketut',
  // TBD: ссылка на бота для чеков. Пока ведём в основной Telegram.
  botUrl: 'https://t.me/ask_ketut',
  // TBD: ссылка на канал «Где деньги, Кетут?». Пока пусто, ссылки на канал не показываются.
  channelUrl: '',
  channelName: 'Где деньги, Кетут?',
  email: 'evgenii@axiomco.io',
  // Портал клиента: управленческий учёт, заявки, дашборды.
  portalUrl: 'https://client.axiomco.io',
  description:
    'Финансовый консалтинг для девелопмента и строительства: финансовые модели, аудит моделей, управленческий учёт и контроль платежей. Юго-Восточная Азия и СНГ.',
};
