import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, KFold

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/felicidad.csv')
    print(dataset.head())