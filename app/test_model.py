# Adjust the import path if necessary, depending on where PredictPipeline is defined
try:
    from app.model import PredictPipeline
except ImportError:
    try:
        from Pipeline.prediction_pipeline import PredictPipeline
    except ImportError:
        print("❌ Could not import PredictPipeline. Check your file structure and import paths.")
        raise

# Sample input data matching your model's expected features
input_data = {
    'price': 35000,
    '1h': 0.5,
    '24h': 2.1,
    '7d': -1.5,
    '24h_volume': 1000000000,
    'mkt_cap': 50000000000,
    'date': 20250430,
    'price_change': 1200,
    'volume_change': 10000000,
    'coin_category': 2  # Or whatever encoding your model expects
}

# Run prediction
try:
    pipeline = PredictPipeline()
    prediction = pipeline.predict(input_data)
    print(f"✅ Prediction successful: {prediction}")
except Exception as e:
    print(f"❌ Prediction failed: {e}")