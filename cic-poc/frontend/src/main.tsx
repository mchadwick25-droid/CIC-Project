import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import { GetMoreFrame } from './components/GetMoreFrame'

// Self-hosted brand typefaces (Increment 1 §1.2) - no font CDN. Alegreya
// Sans ships 400/500/700/800/900, not 600; 700 stands in for the spec's
// "600" UI-semibold weight.
import '@fontsource/alegreya/400.css'
import '@fontsource/alegreya/400-italic.css'
import '@fontsource/alegreya/500.css'
import '@fontsource/alegreya/700.css'
import '@fontsource/alegreya-sans/400.css'
import '@fontsource/alegreya-sans/500.css'
import '@fontsource/alegreya-sans/700.css'

import './app.css'

// The site's landing page frames the app with #get-more to show the offer panel alone.
const panelOnly = window.self !== window.top && window.location.hash === '#get-more'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    {panelOnly ? <GetMoreFrame /> : <App />}
  </React.StrictMode>,
)
