import joblib
import pandas as pd

model = joblib.load("model/ids_model.pkl")

def predict_attack(features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    confidence = max(model.predict_proba(df)[0]) * 100
    return ("Attack" if prediction == 1 else "Normal", round(confidence, 2))
