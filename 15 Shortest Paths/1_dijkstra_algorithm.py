# Single Source Shortest Path (SSSP) : Dijkstra's Algorithm
from collections import defaultdict
import sys

class Dijkstra:
    def __init__(self, n):
        self.n = n
        self.g = defaultdict(list)

    def add_edge(self, u, v, w):
        self.g[u].append((v, w))

    def min_heapify(self, arr, n, i):
        smallest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[left][1] < arr[smallest][1]:
            smallest = left
        if right < n and arr[right][1] < arr[smallest][1]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.min_heapify(arr, n, smallest)

    def build_min_heap(self, arr, n):
        for i in range(n//2, -1, -1):
            self.min_heapify(arr, n, i)

    def extract_min(self, arr):
        val = arr[0][0]
        arr[0], arr[self.n - 1] = arr[self.n - 1], arr[0]
        self.n -= 1
        self.min_heapify(arr, self.n, 0)
        return val

    def decrease_key(self, arr, x, k):
        i = 0
        for j in range(self.n):
            if arr[j][0] == x:
                i = j
                break
        arr[i][1] = k
        parent = i
        while parent >= 0:
            if i % 2 == 0:
                parent = i//2 - 1
            else:
                parent = (i + 1)//2 - 1
            if arr[i][1] < arr[parent][1]:
                arr[i], arr[parent] = arr[parent], arr[i]
                i = parent
            else:
                break

    def initialize_single_source(self, g, s):
        self.d = [sys.maxsize]*self.n
        self.pred = [-1]*self.n
        self.d[s] = 0

    def relax(self, u, v, w, pq):
        if self.d[v] > self.d[u] + w:
            self.d[v] = self.d[u] + w
            self.pred[v] = u
            self.decrease_key(pq, v, self.d[u] + w)

    def dijkstra(self, s):
        self.initialize_single_source(self.g, s)
        pq = []
        for i, v in enumerate(self.d):
            pq.append([i, v])
        self.build_min_heap(pq, self.n)
        covered = []
        while self.n > 0:
            u = self.extract_min(pq)
            covered.append(u)
            for v, w in self.g[u]:
                self.relax(u, v, w, pq)
        print(covered)

g = Dijkstra(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 1, 3)
g.add_edge(3, 2, 9)
g.add_edge(3, 4, 2)
g.add_edge(4, 0, 7)
g.add_edge(4, 2, 6)
g.dijkstra(0)
print(g.d)
print(g.pred)
