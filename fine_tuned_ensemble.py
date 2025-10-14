import os
import sys
import pandas as pd
import numpy as np

print("=== FINE-TUNED ENSEMBLES ===")

# Prefer a 'first_model_submission.csv' if present (e.g., Random Forest),
# otherwise fall back to CatBoost submission as the first model.
base1_path = 'first_model_submission.csv' if os.path.exists('first_model_submission.csv') else 'catboost_submission.csv'
if base1_path == 'catboost_submission.csv' and not os.path.exists('catboost_submission.csv'):
    print("Missing 'first_model_submission.csv' and fallback 'catboost_submission.csv'.")
    sys.exit(1)

required = [base1_path, 'lightgbm_submission.csv', 'xgboost_submission.csv', 'sample_submission.csv']
missing = [f for f in required if not os.path.exists(f)]
if missing:
    print(f"Missing required files for fine-tuned ensemble: {missing}")
    sys.exit(1)

m1_pred = pd.read_csv(base1_path)['accident_risk']
lgb_pred = pd.read_csv('lightgbm_submission.csv')['accident_risk']
xgb_pred = pd.read_csv('xgboost_submission.csv')['accident_risk']

weights_combinations = [
    [0.4, 0.35, 0.25],  # M1, LGB, XGB
    [0.45, 0.35, 0.20],
    [0.35, 0.40, 0.25],
]

for i, weights in enumerate(weights_combinations):
    ensemble = (
        m1_pred * weights[0] +
        lgb_pred * weights[1] +
        xgb_pred * weights[2]
    )
    submission = pd.read_csv('sample_submission.csv')
    submission['accident_risk'] = ensemble
    out_path = f'fine_ensemble_{i}.csv'
    submission.to_csv(out_path, index=False)
    print(f"Fine ensemble {i} created: M1 {weights[0]}, LGB {weights[1]}, XGB {weights[2]} -> {out_path}")

print("Fine-tuned ensembles ready!")
