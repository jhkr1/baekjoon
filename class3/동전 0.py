import sys
n, k = map(int, sys.stdin.readline().split())
coin_list = [int(sys.stdin.readline()) for _ in range(n)]

result = 0

for i in range(n-1, -1, -1):
    if k >= coin_list[i]:
        result += (k // coin_list[i])
        k %= coin_list[i]

print(result)


