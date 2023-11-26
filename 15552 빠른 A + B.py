import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.
# 문자열의 오른쪽에 있는 개행 문자(\n)를 제거하기 위해 .rstrip()을 추가합니다.
# 입력은 공백으로 구분되어 있으므로 split()을 사용하여 나눕니다.
t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    # a와 b를 더한 결과를 출력합니다.
    print(a + b)