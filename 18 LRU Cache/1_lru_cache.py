class DLLNode:
    def __init__(self) -> None:
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.cache = {}
        self.capacity = capacity
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache.get(key)
        if node:
            self.__move_to_head(node)
            return node.value
        return -1

    def __move_to_head(self, node):
        self.__delete_node(node)
        self.__add_node(node)

    def __delete_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def __add_node(self, node):
        next = self.head.next
        node.next = next
        next.prev = node
        self.head.next = node
        node.prev = self.head

    def put(self, key, value):
        node = self.cache.get(key)
        if not node:
            node = DLLNode()
            node.key = key
            node.value = value
            if len(self.cache) < self.capacity:
                self.cache[key] = node
                self.__add_node(node)
            else:
                tail = self.__delete_tail_node()
                del self.cache[tail.key]
                self.__add_node(node)
                self.cache[key] = node
        else:
            node.value = value
            self.__move_to_head(node)

    def __delete_tail_node(self):
        node = self.tail.prev
        self.__delete_node(node)
        return node

cache = LRUCache(2)

cache.put(1, 1)

cache.put(2, 2)

print(cache.get(1))  # returns 1

cache.put(3, 3)  # evicts key 2

print(cache.get(2))  # returns -1 (not found)

cache.put(4, 4)  # evicts key 1

print(cache.get(1))  # returns -1 (not found)

print(cache.get(3))  # returns 3

print(cache.get(4))  # returns 4