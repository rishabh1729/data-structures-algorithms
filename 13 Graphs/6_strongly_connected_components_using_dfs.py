# Application of DFS : Find strongly connected components in a directed graph
# Kosaraju's Algorithm

from collections import defaultdict

class StronglyConnected:
    def __init__(self,n):
        self.color = ['white']*n
        self.pred = [-1]*n
        self.d = [0]*n                     # detection / discovery timestamp
        self.f = [0]*n                     # finishing timestamp
        self.time  = 0
        self.n = n
        self.graph = defaultdict(list)
        self.scc = {}
        self.count = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertices):
        for u in vertices:
            if self.color[u] == 'white':
                self.count += 1
                self.scc[self.count] = [u]
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        self.d[u] = self.time
        self.color[u] = 'gray'
        for v in self.graph[u]:
            if self.color[v] == 'white':
                self.scc[self.count].append(v)
                self.pred[v] = u
                self.dfs_visit(v)
        self.color[u] = 'black'
        self.time += 1
        self.f[u] = self.time

g = StronglyConnected(8)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(1,5)
g.add_edge(2,3)
g.add_edge(2,6)
g.add_edge(3,2)
g.add_edge(3,7)
g.add_edge(4,0)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,5)
g.add_edge(6,7)
g.add_edge(7,7)
vertices_g = list(range(g.n))
g_transpose = StronglyConnected(8)
for u in g.graph:
    for v in g.graph[u]:
        g_transpose.add_edge(v,u)
g.dfs(vertices_g)
vertices_gt = []
ft = list(enumerate(g.f))
ft = sorted(ft, key = lambda x:x[1], reverse = True)
for t in ft:
    vertices_gt.append(t[0])
g_transpose.dfs(vertices_gt)
for sc in g_transpose.scc.values():
    print(sc)
