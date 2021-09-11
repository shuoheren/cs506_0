import numpy as np
import math
from hw0ex2 import xxxx
from hw0ex2 import yyyy
from hw0ex3 import shuffle_data
 
#5a 
def train_test_split(X, y, t_f):
    X = np.array(X)
    y = np.array(y)
    sx = np.split(X,[int(t_f * len(X))]) 
    sy = np.split(y,[int(t_f * len(y))]) 
    sx, sy = shuffle_data(sx,sy)
    x_t = sx[0]
    y_t = sy[0]
    x_train = sx[1]
    y_train = sy[1]
    
    return x_train, y_train, x_t, y_t


#5b
def train_test_CV_split(X,y, t_f, cv_f):
    X = np.array(X)
    y = np.array(y)
    s_x = np.split(X,[int(t_f * len(X))]) 
    s_y = np.split(y,[int(t_f * len(y))]) 
    s_x,s_y = shuffle_data(s_x,s_y)
    x_test = s_x[0]
    valid = np.split(s_x[1],[int(cv_f * len(s_x[1]))]) 
    x_valid = valid[1]
    x_train = valid[0]
    y_test = s_y[0] 
    valid_y = np.split(s_y[1],[int(cv_f * len(s_y[1]))])
    y_valid = valid_y[1]
    y_train = valid_y[0]
    return x_train, y_train, x_test, y_test, x_valid, y_valid


a,b,c,d= train_test_split(xxxx, yyyy, 0.2)
print(len(a))
print(len(b))
print(len(c))
print(len(d))

