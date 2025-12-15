# Implementation of a Graph --> Nonlinear DS consists of Vertex(Nodes) and edge(connection between vertex)

class Graph:
    def __init__(self):
        self.adjancenyList = {}

    def addVertex(self,vertex):
        if vertex not in self.adjancenyList:  # to avoid duplicating the vertex
            # self.adjancenyList.keys() = vertex --> wrong since it's used only to view the keys and not to assign or store
            self.adjancenyList[vertex] = []
    
    def printGraph(self):
        for vertex in self.adjancenyList:
            print(vertex, ":", self.adjancenyList[vertex])

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjancenyList.keys() and vertex2 in self.adjancenyList.keys():
            self.adjancenyList[vertex1].append(vertex2)
            self.adjancenyList[vertex2].append(vertex1)  # because it's a edge and they both will have each other
            return "Added an edge to the vertex!!"
        return False

    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adjancenyList.keys() and vertex2 in self.adjancenyList.keys():
            self.adjancenyList[vertex1].remove(vertex2)
            self.adjancenyList[vertex2].remove(vertex1)
            return True
        return False
    
    # Important --> We need to iterate to each list of vertex to remove them from the connection
    def removeVertex(self,vertex):
        if vertex in self.adjancenyList.keys():
            for other_vertex in self.adjancenyList[vertex]:
                self.adjancenyList[other_vertex].remove(vertex)
            del self.adjancenyList[vertex]
            return True
        return False
    
    # TRAVERSAL IN GRAPHS
    
    # USING QUEUE --> TC: O(V + E), SC:O(V)
    def bfs(self,vertex):                                              
        visited_nodes = set()
        visited_nodes.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.adjancenyList[current_vertex]:
                if adjacent_vertex not in visited_nodes:
                    visited_nodes.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    # USING STACK - TC: O(V + E) , SC:O(V)
    def dfs(self,vertex):
        visited_nodes = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited_nodes:
                print(current_vertex)
                visited_nodes.add(current_vertex)
            for adjancency_vertex in self.adjancenyList[current_vertex]:
                if adjancency_vertex not in visited_nodes:
                    stack.append(adjancency_vertex)




customGraph = Graph()
customGraph.addVertex("a")
customGraph.addVertex("b")
customGraph.addVertex("c")
customGraph.printGraph()
customGraph.addEdge("a", "b")
customGraph.addEdge("a", "c")
customGraph.addEdge("b", "c")
customGraph.printGraph()
print("After remove")
customGraph.removeEdge("a","c")
customGraph.printGraph()














# class Graph:
#     def __init__(self,gdict=None):
#         if not gdict:
#             gdict = {}
#         self.gdict = gdict

#     def addEdge(self,vertex,edge):
#         self.gdict[vertex].append(edge)
    
# customDict = {
#                 "a" : ["b","d","c"],
#                 "b": ["a", "e"],
#                 "c" :["a", "d"],
#                 "d" : ["a", "c", "e"],
#                 "e" : ["b", "d"]
#             }

# graph = Graph(customDict)
# print(graph.gdict)
# graph.addEdge("e", "a")
# print(graph.gdict)