## Topological Sort

An algorithm that takes a directed graph and returns an array of nodes where each node appears before all the node it points to. Hence, for every directed edge u v, vertex u comes before v in the ordering. **Topological sorting order can be derived only for directed acyclic graphs**.

## Kahn's Algorithm

A directed acyclic graph (DAG) has at least one vertex with the indegree zero (no nodes connected to it) and one vertex with the out-degree zero (not connected to other nodes).

Algorithm works by keeping track of the number of incoming edges into each node (indegree). It repeatedly:

1. Finds nodes with no incoming edge i.e. zero indegree
2. Stores the nodes in a stack/queue and deletes them from the original graph
3. Deletes the edges originating from the nodes stored in step 2 by decrementing the indegree of each node connected to the removed nodes in step 2

If the result of topological sorting contains the same initial number of elements, no cycle is encountered, and the sorted order is returned. If they don't, **a cycle was encountered, and topological sorting is not possible.**

### Steps

1. Store the current indegree of each node
2. Initialize count of visited nodes to 0
3. Remove a node from the stack/queue and:

   - Increment the count of visited nodes by 1
   - Reduce the indegree by 1 for all its neighboring nodes (outward nodes)
   - If the indegree of a neighboring node is reduced to 0, add to stack/queue

4. Repeat step 3 until the queue/stack is empty
5. Check the count of visited nodes with the number of nodes in the graph

```py
from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.V = vertices # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    # The function to do Topological Sort.
    def topologicalSort(self):

        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0]*(self.V)

        # Traverse adjacency lists to fill indegrees of vertices.
        # This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
            print ("There exists a cycle in the graph")
        else :
            # Print topological order
            print (top_order)


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
```
