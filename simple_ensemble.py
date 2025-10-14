import os
import sys
import pandas as pd
import numpy as np

print("=== SIMPLE ENSEMBLE ===")

required_files = [
    'lightgbm_submission.csv',
    'catboost_submission.csv',
    'xgboost_submission.csv',
    'sample_submission.csv',
]
missing = [f for f in required_files if not os.path.exists(f)]
if missing:
    print(f"Missing required files for ensembling: {missing}")
    sys.exit(1)

lightgbm_pred = pd.read_csv('lightgbm_submission.csv')['accident_risk']
catboost_pred = pd.read_csv('catboost_submission.csv')['accident_risk']
xgboost_pred = pd.read_csv('xgboost_submission.csv')['accident_risk']

weights = [0.5, 0.3, 0.2]  # LightGBM, CatBoost, XGBoost
ensemble_pred = (
    lightgbm_pred * weights[0] +
    catboost_pred * weights[1] +
    xgboost_pred * weights[2]
)

submission = pd.read_csv('sample_submission.csv')
submission['accident_risk'] = ensemble_pred
submission.to_csv('ensemble_submission.csv', index=False)

print("✅ Ensemble submission created!")
print(f"📊 LightGBM weight: {weights[0]}, CatBoost: {weights[1]}, XGBoost: {weights[2]}")
print(f"📊 Ensemble range: [{ensemble_pred.min():.3f}, {ensemble_pred.max():.3f}]")
