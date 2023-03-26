class Infix2Postfix:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return -1
        else:
            self.top -= 1
            return self.stack.pop()

    def priority(self, c):
        if c == '(':
            return 0
        if (c == '+') or (c == '-'):
            return 1
        if (c == '*') or (c == '/'):
            return 2

    def infix_to_postfix(self, expr):
        p = ''
        for i in range(len(expr)):
            if expr[i] == '(':
                self.push(expr[i])
            elif expr[i].isalnum():
                p += expr[i]
            elif expr[i] == ')':
                x = self.pop()
                while x != '(':
                    p += x
                    x = self.pop()
            else:
                while (self.top != -1) and (self.priority(self.stack[self.top]) >= self.priority(expr[i])):
                    p += self.pop()
                self.push(expr[i])
        while self.top != -1:
            p += self.pop()
        print(p)


i2p = Infix2Postfix()
expr = input('Enter the expression: ')
i2p.infix_to_postfix(expr)
