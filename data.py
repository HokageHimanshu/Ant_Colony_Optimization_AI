import numpy as np


def returnDistance(n,low,high):
	a = np.random.randint(low,high,size=(n,n))
	l,b=a.shape
	for i in range(l):
		for j in range(i+1):
			if i==j:
				a[i][j]=0
			else :
				a[i][j]=a[j][i]
	return a

def returnNij(a):
	l,b=a.shape
	nij =np.zeros((l,b))
	for i in range(l):
		for j in range(b):
			if i==j:
				a[i][j]=0
			else :
				nij[i][j]=1/a[i][j]
	return nij

def returnInitialPheromone(n):
	pher = np.ones((n,n))
	for i in range(n):
		pher[i][i]=0
	return pher

