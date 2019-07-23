#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#created by Norhasliza Yusof for SIF2007/SMES2105 Numerical and Computational Methods class
#created on Wed, 28 November 2018; 12.17 pm

import numpy as np
import math as mt
import matplotlib.pyplot as mpl


def f(x):
    return 4.0*x-1.8*x**2+1.2*x**3-0.3*x**4
x = np.arange(0,2,0.2)
tol = 10**(-3)

xu = -2.0 
xl = 4.0
#c = a+0.5*(b-a)
#delx = abs(b-a)
x1 = xl+0.61803*(xl-xu)
x2 = xu-0.61803*(xl-xu)

for i in range(0,10):
  
  if f(x1)>f(x2):
    xl = x2
    x2 = x1
    x1 = xl+0.61803*(xu-xl)
    xu = xu
    delx= abs(xu-xl)
    if delx < tol:
       print((xu+x1)/2.0)
    print(xl,xu, f(xu),f(xl))
  else:
    xl = xl
    xu = x1
    x1=  x2
    x2 = xu-0.61803*(xu-xl)
    delx= abs(xu-xl)
    if delx < tol:
       print((xu+x1)/2.0)







            
