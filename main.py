from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import os

from app.model import PredictPipeline

app = FastAPI()

# Set up templates and static folder (for Bootstrap or assets)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

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

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    coins = load_coins_from_csv()
    return templates.TemplateResponse("index.html", {"request": request, "coins": coins})

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    coin: str = Form(...),
    price: float = Form(None),
    hour_1: float = Form(None, alias="1h"),
    hour_24: float = Form(None, alias="24h"),
    day_7: float = Form(None, alias="7d"),
    volume_24h: float = Form(None, alias="24h_volume"),
    mkt_cap: float = Form(None),
    date: str = Form(None),
    price_change: float = Form(None),
    volume_change: float = Form(None),
    coin_category: float = Form(None)
):
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        coin_row = df[df['coin'] == coin]
        if coin_row.empty:
            raise HTTPException(status_code=404, detail="Coin not found.")

        coin_row = coin_row.iloc[0]

        # Convert date string to int
        if date:
            date_int = int(pd.to_datetime(date).strftime('%Y%m%d'))
        else:
            date_int = coin_row.get('date', 0)

        def get_value(user_val, default_val):
            return float(user_val) if user_val is not None else default_val

        input_data = {
            'price': get_value(price, coin_row.get('price', 0)),
            '1h': get_value(hour_1, coin_row.get('1h', 0)),
            '24h': get_value(hour_24, coin_row.get('24h', 0)),
            '7d': get_value(day_7, coin_row.get('7d', 0)),
            '24h_volume': get_value(volume_24h, coin_row.get('24h_volume', 0)),
            'mkt_cap': get_value(mkt_cap, coin_row.get('mkt_cap', 0)),
            'date': date_int,
            'price_change': get_value(price_change, coin_row.get('price_change', 0)),
            'volume_change': get_value(volume_change, coin_row.get('volume_change', 0)),
            'coin_category': get_value(coin_category, coin_row.get('coin_category', 0)),
        }

        prediction_pipeline = PredictPipeline()
        result = prediction_pipeline.predict(input_data)

        return templates.TemplateResponse("index.html", {
            "request": request,
            "coins": load_coins_from_csv(),
            "prediction_text": f"🔮 Predicted Liquidity Ratio: {result:.4f}"
        })

    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "coins": load_coins_from_csv(),
            "prediction_text": f"❌ Error: {str(e)}"
        })
