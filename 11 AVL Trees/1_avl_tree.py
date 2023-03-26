class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def getHeight(self, root):
        if root is None:
            return 0
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        return (self.getHeight(root.left) - self.getHeight(root.right))

    def leftRotate(self, p):
        y = p.right
        temp = y.left
        y.left = p
        p.right = temp
        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, p):
        y = p.left
        temp = y.right
        y.right = p
        p.left = temp
        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def insertion(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insertion(root.left, key)
        else:
            root.right = self.insertion(root.right, key)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance < -1:
            if key > root.right.data:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        if balance > 1:
            if key < root.left.data:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        return root

    def successor(self, p):
        p = p.right
        while p.left:
            p = p.left
        return p.data

    def deletion(self, root, key):
        if root == None:
            return root
        if key < root.data:
            root.left = self.deletion(root.left, key)
        elif key > root.data:
            root.right = self.deletion(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            root.data = self.successor(root)
            root.right = self.deletion(root.right, root.data)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance < -1:
            if root.right.right:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        if balance > 1:
            if root.left.left:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        return root

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)


a = AVL()
root = None
for el in [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]:
    root = a.insertion(root, el)
a.inorder(root)
print('Height of the Tree:', root.height)
print('****')
for el in [2, 3, 10, 18, 4, 9, 14, 7, 15]:
    root = a.deletion(root, el)
    print('Height of the Tree:', root.height)
a.inorder(root)
