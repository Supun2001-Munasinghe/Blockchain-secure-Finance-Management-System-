#!/usr/bin/env python
"""
Quick fix for AI page loading issues
"""
import os
import json

print("=" * 60)
print("🔧 AI PAGE LOADING FIX")
print("=" * 60)

# 1. Check environment variables
print("\n1. Checking .env file...")
env_path = r"d:\Final Year Project\SecureAI_Finance_Smart_system\backend\.env"
if os.path.exists(env_path):
    print("   ✅ .env file exists")
    with open(env_path, 'r') as f:
        content = f.read()
        if 'DEBUG=True' in content:
            print("   ✅ DEBUG mode enabled")
        else:
            print("   ⚠️  DEBUG mode might be off (check manually)")
else:
    print("   ❌ .env file not found - this might be the issue!")
    print("   📝 Create a .env file in backend/ directory")

# 2. Check settings
print("\n2. Checking Django CORS settings...")
settings_path = r"d:\Final Year Project\SecureAI_Finance_Smart_system\backend\secureai_finance\settings.py"
with open(settings_path, 'r') as f:
    settings_content = f.read()
    if 'CORS_ALLOWED_ORIGINS' in settings_content:
        print("   ✅ CORS configured")
    else:
        print("   ⚠️  CORS might need configuration")

# 3. Check URLs
print("\n3. Checking URL routes...")
urls_path = r"d:\Final Year Project\SecureAI_Finance_Smart_system\backend\finance_app\urls.py"
with open(urls_path, 'r') as f:
    urls_content = f.read()
    ai_routes = ['ai/predict', 'ai/growth', 'ai/market', 'ai/fraud', 'ai/health']
    for route in ai_routes:
        if route in urls_content:
            print(f"   ✅ {route} endpoint registered")
        else:
            print(f"   ❌ {route} endpoint MISSING")

# 4. Check frontend API configuration
print("\n4. Checking frontend API configuration...")
api_path = r"d:\Final Year Project\SecureAI_Finance_Smart_system\frontend\src\services\api.js"
with open(api_path, 'r') as f:
    api_content = f.read()
    if 'aiAPI' in api_content:
        print("   ✅ aiAPI is configured in frontend")
        if 'getRevenueForecast' in api_content:
            print("   ✅ Revenue forecast method defined")
        if 'getMarketForecast' in api_content:
            print("   ✅ Market forecast method defined")
    else:
        print("   ❌ aiAPI not found in frontend")

print("\n" + "=" * 60)
print("FIX RECOMMENDATIONS:")
print("=" * 60)
print("""
1️⃣  Make sure backend is running:
   cd backend
   python manage.py runserver

2️⃣  Make sure frontend is running (in another terminal):
   cd frontend
   npm run dev

3️⃣  Check browser console (F12 → Console tab) for errors

4️⃣  Check the Network tab for failed API calls

5️⃣  If you see 401 Unauthorized:
   - Make sure you're logged in
   - Check if JWT token is stored in localStorage

6️⃣  If you see 500 error:
   - Check Django console for detailed error messages
""")
