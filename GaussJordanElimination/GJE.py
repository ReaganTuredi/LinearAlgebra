%matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym

def basic_gauss_jordan(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(m):
            if not i == j:
                Ratio = A[j][i]/A[i][i]
                # Elementary Row Operation 3
                for k in range(n): 
                    A[j][k] = A[j][k] - Ratio * A[i][k]

        #Elementary Row Operation 2
        Const = A[i][i]
        for k in range(n):
            A[i][k] = A[i][k]/Const
    return A
    
    
