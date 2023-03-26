def merge_sort(arr, p, r):
    if p<r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0]*(n1 + 1)
    right = [0]*(n2 + 1)
    for i in range(n1):
        left[i] = arr[p+i]
    for j in range(n2):
        right[j] = arr[q+j+1]
    left[n1] = max(arr) + 1
    right[n2] = max(arr) + 1
    i, j = 0, 0
    for k in range(p, r+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1


arr = [1, 5, 3, 6, 3]
merge_sort(arr, 0, len(arr)-1)
print(arr)
