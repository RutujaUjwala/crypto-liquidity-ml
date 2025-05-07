# 📄 Low-Level Design (LLD) - Cryptocurrency Liquidity Prediction

## 🔍 Component-Level Details

---

### 1. `main.py`

* Entry point for the FastAPI app
* Routes:

  * `/`: Renders form to enter coin and feature values
  * `/predict`: Handles form submission, loads defaults if fields are empty, and predicts liquidity ratio
* Uses `Jinja2Templates` for rendering `index.html`
* Reads from `crypto_data.csv` for coin-wise defaults

### 2. `model.py`

* Loads `best_rf_model.pkl` (Random Forest Regressor trained via RandomizedSearchCV)
* Contains `PredictPipeline`:

  ```python
  class PredictPipeline:
      def __init__(self):
          self.model = joblib.load("artifacts/best_rf_model.pkl")
      def predict(self, data: dict):
          df = pd.DataFrame([data])
          return float(self.model.predict(df)[0])
  ```

### 3. `schemas.py`

* Not heavily used in current version since HTML form is submitted, but can define JSON APIs if needed

### 4. `templates/index.html`

* Bootstrap form with dropdown of coins and input fields for features
* Uses conditional rendering to show predictions
* Compatible with FastAPI’s `Jinja2Templates`

### 5. `crypto_data.csv`

* Combined data from March 16–17, 2022
* Used to pre-fill default values when form inputs are left blank
* Derived features included:

  * `liquidity_ratio`
  * `price_change`
  * `volume_change`
  * `coin_category`

### 6. `eda/eda.ipynb`

* Distribution plots (histograms, KDEs, boxplots)
* Heatmaps for correlation
* Trend charts (mean price, volume, market cap)
* Outlier detection and capping using IQR
* VIF scores for multicollinearity

### 7. `notebooks/model_training.ipynb`

* Data splitting, scaling (`StandardScaler`)
* Multiple models tested: Linear Regression, Decision Tree, Random Forest, XGBoost
* Evaluation metrics: RMSE, MAE, R²
* Best model saved using `pickle`
* Feature importance and residual analysis included

---

## ⚙️ Workflow Example

1. User inputs features (or uses defaults)
2. Data passed to `PredictPipeline`
3. Model predicts liquidity ratio
4. Result shown on web UI

---

## 📌 Technologies Used

* Python 3.x, Pandas, Scikit-learn, XGBoost
* FastAPI, Jinja2, Bootstrap
* Matplotlib, Seaborn, Plotly

---

## 🧩 Notes

* Categorical field `coin_category` encoded numerically
* Outliers capped using IQR method
* VIF check ensures low multicollinearity
* Ready for JSON API extension if needed
