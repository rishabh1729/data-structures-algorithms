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

    def insert_at_end(self, info):
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newNode
        else:
            self.head = newNode

    def insert_at_position(self, pos, info):
        if pos == 0:
            self.insert_at_beginning(info)
            return
        if self.head != None:
            newNode = Node(info)
            ind = 0
            current = self.head
            while ind < (pos-1):
                if current.link != None:
                    current = current.link
                    ind += 1
                    continue
                print('Index out of range')
                return
            newNode.link = current.link
            current.link = newNode
        else:
            print('Index out of range')


    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link

ll = LinkedList()
ll.insert_at_position(1, 1000)
ll.insert_at_beginning(5)
ll.insert_at_beginning(10)
ll.insert_at_end(15)
ll.insert_at_end(20)
ll.display()
print('****')
ll.insert_at_position(0, 25)
ll.display()
print('****')
ll.insert_at_position(3, 100)
ll.display()
print('****')
ll.insert_at_position(6, 200)
ll.display()
print('****')
ll.insert_at_position(8, 300)
ll.display()
