import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    # Cargar los datos
    data = pd.read_csv('./data/heart_bd.csv')

    # Preparar las variables predictoras y la variable objetivo
    X = data.drop(['target'], axis=1)
    Y = data['target']

    # Dividir en conjunto de entrenamiento y prueba
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=42)

    # Definir el rango de valores a probar para los hiperparámetros
    param_grid = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.2],
        'max_depth': [3, 5, 7]
    }

    # Crear un modelo de Gradient Boosting
    gb_model = GradientBoostingClassifier(random_state=42)

    # Crear GridSearchCV para buscar la mejor combinación de parámetros
    grid_search = GridSearchCV(estimator=gb_model, param_grid=param_grid, cv=5, scoring='accuracy')

    # Entrenar el GridSearchCV
    grid_search.fit(X_train, Y_train)

    # Imprimir todos los resultados de las combinaciones
    results = grid_search.cv_results_
    print("Resultados para cada combinación de hiperparámetros de Gradient Boosting:")
    for mean_score, params in zip(results['mean_test_score'], results['params']):
        print(f"Parámetros: {params}, Precisión promedio: {mean_score}")

    # Mejor modelo encontrado
    best_params = grid_search.best_params_
    print(f"\nMejores parámetros encontrados: {best_params}")

    # Evaluar el mejor modelo en los datos de prueba
    best_model = grid_search.best_estimator_
    Y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"\nPrecisión del mejor modelo en los datos de prueba: {accuracy}")