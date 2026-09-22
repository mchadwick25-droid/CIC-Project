import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

// Stage 3c (Build-Plan.md): "Add vitest + @testing-library/react, a test
// script, and a frontend-tests CI job." Separate from vite.config.ts on
// purpose - the dev-server proxy config there has no meaning for a test
// run, and vitest's own `test` block would just sit unused in the config
// vite itself reads for `dev`/`build`.
export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    // No globals: true - test files import describe/it/expect explicitly
    // from 'vitest', so the production tsconfig (tsc && vite build, which
    // type-checks everything under src/ including tests) never needs a
    // test-only ambient-types entry.
    setupFiles: ['./src/test/setup.ts'],
  },
});
