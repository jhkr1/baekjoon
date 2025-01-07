class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()
k = int(input())
result = 0
for i in range(k):
    n = int(input())
    if (n != 0):
        stack.push(n)
    else:
        stack.pop()

for i in range(stack.size()):
    result += stack.pop()

print(result)
