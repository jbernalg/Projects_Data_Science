# Importar librerias principales
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

# importar submodulos que contienen todo sobre kernel
from sklearn.decomposition import KernelPCA

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

    # validar que los datos esten correctamente divididos
    print(X_train.shape)
    print(y_train.shape)

    # configurar KernelPCA
    # si n_components no se define, PCA toma la cantidad total de features
    # define el kernel a usar
    kpca = KernelPCA(n_components=4, kernel='poly')

    # aplicar KPCA a los datos de entrenamiento
    kpca.fit(X_train)

    # aplicar KPCA a los datos de entrenamiento y prueba
    df_train = kpca.transform(X_train)
    df_test = kpca.transform(X_test)

    # configurar regresion logistica
    logistic = LogisticRegression(solver='lbfgs')

    # entrenamos el modelos con los datos de entrenamiento
    logistic.fit(df_train, y_train)

    # obtenemos una metrica para medir la efectividad del modelo
    print('SCORE KPCA: ', logistic.score(df_test, y_test))