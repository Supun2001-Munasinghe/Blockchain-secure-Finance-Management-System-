#!/usr/bin/env python
"""Quick check for AI imports without Django"""
import sys
import os

print("Checking TensorFlow...")
try:
    import tensorflow as tf
    print(f"✅ TensorFlow {tf.__version__} found")
except Exception as e:
    print(f"❌ TensorFlow issue: {e}")

print("\nChecking pandas...")
try:
    import pandas as pd
    print(f"✅ pandas found")
except Exception as e:
    print(f"❌ pandas issue: {e}")

print("\nChecking numpy...")
try:
    import numpy as np
    print(f"✅ numpy found")
except Exception as e:
    print(f"❌ numpy issue: {e}")

print("\nChecking sklearn...")
try:
    from sklearn.preprocessing import MinMaxScaler
    print(f"✅ sklearn found")
except Exception as e:
    print(f"❌ sklearn issue: {e}")

print("\nChecking LSTM model files...")
model_path = r"d:\Final Year Project\SecureAI_Finance_Smart_system\ai_models\saved"
if os.path.exists(model_path):
    files = os.listdir(model_path)
    print(f"✅ Models directory exists with {len(files)} files:")
    for f in files:
        print(f"   - {f}")
else:
    print("❌ Model directory not found")

print("\n✅ Basic dependencies check complete")
