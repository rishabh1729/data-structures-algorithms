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

    def delete_node(self, val):
        if self.head == None:
            print('Empty List')
            return
        if self.head.info == val:
            temp = self.head
            self.head = temp.link
            temp = None
            return
        current = self.head
        while current.link != None:
            if current.link.info == val:
                temp = current.link
                current.link = temp.link
                temp = None
                return
            current = current.link
        print('Element Not Found')

    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link


ll = LinkedList()
ll.delete_node(7)
print('****')
ll.insert_at_beginning(100)
ll.insert_at_beginning(200)
ll.insert_at_beginning(300)
ll.display()
print('****')
ll.delete_node(300)
ll.display()
print('****')
ll.delete_node(100)
ll.display()
print('****')
ll.delete_node(300)
print('****')
ll.display()
