class PostfixEvaluation:
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

    def postfix_eval(self, po):
        self.stack = []
        self.top = -1
        for c in po:
            if c <= '9' and c >= '0':
                self.push(int(c))
            else:
                res = 0
                b = self.pop()
                a = self.pop()
                if c == '+':
                    res = a+b
                elif c == '-':
                    res = a-b
                elif c == '*':
                    res = a*b
                elif c == '/':
                    res = a/b
                elif c == '^':
                    res = a**b
                self.push(res)
        return self.pop()


po_eval = PostfixEvaluation()
expr = input('Enter the expression: ')
po = po_eval.infix_to_postfix(expr)
print('Postfix Expression:', po)
soln = po_eval.postfix_eval(po)
print('Solution:', soln)
