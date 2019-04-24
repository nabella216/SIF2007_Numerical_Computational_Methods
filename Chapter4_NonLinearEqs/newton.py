import numpy as np
import math as mt
import matplotlib.pyplot as mpl

def f(x):
    return (20*x-1)/19*x

def fp(x):
    return 1/(19*x**2)

x = 1.0
for i in range (0,10):
    xi = x - f(x)/fp(x) 
    delx = abs(xi-x)
    if delx > 1.0e-6:
        print(i,x,xi,delx)
    x = xi
#    mpl.plot(x,f(x),'bx--')



x = np.arange(-0.5,0.5,0.1)
mpl.title ('Newton Method for Non-Linear Equations')
mpl.xlabel('x-axis')
mpl.ylabel ('y-axis')
mpl.plot(x, f(x),'g-')



mpl.show()
