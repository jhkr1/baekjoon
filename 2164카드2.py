# 큐를 이용하는 것 같다 why? 1번 카드가 제일 위에 즉, 1번부터 아래로 push()
# 제일 위에 있는 카드를 바닥에 버린다 -> pop()
# 그 다음, 제일 위에 있는 카드를 제일 아래 있는 카드 밑으로 옮긴다. pop() 한 걸 다시 push()
# 예시 1234 -> 234 -> 342 -> 42 -> 24 -> 4
# 123456 -> 23456 -> 34562 -> 4562 -> 5624 -> 624 -> 246 -> 46 -> 64 -> 4
from collections import deque

que = deque()
for i in range(int(input())):
    que.append(i+1)

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que.popleft())

    
