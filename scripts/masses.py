# First, lets make a system with 3 masses
import numpy as np
from scipy import linalg as la

m=1 #Mass
k=1 #Elastic Constant
n=100 #Number of masses

D = np.zeros(shape=(n,n))

D[0][0]=k/m
D[0][1]=-k/m
for i in range(1,(n-1)):
    D[i][i]=2*k/m
    D[i][i+1]=-k/m
    D[i][i-1]=-k/m
D[n-1][n-2]=-k/m
D[n-1][n-1]=k/m

eigvalues = la.eig(D)[0]
eigvectors = la.eig(D)[1]

'''
print('Frequencies: ', eigvalues)
print('Displacements: ', eigvectors)
print('Displacement of the first frequency: ', eigvectors[0])
'''