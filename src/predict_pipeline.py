import numpy as np
from src.utils import load_model

class PredictPipeline:
    def __init__(self):
        self.model = load_model()

    def predict(self, features):
        input_array = np.array([[
            features['price'],
            features['1h'],
            features['24h'],
            features['7d'],
            features['24h_volume'],
            features['mkt_cap'],
            features['date'],
            features['price_change'],
            features['volume_change'],
            features['coin_category']
        ]])
        return self.model.predict(input_array)[0]
