# Minimal Spanning Tree : Prim's Algorithm
from collections import defaultdict
class Prim:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.pred = [-1]*n
        self.key = list(zip(range(n), [9999]*n))
        self.key = [list(item) for item in self.key]
        self.d = {}

    def add_edge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

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
        val = arr[0]
        arr[0], arr[self.n - 1] = arr[self.n - 1], arr[0]
        self.n -= 1
        self.min_heapify(arr, self.n, 0)
        return val

    def decrease_key(self, arr, x, dk):
        i = 0
        for j in range(self.n):
            if arr[j][0] == x:
                i = j
                break
        arr[i][1] = dk
        self.d[x] = dk
        parent = i
        while True:
            if i % 2 == 0:
                parent = i//2 - 1
            else:
                parent = (i+1)//2 - 1
            if parent < 0:
                break
            if arr[i][1] < arr[parent][1]:
                arr[i], arr[parent] = arr[parent], arr[i]
                i = parent
            else:
                break

    def prim_algorithm(self, r):
        self.key[r][1] = 0
        self.pred[r] = -1
        pq = list(range(self.n))
        self.build_min_heap(self.key, self.n)
        for item in self.key:
            self.d[item[0]] = item[1]
        while self.n > 0:
            u, _ = self.extract_min(self.key)
            pq.remove(u)
            for v, w in self.graph[u]:
                k = self.d[v]
                if v in pq and w < k:
                    self.pred[v] = u
                    self.decrease_key(self.key, v, w)

g= Prim(6)
g.add_edge(0,1,4)
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(2,3,3)
g.add_edge(2,4,4)
g.add_edge(2,5,2)
g.add_edge(3,4,3)
g.add_edge(4,5,3)
g.prim_algorithm(4)
print(g.pred)
print(g.key)
