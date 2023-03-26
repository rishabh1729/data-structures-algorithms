# 0/1 Knapsack : Top-down approach (Memoization)

def knapsack(wt, val, n, W):
    if K[n][W] == -1:
        if n == 0 or W == 0:
            K[n][W] = 0
        elif wt[n-1] > W:
            K[n][W] = knapsack(wt, val, n-1, W)
        else:
            K[n][W] = max(knapsack(wt, val, n-1, W), knapsack(wt, val, n-1, W-wt[n-1]) + val[n-1])
    return K[n][W]

if __name__ == '__main__':
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]
    n = len(wt)
    W = 7
    K = [[-1 for w in range(W+1)] for i in range(n+1)]
    print(knapsack(wt, val, n, W))
