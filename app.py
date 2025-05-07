import os
import pandas as pd
from flask import Flask, request, render_template
from src.predict_pipeline import PredictPipeline

app = Flask(__name__)

CSV_FILE_PATH = "env/Notebook/data/crypto_data.csv"

def load_coins_from_csv():
    try:
        if not os.path.exists(CSV_FILE_PATH):
            raise FileNotFoundError(f"File not found: {CSV_FILE_PATH}")
        df = pd.read_csv(CSV_FILE_PATH)
        return df['coin'].dropna().unique().tolist()
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html', coins=load_coins_from_csv())

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form
        coin_id = form_data['coin']

        df = pd.read_csv(CSV_FILE_PATH)
        coin_row = df[df['coin'] == coin_id]
        if coin_row.empty:
            return render_template('index.html', coins=load_coins_from_csv(),
                                   prediction_text="Error: Coin not found.")
        coin_row = coin_row.iloc[0]

        def get_input(field):
            value = form_data.get(field)
            if value:
                if field == 'date':
                    return int(pd.to_datetime(value).strftime('%Y%m%d'))
                return float(value)
            return coin_row.get(field, 0)

        input_data = {
            'price': get_input('price'),
            '1h': get_input('1h'),
            '24h': get_input('24h'),
            '7d': get_input('7d'),
            '24h_volume': get_input('24h_volume'),
            'mkt_cap': get_input('mkt_cap'),
            'date': get_input('date'),
            'price_change': get_input('price_change'),
            'volume_change': get_input('volume_change'),
            'coin_category': get_input('coin_category'),
        }

        prediction_pipeline = PredictPipeline()
        result = prediction_pipeline.predict(input_data)

        return render_template('index.html', coins=load_coins_from_csv(),
                               prediction_text=f"🔮 Predicted Liquidity Ratio: {result:.2f}")
    except Exception as e:
        return render_template('index.html', coins=load_coins_from_csv(),
                               prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
