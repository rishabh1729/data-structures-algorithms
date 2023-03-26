class Graph:
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])

    def add_edge(self, s, d):
        if s == d:
            print('Both are same nodes')
            return
        self.adjMatrix[s][d] = 1
        self.adjMatrix[d][s] = 1

    def remove_edge(self, s, d):
        if self.adjMatrix[s][d] == 0:
            print('There is no edge between the two nodes')
            return
        self.adjMatrix[s][d] = 0
        self.adjMatrix[d][s] = 0

    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_matrix()
