class Node:
    def __init__(self, data):
        self.data = data
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

    def max_depth(self, root):
        if root == None:
            return 0
        lst_depth = self.max_depth(root.left)
        rst_depth = self.max_depth(root.right)
        return 1 + max(lst_depth, rst_depth)

    def max_depth_iterative(self, root):
        if root == None:
            return 0
        stack = []
        stack.append((1, root))
        depth = 0
        while stack:
            current_depth, current = stack.pop()
            depth = max(depth, current_depth)
            if current.left:
                stack.append((current_depth + 1, current.left))
            if current.right:
                stack.append((current_depth + 1, current.right))
        return depth

root = None
b = BST()
for el in [2, 1, 33, 0, 25, 40, 11, 34, 7, 12, 36, 13]:
    root = b.build_BST(root, el)
print('Maximum Depth of Binary Tree:', b.max_depth_iterative(root))
