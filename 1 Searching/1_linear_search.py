def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return 'Element {} found at index {}'.format(x, i)
    return 'Element {} not found'.format(x)

if __name__ == '__main__':
    arr = [4, 6, 2, 3, 8, 21]
    x = 6
    print(linear_search(arr, x))
    x = 7
    print(linear_search(arr, x))
