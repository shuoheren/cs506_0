import math
from hw0ex1 import import_data


def transpose(x):
    result = list(map(list,zip(*x)))
    return result

def median(x):
    l = len(x)
    xx = sorted(x)
    return (sum(xx[l//2-1:l//2+1])/2.0,xx[l//2])[l%2] if l else None

def remove_nan(a):
    result = [[]] * len(a)
    for i in range(len(a)):
        result[i] = [x for x in a[i] if math.isnan(x) == False]
    return result

def replace_nan(a,value):
    new_list = []
    for i in range(len(a)):
        if math.isnan(a[i]):
            new_list.append(value)
        else:
            new_list.append(a[i])

    return new_list
            

#2a
def impute_missing(X):
    xT = transpose(X)
    new_list = [[]] * len(xT)
    cleaned_trans_x = remove_nan(xT)
    q = []
    for item in cleaned_trans_x:
        q.append(median(item))
    index = 0
    for x in xT:
        new_list[index] = replace_nan(x,q[index]) 
        index += 1     
    return transpose(new_list)


#2b
# there are some extreme data that would impact the result so we prefer use the median.


#2c
def has_nan(X):
    results = []
    for element in X:
        if math.isnan(element):
            results.append(True)
        else:
            results.append(False)
    return any(results)

def discard_missing(X,y):
    x1 = []
    y1 = []
    for row in range(len(X)):
        if has_nan(X[row]) == False:
            x1.append(X[row])
            y1.append(y[row])
    return (x1, y1)


#test:
X, y = import_data('arrhythmia.data')
test = [[float('nan'),2,3,4],[1,2,3,float('nan')],[2,2,4,5],[1,2,5,6,]]
testy = [0,1,2,3]
print(impute_missing(test))


xxxx, yyyy = discard_missing(X,y) 
print(len(xxxx)) 