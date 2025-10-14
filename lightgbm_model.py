import os
import sys
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

print("=== LIGHTGBM MODEL ===")

required_files = ["train.csv", "test.csv", "sample_submission.csv"]
missing = [f for f in required_files if not os.path.exists(f)]
if missing:
    print(f"Missing required files: {missing}. Place them in the working directory.")
    sys.exit(1)

# Load data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Enhanced feature engineering
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    categorical_cols = [
        'road_type', 'lighting', 'weather', 'road_signs_present',
        'public_road', 'time_of_day', 'holiday', 'school_season'
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category').cat.codes

    # Interaction and polynomial features
    if {'curvature', 'speed_limit'}.issubset(df.columns):
        df['curvature_speed'] = df['curvature'] * df['speed_limit']
        df['curvature_squared'] = df['curvature'] ** 2
        df['speed_squared'] = df['speed_limit'] ** 2
    if {'lighting', 'weather'}.issubset(df.columns):
        df['lighting_weather'] = df['lighting'] * df['weather']
    if {'num_lanes', 'speed_limit'}.issubset(df.columns):
        df['lanes_speed'] = df['num_lanes'] * df['speed_limit']
    if {'curvature', 'speed_limit', 'num_reported_accidents'}.issubset(df.columns):
        df['total_risk_score'] = (
            df['curvature'] + df['speed_limit'] * 0.5 + df['num_reported_accidents'] * 2
        )

    return df

X_train = create_features(train.drop(columns=['id', 'accident_risk']))
y_train = train['accident_risk']
X_test = create_features(test.drop(columns=['id']))

print(f"Features: {X_train.shape[1]}")

X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

train_data = lgb.Dataset(X_tr, label=y_tr)
val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

params = {
    'objective': 'regression',
    'metric': 'rmse',
    'learning_rate': 0.05,
    'num_leaves': 31,
    'max_depth': -1,
    'min_data_in_leaf': 20,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'lambda_l1': 0.1,
    'lambda_l2': 0.1,
    'random_state': 42,
    'verbosity': -1,
}

model = lgb.train(
    params=params,
    train_set=train_data,
    num_boost_round=1000,
    valid_sets=[val_data],
    callbacks=[lgb.early_stopping(50), lgb.log_evaluation(100)],
)

val_pred = model.predict(X_val)
rmse = float(np.sqrt(mean_squared_error(y_val, val_pred)))
print(f"🎯 LightGBM Validation RMSE: {rmse:.6f}")

importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importance(),
}).sort_values('importance', ascending=False)
print("\n🔝 Top LightGBM Features:")
print(importance.head(10))

# Final predictions
test_pred = model.predict(X_test)
submission = pd.read_csv('sample_submission.csv')
submission['accident_risk'] = test_pred
submission.to_csv('lightgbm_submission.csv', index=False)

print("✅ LightGBM submission created!")
print(f"📊 Prediction range: [{test_pred.min():.3f}, {test_pred.max():.3f}]")
