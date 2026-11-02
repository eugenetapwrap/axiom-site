import { defineConfig } from 'astro/config';

// Домен ещё не утверждён (axiomco.io или другой) — поправить перед запуском.
export default defineConfig({
  site: 'https://axiomco.io',
  build: { inlineStylesheets: 'always' },
});
