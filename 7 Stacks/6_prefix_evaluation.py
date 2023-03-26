class PrefixEvaluation:
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
        rev_expr = ''
        for i in range(len(expr)-1, -1, -1):
            if expr[i] == '(':
                rev_expr += ')'
            elif expr[i] == ')':
                rev_expr += '('
            else:
                rev_expr += expr[i]
        po = self.infix_to_postfix(rev_expr)
        pr = po[::-1]
        return pr

    def prefix_evaluation(self, pr):
        self.stack = []
        self.top = -1
        for i in range(len(pr)-1, -1, -1):
            if pr[i].isdigit():
                self.push(pr[i])
            else:
                a = self.pop()
                b = self.pop()
                res = eval(a + pr[i] + b)
                self.push(str(res))
        return int(self.pop())


pr_eval = PrefixEvaluation()
expr = input('Enter the expression: ')
pr = pr_eval.infix_to_prefix(expr)
print('Prefix Expression:', pr)
soln = pr_eval.prefix_evaluation(pr)
print('Solution:', soln)
