import pandas as pd

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/felicidad.csv')
    print(dataset.head())

    # saparamos features y target
    X = dataset.drop(['country', 'rank', 'score'], axis=1)
    y = dataset['score']

    # definir modelo
    reg = RandomForestRegressor()

    # definir grilla de parametro que usara el optimizador
    parametros = {
        'n_estimators': range(4,16), # rango de arboles
        'criterion': ['mse', 'mae'], # medida de calidad
        'max_depth': range(2, 11) # rango de limitacion del arbol
    }

    # definir optimizador
    # n_iter: maximo de muestreo. Elige una configuracion de parametros y lo itera
    # cv: validacion cruzada. Define el numero de pliegue en que se dividen los datos
    # scoring: metrica para evaluar el modelo
    rand_est = RandomizedSearchCV(reg, parametros, n_iter=10, cv=3, scoring='neg_mean_absolute_error').fit(X, y)

    # muestra mejor configuracion
    print(rand_est.best_estimator_)
    # muestra mejores parametros
    print(rand_est.best_params_)
    # obtener prediccion para la primera fila
    print(rand_est.predict(X.loc[[0]]))

    # valor real de score: 7.5944