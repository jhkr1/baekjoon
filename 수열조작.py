from collections import deque

dq = deque()

n = int(input())


for i in range(1, n+1):
    dq.append(i)

while len(dq) > 2:
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

print(dq.pop())




