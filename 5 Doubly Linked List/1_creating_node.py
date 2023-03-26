class Node:
    def __init__(self, info, prev = None, next = None):
        self.info = info
        self.prev = prev
        self.next = next

first = Node(10)
print(first.info)
