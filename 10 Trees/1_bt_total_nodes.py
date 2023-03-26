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

    def count_nodes(self, root):
        if root == None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def count_nodes_iterative(self, root):
        if root == None:
            return 0
        stack = []
        stack.append(root)
        count = 0
        while stack:
            current = stack.pop()
            count += 1
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return count

root = None
b = BST()
for el in [2, 1, 33, 0, 25, 40, 11, 34, 7, 12, 36, 13]:
    root = b.build_BST(root, el)
print('Total Nodes:', b.count_nodes_iterative(root))
