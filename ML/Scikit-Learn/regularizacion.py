import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# script principal
if __name__ == '__main__':

    # cargar datos
    dataset = pd.read_csv('./data/felicidad.csv') 
    print(dataset.head())

    # dividir los datos en features y target
    # la seleccion de loa features ha sido personal
    X = dataset[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']]
    y = dataset[['score']]

    # verificar tamano de ambos conjuntos
    print(X.shape)
    print(y.shape)

    # dividir los datos en train y test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # definir modelo de regresion
    model_linear = LinearRegression().fit(X_train, y_train)

    # obtener predicciones del modelo de regresion
    y_pred_linear = model_linear.predict(X_test)

    # definir modelo con lasso
    # alpha hace referencia al parametro lambda. Por defecto tiene valor 1
    # a mayor alpha, mayor la penalizacion
    model_lasso = Lasso(alpha=0.02).fit(X_train, y_train)

    # obtener predicciones del modelo con lasso
    y_pred_lasso = model_lasso.predict(X_test)

    # definr modelo con ridge
    model_ridge = Ridge(alpha=1).fit(X_train, y_train)

    # obtener predicciones del modelo con ridge
    y_pred_ridge = model_ridge.predict(X_test)

     