import pandas as pd

from sklearn.cluster import MiniBatchKMeans

# Script principal
if __name__ == '__main__':

    df = pd.read_csv('./data/candy.csv')
    print(df.head())