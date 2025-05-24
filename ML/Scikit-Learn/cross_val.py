import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, KFold

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/felicidad.csv')
    print(dataset.head())

    # Seleccionamos los features y el target
    X = dataset.drop(['country', 'score'], axis=1)
    y = dataset['score']

    # Definimos el modelo
    model = DecisionTreeRegressor()

    # realiza una validacion rapida
    # scoring: define el metodo a utilizar para hacer el calculo cd CV
    # por defecto, crea 5 pliegue con los datos
    score = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    print(score)