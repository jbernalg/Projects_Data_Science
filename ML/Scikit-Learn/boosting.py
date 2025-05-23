import pandas as pd

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

    # definir y entrenar modelo
    # n_estimators: cantidad de arboles a utilizar
    boots = GradientBoostingClassifier(n_estimators=50).fit(X_train, y_train)

    # obtener predicciones
    pred_boost = boots.predict(X_test)

    # mostrar evaluacion del modelo
    print('='*64)
    print('Accuracy Gradient Boosting: ',accuracy_score(pred_boost, y_test))