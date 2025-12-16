## SSSP --> Shortest distance between the source vertex and the destination
## Implemented using 3 ways:
# # 1. BFS 

class Graph:
    def __init__(self,gDict= None):
        if not gDict:
            gDict = {}
        self.gDict = gDict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent_vertex in self.gDict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent_vertex)
                queue.append(new_path)