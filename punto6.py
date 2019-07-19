import matplotlib.pyplot as pp
import numpy as np
import scipy  as sc
data = np.loadtxt('punto4.dat',delimiter="\t")
x=data[:,0]
y=data[:,1] 
# Ajuste a una recta (polinomio de grado 1)
p = np.polyfit(x, y, 1)
q = np.polyfit(x, y, 2)
print(p)
print(q)
y_ajuste_lineal = p[0]*x + p[1]
y_ajuste_cuad = q[0]*x*x + q[1]*x + q[2]
pp.ylabel('Temperature (C)', fontsize = 16)
pp.xlabel('time (s)', fontsize = 16)
pp.plot(x, y_ajuste_lineal, color='green', label='Lineal')
pp.plot(x, y_ajuste_cuad, '.',color='black', label='Cuadratico')
pp.scatter(x,y, color='red',label= 'dato')  
pp.legend()
pp.savefig('punto4.pdf', bbox_inches=0, dpi=600)
pp.show()   
