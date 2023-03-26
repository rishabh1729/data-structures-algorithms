class Parenthesis:
    def __init__(self):
        self.stack = []
        self.top = -1

    def check(self, expr):
        ob = ['(', '{', '[']
        cb = [')', '}', ']']
        for i in range(len(expr)):
            if (expr[i] not in ob) and (expr[i] not in cb):
                continue
            if expr[i] in ob:
                self.stack.append(expr[i])
                self.top += 1
                continue
            if self.top != -1:
                if expr[i] == ')':
                    c = self.stack.pop()
                    if c == '(':
                        self.top -= 1
                        continue
                    else:
                        return False, expr[i], i
                if expr[i] == '}':
                    c = self.stack.pop()
                    if c == '{':
                        self.top -= 1
                        continue
                    else:
                        return False, expr[i], i
                if expr[i] == ']':
                    c = self.stack.pop()
                    if c == '[':
                        self.top -= 1
                        continue
                    else:
                        return False, expr[i], i
            else:
                return False, expr[i], i
        if self.top != -1:
            return False, self.stack[-1], expr.index(self.stack[-1])
        else:
            return True, None, None


p = Parenthesis()
expr = input('Enter the expression: ')
balance, c, pos = p.check(expr)
if balance:
    print('Input expression is balanced')
else:
    print('Input expression is not balance at {} index and at {} character'.format(pos, c))
