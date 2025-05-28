import joblib
import numpy as np

from flask import Flask
from flask import jsonify

# configurar servidor local
app = Flask(__name__)

# postman para pruebas
@app.route('/predict', methods=['GET'])
def predict():
    X_test = np.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
    prediccion = model.predict(X_test.reshape(1, -1))
    return jsonify({'prediccion': list(prediccion)})

if __name__ == '__main__':
    model = joblib.load('./models/best_model_0.932.pkl')
    app.run(port=8080)