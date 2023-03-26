class Node:
    def __init__(self, info, next = None):
            self.info = info
            self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enQueue(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def deQueue(self):
        if self.head == None:
            return -1
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
        return temp.info

    def display(self):
        if self.head == None:
            print('Empty Queue')
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.next


q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.display()
print('****')
x = q.deQueue()
if x == -1:
    print('Empty Queue')
else:
    print('Removed Element:', x)
q.display()
