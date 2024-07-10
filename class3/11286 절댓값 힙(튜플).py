'''
                문제
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러 개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''
# 1. 비어있는 배열 만들기
# 2. 첫째 줄에 연산의 개수(N) 입력 받기
# 3. 다음 N개의 줄에 정수 x가 주어진다.
# 4. 만약 x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 제거
# 5. 만약 x가 0이 아니라면 배열에 x라는 값을 추가하는 연산
# 6. 번째 해야할 것 절댓값으로 변환 그중 가작 작은 것 출력 후 제거
# 7. 번쨰 해야할 것 가장 작은 절댓값이 여러 개일 경우 비교 후 가장 작은 수 출력 후 제거
# 8. 만약 힙이 비어있다면 0 출력

# 문제점 -> 절대값이 적용되지 않음!
# 꺠달은 것 -> 튜플을 활용해보자. 튜플을 이용하여 정렬하면 첫 번째 수 비교 후 두 번째 수 비교
# 절대값은 abs(), 삼항 연산자

import sys
import heapq as hq

# pq = []
# input = sys.stdin.readline
# n = int(input())
# for _ in range(n):
#     x = int(input())
#     if x != 0:
#         hq.heappush(pq, (abs(x), x))
#     else:
#         if pq:
#             print(hq.heappop(pq)[1])
#         else:
#             print(0)


import sys
import heapq as hq
input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)







