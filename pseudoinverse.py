import numpy as np  
import numpy.matlib  
import math

def run(x, y):
    xt = np.matrix.getT((np.matrix(x)))
    n = np.matrix.getI((xt*np.matrix(x)))
    return n*(xt*np.matrix(y))


def convert_for_log(y):
    return -math.log(1 / y - 1)

x = np.matrix('-2 1; 0 1; 1 1')

#print(convert_for_log(0.9))
y = np.matrix('-2.1972245773362196; 0.8472978603872036; 2.197224577336219')

print(run(x, y))