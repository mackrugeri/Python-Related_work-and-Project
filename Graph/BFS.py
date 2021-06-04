import sys

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self, s):
        path = []
        visited = []
        i = 0
        while i < len(self.graph):
            visited.append(False)
            i = i + 1
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            path.append(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return path
    def printPath(self,s,v):
        for i in v:
            print(i," -> ",end = "")
            
        