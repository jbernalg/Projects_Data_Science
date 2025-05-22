import pandas as pd

from sklearn.ensemble import BaggingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# estimadores a usar
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


# Script principal
if __name__ == '__main__':

    # cargar datos
    df_heart = pd.read_csv('./data/heart_bd.csv')

    # seleccionar features y target
    X = df_heart.drop(['target'], axis=1)
    y = df_heart['target']

    # dividir datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # estimador KNN
    knn_class = KNeighborsClassifier().fit(X_train, y_train)
    # predicciones KNN
    knn_pred = knn_class.predict(X_test)
    # evaluacion KNN
    print('='*64)
    print('Accuracy KNN: ', accuracy_score(knn_pred, y_test))

    # diccionario de estimadores
    classifier = {
        'KNeighbors': KNeighborsClassifier(),
        'LinearSVC': LinearSVC(),
        'SVC': SVC(),
        'SGDC': SGDClassifier(),
        'DecisionTree': DecisionTreeClassifier()
    }

    # iteramos cada clasificador sobre el ensamble
    for name, estimador in classifier.items():
        bag_class = BaggingClassifier(base_estimator=estimador, n_estimators=50).fit(X_train, y_train)
        bag_pred = bag_class.predict(X_test)
        print('='*64)
        print(f'Accuracy Bagging con {estimador}: {accuracy_score(knn_pred, y_test)}')
        