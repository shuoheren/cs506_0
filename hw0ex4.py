import math
from hw0ex1 import *
from hw0ex2 import *
from hw0ex3 import *
import numpy as np
import random
import math

def replace(l):
    new_list = []
    for element in l:
        if element == "female":
            new_list.append(int(0))
        elif element == "male":
            new_list.append(int(1))
        elif element == 'C':
            new_list.append(int(0))
        elif element == 'Q':
            new_list.append(int(1))
        elif element == 'S':
            new_list.append(int(2))
        elif element == "":
                element = float('NaN')
        else:
            new_list.append(float(element))
    return new_list


def import_data2(file):
    file = open(file, 'r')
    X = []
    y = []
    data = file.readlines()
    for line in data[1:]:
        z = []
        aaa = line.find('"') 
        bbb = line.rfind('"')
        r1 = line[0:aaa].strip(',').split(',')
        r2 = line[bbb+1:].strip(',').split(',')
        z.append(r1[0])
        z.append(r1[2])
        z.append(r2[0])
        z.append(r2[1])
        z.append(r2[2])
        z.append(r2[3])
        z.append(r2[5])
        z.append(r2[7].strip('\n'))
        y.append(r1[1])
        X.append(z)
        new_X = []
    for l in X:
        new_X.append(replace(l)) 
    return new_X , y
\
X, y = import_data2("train.csv")
# used to test functionsq
print(X[0]) 