import pandas as pd
from sklearn.cluster import MeanShift

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/candy.csv')
    print(dataset.head())

    # seleccionamos los features
    X = dataset.drop('competitorname', axis=1)

    # definimos el modelo
    meanshift = MeanShift().fit(X)

    # mostrar etiquetas creadas
    print(max(meanshift.labels_))

    print('='*64)
    # mostrar centroides
    print(meanshift.cluster_centers_)

    # guardar etiquetas del modelo en el df
    dataset['meanshift'] = meanshift.labels_
    print('='*64)
    print(dataset.head())