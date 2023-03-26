class BFS:

    def __init__(self, n):
        self.graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 5, 7], 5: [3, 4, 6, 7], 6: [5, 7], 7: [4, 5, 6]}
        self.color = ['white']*n
        self.dist = [0]*n
        self.pred = [-1]*n

    def bfs(self, source):
        queue = []
        self.color[source] = 'gray'
        self.dist[source] = 0
        self.pred[source] = -1
        queue.append(source)
        while queue:
            current = queue.pop(0)
            print(current)
            for v in self.graph[current]:
                if self.color[v] == 'white':
                    self.color[v] = 'gray'
                    self.dist[v] = self.dist[current] + 1
                    self.pred[v] = current
                    queue.append(v)
            self.color[current] = 'black'

g = BFS(8)
g.bfs(2)
