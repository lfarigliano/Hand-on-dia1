import numpy as np
import matplotlib.pyplot as pp
from scipy.misc import derivative
def f(x):
    return x*x*x + x*x - 4*x + 4
x = np.arange(-10,10.25,0.25)
yy= derivative(f, x, dx=1e-6)
y = f(x) 
y_maximo=max(y)
index_max=np.argmax(y)
x_maximo=x[index_max]
y_minimo=min(y)
index_min=np.argmin(y)
x_ext=[]
y_ext=[]
x_minimo=x[index_min]
x_ext.append(x_minimo)
x_ext.append(x_maximo)
y_ext.append(y_minimo)
y_ext.append(y_maximo)
#print (x_minimo,y_minimo,x_maximo,y_maximo)
pp.scatter(x,y, color='black',label= 'dato')
pp.scatter(x,yy, color='red',label= 'dato')
pp.scatter(x_ext,y_ext, color='green',label= 'dato')
pp.show()
