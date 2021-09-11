import math
def import_data(filename):
    file = open(filename, 'r')
    X = []
    y = []
    attributes = []
    position = 0
    lines = file.readlines()
    for line in lines:
        line = line.split(',')
        for item in line:
            position +=1
            if item == "?":
                item = float('NaN')
            else:
                item  = float(item)
            if position < 280:
                attributes.append(item)
            if position == 280:
                position = 0
                y.append(item)
                X.append(attributes)
                attributes = []
            
    return X, y
