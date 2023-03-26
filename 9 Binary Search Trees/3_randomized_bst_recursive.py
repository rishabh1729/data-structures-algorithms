from random import shuffle

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class RandomizedBST:
    def build_BST(self, root, val):
        if root == None:
            return Node(val)
        if val < root.data:
            root.left = self.build_BST(root.left, val)
        else:
            root.right = self.build_BST(root.right, val)
        return root

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def preorder(self, root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def search(self, root, key):
        if root == None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def minimum(self, root):
        if root == None:
            return 'Empty BST'
        current = root
        while current.left:
            current = current.left
        return current.data

    def maximum(self, root):
        if root == None:
            return 'Empty BST'
        current = root
        while current.right:
            current = current.right
        return current.data

    def successor(self, root):
        current = root.right
        while current.left:
            current = current.left
        return current.data

    def predecessor(self, root):
        current = root.left
        while current.right:
            current = current.right
        return current.data

    def delete_node(self, root, val):
        if root == None:
            return None
        if val < root.data:
            root.left = self.delete_node(root.left, val)
        if val > root.data:
            root.right = self.delete_node(root.right, val)
        else:
            if (not root.left) and (not root.right):
                root = None
            elif root.right:
                root.data = self.successor(root)
                root.right = self.delete_node(root.right, root.data)
            else:
                root.data = self.successor(root)
                root.left = self.delete_node(root.left, root.data)
        return root


b = RandomizedBST()
root = None
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(l)
for el in l:
    root = b.build_BST(root, el)
b.inorder(root)
print('****')
b.preorder(root)
print('****')
b.postorder(root)
print('****')
if b.search(root, 8):
    print('Element Found')
else:
    print('Element Not Found')
print('Minimum value in BST:', b.minimum(root))
print('Maximum value in BST:', b.maximum(root))
print('****')
root = b.delete_node(root, 8)
b.inorder(root)
