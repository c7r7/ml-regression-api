from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load model (example: model.pkl must exist in your repo)
# model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return "ML Regression API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Example input: {"features": [1.2, 3.4, 5.6]}
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    
    # Replace below with your model's prediction
    # prediction = model.predict(features).tolist()
    prediction = [139.54, 179.51, 134.03, 291.41, 123.78]  # dummy
    
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
