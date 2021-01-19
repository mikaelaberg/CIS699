''' Program to shortest path from a given source vertex s to 
	a given destination vertex t. Expected time complexity 
	is O(V+E)'''
from collections import defaultdict 
import random
import turtle
#This class represents a directed graph using adjacency list representation 
class Graph: 

	def __init__(self,vertices): 
		self.V = vertices #No. of vertices 
		self.V_org = vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 
		self.pathList = []                                                                 #NEW

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
			self.pathList.append(j)                                                         #NEW
			return 0 # when parent[-1] then path length = 0   
		
		l = self.printPath(parent , parent[j]) 
		
		#incerement path length 
		Path_len = l + Path_len 

		# print node only if its less than original node length. 
		# i.e do not print any new node that has been added later 
		if j < self.V_org : 
			print (j)
			self.pathList.append(j)                                                         #NEW

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
g = Graph(16)

g.addEdge(0, 1, (random.randint(1,10)))
g.addEdge(1, 2, (random.randint(1,10)))
g.addEdge(0, 4, (random.randint(1,10)))
g.addEdge(1, 5, (random.randint(1,10)))
g.addEdge(2, 3, (random.randint(1,10)))
g.addEdge(2, 6, (random.randint(1,10)))
g.addEdge(3, 7, (random.randint(1,10)))
g.addEdge(4, 5, (random.randint(1,10)))
g.addEdge(4, 8, (random.randint(1,10)))
g.addEdge(5, 6, (random.randint(1,10)))
g.addEdge(5, 9, (random.randint(1,10)))
g.addEdge(6, 7, (random.randint(1,10)))
g.addEdge(6, 10, (random.randint(1,10)))
g.addEdge(7, 11, (random.randint(1,10)))
g.addEdge(8, 9, (random.randint(1,10)))
g.addEdge(8, 12, (random.randint(1,10)))
g.addEdge(9, 10, (random.randint(1,10)))
g.addEdge(9, 13, (random.randint(1,10)))
g.addEdge(10, 11, (random.randint(1,10)))
g.addEdge(10, 14, (random.randint(1,10)))
g.addEdge(11, 15, (random.randint(1,10)))
g.addEdge(12, 13, (random.randint(1,10)))
g.addEdge(13, 14, (random.randint(1,10)))
g.addEdge(14, 15, (random.randint(1,10))) #24

src = 0; dest = 15
print ("Shortest Path between %d and %d is " %(src, dest))
l = g.findShortestPath(src, dest)
print ("\nShortest Distance between %d and %d is %d " %(src, dest, l))

## Graphing

t = turtle.Turtle()

dot_distance = 100
width = 4
height = 4

t.penup()

for y in range(height):
	for i in range(width):
		t.dot()
		t.forward(dot_distance)
	t.backward(dot_distance * width)
	t.right(90)
	t.forward(dot_distance)
	t.left(90)

t.color('black')
style = ('Courier', 11, 'italic')
t.home()
t.write('0', font=style)

t.home()
t.pendown()

print(g.pathList)                                                               #NEW
place = g.pathList
list1 = iter(place)
next(list1)

nextup = next(list1, 1)
if nextup == 1:
	t.forward(100)
	nextup = next(list1)
	if nextup == 2:
		t.forward(100)
		nextup = next(list1)
		if nextup == 3:
			t.forward(100)
			nextup = next(list1)
			if nextup == 7:
				t.right(90)
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.forward(100)
					t.forward(100)
		elif nextup == 6:
			t.right(90)
			t.forward(100)
			nextup = next(list1)
			if nextup == 7:
				t.left(90)
				t.forward(100)
				t.right(90)
				t.forward(200)
			elif nextup == 10:
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.left(90)
					t.forward(100)
					t.right(90)
					t.forward(100)
				elif nextup == 14:
					t.forward(100)
					t.left(90)
					t.forward(100)
	elif nextup == 5:
		t.right(90)
		t.forward(100)
		nextup = next(list1)
		if nextup == 6:
			t.left(90)
			t.forward(100)
			nextup = next(list1)
			if nextup == 7:
				t.forward(100)
				t.right(90)
				t.forward(200)
			elif nextup == 10:
				t.right(90)
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.left(90)
					t.forward(100)
					t.right(90)
					t.forward(100)
				elif nextup == 14:
					t.forward(100)
					t.left(90)
					t.forward(100)
		elif nextup == 9:
			t.forward(100)
			nextup = next(list1)
			if nextup == 10:
				t.left(90)
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.forward(100)
					t.right(90)
					t.forward(100)
				elif nextup == 14:
					t.right(90)
					t.forward(100)
					t.left(90)
					t.forward(100)
			elif nextup == 13:
				t.forward(100)
				t.left(90)
				t.forward(200)
elif nextup == 4:
	t.right(90)
	t.forward(100)
	nextup = next(list1)
	if nextup == 5:
		t.left(90)
		t.forward(100)
		nextup = next(list1)
		if nextup == 6:
			t.forward(100)
			nextup = next(list1)
			if nextup == 7:
				t.forward(100)
				t.right(90)
				t.forward(200)
			elif nextup == 10:
				t.right(90)
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.left(90)
					t.forward(100)
					t.right(90)
					t.forward(100)
				elif nextup == 14:
					t.forward(100)
					t.left(90)
					t.forward(100)
		elif nextup == 9:
			t.right(90)
			t.forward(100)
			nextup = next(list1)
			if nextup == 10:
				t.left(90)
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.forward(100)
					t.right(90)
					t.forward(100)
				elif nextup == 14:
					t.right(90)
					t.forward(100)
					t.left(90)
					t.forward(100)
			elif nextup == 13:
				t.forward(100)
				t.left(90)
				t.forward(200)
	elif nextup == 8:
		t.forward(100)
		nextup = next(list1)
		if nextup == 9:
			t.left(90)
			t.forward(100)
			nextup = next(list1)
			if nextup == 10:
				t.forward(100)
				nextup = next(list1)
				if nextup == 11:
					t.forward(100)
					t.right(90)
					t.forward(100)
				elif nextup == 14:
					t.right(90)
					t.forward(100)
					t.left(90)
					t.forward(100)
			elif nextup == 13:
				t.right(90)
				t.forward(100)
				t.left(90)
				t.forward(200)
		elif nextup == 12:
			t.forward(100)
			t.left(90)
			t.forward(300)
turtle.done()



