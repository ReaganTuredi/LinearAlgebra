import math
import copy

def proj(v,u):
    c=dot(v,u)/dot(u,u)
    
    pv=[]
    
    for i in range(len(u)):
        pv.append(c*u[i])
    return pv
  
def transpose(A):
    #Calculate the transpose of matrix A represented as list of lists
    n = len(A)
    m = len(A[0])
    AT = list()
    for j in range(0,m):    
        temp = list()
        for i in range(0,n):
            temp.append(A[i][j])
        AT.append(temp)
    return AT

def sub_vectors(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]-v2[i])
    return v3

def GramSchmidt(A):
    AT=transpose(A)
    GT=AT
    for i in range(len(AT)):
        for j in range(i):
            GT[i]=sub_vectors(GT[i],proj(GT[i],GT[j]))
    G=transpose(GT)
    return G
