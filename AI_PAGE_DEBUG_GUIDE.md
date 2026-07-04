## 🛠️ AI Page Loading - Debug Guide

Your system configuration is **correct**. The issue is likely one of these:

---

### **STEP 1: Check if servers are running**

#### Terminal 1 - Backend
```bash
cd backend
python manage.py runserver
```
✅ You should see: `Quit the server with CTRL-BREAK`

#### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```
✅ You should see: `Local: http://localhost:5173`

---

### **STEP 2: Open browser and check console**

1. **Open browser** → Go to `http://localhost:5173` (or your frontend URL)
2. **Press F12** to open Developer Tools
3. **Click Console tab** and look for RED errors
4. **Click Network tab** and check for failed requests (red status codes)

---

### **STEP 3: Common errors and solutions**

#### ❌ Error: `GET /api/ai/predict 404`
**Problem:** Backend not running or routes not loaded
**Solution:** 
```bash
cd backend
python manage.py runserver
```

#### ❌ Error: `GET /api/ai/predict 500`
**Problem:** Server error in AI module
**Solution:** Check Django console for detailed error message

#### ❌ Error: `GET /api/ai/predict 401 Unauthorized`
**Problem:** Not logged in or token expired
**Solution:** 
- Log out and log back in
- Clear browser cookies/cache
- Check localStorage has `access_token`

#### ❌ Error: `Cannot GET /api/ai/predict`
**Problem:** API base URL might be wrong
**Solution:** 
Check frontend `src/services/api.js`:
```javascript
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';
```

#### ❌ Error: Page loads but data is empty/spinning forever
**Problem:** TensorFlow models taking time to load (first call can take 10-30 seconds)
**Solution:** 
- Wait longer (models are large ~100MB+ combined)
- Check Network tab - look for long pending requests
- Check Django console for progress

---

### **STEP 4: Check Django logs**

In your backend terminal, you should see logs like:
```
[timestamp] "GET /api/ai/health/ HTTP/1.1" 200 OK
[timestamp] "GET /api/ai/predict/ HTTP/1.1" 200 OK
```

If you see errors, paste them here.

---

### **STEP 5: Check if models are loading**

Run this quick test:
```bash
cd backend
python manage.py shell
```

Then paste this:
```python
from finance_app.ai_module import FinanceAIService
result = FinanceAIService.get_revenue_forecast(6)
print(result)
```

If it works, you'll see forecast data. If it hangs or errors, that's the issue.

---

### **STEP 6: Still stuck?**

Share these details with me:

1. What error message appears in browser console? (F12 → Console)
2. What's the Network status code? (F12 → Network → find `/api/ai/*` request)
3. What errors appear in Django console?
4. Is the page spinning/loading forever or is it showing an error?
5. When did this start? After any recent changes?

---

### **Quick Test URL**

Try this in browser to test backend:
```
http://localhost:8000/api/ai/health/
```

You should get JSON response (might show 401 if not logged in - that's OK).

---

**Come back with the console errors and I'll fix it! 🚀**
