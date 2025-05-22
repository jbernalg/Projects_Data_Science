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