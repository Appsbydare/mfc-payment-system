#!/bin/bash

# MFC Payment System Deployment Script
echo "🚀 Starting MFC Payment System deployment..."

# Check if we're in the correct directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: package.json not found. Please run this script from the project root."
    exit 1
fi

# Build Frontend
echo "📦 Building frontend..."
npm run build:frontend
if [ $? -ne 0 ]; then
    echo "❌ Frontend build failed"
    exit 1
fi
echo "✅ Frontend build completed"

# Build API
echo "🔧 Building API..."
cd api
npm run build
if [ $? -ne 0 ]; then
    echo "❌ API build failed"
    exit 1
fi
cd ..
echo "✅ API build completed"

echo "🎉 All builds completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Deploy frontend to Vercel (root directory)"
echo "2. Deploy API to Vercel (api/ directory)"
echo "3. Configure environment variables"
echo "4. Update API URLs in frontend"
echo ""
echo "📖 See VERCEL_DEPLOYMENT.md for detailed instructions" 