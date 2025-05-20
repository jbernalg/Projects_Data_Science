# manejo de datos
import pandas as pd

# modelos de regresion robusta
from sklearn.linear_model import (
    RANSACRegressor,
    HuberRegressor
)

# modelo de maquina de soporte vectorial
from sklearn.svm import SVR

# libreria para dividir los datos y metrica para evaluacion
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Script Principal
if __name__ == '__main__':
    
    # cargar datos 
    dataset = pd.read_csv('./data/felicidad_corrupt.csv')
    print(dataset.head())

    # seleccion de features
    X = dataset.drop(['country', 'score'], axis=1)
    y = dataset[['score']]

    # dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # obtener varios estimadores de forma efectiva
    estimadores = {
        'SVR' : SVR(gamma='auto', C=1.0, epsilon=0.1),
        'RANSAC' : RANSACRegressor(),
        'HUBER' : HuberRegressor(epsilon=1.35)
    }