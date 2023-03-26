def radix_sort(arr):
    largest = max(arr)                            # Largest number decides the no. of digits
    place = 1                                     # Starting with ones place digit (i.e. unit digit)
    while largest//place > 0:
        counting_sort(arr, place)
        place = place * 10

def counting_sort(arr, place):
    n = len(arr)
    result = [0]*n
    aux = [0]*10                                  # Auxiliary array which stores the count
    for i in range(n):
        index = arr[i]//place
        aux[index % 10] += 1
    for i in range(1, 10):
        aux[i] += aux[i-1]
    for i in range(n-1, -1, -1):
        index = arr[i]//place
        result[aux[index % 10] - 1] = arr[i]
        aux[index % 10] -= 1
    for i in range(n):
        arr[i] = result[i]

arr = [121, 432, 564, 23, 1, 45, 788]
print(arr)
radix_sort(arr)
print(arr)
