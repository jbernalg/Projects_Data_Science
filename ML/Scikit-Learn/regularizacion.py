import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

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

    # definir modelo elasticNet
    model_elastic = ElasticNet(alpha=0.02).fit(X_train, y_train)

    # obtener predicciones del modelo elasticNet
    y_pred_elastic = model_elastic.predict(X_test)

    # Calcular perdida para cada modelo con la metrica error cuadratico medio
    linear_loss = mean_squared_error(y_test, y_pred_linear)
    print('Perdida lineal: ', linear_loss)

    lasso_loss = mean_squared_error(y_test, y_pred_lasso)
    print('Perdida lasso: ', lasso_loss)

    ridge_loss = mean_squared_error(y_test, y_pred_ridge)
    print('Perdida ridge: ', ridge_loss)

    elastic_loss = mean_squared_error(y_test, y_pred_elastic)
    print('Perdida ElasticNet: ', elastic_loss)

    # mostrar en tiempo real el efecto de los features sobre cada regresion
    print('='*32)
    print('Coeficientes lasso')
    print(model_lasso.coef_)

    print('='*32)
    print('Coeficientes ridge')
    print(model_ridge.coef_) 

    print('='*32)
    print('Coeficientes ElasticNet')
    print(model_elastic.coef_)
     