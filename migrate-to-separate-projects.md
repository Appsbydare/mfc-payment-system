# Migration Guide: Separating Frontend and Backend

This guide will help you migrate from the current monorepo structure to separate frontend and backend projects for better Vercel deployment.

## Current Issues

1. **Vercel Build Error**: The current setup confuses Vercel about which `package.json` to use
2. **Mixed Concerns**: Frontend and backend code are in the same repository
3. **Deployment Complexity**: Single deployment trying to handle both services

## Migration Steps

### Step 1: Create New Repositories

Create two new GitHub repositories:
- `mfc-payment-frontend`
- `mfc-payment-backend`

### Step 2: Migrate Frontend Code

1. **Copy frontend files to new repository:**
   ```bash
   # Create frontend directory structure
   mkdir mfc-payment-frontend
   cd mfc-payment-frontend
   
   # Copy frontend-specific files
   cp -r ../src ./
   cp -r ../public ./
   cp ../index.html ./
   cp ../vite.config.ts ./
   cp ../tsconfig.json ./
   cp ../tsconfig.node.json ./
   cp ../tailwind.config.js ./
   cp ../postcss.config.js ./
   cp ../package.json ./
   cp ../.gitignore ./
   ```

2. **Update package.json name:**
   ```json
   {
     "name": "mfc-payment-frontend",
     // ... rest of the file
   }
   ```

3. **Create Vercel configuration:**
   ```json
   // vercel.json
   {
     "buildCommand": "npm run build",
     "outputDirectory": "dist",
     "framework": "vite",
     "rewrites": [
       {
         "source": "/(.*)",
         "destination": "/index.html"
       }
     ]
   }
   ```

### Step 3: Migrate Backend Code

1. **Copy backend files to new repository:**
   ```bash
   # Create backend directory structure
   mkdir mfc-payment-backend
   cd mfc-payment-backend
   
   # Copy backend-specific files
   cp -r ../api/src ./
   cp ../api/package.json ./
   cp ../api/tsconfig.json ./
   cp ../api/env.example ./
   cp ../api/GOOGLE_SHEETS_SETUP.md ./
   cp ../api/VERCEL_DEPLOYMENT.md ./
   ```

2. **Update package.json name:**
   ```json
   {
     "name": "mfc-payment-backend",
     // ... rest of the file
   }
   ```

3. **Create Vercel configuration:**
   ```json
   // vercel.json
   {
     "version": 2,
     "builds": [
       {
         "src": "dist/index.js",
         "use": "@vercel/node"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "dist/index.js"
       }
     ]
   }
   ```

### Step 4: Update Environment Variables

#### Frontend Environment Variables
Create `.env` in frontend project:
```env
VITE_API_BASE_URL=https://your-backend-domain.vercel.app/api
VITE_APP_NAME=MFC Payment System
```

#### Backend Environment Variables
Create `.env` in backend project:
```env
PORT=3000
NODE_ENV=production
JWT_SECRET=your-jwt-secret
JWT_EXPIRES_IN=24h
GOOGLE_SHEETS_PRIVATE_KEY=your-private-key
GOOGLE_SHEETS_CLIENT_EMAIL=your-client-email
GOOGLE_SHEETS_SPREADSHEET_ID=your-spreadsheet-id
ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app
```

### Step 5: Update API Service Configuration

In the frontend project, update `src/services/api.ts`:

```typescript
// Update the base URL to point to your backend
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:3000/api';

export const api = axios.create({
  baseURL: API_BASE_URL,
  // ... rest of configuration
});
```

### Step 6: Deploy to Vercel

#### Deploy Backend First
1. Connect your `mfc-payment-backend` repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy and note the URL (e.g., `https://mfc-backend.vercel.app`)

#### Deploy Frontend
1. Connect your `mfc-payment-frontend` repository to Vercel
2. Set `VITE_API_BASE_URL` to your backend URL
3. Deploy and note the URL (e.g., `https://mfc-frontend.vercel.app`)

### Step 7: Update CORS Configuration

In your backend, ensure CORS allows your frontend domain:

```typescript
// src/index.ts or wherever CORS is configured
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:5173'],
  credentials: true
}));
```

## Benefits of This Approach

1. **Clear Separation**: Each project has its own concerns
2. **Independent Deployment**: Deploy frontend and backend separately
3. **Better Scaling**: Scale each service independently
4. **Easier Development**: Teams can work on each service independently
5. **Clearer CI/CD**: Separate build and deployment pipelines
6. **Better Error Handling**: Easier to identify which service has issues

## Post-Migration Checklist

- [ ] Both repositories are created and populated
- [ ] Environment variables are configured in both Vercel projects
- [ ] CORS is properly configured in backend
- [ ] Frontend API service points to correct backend URL
- [ ] Both applications deploy successfully
- [ ] Authentication flow works between frontend and backend
- [ ] All features are tested and working

## Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure `ALLOWED_ORIGINS` includes your frontend domain
2. **Environment Variables**: Double-check all environment variables are set in Vercel
3. **Build Failures**: Ensure each project has its own `package.json` and dependencies
4. **API Connection**: Verify the frontend is pointing to the correct backend URL

### Testing Locally

1. **Backend**: `npm run dev` (runs on port 3000)
2. **Frontend**: `npm run dev` (runs on port 5173)
3. **Set environment**: `VITE_API_BASE_URL=http://localhost:3000/api`

This migration will resolve your current Vercel deployment issues and provide a much cleaner, more maintainable architecture. 