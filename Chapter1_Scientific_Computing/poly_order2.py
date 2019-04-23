#Exercise to test polynomial order 2 for f(x)=sqrt(x+1)

import numpy as np
import math as mt
import matplotlib.pyplot as mpl

#insert equations

def f(x):
   return np.sqrt(x+1)


x0 = 0.0
n =  3

#calculate polynomial
for x in np.arange (0.0,1.0,0.1):
    p = 1.0+0.5*x-(1.0/8.0)*x**2
    print (x,p)
    mpl.plot(x,p,'ko')

#error
r2 = (1.0/16.0)*abs(1.0)**3*(1)**(-5/2)
print('error=',r2)

#test with the exact values
x = np.arange(0.0,1.0,0.1)
mpl.title('f(x)=$\sqrt{(x+1)}$')
mpl.xlabel('x-axis')
mpl.ylabel('y-axis')
mpl.plot(x,f(x),'r-')

mpl.show()


