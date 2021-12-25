%matplotlib inline
import scipy.sparse as sparse 
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
sym.init_printing(use_unicode=True)
from matplotlib import animation, rc
from IPython.display import HTML

# Create a lower triangular matrix that eliminates all of the subdiagonal entries of the first column of A.
A = np.matrix([[2,1,1,0],[4,3,3,1],[8,7,9,5],[6,7,9,8]]) 
As = sym.Matrix(A)
As

L1 = np.matrix([[1,0,0,0],[-2,1,0,0],[-4,0,1,0],[-3,0,0,1]])
L1s=sym.Matrix(L1)
L1s

A1=L1*A
A1s=sym.Matrix(A1)
A1s

#Left multiply A by L1
A1=L1*A
A1s=sym.Matrix(A1)
A1s

# Creates a 4x4 lower triangular matrix that eliminates all subdiagonal entries of the second column of A^1
L2 = np.matrix([[1,0,0,0],[0,1,0,0],[0,-3,1,0],[0,-4,0,1]])
L2s=sym.Matrix(L2)
L2s

#Left multiply A^1 by L2
A2=L2*A1
A2s=sym.Matrix(A2)
A2s

# Creates a 4x4 lower triangular matrix that eliminates all subdiagonal entries of the second column of A^2
L3 = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,-1,1]])
L3s=sym.Matrix(L3)
L3s

#Left multiply A^2 by L3
A3=L3*A2
A3s=sym.Matrix(A3)
A3s
