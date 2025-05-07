# 🔄 Pipeline Architecture - Cryptocurrency Liquidity Prediction

## 📌 Objective

Provide a clear step-by-step outline of how data flows from raw input to final prediction through various stages in the ML pipeline.

---

## 🧩 Architecture Overview

'''
[Raw CSV Data]
     ↓
[Data Merging (March 16 & 17)]
     ↓
[Data Cleaning]
     - Handling missing values (mean imputation)
     - Handling duplicates
     - Type conversion (e.g., date)
     ↓
[Feature Engineering]
     - Liquidity Ratio = 24h_volume / mkt_cap
     - Price Change = diff(price)
     - Volume Change = diff(24h_volume)
     - Coin Category based on market cap quantiles
     ↓
[Outlier Capping (IQR method)]
     ↓
[Feature Scaling]
     - StandardScaler applied to numeric features
     ↓
[Model Selection & Training]
     - Random Forest Regressor (tuned via RandomizedSearchCV)
     ↓
[Model Serialization]
     - Saved as `best_rf_model.pkl`
     ↓
[FastAPI Interface]
     - `/predict` endpoint accepts inputs
     - Uses default values if form inputs are empty
     ↓
[Output: Predicted Liquidity Ratio]
'''

---

## ⚙️ Tools & Technologies

* **Data Processing**: pandas, numpy
* **Visualization**: seaborn, matplotlib, plotly
* **Modeling**: scikit-learn, XGBoost
* **Serving**: FastAPI, Jinja2, Bootstrap
* **Model Persistence**: pickle

---

## 🧠 Notes

* Coin category is encoded numerically before modeling
* Data is from only two days (March 16 & 17, 2022)
* Pipeline avoids trimming to preserve small dataset

---

## ✅ Summary

This pipeline supports prediction of cryptocurrency liquidity using short-term historical data, outlier-robust feature transformations, and a locally hosted web interface for manual or automated input submission.
