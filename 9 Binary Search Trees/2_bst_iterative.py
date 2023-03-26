class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
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
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                break

    def preorder(self, root):
        if root == None:
            return
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            print(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder(self, root):             # Using 2 stacks: 'recursion' stack and 'result' stack
        if root == None:
            return
        recursion = []
        result = []
        recursion.append(root)
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

    def postorder2(self, root):            # Using 1 stack
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
            elif prev == current.left:
                if current.right:
                    stack.append(current.right)
                else:
                    print(current.data)
                    stack.pop()
            else:
                print(current.data)
                stack.pop()
            prev = current


b = BST()
root = None
for el in [10, 5, 25, 2, 7, 30]:
    root = b.build_BST(root, el)
b.postorder2(root)
