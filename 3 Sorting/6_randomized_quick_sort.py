# Works well even when the input array is already sorted
import random

def randomized_quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        randomized_quick_sort(arr, p, q-1)
        randomized_quick_sort(arr, q+1, r)

def partition(arr, p, r):
    m = random.randint(p, r)
    arr[p], arr[m] = arr[m], arr[p]
    x = arr[p]
    i = p
    for j in range(p+1, r+1):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i


arr = [1, 5, 3, 6, 3]
randomized_quick_sort(arr, 0, len(arr)-1)
print(arr)
