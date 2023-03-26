# 0/1 Knapsack : Bottom-up dynamic programming (Tabulation)

def knapsack(wt, val, W):
    n = len(wt)
    K = [[-1 for w in range(W+1)] for i in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] > w:
                K[i][w] = K[i-1][w]
            else:
                K[i][w] = max(K[i-1][w], K[i-1][w-wt[i-1]] + val[i-1])
    return K[n][W]

wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
print(knapsack(wt, val, W))
