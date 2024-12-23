class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        ## 비어있다면 true
        ## 비어있지않다면 false
        return not self.items
    def top(self):
        if self.empty():
            return(-1)
        else:
            return(self.items[-1])

    def pop(self):
        if self.empty():
            return(-1)
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)
    

stack = Stack()

num = int(input())

result = []

for i in range(num):
    command = input().split()
    if command[0] == 'push':
        n = int(command[1])
        stack.push(n)
    elif command[0] == 'pop':
        result.append(stack.pop())
    elif command[0] == 'top':
        result.append(stack.top())
    elif command[0] == 'size':
        result.append(stack.size())
    elif command[0] == 'empty':
        if(stack.empty()):
            result.append(1)
        else:
            result.append(0)
    else:
        print('not a command')


for i in range(len(result)):
    print(result[i])
        



