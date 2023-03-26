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

    def leaf_nodes(self, root):
        if root == None:
            return 0
        if not root.left and not root.right:
            return 1
        return self.leaf_nodes(root.left) + self.leaf_nodes(root.right)

    def leaf_nodes_iterative(self, root):
        if root == None:
            return 0
        stack = []
        stack.append(root)
        count = 0
        while stack:
            current = stack.pop()
            if not current.left and not current.right:
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
print('No. of Leaf Nodes:', b.leaf_nodes_iterative(root))
