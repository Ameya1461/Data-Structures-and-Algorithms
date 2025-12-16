# Implementation of Topological sort (uses stack)
# Topological sort - If a vertex depends on current_vertex, then go to the vertex and then come back to the current_vertex
#                    else push the current_vertex to the stack

# Complexity --> TC: O(V + E), SC: O(V + E)
from collections import defaultdict

class Graph:
    def __init__(self,numberOfVerticies):
        self.graph = defaultdict(list)   # as a form of list --> ['A', 'B',...]
        self.numberOfVerticies = numberOfVerticies

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:   # O(E)
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)  # recusrive call
        stack.insert(0,v)   # at 0 because FILO(stack)  --> we need to print the last element from the stack first

    def topologicalSortAlgorithm(self):
        visited = []
        stack = []

        # O(V + E)
        for k in list(self.graph):   ## We r accessing only the keys from the defaultlist which is a collection of vertex
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)

graph = Graph(8)
graph.addEdge("A","C")
graph.addEdge("C","E")
graph.addEdge("E","H")
graph.addEdge("E","F")
graph.addEdge("F","G")
graph.addEdge("B","D")
graph.addEdge("B","C")
graph.addEdge("D","F")

graph.topologicalSortAlgorithm()