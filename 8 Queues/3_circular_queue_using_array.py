class CircularQueue:
    def __init__(self):
        self.queue = [0]*5
        self.head = -1
        self.tail = -1

    def enQueue(self, val):
        if self.head == -1:
            self.queue[0] = val
            self.head = 0
            self.tail = 0
            return
        if (self.tail - self.head == 4) or (self.head - self.tail == 1):
            print('Queue is Full')
            return
        if self.tail == 4:
            self.tail = 0
        else:
            self.tail += 1
        self.queue[self.tail] = val

    def deQueue(self):
        if self.head == -1:
            return -1
        x = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return x
        if self.head == 4:
            self.head = 0
        else:
            self.head += 1
        return x

    def display(self):
        if self.head == -1:
            print('Empty Queue')
            return
        current = self.head
        while current != self.tail:
            print(self.queue[current])
            if current == 4:
                current = 0
            else:
                current += 1
        print(self.queue[current])


cq = CircularQueue()
cq.enQueue(10)
cq.enQueue(20)
cq.enQueue(30)
cq.enQueue(40)
cq.enQueue(50)
cq.display()
print('****')
cq.enQueue(60)
print('****')
x = cq.deQueue()
if x == -1:
    print('Empty Queue')
else:
    print('Removed Element:', x)
cq.display()
print('****')
cq.enQueue(60)
cq.display()
print('****')
x = cq.deQueue()
if x == -1:
    print('Empty Queue')
else:
    print('Removed Element:', x)
cq.display()
print('****')
cq.enQueue(70)
cq.display()
