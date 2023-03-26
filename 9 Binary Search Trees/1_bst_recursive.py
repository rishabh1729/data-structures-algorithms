class Node:
    def __init__(self, data):
        self.data = info
        self.left = None
        self.right = None

class BST:
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
        while current.left != None:
            current = current.left
        return current.data

    def maximum(self, root):
        if root == None:
            return 'Empty BST'
        current = root
        while current.right != None:
            current = current.right
        return current.data

    def successor(self, root):
        current = root.right
        while current.left != None:
            current = current.left
        return current.data

    def predecessor(self, root):
        current = root.left
        while current.right != None:
            current = current.right
        return current.data

    def delete_node(self, root, key):
        if root == None:
            return None
        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if (not root.left) and (not root.right):
                root = None
            elif root.right != None:
                root.data = self.successor(root)
                root.right = self.delete_node(root.right, root.data)
            else:
                root.data = self.predecessor(root)
                root.left = self.delete_node(root.left, root.data)
        return root


b = BST()
root = None
for el in [10, 5, 25, 2, 7, 30]:
    root = b.build_BST(root, el)
#b.inorder(root)
if b.search(root, 35):
    print('Element Found')
else:
    print('Element Not Found')
print('Minimum value in BST:', b.minimum(root))
print('Maximum value in BST:', b.maximum(root))
root = b.delete_node(root, 5)
b.inorder(root)
