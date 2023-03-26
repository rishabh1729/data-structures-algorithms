class PriorityQueue:

    def __init__(self, arr):
        self.pq = arr
        self.length = len(arr)
        self.build_max_heap(self.pq, self.length)

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

    def maximum(self):
        return self.pq[0]

    def extract_max(self):
        x = self.pq[0]
        self.pq[0], self.pq[self.length - 1] = self.pq[self.length - 1], self.pq[0]
        self.length -= 1
        self.max_heapify(self.pq, self.length, 0)
        return x

    def insert(self, x):
        if len(self.pq) == self.length:
            self.pq.append(x)
        else:
            self.pq[self.length] = x
        self.length += 1
        index = self.length - 1
        parent = index
        while index > 0:
            if index % 2 == 0:
                parent = index//2 - 1
            else:
                parent = index//2
            if self.pq[index] > self.pq[parent]:
                self.pq[index], self.pq[parent] = self.pq[parent], self.pq[index]
                index = parent
            else:
                break

    def increase_key(self, x, k):
        try:
            index = self.pq.index(x)
            if index >= self.length:
                raise ValueError
            self.pq[index] = k
            parent = index
            while index > 0:
                if index % 2 == 0:
                    parent = index//2 - 1
                else:
                    parent = index//2
                if self.pq[index] > self.pq[parent]:
                    self.pq[index], self.pq[parent] = self.pq[parent], self.pq[index]
                    index = parent
                else:
                    break
        except:
            print('{} is not in list'.format(x))


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
prq = PriorityQueue(arr)
print(prq.pq[:prq.length])
res = prq.maximum()
print('Maximum:', res)
print('****')
res = prq.extract_max()
print(prq.pq[:prq.length])
print('Maximum:', res)
print('****')
prq.increase_key(16, 18)
print('****')
prq.insert(res)
print(prq.pq[:prq.length])
print('****')
prq.increase_key(12, 18)
print('****')
prq.increase_key(14, 18)
print(prq.pq[:prq.length])
