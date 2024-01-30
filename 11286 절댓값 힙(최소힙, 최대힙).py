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

# 최소힙은 가장 작은 값을 루트로(음수일 경우 절댓값이 가장 큰 값이 루트로)
# 최대힙은 가장 큰 값을 루트로 (음수일 경우 절댓값이 가장 작은 값이 루트로)

import sys
import heapq as hq

min_heap = []
max_heap = []
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())
    if x: # x가 0이 아닐 경우
        hq.heappush(min_heap, x) if (x > 0) else hq.heappush(max_heap, -x) # 양수일 경우에는 최소힙에, 음수일 경우에 최대힙에
        # why? 최소힙은 가장 작은 값을 루트로 보내기 때문에 양수 중 가장 작은 값이 루트로 온다. 최대힙은 가장 큰 값이 루트로 오기 때문에 절댓값이 가장 작은 음수가 루트로 온다.
    else: # x가 0인 경우
        if min_heap: # 최소힙이 존재하고
            if max_heap: # 최대힙이 존재하는 경우
                if min_heap[0] >= max_heap[0]: # 최소힙과 최대힙의 루트를 비교하여, 더 작은 값 출력
                    print(-hq.heappop(max_heap))
                else:
                    print(hq.heappop(min_heap))
            else: # 최대힙이 존재하지 않는 경우
                print(hq.heappop(min_heap))
        else: # 최소힙이 존재하지 않고
            if max_heap: # 최대힙이 존재하는 경우
                print(-hq.heappop(max_heap))
            else: # 최대힙이 존재하지 않는 경우
                print(0)



