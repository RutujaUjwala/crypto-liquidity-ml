# 🧾 High-Level Design (HLD) - Cryptocurrency Liquidity Prediction

## 📌 Objective

To design a machine learning pipeline that predicts cryptocurrency liquidity levels using historical data, with a local deployment interface via FastAPI.

---

## 🔧 System Components

### 1. **Data Layer**

* Raw historical data (price, volume, market cap, etc.)
* Source: Provided dataset from Assingment PW skills 

### 2. **Processing Layer**

* Preprocessing scripts to clean data
* Feature engineering (moving averages, volatility, ratios)

### 3. **Modeling Layer**

* Trained model: Regression (e.g., Random Forest, XGBoost)
* Output: Liquidity ratio prediction

### 4. **Serving Layer**

* FastAPI app for local deployment
* Endpoint `/predict` receives data and returns prediction
* Template rendering for form input/output using Jinja2

---

## 📊 Data Flow Diagram

'''
[Raw Data CSV] → [Preprocessing + Feature Engineering] → [ML Model] → [FastAPI Endpoint] → [HTML Output]
'''

---

## 🔌 Technology Stack

* **Python 3.x**
* **Pandas / NumPy / Scikit-learn** for data handling and modeling
* **FastAPI** for deployment
* **HTML + Bootstrap** for frontend UI
* **Jinja2** for server-side rendering

---

## ✅ Key Features

* Predicts liquidity for specific cryptocurrencies using historical data
* Web interface accepts manual or prefilled inputs
* Model is saved and reused using `joblib`

---

## 🗂️ File Overview

* `main.py`: FastAPI app, endpoints and routing
* `model.py`: Prediction logic, model loading
* `schemas.py`: Request/response models
* `index.html`: Bootstrap form interface
* `liquidity_model.pkl`: Trained ML model

---

## 📌 Future Scope

* Real-time data integration from APIs
* Cloud-based deployment (e.g., AWS, Azure)
* Alerting mechanism for low liquidity levels
