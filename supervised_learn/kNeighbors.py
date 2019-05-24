from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import cross_val_score, ShuffleSplit
from sklearn import datasets


def kNeighbors(dataset):

    clf = KNeighborsClassifier()
    cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=1)

    score = cross_val_score(clf, dataset.data, dataset.target, cv=cv)
    return score
