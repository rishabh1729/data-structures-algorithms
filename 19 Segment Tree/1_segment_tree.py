# Range Sum Query

from math import ceil, log2


def constructSegmentTree(arr, sTree, position, start, end):
    if start == end:
        sTree[position] = arr[start]
    else:
        mid = (start + end) // 2
        constructSegmentTree(arr, sTree, 2 * position + 1, start, mid)
        constructSegmentTree(arr, sTree, 2 * position + 2, mid + 1, end)
        sTree[position] = sTree[2 * position + 1] + sTree[2 * position + 2]

def rangeSumQuery(arr, L, R):
    n = len(arr)
    sTree = [0] * (2 ** (ceil(log2(n)) + 1) - 1)
    constructSegmentTree(arr, sTree, 0, 0, n - 1)
    return rangeSum(arr, L, R, sTree, 0, 0, n - 1)

def rangeSum(arr, L, R, sTree, position, start, end):
    if start > R or end < L:
        return 0
    if start >= L and end <= R:
        return sTree[position]
    mid = (start + end) // 2
    return rangeSum(arr, L, R, sTree, 2 * position + 1, start, mid) + \
        rangeSum(arr, L, R, sTree, 2 * position + 2, mid + 1, end)


arr = [2, 3, 1, 9, 4, 3, 7, 8]
L = 2
R= 6
result = rangeSumQuery(arr, L, R)
print(result)