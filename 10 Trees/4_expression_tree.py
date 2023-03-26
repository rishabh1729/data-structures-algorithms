class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ExpressionTree:

    def priority(self, c):
        if c == '(':
            return 0
        if c == '+' or c == '-':
            return 1
        if c == '*' or c == '/':
            return 2

    def infix2postfix(self, expr):
        po = ''
        stack = []
        for c in expr:
            if c == '(':
                stack.append(c)
            elif c.isalnum():
                po += c
            elif c == ')':
                x = stack.pop()
                while x != '(':
                    po += x
                    x = stack.pop()
            else:
                while stack and (self.priority(stack[-1]) >= self.priority(c)):
                    po += stack.pop()
                stack.append(c)
        while stack:
            po += stack.pop()
        return po

    def postfix2expressionTree(self, po):
        stack = []
        for c in po:
            if c.isalnum():
                stack.append(Node(c))
            else:
                b = stack.pop()
                a = stack.pop()
                root = Node(c)
                root.left = a
                root.right = b
                stack.append(root)
        return stack.pop()

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def evaluate(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return int(root.data)
        lst = self.evaluate(root.left)
        rst = self.evaluate(root.right)
        if root.data == '+':
            return lst + rst
        elif root.data == '-':
            return lst - rst
        elif root.data == '*':
            return lst * rst
        elif root.data == '/':
            return lst / rst


et = ExpressionTree()
expr = '(2+3)*(4*(5+6))'
po = et.infix2postfix(expr)
print(expr)
root = et.postfix2expressionTree(po)
et.inorder(root)
result = et.evaluate(root)
print('Solution:', result)
