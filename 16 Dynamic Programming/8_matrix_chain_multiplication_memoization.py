# Matrix Chain Multiplication : A1.........An
# Top-down dynamic programming (Memoization)

# Ai.......Ak........Aj ------> (Ai.......Ak)(Ak+1.......Aj)
# p = [p0, p1, p2, p3,........, pn]
# (Ai.......Ak) : size = pi-1 * pk
# (Ak+1.......Aj) : size = pk * pj
# l : length of chain. l varies from 2 to n
# l = 2 means A1*A2, A2*A3 etc.
# l = n means A1.........An

import sys

def matrix_chain_mul_order(i, j, p):
    if i != j:
        m[i][j] = sys.maxsize
        for k in range(i, j):
            cost = matrix_chain_mul_order(i, k, p)[0] + matrix_chain_mul_order(k+1, j, p)[0] + p[i] * p[k+1] * p[j+1]
            if cost < m[i][j]:
                m[i][j] = cost
                s[i][j] = k + 1
    return m[i][j], s

if __name__ == '__main__':
    p = [10, 30, 5, 60]
    n = len(p) - 1
    m = [[-1 for j in range(n)] for i in range(n)]
    s = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        m[i][i] = 0
    cost, s = matrix_chain_mul_order(0, n-1, p)
    print(cost)
    print(s)
