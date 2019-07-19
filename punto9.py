import numpy as np
import matplotlib.pyplot as pp
from scipy.misc import derivative  
import csv
def f(x):
    return x*x*x + x*x - 4*x + 4
x = np.arange(-10,10.1,0.1)
y = f(x)                    
with open('punto9.dat', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(x,y))
