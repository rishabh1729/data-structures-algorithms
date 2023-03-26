class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

s = Stack()
while True:
    print('push')
    print('pop')
    print('peek')
    choice = input('Enter your choice: ')
    if choice == 'push':
        item = int(input('Enter the item to push: '))
        s.push(item)
    elif choice == 'pop':
        x = s.pop()
        if x == -1:
            print('Empty Stack')
        else:
            print('Popped Element:', x)
    elif choice == 'peek':
        x = s.peek()
        if x == -1:
            print('Empty Stack')
        else:
            print('Top of the stack:', x)
    else:
        break
