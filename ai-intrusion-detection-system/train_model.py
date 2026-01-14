from preprocess import load_data
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

X, y = load_data("data/sample_logs.csv")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/ids_model.pkl")

print("✅ IDS Model trained and saved successfully")
