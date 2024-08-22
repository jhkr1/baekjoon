class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception('Stack is Empty')
        return self.items.pop()
    
    def top(self):
        if self.empty():
            raise Exception("Stack is Empty")
        return self.items[-1]

stack = Stack()
words = input().strip()
is_balanced = True

for char in words:
    if char == '(':
        stack.push(char)
    elif char == ')':
        if stack.empty():
            is_balanced = False
            break
        stack.pop()

if stack.empty() and is_balanced:
    print('Yes')
else:
    print('No')

    
