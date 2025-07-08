import sys
n = int(sys.stdin.readline())
num_list = [[0, 0] for i in range(n)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num_list[i][0] = a
    num_list[i][1] = b

num_list.sort(key = lambda x:(x[1], x[0]))

for i in range(len(num_list)):
    print(num_list[i][0], num_list[i][1])
