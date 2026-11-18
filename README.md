# SAHAAYA · ಸಹಾಯ

**An outcome-financed cooperative for sustainable digital inclusion.**
SAHAAYA means "help" in Kannada. The whole design is about the moment that help is no longer needed: a household counts as included only when it uses digital financial services on its own, again and again, and that has been independently verified.

This repository holds the **SAHAAYA Inclusion Platform**, the software that tracks each household's journey from assisted to independent use, verifies outcomes against evidence, prices them for an outcome payer, and reports progress to the community.

> **Proof of concept.** The platform opens on a **synthetic sample cohort** so every screen can be explored. None of it describes real people or real results. A separate, empty **live workspace** is provided for real records.

![Overview](docs/screenshots/overview.png)

---

## Contents

- [Context](#context)
- [Run it](#run-it)
- [What the platform does](#what-the-platform-does)
- [Core measures](#core-measures)
- [How outcomes are verified](#how-outcomes-are-verified)
- [Data protection](#data-protection)
- [Project structure](#project-structure)
- [Build and test](#build-and-test)
- [Documentation](#documentation)
- [Status and next steps](#status-and-next-steps)

---

## Context

| | |
|---|---|
| **Programme** | IEEE Connecting the Unconnected Challenge 2026, Business Models category |
| **Geography** | Ammathi, Bittangala and Pollibetta Gram Panchayats, Virajpet Taluk, Kodagu, Karnataka |
| **Release 1 scope** | Financial inclusion only: UPI payment, balance or statement check, bill payment or recharge, benefit (DBT) credit check, money transfer to family |
| **Team** | Dr. Chengappa Munjandira (lead), Subramanya Navada K R |

**The gap.** Many rural households have a bank account, a smartphone and money in the account, and still someone else makes the payment for them: a relative, a neighbour or a shopkeeper, sometimes with the household's PIN. On paper they are connected. In practice they are not.

**The model.** Local Digital Ambassadors, with women and youth prioritised, guide real tasks and step back as independence grows. They never transact on anyone's behalf. An outcome payer funds each household that is verified as independently and repeatedly using digital financial services. Attending a workshop is not an outcome. Independence is.

---

## Run it

The platform is a single self-contained HTML file with no server, no build step needed to run it, and no external services beyond Google Fonts.

1. **Open it directly.** Download [`index.html`](index.html) and open it in any modern browser (Chrome, Edge, Firefox, Safari), on desktop or phone.
2. **Or serve it locally:** `npx serve .` or `python3 -m http.server 8000` in the repository folder, then open the address shown.

### Deploy to Vercel

1. Go to <https://vercel.com/new> and import this GitHub repository.
2. Framework Preset: **Other**. Leave Build Command and Output Directory empty. There is no build step: `index.html` is committed already built.
3. Click **Deploy**.

Or from the CLI: `npm i -g vercel`, then `vercel` for a preview and `vercel --prod` for production.

[`vercel.json`](vercel.json) sets clean URLs and security headers, and [`.vercelignore`](.vercelignore) leaves tests out of the deployment. The platform uses hash-based routing (`#households`, `#field`, …), so no rewrites are needed.

### Or GitHub Pages

In the repository, go to **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/ (root)`, and save. The platform is then served at `https://krsnevam.github.io/sahaya/`.

Records are saved in the browser it is used in (`localStorage`). The sample cohort can be reset at any time from **Setup**. Use **Setup → Export workspace (JSON)** to keep a copy of live records.

---

## What the platform does

The platform implements the five components of the SAHAAYA model.

| Component | Where it lives | What it does |
|---|---|---|
| **Digital Inclusion Platform** | Overview, Households | Tracks every household through Access → Assisted use → First independent use → Repeat independent use → Verified outcome, under a pseudonymous reference |
| **AI Inclusion Copilot** | Households, Field work | Rule-based progression score (0 to 100) and next-step flags for stalled or dormant households, with an optional AI-drafted visit brief in English or Kannada when run inside Claude |
| **Outcome Verification Engine** | Verification | Confirms independence against a four-tier evidence hierarchy with sample-based audits; self-reported use never counts |
| **Community Outcome Dashboard** | Community board | Progress by Gram Panchayat in English or Kannada, printable, with no household identifiers and counts under 5 suppressed |
| **Digital Ambassador Operating Framework** | Field work | Recruitment profile, training records, code of conduct, the step-back ladder (explain → prompt → watch → alone) and Kannada picture cards for low-literacy users |

All screens:

| Screen | Purpose |
|---|---|
| **Overview** | IDFIR headline ("households that no longer need our help"), journey funnel, core measures, what needs attention |
| **Roadmap** | Five phases (baseline, Ambassadors, journeys, verification, payer test) with status read from the records, challenges planned for, next steps, support being sought |
| **Households** | Every household, its stage, progress score and Copilot flag; programme and comparison cohorts |
| **Field work** | Copilot-ordered visit lists, the Ambassador framework, and visual journeys |
| **Verification** | Evidence hierarchy, partner evidence imports, cohort reconciliation, audit queue, all claims |
| **Impact** | The six metrics, a fair comparison against a delayed-intervention cohort, the baseline, and an inclusion lens by gender, age, first-time users, Scheduled Tribe, vulnerable households and accessibility needs |
| **Community board** | Public-facing progress in English or ಕನ್ನಡ |
| **Partners** | Who pays for outcomes, the partners register, Outcome-Based Service Agreements and statements |
| **Finance** | The three-stage financing path, cost and outcome revenue, outcome payment coverage, demonstration capital, and a price test |
| **Scale** | Evidence gates that must hold before replicating, the repeatable unit per Gram Panchayat, connectivity, and the cooperative (unlocked only after validation) |
| **Ledger** | Append-only, SHA-256 hash-chained record of every entry, with an integrity check and CSV export |
| **Setup** | Workspaces, outcome rules and thresholds, Ambassadors, Gram Panchayats, data protection |

<table>
<tr>
<td width="50%"><img src="docs/screenshots/verification.png" alt="Verification hierarchy and cohort reconciliation"></td>
<td width="50%"><img src="docs/screenshots/impact.png" alt="Impact metrics and fair comparison"></td>
</tr>
<tr>
<td><img src="docs/screenshots/community-board-kannada.png" alt="Community board in Kannada"></td>
<td><img src="docs/screenshots/visual-journeys.png" alt="Kannada picture cards"></td>
</tr>
<tr>
<td><img src="docs/screenshots/finance.png" alt="Financing stages and price test"></td>
<td><img src="docs/screenshots/scale.png" alt="Evidence gates and repeatable unit"></td>
</tr>
</table>

---

## Core measures

| Measure | Definition |
|---|---|
| **IDFIR**, Independent Digital Financial Inclusion Rate | Households with verified repeat independent use ÷ eligible participating households |
| **Assisted-to-independent rate** | Households that completed a task alone ÷ households that received assisted sessions |
| **Repeat usage rate** | Independent users meeting the repeat rule (default: 3 tasks in 2 calendar months) |
| **Retention** | Still independently active a set time (default 60 days) after first independent use |
| **Cost per verified household** | Total programme cost ÷ verified independent households |
| **Payer ROI** | Institutional value created ÷ outcome payment |
| **Outcome payment coverage ratio** | Outcome-linked revenue ÷ recurring operating cost |

Training attendance, sessions run and self-reported use are **never** counted as outcomes. Full definitions and formulas: [docs/metrics-and-verification.md](docs/metrics-and-verification.md).

---

## How outcomes are verified

A claim opens when a household meets the repeat-use rule. It is then tested against the highest tier of evidence available:

1. **Institutional or platform evidence, where legally shareable.** A partner's monthly rows show the account digitally active, for households that consented. 10% audited.
2. **Cohort-level reconciliation using pseudonymous IDs.** Where rows cannot be shared, the partner returns only how many of a cohort's references were active. Our own claims for that month must not exceed it; an over-claimed month supports no outcome. 20% audited.
3. **Defined evidence rules where direct data is unavailable.** At least 3 transaction references (last 4 to 6 characters only) across 2 months. 30% audited.
4. **Independent sample-based audit,** on top of every tier. The auditor visits without the Ambassador and confirms the person performed the task themselves.

Every enrolment, session, survey, evidence import and decision is written to an append-only ledger in which each entry carries a SHA-256 hash of itself and the entry before it, so any later change breaks the chain.

---

## Data protection

- **No credentials stored.** No PIN, OTP, password, UPI ID, account number or phone number is ever entered. Free-text notes that look like one are refused.
- **Data minimisation.** A household is a reference such as `SH-AMM-0042`, its Gram Panchayat, a banded profile, three survey answers and its session record.
- **Consent and purpose limitation.** A household record needs consent; partner matching is a separate, optional consent. Withdrawal removes the household from every rate and payment.
- **Not a bank, Business Correspondent or payment provider.** No money moves through SAHAAYA.

Details: [docs/data-protection.md](docs/data-protection.md).

---

## Project structure

```
index.html                 the built platform: open or deploy this
vercel.json                Vercel settings: clean URLs, security headers
.vercelignore              files left out of the Vercel deployment
build.py                   joins src/ into index.html (and dist/artifact.html)
package.json               npm script shortcuts (no dependencies, no build step for hosting)
src/
  head.html                title, fonts and all styles (light and dark themes)
  body.html                application shell
  engine.js                ledger, journey rules, Copilot, verification, metrics, finance, evaluation, gates (no DOM)
  seed.js                  deterministic synthetic sample cohort and live-workspace defaults
  ui-core.js               state, persistence, formatters, icons, charts, overlays
  ui-views.js              Overview, Households, Field work, Verification, Ledger, Setup
  ui-views-plan.js         Roadmap, Impact, Community board, Partners, Finance, Scale
  ui-actions.js            forms, actions, events and start-up
test/
  engine.test.js           engine tests (Node, no dependencies)
  e2e.py                   end-to-end browser tests (Playwright)
docs/
  architecture.md
  metrics-and-verification.md
  data-protection.md
  demo-guide.md
  screenshots/
```

---

## Build and test

Requirements: Python 3.8+ to build, Node 18+ for engine tests, and Playwright for browser tests. The platform itself has no runtime dependencies.

```bash
python3 build.py                 # writes index.html and dist/artifact.html
node test/engine.test.js         # engine tests: hashing, ledger integrity, verification tiers, migration
pip install playwright && python -m playwright install chromium
python3 test/e2e.py              # full browser run, desktop, phone width and dark mode
```

Or with npm: `npm run bundle`, `npm test`, `npm run test:e2e`.

Edit files in `src/`, run `python3 build.py`, and commit the rebuilt `index.html` with your change. Do not edit `index.html` by hand. Hosting serves the committed `index.html` as it is.

---

## Documentation

- [Architecture](docs/architecture.md): modules, data model, ledger, derivation pipeline, persistence
- [Metrics and verification](docs/metrics-and-verification.md): every formula, rule and threshold
- [Data protection](docs/data-protection.md): what is stored, what never is, consent and withdrawal
- [Demo guide](docs/demo-guide.md): a five-minute walkthrough for reviewers

---

## Status and next steps

This is a proof of concept running on sample data. Next steps:

- Finalise the cohort and baseline with the three Gram Panchayats.
- Agree a legally shareable evidence mechanism with a financial institution.
- Onboard the first Digital Ambassadors.
- Move records from browser storage to shared, access-controlled storage designed to the Digital Personal Data Protection Act, 2023, with an offline-first Ambassador app.

The support being sought: a financial institution for evidence now and outcome payment after validation, a CSR or foundation outcome payer, IEEE mentors in outcome contracts, data protection and evaluation, and field partners in Virajpet Taluk.

## Licence

No licence has been chosen yet. Until one is added, all rights are reserved by the authors.
