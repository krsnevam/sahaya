# SAHAAYA Inclusion Platform

A single-page, self-contained web app (`index.html`). No build step, no dependencies.

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
npx serve .
```

## Deploy to Vercel

1. Go to <https://vercel.com/new> and import this GitHub repository.
2. Framework Preset: **Other**. Leave Build Command and Output Directory empty.
3. Click **Deploy**.

Or from the CLI:

```bash
npm i -g vercel
vercel        # preview
vercel --prod # production
```

`vercel.json` sets clean URLs and a few security headers. The app uses hash-based
routing (`#households`, `#field`, …), so no rewrites are needed.
