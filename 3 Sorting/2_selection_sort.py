def selection_sort(arr):
    for i in range(len(arr)-1):
        imin = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[imin]:
                imin = j
        if imin != i:
            arr[i], arr[imin] = arr[imin], arr[i]


arr = [1, 5, 3, 6, 3]
selection_sort(arr)
print(arr)
