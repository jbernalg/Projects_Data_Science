import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    # cargar los datos
    df_heart = pd.read_csv('./data/heart_bd.csv')
    # estadistica de target
    print(df_heart['target'].describe())

    # seleccionar los features y target
    X = df_heart.drop(['target'], axis=1)
    y = df_heart['target']

    # dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # definimos y entrenamos el clasificador KNN
    knn_classifier = KNeighborsClassifier().fit(X_train, y_train)

    # generamos las predicciones
    knn_pred = knn_classifier.predict(X_test)

    # evaluar modelo
    print('='*64)
    print('Accuracy KNN: ',accuracy_score(knn_pred, y_test))