def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break

def bubble_sort2(arr):
    i = 0
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        i = i + 1


arr = [1, 5, 3, 6, 3]
bubble_sort(arr)
print(arr)
