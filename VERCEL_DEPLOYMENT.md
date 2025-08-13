# Vercel Deployment Guide

## Project Structure
This project consists of two parts:
- **Frontend**: React + Vite application (root directory)
- **API**: Express.js + TypeScript backend (`api/` directory)

## Deployment Strategy

### Option 1: Separate Deployments (Recommended)

#### Frontend Deployment
1. Deploy the root directory to Vercel
2. The `vercel.json` in the root is configured for frontend deployment
3. Build command: `npm run build:frontend`
4. Output directory: `dist`

#### API Deployment
1. Deploy the `api/` directory as a separate Vercel project
2. Use the `vercel.json` in the `api/` directory
3. Configure as serverless functions

### Option 2: Monorepo Deployment
If you want to deploy both together, you'll need to:
1. Configure Vercel to handle both frontend and API builds
2. Set up proper routing between frontend and API

## Environment Variables

### Frontend Environment Variables
Create a `.env` file in the root directory:
```
VITE_API_URL=https://your-api-domain.vercel.app
```

### API Environment Variables
Set these in your Vercel project settings:
```
NODE_ENV=production
PORT=5000
JWT_SECRET=your-super-secret-jwt-key-here
JWT_EXPIRES_IN=7d
CORS_ORIGIN=https://your-frontend-domain.vercel.app
MAX_FILE_SIZE=10485760
UPLOAD_PATH=./uploads
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100
LOG_LEVEL=info
```

## Deployment Steps

### 1. Frontend Deployment
1. Connect your GitHub repository to Vercel
2. Set the root directory as the source
3. Configure build settings:
   - Build Command: `npm run build:frontend`
   - Output Directory: `dist`
   - Install Command: `npm install`

### 2. API Deployment
1. Create a new Vercel project for the API
2. Set the source directory to `api/`
3. Configure build settings:
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

### 3. Update API URL
After both deployments are complete:
1. Update the frontend's API URL to point to your deployed API
2. Update the API's CORS_ORIGIN to allow your frontend domain

## Troubleshooting

### Common Issues
1. **Build Errors**: Ensure all dependencies are installed
2. **TypeScript Errors**: Check for type errors in both frontend and API
3. **Environment Variables**: Make sure all required env vars are set in Vercel
4. **CORS Issues**: Verify CORS_ORIGIN is set correctly

### Build Commands
- Frontend: `npm run build:frontend`
- API: `npm run build` (from api directory)

## File Structure
```
Jay R/
├── src/                    # Frontend source
├── api/
│   ├── src/               # API source
│   ├── package.json       # API dependencies
│   └── vercel.json       # API deployment config
├── package.json           # Frontend dependencies
└── vercel.json           # Frontend deployment config
``` 