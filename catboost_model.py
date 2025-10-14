import os
import sys
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

print("=== CATBOOST MODEL ===")

required_files = ["train.csv", "test.csv", "sample_submission.csv"]
missing = [f for f in required_files if not os.path.exists(f)]
if missing:
    print(f"Missing required files: {missing}. Place them in the working directory.")
    sys.exit(1)

# Load data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

categorical_features = [
    'road_type', 'lighting', 'weather', 'road_signs_present',
    'public_road', 'time_of_day', 'holiday', 'school_season'
]

X_train = train.drop(columns=['id', 'accident_risk'])
y_train = train['accident_risk']
X_test = test.drop(columns=['id'])

# Map categorical feature names to indices present in X_train
cat_feature_indices = [i for i, c in enumerate(X_train.columns) if c in categorical_features]

X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

model = CatBoostRegressor(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    cat_features=cat_feature_indices,
    random_seed=42,
    verbose=100,
    early_stopping_rounds=50,
    loss_function='RMSE',
)

model.fit(X_tr, y_tr, eval_set=(X_val, y_val))

val_pred = model.predict(X_val)
rmse = float(np.sqrt(mean_squared_error(y_val, val_pred)))
print(f"🎯 CatBoost Validation RMSE: {rmse:.6f}")

importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.get_feature_importance(),
}).sort_values('importance', ascending=False)
print("\n🔝 Top CatBoost Features:")
print(importance.head(10))

# Final predictions
test_pred = model.predict(X_test)
submission = pd.read_csv('sample_submission.csv')
submission['accident_risk'] = test_pred
submission.to_csv('catboost_submission.csv', index=False)

print("✅ CatBoost submission created!")
