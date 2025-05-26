import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/felicidad.csv')
    print(dataset.head())

    # definir modelo
    reg = RandomForestRegressor()

    # definir grilla de parametro que usara el optimizador