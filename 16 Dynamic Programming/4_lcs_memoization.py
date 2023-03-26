# Longest Common Subsequence
# Top-down dynamic programming (Memoization)

def lcs_memoization(s1, s2):
    m = len(s1)
    n = len(s2)
    if L[m][n] == -1:
        if m == 0 or n == 0:
            L[m][n] = 0
        elif s1[m-1] == s2[n-1]:
            L[m][n] = lcs_memoization(s1[:m-1], s2[:n-1]) + 1
        else:
            L[m][n] = max(lcs_memoization(s1, s2[:n-1]), lcs_memoization(s1[:m-1], s2))
    return L[m][n]

if __name__ == '__main__':
    s1 = 'ACADB'
    s2 = 'CBDA'
    m = len(s1)
    n = len(s2)
    L = [[-1 for j in range(n+1)] for i in range(m+1)]
    print(lcs_memoization(s1, s2))

    s1 = 'QPQRR'
    s2 = 'PQPRQRP'
    m = len(s1)
    n = len(s2)
    L = [[-1 for j in range(n+1)] for i in range(m+1)]
    print(lcs_memoization(s1, s2))
