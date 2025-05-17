# Importar librerias principales
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

# importar submodulos que contienen todo sobre PCA
from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

# importar modelo de regresion logistica
from sklearn.linear_model import LogisticRegression

# importar utilidades para procesar los datos
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Script pincipal
if __name__ == '__main__':
    
    # cargar dataset
    df_heart = pd.read_csv('./data/heart_bd.csv')
    print(df_heart.head(5))