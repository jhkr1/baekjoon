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

n, k = map(int, input().split())

q = Queue()

for i in range(1, n+1):
    q.push(i)

while q.size() > 1:
    for _ in range(k-1):
        q.push(q.front())
        q.pop()
    print(q.front(), end = ' ')
    q.pop()

print(q.front(), end= ' ')

