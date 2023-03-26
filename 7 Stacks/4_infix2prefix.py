class Infix2Prefix:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.stack.pop()
        else:
            return '$'

    def peek(self):
        if self.top != -1:
            return self.stack[-1]
        else:
            return '$'

    def priority(self, c):
        if c == '(':
            return 0
        if (c == '+') or (c == '-'):
            return 1
        if (c == '*') or (c == '/'):
            return 2
        if c == '^':
            return 3
        if c == '$':
            return -1

    def infix_to_postfix(self, expr):
        po = ''
        for c in expr:
            if c == '(':
                self.push(c)
            elif c.isalnum():
                po += c
            elif c == ')':
                x = self.pop()
                while x != '(':
                    po += x
                    x = self.pop()
            else:
                while (self.top != -1) and (self.priority(self.peek()) >= self.priority(c)):
                    po += self.pop()
                self.push(c)
        while self.top != -1:
            po += self.pop()
        return po

    def infix_to_prefix(self, expr):
        pre = ''
        rev_expr = ''
        for i in range(len(expr)-1, -1, -1):
            if expr[i] == '(':
                rev_expr += ')'
            elif expr[i] == ')':
                rev_expr += '('
            else:
                rev_expr += expr[i]
        po = self.infix_to_postfix(rev_expr)
        pre = po[::-1]
        return pre


i2pr = Infix2Prefix()
expr = input('Enter the expression: ')
print(i2pr.infix_to_prefix(expr))
