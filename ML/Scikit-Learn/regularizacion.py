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