# Detect cycles in a directed graph using Depth First Search
from collections import defaultdict

class DetectCycles:

    def __init__(self, n):
        self.color = ['white']*n
        self.pred = [-1]*n
        self.d = [0]*n                  # detection / discovery timestamp
        self.f = [0]*n                  # finishing timestamp
        self.time = 0
        self.graph = defaultdict(list)
        self.count = 0                  # number of back-edges

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        for u in self.graph:
            if self.color[u] == 'white':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'gray'
        for v in self.graph[u]:
            if self.color[v] == 'gray':
                self.count += 1
            if self.color[v] == 'white':
                self.pred[v] = u
                self.dfs_visit(v)
        self.color[u] = 'black'
        self.time += 1
        self.f[u] = self.time

g = DetectCycles(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
g.dfs()
if g.count:
    print('Cycle detected in directed graph')
else:
    print('No cycle detected in directed graph')
