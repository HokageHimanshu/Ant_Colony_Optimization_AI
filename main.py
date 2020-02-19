# Himanshu Singh, 2017291

import numpy as np
import networkx as nx
import string
import data
from aco import ACOsolver
import matplotlib.pyplot as plt
import plot
 # α, or the pheromone’s attractiveness to the ant, and 
 # β, or the exploration capability of the ant


# Initialize the parameters and data
n = 5  # no of cities
minValueofDis = 1
maxValueofDis = 10
alpha=0.7
beta= 0.7
rho=0
noofiterations =5
noofAnts=n
dij = data.returnDistance(n,minValueofDis,maxValueofDis)
# dij = np.array([[0,3,6,2,3],[3,0,5,2,3],[6,5,0,6,4],[2,2,6,0,6],[3,3,4,6,0]]) 
nij = data.returnNij(dij)
pher = data.returnInitialPheromone(n)

#---------------------------------------------------------

# Implement the Algo
acoAlgo = ACOsolver(dij,nij,pher,n,noofiterations,alpha,beta,rho,noofAnts)
path,cost = acoAlgo.solve()
print('no of cities ='+str(n))
print('alpha ='+str(alpha)+", beta="+str(beta)+', rho='+str(rho))
print('no of iterations = '+str(noofiterations))
print('Distance Matrix = ')
print(dij)
print('Final Path Choosen (one of the possiblity) is '+ str(path))
print('Final cost is '+str(cost))
#----------------------------------------------------------

# plotting
pos=None
pos = plot.plotDisGraph(dij,pos,1)
pos = plot.plotGraph(acoAlgo.pher,pos,1)
pos = plot.plotPath(path,cost,pos,1)
#----------------------------------------------------------



# for comparison --------------------------------------------

# alpha=1
# beta= 0
# rho=0.5
# acoAlgo = ACOsolver(dij,nij,pher,n,noofiterations,alpha,beta,rho,noofAnts)
# path,cost = acoAlgo.solve()
# print('Final Path Choosen (one of the possiblity) is '+ str(path))
# print('Final cost is '+str(cost))
# #----------------------------------------------------------

# # plotting
# # pos=None
# pos = plot.plotDisGraph(dij,pos,2)
# pos = plot.plotGraph(acoAlgo.pher,pos,2)
# pos = plot.plotPath(path,cost,pos,2)
# #----------------------------------------------------------


# alpha=0
# beta= 1
# rho=0.5
# acoAlgo = ACOsolver(dij,nij,pher,n,noofiterations,alpha,beta,rho,noofAnts)
# path,cost = acoAlgo.solve()
# print('Final Path Choosen (one of the possiblity) is '+ str(path))
# print('Final cost is '+str(cost))
# #----------------------------------------------------------

# # plotting
# # pos=None
# pos = plot.plotDisGraph(dij,pos,3)
# pos = plot.plotGraph(acoAlgo.pher,pos,3)
# pos = plot.plotPath(path,cost,pos,3)
# #----------------------------------------------------------