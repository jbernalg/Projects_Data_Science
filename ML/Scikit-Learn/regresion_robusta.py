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

# evita mostrar los warnings
import warnings
warnings.simplefilter('ignore')

# libreria para visualizacion
import matplotlib.pyplot as plt

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

    # diccionarios de estimadores
    estimadores = {
        'SVR' : SVR(gamma='auto', C=1.0, epsilon=0.1),
        'RANSAC' : RANSACRegressor(),
        'HUBER' : HuberRegressor(epsilon=1.35)
    }

    # entrenando y evaluando estimadores
    for name, estimador in estimadores.items():
        estimador.fit(X_train, y_train)
        prediccion = estimador.predict(X_test)

        print('-'*64)
        print(name)
        print('MSE: ', mean_squared_error(y_test, prediccion))
        
        # viualizacion de las predicciones vs valores reales
        plt.ylabel('Predicciones')
        plt.xlabel('Datos Reales')
        plt.title(f'Predicciones {name} VS Datos Reales')
        plt.scatter(y_test, prediccion)
        plt.plot(prediccion, prediccion,'r--')
        plt.show()
        
