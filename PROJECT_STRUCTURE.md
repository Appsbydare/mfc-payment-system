# Project Structure Guide

This repo hosts both frontend (React) and backend (Node/Express) code plus archives and scripts. Use this as a quick primer for future improvements and for AI agents.

## Top-level layout
- `frontend/` React + Vite + TypeScript app (UI)
- `backend/` Express API (runs from compiled `dist/`)
- `archive/` and `project-archive/` historical snapshots, logs and docs
- `scripts/` utility scripts (e.g., CSV/XLSX helpers)
- `README.md` project notes

## Frontend (Vite + React + TS)
- Entry points: `frontend/index.html`, `frontend/src/main.tsx`, `frontend/src/App.tsx`
- Styling: TailwindCSS (`frontend/tailwind.config.js`, `frontend/src/index.css`)
- Routing/UI pages: `frontend/src/pages/`
  - `Dashboard.tsx`, `DataImport.tsx`, `RuleManager.tsx`, `DiscountManager.tsx`, `VerificationManager.tsx` (also contains Coaches Summary UI), etc.
- Components: `frontend/src/components/`
- State: Redux Toolkit slices in `frontend/src/store/` (e.g., `authSlice.ts`, `verificationSlice.ts`)
- API layer: `frontend/src/services/api.ts` (wraps backend endpoints; contains mock fallbacks)
- Config: `frontend/src/config/env.ts` (API base URL)

Run locally
```bash
cd frontend
npm i
npm run dev
```

Build
```bash
npm run build && npm run preview
```

Environment (Frontend)
- API base is configured in `src/config/env.ts`; for Vercel frontend project, set `VITE_API_BASE_URL` if needed.

## Backend (Express API)
- Runtime entry (on Vercel): `backend/dist/index.js`
- Source (not required at runtime): TypeScript sources previously under `src/`; compiled JS lives in `backend/dist/**`
- Routes: `backend/dist/routes/`
  - `auth.js`, `data.js`, `reports.js`, `discounts.js`, `rules.js`, `attendanceVerification.js`, `coaches.js`
- Services: `backend/dist/services/` (e.g., `googleSheets.js`)
- Middleware: `backend/dist/middleware/`
- Config: `backend/dist/config/database.js` (init), CORS, rate limiting in `dist/index.js`

Key endpoints
- `GET /api/health` health check
- `GET /api/data/*`, `POST /api/data/*` various data ops
- `POST /api/rules/*`, `POST /api/discounts/*` configuration
- `GET /api/attendance-verification/master` master verification dataset
- Coaches Summary
  - `GET /api/coaches/summary?fromDate=&toDate=`
  - `GET /api/coaches/:coachName/sessions?fromDate=&toDate=`

Environment (Backend)
- `CORS_ORIGIN` allowed origin for frontend
- Google Sheets:
  - `GOOGLE_SHEETS_SPREADSHEET_ID`
  - `GOOGLE_SHEETS_CLIENT_EMAIL`
  - `GOOGLE_SHEETS_PRIVATE_KEY` (JSON key; keep newlines as `\n` if needed)
  - optionally `GOOGLE_SHEETS_PROJECT_ID`
- Others: `NODE_ENV`, `RATE_LIMIT_WINDOW_MS`, `RATE_LIMIT_MAX_REQUESTS`

Run locally
```bash
cd backend
npm i
# Run compiled build directly
node dist/index.js
```

## Deploy model (Important)
We deploy from split repositories to keep Vercel simple:
- Frontend: `Appsbydare/mfc-payment-frontend` (Vercel project: mfc-payment-frontend)
- Backend: `Appsbydare/mfc-payment-backend` (Vercel project: mfc-payment-backend)

This monorepo (`Appsbydare/mfc-payment-system`) is the source of truth. We sync subtrees to the split repos:
```bash
# Frontend sync
git subtree split --prefix=frontend -b frontend-split
git push https://github.com/Appsbydare/mfc-payment-frontend.git frontend-split:main --force

# Backend sync
git subtree split --prefix=backend -b backend-split
git push https://github.com/Appsbydare/mfc-payment-backend.git backend-split:main --force
```

Backend Vercel config
- Uses `dist/index.js` as entry (`backend/vercel.json`)
- No build step required; compiled JS is committed

## Data sources
- Google Sheet `payment_calc_detail` powers verification and coaches summary
  - Important columns observed: `Customer Name`, `Event Starts At`, `Instructors`, `Status`, `Discount`, `Discount %`, `Invoice #`, `Amount`, `Payment Date`, `Package Price`, `Session Price`, `Discounted Session Price`, `Coach Amount`, `BGM Amount`, `Management Amount`, `MFC Amount`, `UniqueKey`

## Quick checks
- Health: `GET <backend>/api/health`
- Coaches summary: `GET <backend>/api/coaches/summary`
- Frontend base URL points to backend; verify CORS allows the frontend domain

## Conventions
- Typescript/JS: prefer explicit names, no 1–2 char identifiers
- Avoid try/catch unless handling known error cases
- Keep comments brief and meaningful

## Troubleshooting
- If Vercel fails building an old project connected to this monorepo, ensure it’s disconnected or configured with a Root Directory. Only the split repos should auto-deploy.
