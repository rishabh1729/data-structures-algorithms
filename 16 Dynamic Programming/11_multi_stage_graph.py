# Shortest path from source to destination in multi-stage graph
# Forward Method (Dynamic Programming)
# G.V = [0, 1,......, n-1]
# Source = 0, Destination = N-1

import sys

def shortest_path(G):
    n = len(G)
    dist = [0]*n                  # dist[i] gives the distance from i to destination
    next = [-1]*n                 # next[i] gives the next vertex after i which leads to shortest path
    dist[n-1] = 0
    next[n-1] = -1
    inf = sys.maxsize
    for i in range(n-2, -1, -1):
        dist[i] = inf
        for j in range(n):
            if G[i][j] == inf:
                continue
            cost = G[i][j] + dist[j]
            if cost < dist[i]:
                dist[i] = cost
                next[i] = j
    print('Shortest Path Length: ', dist[0])
    print('Shortest Path:')
    i = 0
    while i != n-1:
        print(i, '--->', end = ' ')
        i = next[i]
    print(n-1)

n = 8
inf = sys.maxsize
G = [[inf for j in range(n)] for i in range(n)]
G[0][1] = 1
G[0][2] = 2
G[0][3] = 5
G[1][4] = 4
G[1][5] = 11
G[2][4] = 9
G[2][5] = 5
G[2][6] = 16
G[3][6] = 2
G[4][7] = 18
G[5][7] = 13
G[6][7] = 2
shortest_path(G)
