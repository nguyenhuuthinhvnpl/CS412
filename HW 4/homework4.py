#CS 412 Homework 4 Submission Stub
#Pouya  Akbarzadeh


import numpy as np

def get_splits(n, k):
    arr = np.arange(n)
    np.random.shuffle(arr)
    split = np.split(arr, k)
    fsplit = []
    for i in range (k):
        fsplit.append(split[i])
    fsplit = np.asarray(fsplit)
    return fsplit


def my_cross_val(method, X, y, k):

    return np.array([1]*k)

def my_train_test(method, X, y, pi, k):

    return np.array([1]*k)
