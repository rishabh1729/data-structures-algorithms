from collections import defaultdict

class DFS:
    def __init__(self, n):
        self.color = ['white']*n
        self.pred = [-1]*n
        self.d = [0]*n                   # detection / discovery timestamp
        self.f = [0]*n                   # finishing timestamp
        self.time = 0
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self):
        for u in self.graph:
            if self.color[u] == 'white':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        self.color[u] = 'gray'
        self.d[u] = self.time
        print(u)
        for v in self.graph[u]:
            if self.color[v] == 'white':
                self.pred[v] = u
                self.dfs_visit(v)
        self.color[u] = 'black'
        self.time += 1
        self.f[u] = self.time

g = DFS(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(4,3)
g.add_edge(4,5)
g.add_edge(5,5)
g.dfs()
print(g.d)
print(g.f)
print(g.color)
