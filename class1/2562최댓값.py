n = 9
max_list = []
result = 0
for i in range(n):
    num = int(input())
    max_list.append(num)

print(max(max_list))

for i in range(len(max_list)):
    if(max_list[i] == max(max_list)):
        result = i+1

print(result)