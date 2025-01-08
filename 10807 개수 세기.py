import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
v = int(input())
cnt = 0
for i in range(len(numbers)):
    if numbers[i] == v:
        cnt += 1
print(cnt)
