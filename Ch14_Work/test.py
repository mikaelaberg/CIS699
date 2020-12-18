# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict
import sys # Library for INT_MAX
# Class to represent a graph


class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = [] # default dictionary
		# to store graph

	# function to add an edge to graph
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	# A utility function to find set of an element i
	# (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# A function that does union of two sets of x and y
	# (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# If ranks are same, then make one as root
		# and increment its rank by one
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's
		# algorithm
	def KruskalMST(self):

		result = [] # This will store the resultant MST
		
		# An index variable, used for sorted edges
		i = 0
		
		# An index variable, used for result[]
		e = 0

		# Step 1: Sort all the edges in 
		# non-decreasing order of their
		# weight. If we are not allowed to change the
		# given graph, we can create a copy of graph
		self.graph = sorted(self.graph, 
							key=lambda item: item[2])

		parent = []
		rank = []

		# Create V subsets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		while e < self.V - 1:

			# Step 2: Pick the smallest edge and increment
			# the index for next iteration
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			# If including this edge does't
			# cause cycle, include it in result 
			# and increment the indexof result 
			# for next edge
			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)
			# Else discard the edge

		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)

# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# Function call
g.KruskalMST()

# This code is contributed by Neelam Yadav


''' Program to shortest path from a given source vertex s to 
	a given destination vertex t. Expected time complexity 
	is O(V+E)'''
from collections import defaultdict 

#This class represents a directed graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V = vertices #No. of vertices 
		self.V_org = vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 

	# function to add an edge to graph 
	def addEdge(self,u,v,w): 
		if w == 1: 
			self.graph[u].append(v) 
		else:	 
			'''split all edges of weight 2 into two 
			edges of weight 1 each. The intermediate 
			vertex number is maximum vertex number + 1, 
			that is V.'''
			self.graph[u].append(self.V) 
			self.graph[self.V].append(v) 
			self.V = self.V + 1
	
	# To print the shortest path stored in parent[] 
	def printPath(self, parent, j): 
		Path_len = 1
		if parent[j] == -1 and j < self.V_org : #Base Case : If j is source 
			print (j) 
			return 0 # when parent[-1] then path length = 0	 
		l = self.printPath(parent , parent[j]) 

		#incerement path length 
		Path_len = l + Path_len 

		# print node only if its less than original node length. 
		# i.e do not print any new node that has been added later 
		if j < self.V_org : 
			print (j)

		return Path_len 

	''' This function mainly does BFS and prints the 
		shortest path from src to dest. It is assumed 
		that weight of every edge is 1'''
	def findShortestPath(self,src, dest): 

		# Mark all the vertices as not visited 
		# Initialize parent[] and visited[] 
		visited =[False]*(self.V) 
		parent =[-1]*(self.V) 

		# Create a queue for BFS 
		queue=[] 

		# Mark the source node as visited and enqueue it 
		queue.append(src) 
		visited[src] = True

		while queue : 
			
			# Dequeue a vertex from queue 
			s = queue.pop(0) 
			
			# if s = dest then print the path and return 
			if s == dest: 
				return self.printPath(parent, s) 
				

			# Get all adjacent vertices of the dequeued vertex s 
			# If a adjacent has not been visited, then mark it 
			# visited and enqueue it 
			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True
					parent[i] = s 


# Create a graph given in the above diagram 
g = Graph(4) 
g.addEdge(0, 1, 2) 
g.addEdge(0, 2, 2) 
g.addEdge(1, 2, 1) 
g.addEdge(1, 3, 1) 
g.addEdge(2, 0, 1) 
g.addEdge(2, 3, 2) 
g.addEdge(3, 3, 2) 

src = 0; dest = 3
print ("Shortest Path between %d and %d is " %(src, dest)), 
l = g.findShortestPath(src, dest) 
print ("\nShortest Distance between %d and %d is %d " %(src, dest, l)), 

#This code is contributed by Neelam Yadav 
