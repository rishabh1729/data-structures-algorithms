class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, size):
        self.graph = [None]*size
        self.n = size

    def add_edge(self, s, d):
        p = Node(d)
        p.next = self.graph[s]
        self.graph[s] = p

        p = Node(s)
        p.next = self.graph[d]
        self.graph[d] = p

    def remove_edge(self, s, d):
        t1 = self.graph[s]
        t2 = None
        while t1:
            if t1.vertex == d:
                if t2 == None:
                    self.graph[s] = t1.next
                else:
                    t2.next = t1.next
            else:
                t2 = t1
            t1 = t1.next

        t1 = self.graph[d]
        t2 = None
        while t1:
            if t1.vertex == s:
                if t2 == None:
                    self.graph[d] = t1.next
                else:
                    t2.next = t1.next
            else:
                t2 = t1
            t1 = t1.next

    def print_graph(self):
        for i in range(self.n):
            t = self.graph[i]
            while t:
                print('{} ---> {}'.format(i, t.vertex))
                t = t.next

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.remove_edge(0,1)
g.print_graph()
