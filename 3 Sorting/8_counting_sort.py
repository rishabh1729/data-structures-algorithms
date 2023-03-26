def counting_sort(arr):
    n = len(arr)
    k = max(arr)
    result = [0]*n
    aux = [0]*(k+1)                   # Auxiliary array which stores the count
    for i in range(n):
        aux[arr[i]] += 1
    # aux[i] now contains the no. of elements equal to 'i'
    for i in range(1, k+1):
        aux[i] += aux[i-1]
    # aux[i] now contains the no. of elements less than or equal to 'i'
    for i in range(n-1, -1, -1):      # This loop is run in reverse order to make counting sort, a stable sort
        result[aux[arr[i]]-1] = arr[i]
        aux[arr[i]] -= 1
    for i in range(n):                # Filling the input array 'arr' with the sorted array 'result'
        arr[i] = result[i]


arr = [1, 5, 3, 1, 3, 2, 3]
print(arr)
counting_sort(arr)
print(arr)
