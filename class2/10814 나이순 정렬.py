import sys

n = int(sys.stdin.readline())
name_age_list = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    name_age_list.append((int(age), name))


name_age_list.sort(key= lambda x:x[0])
# 문제점 -> 나이가 같다면, 가입한 순서대로


for i in range(n):
    print(name_age_list[i][0], name_age_list[i][1])