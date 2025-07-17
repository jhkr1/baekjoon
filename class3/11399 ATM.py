import sys
n = int(sys.stdin.readline())
time_list = list(map(int, sys.stdin.readline().split()))


# 1  = 1
# 1 + 2  = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 3 = 9
# 1 + 2 + 3 + 3 + 4 = 13

# 32분
result = 0
# 정렬
time_list.sort()
for i in range(n):
    for j in range(i+1):
        result += time_list[j]
print(result)