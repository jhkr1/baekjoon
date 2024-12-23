from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.dq.popleft()
    def front(self):
        if self.empty():
            return -1
        else:
            return self.dq[0]
    def back(self):
        if self.empty():
            return -1
        else:
            return self.dq[-1]
    

que = Queue()

num = int(input())

result = []

for i in range(num):
    command = input().split()
    if command[0] == 'push':
        n = int(command[1])
        que.push(n)
    elif command[0] == 'pop':
        result.append(que.pop())
    elif command[0] == 'front':
        result.append(que.front())
    elif command[0] == 'back':
        result.append(que.back())
    elif command[0] == 'size':
        result.append(que.size())
    elif command[0] == 'empty':
        if(que.empty()):
            result.append(1)
        else:
            result.append(0)

    else:
        print('not a command')


for i in range(len(result)):
    print(result[i])