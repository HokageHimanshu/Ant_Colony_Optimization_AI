import numpy as np

class ACOsolver:

	def __init__(self,dij,nij,pher,n,iterations,alpha,beta,rho,noofAnts):
		self.dij = dij;
		self.nij = nij;
		self.pher=pher
		self.n =n
		self.iter=iterations
		self.alpha=alpha
		self.beta=beta
		self.rho=rho
		self.noofAnts=noofAnts

	def solve(self):
		# initializing the cities randomly to the ants
		ants=[]
		optimumCost = 10000000
		bestPath=[]
		cities = np.arange(self.n)
		np.random.shuffle(cities)
		for i in range(self.noofAnts):
			ants.append(Ant(self.dij,self.nij,self.pher,self.n,cities[i],self.alpha,self.beta))

		for i in range(self.iter):  #iterations
			for k in range(self.noofAnts):  #noofAnts
				for moves in range(self.n-1):    #noOfValidMoves or lengthOfPath
					ants[k].move()
		
				ants[k].updateCost()
				if optimumCost>ants[k].totalCost:
					optimumCost=ants[k].totalCost
					bestPath = ants[k].path
				ants[k].updatePhermone()
			self.updatePherTable(ants)
			for k in range(self.noofAnts):
				ants[k].reset(self.pher)

		return bestPath,optimumCost

	def solve2(self):
		# initializing the cities randomly to the ants
		ants=[]
		optimumCost = 10000000
		bestPath=[]
		cities = np.arange(self.n)
		for i in range(self.iter):  #iterations
			# np.random.shuffle(cities)
			for i in range(self.noofAnts):
				ants.append(Ant(self.dij,self.nij,self.pher,self.n,cities[i],self.alpha,self.beta))

			for k in range(self.noofAnts):  #noofAnts
				for moves in range(self.n-1):    #noOfValidMoves or lengthOfPath
					ants[k].move()
		
				ants[k].updateCost()
				if optimumCost>ants[k].totalCost:
					optimumCost=ants[k].totalCost
					bestPath = ants[k].path
				ants[k].updatePhermone()
			self.updatePherTable(ants)

		return bestPath,optimumCost


	
	def updatePherTable(self,ants):
		l,b = self.pher.shape
		for i in range(l):
			for j in range(b):
				newPherAmount = self.rho*self.pher[i][j]
				for k in range(len(ants)):
					newPherAmount+=ants[k].pher[i][j]
				self.pher[i][j] = newPherAmount




class Ant:

	def __init__(self,dij,nij,pher,n,start,alpha,beta):
		self.dij=dij
		self.nij=nij
		self.pher=pher
		self.n=n
		self.start=start
		self.current=start
		self.alpha=alpha
		self.beta=beta
		self.path=[] # path traveled
		self.path.append(start)
		self.totalCost=0.0
		self.availableOptions = [i for i in range(self.n)]
		self.availableOptions.remove(start)

	def move(self):
		# probabilites = np.zeros(n)
		# print('move by '+str(self.start));
		denominator=0;
		for i in range(len(self.availableOptions)):
			denominator+= (self.pher[self.current][self.availableOptions[i]]**self.alpha)*(self.nij[self.current][self.availableOptions[i]]**self.beta)

		maxProb=0
		nextCity=-1
		for i in range(len(self.availableOptions)):
			p = ((self.pher[self.current][self.availableOptions[i]]**self.alpha)*(self.nij[self.current][self.availableOptions[i]]**self.beta)) / denominator
			if p>maxProb:
				maxProb=p
				nextCity=self.availableOptions[i]
		
		if nextCity==-1:
			print('Problem in selecting the nextCity');
		else:
			self.availableOptions.remove(nextCity)
			self.path.append(nextCity)
			# self.totalCost +=self.dij[self.current][nextCity]
			self.current=nextCity



	def updateCost(self):
		self.totalCost=0
		for i in range(1,len(self.path)):
			self.totalCost +=self.dij[self.path[i-1]][self.path[i]]
		self.totalCost+=self.dij[self.path[-1]][self.path[0]]
		# print('totalCost by '+str(self.start)+" is "+str(self.totalCost))
		# print(str(self.path));

	

	def updatePhermone(self):
		self.pher=np.zeros((self.n,self.n))
		# print('updatePhermone by '+str(self.start))
		# print(self.path)
		# print(self.totalCost)
		for i in range(1,len(self.path)):
			self.pher[self.path[i-1]][self.path[i]] = 1/self.totalCost
		# print(self.totalCost)
		self.pher[self.path[-1]][self.path[0]] = 1/self.totalCost      # doubt

	

	def reset(self,pher):
		self.current=self.start
		self.pher=pher
		self.path=[] # path traveled
		self.path.append(self.start)
		self.totalCost=0.0
		self.availableOptions = [i for i in range(self.n)]
		self.availableOptions.remove(self.start)







