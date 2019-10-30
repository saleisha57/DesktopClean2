# Use for the queue
from collections import deque


# Graph from figure 3.11a (Start at a)
graph1 = [[0,0,1,1,1,0,0,0,0,0],
		  [0,0,0,0,1,1,0,0,0,0],
		  [1,0,0,1,0,1,0,0,0,0],
		  [1,0,1,0,0,0,0,0,0,0],
		  [1,1,0,0,0,1,0,0,0,0],
		  [0,1,1,0,1,0,0,0,0,0],
		  [0,0,0,0,0,0,0,1,0,1],
		  [0,0,0,0,0,0,1,0,1,0],
		  [0,0,0,0,0,0,1,1,0,1],
		  [0,0,0,0,0,0,0,0,1,0]]
		  

# Graph from figure 3.12a (Start at a)	  
graph2 = [[0,1,0,0,1,0,0,0],
		  [1,0,1,0,0,1,0,0],
		  [0,1,0,1,0,0,1,0],
		  [0,0,1,0,0,0,0,1],
		  [1,0,0,0,0,1,0,0],
		  [0,1,0,0,1,0,1,0],
		  [0,0,1,0,0,1,0,1],
		  [0,0,0,1,0,0,1,0]]
	 

# Each vertex in the graph 3.11a
vertex1 = [False,False,False,False,False,False,False,False,False,False] # [a,b,c,d,e,f,g,h,i,j]


# Each vertex in the graph 3.12a
vertex2 = [False,False,False,False,False,False,False,False] # [a,b,c,d,e,f,g,h]
		 

# Executes the BFS algorithm (True will be the points with no edges to the starting vertex)
def BFS(v,g,number, vertex,r):
	q = deque()
	q.append(v[number])
	while len(q) != 0:
		for i in range(number,len(g)):
			if g[number][i] == 1 and vertex[i] == False:
				q.append(i)
				r.append(i)
				vertex[i] = True
		q.popleft()



# Iterates through each of the graphs
def graphTr(graph,vertex):
	results = []
	count = 0
	for x in range(0,len(graph)):
		if vertex[x] == False:
			results.append(x)
			BFS(graph[x],graph,x,vertex,results)
	return results


# Function calls for iterrating through graphs (Sending in each graph and it's corresponding visited list)
t1 = graphTr(graph1,vertex1)
t2 = graphTr(graph2,vertex2)


# Display the results
print(t1)
print(t2)




