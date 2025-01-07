# 리스트로 구현하는 방식
n, k = map(int, input().split())
people = [x for x in range(1, n+1)]

josephus_order = []

idx = 0

while people:
    idx = (idx + k - 1) % len(people)
    josephus_order.append(people.pop(idx))

print("<" + ", ".join(map(str, josephus_order)) + ">")



# 원형 큐로 구현하는 방식
# from collections import deque
# n, k = map(int, input().split())
# queue = deque(range(1, n+1))
#
# josephus_order = []
#
# while queue:
#     queue.rotate(-(k-1))
#     josephus_order.append(queue.popleft())
# print("<" + ", ".join(map(str, josephus_order)) + ">")
