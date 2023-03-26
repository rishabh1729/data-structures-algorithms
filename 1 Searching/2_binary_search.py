def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r)//2
        if x == arr[m]:
            return 'Element {} found at index {}'.format(x, m)
        if x < arr[m]:
            r = m - 1
        if x > arr[m]:
            l = m + 1
    return 'Element {} not found'.format(x)

def binary_search_recursive(arr, x, l, r):
    if l > r:
        return 'Element {} not found'.format(x)
    m = (l + r)//2
    if x == arr[m]:
        return 'Element {} found at index {}'.format(x, m)
    if x < arr[m]:
        return binary_search_recursive(arr, x, l, m-1)
    if x > arr[m]:
        return binary_search_recursive(arr, x, m+1, r)


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 8, 10, 12, 14, 16, 19]
    x = 6
    print(binary_search(arr, x))
    print(binary_search_recursive(arr, x, 0, len(arr)-1))
    x = 7
    print(binary_search(arr, x))
    print(binary_search_recursive(arr, x, 0, len(arr)-1))
