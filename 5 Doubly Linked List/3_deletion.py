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

    def delete_node(self, item):
        if self.head == None:
            print('Empty List')
            return
        # If only 1 node is present
        if self.head.next == None:
            if self.head.info == item:
                temp = self.head
                self.head = None
                temp = None
                return
            print('Item {} not found'.format(item))
            return
        # Deleting First Node
        if self.head.info == item:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None
            return
        # Deleting node in between
        temp = self.head.next
        while temp.next != None:
            if temp.info == item:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
                return
            temp = temp.next
        # Deleting Last Node
        if temp.info == item:
            temp.prev.next = None
            temp = None
            return
        print('Item {} not found'.format(item))

    def display(self):
        if self.head == None:
            print('Empty List')
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.next


ll = LinkedList()
ll.delete_node(10)
print('****')
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
ll.display()
print('****')
ll.delete_node(10)
ll.display()
print('****')
ll.delete_node(10)
ll.display()
print('****')
ll.delete_node(30)
ll.display()
print('****')
ll.delete_node(20)
ll.display()
print('****')
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
ll.display()
print('****')
ll.delete_node(20)
ll.display()
