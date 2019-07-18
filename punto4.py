import matplotlib.pyplot as pp
import numpy as np

#f_in = open('punto4.dat', 'r')
data = np.loadtxt('punto4.dat',delimiter="\t")
x=data[:,0]
y=data[:,1]
print(x,y) 
pp.scatter(x,y,color=red) 
pp.savefig('punto4.pdf', bbox_inches=0, dpi=600)
pp.show()
