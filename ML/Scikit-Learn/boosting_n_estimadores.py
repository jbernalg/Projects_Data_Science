import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# librerias de boosting
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Script principal
if __name__ == '__main__':

    # cargar datos
    df_heart = pd.read_csv('./data/heart_bd.csv')

    # seleccionar features y target
    X = df_heart.drop(['target'], axis=1)
    y = df_heart['target']

    # dividir datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # definir rango de estimadores a probar
    estimadores = range(10, 200, 10)

    # definir lista para almacenar accuracy de cada cantidad diferente de estimadores
    total_accuracy = []

    # iteramos sobre las diferentes cantidades de estimadores
    for i in estimadores:
        boots = GradientBoostingClassifier(n_estimators=i).fit(X_train, y_train)
        pred_boots = boots.predict(X_test)
        total_accuracy.append(accuracy_score(y_test, pred_boots))

    # visualizar los accuracy de cada cantidad de estimador
    plt.plot(estimadores, total_accuracy)
    plt.xlabel('Estimadores')
    plt.ylabel('Accuracy')
    plt.show()
    
    # encontrar el mejor accuracy
    max_accu = max(total_accuracy)

    # encontrar los índices donde se logra ese accuracy
    best_index = [i for i, v in enumerate(total_accuracy) if v == max_accu]

    # traducir esos índices a los valores de n_estimators reales
    best_estimators = [estimadores[i] for i in best_index]

    # imprimir resultados
    print(f"Mejor accuracy: {max_accu}")
    print(f"Cantidad de estimadores con el mejor accuracy: {len(best_estimators)}")
    print(f"Estimadores con mejor accuracy: {best_estimators}")
