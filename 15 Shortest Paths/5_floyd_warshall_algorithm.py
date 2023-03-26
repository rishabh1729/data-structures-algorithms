# All Pair Shortest Path (APSP) : Floyd-Warshall Algorithm
import sys

class FloydWarshall:

    def __init__(self, n):
        inf = sys.maxsize
        self.n = n
        self.W = [[inf for i in range(n)] for j in range(n)]
        self.Pi = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            self.W[i][i] = 0

    def add_edge(self, u, v, w):
        self.W[u][v] = w
        self.Pi[u][v] = u

    def floyd_warshall(self):
        D0 = [[self.W[i][j] for j in range(self.n)] for i in range(self.n)]
        Pi0 = [[self.Pi[i][j] for j in range(self.n)] for i in range(self.n)]
        for k in range(self.n):
            D1 = [[sys.maxsize for j in range(self.n)] for i in range(self.n)]
            Pi1 = [[None for j in range(self.n)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    D1[i][j] = min(D0[i][j], D0[i][k] + D0[k][j])
                    if D0[i][j] > D0[i][k] + D0[k][j]:
                        Pi1[i][j] = Pi0[k][j]
                    else:
                        Pi1[i][j] = Pi0[i][j]
            D0 = D1
            Pi0 = Pi1
        return D1, Pi1

g = FloydWarshall(5)
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
D, Pi = g.floyd_warshall()
print(D)
print(Pi)
