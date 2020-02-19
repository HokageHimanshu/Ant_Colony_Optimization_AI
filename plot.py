import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


def plotDisGraph(a,pos1,no):
	G=nx.from_numpy_matrix(a)
	# pos=nx.spring_layout(G,scale=2)
	if pos1 == None:
		pos = nx.fruchterman_reingold_layout(G)
	else :
		pos =pos1

	weights=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0]
	weights = nx.get_edge_attributes(G,'weight')
	# print(labels)
	nx.draw_networkx_nodes(G,pos,node_size=400)
	nx.draw_networkx_edges(G,pos,edgelist=weights,width=0.4)
	nx.draw_networkx_edge_labels(G,pos,edge_labels=weights,font_size=10,font_color='r',bbox=dict(facecolor='red', alpha=0.1))
	nx.draw_networkx_labels(G,pos,font_size=15,font_family='sans-serif')
	plt.suptitle('PLOT 1')
	plt.title('Distance Graph of Cities in TSP')
	plt.savefig("DistanceGraph"+str(no)+".png") # save as png
	plt.show()
	return pos
	# fig=plt.figure()


def plotGraph(a,pos1,no):
	G = nx.from_numpy_matrix(a) 
	elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >5]
	esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=5]
	if pos1 == None:
		pos = nx.fruchterman_reingold_layout(G)
	else :
		pos =pos1
	
	labels = nx.get_edge_attributes(G,'weight')
	# print(labels)
	# nodes
	nx.draw_networkx_nodes(G,pos,node_size=600)

	# edges
	maxVal = 0
	for (u,v,d) in G.edges(data=True):
		if d['weight']>maxVal:
			maxVal=d['weight']

	
	for (u,v,d) in G.edges(data=True):
		l=[]
		widthVal=0
		l.append((u,v))
		widthVal=d['weight']/maxVal
		widthVal*=3
		# print(widthVal)
		nx.draw_networkx_edges(G,pos,edgelist=l,width=widthVal)
	
	# nx.draw_networkx_edges(G,pos,edgelist=esmall,width=6,alpha=0.5,edge_color='b',style='dashed')

	# nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=10,font_color='r')
	# labels
	nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
	plt.suptitle('PLOT 2')
	plt.title('Final Pheromone Graph of TSP')
	plt.savefig("PheromoneGraph"+str(no)+".png") # save as png
	plt.show()
	return pos

def plotPath(p,cost,pos1,no):
	n=len(p)
	a = np.zeros((n,n))
	for i in range(1,n):
		a[p[i-1]][p[i]]=1
	a[p[-1]][p[0]]=1
	G= nx.from_numpy_matrix(a) 
	if pos1 == None:
		pos = nx.fruchterman_reingold_layout(G)
	else :
		pos =pos1

	weights=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0]
	weights = nx.get_edge_attributes(G,'weight')
	# print(labels)
	nx.draw_networkx_nodes(G,pos,node_size=400)
	nx.draw_networkx_edges(G,pos,edgelist=weights,width=1,edge_color='r')
	# nx.draw_networkx_edge_labels(G,pos,edge_labels=weights,font_size=10,font_color='r',bbox=dict(facecolor='red', alpha=0.1))
	nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
	plt.suptitle('PLOT 3')
	plt.title('Final Path Choosen in TSP '+'\n'+'Total Cost = '+str(cost))
	plt.savefig("PathChosenGraph"+str(no)+".png") # save as png
	plt.show()
	return pos


