fixed_num = 42
repeat_num = 10
rest_set = set()
result = 0


for i in range(repeat_num):
    a = int(input())
    rest_set.add(a % fixed_num)


for i in rest_set:
    result += 1

print(result)
