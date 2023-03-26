class Heap:

    def max_heapify(self, arr, n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.max_heapify(arr, n, largest)

    def build_max_heap(self, arr, n):
        for i in range(n//2, -1, -1):
            self.max_heapify(arr, n, i)

    def heap_sort(self, arr):
        n = len(arr)
        self.build_max_heap(arr, n)
        while n != 0:
            arr[0], arr[n-1] = arr[n-1], arr[0]
            n = n - 1
            self.max_heapify(arr, n, 0)


h = Heap()
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
h.heap_sort(arr)
print(arr)
