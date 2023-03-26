class Node:
    def __init__(self, info, next = None):
        self.info = info
        self.next = next

class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enQueue(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.head
            return
        self.tail.next = newNode
        self.tail = self.tail.next
        self.tail.next = self.head

    def deQueue(self):
        if self.head == None:
            return -1
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return temp.info

    def display(self):
        if self.head == None:
            print('Empty Queue')
            return
        current = self.head
        while current.next != self.head:
            print(current.info)
            current = current.next
        print(current.info)


cq = CircularQueue()
cq.enQueue(10)
cq.enQueue(20)
cq.enQueue(30)
cq.display()
print('****')
x = cq.deQueue()
if x == -1:
    print('Empty Queue')
else:
    print('Removed Element:', x)
cq.display()
