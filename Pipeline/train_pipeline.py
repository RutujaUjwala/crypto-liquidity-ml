# train_pipeline.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
import os

# Load the cleaned data
df = pd.read_csv(r"C:\Users\rutum\Desktop\flask2024\env\Notebook\data\preprocessed_crypto_data.csv")

# Define features and target
features = ['price', '1h', '24h', '7d', '24h_volume', 'mkt_cap',
            'date', 'price_change', 'volume_change', 'coin_category']
target = 'liquidity_ratio'

X = df[features]
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Hyperparameter grid
param_grid = {
    'n_estimators': [100, 200, 300, 320, 500],
    'max_depth': [20, 21, 22, 23, 24, 30, None],
    'min_samples_split': [2, 3, 5, 10, 11, 12, 20],
    'min_samples_leaf': [1, 2, 3, 4, 5, 6, 8],
    'max_features': ['auto', 'sqrt', 'log2', None],
    'bootstrap': [True, False]
}

# Initialize model and search
rf = RandomForestRegressor(random_state=42)
cv = KFold(n_splits=12, shuffle=True, random_state=42)
search = RandomizedSearchCV(estimator=rf, param_distributions=param_grid,
                             n_iter=50, cv=cv, scoring='r2',
                             random_state=42, n_jobs=-1)

# Train the model
search.fit(X_train_scaled, y_train)
best_rf = search.best_estimator_

# Evaluate
y_pred = best_rf.predict(X_test_scaled)
print("Best Parameters:", search.best_params_)
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Save model and scaler
os.makedirs("artifacts", exist_ok=True)
with open("artifacts/liquidity_model.pkl", "wb") as f:
    pickle.dump(best_rf, f)
with open("artifacts/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model and scaler saved successfully.")
