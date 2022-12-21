import numpy as np  
import numpy.matlib  
import math

def run(x, y):
    xt = np.matrix.getT((np.matrix(x)))
    n = np.matrix.getI((xt*np.matrix(x)))
    return n*(xt*np.matrix(y))

x = np.matrix('-2 1; 0 1; 1 1')
y = np.matrix('0.1; 0.7; 0.9')

print(run(x, y))