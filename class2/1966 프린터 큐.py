from collections import deque 

# 첫 줄에는 테스트 케이스의 수
num = int(input())
# 각 테스트 케이스는 두 줄로 이루어져 있다.
# 문서의 개수 n
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M

for _ in range(num):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = deque([importance[i], i] for i in range(n))
    print_order = 0

    while queue:
        current = queue.popleft()

        if any(current[0] < doc[0] for doc in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[1] == m:
                print(print_order)
                break
    