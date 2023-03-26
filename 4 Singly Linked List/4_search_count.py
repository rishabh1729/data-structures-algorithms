class Node:
    def __init__(self, info):
        self.info = info
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, info):
        newNode = Node(info)
        newNode.link = self.head
        self.head = newNode

    def display(self):
        if self.head == None:
            print('Empty List')
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.link

    def search(self, val):
        if self.head == None:
            print('Empty List')
            return
        pos = 1
        current = self.head
        while current != None:
            if current.info == val:
                print('Item {} found at position {}'.format(val, pos))
                return
            pos += 1
            current = current.link
        print('Item {} Not Found'.format(val))

    def count(self):
        c = 0
        current = self.head
        while current != None:
            c += 1
            current = current.link
        print('No. of items in the list: ', c)


ll = LinkedList()
ll.display()
ll.count()
ll.search(10)
print('****')
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.display()
ll.search(30)
ll.search(10)
ll.search(20)
print('****')
ll.display()
ll.count()
