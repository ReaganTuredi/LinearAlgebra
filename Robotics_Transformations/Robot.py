%matplotlib inline
import matplotlib.pylab as plt
import numpy as np
import sympy as sym
import math
sym.init_printing()

# This code transforms a robotic arms with possible movements in all three axes.

q1,q2,d4,q4,v1,v2,a1,a2 = sym.symbols('\Theta_1, \Theta_2, d_4, \Theta_4, V_1, V_2,A_1,A_2', negative=False)

#constructing a joint transformation matrix of a robot's shoulder
J1a = sym.Matrix([[sym.cos(q1), -sym.sin(q1), 0, 0 ], 
                [sym.sin(q1), sym.cos(q1), 0, 0 ], 
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
J1b = sym.Matrix([[1,0, 0, 0 ], 
                [0, 1, 0, 0 ], 
                [0, 0, 1, v1],
                [0, 0, 0, 1]])
J1 = J1b*J1a
J1
#constructing a joint transformation matrix of a robot's elbow between two rotating arms
J2a = sym.Matrix([[sym.cos(q2), -sym.sin(q2), 0, 0 ], 
                [sym.sin(q2), sym.cos(q2), 0, 0 ], 
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
J2b = sym.Matrix([[1, 0, 0, a1 ], 
                [0, 1, 0, 0 ], 
                [0, 0, 1, v2],
                [0, 0, 0, 1]])

J2=J2b*J2a
J2

#constructing a joint transformation matrix of a robot's elbow between horizontal ends

J3 = sym.Matrix([[1, 0, 0, a2 ], 
                [0, 1, 0, 0 ], 
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
J3
#constructing a joint transformation matrix of a robot's hand
J1 = sym.Matrix([[sym.cos(q4), -sym.sin(q4), 0, 0 ], 
                [sym.sin(q4), sym.cos(q4), 0, 0 ], 
                [0, 0, 1, d4-v1-v2],
                [0, 0, 0, 1]])
J1

########

from ipywidgets import interact
from mpl_toolkits.mplot3d import Axes3D

def Robot_Simulator(theta1=0,theta2=-0,d4=0,theta4=0):

    #Convert from degrees to radians
    q1 = theta1/180 * math.pi
    q2 = theta2/180 * math.pi
    q4 = theta4/180 * math.pi

    #Define robot geomitry
    V1 = 4 
    V2 = 0
    A1 = 2 
    A2 = 2 

    #Define your transfomraiton matrices here. 
    J1 = np.matrix([[math.cos(q1), -math.sin(q1), 0, 0 ], 
                    [math.sin(q1), math.cos(q1), 0, 0 ], 
                    [0, 0, 1, V1],
                    [0, 0, 0, 1]])

    J2 = np.matrix([[math.cos(q2), -math.sin(q2), 0, A1 ], 
                    [math.sin(q2), math.cos(q2), 0, 0 ], 
                    [0, 0, 1, V2],
                    [0, 0, 0, 1]])

    J3 = np.matrix([[1, 0, 0, A2 ], 
                    [0, 1, 0, 0 ], 
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])

    J4 = np.matrix([[math.cos(q4), -math.sin(q4), 0, 0 ], 
                    [math.sin(q4), math.cos(q4), 0, 0 ], 
                    [0, 0, 1, d4-V1-V2],
                    [0, 0, 0, 1]])

    
    #Make the rigid end effector
    p = np.matrix([[-0.5,0,0, 1], [-0.5,0,0.5,1], [0.5,0,0.5, 1], [0.5,0,0,1],[0.5,0,0.5, 1], [0,0,0.5,1], [0,0,V1+V2,1]]).T
    
    #Propogate and add joint points though the simulation
    p = np.concatenate((J4*p, np.matrix([0,0,0,1]).T), axis=1 )
    p = np.concatenate((J3*p, np.matrix([0,0,0,1]).T), axis=1 )
    p = np.concatenate((J2*p, np.matrix([0,0,0,1]).T), axis=1 )
    p = np.concatenate((J1*p, np.matrix([0,0,0,1]).T), axis=1 )
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(p[0,:].tolist()[0],(p[1,:]).tolist()[0], (p[2,:]).tolist()[0], s=20, facecolors='blue', edgecolors='r')
    ax.scatter(0,0,0, s=20, facecolors='r', edgecolors='r')
    ax.plot(p[0,:].tolist()[0],(p[1,:]).tolist()[0], (p[2,:]).tolist()[0])
    ax.set_xlim([-5,5])
    ax.set_ylim([-5,5])
    ax.set_zlim([0,6])
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')    
    ax.set_zlabel('z-axis') 

    plt.show()
    
target = interact(Robot_Simulator, theta1=(-180,180), theta2=(-180,180), d4=(0,6), theta4=(-180,180));

