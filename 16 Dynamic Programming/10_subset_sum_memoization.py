# Subset-sum problem : Top-down DP (Memoization)
# Input: arr = [3, 34, 4, 12, 5, 2], SUM = 9
# Output: True, if there exists subset of items in 'arr' whose summation = SUM, otherwise False

def subset_sum(arr, n, SUM):
    if S[n][SUM] == -1:
        if n == 0 and SUM > 0:
            S[n][SUM] = False
        elif SUM == 0:
            S[n][SUM] = True
        elif arr[n-1] > SUM:
            S[n][SUM] = subset_sum(arr, n-1, SUM)
        else:
            S[n][SUM] = subset_sum(arr, n-1, SUM) or subset_sum(arr, n-1, SUM - arr[n-1])
    return S[n][SUM]

if __name__ == '__main__':
    arr = [3, 34, 4, 12, 5, 2]
    n = len(arr)
    SUM = 9
    S = [[-1 for sum in range(SUM+1)] for i in range(n+1)]
    print(subset_sum(arr, n, SUM))
