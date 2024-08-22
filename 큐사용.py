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
            raise Exception("Queue is Empty")

        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception("Queue is Empty")
        
        return self.dq[0]

queue = Queue()
n = int(input())

for i in range(n):
    command = input().split()

    if (command[0] == 'push'):
        val = command[1]
        queue.push(val)
    
    elif command[0] == 'pop':
        print(queue.pop())
    
    elif command[0] == 'size':
        print(queue.size())
    
    elif command[0] == 'empty':
        if (queue.empty()):
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        print(queue.front())
    


