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