@echo off
setlocal enabledelayedexpansion

echo 🚀 MFC Payment System - Separate Projects Deployment
echo ==================================================

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Vercel CLI is not installed. Please install it first:
    echo npm i -g vercel
    pause
    exit /b 1
)
echo [SUCCESS] Vercel CLI is installed

REM Create frontend project
echo [INFO] Creating frontend project...
if exist "frontend" (
    echo [WARNING] Frontend directory already exists. Removing...
    rmdir /s /q frontend
)

mkdir frontend
cd frontend

REM Copy frontend files
xcopy /e /i ..\src src\
xcopy /e /i ..\public public\
copy ..\index.html .\
copy ..\vite.config.ts .\
copy ..\tsconfig.json .\
copy ..\tsconfig.node.json .\
copy ..\tailwind.config.js .\
copy ..\postcss.config.js .\
copy ..\package.json .\

REM Update package.json name (simple replacement)
powershell -Command "(Get-Content package.json) -replace '\"name\": \"mfc-payment-system\"', '\"name\": \"mfc-payment-frontend\"' | Set-Content package.json"

REM Create vercel.json
echo {> vercel.json
echo   "buildCommand": "npm run build",>> vercel.json
echo   "outputDirectory": "dist",>> vercel.json
echo   "framework": "vite",>> vercel.json
echo   "rewrites": [>> vercel.json
echo     {>> vercel.json
echo       "source": "/(.*)",>> vercel.json
echo       "destination": "/index.html">> vercel.json
echo     }>> vercel.json
echo   ]>> vercel.json
echo }>> vercel.json

REM Create .gitignore
echo # Logs> .gitignore
echo logs>> .gitignore
echo *.log>> .gitignore
echo npm-debug.log*>> .gitignore
echo yarn-debug.log*>> .gitignore
echo yarn-error.log*>> .gitignore
echo pnpm-debug.log*>> .gitignore
echo lerna-debug.log*>> .gitignore
echo.>> .gitignore
echo node_modules>> .gitignore
echo dist>> .gitignore
echo dist-ssr>> .gitignore
echo *.local>> .gitignore
echo.>> .gitignore
echo # Editor directories and files>> .gitignore
echo .vscode/*>> .gitignore
echo !.vscode/extensions.json>> .gitignore
echo .idea>> .gitignore
echo .DS_Store>> .gitignore
echo *.suo>> .gitignore
echo *.ntvs*>> .gitignore
echo *.njsproj>> .gitignore
echo *.sln>> .gitignore
echo *.sw?>> .gitignore
echo.>> .gitignore
echo # Environment variables>> .gitignore
echo .env>> .gitignore
echo .env.local>> .gitignore
echo .env.development.local>> .gitignore
echo .env.test.local>> .gitignore
echo .env.production.local>> .gitignore
echo.>> .gitignore
echo # Build outputs>> .gitignore
echo build/>> .gitignore
echo out/>> .gitignore
echo.>> .gitignore
echo # Temporary files>> .gitignore
echo *.tmp>> .gitignore
echo *.temp>> .gitignore

echo [SUCCESS] Frontend project created successfully
cd ..

REM Create backend project
echo [INFO] Creating backend project...
if exist "backend" (
    echo [WARNING] Backend directory already exists. Removing...
    rmdir /s /q backend
)

mkdir backend
cd backend

REM Copy backend files
xcopy /e /i ..\api\src src\
copy ..\api\package.json .\
copy ..\api\tsconfig.json .\
copy ..\api\env.example .\
copy ..\api\GOOGLE_SHEETS_SETUP.md .\
copy ..\api\VERCEL_DEPLOYMENT.md .\

REM Update package.json name
powershell -Command "(Get-Content package.json) -replace '\"name\": \"mfc-payment-api\"', '\"name\": \"mfc-payment-backend\"' | Set-Content package.json"

REM Create vercel.json
echo {> vercel.json
echo   "version": 2,>> vercel.json
echo   "builds": [>> vercel.json
echo     {>> vercel.json
echo       "src": "dist/index.js",>> vercel.json
echo       "use": "@vercel/node">> vercel.json
echo     }>> vercel.json
echo   ],>> vercel.json
echo   "routes": [>> vercel.json
echo     {>> vercel.json
echo       "src": "/(.*)",>> vercel.json
echo       "dest": "dist/index.js">> vercel.json
echo     }>> vercel.json
echo   ],>> vercel.json
echo   "functions": {>> vercel.json
echo     "dist/index.js": {>> vercel.json
echo       "maxDuration": 30>> vercel.json
echo     }>> vercel.json
echo   }>> vercel.json
echo }>> vercel.json

REM Create .gitignore
echo # Dependencies> .gitignore
echo node_modules/>> .gitignore
echo npm-debug.log*>> .gitignore
echo yarn-debug.log*>> .gitignore
echo yarn-error.log*>> .gitignore
echo.>> .gitignore
echo # Build outputs>> .gitignore
echo dist/>> .gitignore
echo build/>> .gitignore
echo.>> .gitignore
echo # Environment variables>> .gitignore
echo .env>> .gitignore
echo .env.local>> .gitignore
echo .env.development.local>> .gitignore
echo .env.test.local>> .gitignore
echo .env.production.local>> .gitignore
echo.>> .gitignore
echo # Logs>> .gitignore
echo logs>> .gitignore
echo *.log>> .gitignore
echo.>> .gitignore
echo # Runtime data>> .gitignore
echo pids>> .gitignore
echo *.pid>> .gitignore
echo *.seed>> .gitignore
echo *.pid.lock>> .gitignore
echo.>> .gitignore
echo # Coverage directory used by tools like istanbul>> .gitignore
echo coverage/>> .gitignore
echo *.lcov>> .gitignore
echo.>> .gitignore
echo # nyc test coverage>> .gitignore
echo .nyc_output>> .gitignore
echo.>> .gitignore
echo # Dependency directories>> .gitignore
echo node_modules/>> .gitignore
echo jspm_packages/>> .gitignore
echo.>> .gitignore
echo # Optional npm cache directory>> .gitignore
echo .npm>> .gitignore
echo.>> .gitignore
echo # Optional eslint cache>> .gitignore
echo .eslintcache>> .gitignore
echo.>> .gitignore
echo # Microbundle cache>> .gitignore
echo .rpt2_cache/>> .gitignore
echo .rts2_cache_cjs/>> .gitignore
echo .rts2_cache_es/>> .gitignore
echo .rts2_cache_umd/>> .gitignore
echo.>> .gitignore
echo # Optional REPL history>> .gitignore
echo .node_repl_history>> .gitignore
echo.>> .gitignore
echo # Output of 'npm pack'>> .gitignore
echo *.tgz>> .gitignore
echo.>> .gitignore
echo # Yarn Integrity file>> .gitignore
echo .yarn-integrity>> .gitignore
echo.>> .gitignore
echo # dotenv environment variables file>> .gitignore
echo .env.test>> .gitignore
echo.>> .gitignore
echo # parcel-bundler cache (https://parceljs.org/)>> .gitignore
echo .cache>> .gitignore
echo .parcel-cache>> .gitignore
echo.>> .gitignore
echo # Next.js build output>> .gitignore
echo .next>> .gitignore
echo.>> .gitignore
echo # Nuxt.js build / generate output>> .gitignore
echo .nuxt>> .gitignore
echo.>> .gitignore
echo # Gatsby files>> .gitignore
echo .cache/>> .gitignore
echo public>> .gitignore
echo.>> .gitignore
echo # Storybook build outputs>> .gitignore
echo .out>> .gitignore
echo .storybook-out>> .gitignore
echo.>> .gitignore
echo # Temporary folders>> .gitignore
echo tmp/>> .gitignore
echo temp/>> .gitignore
echo.>> .gitignore
echo # Editor directories and files>> .gitignore
echo .vscode/*>> .gitignore
echo !.vscode/extensions.json>> .gitignore
echo .idea>> .gitignore
echo .DS_Store>> .gitignore
echo *.suo>> .gitignore
echo *.ntvs*>> .gitignore
echo *.njsproj>> .gitignore
echo *.sln>> .gitignore
echo *.sw?>> .gitignore
echo.>> .gitignore
echo # Database files>> .gitignore
echo *.db>> .gitignore
echo *.sqlite>> .gitignore
echo *.sqlite3>> .gitignore
echo.>> .gitignore
echo # Upload directories>> .gitignore
echo uploads/>> .gitignore
echo public/uploads/>> .gitignore

echo [SUCCESS] Backend project created successfully
cd ..

echo [INFO] Projects created successfully!
echo.
echo [INFO] Next steps:
echo 1. Update environment variables in both projects
echo 2. Deploy backend first: cd backend ^&^& vercel --prod
echo 3. Update frontend .env with backend URL
echo 4. Deploy frontend: cd frontend ^&^& vercel --prod
echo.
set /p response="Would you like to proceed with deployment now? (y/n): "

if /i "%response%"=="y" (
    echo [INFO] Deploying backend to Vercel...
    cd backend
    
    if not exist ".env" (
        echo [WARNING] No .env file found. Please create one with your environment variables.
        echo [INFO] You can copy from env.example and update the values.
    )
    
    echo [INFO] Running Vercel deployment for backend...
    vercel --prod
    
    echo [SUCCESS] Backend deployed successfully!
    echo [INFO] Note down the backend URL for frontend configuration.
    
    cd ..
    
    echo.
    echo [INFO] Please update the frontend .env file with your backend URL, then press Enter to continue...
    pause
    
    echo [INFO] Deploying frontend to Vercel...
    cd frontend
    
    if not exist ".env" (
        echo [WARNING] No .env file found. Creating template...
        echo VITE_API_BASE_URL=https://your-backend-domain.vercel.app/api> .env
        echo VITE_APP_NAME=MFC Payment System>> .env
        echo [INFO] Please update .env with your actual backend URL before deploying.
    )
    
    echo [INFO] Running Vercel deployment for frontend...
    vercel --prod
    
    echo [SUCCESS] Frontend deployed successfully!
    
    cd ..
    
    echo [SUCCESS] Both projects deployed successfully!
) else (
    echo [INFO] Deployment skipped. You can run the deployment manually later.
)

pause 