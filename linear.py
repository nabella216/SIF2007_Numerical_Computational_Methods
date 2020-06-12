

import numpy as np

#Input your matrix A using numpy arrays
A = np.array([[4.0,2.0,0.0],[2.0,3.0,1.0],[0.0,1.0,2.5]])

# Define matrix B using numpy arrays
b = np.array([5,0,12.0,12.0])

def gauss(A,b):
    n =  len(b) #define lenght/size of matrix
    for j in range(0,n-1):
      for i in range(j+1,n):
        lam = A[i,j]/A[j,j]
        A[i] = A[i] - lam*A[j]
        b[i] = b[i] - lam*b[j]
        x = np.zeros(n)
    for j in range (n-1,-1,-1):
     x[j]=b[j]/A[j,j]
     b = b-x[j]*A[:,j]
    return x

print(gauss(A,b))
