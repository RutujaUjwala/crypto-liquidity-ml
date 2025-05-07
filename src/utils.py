def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "..", "model", "best_rf_model.pkl")
    with open(model_path, "rb") as f:
        return pickle.load(f)
