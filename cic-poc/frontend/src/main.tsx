import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'

// Self-hosted brand typefaces (Increment 1 §1.2) - no font CDN. Alegreya
// Sans ships 400/500/700/800/900, not 600; 700 stands in for the spec's
// "600" UI-semibold weight (see Decision-Log).
import '@fontsource/alegreya/400.css'
import '@fontsource/alegreya/400-italic.css'
import '@fontsource/alegreya/500.css'
import '@fontsource/alegreya/700.css'
import '@fontsource/alegreya-sans/400.css'
import '@fontsource/alegreya-sans/500.css'
import '@fontsource/alegreya-sans/700.css'

import './styles/table.css'
// Two-tier citation styling. Kept in its own file rather than folded into
// table.css because it is one self-contained decision with its own
// reasoning - but a stylesheet nothing imports is dead, and this one was:
// added 2026-08-10 with the two-tier work, never wired up, so the
// consulted/drawn-on distinction rendered identically in the browser for
// the whole of that change's life. Vite only bundles what is imported.
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
