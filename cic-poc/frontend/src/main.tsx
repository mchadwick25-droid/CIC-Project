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

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
