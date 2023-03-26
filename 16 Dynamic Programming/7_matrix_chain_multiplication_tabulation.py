# Matrix Chain Multiplication : A1.........An
# Bottom-up dynamic programming (Tabulation)

# Ai.......Ak........Aj ------> (Ai.......Ak)(Ak+1.......Aj)
# p = [p0, p1, p2, p3,........, pn]
# (Ai.......Ak) : size = pi-1 * pk
# (Ak+1.......Aj) : size = pk * pj
# l : length of chain. l varies from 2 to n
# l = 2 means A1*A2, A2*A3 etc.
# l = n means A1.........An

import sys

def matrix_chain_mul_order(p):
    n = len(p) - 1
    m = [[-1 for j in range(n)] for i in range(n)]
    s = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        m[i][i] = 0
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k+1
    return m, s

p = [10, 30, 5, 60]
m, s = matrix_chain_mul_order(p)
print(m)
print(s)
