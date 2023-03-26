# Single Source Shortest Path (SSSP) : Bellman-Ford Algorithm
from collections import defaultdict
import sys

class BellmanFord:

    def __init__(self, n):
        self.g = defaultdict(list)
        self.n = n

    def add_edge(self, u, v, w):
        self.g[u].append((v, w))

    def initialize_single_source(self, s):
        self.d = [sys.maxsize]*self.n
        self.pred = [-1]*self.n
        self.d[s] = 0

    def relax(self, u, v, w):
        if self.d[v] > self.d[u] + w:
            self.d[v] = self.d[u] + w
            self.pred[v] = u

    def bellman_ford(self, s):
        self.initialize_single_source(s)
        for i in range(self.n - 1):
            for u in self.g:
                for v, w in self.g[u]:
                    self.relax(u, v, w)
        for u in self.g:
            for v, w in self.g[u]:
                if self.d[v] > self.d[u] + w:
                    return False
        return True

g = BellmanFord(5)
g.add_edge(0, 1, 6)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, -4)
g.add_edge(2, 1, -2)
g.add_edge(3, 2, -3)
g.add_edge(3, 4, 9)
g.add_edge(4, 0, 2)
g.add_edge(4, 2, 7)
if g.bellman_ford(0):
    print(g.d)
    print(g.pred)
else:
    print('SSSP cannot contain negative cycles')
