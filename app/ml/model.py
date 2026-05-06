import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Leer dataset
df = pd.read_csv("app/data/logs.csv")

# Features
X = df[["failed_logins", "requests_per_minute"]]

# Crear modelo
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

# Entrenar
model.fit(X)

# Guardar modelo
joblib.dump(model, "app/models/anomaly_model.pkl")

print("Modelo entrenado y guardado")
