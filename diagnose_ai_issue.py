#!/usr/bin/env python
"""
Diagnostic script to check AI page loading issues
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secureai_finance.settings')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

django.setup()

print("=" * 60)
print("🔍 AI PAGE LOADING DIAGNOSTIC")
print("=" * 60)

# Test 1: Check imports
print("\n✓ TEST 1: Checking AI module imports...")
try:
    from finance_app.ai_module import FinanceAIService
    print("   ✅ FinanceAIService imported successfully")
except Exception as e:
    print(f"   ❌ ERROR importing FinanceAIService: {e}")
    sys.exit(1)

# Test 2: Check AI views
print("\n✓ TEST 2: Checking AI views...")
try:
    from finance_app.ai_views import (
        AIPredictionView, AIGrowthAnalysisView,
        AIMarketForecastView, AIFraudCheckView,
        AIFinancialHealthView
    )
    print("   ✅ All AI views imported successfully")
except Exception as e:
    print(f"   ❌ ERROR importing AI views: {e}")
    sys.exit(1)

# Test 3: Check LSTM models exist
print("\n✓ TEST 3: Checking LSTM model files...")
model_dir = os.path.join(os.path.dirname(__file__), 'ai_models', 'saved')
models = ['bitcoin_lstm_model.keras', 'gold_lstm_model.keras', 'cse_lstm_model.keras']
for model in models:
    path = os.path.join(model_dir, model)
    if os.path.exists(path):
        size = os.path.getsize(path) / (1024 * 1024)  # Size in MB
        print(f"   ✅ {model} ({size:.2f} MB)")
    else:
        print(f"   ⚠️  {model} MISSING")

# Test 4: Check TensorFlow/Keras
print("\n✓ TEST 4: Checking TensorFlow/Keras...")
try:
    import tensorflow as tf
    print(f"   ✅ TensorFlow version: {tf.__version__}")
except ImportError:
    print("   ❌ TensorFlow not installed")
    sys.exit(1)

try:
    from ai_models.lstm_finance_model import LSTMFinanceModel
    print("   ✅ LSTMFinanceModel imported successfully")
except Exception as e:
    print(f"   ❌ ERROR importing LSTMFinanceModel: {e}")
    sys.exit(1)

# Test 5: Test AI methods
print("\n✓ TEST 5: Testing AI methods...")

# Test revenue forecast
try:
    result = FinanceAIService.get_revenue_forecast(6)
    if result.get('status') == 'success':
        print("   ✅ get_revenue_forecast() working")
    else:
        print(f"   ❌ get_revenue_forecast() returned: {result}")
except Exception as e:
    print(f"   ❌ ERROR in get_revenue_forecast(): {e}")

# Test growth analysis
try:
    result = FinanceAIService.get_growth_analysis()
    if result.get('status') == 'success':
        print("   ✅ get_growth_analysis() working")
    else:
        print(f"   ❌ get_growth_analysis() returned: {result}")
except Exception as e:
    print(f"   ❌ ERROR in get_growth_analysis(): {e}")

# Test financial health
try:
    result = FinanceAIService.get_financial_health()
    if result.get('status') == 'success':
        print("   ✅ get_financial_health() working")
    else:
        print(f"   ❌ get_financial_health() returned: {result}")
except Exception as e:
    print(f"   ❌ ERROR in get_financial_health(): {e}")

# Test market forecast (can take time)
print("\n   ⏳ Testing get_market_forecast() - this may take a minute...")
try:
    result = FinanceAIService.get_market_forecast('bitcoin', 'monthly')
    if result.get('status') == 'success':
        print("   ✅ get_market_forecast() working")
    else:
        print(f"   ❌ get_market_forecast() returned: {result}")
except Exception as e:
    print(f"   ❌ ERROR in get_market_forecast(): {e}")

# Test fraud check
try:
    result = FinanceAIService.get_fraud_risk({'amount': 5000, 'transaction_type': 'deposit'})
    if result.get('status') == 'success':
        print("   ✅ get_fraud_risk() working")
    else:
        print(f"   ❌ get_fraud_risk() returned: {result}")
except Exception as e:
    print(f"   ❌ ERROR in get_fraud_risk(): {e}")

print("\n" + "=" * 60)
print("✅ DIAGNOSTIC COMPLETE")
print("=" * 60)
