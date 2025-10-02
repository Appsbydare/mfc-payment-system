# MFC Payment System - Response Guide

## Project Overview
This is a **monorepo-style project** for the MFC Payment System with separate frontend and backend repositories that need to be deployed independently. Each repository has its own Git repository and must be pushed separately.

## Project Structure
```
D:\01. Fiverr\602 - JR_New_Restore - 2\
├── frontend/          # React + TypeScript + Vite frontend
├── backend/           # Node.js + Express + TypeScript backend
├── api/               # Legacy API files (being migrated)
├── scripts/           # Utility scripts
└── [various config files]
```

## Technology Stack

### Frontend
- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **State Management**: Redux Toolkit
- **Routing**: React Router
- **UI Components**: Custom components with dark theme
- **API Client**: Custom API service
- **Notifications**: React Hot Toast

### Backend
- **Runtime**: Node.js
- **Framework**: Express.js
- **Language**: TypeScript (compiled to JavaScript)
- **Database**: Google Sheets API (primary data storage)
- **Authentication**: JWT
- **File Processing**: CSV parsing, Excel handling
- **Deployment**: Vercel

## Key Features Implemented
1. **Data Import System** - CSV/Excel file upload and processing
2. **Rule Manager** - Payment calculation rules management
3. **Discount Manager** - Discount codes and percentage management
4. **Verification Manager** - Payment verification and attendance tracking
5. **Reports System** - Data export and reporting
6. **Settings** - System configuration including Coaches management
7. **Google Sheets Integration** - All data persisted to Google Sheets

## Deployment Process

### Important: Separate Deployments Required
This project uses **separate repositories** for frontend and backend. Each must be deployed independently.

### Backend Deployment
```powershell
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Build TypeScript to JavaScript
npm run build

# Deploy to Vercel
vercel --prod
```

### Frontend Deployment
```powershell
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Build for production
npm run build

# Deploy to Vercel
vercel --prod
```

### Development Setup
**Note**: This project is deployed directly to Vercel without local testing. All environment variables are configured in the Vercel backend repository.

```powershell
# Backend (Terminal 1) - For development only
cd backend
npm start

# Frontend (Terminal 2) - For development only
cd frontend
npm run dev
```

## Environment Configuration

### Backend Environment Variables Required
**Note**: All environment variables are already configured in the Vercel backend repository. Google Sheets and Google Console settings are saved under environment variables in Vercel.

```env
# Server Configuration
PORT=5000
NODE_ENV=production

# CORS Configuration
CORS_ORIGIN=https://your-frontend-domain.vercel.app

# Google Sheets API Configuration (CRITICAL) - Already configured in Vercel
GOOGLE_SHEETS_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n"
GOOGLE_SHEETS_CLIENT_EMAIL=your-service-account@your-project.iam.gserviceaccount.com
GOOGLE_SHEETS_PROJECT_ID=your-project-id
GOOGLE_SHEETS_SPREADSHEET_ID=your-spreadsheet-id

# JWT Configuration
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_EXPIRES_IN=7d

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
```

### Frontend Environment Variables
```env
# API Configuration - Already configured in Vercel
VITE_API_URL=https://your-backend-domain.vercel.app/api
```

## Google Sheets Integration

### Required Sheets Structure
The system expects these sheets in the Google Spreadsheet:
- **attendance** - GoTeamUp attendance data
- **payments** - Historical payment data
- **rules** - Payment calculation rules
- **coaches** - Coach information (Instructors, Email, Hourly Rate, Status)
- **discounts** - Discount codes and rules
- **reports** - Generated reports
- **settings** - System configuration

### Coaches Sheet Format
```
| Instructors | Email | Hourly Rate | Status |
|-------------|-------|-------------|--------|
| Coach Name  | email@example.com | 45.00 | Active |
```

## API Endpoints

### Core Endpoints
- `GET /api/health` - Health check
- `GET /api/data/attendance` - Get attendance data
- `POST /api/data/import` - Import CSV/Excel files
- `GET /api/rules` - Get payment rules
- `POST /api/rules` - Create/update rules
- `GET /api/discounts` - Get discount rules
- `POST /api/discounts` - Create/update discounts
- `GET /api/coaches` - Get coaches data
- `POST /api/coaches` - Create coach
- `PUT /api/coaches/:id` - Update coach
- `DELETE /api/coaches/:id` - Delete coach

### Verification System
- `GET /api/attendance-verification/master` - Get verification master data
- `POST /api/attendance-verification/verify` - Verify payments
- `POST /api/attendance-verification/add-discounts` - Apply discounts
- `POST /api/attendance-verification/recalculate-discounts` - Recalculate amounts

## UI/UX Guidelines

### Design System
- **Primary Theme**: Dark mode with gray-800 backgrounds
- **Accent Color**: Primary blue (#3B82F6)
- **Text**: White text on dark backgrounds
- **Cards**: Rounded corners with backdrop blur
- **Tables**: Sticky headers, scrollable content
- **Buttons**: Rounded with proper hover states
- **Status Badges**: Color-coded (green=active, red=inactive)

### Component Styling Pattern
```tsx
// Main container
<div className="p-6">
  <h1 className="text-2xl font-bold text-white mb-4">Page Title</h1>
  
  // Tabs
  <nav className="flex gap-2" aria-label="Tabs">
    <button className={`px-3 py-2 text-sm font-medium rounded-md ${
      active ? 'bg-primary-600 text-white' : 'bg-gray-700 text-white hover:bg-gray-600'
    }`}>
      Tab Name
    </button>
  </nav>
  
  // Content cards
  <div className="bg-gray-800 p-4 rounded-lg">
    // Content here
  </div>
</div>
```

## Common Issues & Solutions

### Google Sheets Not Working
- Check environment variables are set correctly
- Verify service account has Editor access to spreadsheet
- Ensure private key is properly formatted with `\n` for line breaks

### Build Failures
- Run `npm install` in both frontend and backend
- Check TypeScript compilation errors
- Verify all imports are correct

### CORS Issues
- Update CORS_ORIGIN in backend environment
- Ensure frontend API_URL points to correct backend URL

## Development Workflow

### When Making Changes
1. **Backend Changes**: Modify TypeScript files in `backend/src/`, then run `npm run build`
2. **Frontend Changes**: Modify files in `frontend/src/`, Vite will hot-reload
3. **API Changes**: Update both backend routes and frontend API service
4. **Styling**: Follow the dark theme pattern established in Verification Manager

### Testing
**Note**: This project is deployed directly to Vercel without local testing. All testing is done on the production environment.

- Backend: Check Vercel logs for Google Sheets connection status
- Frontend: Verify API calls work in production environment
- Integration: Test full workflows (import → verify → export) on deployed application

## File Organization

### Backend Structure
```
backend/
├── src/
│   ├── config/        # Database and app configuration
│   ├── middleware/    # Express middleware
│   ├── routes/        # API route handlers
│   └── services/      # Business logic services
├── dist/              # Compiled JavaScript (generated)
├── api/               # Legacy API files (being migrated)
└── package.json
```

### Frontend Structure
```
frontend/
├── src/
│   ├── components/    # Reusable UI components
│   ├── pages/         # Page components
│   ├── services/      # API service layer
│   ├── store/         # Redux store and slices
│   ├── types/         # TypeScript type definitions
│   └── config/        # App configuration
├── public/            # Static assets
└── package.json
```

## Response Guidelines for AI Assistant

### When User Requests Changes
1. **Always check existing code structure** before making changes
2. **Follow the established patterns** (dark theme, API structure, etc.)
3. **Update both frontend and backend** if API changes are needed
4. **Test integration** between frontend and backend
5. **Document any new environment variables** or setup requirements

### Mandatory Response Footer (Every Conversation)
- Always append the "Git Push Commands" block (backend and frontend) tailored to this monorepo.
- If any deployment/build errors were seen in current or previous messages, list them briefly under "Known Deployment Errors" and confirm fixes or the next action.
- Keep the footer concise and copy-paste ready.

### Deployment Error Log (Running Ledger)
- Maintain a short running ledger of the latest deployment errors to avoid repeats.
- Update this list when new errors occur and when they are fixed.

Known Deployment Errors (examples)
- Frontend TS build: String has no call signatures in `VerificationManager.tsx` → fixed by using template literals instead of `String(...)` and ordering variable initialization.
- Frontend TS build: implicit any/self-referential initializer for `changeHistory` → fixed by explicit string typing and separate variables.

### Code Style Requirements
- Use TypeScript for type safety
- Follow existing naming conventions
- Maintain dark theme consistency
- Use proper error handling with toast notifications
- Include loading states for async operations

### Deployment Reminders
- **Always mention separate deployment** for frontend and backend
- **Provide PowerShell commands** for deployment
- **Check environment variables** are properly configured
- **Verify Google Sheets integration** is working

### Common User Requests
- **New features**: Implement in both frontend and backend
- **UI changes**: Follow Verification Manager styling pattern
- **Data management**: Ensure Google Sheets integration
- **Reports**: Use existing export functionality
- **Settings**: Add to Settings page with proper tab structure

## Quick Reference Commands

### Development
```powershell
# Backend
cd backend && npm start

# Frontend  
cd frontend && npm run dev

# Build backend
cd backend && npm run build
```

### Deployment
```powershell
# Backend deployment
cd backend && vercel --prod

# Frontend deployment
cd frontend && vercel --prod
```

### Troubleshooting
```powershell
# Check backend health (production)
curl https://your-backend-domain.vercel.app/api/health

# Check frontend (production)
# Open https://your-frontend-domain.vercel.app in browser
```

## Git Push Commands

### Backend Repository (always include)
```powershell
# Navigate to backend directory
cd backend

# Add all changes
git add .

# Commit the changes
git commit -m "Your commit message here"

# Push to backend repository
git push origin main
```

### Frontend Repository (always include)
```powershell
# Navigate to frontend directory
cd frontend

# Add all changes
git add .

# Commit the changes
git commit -m "Your commit message here"

# Push to frontend repository
git push origin main
```

---

When responding to the user, always end with the two Git Push blocks above and, if applicable, a brief "Known Deployment Errors" note reflecting the ledger here.

---

**Remember**: This project uses separate repositories for frontend and backend. Each must be pushed to its own Git repository independently. All environment variables are configured in Vercel, and the project is deployed directly to production without local testing.
