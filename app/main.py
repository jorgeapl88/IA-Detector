from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI()

# 1. Cargamos el modelo entrenado al iniciar el servidor
MODEL_PATH = "app/models/anomaly_model.pkl"

@app.get("/")
def home():
    return {"message": "API de Detección de IA lista"}

@app.post("/analyze")
def analyze_logs(data: dict):
    # Verificamos si el modelo existe
    if not os.path.exists(MODEL_PATH):
        return {"error": "El modelo no ha sido entrenado. Ejecuta model.py primero."}

    # 2. Cargamos el cerebro de la IA
    model = joblib.load(MODEL_PATH)
    
    # 3. Convertimos los datos que enviaste en Swagger a un formato que la IA entienda
    # Usamos los mismos nombres que en el entrenamiento
    input_data = pd.DataFrame([[data["failed_logins"], data["requests_per_minute"]]])
    
    # 4. La IA predice: 1 es normal, -1 es ANOMALÍA (ataque)
    prediction = model.predict(input_data)[0]
    
    status = "NORMAL" if prediction == 1 else "ANOMALÍA DETECTADA"
    threat_detected = True if prediction == -1 else False

    # 5. Respuesta final como la de tu guía
    return {
        "threat": threat_detected,
        "status": status,
        "action": "BLOCK" if threat_detected else "NONE"
    }