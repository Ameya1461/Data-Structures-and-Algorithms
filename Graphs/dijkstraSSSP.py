# Implementation of Dijkstra's algorithm --> Used for directed weighted graphs

import heapq
# Class of a Edge
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

# class for a Node
class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.min_distance = float("inf")

    # less than function to comapre min distance of 2 nodes of same class
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self,weight,destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbours.append(edge)

# Class Dijkstra's Algorithm
class DijkstraAlgorithm:
    def __init__(self):
        self.heap = []

    def calculate(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)

        while self.heap:
            # Pop the lowest value which is at index 0 by default bcoz of heapq property
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue

            for edge in actual_vertex.neighbours:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight

                # Here new distance < target distance --> works when target vertex is not visited (has infinite distance), hence we push in this loop, if greater means visited and is in heap
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    heapq.heappush(self.heap, target)  # Not visited as it has infite min_distance at start
                    # [F-19, F-17] --> will sort it with min first acc to heapq and make it visited so need not check F-19(ignored)
            actual_vertex.visited = True   

    def get_shortest_path(self, target):
        print(f"The shortest path to target is: {target.min_distance}")
        actual_vertex = target
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor

# Step 1 --> Creating the Nodes
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step 2 -- create edge
nodeA.add_edge(6,nodeB)
nodeA.add_edge(10,nodeC)
nodeA.add_edge(9,nodeD)

nodeB.add_edge(16,nodeE)
nodeB.add_edge(13,nodeF)
nodeB.add_edge(5,nodeD)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10,nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = DijkstraAlgorithm()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeB)