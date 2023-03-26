# Single Source Shortest Path (SSSP) : Directed Acyclic Graphs (DAGs)
from collections import defaultdict
import sys

class DAG:

    def __init__(self, n):
        self.n = n
        self.g = defaultdict(list)
        self.time = 0
        self.d = [0]*n
        self.f = [0]*n
        self.pred = [-1]*n
        self.color = ['white']*n
        self.ll = []

    def add_edge(self, u, v, w):
        self.g[u].append((v,w))

    def dfs(self):
        for u in range(self.n):
            if self.color[u] == 'white':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'gray'
        for v, w in self.g[u]:
            if self.color[v] == 'white':
                self.pred[v] = u
                self.dfs_visit(v)
        self.color[u] = 'black'
        self.time += 1
        self.f[u] = self.time
        self.ll.append(u)

    def topological_sort(self):
        self.dfs()
        self.ll = self.ll[-1::-1]

    def initialize_single_source(self, s):
        self.dist = [sys.maxsize]*self.n
        self.pred = [-1]*self.n
        self.dist[s] = 0

    def relax(self, u, v, w):
        if self.dist[v] > self.dist[u] + w:
            self.dist[v] = self.dist[u] + w
            self.pred[v] = u

    def sssp_dag(self, s):
        self.topological_sort()
        self.initialize_single_source(s)
        for u in self.ll:
            for v, w in self.g[u]:
                self.relax(u, v, w)

g = DAG(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 7)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(3, 4, -1)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, -2)
g.sssp_dag(1)
print(g.dist)
print(g.pred)
