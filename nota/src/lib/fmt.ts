// Экранирует текст и подсвечивает заглушки ⟦…⟧ — места, где нужны факты от основателя.
export function fmt(s: string): string {
  const esc = s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return esc.replace(/⟦(.+?)⟧/g, '<mark class="todo">$1</mark>');
}
