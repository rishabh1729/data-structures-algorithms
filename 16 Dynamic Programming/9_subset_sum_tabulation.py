# Subset-sum problem : Bottom-up DP (Tabulation)
# Input: arr = [3, 34, 4, 12, 5, 2], SUM = 9
# Output: True, if there exists subset of items in 'arr' whose summation = SUM, otherwise False

def subset_sum(arr, SUM):
    n = len(arr)
    S = [[-1 for sum in range(SUM+1)] for i in range(n+1)]
    for i in range(n+1):
        for sum in range(SUM+1):
            if i == 0 and sum > 0:
                S[i][sum] = False
            elif sum == 0:
                S[i][sum] = True
            elif arr[i-1] > sum:
                S[i][sum] = S[i-1][sum]
            else:
                S[i][sum] = S[i-1][sum] or S[i-1][sum - arr[i-1]]
    return S[n][SUM]

arr = [3, 34, 4, 12, 5, 2]
SUM = 9
print(subset_sum(arr, SUM))
