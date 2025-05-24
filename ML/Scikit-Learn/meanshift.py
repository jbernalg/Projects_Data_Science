import pandas as pd
from sklearn.cluster import MeanShift

# Script principal
if __name__ == '__main__':

    dataset = pd.read_csv('./data/candy.csv')
    print(dataset.head())