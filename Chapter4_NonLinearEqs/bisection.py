#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#created by Norhasliza Yusof for SIF2007/SMES2105 Numerical and Computational Methods class
#created on Wed, 28 November 2018; 12.17 pm

import numpy as np
import math as mt
import matplotlib.pyplot as mpl

#function f(x) = 3.0 - 2.0^x
def f(x):
    return 3.0-2.0**x

#this range is used for plotting
x = np.arange(0,3,0.2)

#error bound
tol = 0.01

#[a,b] is the range for the function
a = 0.0
b = 2.0

#calculate mid-point
c = a+0.5*(b-a)

#find the difference
delx = abs(b-a)

#start bisection calculation

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

#plotting format

#to create title
mpl.title('Solution for bisection method:  $f(x)=3.0-2^x$')

#mark the root
mpl.text(0.69438,0.00125, 'root')

#plot the convergenced function
mpl.plot(a,f(a),'o')

#label x-axis
mpl.xlabel('x')
#label y-axis
mpl.ylabel('f(x)')

#plot the exact function
mpl.plot(x,f(x),'b-')

mpl.show()

            
