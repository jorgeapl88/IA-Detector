import joblib
import numpy as np

# Cargar modelo
model = joblib.load("app/models/anomaly_model.pkl")

def predict_anomaly(failed_logins, requests_per_minute):

    data = np.array([[failed_logins, requests_per_minute]])

    prediction = model.predict(data)

    return prediction[0]
