# All Pair Shortest Path (APSP): Matrix Operations
import sys

class MatrixOperations:

    def __init__(self, n):
        inf = sys.maxsize
        self.n = n
        self.W = [[inf for i in range(n)] for j in range(n)]
        for i in range(n):
            self.W[i][i] = 0

    def add_edge(self, u, v, w):
        self.W[u][v] = w

    def extend_shortest_path(self, L, W):
        inf = sys.maxsize
        L_ = [[inf for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    L_[i][j] = min(L_[i][j], L[i][k] + W[k][j])
        return L_

    def slow_apsp(self):
        L1 = [[self.W[i][j] for j in range(self.n)] for i in range(self.n)]
        for m in range(2, self.n):
            L2 = self.extend_shortest_path(L1, self.W)
            L1 = L2
        return L2

    def fast_apsp(self):
        L1 = [[self.W[i][j] for j in range(self.n)] for i in range(self.n)]
        for m in range(2, self.n):
            L2 = self.extend_shortest_path(L1, L1)
            L1 = L2
        return L2

g = MatrixOperations(5)
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 8)
g.add_edge(0, 4, -4)
g.add_edge(1, 3, 1)
g.add_edge(1, 4, 7)
g.add_edge(2, 1, 4)
g.add_edge(3, 0, 2)
g.add_edge(3, 2, -5)
g.add_edge(4, 3, 6)
print(g.W)
print('****')
print(g.slow_apsp())
print('****')
print(g.fast_apsp())
