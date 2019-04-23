#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#created by Norhasliza Yusof for SIF2007/SMES2105 Numerical and Computational Methods class
#created on Wed, 28 November 2018; 12.17 pm

import numpy as np
import math as mt
import matplotlib.pyplot as mpl


def f(x):
    return 3.0-2.0**x
x = np.arange(0,3,0.2)
tol = 0.01

a = 0.0
b = 2.0
c = a+0.5*(b-a)
delx = abs(b-a)


for i in range(0,10):
  c = a+0.5*(b-a)
  if f(c)*f(a)<0:
    a = a
    b = c
    delx = abs(b-a)
  else:
       a = c
  if delx > tol:
   print("{:f} {:f} {:f} {:f} {:f} ".format(a,f(a),b,f(b),delx))
mpl.title('Solution for bisection method:  $f(x)=3.0-2^x$')
mpl.text(0.69438,0.00125, 'root')
mpl.plot(a,f(a),'o')






mpl.xlabel('x')
mpl.ylabel('f(x)')
mpl.plot(x,f(x),'b-')

mpl.show()

            
