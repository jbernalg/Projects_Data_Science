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

    # dividir los datos en features y target
    features = df_heart.drop(['target'], axis=1)
    target = df_heart['target']

    # normalizar los datos es vital al usar PCA
    features = StandardScaler().fit_transform(features)
    
    # dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)
    