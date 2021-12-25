%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
sym.init_printing(use_unicode=True)
import copy
import random



def makeM(A,i,j):
    # Deletes the ith row and jth column from A
    M = copy.deepcopy(A)
    del M[i]
    for k in range(len(M)):
        del M[k][j]
    return M

def mydet(A):
    #Calculate the determinant from list-of-lists matrix A
    if type(A) == np.matrix:
        A = A.tolist()   
    n = len(A)
    if n == 2:
        det = (A[0][0]*A[1][1] - A[1][0]*A[0][1]) 
        return det
    det = 0
    i = 0
    for j in range(n):
        M = makeM(A,i,j)
        
        #Calculate the determinant
        det += (A[i][j] * ((-1)**(i+j+2)) * mydet(M))
    return det
  
def makeAi(A,i,b):
    #Replace the ith column in A with b
  if type(A) == np.matrix:
      A = A.tolist()
  if type(b) == np.matrix:
      b = b.tolist()
  Ai = copy.deepcopy(A)
  for j in range(len(Ai)):
      Ai[j][i] = b[j][0]
  return Ai
  
def cramersRule(A,b)
  n = len(A)
  detA = np.linalg.det(A)
    
  x = []
    
  for i in range(n):
      Ai = makeAi(A,i,b)
      x.append([np.linalg.det(Ai)/detA])
    
  return x

