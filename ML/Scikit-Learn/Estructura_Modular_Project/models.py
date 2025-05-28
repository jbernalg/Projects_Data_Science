import pandas as pd
import numpy as np

from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

from utils import Utils

class Models:

    def __init__(self):
        self.reg = {
            'SVR': SVR(),
            'GRADIENT': GradientBoostingRegressor()
        }

        # diccionario de daiccionarios para definir parametros de los modelos
        self.params = {
            'SVR': {
                'kernel': ['linear', 'poly', 'rbf'],
                'gamma': ['auto', 'scale'],
                'C':[1,5,10 ]
            },
            'GRADIENT': {
                'loss': ['ls', 'lad'],
                'learning_rate': [0.01, 0.05, 0.1]
            }
        }
        