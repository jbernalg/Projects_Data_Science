import pandas as pd

from sklearn.cluster import MiniBatchKMeans

# Script principal
if __name__ == '__main__':

    df = pd.read_csv('./data/candy.csv')
    print(df.head())

    # guardar las variables excepto el nombre del caramelo
    X = df.drop('competitorname', axis=1)

    # definir y entrenar modelo de clusterizacion. 
    # Usamos k=4 elegido a nuestra conveniencia
    # elegimos un tamano de batch de 8
    kmeans = MiniBatchKMeans(n_clusters=4, batch_size=8).fit(X)

    # mostrar total de clusteres
    print('Total de clusteres: ', len(kmeans.cluster_centers_))
    print('='*64)
    # mostrar las etiquetas 
    print(kmeans.predict(X))

    # agregar las etiquetas dadas por el modelo al dataframe
    df['KMeans'] = kmeans.predict(X)
    print(df.head())