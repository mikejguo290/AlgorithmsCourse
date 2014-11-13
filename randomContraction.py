import random
import copy
from math import log

f = open('AdjacencyList.txt','r')

AdjacencyDicc = {}
#AdjacencyList = f.read()
f.close()

AdjacencyList=AdjacencyList.split('\n')
for line in AdjacencyList:
	line = line.split('\t')
	intList =[]
	for num in line:
		try:
			intList.append(int(num))
		except:
			pass
	AdjacencyDicc[intList[0]] = intList[1:]

 	
def randomContractionAlgorithm(dicc):
	while len(dicc.keys())>2:
		#reduce the number of vertices
		mergeVertices(dicc)
		# the number of items in each of the dicc entries both = number of cuts
	selectedCut = float("inf")
	for key,item in dicc.items():
		cut = len(item)
		if cut < selectedCut:
			selectedCut = cut
	return selectedCut #.items() # dicc containing just the final 2 vertices.
	
def mergeVertices(graph):
	# randomly select two vertices
	nodei,nodej = randomSelectOneEdge(graph)
	graph[nodei].extend(graph[nodej])
	del graph[nodej]
	updateGraph(graph,nodei,nodej)
	
	
def randomSelectOneEdge(graph):
	# one edge, represented by two vertices.
	randNodei = random.choice(graph.keys())
	randNodej = random.choice(graph[randNodei]) #crucial! i is totally random, j isn't!
	return randNodei,randNodej
	 
def updateGraph(graph,i,j):
	# update so that every vertex that referred to 3 now refers to 1. 
	# self loops must be deleted, i.e if a list index contains a ref to itself in i:list,
	for vertex in graph:
		for idx, vertexRef in enumerate(graph[vertex]):
			if vertexRef == j:
				graph[vertex][idx] = i
					
		graph[vertex] = [vertexRef for vertexRef in graph[vertex] if vertexRef != vertex]
		# iterating over a list I'm changing is not good practice.
					
def repeatSampling(graph):
	i = 0
	min = float('inf')
	while i< 60:
		copyGraph = copy.deepcopy(graph)
		result=randomContractionAlgorithm(copyGraph)
		if result < min:
			min = result
		i+=1
	return min

print repeatSampling(AdjacencyDicc)
