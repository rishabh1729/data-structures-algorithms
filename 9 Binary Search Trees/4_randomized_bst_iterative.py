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
        current = root
        while True:
            if val < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break
        return root

    def inorder(self, root):
        if root == None:
            return
        stack = []
        current = root
        stack.append(root)
        while True:
            if current.left:
                stack.append(current.left)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                if current.right:
                    current = current.right
                    stack.append(current)
            else:
                break

    def preorder(self, root):
        if root == None:
            return
        stack = []
        stack.append(root)
        current = root
        while stack:
            current = stack.pop()
            print(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder(self, root):                     # Using 2 stacks: 'recursion' stack and 'result' stack
        if root == None:
            return
        recursion = []
        result = []
        recursion.append(root)
        current = root
        while recursion:
            current = recursion.pop()
            result.append(current)
            if current.left:
                recursion.append(current.left)
            if current.right:
                recursion.append(current.right)
        while result:
            current = result.pop()
            print(current.data)

    def postorder2(self, root):                    # Using 1 stack
        if root == None:
            return
        stack = []
        prev = None
        stack.append(root)
        while stack:
            current = stack[-1]
            if prev == None or prev.left == current or prev.right == current:
                if current.left:
                    stack.append(current.left)
                elif current.right:
                    stack.append(current.right)
                else:
                    print(current.data)
                    stack.pop()
            elif current.left == prev:
                if current.right:
                    stack.append(current.right)
                else:
                    print(current.data)
                    stack.pop()
            else:
                print(current.data)
                stack.pop()
            prev = current

b = RandomizedBST()
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(l)
root = None
for el in l:
    root = b.build_BST(root, el)
b.postorder2(root)
