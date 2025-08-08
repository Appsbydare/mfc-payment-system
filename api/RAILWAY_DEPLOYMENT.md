# Railway Deployment Guide

## Environment Variables to Set in Railway:

```env
# Server Configuration
PORT=5000
NODE_ENV=production

# Database Configuration
DATABASE_URL=file://./data.json

# JWT Configuration
JWT_SECRET=mfc-payment-system-2024-super-secure-jwt-secret-key-production
JWT_EXPIRES_IN=7d

# CORS Configuration
CORS_ORIGIN=https://mfc-payment-system.vercel.app

# File Upload Configuration
MAX_FILE_SIZE=10485760
UPLOAD_PATH=./uploads

# Email Configuration (for reports)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Rate Limiting
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100

# Logging
LOG_LEVEL=info
```

## Deployment Steps:

1. Connect your GitHub repository to Railway
2. Select the `api` folder as the source
3. Set the environment variables above in Railway dashboard
4. Deploy the service
5. Get the Railway URL (e.g., `https://mfc-payment-api.railway.app`)
6. Update the `vercel.json` in the frontend with the Railway URL

## Health Check:
After deployment, test: `https://your-railway-url.railway.app/api/health` 