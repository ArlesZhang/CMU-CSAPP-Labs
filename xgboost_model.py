import os
import sys
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

print("=== XGBOOST MODEL ===")

required_files = ["train.csv", "test.csv", "sample_submission.csv"]
missing = [f for f in required_files if not os.path.exists(f)]
if missing:
    print(f"Missing required files: {missing}. Place them in the working directory.")
    sys.exit(1)

# Load data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Feature engineering
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    categorical_cols = [
        'road_type', 'lighting', 'weather', 'road_signs_present',
        'public_road', 'time_of_day', 'holiday', 'school_season'
    ]
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category').cat.codes

    if {'curvature', 'speed_limit'}.issubset(df.columns):
        df['curvature_speed_interaction'] = df['curvature'] * df['speed_limit']
        df['curvature_squared'] = df['curvature'] ** 2
        df['speed_squared'] = df['speed_limit'] ** 2
    if {'lighting', 'weather'}.issubset(df.columns):
        df['lighting_weather_interaction'] = df['lighting'] * df['weather']
    if {'curvature', 'speed_limit'}.issubset(df.columns):
        df['risk_factor'] = df['curvature'] + df['speed_limit'] * 0.1

    return df

X_train = create_features(train.drop(columns=['id', 'accident_risk']))
y_train = train['accident_risk']
X_test = create_features(test.drop(columns=['id']))

X_tr, X_val, y_tr, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

model = XGBRegressor(
    n_estimators=1000,
    learning_rate=0.1,
    max_depth=6,
    random_state=42,
    n_jobs=-1,
    objective='reg:squarederror',
)

model.fit(
    X_tr, y_tr,
    eval_set=[(X_val, y_val)],
    early_stopping_rounds=50,
    verbose=False,
)

val_pred = model.predict(X_val)
rmse = float(np.sqrt(mean_squared_error(y_val, val_pred)))
print(f"🎯 XGBoost Validation RMSE: {rmse:.6f}")

importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_,
}).sort_values('importance', ascending=False)
print("\n🔝 Top XGBoost Features:")
print(importance.head(10))

final_model = XGBRegressor(
    n_estimators=getattr(model, 'best_iteration', None) or 1000,
    learning_rate=0.1,
    max_depth=6,
    random_state=42,
    n_jobs=-1,
    objective='reg:squarederror',
)
final_model.fit(X_train, y_train)

predictions = final_model.predict(X_test)
submission = pd.read_csv('sample_submission.csv')
submission['accident_risk'] = predictions
submission.to_csv('xgboost_submission.csv', index=False)

print("✅ XGBoost submission created!")
print(f"📊 Prediction range: [{predictions.min():.3f}, {predictions.max():.3f}]")
