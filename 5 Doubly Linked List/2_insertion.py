class Node:
    def __init__(self, info, prev = None, next = None):
        self.info = info
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insert_at_end(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        current = self.head
        while current.next != None:
            current = current.next
        newNode.prev = current
        current.next = newNode

    def insert_after_given_node(self, val, item):        #Insert val after a node whose info is item
        if self.head == None:
            print('Empty List')
            return
        current = self.head
        while current != None:
            if current.info == item:
                newNode = Node(val)
                newNode.prev = current
                newNode.next = current.next
                if current.next != None:
                    current.next.prev = newNode
                current.next = newNode
                return
            current = current.next
        print('Item {} not present in the list'.format(item))

    def display(self):
        if self.head == None:
            print('Empty List')
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.next


ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.display()
print('****')
ll.insert_at_end(20)
ll.display()
print('****')
ll.insert_after_given_node(15, 10)
ll.display()
print('****')
ll.insert_after_given_node(25, 20)
ll.display()
print('****')
ll.insert_after_given_node(35, 30)
