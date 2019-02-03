#https://www.geeksforgeeks.org/topological-sorting/
from collections import defaultdict


class Graph:
    def __init__(self, verticies=0):
        self.graph = defaultdict(list)
        self.numOfVerticies = verticies

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def __str__(self):
        op = []
        for i in self.graph.items():
            op.append(i)
        return (str(op))

    def _topoSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self._topoSortUtil(i, visited, stack)
        stack.insert(0, v)

    def topoSort(self):
        visited = [False] * self.numOfVerticies
        stack = []
        for i in range(self.numOfVerticies):
            if visited[i] is False:
                self._topoSortUtil(i, visited, stack)

        print(stack)


#
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g)
g.topoSort()
