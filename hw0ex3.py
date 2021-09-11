import math
from hw0ex1 import import_data
from hw0ex2 import *
import numpy as np
import random
import math


def shuffle_data(X, y):
    #shuffle the data
    random_list = np.array(range(len(X)))
    np.random.shuffle(random_list)
    nX = []
    ny = []
    for i in random_list:
        nX.append(X[i])
        ny.append(y[i])
    return nX, ny

def std_row(row):
    #computes std of a entire row
    mean= sum(row)/len(row)
    std = (sum( (x-mean)**2.0 for x in row ) / float(len(row)-1) )**0.5
    return std

def compute_std(X):
    ''' computes std for each column, returns list of stds'''
    std_list = []
    X = X.transpose()
    for l in X:
        std_list.append(std_row(l))
    return std_list
        
#3c

def mean(l):
    # calculates mean
    return (sum(l)/len(l))

def remove_outlier( X, y):
    X = transpose(X)
    treshold = []
    new_X = [] * len(X)
    ol = [] * len(X)

    new_y = []
    oly = []
    for item in X:
        m1 = mean(item)
        feature_std = std_row(item)
        up = abs(m1 + (2* feature_std))
        low = abs(m1 - (2* feature_std))
        
        for value in item: 
            if abs(value) > abs(up) or abs(value) < abs(low):
                ol.append(item) 
            else:
                treshold.append(item)
        new_X.append(treshold)
        treshold = []

    for value in y:
        y_mean = mean(y)
        std_y = std_row(y)
        high = y_mean + 2 * std_y
        low = y_mean - 2* std_y
        if abs(value) > abs(high) or abs(value) < abs(low):
            oly.append(value) # removing individual elements 
        else:
            new_y.append(value)
    
    return (transpose(new_X) ,new_y)

#3d
#transpose
# helper function that takes value - mean // std of list  (x to x prime)
# apply to X

def standard(l):
    ''' standardizes row'''
    m = sum(l)/len(l)
    std = std_row(l)
    s_list = [] * len(l)
    for value in l:
        #how to tackle divide by 0 errors
        if value == float(0):
            s_list.append(value)
        else:
            s_list.append((value - m) // std)
    return s_list 



def standardize_data(X):
    # takes nested list X and converts values in sub lists to standardized values
    X = transpose(X)
    new_X = [] * len(X)
    #first Loop
    for l in X:
        new_X.append(standard(l))
    return transpose(new_X)

# Time complexity should be O(nm) where n is the number of data points and m is the number of features in each data point. 
# Space complexity should also be O(nm).



X, y = import_data('arrhythmia.data')

remove_outlier( X, y)
print (len(X))