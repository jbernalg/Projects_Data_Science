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

    # validar que los datos esten correctamente divididos
    print(X_train.shape)
    print(y_train.shape)

    # configurar PCA
    # si n_components no se define, PCA toma la cantidad total de features
    pca = PCA(n_components=3)

    # aplicar PCA a los datos de entrenamiento
    pca.fit(X_train)

    # configurar IPCA
    ipca = IncrementalPCA(n_components=3, batch_size=10)

    # aplicar IPCA a los datos de entrenamiento
    ipca.fit(X_train)

    # visualizar la varianza de los componentes que PCA extrae
    plt.plot(range(len(pca.explained_variance_)), pca.explained_variance_ratio_)
    plt.show() 

    # configurar regresion logistica
    logistic = LogisticRegression(solver='lbfgs')

    # aplicar PCA a los features de entrenamiento y de prueba
    df_train = pca.transform(X_train)
    df_test = pca.transform(X_test)

    # aplicamos el modelos a ambos grupos de datos
    logistic.fit(df_train, y_train)

    # obtenemos una metrica para medir la efectividad del modelo
    print('SCORE PCA: ', logistic.score(df_test, y_test))

    # aplicar IPCA a los features de entrenamiento y de prueba
    df_train = ipca.transform(X_train)
    df_test = ipca.transform(X_test)

    # aplicamos el modelos a ambos grupos de datos
    logistic.fit(df_train, y_train)

    # obtenemos una metrica para medir la efectividad del modelo
    print('SCORE IPCA: ', logistic.score(df_test, y_test))

