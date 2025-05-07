# 📊 Final Report - Cryptocurrency Liquidity Prediction

---

## 📌 Project Title

**Cryptocurrency Liquidity Prediction for Market Stability**

---

## 🧠 Problem Statement

Cryptocurrency markets are highly volatile, and liquidity plays a crucial role in maintaining market stability. The objective of this project is to predict liquidity ratios using historical trading data and engineered market indicators. Early prediction of liquidity shortfalls can help traders and exchanges better manage financial risks.

---

## 📁 Dataset Overview

* **Source**: CoinGecko historical data (March 16 & 17, 2022)
* **Features**:

  * price, 1h, 24h, 7d percentage changes
  * trading volume (24h), market cap
  * engineered: `liquidity_ratio`, `price_change`, `volume_change`, `coin_category`
* **Target**: `liquidity_ratio`

---

## 🧼 Data Processing

* Missing values imputed with mean
* Duplicates removed
* Outliers capped using IQR method
* Date column converted to integer (day only)
* Categorical variable `coin_category` encoded numerically

---

## 🏗️ Feature Engineering

* **Liquidity Ratio**: `24h_volume / mkt_cap`
* **Price Change**: `price.diff()`
* **Volume Change**: `volume.diff()`
* **Coin Category**: binned based on market cap quantiles

---

## 📊 EDA Highlights

* Price, volume, and market cap are right-skewed
* Change % features are roughly normally distributed
* Market cap strongly correlates with 24h volume
* Top 10 coins like Bitcoin and Ethereum dominate liquidity

---

## 🤖 Model Training

* Models tested:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor ✅ (Best)
  * XGBoost Regressor

* Metrics (Random Forest):

  * **R²**: 0.968
  * **RMSE**: 0.0117
  * **MAE**: 0.0068

* Model saved as `best_rf_model.pkl`

---

## 🚀 Deployment

* FastAPI used to build prediction endpoint
* HTML form interface created with Bootstrap
* Default values loaded from CSV if user leaves fields blank
* Output shown on page after submission

---

## 📌 Insights

* Liquidity ratio is heavily dependent on market cap and trading volume
* Feature engineering significantly boosted model performance
* Model generalizes well despite short 2-day dataset due to normalization and careful handling of variance

---

## 🛠️ Limitations

* Limited to 2-day dataset
* No real-time or multi-exchange data yet
* No handling of sentiment/social data

---

## 🔮 Future Improvements

* Integrate real-time data feeds (CoinGecko API, Twitter, Reddit)
* Deploy on cloud (e.g., Streamlit, Render, or AWS Lambda)
* Add alerting for predicted low liquidity values
* Enhance feature set with sentiment analysis or technical indicators
