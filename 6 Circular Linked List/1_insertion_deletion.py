class Node:
    def __init__(self, info, link = None):
        self.info = info
        self.link = link

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, info):
        newNode = Node(info)
        if self.head == None:
            self.head = newNode
            self.head.link = self.head
            return
        current = self.head
        while current.link != self.head:
            current = current.link
        current.link = newNode
        newNode.link = self.head
        self.head = newNode

    def insert_at_end(self, info):
        newNode = Node(info)
        if self.head == None:
            self.head = newNode
            self.head.link = self.head
            return
        current = self.head
        while current.link != self.head:
            current = current.link
        current.link = newNode
        newNode.link = self.head

    def delete_node(self, item):
        if self.head == None:
            print('Empty List')
            return
        # If only 1 node in the list
        if self.head.link == self.head:
            if self.head.info == item:
                temp = self.head
                self.head = None
                temp = None
                return
            print('Item {} not present'.format(item))
            return
        # Deleting First Node
        if self.head.info == item:
            current = self.head
            while current.link != self.head:
                current = current.link
            temp = self.head
            current.link = self.head.link
            self.head = self.head.link
            temp = None
            return
        # Delete for other cases
        current = self.head
        while current.link != self.head:
            if current.link.info == item:
                temp = current.link
                current.link = temp.link
                temp = None
                return
            current = current.link
        print('Item {} not present'.format(item))

    def display(self):
        if self.head == None:
            print('Empty List')
            return
        current = self.head
        while current.link != self.head:
            print(current.info)
            current = current.link
        print(current.info)


cll = CircularLinkedList()
cll.delete_node(40)
cll.insert_at_beginning(20)
cll.insert_at_beginning(10)
cll.insert_at_end(30)
cll.insert_at_end(40)
cll.display()
print('****')
cll.delete_node(50)
cll.display()
print('****')
cll.delete_node(40)
cll.display()
print('****')
cll.delete_node(20)
cll.display()
print('****')
cll.delete_node(10)
cll.display()
print('****')
cll.delete_node(20)
cll.display()
print('****')
cll.delete_node(30)
cll.display()
