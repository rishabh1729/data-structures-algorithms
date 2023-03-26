# Application of DFS : Topological Sort
from collections import defaultdict

class TopologicalSort:
    def __init__(self, n):
        self.color = ['white']*n
        self.d = [0]*n               # detection / discovery timestamp
        self.f = [0]*n               # finishing timestamp
        self.time = 0
        self.pred = [-1]*n
        self.graph = defaultdict(list)
        self.n = n
        self.ll = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        for u in range(self.n):
            if self.color[u] == 'white':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'gray'
        for v in self.graph[u]:
            if self.color[v] == 'white':
                self.pred[v] = u
                self.dfs_visit(v)
        self.color[u] = 'black'
        self.time += 1
        self.f[u] = self.time
        self.ll.append(u)

    def topological_sort(self):
        self.dfs()
        print(self.ll[-1::-1])

g = TopologicalSort(9)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(0,3)
g.add_edge(3,2)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(6,7)
g.add_edge(5,7)
g.add_edge(8,7)
g.dfs()
g.topological_sort()
