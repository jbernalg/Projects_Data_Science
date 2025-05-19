import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# script principal
if __name__ == '__main__':
    dataset = pd.read_csv('./data/felicidad.csv') 
    print(dataset.head())