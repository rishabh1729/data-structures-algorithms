# Longest Common Subsequence
# Bottom-up dynamic programming (Tabulation)

def lcs_tabulation(s1, s2):
    m = len(s1)
    n = len(s2)
    L = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    return L[m][n]

s1 = 'ACADB'
s2 = 'CBDA'
print(lcs_tabulation(s1, s2))

s1 = 'QPQRR'
s2 = 'PQPRQRP'
print(lcs_tabulation(s1, s2))    
