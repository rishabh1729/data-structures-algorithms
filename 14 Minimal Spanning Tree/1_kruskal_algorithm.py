# Minimal Spanning Tree : Kruskal's Algorithm
class Kruskal:
    def __init__(self, n):
        self.n = n
        self.graph = []
        self.parent = [i for i in range(n)]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def kruskal_algorithm(self):
        mst = []
        self.graph = sorted(self.graph, key = lambda x:x[2])
        for edge in self.graph:
            x = self.find(edge[0])
            y = self.find(edge[1])
            if x != y:
                mst.append(edge)
                self.parent[y] = x
        return mst

g= Kruskal(6)
g.add_edge(0,1,4)
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(2,3,3)
g.add_edge(2,4,4)
g.add_edge(2,5,2)
g.add_edge(3,4,3)
g.add_edge(4,5,3)
result = g.kruskal_algorithm()
print(result)
