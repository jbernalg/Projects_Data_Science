import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/felicidad.csv')
    print(dataset.head())

    # Seleccionamos los features y el target
    X = dataset.drop(['country', 'score'], axis=1)
    y = dataset['score']

    # Definimos el modelo
    model = DecisionTreeRegressor()

    # realiza una validacion rapida con cross_val_score
    # scoring: define el metodo a utilizar para hacer el calculo cd CV
    # por defecto, crea 5 pliegue con los datos
    score = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    print(score)

    # obtenemos la media de los 5 scores de cada pliegue
    print(np.mean(score))

    # el score que interpretamos es el valor absoluto de la media anterior
    print(np.abs(np.mean(score)))

    # realiza una validadion con KFold para entender las particiones de los datos
    # n_split: define la cantidad de pliegues
    # shuffle: define el orden de los datos
    kf = KFold(n_splits=3, shuffle=True, random_state=42)

    # lista para almacenar la evaluacion del modelo en los diferentes pliegues
    mse_values = []

    # mostrar los 3 pliegues de datos generados
    for train, test in kf.split(dataset):
        print(train)
        print(test)

        # dividir cada pliegue en datos de entrenamiento y prueba
        X_train = X.iloc[train]
        y_train = y.iloc[train]
        X_test = X.iloc[test]
        y_test = y.iloc[test]

        # definir y entrenar el modelo     
        model = DecisionTreeRegressor().fit(X_train, y_train)

        # obtener las predicciones del modelo
        predict = model.predict(X_test)

        # evaluar el modelo y guardar evaluacion
        mse_values.append(mean_squared_error(y_test, predict)) 

    
    # mostrar metrica de evaluacion de cada modelo
    print('MSE de cada pliegue: ', mse_values)
    # mostrar promedio 
    print('MSE promedio: ', np.mean(mse_values))

        