@echo off
echo 🚀 Starting MFC Payment System deployment...

REM Check if we're in the correct directory
if not exist "package.json" (
    echo ❌ Error: package.json not found. Please run this script from the project root.
    exit /b 1
)

REM Build Frontend
echo 📦 Building frontend...
call npm run build:frontend
if %errorlevel% neq 0 (
    echo ❌ Frontend build failed
    exit /b 1
)
echo ✅ Frontend build completed

REM Build API
echo 🔧 Building API...
cd api
call npm run build
if %errorlevel% neq 0 (
    echo ❌ API build failed
    exit /b 1
)
cd ..
echo ✅ API build completed

echo 🎉 All builds completed successfully!
echo.
echo 📋 Next steps:
echo 1. Deploy frontend to Vercel (root directory)
echo 2. Deploy API to Vercel (api/ directory)
echo 3. Configure environment variables
echo 4. Update API URLs in frontend
echo.
echo 📖 See VERCEL_DEPLOYMENT.md for detailed instructions
pause 