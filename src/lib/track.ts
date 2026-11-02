// События для аналитики (план из исследования рынка 02.11.2026).
// Счётчик ещё не выбран: Plausible, Umami, GA4 или Яндекс Метрика. Функция отдаёт событие тому, что подключено,
// а без счётчика только складывает его в window.axiomEvents, чтобы проверить разметку в консоли.
type Props = Record<string, string | number | boolean>;

export function track(name: string, props: Props = {}) {
  const w = window as any;
  try {
    w.plausible?.(name, { props });
    w.umami?.track?.(name, props);
    w.gtag?.('event', name, props);
    if (w.ym && w.YM_ID) w.ym(w.YM_ID, 'reachGoal', name, props);
  } catch {
    // аналитика не должна ломать страницу
  }
  (w.axiomEvents ||= []).push({ name, props, t: Date.now() });
}
