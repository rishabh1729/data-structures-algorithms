# Works well even when the input array is already sorted
# Works well even when all the elements in the input array are same
import random

def quick_sort3(arr, p, r):
    if p < r:
        i, k = partition(arr, p, r)
        quick_sort3(arr, p, i-1)
        quick_sort3(arr, k+1, r)

def partition(arr, p, r):
    m = random.randint(p, r)
    arr[p], arr[m] = arr[m], arr[p]
    x = arr[p]                       # pivot
    i = p                            # index from p to (i-1) contain elements having value less than pivot
    k = p                            # index from i to k contain elements having same value as pivot
    for j in range(p+1, r+1):
        if arr[j] < x:
            i = i + 1
            k = k + 1
            arr[i], arr[j] = arr[j], arr[i]
            if i != k:
                arr[k], arr[j] = arr[j], arr[k]
        elif arr[j] == x:
            k = k + 1
            arr[k], arr[j] = arr[j], arr[k]
    arr[i], arr[p] = arr[p], arr[i]
    return i, k


arr = [1, 5, 3, 6, 3]
quick_sort3(arr, 0, len(arr)-1)
print(arr)
