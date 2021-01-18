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


print(g.findShortestPath(src, dest))

print(type(g.findShortestPath(src, dest)))
test = []
for i in l:
    test.append(i)

print (test)


"""
Psudocode:

for i in range(len(l)):
	for start @ 0:
		if next == 1:
			move arrow 100 px in the +x
		else next == 4:
			move arrow 100 px in the -y
	for new start @ 1:
		if next == 2:
			move arrow 100 px in the +x
		else next == 5:
			move arrow 100 px in the -y
	for new start @ 3:
		next == 7:
			move arrow 100 px in the -y
	for new start @ 4:
		if next == 5:
			move arrow 100 px in the +x
		else next == 8:
			move arrow 100 px in the -y
	for new start @ 5:
		if next == 6:
			move arrow 100 px in the +x
		else next == 9:
			move arrow 100 px in the -y
	for new start @ 6:
		if next == 7:
			move arrow 100 px in the +x
		else next == 10:
			move arrow 100 px in the -y
	for new start @ 7:
		next == 11:
			move arrow 100 px in the -y
	for new start @ 8:
		if next == 9:
			move arrow 100 px in the +x
		else next == 12:
			move arrow 100 px in the -y
	for new start @ 9:
		if next == 10:
			move arrow 100 px in the +x
		else next == 13:
			move arrow 100 px in the -y
	for new start @ 10:
		if next == 11:
			move arrow 100 px in the +x
		else next == 14:
			move arrow 100 px in the -y
	for new start @ 11:
		next == 15:
			move arrow 100 px in the -y ---- end
	for new start @ 12:
		next == 13:
			move arrow 100 px in the +x
	for new start @ 13:
		next == 14:
			move arrow 100 px in the +x
	for new start @ 14:
		next == 15:
			move arrow 100 px in the +x ----- end

"""


## Graphing

# t = turtle.Turtle()

# dot_distance = 100
# width = 4
# height = 4

# t.penup()

# for y in range(height):
#     for i in range(width):
#         t.dot()
#         t.forward(dot_distance)
#     t.backward(dot_distance * width)
#     t.right(90)
#     t.forward(dot_distance)
#     t.left(90)

# turtle.color('black')
# style = ('Courier', 11, 'italic')
# turtle.write('0', font=style)
# turtle.hideturtle()

# t.penup()


# # how to make a circle in turtle
# # import turtle
# # count = 0
# # while(count < 360):
# # turtle.forward(2)
# # turtle.left(1)
# # count = count + 1
# # print("Finished!")

# turtle.done()


