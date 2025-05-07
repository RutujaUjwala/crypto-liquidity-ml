import streamlit as st
import pandas as pd
import numpy as np
from src.predict_pipeline import PredictPipeline

CSV_FILE_PATH = "env/Notebook/data/crypto_data.csv"

# Load CSV
@st.cache_data
def load_csv_data():
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        return df
    except Exception as e:
        st.error(f"Failed to load CSV: {e}")
        return pd.DataFrame()

df = load_csv_data()
coins = df['coin'].dropna().unique().tolist()

# Title
st.title("🔍 Predict Crypto Liquidity")

# Form
with st.form("prediction_form"):
    st.subheader("📊 Input Coin Data")

    coin = st.selectbox("Select a Coin", options=coins)

    default_row = df[df['coin'] == coin].iloc[0] if coin else {}

    price = st.text_input("Price", value=str(default_row.get('price', '')))
    h1 = st.text_input("1h % Change", value=str(default_row.get('1h', '')))
    h24 = st.text_input("24h % Change", value=str(default_row.get('24h', '')))
    d7 = st.text_input("7d % Change", value=str(default_row.get('7d', '')))
    vol24 = st.text_input("24h Volume", value=str(default_row.get('24h_volume', '')))
    mkt_cap = st.text_input("Market Cap", value=str(default_row.get('mkt_cap', '')))
    date = st.text_input("Date (YYYYMMDD)", value=str(default_row.get('date', '')))
    price_change = st.text_input("Price Change", value=str(default_row.get('price_change', '')))
    volume_change = st.text_input("Volume Change", value=str(default_row.get('volume_change', '')))
    coin_category = st.text_input("Coin Category", value=str(default_row.get('coin_category', '')))

    submitted = st.form_submit_button("Predict")

# Run prediction
if submitted:
    try:
        input_data = {
            'price': float(price),
            '1h': float(h1),
            '24h': float(h24),
            '7d': float(d7),
            '24h_volume': float(vol24),
            'mkt_cap': float(mkt_cap),
            'date': float(date),
            'price_change': float(price_change),
            'volume_change': float(volume_change),
            'coin_category': coin_category
        }

        model = PredictPipeline()
        result = model.predict(input_data)
        st.success(f"🔮 Predicted Liquidity Ratio: {result:.2f}")
    except ValueError as ve:
        st.error(f"Invalid input: {ve}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
