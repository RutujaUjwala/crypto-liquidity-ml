import pickle
import numpy as np
import pandas as pd
import os

class PredictPipeline:
    def __init__(self):
        # Load model and scaler
        model_path = os.path.join("artifacts", "liquidity_model.pkl")
        scaler_path = os.path.join("artifacts", "scaler.pkl")

        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)

        # Expected feature order
        self.features = ['price', '1h', '24h', '7d', '24h_volume', 'mkt_cap', 
                         'date', 'price_change', 'volume_change', 'coin_category']

    def predict(self, input_data: dict):
        try:
            # Ensure input order matches model
            input_values = [input_data[feature] for feature in self.features]

            # Convert to 2D array
            input_array = np.array(input_values).reshape(1, -1)

            # Scale input
            input_scaled = self.scaler.transform(input_array)

            # Predict
            prediction = self.model.predict(input_scaled)

            return prediction[0]

        except Exception as e:
            raise ValueError(f"Prediction failed: {str(e)}")