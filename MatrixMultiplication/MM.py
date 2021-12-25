import numpy as np
import sympy as sym
import random
import time

def multiply(m1,m2):
    #first matrix is nxd in size
    #second matrix is dxm in size
    n = len(m1) 
    d = len(m2)
    m = len(m2[0])
    
    if len(m1[0]) != d:
        print("ERROR - inner dimentions not equal")
    
    result = [[0 for i in range(m)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,m):
            for k in range(0,d):
                result[i][j] = result[i][j] + m1[i][k] * m2[k][j]
    
    return result
