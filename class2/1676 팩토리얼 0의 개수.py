import sys

n = int(sys.stdin.readline())
factorial_result = 1
for i in range(n, 1, -1):
    factorial_result *= i

result = 0
# 10으로 계속 나누기 if 10으로 나눈 값의 나머지가 0이 아니라면 그게 정답

while factorial_result % 10 == 0:
    factorial_result = factorial_result // 10
    result += 1

print(result)