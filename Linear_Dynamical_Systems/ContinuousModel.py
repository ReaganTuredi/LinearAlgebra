%matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
sym.init_printing()

# Using the SIR Model with the following parameters: 
#   5% of the susceptible individuals will get infected
#   3% of infected inviduals will die
#   10% of infected inviduals will recover and immuned to the disease
#   4% of infected inviduals will recover but not immuned to the disease
#   83% of the infected inviduals will remain

A = np.matrix([[0.95, 0.04, 0, 0],[0.05, 0.83, 0, 0],[0, 0.1, 1, 0],[0,0.03,0,1]])
sym.Matrix(A)

#Iterating through 50 days 
x0 = np.matrix([[1],[0],[0],[0]])
x  = x0
for i in range(50):
    x = A*x
print(x)

#200 iterations
x0=np.matrix([[1],[0],[0],[0]])
n=200
x=x0
x_all=np.matrix(np.zeros((4,n)))
for i in range(n):
    x=A*x
    x_all[:,i]=x[:,0]
for i in range(4):
    plt.plot(x_all[i].T)
    
    
#Continuous Model 
#   $$\dot{x}_1 = {dx_1(t)\over dt} = -0.05x_1(t)+ 0.04 x_2(t)$$
#   $$\dot{x}_2 = {dx_2(t)\over dt} = 0.05x_1(t)-0.17 x_2(t) \\ 
#   \dot{x}_3 = {dx_3(t)\over dt}= 0.1 x_2(t) \\
#   \dot{x}_4 = {dx_4(t)\over dt} = 0.03 x_2(t)$$


B=np.matrix([[-0.05,0.04,0,0],[0.05,-0.17,0,0],[0,0.1,0,0],[0,0.03,0,0]])
B


D2, C2 = np.linalg.eig(B)
np.allclose(C2*np.diag(D2)*C2**(-1), B)
C = C2
print(D2)
print(C2)

x0 = np.matrix([[1],[0],[0],[0]])
n = 200
x_all = np.matrix(np.zeros((4,n)))

y0=C**(-1)*x0
DD=np.diag(np.exp(D2))
for i in range(n):
    y=np.matrix(DD)**i*y0
    x=C*y
    x_all[:,i]=x[:,0]
for i in range(4):
    plt.plot(x_all[i].T)
